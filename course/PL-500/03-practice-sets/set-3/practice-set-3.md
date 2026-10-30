# Microsoft Exam PL-500: Practice Exam 3 — Customs Brokerage, Freight Gateways & Custom Actions — Reviewer Study Key

**Theme:** On-Premises Data Gateway, Business vs System exceptions, ms-powerautomate URLs, signed .NET CAB custom actions, and VM session hygiene  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E3Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

A port operations team triggers unattended manifest-filing bots at 02:00 local time on locked Windows Server VMs. Arrange the four unattended lifecycle steps in the exact runtime order.

- **A.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **B.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text
- **C.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically
- **D.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Unattended runs verify clean session state, connect via Machine Group credentials, create a background Windows session to run the flow, and sign out afterward. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **B:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.
- **C:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.
- **D:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.

</details>

### Q002 (`E3Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

A customs operations manager wants to see a single cross-environment or environment-wide dashboard of desktop flow success rates, average run duration, machine utilization, and top error categories. Where in Power Automate portal is this surfaced?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The **Automation Center** and `Monitor -> Desktop flow runs` / `Machines` pages provide end-to-end SLA, queue, machine utilization, and failure analytics. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **C:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.

</details>

### Q003 (`E3Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A bonded warehouse receives arrival notices via REST webhook, validates duty rates in Microsoft Dataverse, and must enter bonded-release codes into a 2004 Windows Forms customs desktop client that offers no API. Which end-to-end design applies?

- **A.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A hybrid RPA architecture pairs a webhook/Dataverse cloud flow orchestrator with an unattended Power Automate for desktop flow driving the legacy WinForms client. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.

</details>

### Q004 (`E3Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

When importing a Managed RPA Solution into UAT for the first time, which component prompts the admin (or reads the deployment settings JSON) to connect `Desktop flows` to `UAT-MachineGroup` and `UAT-BotCredential`?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Solution **Connection References** map the imported flows to target UAT Connections, Machine Groups, and Credentials without modifying flow definitions. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **C:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q005 (`E3Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

During unattended SAP GUI entry, a network hiccup crashes `saplogon.exe`. You want Power Automate for desktop to catch any UI error across the 18 SAP actions, store error details in `%____%` (`%LastError%`), invoke `Restart_SAP`, and resume cleanly. Which container should wrap those 18 actions?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **D.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `On block error` wraps multi-step UI blocks, populates `%LastError%` (`Get last error`), calls a cleanup/restart subflow, and controls block retry or continuation. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **D:** Incorrect — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.

</details>

### Q006 (`E3Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

A freight enterprise is automating Managed Solution releases (`CustomsRPA`) from Dev to UAT and Production using Power Platform pipelines. Select the compliant four-step ALM sequence.

- **A.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **B.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs
- **C.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows
- **D.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Package all RPA artifacts in an Unmanaged Dev Solution, clear Dev values & export Managed, verify target Prod Machine Groups/Credentials, and deploy Managed Upgrade binding stage references. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **B:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.
- **C:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.
- **D:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.

</details>

### Q007 (`E3Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

Which two security configurations align with Microsoft’s least-privilege governance guidance for enterprise RPA environments? Select two.

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **E.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Assign `Desktop Flows Machine Owner` / `Machine User` roles according to duties, own headless cloud flows/pipelines with Service Principals, and use Key Vault-backed Windows service accounts for VM sessions. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **E:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).

</details>

### Q008 (`E3Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

An auditor asks how Power Automate separates operational usage from administrative control across Desktop flows and Machine Groups. Which two sharing rules are accurate? Select two.

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **E.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Both Desktop flows and Machine Groups separate `User` (execute/dispatch) from `Co-owner` (modify/administer/share). [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **E:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q009 (`E3Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

A freight forwarder’s legacy maritime booking terminal uses `VT100` / `IBM 3270` green-screen sessions over Telnet/TLS. Which Power Automate for desktop capability interacts with cursor coordinates and screen fields reliably?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Built-in Terminal emulation actions (`Open terminal session`, `Get text from terminal session`, `Send key`) drive `VT100`/`3270`/`5250` hosts directly. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q010 (`E3Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

A developer tries to create a `Desktop flows` connection in UAT using a Microsoft Entra App Registration (`Client ID` + `Client Secret`) as the **Windows desktop login credential** for an unattended Windows 11 VM, and sign-in fails! Why?

- **A.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **B.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **C.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Windows OS interactive desktop sessions cannot sign in with a headless Entra Service Principal; unattended sessions require an AD / Microsoft Entra ID user account (`DOMAIN\user` or UPN). [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **B:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **C:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q011 (`E3Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

A freight-forwarding cloud flow parses a webhook’s JSON string body into typed fields, filters overdue containers (`DaysAtPort > 5`), and builds a downloadable CSV demurrage report. Which two Data Operation sets handle this? Select two.

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **C.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **E.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). `Parse JSON` provides typed property tokens while `Filter array` + `Create CSV table` produce the CSV demurrage report cleanly. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **C:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **E:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q012 (`E3Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

A developer exported `CustomsRPA` as Managed after testing in Dev, accidentally leaving Dev’s `Current Value` (`https://dev-customs.local`) inside Environment Variable `cus_PortalUrl`. When imported into Production, flows hit `dev-customs.local`! What ALM step prevents this?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Removing `Current Value` from Environment Variables in Dev before export (and supplying Prod’s value via pipeline deployment settings on import) prevents Dev URLs from leaking into Prod. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q013 (`E3Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A freight claims inbox receives unstructured shipper complaint emails in six languages and needs a cloud flow to draft a concise standardized customs summary and extract incident tone using generative AI instructions. Which AI Builder capability fits?

- **A.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **B.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **C.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). AI Builder `Create text with GPT using a prompt` (`AI Prompts`) processes multilingual unstructured text into structured summaries in cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **B:** Correct — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **C:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q014 (`E3Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

A warehouse desktop bot calls an internal REST yard-management API (`POST https://yard.intra/api/v2/gatein`) with `Content-type: application/json` and body `{"truck":"TX-491","gate":3}`. Proposed solution: Use `Invoke web service` and toggle `Encode request body` to `Off` under Advanced settings. Does this transmit valid raw JSON?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **D.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — turning `Encode request body` `Off` prevents PAD from URL-encoding curly braces and quotes in raw JSON POST bodies. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **D:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.

</details>

### Q015 (`E3Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

A freight company’s legacy AS/400 DB2 and SQL Server databases sit inside an on-premises datacenter, and cloud flows must query tariff tables before enqueueing Work Queue items. Proposed solution: Install a 2-node clustered On-Premises Data Gateway in the datacenter and reference it in the SQL Server Connection. Does this provide high-availability cloud-to-on-prem access?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — clustering On-Premises Data Gateways across two or more servers eliminates single points of failure for cloud flow on-premises SQL/DB2/File connections. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q016 (`E3Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow authenticates to an Azure Function customs-duty calculator locked down to Microsoft Entra ID tokens using the `HTTP` action’s built-in `____` (`ActiveDirectoryOAuth` / `Managed Identity`) authentication mode. Which capability avoids hardcoding bearer tokens?

- **A.** Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Cloud `HTTP` action authentication natively supports `ActiveDirectoryOAuth` and `Managed Identity` for zero-secret Entra token acquisition. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Correct — Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.

</details>

## Case Study Vignette — PacificHarbor Terminal

> [Scenario: PacificHarbor Terminal experienced intermittent `Cannot sign in to unlocked/active session` unattended RPA failures whenever support engineers closed RDP windows with `[X]` instead of signing out on target VMs. Admins are standardizing VM preparation, Machine Group sharing (`User` vs `Co-owner`), and Managed Solution upgrades.]

### Q017 (`E3Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — PacificHarbor Terminal: Why did PacificHarbor Terminal’s unattended runs fail whenever support engineers closed Remote Desktop with `[X]` on single-session VMs, and what operational fix resolves it?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Closing RDP with `[X]` leaves an active disconnected Windows session that blocks single-session unattended logins; engineers must run `Sign out` (`logoff`) or use Windows Server RDSH. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.

</details>

### Q018 (`E3Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — PacificHarbor Terminal: PacificHarbor’s security team wants to ensure no desktop flow in Production can execute `Run DOS command` or `Run VBScript` while allowing `Browser` and `UI automation` modules. Which control enforces this?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Desktop flow module and action DLP rules block `Command line (DOS)` and `VBScript` modules across the Production environment. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **D:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.

</details>

### Q019 (`E3Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — PacificHarbor Terminal: When a vessel arrives 6 hours early, PacificHarbor’s terminal dispatcher needs its queued manifest bot run moved ahead of 18 routine yard-inventory runs waiting on the Machine Group. Which portal actions accomplish this?

- **A.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). In `Monitor -> Machines -> Run queue`, changing the vessel run’s priority to `High` (`Change priority`) and selecting `Move to top` dispatches it next. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.
- **B:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q020 (`E3Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Gate clerks use a Power Apps Canvas scanner app to photograph damaged seals and pass `(ContainerId, PhotoBase64)` into a solution cloud flow via `DamageReportFlow.____(txtContainer.Text, varBase64)`. Which trigger/integration pattern applies?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **C.** Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Canvas apps invoke Instant cloud flows synchronously or asynchronously using the Power Apps (V2) trigger (`FlowName.Run(...)`). [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **C:** Correct — Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q021 (`E3Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Yard clerks trigger a solution desktop flow through a parent cloud flow, and you must ensure clerks can view their own triggers **without** opening Power Automate for desktop Designer to edit or delete the bot. Which Desktop flow permission prevents editing?

- **A.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **B.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Sharing a Desktop flow as `User` (or invoking via embedded cloud flow `Run-only` connection) withholds `Co-owner` edit and delete permissions. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **B:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **C:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q022 (`E3Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

How does targeting a **Machine Group** in a `Desktop flows` Connection Reference improve resiliency compared with targeting a single standalone Machine?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Targeting a Machine Group eliminates single-VM bottlenecks and SPOFs by automatically queuing and distributing runs across all healthy online member VMs. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.

</details>

### Q023 (`E3Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

A producer cloud flow adds container manifests into a Dataverse Work Queue, and the architect wants Dataverse to reject any duplicate enqueue attempt carrying an already-queued `BillOfLadingNo`. Which Work Queue item field enforces deduplication?

- **A.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **D.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Populating the Work Queue item’s `Unique reference` field with `BillOfLadingNo` prevents duplicate items with the same key inside the queue. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **D:** Incorrect — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.

</details>

### Q024 (`E3Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

A customs brokerage is rolling out the Microsoft Document Automation Toolkit to ingest emailed commercial invoices and route uncertain HS codes to human clerks. Order the four architectural stages from start to finish.

- **A.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **B.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email
- **C.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows
- **D.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Email attachments trigger intake cloud flows, AI Builder Document Processing extracts fields/confidence scores, clerks validate uncertain documents in Canvas Validation Station, and verified Dataverse data flows downstream. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **B:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.
- **C:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.
- **D:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.

</details>

### Q025 (`E3Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

A cloud flow passes a JSON string `{"bol":"MAEU991","containers":14}` into a desktop flow’s `Input` variable `%ShipmentPayload%` (`Data type = Text` or `Custom object`). Where must `ShipmentPayload` be defined so the cloud flow action displays an input box for it?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **C.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Variables created in Power Automate for desktop’s **Input/output variables** pane (`Input` direction with External name) surface as typed input fields on `Run a flow built with Power Automate for desktop`. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **C:** Correct — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q026 (`E3Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Unattended desktop flows fail at `1920x1080` screen-dependent legacy layout checks when executed headlessly because the VM defaulted to `1024x768` in background sessions. Where can you enforce `1920x1080` resolution for unattended sessions?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Unattended display resolution and scaling are configured in machine/unattended session settings (or `Microsoft.Flow.RPA.Agent.exe.config` / Hosted VM image settings) alongside clean signed-out sessions. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.

</details>

### Q027 (`E3Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

After submitting an ocean bill of lading in Chrome, the `Customs Reference #` span renders asynchronously via AJAX between 0.5 and 18 seconds later. Which PAD action waits dynamically for that DOM element up to a 30-second timeout?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Wait for web page content` polls for the target DOM element or text and proceeds immediately once rendered (or throws a timeout error after 30 seconds). [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.

</details>

### Q028 (`E3Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A warehouse desktop flow runs `Get-Printer | Where-Object PrinterStatus -ne 'Normal'` locally on the Windows print server VM to check Zebra label printers before dispatching labels. Which PAD action executes this cmdlet?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **C.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run PowerShell script` runs native Windows PowerShell pipelines locally and outputs `%PowershellOutput%` and `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **C:** Correct — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q029 (`E3Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

A freight architect must call both a public cloud carrier GraphQL API and a weighbridge controller HTTP endpoint bound exclusively to `192.168.10.5` on the warehouse LAN (with no On-Premises Data Gateway). Which two action choices match each endpoint? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **E.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). The public GraphQL API runs headlessly via the cloud `HTTP` action, while the warehouse LAN weighbridge endpoint is called directly from the local bot VM via PAD `Invoke web service`. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **E:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q030 (`E3Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Two regional IT leads co-manage `MG-PortBots` and need rights to add newly imaged VMs, remove retired VMs, and share the group with solution pipelines. Which permission on `MG-PortBots` must both IT leads receive?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Granting `Co-owner` on the Machine Group allows IT leads to manage member VMs, keys, and sharing permissions. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q031 (`E3Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

An RPA developer modularizes a 400-action freight desktop flow into `Main`, `Login_TMS`, `Enter_Waybill`, and `Logout_TMS`. If `Login_TMS` sets `%SessionToken% = 'OK'`, how does `Enter_Waybill` read `%SessionToken%`?

- **A.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers
- **B.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). All subflows inside a desktop flow share a single global variable scope, so `Enter_Waybill` reads `%SessionToken%` directly with zero parameter marshaling. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.
- **B:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q032 (`E3Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A maritime tracking portal renders vessel schedules inside nested shadow-root web components inaccessible to standard UI recorders, so you run `return document.querySelector('vessel-card').shadowRoot.querySelector('.eta').innerText;` inside `function ____()`. Which PAD action executes this?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { ... }` directly inside the live browser DOM, including piercing open Shadow DOM trees. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — `Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q033 (`E3Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

When a parent cloud flow’s `Try` Scope fails, how can the `Catch` Scope extract the exact failing action name and error message dynamically for a Teams alert (`____('Try_Scope')`)?

- **A.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). In cloud flows, `result('Try_Scope')` inside a `Catch` Scope (`Configure run after`: failed/skipped/timed out) returns an array of action statuses and error details from `Try_Scope`. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q034 (`E3Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

A port authority exposes an OpenAPI 3.0 berth-scheduling REST service that makers want to call across 20 solution cloud flows with environment-specific credentials. Which two solution components should you create? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **E.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Import the OpenAPI 3.0 spec as a solution-aware **Custom Connector** and bind flows via a **Connection Reference**. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **E:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q035 (`E3Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A customs single-window system returns an XML release receipt `<CustomsRelease ReceiptNo="US-88412"><Status>CLEARED</Status></CustomsRelease>`, and a cloud flow extracts the `ReceiptNo` attribute via `____(xml(outputs('XML_Receipt')), 'string(/CustomsRelease/@ReceiptNo)')`. Which WDL function applies?

- **A.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `xpath(xml(...), 'string(/CustomsRelease/@ReceiptNo)')` evaluates XPath attribute and text queries directly inside cloud flows. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.

</details>

### Q036 (`E3Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

What secret artifact is generated when creating a standard **Machine Group** and required whenever joining an additional registered VM into that Machine Group?

- **A.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Joining a VM to a standard Machine Group requires the **Machine Group password / recovery key** established during group creation (or managed via Key Vault). [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q037 (`E3Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

IronRail’s platform team is authoring, signing, uploading, and enabling a custom `.NET Framework` railcar check-digit action for Power Automate for desktop. Choose the valid four-step sequence.

- **A.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand
- **B.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically
- **C.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop
- **D.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Build the `ActionBase` class with the Custom Actions SDK, package & sign the `.cab` with a trusted certificate, upload under Custom actions in Portal, and add to a Solution. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.
- **B:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.
- **C:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).
- **D:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.

</details>

### Q038 (`E3Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

An unattended desktop bot inspects a legacy Java Swing weighbridge window that renders faded dot-matrix digits where scaling image width/height by `3x` in Tesseract dramatically improves character recognition. Which PAD action configuration supports scale multipliers?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **C.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **D.** AI Builder Category Classification or Entity Extraction model in cloud flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Extract text with OCR` with the `Tesseract engine` exposes `Image width multiplier` and `Image height multiplier` parameters alongside custom `.traineddata` packs. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **C:** Correct — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **D:** Incorrect — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.

</details>

### Q039 (`E3Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Inside a cloud flow `Apply to each` loop iterating over 40 independent carrier REST calls, sequential execution takes 8 minutes. Enabling `Apply to each` Concurrency Control (`Degree of Parallelism = ____`) speeds up independent stateless iterations, EXCEPT when mutating a cloud `Set variable` inside the loop. Which concurrency principle governs cloud flow parallelism?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Cloud trigger and `Apply to each` Concurrency Control (`1–50`) parallelize stateless API calls, whereas shared variable mutations serialize or contend across parallel branches. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q040 (`E3Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

A freight carrier hosts sandbox APIs at `uat-api.carrier.example` and live APIs at `prod-api.carrier.example`. Which codeless Custom Connector policy template dynamically overrides the target host URL per Connection or parameter at runtime?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **D.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Set host URL` policy template dynamically rewrites the backend target hostname at runtime without duplicating Custom Connectors per stage. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **D:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.

</details>

### Q041 (`E3Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

During a Production hotfix audit, an architect discovers someone imported an Unmanaged patch and edited a cloud flow directly in Production, creating an `Active` layer above Managed `1.8.0.0`. Which two actions restore clean ALM? Select two.

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **E.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Run `Remove active customizations` on Solution Layers in Production and deploy fixes exclusively from Dev as Managed Solution upgrades via pipelines. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **E:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

## Case Study Vignette — IronRail Intermodal

> [Scenario: IronRail Intermodal runs attended yard-clerk desktop flows launched instantaneously from a Canvas tablet app and desktop `ms-powerautomate:` URLs, alongside unattended yard-gate SAP GUI bots packaged with a signed `.NET Framework` Custom Action CAB module (`Desktop Flow Module`) that calculates railcar check-digits offline.]

### Q042 (`E3Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — IronRail Intermodal: IronRail Intermodal also plans to automate emailed drayage carrier freight bills where clerks review `< 90%` confidence line items in a prebuilt Canvas app. Which Microsoft starter kit matches this pattern?

- **A.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Microsoft Document Automation Toolkit provides email ingestion, AI Builder Document Processing, Dataverse tables, and the Canvas Validation Station app. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q043 (`E3Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — IronRail Intermodal: Yard clerks launch attended helper bots via `ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...` while unattended bots drive SAP GUI controls whose screen IDs include variable plant prefixes (`wnd[0]/usr/ctxt____`). Which selector approach stabilizes the SAP/UI elements?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Parameterizing dynamic `%PlantPrefix%` variables and pattern operators inside Selector Builder keeps UI elements stable across rail yards. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.

</details>

### Q044 (`E3Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — IronRail Intermodal: IronRail’s signed `.NET Framework` Custom Action (`Desktop Flow Module`) computes railcar check-digits offline, and the desktop bot then POSTs raw JSON gate events to a yard controller via `Invoke web service` (`Encode request body = ____`). What setting prevents JSON corruption?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Setting `Encode request body` to `Off` in `Invoke web service` ensures raw JSON gate events are transmitted without URL-encoding corruption. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q045 (`E3Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

While stepping through a complex customs desktop flow in PAD Designer, you press `____` (`Run next action` / `F10`) at a Breakpoint to inspect how `%DutyTotal%` changes in the Variables pane one action at a time. Which toolset supports this?

- **A.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop Designer provides `Breakpoints`, `Run next action (F10)`, `Run from here`, `Run delay`, and real-time `Variables` inspection. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **B:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

### Q046 (`E3Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

A developer notices that importing an Unmanaged flow created outside Solutions hardcodes personal connector bindings, breaking UAT automation. Moving the flow into a Dataverse Solution automatically introduces which abstraction layer?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Solution-aware flows reference connectors through **Connection References**, cleanly decoupling flow logic from concrete environment Connections. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q047 (`E3Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

A maker builds a cloud flow triggered by `SharePoint` (`Business` group) that calls `Run a flow built with Power Automate for desktop` (`Desktop flows`) and posts status to `X / Twitter` (`Blocked` group). Why does Power Automate suspend the flow on save?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Platform DLP immediately blocks any flow referencing a `Blocked` connector or mixing `Business` and `Non-Business` connectors. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q048 (`E3Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

An intermodal IT engineer is registering five freshly imaged Windows 11 Enterprise VMs into `MG-YardGates` in Production using Power Automate machine runtime. Place the steps in the valid order.

- **A.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference
- **B.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly
- **C.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **D.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create `MG-YardGates` in Portal, register each VM to Production via Power Automate machine runtime, join `MG-YardGates` with the group key, and share as `User` with Connection References. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.
- **B:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.
- **C:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **D:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.

</details>

### Q049 (`E3Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow queries a customs tariff REST endpoint that returns 250 HS codes per response page out of 12,000 total codes. Proposed solution: Enable `Pagination` on the `HTTP` action and set `Threshold = 15000`. Does this retrieve all 12,000 codes across continuation links?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — turning on `Pagination` with a `Threshold` above `12000` instructs the cloud `HTTP` action to follow `@odata.nextLink` / next-page links until all items are aggregated. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q050 (`E3Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

A customs integration developer needs a Custom Connector to authenticate with an `X-Broker-ApiKey` HTTP header and compute an SHA-256 canonical body digest in C# before forwarding requests. Which two Custom Connector features should they configure? Select two.

- **A.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **B.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **E.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). `API Key` security injects `X-Broker-ApiKey`, while `Script : ScriptBase` (`ExecuteAsync()`) computes the fast `< 5s` SHA-256 request digest. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **B:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.
- **C:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **E:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q051 (`E3Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

How should unattended Windows bot credentials be managed so warehouse RPA developers can bind `Desktop flows` connections to bot pools without ever knowing or viewing the Windows account password?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Creating Power Automate `Credentials` backed by Azure Key Vault or CyberArk and sharing the Credential artifact lets makers bind connections without seeing underlying passwords. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.

</details>

### Q052 (`E3Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

An enterprise freight solution decomposes a monolithic 180-action cloud flow into a lightweight parent flow and four modular Child Cloud Flows. Which two rules govern Child Cloud Flows? Select two.

- **A.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **E.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Child cloud flows must live inside a Dataverse Solution and configure `Run only users` connections to `Use this connection` (embedded credentials). [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **E:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.

</details>

### Q053 (`E3Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

A maritime logistics firm must pass rotating customs-broker API tokens from Azure Key Vault through a parent cloud flow into an unattended desktop bot with zero plaintext log exposure. Select the correct four-step sequence.

- **A.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs
- **B.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step
- **C.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log
- **D.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Key Vault-backed Credentials/Secret Env Vars, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags protect secrets across every hop. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.
- **B:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.
- **C:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.
- **D:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.

</details>

### Q054 (`E3Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

An intermodal reconciliation bot queries a local SQL Express yard database, reads an XML rail-consist file with XPath (`//Car/@Initial`), and writes reconciled discrepancies to the next empty row of `YardAudit.xlsx`. Which three PAD action groups accomplish this? Select three.

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **E.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **F.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D, E` (`CSV: 1,4,5`)

Correct answers: A, D, and E (are correct). `Open SQL connection` / `Execute SQL statement`, `Read XML from file` / `Execute XPath expression`, and `Launch Excel` / `Get first free column/row` + Datatables cover all three operations. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **E:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **F:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q055 (`E3Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

An EDI AS2 webhook posts JSON batches containing 100 container status events per array, and you notice 100 parallel flow runs starting per POST instead of 1 batch run. Which trigger toggle is currently `On` and must be switched `Off`?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Triggers on array outputs enable `Split On` by default to fan out one run per item; switching `Split On` to `Off` processes the entire batch array in a single run. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Correct — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.

</details>

### Q056 (`E3Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A network share briefly disconnects for 3 seconds during nightly switch failover while a desktop flow writes manifest logs, causing `Write text to file` to throw an I/O error once a week. Which declarative PAD setting resolves this without cluttering the canvas?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configuring `Retry action if an error occurs` (for example `3` retries at `3`-second intervals) in `Write text to file`’s `On error` policy masks brief network-share blips. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).

</details>

### Q057 (`E3Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A customs Custom Connector is placed in the `Business` DLP group, and admins configure Custom Connector URL patterns: `Order 1: Allow https://sw.customs.gov/*`, `Order 2: Deny *`. What happens if a maker modifies the Custom Connector’s host to `https://webhook.evil.example/steal`?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The ordered DLP Custom Connector URL pattern rejects `https://webhook.evil.example/*` under the `Order 2: Deny *` catch-all rule and blocks flow execution. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q058 (`E3Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

A warehouse RPA engineer is fixing a brittle WinForms dock-scheduling selector that broke when the app upgraded from `v4.1` to `v4.2` (`WindowTitle = "DockSched v4.2 - Bay 09"`). Choose the resilient Selector Builder sequence.

- **A.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **B.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs
- **C.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field
- **D.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Removing hardcoded version suffixes, applying `Starts with` / `%BayNumber%` in Selector Builder, and adding fallback selectors keeps WinForms selectors resilient across minor upgrades. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **B:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.
- **C:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.
- **D:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).

</details>

### Q059 (`E3Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

A customs compliance team uses a Model-driven app over `ShipmentDeclaration` rows and needs auditable relational storage with field-level security on `ImporterTaxId` plus native server triggers. Which platform database satisfies all three requirements?

- **A.** Microsoft Dataverse custom/standard tables providing relational storage, security roles, and native triggers
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Microsoft Dataverse provides relational tables, column-level security profiles, audit logs, and native cloud flow triggers. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Correct — Dataverse serves as the enterprise state store for Power Platform RPA metadata, Work Queues, audit logs, and business records.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q060 (`E3Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

Which built-in connectors also support **Connector endpoint filtering** (`Allow` / `Deny` host patterns, SQL server names, or SharePoint site URLs) in Power Platform DLP alongside Custom Connectors?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Connector endpoint filtering governs `HTTP`, `HTTP with Microsoft Entra ID`, `SQL Server`, `Dataverse`, `SharePoint`, `Azure Blob`, and `SMTP` endpoints alongside Custom Connector host patterns. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q061 (`E3Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

A cloud flow receives an array of 1,200 ocean container objects and needs an array containing ONLY `{"ContainerNo": item()?['cntr'], "Seal": item()?['seal_no']}` without running 1,200 `Append to array variable` iterations. Which single Data Operation projects this new shape?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The cloud `Select` Data Operation maps every element of an input array into a projected JSON object shape in a single step. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q062 (`E3Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A customs broker wants a cloud flow to classify incoming trade compliance inquiries into `Tariff Dispute`, `Valuation`, `Origin Certificate`, or `Sanctions Hold` using historical labeled rows in Dataverse. Which AI Builder model applies?

- **A.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **B.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **C.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder Category Classification trains on labeled historical Dataverse text to classify new inquiries automatically inside cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **B:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **C:** Correct — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **D:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q063 (`E3Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Six customs-entry bots process 9,000 commercial invoices daily where high-value perishable shipments (`Priority = High`) must jump ahead of standard ocean freight in a durable Dataverse backlog. Which Power Automate feature should you design?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **C.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dataverse Work Queues natively support item-level `Priority`, `ExpiresOn` SLAs, `Unique reference` deduplication, and multi-bot concurrent leasing. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **C:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q064 (`E3Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

A customs supervisor wants to test an updated desktop flow action-by-action directly on their development workstation before triggering it from the cloud. Which execution method fits?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **C.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Launching the flow interactively from the Power Automate for desktop console or Designer supports live local testing and step-through inspection. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Correct — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **C:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q065 (`E3Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

A desktop flow reads 35 carrier portal timeout thresholds and folder paths at startup. Combining Dataverse `Environment Variables` for environment URLs with a versioned JSON config file parsed via `Convert JSON to custom object` implements which best practice?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Externalizing non-secret operational settings into Dataverse Environment Variables and structured JSON/XML config files eliminates hardcoded constants inside desktop flows. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q066 (`E3Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

A customs parent cloud flow invokes `Run a Child Flow` (`Calculate_Harbor_Maintenance_Fee`), which finishes its Dataverse steps but lacks a `Respond to a Power App or flow` or `Response` action. What happens when you save or run the flows?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate validation requires every Child Cloud Flow to include `Respond to a Power App or flow` or HTTP `Response` so the parent flow receives synchronous completion. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.

</details>

## Case Study Vignette — AeroLink Cold Chain

> [Scenario: AeroLink Cold Chain polls cold-storage sensor APIs from a cloud flow using `@and(...)` Trigger Conditions, ISO 8601 `PT10M` timeouts, and exponential retry policies, then calls reusable solution Child Cloud Flows and subflow-modularized desktop flows that log temperature excursions into Excel and CSV manifests.]

### Q067 (`E3Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — AeroLink Cold Chain: AeroLink’s cold-storage carrier portal renders live reefer telemetry charts inside HTML5 custom elements whose underlying array `window.__reeferReadings` is accessible only via in-tab JavaScript. Which PAD action reads `window.__reeferReadings`?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { return JSON.stringify(window.__reeferReadings); }` inside the live browser tab. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q068 (`E3Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — AeroLink Cold Chain: AeroLink’s sensor API keys are retrieved in the parent cloud flow (`Timeout = PT10M`, `@and(...)` Trigger Conditions) and passed to child/desktop flows. Which cloud action Settings flags keep those API keys out of 28-day Run History?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enabling `Secure Inputs` and `Secure Outputs` on the cloud flow actions redacts API keys and tokens across Run History and telemetry. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Correct — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.

</details>

### Q069 (`E3Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — AeroLink Cold Chain: AeroLink wraps its cold-storage sensor REST API in a solution Custom Connector using OAuth 2.0 and needs codeless header injection (`X-ColdChain-Tenant`) on every call. Which Custom Connector feature should they configure?

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A `Set HTTP header` **Policy template** on the Custom Connector injects `X-ColdChain-Tenant` on every outbound API request without code. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **D:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q070 (`E3Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A desktop flow needs to execute retryable tariff lookups for index `%RowIdx%` starting at `0`, ending at `%TariffTable.RowsCount - 1%`, incrementing by `1`. Complete the PAD loop action: `____` (`Start from = 0`, `End to = %TariffTable.RowsCount - 1%`, `Increment by = 1`). Which PAD action group applies?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Power Automate for desktop `Loop` action iterates an integer `%LoopIndex%` from `Start from` through `End to` by `Increment by` (alongside `For each` and `Loop condition`). [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q071 (`E3Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

An ocean freight carrier wants a flow to execute automatically whenever a new customs declaration XML blob lands in Azure Blob Storage and post a summary into Microsoft Teams without spinning up any Windows bots. Which flow type should you design?

- **A.** Automated cloud flow triggered asynchronously by an external connector event
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). An Automated cloud flow reacts directly to connector events such as new Azure Blob or SharePoint items with zero desktop session overhead. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q072 (`E3Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

Inside a desktop flow, when a customs portal displays `Account Locked — Contact Port Security`, the bot must immediately stop all remaining subflows and cause the parent cloud flow’s `Run a flow built with Power Automate for desktop` action to enter its `Catch` Scope. Which PAD action achieves this?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Stop flow` configured `With error message` terminates the entire desktop flow run in a failed state and passes the error message back to the calling cloud flow. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **C:** Correct — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.

</details>

### Q073 (`E3Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

A global 3PL automates a local WPF dock-door app, an external carrier portal in Google Chrome, and a remote Microsoft RDP-hosted warehouse client. Which three components enable rich element selectors across all three targets? Select three.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors
- **C.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **E.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **F.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). Native Windows UIA drives local WPF controls, the Chrome Power Automate browser extension exposes web DOM nodes, and the virtual desktop agent enables UI selectors inside remote RDP/Citrix hosts. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Correct — UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.
- **C:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **D:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **E:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **F:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q074 (`E3Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A Dataverse `When a row is added, modified or deleted` cloud flow on `FreightBooking` must ONLY start when `BookingType` equals `'HAZMAT'` and `WeightKg` is at least `1000`: `@and(equals(triggerOutputs()?['body/cr12_bookingtype'], 'HAZMAT'), ____(triggerOutputs()?['body/cr12_weightkg'], 1000))`. Which feature and WDL function applies?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **D.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Trigger Conditions (`@and(equals(...), greaterOrEquals(...))`) discard non-HAZMAT or light bookings before spinning up a cloud flow instance. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **D:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.

</details>

### Q075 (`E3Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

A freight-audit developer is configuring a solution cloud flow to trigger an unattended tariff-entry desktop flow and capture `%CustomsEntryNumber%` back in the cloud flow. Select the correct four-step workflow.

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod
- **C.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **D.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Declare Input/Output variables in the solution desktop flow, add `Run a flow built with Power Automate for desktop`, bind Machine/Group Connection Reference & Inputs, and consume returned Output tokens. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.
- **C:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **D:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.

</details>

### Q076 (`E3Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

A customs desktop flow enters tariff lines into a legacy Win32 app whose control hierarchy differs slightly between Windows 10 branch PCs and Windows Server 2022 unattended VMs. Which two PAD UI selector features handle dynamic text and dual control trees inside one UI element? Select two.

- **A.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **B.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Dynamic `%Variable%` / Regex operators match variable captions, and defining multiple ranked selectors inside a single UI element lets PAD fall back automatically across OS control trees. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **B:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q077 (`E3Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

A security team creates a Desktop Flow DLP policy that blocks the `FTP` and `Run Python script` modules in Production. Proposed solution: Enforce Desktop Flow DLP in Power Platform Admin Center so any desktop flow containing `FTP` or `Run Python script` is automatically suspended from running. Does Power Platform DLP support desktop module blocking?

- **A.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — Desktop flow module and action governance inside Power Platform DLP policies blocks prohibited PAD modules/actions and suspends offending desktop flows. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q078 (`E3Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A desktop bot on a rail-yard PC needs to invoke a legacy `.vbs` script that connects to an ActiveX serial-port barcode multiplexer (`CreateObject("MSCommLib.MSComm")`) and reads `%____%` (`%VBScriptOutput%`). Which scripting action should you use?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run VBScript` executes Windows COM/ActiveX `.vbs` code locally and captures stdout in `%VBScriptOutput%` and errors in `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Correct — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

### Q079 (`E3Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

A drayage dispatcher sits at their workstation, highlights a container number, presses a shortcut to run a helper bot that populates five web fields, and visually confirms the tariff before pressing Submit. Proposed solution: Run the desktop flow in `Attended` mode inside the dispatcher’s active Windows session. Does this match the scenario?

- **A.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — Attended mode is purpose-built for human-present desktop automation running inside the signed-in operator’s active session. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Correct — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.

</details>

### Q080 (`E3Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

An auditor requires UAT bots to log into Windows VMs using `CORP\svc-rpa-uat` and Production bots to log in using `CORP\svc-rpa-prod`, both rotated nightly in Azure Key Vault. How is this configured cleanly?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Define environment-specific Power Automate `Credentials` backed by UAT and Prod Key Vaults and bind each stage’s `Desktop flows` Connection Reference to its respective Credential. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q081 (`E3Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

Before promoting a freight RPA release, QA engineers run cloud flow unit tests without hitting live customs endpoints, debug PAD subflows interactively, and verify stage URLs switch dynamically. Which three features support those three tasks? Select three.

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **E.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **F.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). `Static Result` mocks cloud actions offline, PAD Designer debugging tools (`Breakpoints` / `Run from here`) test subflows, and `Environment Variables` supply stage URLs. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **C:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **E:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **F:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q082 (`E3Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

Inside a Power Automate for desktop action input field, you need to concatenate `%PortCode%`, a hyphen, and `%VesselId%` inside a single expression: `%PortCode + '-' + ____%`. How does PAD evaluate inline variable expressions?

- **A.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop evaluates arithmetic and string concatenation inside single enclosing percent signs (`%PortCode + '-' + VesselId%`). [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **B:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **D:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q083 (`E3Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A logistics automation architect is mapping dispatch workflows across Instant, Scheduled, and Desktop flows. Which two scenarios belong in Power Automate cloud flows (`Instant` or `Scheduled`) rather than standalone desktop flows? Select two.

- **A.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **E.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Mobile/Canvas dispatch button triggers (`Instant`) and hourly carrier-tariff API polls (`Scheduled`) execute natively in headless cloud flows. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Correct — Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **E:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q084 (`E3Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

Unattended customs bots dequeue items via `Process work queue items`. When a declaration succeeds versus fails a deterministic tariff validation, which two status updates properly close out the Work Queue item? Select two.

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **E.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). `Update work queue item` marks completed entries `Processed` and marks business-rule exceptions `On hold` or `Generic exception` with processing notes without retrying UI steps. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **E:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q085 (`E3Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

Inside a C# Custom Action class inheriting `____` (`ActionBase`), which method must you override to execute the custom action’s runtime logic?

- **A.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate Custom Actions SDK classes inherit `ActionBase` and override `public override void Execute(ActionContext context)`. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q086 (`E3Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

A customs brokerage separates **System Exceptions** (portal HTTP 500, hung browser) from **Business Exceptions** (missing country-of-origin certificate, prohibited HS code). Which two engineering practices enforce this distinction? Select two.

- **A.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **E.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). System Exceptions use `On block error` + `Scope` retries/recovery, whereas Business Exceptions bypass UI retries immediately and update Work Queue items (`On hold` / business error) for broker review. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **E:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.

</details>

### Q087 (`E3Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

Thirty container-release desktop runs are queued against `MG-CustomsPool` (5 VMs): 28 `Normal` runs queued at 09:00 and 2 `High` priority perishable-cargo runs queued at 09:04. In what order are waiting runs dispatched as VMs free up?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The Machine Group dispatches the 2 waiting `High` priority runs first (FIFO among `High`), followed by the 28 `Normal` runs in FIFO order. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).

</details>

### Q088 (`E3Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A carrier API returns stringified JSON inside a string property `"metadata": "{\"vessel\":\"Aurora\",\"voyage\":null}"`. Proposed solution: Use `coalesce(json(triggerBody()?['metadata'])?['voyage'], 'UNASSIGNED')` in the cloud flow. Does this parse the nested JSON string and default `voyage` safely?

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — `json()` deserializes the nested JSON string and `coalesce(..., 'UNASSIGNED')` substitutes a safe fallback whenever `voyage` is null. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q089 (`E3Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

An intermodal carrier wants to distribute a proprietary ISO-6346 container check-digit calculator (`ActionBase`) to 30 desktop flow makers as a native toolbox category in Power Automate for desktop. What must they build?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **D.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Authoring a .NET Framework Custom Actions SDK assembly packaged into a signed `.cab` and uploaded to Dataverse Custom actions adds custom toolbox actions to PAD Designer. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **D:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

## Case Study Vignette — Portside Customs Brokerage

> [Scenario: Portside Customs Brokerage extracts multi-page ocean bills of lading using AI Builder and PDF table extraction, validates HS tariff codes against an on-premises SQL Server via an On-Premises Data Gateway in cloud flows, and flags mismatched container weights as Business Exceptions (`On hold`) without triggering 3x UI system retries.]

### Q090 (`E3Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — Portside Customs Brokerage: Portside Customs Brokerage extracts multi-page digital PDF ocean bills of lading and also reads scanned stamped annexes. Which two-tier Microsoft capability pairs cloud multi-layout extraction with local PDF table parsing?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder Document Processing extracts multi-layout scanned/digital documents with confidence scores, complemented by PAD `Extract tables from PDF` for digital tables. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q091 (`E3Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — Portside Customs Brokerage: Which infrastructure component allows Portside’s **cloud flow** to validate extracted HS tariff codes against its private on-premises SQL Server database?

- **A.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **D.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A clustered **On-Premises Data Gateway** relays cloud flow SQL Server queries securely into Portside’s private datacenter over outbound TLS. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **D:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.

</details>

### Q092 (`E3Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — Portside Customs Brokerage: When a container’s declared weight disagrees with the carrier manifest by `> 5%`, how should Portside’s unattended desktop flow record this **Business Exception** in the Dataverse Work Queue?

- **A.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Skip UI retries and invoke `Update work queue item` setting status to `On hold` (or `Generic exception` with business reason notes) so customs brokers review the weight discrepancy. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q093 (`E3Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

An ocean carrier’s HTML manifest table uses dynamic row classes (`tr.row_even`, `tr.row_odd`) while every container cell carries `<td data-col="cntr_no">MSCU1234567</td>`. Complete the resilient CSS selector: `table#manifest tbody tr td[____="cntr_no"]`. Which strategy applies?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **C.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Attribute-based CSS selectors (`td[data-col="cntr_no"]`) decouple web extraction from alternating presentation classes or pixel layouts. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **C:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q094 (`E3Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow action calls a slow port-authority vessel manifest service and must fail fast after exactly 45 seconds (`Timeout = ____`) so the `Catch` Scope can switch to a secondary mirror API. Which ISO 8601 Timeout format is valid?

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting `PT45S` in the cloud action’s ISO 8601 `Timeout` setting aborts hung requests at 45 seconds. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.

</details>

### Q095 (`E3Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow initializes `%ContainerList%` via `Create new list`, appends 80 container IDs, sorts them alphabetically via `____` (`Sort list`), and removes duplicates. Which PAD variable category handles 1D collections and JSON dictionaries?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop `List` actions (`Create new list`, `Add item to list`, `Sort list`, `Remove duplicate items from list`) and `Custom object` variables manage collections and key-value maps. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q096 (`E3Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

A customs desktop flow receives multi-page digital PDF commercial invoices and must pull all embedded line-item grids directly into `%PdfTables%` (`List of Datatables`) locally without consuming AI Builder credits. Which built-in PDF action accomplishes this?

- **A.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **B.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Extract tables from PDF` parses tabular grids out of digital PDF files locally into Power Automate for desktop Datatables. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **B:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q097 (`E3Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A developer compiles a custom action `.cab` without signing it with a certificate. Proposed solution: Upload the unsigned `.cab` directly to Production unattended bot pools without code signing. Will hardened Production machines load the unsigned custom action?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No — Production Power Automate for desktop machines verify the digital signature of `.cab` Custom Action modules against trusted Windows certificate stores before loading them. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q098 (`E3Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow loads a 600-row customs tariff schedule into `%TariffTable%` and needs to replace every occurrence of `'N/A'` with `'0.00'` across the Datatable before filtering duty-free rows. Which PAD action family performs this in memory?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Find or replace in data table` and `Filter data table` manipulate `Datatable` variables directly in memory inside Power Automate for desktop. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **C:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q099 (`E3Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

A port operator wants burst capacity for peak shipping season without managing hypervisors, while keeping 2 on-premises Windows Server 2022 hosts running 4 concurrent sessions each for LAN-only terminal access. Which two capabilities fit? Select two.

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **D.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **E.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Hosted Machine Groups auto-scale cloud Azure VMs from Azure Compute Gallery images, while on-premises Windows Server RDSH hosts run concurrent multi-session LAN bots. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **D:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **E:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.

</details>

### Q100 (`E3Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A customs broker’s cloud `HTTP` action receives occasional `HTTP 408` and `HTTP 504` timeouts from a national single-window gateway. Which action setting automatically re-attempts transient gateway timeouts up to 4 times at fixed 20-second intervals (`PT20S`)?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configuring `Fixed Interval` (or `Exponential Interval`) in the cloud action’s `Retry Policy` automatically retries `408`, `429`, and `5xx` transient errors. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **C:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>
