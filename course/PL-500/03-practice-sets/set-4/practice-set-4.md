# Microsoft Exam PL-500: Practice Exam 4 — Automotive AS/400 5250, COM Scripting & Custom Connectors — Reviewer Study Key

**Theme:** IBM 5250 terminal sessions, Datatables, VBScript/PowerShell COM automation, Custom Connector C# ScriptBase, and Portal Monitor telemetry  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E4Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

Supplier packing slips arrive in 25 different scanned PDF formats containing part numbers, quantities, and PO tables. Which Microsoft AI capability extracts structured fields and table rows with confidence scores in a cloud flow?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **C.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder Document Processing extracts header fields and multi-row line items with confidence scores across varied supplier layouts. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **C:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **D:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q002 (`E4Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Plant Windows service-account passwords rotate weekly in Azure Key Vault (`kv-plant-rpa-prod`). How does Power Automate consume rotated VM sign-in secrets automatically without touching Connection References or flows?

- **A.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **B.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate **Credentials** linked to Azure Key Vault secrets (via an Entra/Key Vault setup) retrieve the current secret version dynamically on each unattended run. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **B:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q003 (`E4Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

A Machine Group contains 3 VMs, all currently busy running 20-minute inventory bots. At 10:02 `Run_A` (`Normal`), at 10:03 `Run_B` (`High`), and at 10:04 `Run_C` (`High`) enter the queue. When VM #1 finishes at 10:05, what exact dispatch order follows?

- **A.** Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Run_B` dispatches first, then `Run_C` (FIFO within `High` priority), and finally `Run_A` (`Normal` priority) unless manually reordered via `Move to top`. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Correct — Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q004 (`E4Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

A plant desktop bot calls a legacy SOAP 1.2 ERP material-staging service (`http://erp.plant.local:8000/MaterialService?wsdl`) directly from the shop-floor VLAN. Which PAD action consumes the WSDL contract natively?

- **A.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **D.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Invoke SOAP web service` imports WSDL endpoints and executes typed XML SOAP operations from the local bot workstation. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Correct — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **D:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.

</details>

### Q005 (`E4Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

An unattended MES bot finishes posting a Work Queue item into the AS/400 schedule cleanly. Which Power Automate for desktop action marks the leased item completed (`Status = ____` -> `Processed`) and records the AS/400 confirmation code in `Processing notes`?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **C.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Update work queue item` sets the leased item’s status to `Processed` (or `Generic exception` / `On hold`) and writes confirmation metadata to `Processing notes`. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **C:** Incorrect — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q006 (`E4Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A Dataverse-triggered cloud flow on `QualityInspection` should start ONLY when `ScrapCount` exceeds `0` and `PlantCode` is not null: `@and(greater(triggerOutputs()?['body/cr44_scrapcount'], 0), not(____(triggerOutputs()?['body/cr44_plantcode'], null)))`. Which trigger feature applies?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Trigger Conditions (`@and(greater(...), not(equals(..., null)))`) suppress non-scrap events at the trigger boundary without consuming runs. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.

</details>

### Q007 (`E4Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

A plant bot opens `ShiftScrap.xlsx`, calls `Get first free column/row from Excel worksheet` storing `%FirstFreeRow%`, writes new scrap rows, and saves the workbook via `Close Excel` (`Before closing Excel = ____`). Which PAD action group handles native workbook automation?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Built-in Excel actions (`Launch Excel`, `Get first free column/row`, `Write to Excel worksheet`, `Close Excel -> Save document`) automate workbooks reliably. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q008 (`E4Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

An automotive cryptography team wants plant RPA makers to sign firmware manifests using a custom C# `.NET Framework` class (`ActionBase`) packaged as a signed `.cab` module in Power Automate for desktop. Which feature is this?

- **A.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate Custom Actions SDK `.cab` packages signed with a trusted certificate extend PAD Designer with governed custom `.NET` actions. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **B:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q009 (`E4Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

When promoting a parent-and-child cloud flow architecture across Dev, UAT, and Production, which two requirements prevent broken parent-to-child references and connection errors? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **E.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Keep both parent and child flows inside a Dataverse Solution and configure the child flow’s `Run only users` connections to `Use this connection`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **E:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.

</details>

### Q010 (`E4Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Where are uploaded `.cab` Power Automate for desktop Custom Action modules stored so they travel automatically with Managed Solutions across Dev, UAT, and Production?

- **A.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Uploaded custom actions are stored in Microsoft Dataverse (`Desktop Flow Module` table) and packaged inside Dataverse Solutions alongside the desktop flows that use them. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q011 (`E4Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

Which two statements accurately describe sharing permissions for RPA components in Power Automate? Select two.

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **E.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Desktop flows offer `User` (run) and `Co-owner` (edit/manage), while Machines and Machine Groups offer `User` (dispatch runs) and `Co-owner` (manage machines & sharing). [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **E:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.

</details>

### Q012 (`E4Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Plant maintenance technicians use a locked-down kiosk batch script (`schtasks.exe`) that launches an attended calibration desktop flow locally via URI: `start "" "____"`. Which protocol format runs the local PAD flow with input parameters?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Invoking `ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...&input=...` launches local attended desktop flows from scripts, links, or Task Scheduler. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Correct — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q013 (`E4Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

An enterprise infrastructure team supports both cloud-only supplier portals (bursty workloads) and factory-floor serial/COM tester PCs. Which two unattended hosting rules apply? Select two.

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **E.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Use **Hosted Machine Groups** (`Hosted RPA` with Azure Compute Gallery images) for elastic cloud portals, and keep single-session shop-floor VMs fully **signed out** for unattended runs. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **E:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.

</details>

### Q014 (`E4Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

A battery-plant engineer compares calling a cloud supplier REST portal versus polling a local shop-floor torque controller at `http://10.40.2.19:8080/status` directly from a plant bot VM. Which two HTTP choices are optimal? Select two.

- **A.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **B.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Use the cloud `HTTP` action for cloud-reachable supplier APIs and PAD `Invoke web service` for direct bot-to-controller LAN HTTP traffic. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **B:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q015 (`E4Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

An automotive cloud flow calls an internal SAP OData gateway secured with mutual TLS (`Client Certificate` `.pfx` stored in Key Vault). Which `HTTP` action Authentication option supports PFX base64 + password authentication natively?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **D.** Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The cloud `HTTP` action’s built-in Authentication menu supports `Client Certificate` (PFX + password), `ActiveDirectoryOAuth`, `Managed Identity`, and `Basic`. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **D:** Correct — Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.

</details>

### Q016 (`E4Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

Inside a `Verify_Calibration` subflow, if the master gage is expired (`%DaysOverdue% > 0`), the bot must abort the entire desktop flow run immediately with error `'GAGE_EXPIRED'` rather than returning to `Main`. Proposed solution: Use `Exit subflow` inside the `If` block. Does `Exit subflow` abort the entire desktop flow with an error?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — `Exit subflow` merely returns control to the caller (`Main`) as a normal step; you must use **`Stop flow` (`With error message`)** to abort the entire desktop flow and report failure. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Correct — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.

</details>

## Case Study Vignette — Kestrel Precision Castings

> [Scenario: Kestrel Precision Castings built a Custom Connector wrapping an internal MES REST API with OAuth 2.0 authentication, a `Set HTTP header` policy template injecting plant routing codes, and a C# `ScriptBase` transform converting nested XML responses to JSON for downstream cloud and desktop flows.]

### Q017 (`E4Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — Kestrel Precision Castings: Kestrel’s web-based metallurgy portal renders alloy heat-treatment curves inside an HTML5 `<canvas>` backed by `window.alloyChart.data`, which cannot be scraped via static HTML tags. Which PAD action retrieves `window.alloyChart.data`?

- **A.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { return JSON.stringify(window.alloyChart.data); }` inside the open browser tab. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **B:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q018 (`E4Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — Kestrel Precision Castings: Kestrel’s OAuth 2.0 client secrets and alloy recipe parameters traverse parent cloud flows into desktop bots. Which cloud action Settings switches mask those payloads in cloud Run History?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Turning on `Secure Inputs` and `Secure Outputs` in cloud action Settings masks sensitive inputs and outputs (`*REDACTED*`) in Run History. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.

</details>

### Q019 (`E4Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — Kestrel Precision Castings: In Kestrel’s MES Custom Connector (`OAuth 2.0` + `Set HTTP header` policy template), what C# mechanism converts nested XML responses into JSON within the 5-second limit?

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Implementing `public class Script : ScriptBase` and overriding `ExecuteAsync()` transforms the HTTP response payload inside the Custom Connector in under 5 seconds. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.

</details>

### Q020 (`E4Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

An automotive CoE is building, code-signing, uploading, and solution-packaging a `.NET Framework` CRC-32 CAN-frame custom action for Power Automate for desktop. Choose the valid four-step sequence.

- **A.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD
- **B.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop
- **C.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand
- **D.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Author the `ActionBase` class with Custom Actions SDK, package & sign the `.cab` with a trusted certificate, upload to Custom actions in Portal, and package in a Solution. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.
- **B:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).
- **C:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.
- **D:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.

</details>

### Q021 (`E4Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

Plant IT creates an Azure DevOps CI/CD pipeline using an Entra **Application User (Service Principal)** to import Managed RPA solutions and own parent cloud flows. What Dataverse and Windows account model is required so unattended VMs still sign into Windows?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The Service Principal owns the cloud flows/solution deployment in Dataverse, while the `Desktop flows` connection binds to an interactive AD/Entra Windows service account for VM login. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q022 (`E4Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

When an unattended desktop flow fails on a locked plant VM, how can an authorized RPA support engineer visually inspect the exact Win32 popup state at the moment of failure without logging into the VM via RDP?

- **A.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Inspecting the failed run under `Monitor -> Desktop flow runs` in Power Automate portal surfaces the action error details and failure screenshot telemetry (when configured). [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.

</details>

### Q023 (`E4Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

Before reading press cycle counts from a Win32 HMI window, the bot must pause ONLY until the label `'Cycle Complete'` appears inside that window (up to a 45-second timeout). Which PAD action implements this event-driven gate?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Wait for window content` blocks only until the target UI element or text appears in the window and throws a timeout error if 45 seconds elapse. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q024 (`E4Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

An automotive plant schedules unattended night-shift MRP reconciliation bots on signed-out Windows VMs via a cloud flow. Order the four unattended execution steps correctly.

- **A.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **B.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically
- **C.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse
- **D.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Target single-session VMs must have all human sessions signed out so Power Automate can create a background Windows session, run the bot, and sign out automatically. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **B:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.
- **C:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.
- **D:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.

</details>

### Q025 (`E4Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

An automotive accounts-payable group deploys the Microsoft Document Automation Toolkit for supplier freight invoices. Select the accurate four-stage runtime workflow.

- **A.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **B.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email
- **C.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows
- **D.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Intake cloud flows capture email PDFs, AI Builder Document Processing scores extracted fields, clerks validate low-confidence bills in Canvas Validation Station, and verified Dataverse rows trigger ERP posting. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **B:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.
- **C:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.
- **D:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.

</details>

### Q026 (`E4Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

A manufacturing plant wants 6 concurrent unattended desktop flows running simultaneously on a single powerful on-premises VMware VM. Which Windows OS edition and role must be installed on that VM?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Windows Server** (2019/2022/2025) with the **Remote Desktop Session Host (`RDSH`)** role and RDS CALs enables multiple simultaneous unattended bot sessions on one VM. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **C:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q027 (`E4Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

A 280-action MES desktop flow separates `Open_Terminal`, `Sync_Schedule`, and `Close_Terminal` into dedicated Subflows invoked from `Main` via `____` (`Run subflow`). Why does modularizing into Subflows improve maintainability?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Subflows break complex monolithic scripts into reusable, independently testable routines invoked via `Run subflow` and `Exit subflow` over shared flow variables. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **C:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.

</details>

### Q028 (`E4Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

A plant RPA developer leaves on vacation and wants a teammate to be able to edit selectors, publish updates, view run history, and share their solution desktop flow. Which Desktop flow permission must be granted?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Granting **Co-owner** permission on the Desktop flow gives the teammate full edit, save, delete, run-history, and sharing privileges. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.

</details>

### Q029 (`E4Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

VoltEdge’s desktop bot communicates with a legacy Windows COM DMM (`CreateObject("Keysight.DMM")`) via `Run VBScript` and checks `If %____% <> ""` (`%ScriptError%`) to detect COM exceptions. Which scripting action applies?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run VBScript` automates Windows COM servers locally and populates `%VBScriptOutput%` and `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Correct — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q030 (`E4Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

VoltEdge’s cell-grading telemetry webhook fires bursts of 80 requests per minute, and downstream MES database pools allow at most `20` simultaneous cloud flow runs (`Concurrency Control = On`, `Degree of Parallelism = ____`). Which setting enforces that cap?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting trigger `Concurrency Control` (`Degree of Parallelism = 20`) caps active concurrent runs at 20 while queuing excess webhook deliveries cleanly. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).

</details>

### Q031 (`E4Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A supplier portal renders interactive SVG weld-inspection diagrams where clicking an SVG node requires dispatching `document.querySelector('svg g[data-weld="W14"]').dispatchEvent(new MouseEvent('mousedown'))` inside the open Edge tab. Which PAD action runs this DOM script?

- **A.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { ... }` directly inside the live browser tab’s DOM. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q032 (`E4Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Shop-floor operators use a Power Apps Canvas screen to scan a skid barcode and invoke an Instant cloud flow via `PrintSkidTag.____(lblBarcode.Text)`. Which integration pattern connects the Canvas app to Power Automate?

- **A.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **B.** Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Canvas apps invoke solution-aware Instant cloud flows via the Power Apps (V2) trigger (`FlowName.Run(...)`). [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **B:** Correct — Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

### Q033 (`E4Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A cloud flow splits a newline-delimited CSV string (`PartNo,Qty,Bin`) using `split(outputs('CSV_Text'), '\n')` and parses optional JSON metadata safely via `coalesce(...)`. Which WDL expression family handles this?

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Built-in WDL string and JSON functions (`split()`, `skip()`, `json()`, `coalesce()`) parse delimited text and optional JSON properties in cloud flows. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q034 (`E4Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

A plant shift-handover cloud flow parses a JSON array of downtime events and emails shift superintendents a formatted HTML table embedded directly in the Outlook email body. Which two Data Operations build this cleanly? Select two.

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs
- **E.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). `Parse JSON` validates and types the downtime payload while `Create HTML table` renders the array into an HTML `<table>` for the email body. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.
- **E:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.

</details>

### Q035 (`E4Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

Warranty analysts want a cloud flow to read unstructured dealer repair narratives and extract structured entities (`PartCode`, `FailureSymptom`, `Mileage`) or generate a standardized root-cause summary via GPT instructions. Which AI Builder option fits generative prompt extraction?

- **A.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **B.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **C.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **D.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). AI Builder `Create text with GPT using a prompt` (`AI Prompts`) extracts structured JSON or summaries from unstructured repair text using custom instructions. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Correct — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **B:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **C:** Incorrect — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **D:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.

</details>

### Q036 (`E4Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

An assembly-line team lead triggers a desktop bot on their own unlocked shop-floor PC, scans two physical part labels when prompted by the bot, and reviews the printed KanBan card. Proposed solution: Configure the run in `Unattended` mode on that active unlocked PC. Will `Unattended` mode work while the team lead is actively logged in?

- **A.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — an active signed-in operator interacting with prompts requires **Attended** mode (`Unattended` mode fails on active single-session PCs and forbids human prompts). [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **B:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Correct — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q037 (`E4Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

An automotive security team allows cloud `HTTP` actions in `Env-Plant-RPA-Prod` ONLY to call `https://mes.kestrelcastings.com/*` and `https://SAP-apim.kestrelcastings.com/*`, denying all external internet hosts. Where do you configure these host patterns?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure **Connector endpoint filtering** for the `HTTP` connector (and **Custom connector URL patterns**) inside the environment’s Power Platform DLP policy. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q038 (`E4Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

Eight manufacturing parent cloud flows invoke a shared solution Child Cloud Flow `Notify_Plant_Andon` passing `PlantId`, `LineCode`, and `Severity`. Which response action at the end of `Notify_Plant_Andon` returns `AckTicketId` to the calling parent flow?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Respond to a Power App or flow` (or the HTTP `Response` action) returns typed synchronous output parameters from a Child Cloud Flow to its parent. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q039 (`E4Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

In a cloud flow, you have `Scope_Try`, `Scope_Catch` (`Configure run after`: failed/skipped/timed out), and `Scope_Finally` (which must ALWAYS run to release a plant lock whether `Scope_Catch` ran **or** was skipped because `Scope_Try` succeeded!). Which boxes must be checked in `Scope_Finally`’s `Configure run after`?

- **A.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). For a `Finally` Scope placed after `Scope_Catch` to run in both success and failure paths, check `is successful` **and** `is skipped` (plus `has failed`/`has timed out` if needed) on `Scope_Finally`. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.

</details>

### Q040 (`E4Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A manufacturing RPA lead is assigning triggers across plant automations. Which two requirements map cleanly to an **Automated** cloud flow and an **Instant** cloud flow respectively? Select two.

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Automated cloud flow triggered asynchronously by an external connector event
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **E.** Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Reacting automatically to a new SharePoint quality certificate is `Automated`, while firing on demand when a line supervisor presses a tablet button is `Instant`. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Correct — Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **E:** Correct — Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).

</details>

### Q041 (`E4Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

A plant RPA engineer is repairing a Win32 gage-calibration selector that broke because the window caption includes a changing lot number (`GageCal - Lot #884920`). Select the resilient four-step Selector Builder workflow.

- **A.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs
- **B.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors
- **C.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **D.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Open Selector Builder, uncheck or replace the volatile lot suffix with `Starts with` / `Regex` / `%LotNumber%`, add a fallback selector, and validate across lots. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.
- **B:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).
- **C:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **D:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.

</details>

## Case Study Vignette — VoltEdge Battery Systems

> [Scenario: VoltEdge Battery Systems runs high-frequency cell-grading cloud and desktop automations. Cloud flows enable `Trigger Concurrency Control = 20` and `Secure Outputs` on battery telemetry keys, while desktop flows invoke `Run VBScript` and `Run PowerShell script` actions to query local COM serial testers and capture `%ScriptError%`.]

### Q042 (`E4Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — VoltEdge Battery Systems: VoltEdge also receives PDF supplier certificates of analysis by email that require AI Builder extraction plus lab-chemist review in a Canvas Validation Station when purity fields fall below `95%` confidence. Which Microsoft solution template fits?

- **A.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **B.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Document Automation Toolkit provides email ingestion, AI Builder Document Processing, Dataverse storage, and the Canvas Validation Station app. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **B:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q043 (`E4Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — VoltEdge Battery Systems: Alongside `Run VBScript` and `Run PowerShell script` (`%ScriptError%`) for COM serial testers, VoltEdge’s desktop bot reads a calibration Win32 window whose title changes per cell chemistry (`CellGrader - [LFP-Batch-99]`). How should its UI selector be configured?

- **A.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Parameterizing the selector in Selector Builder with `Starts with` / `Regex` or `%BatchChemistry%` keeps the Win32 selector stable across battery chemistries. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q044 (`E4Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — VoltEdge Battery Systems: VoltEdge’s bot posts raw JSON cell-grading arrays from the shop-floor PC to a local plant historian via `Invoke web service` (`Content-type: application/json`, `Encode request body = ____`). What setting keeps the JSON payload intact?

- **A.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Switching `Encode request body` to `Off` in `Invoke web service` sends valid unencoded raw JSON to the plant historian. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q045 (`E4Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

A stamping-plant desktop bot parses a pipe-delimited (`|`) schedule file into a Datatable, evaluates an XPath query against a local `MachineConfig.xml`, and converts a `%CustomObject%` summary into a JSON payload. Which three PAD capabilities cover this? Select three.

- **A.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **E.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **F.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, F` (`CSV: 1,3,6`)

Correct answers: A, C, and F (are correct). `Read from CSV file` (custom delimiter `|`) into a `Datatable`, `Read XML from file` + `Execute XPath expression`, and `Convert custom object to JSON` handle all three formats natively. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **E:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **F:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.

</details>

### Q046 (`E4Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

When multiple DLP policies apply to the same Power Platform environment, one policy classifies a Custom Connector in `Business` while a second overlapping policy classifies that same Custom Connector in `Blocked`. Which classification wins?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). When multiple DLP policies apply to an environment, **the most restrictive policy always wins**, meaning `Blocked` overrides `Business`. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.

</details>

### Q047 (`E4Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

ForgeLine’s bots interact with both an `IBM 5250` AS/400 terminal screen and a modern WPF quality app whose button AutomationIds vary slightly across two vendor versions (`btnSave` vs `btnCommitSave`). Which two PAD features provide reliable automation? Select two.

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **E.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Native Terminal emulation automates `IBM 5250` fields accurately, while multiple fallback selectors (or `Regex` operators) on a single UI element handle both WPF button versions. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **E:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.

</details>

### Q048 (`E4Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

A plant release pipeline failed to apply updated selector changes in Production because a contractor previously opened PAD Designer connected to Production and saved an ad-hoc edit. Which two ALM remedies prevent and fix this? Select two.

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **E.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Clear the contractor’s Unmanaged override via `Solution Layers -> Remove active customizations` and restrict Production exclusively to automated Managed Solution upgrades. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **C:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **E:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q049 (`E4Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A desktop flow loops over `%LotList%` with `For each`, and as soon as it locates the target urgent lot `%CurrentLot == TargetLot%`, it processes that single lot and must immediately break out of the `For each` loop without scanning the remaining 900 lots. Which PAD action breaks out?

- **A.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **B.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **C.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **D.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Exit loop` immediately terminates the enclosing `For each` / `Loop` / `Loop condition` and continues at the action following `End`. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **B:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **C:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **D:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.

</details>

### Q050 (`E4Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Ten quality-lab cloud flows call `Run a flow built with Power Automate for desktop` at 06:00 targeting a Machine Group of **5 single-session Windows 11 VMs**. How many desktop flows execute simultaneously at 06:00, and what happens to the remaining 5?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Five runs execute concurrently (one per healthy single-session VM in the Machine Group) while the remaining 5 wait safely in the Machine Group Run Queue for the first free VM. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q051 (`E4Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A plant workstation bot needs to parse binary CAN-bus log files using an existing local Python 3 script and capture stdout in `%PythonOutput%`. Proposed solution: Use `Run Python script` (or invoke `python.exe` via `Run PowerShell script` / `Run DOS command` for Python 3.11+ virtual environments) and inspect `%ScriptError%`. Is this supported in Power Automate for desktop?

- **A.** Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation
- **B.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — PAD provides `Run Python script` natively (for supported Python versions) as well as `Run DOS command` / `Run PowerShell script` to invoke custom virtual-environment Python interpreters. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Correct — `Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.
- **B:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **C:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

### Q052 (`E4Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

An RPA developer wants to test how a parent cloud flow’s retry and Teams escalation behave when a supplier API returns `HTTP 500 Internal Server Error`, **without** taking the supplier’s UAT server offline. Which feature mocks that response?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling **Static Result** on the cloud action returns a configured `500` status code and mock error body during test runs. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **D:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.

</details>

### Q053 (`E4Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

Proposed solution: Store the Production AS/400 admin password inside a plain `Text` Dataverse Environment Variable so any maker with `Basic User` read rights on `EnvironmentVariableValue` can read it. Does this satisfy Microsoft credential security guidance?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — never store secrets in plain `Text` Environment Variables; use **Power Automate Credentials** backed by Azure Key Vault / CyberArk or **Secret** Environment Variables backed by Key Vault. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q054 (`E4Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow `HTTP` GET request to a supplier portal intermittently fails with `HTTP 429 Too Many Requests`. Proposed solution: Configure `Retry Policy` as `Exponential Interval` with `Count = 4` and `Interval = PT10S`. Does this respect rate-limiting best practices?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — `Exponential Interval` retry policies automatically honor `Retry-After` headers and back off progressively on `429` and `5xx` responses. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.

</details>

### Q055 (`E4Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

In a Custom Actions SDK C# class, complete the attribute exposing a calculated checksum back into a PAD variable: `[____(Order = 1)] public string FrameCrc { get; set; }`. Which SDK mechanism applies?

- **A.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `[OutputArgument]` on an `ActionBase` property surfaces a typed output variable in Power Automate for desktop Designer. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **B:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.

</details>

### Q056 (`E4Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A web-based Kanban board uses dynamic React class hashes (`class="Card_x89a1"`), while stable ARIA attributes remain `<div role="listitem" aria-label="Press-04">`. Complete the resilient CSS selector: `div[role="listitem"][____="Press-04"]`. Which DOM design applies?

- **A.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). CSS attribute selectors targeting semantic `role` and `aria-label` attributes remain resilient when CSS-module hashes recompile. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q057 (`E4Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

Kestrel’s Custom Connector also executes C# code (`public class Script : ____`) to flatten deeply nested MES XML/JSON payloads before returning them to cloud flows. Which two constraints govern Custom Connector C# code? Select two.

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **E.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Custom Connector code inherits `ScriptBase` (`ExecuteAsync()`), must finish within `5 seconds` (`<= 1 MB` file size), and operates alongside connector OAuth 2.0 / API Key auth. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.
- **C:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **E:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q058 (`E4Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

An automotive EDI translator passes an XML `DELFOR` delivery forecast into a cloud flow, and you extract all `<PartNumber>` values using `xpath(____(triggerBody()?['XmlText']), '//PartNumber/text()')`. Which WDL conversion function wraps `triggerBody()?['XmlText']`?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `xml()` converts the UTF-8 XML string into an XML object required by the outer `xpath()` function. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.

</details>

### Q059 (`E4Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

When deploying `PlantMES_Managed.zip` across three regional Production environments (`US-Prod`, `DE-Prod`, `JP-Prod`), how does the exact same `.zip` artifact point to each country’s local Machine Group and AS/400 hostname?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Per-environment deployment settings bind each target environment’s Connection References (`Desktop flows` Machine Group + Credential) and Environment Variables (`AS400Host`) at import. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.

</details>

### Q060 (`E4Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

What is the critical difference between importing a Managed Solution with **Upgrade** (`Stage for upgrade` -> `Apply upgrade`) versus **Update** when you removed a deprecated desktop flow in v3.0?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Managed **Upgrade** deletes components present in v2.0 that were removed in v3.0, whereas Managed **Update** leaves orphaned v2.0 components behind in Production. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q061 (`E4Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

When a stamping press PLC logs a quality hold in Dataverse, an automation must notify plant quality engineers in Teams and then enter hold codes into an `IBM 5250` AS/400 terminal and a legacy Win32 gage app. Which pattern fits best?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow
- **C.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **D.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A hybrid cloud + unattended desktop flow architecture pairs Dataverse triggers and Teams approvals in the cloud with terminal and Win32 UI automation on bot VMs. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.
- **C:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **D:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.

</details>

### Q062 (`E4Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Twelve unattended bots across three stamping plants pull 15,000 supplier EDI 810 invoices from a central pool where items must track SLA deadlines, prevent duplicate `InvoiceKey` entries, and expose throughput metrics in Automation Center. Which feature should you design?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse Work Queues provide centralized multi-bot item leasing, `Unique reference` deduplication, `ExpiresOn` SLAs, and native queue telemetry. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.

</details>

### Q063 (`E4Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

A tier-1 supplier exposes an internal REST warranty API documented with an OpenAPI (`swagger.json`) file. Which two artifacts let cloud flows in a Solution invoke that API cleanly across Dev, Test, and Prod? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **E.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Create a solution-aware **Custom Connector** from the OpenAPI file and reference it through a **Connection Reference**. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **E:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q064 (`E4Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

VoltEdge’s security team requires battery-calibration signing keys to stay encrypted in Key Vault and redacted across both cloud Run History and PAD variable logs. Select the four-step implementation sequence.

- **A.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log
- **B.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing
- **C.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step
- **D.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Key Vault-backed Credentials/Secret Env Vars, Cloud `Secure Inputs/Outputs`, and PAD `Sensitive` variable flags prevent secret exposure across logs. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.
- **B:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.
- **C:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.
- **D:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.

</details>

### Q065 (`E4Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

A plant VM registered via `Power Automate machine runtime` shows status `Offline` in Power Automate portal after a Windows update stopped its local background Windows service (`____`). Restarting the `Power Automate service` (`UIFlowService`) and checking outbound HTTPS `443` restores connectivity under which architecture?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate machine runtime runs `UIFlowService` locally and connects directly over outbound HTTPS `443` (`*.servicebus.windows.net` / Power Platform endpoints) without legacy gateways. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Correct — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q066 (`E4Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

An environment security matrix separates infrastructure admins who register bot VMs from solution makers who only bind flows to existing shared Machine Groups. Which two built-in Dataverse security roles map to those two personas? Select two.

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **E.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). `Desktop Flows Machine Owner` allows registering/owning machines, while `Desktop Flows Machine User` (plus `User` share on the Machine Group) lets makers run flows on shared pools. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **E:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.

</details>

## Case Study Vignette — ForgeLine Stamping Corp

> [Scenario: ForgeLine Stamping Corp automates legacy green-screen AS/400 (`IBM 5250`) shop-floor schedules alongside modern web supplier portals. Bots connect via native Terminal Emulation actions, parse fixed-width & CSV production schedules into Desktop Datatables (`%ScheduleTable[row][col]%`), and filter defective lot rows without Excel installed.]

### Q067 (`E4Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — ForgeLine Stamping Corp: Which Power Automate for desktop capability should ForgeLine Stamping Corp use to read and update shop-floor schedules on its `IBM 5250` AS/400 green-screen host?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop’s native Terminal emulation actions connect directly to `IBM 5250` AS/400 hosts and address fields by row/column coordinates. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **D:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q068 (`E4Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — ForgeLine Stamping Corp: How should ForgeLine package its AS/400 terminal desktop flows, supplier web flows, Connection References, and Environment Variables so all three stamping plants receive governed Managed upgrades?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Authoring all flows, Connection References, and Environment Variables inside a Dataverse Solution with a custom publisher enables clean Managed upgrades across plants. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q069 (`E4Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — ForgeLine Stamping Corp: After filtering `%ScheduleTable%` (`%ScheduleTable[row][col]%`) in memory via `Filter data table` without Excel installed, ForgeLine’s producer enqueues defective lot rows into a Dataverse Work Queue. How do plant bots dequeue and complete each lot safely?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Bots execute `Process work queue items` to atomically lease `Queued` lots (`Processing`) and call `Update work queue item` (`Processed` / exception) upon completion. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q070 (`E4Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

An automotive RPA lead is establishing engineering standards for testing and configuration management across Dev, UAT, and Prod. Which three capabilities belong in the standard? Select three.

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **E.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **F.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, E` (`CSV: 1,2,5`)

Correct answers: A, B, and E (are correct). Dataverse `Environment Variables` / JSON config files, PAD Designer debugging (`Breakpoints`, `Run from here`, `Run delay`), and cloud `Static Result` mocking form the core testing/config toolkit. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **E:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **F:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q071 (`E4Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Quality inspectors use a **Model-driven** Non-Conformance Report (`NCR`) app and want an automated cloud flow to fire ONLY when `DispositionStatus` changes on the `msdyn_ncr` table (`Select columns = ____`). Which integration pattern minimizes unnecessary runs?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Using Dataverse’s `When a row is added, modified or deleted` trigger with `Select columns` (`cr_dispositionstatus`) ensures the cloud flow triggers only when that specific column changes. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Correct — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q072 (`E4Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

An automotive OEM wants supplier ASN (Advance Shipping Notice) rows added to Microsoft Dataverse to trigger a cloud REST validation against an ERP API immediately without maintaining desktop VMs. Which flow architecture should you select?

- **A.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A headless Automated cloud flow using Dataverse and HTTP/Custom Connectors processes API-to-API integrations with low latency and zero VM footprint. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.

</details>

### Q073 (`E4Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

An automotive supplier operates three legacy interfaces: a Citrix-published Win32 CAD BOM viewer, an intranet supplier portal in Microsoft Edge, and a sealed HMI panel bitmap feed where no software agent can be installed. Which three interaction options match? Select three.

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **E.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **F.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E, F` (`CSV: 1,5,6`)

Correct answers: A, E, and F (are correct). The Power Automate agent for virtual desktops handles Citrix Win32 apps, the Edge browser extension drives live DOM elements, and image/OCR actions automate sealed bitmap feeds. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Correct — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **E:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **F:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.

</details>

### Q074 (`E4Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

When a plant MES modal dialog renders sluggishly under heavy CPU load, `Populate text field in window` occasionally fails on the first millisecond attempt but succeeds 2 seconds later. Which action-level PAD configuration handles this cleanly?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configuring `Retry action if an error occurs` (for example `3` times at `2`-second intervals) in the action’s `On error` policy absorbs transient UI rendering lag. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **D:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q075 (`E4Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

An automotive solution contains 8 cloud flows calling `SQL Server`, `Microsoft Dataverse`, and `Desktop flows`. Why does Microsoft recommend using **Connection References** inside the Solution rather than direct Connections?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Connection References decouple flow definitions from environment-specific credentials so Managed upgrades never turn flows off or create Unmanaged Active layers during rebinding. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q076 (`E4Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

A cloud flow receives 3,000 gage readings in a JSON array and must keep ONLY out-of-tolerance items (`@greater(item()?['deviationMm'], 0.05)`) in a single declarative step. Which Data Operation action should you use?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Filter array` evaluates the predicate across all 3,000 JSON elements in memory without `Apply to each` iteration overhead. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **C:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q077 (`E4Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A plant desktop bot reads stamped serial codes off a legacy Windows gage preview window using `Extract text with OCR` and the built-in Windows 11 German/English OCR language pack (`Engine = ____`). Which OCR configuration applies?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **C.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The `Windows OCR engine` in `Extract text with OCR` uses installed Windows language packs for fast local character recognition. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Correct — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **C:** Incorrect — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q078 (`E4Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

ForgeLine’s production-control host runs on an IBM i (`AS/400`) system over the `IBM 5250` terminal protocol. Which Power Automate for desktop action family automates green-screen fields without fragile screen-scraping OCR?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate for desktop’s Terminal emulation actions natively automate `IBM 5250`, `IBM 3270`, and `VT` terminal sessions with exact row/column field access. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q079 (`E4Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

An automotive CoE uses Dataverse Work Queues to decouple 24/7 supplier EDI cloud ingestion from plant bot maintenance windows. Which two capabilities do Work Queues provide out of the box? Select two.

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **E.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Cloud producers enqueue items with `Priority`, `Unique reference`, and `ExpiresOn` SLAs, while PAD consumers lease (`Process work queue items`), update, or `Requeue item with delay`. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **E:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q080 (`E4Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

A cloud flow reads legacy `.dbf` and SQL Server quality tables located on an isolated factory subnet with no inbound internet access. Which Microsoft component relays those cloud connector queries over outbound port 443?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). An **On-Premises Data Gateway** cluster establishes outbound Azure Relay TLS connections so cloud flows query factory SQL Server and File System data safely. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **D:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q081 (`E4Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Titan Drivetrain Assembly discovers a maker added `Run VBScript` and `Terminate process` to a desktop flow in an environment where a newly applied Desktop Flow DLP policy blocks the `VBScript` module. What occurs immediately?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate enforces Desktop Flow DLP by suspending the non-compliant desktop flow and blocking runs until `Run VBScript` is removed or DLP is adjusted. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q082 (`E4Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

Can a single registered Windows VM belong to **three different Machine Groups simultaneously** at the exact same moment inside one Power Platform environment?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No — a registered machine can belong to **at most one Machine Group at a time** (joining a new Machine Group removes it from its previous group). [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q083 (`E4Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

ForgeLine’s bot reads a production CSV into `%ScheduleTable%` (`Columns: LotId, PressNo, DefectCount`) without Excel installed and filters rows where `DefectCount > 0`. Complete the cell reference for `LotId` in row `%i%`: `%ScheduleTable[____]['LotId']%`. Which PAD feature applies?

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop `Datatable` variables index rows zero-based (`%ScheduleTable[i]['LotId']%`) and filter rows in memory via `Filter data table`. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q084 (`E4Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

An automotive DevOps engineer is configuring automated Managed Solution deployments from Dev to Production for three plant RPA solutions. Select the compliant four-step ALM sequence.

- **A.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs
- **B.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **C.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows
- **D.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Author inside an Unmanaged Dev Solution, clear Dev values & export Managed, confirm Prod Machine Groups/Credentials exist, and deploy Managed Upgrade binding stage references. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.
- **B:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **C:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.
- **D:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.

</details>

### Q085 (`E4Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow deserializes JSON `{"press":"P04","sensors":["Temp","Vibration"]}` via `Convert JSON to custom object` into `%PressInfo%`. How do you access `"Vibration"` in Power Automate for desktop percent notation?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `%PressInfo['sensors'][1]%` (or `%PressInfo.sensors[1]%`) combines `Custom object` property access with zero-based `List` indexing. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).

</details>

### Q086 (`E4Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Kestrel Precision Castings needs its Custom Connector to inject header `X-Plant-Routing: OH-02` on every outbound REST call without writing C# code. Which Custom Connector policy template should they add?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **D.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The codeless `Set HTTP header` **Policy template** adds or updates HTTP headers at runtime on selected operations. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **D:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.

</details>

### Q087 (`E4Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

An MES developer is building a solution cloud flow that dispatches an unattended `IBM 5250` schedule-sync desktop flow and writes `%SyncedLotCount%` into Dataverse. Choose the valid four-step sequence.

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod
- **C.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **D.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Declare Input/Output variables in the solution desktop flow, add `Run a flow built with Power Automate for desktop`, bind the Machine Group Connection Reference & Inputs, and consume Output tokens. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.
- **C:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **D:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.

</details>

### Q088 (`E4Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

While debugging a loop over 500 rows in Power Automate for desktop Designer, you toggle a red dot (`____`) on action #42 so execution pauses automatically whenever action #42 is reached, letting you inspect `%ScheduleTable%` in the Variables pane. Which Designer feature is this?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting a **Breakpoint** in Power Automate for desktop Designer pauses local test runs at the exact target action for live variable inspection and step-over (`F10`) debugging. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

### Q089 (`E4Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

An admin creates a tenant-level DLP policy blocking `HTTP` in `All environments except` `Env-Plant-RPA-Prod`, and creates a second environment-level DLP policy on `Env-Plant-RPA-Prod` placing `HTTP` and `Dataverse` in `Business`. Can flows in `Env-Plant-RPA-Prod` use `HTTP` with `Dataverse`?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — excluding `Env-Plant-RPA-Prod` from the restrictive tenant policy lets its dedicated environment DLP policy govern `HTTP` + `Dataverse` in `Business` (paired with endpoint filtering). [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

## Case Study Vignette — Titan Drivetrain Assembly

> [Scenario: Titan Drivetrain Assembly governs 45 production bots across three plants in Power Automate Portal (`Monitor -> Desktop flow runs` & `Machines`). Plant leads inspect step-level failure screenshots, reprioritize `Line-Down` runs to `High` + `Move to top` in the run queue, and audit Desktop Flow DLP policies before importing new solutions.]

### Q090 (`E4Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — Titan Drivetrain Assembly: Titan Drivetrain Assembly wants elastic unattended Azure VMs provisioned automatically from a custom plant VM image in Azure Compute Gallery whenever month-end inventory runs spike. Which feature should Titan deploy?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Attended run mode executing inside a signed-in user’s active desktop session
- **C.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate **Hosted Machine Groups** (`Hosted RPA`) auto-scale Azure bot VMs from custom images stored in **Azure Compute Gallery**. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **C:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **D:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q091 (`E4Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — Titan Drivetrain Assembly: Before importing new supplier RPA solutions into Production, Titan’s security team audits environment DLP rules to ensure `Run PowerShell script` and `Run DOS command` are blocked inside desktop flows. Which DLP capability governs this?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Desktop flow module and action DLP rules block prohibited PAD modules/actions and flag non-compliant desktop flows during governance checks. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **C:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q092 (`E4Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — Titan Drivetrain Assembly: When an urgent `Line-Down` bot run enters a Machine Group queue behind 30 `Normal` runs (and 2 other `High` runs), which portal Run Queue actions ensure the `Line-Down` run executes very next?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Applying `Change priority` -> `High` followed by `Move to top` in the Machine Group’s Run Queue moves the `Line-Down` run to position #1 ahead of all waiting runs. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.
- **C:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q093 (`E4Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Production support analysts need to trigger a parent cloud flow that runs an unattended bot on `MG-StampingBots`, without having permission to add rogue VMs to `MG-StampingBots`. How should machine access be scoped?

- **A.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Grant **User** (not `Co-owner`) permission on `MG-StampingBots` to the flow’s connection owner and expose the parent cloud flow via embedded `Run-only users`. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q094 (`E4Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

When configuring `Run a flow built with Power Automate for desktop` inside a cloud flow, which parameter determines whether Power Automate requires an active signed-in human desktop session versus signing into a background session automatically?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** `Run a flow built with Power Automate for desktop` action with Machine/Group connection, Run mode, & Inputs
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The `Run mode` parameter (`Attended - runs when you're signed in` vs `Unattended - runs on a machine that's signed out`) controls session execution behavior. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Correct — The Desktop flows connector bridges cloud flows to attended or unattended desktop flows, passing Input variables and returning Output variables.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q095 (`E4Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A parent cloud flow calculates elapsed minutes using WDL expressions and initializes a string variable `varPlantSummary` before appending line statuses. Why should `Append to string variable` inside `Apply to each` NOT run with high loop parallelism?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Shared cloud flow variables (`Set variable` / `Append to ... variable`) lock or interleave unpredictably across parallel `Apply to each` branches; use `Select` / `Join` for parallel array transforms. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.

</details>

### Q096 (`E4Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

A plant desktop flow wraps 10 `IBM 5250` terminal steps inside `On block error`. Proposed solution: Inside `On block error`, call `Get last error` (`%LastError%`), invoke subflow `Reconnect_5250_Session`, and set `Continue flow run` to `Go to end of block` (or retry block once). Does this handle transient terminal disconnects cleanly?

- **A.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — `On block error` catches any system exception across the wrapped terminal actions, captures `%LastError%`, runs session cleanup, and resumes execution predictably. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q097 (`E4Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow `HTTP` step invokes a synchronous CAD mesh validation API and must time out after 5 minutes (`____`) rather than waiting for the default 2-minute or long async timeout. Which ISO 8601 Timeout string specifies 5 minutes?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). ISO 8601 duration `PT5M` configures a 5-minute action Timeout in cloud flow action Settings (`P` + `T` time designator + `5M`). [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **D:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.

</details>

### Q098 (`E4Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

During supplier invoice posting, an AS/400 screen returns `ERR-PO-OVER-TOLERANCE: Invoice exceeds PO by 18%` (domain rule), whereas once a month the 5250 emulator crashes (`SystemException`). Which two handling strategies match these two cases? Select two.

- **A.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **B.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **E.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Route `ERR-PO-OVER-TOLERANCE` immediately as a Business Exception (`On hold` / buyer notification, zero UI retries), and recover emulator crashes via `On block error`. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **B:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **E:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q099 (`E4Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow fetches bill-of-materials items from an internal PLM REST API that caps each page at 500 items (`@odata.nextLink`) across 6,000 parts. Which `HTTP` action Settings configuration pulls all 6,000 parts automatically?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Turning `Pagination` `On` and setting `Threshold = 10000` in the `HTTP` action Settings retrieves all pages automatically. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q100 (`E4Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

An automotive IT engineer is onboarding eight identical Windows Server VMs into `MG-AssemblyBots` using Power Automate machine runtime. Place the registration steps in the proper order.

- **A.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests
- **B.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly
- **C.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **D.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create the Machine Group in Portal, register each VM to the target environment in Power Automate machine runtime, join the group with the group password/key, and bind Connection References with `User` access. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.
- **B:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.
- **C:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **D:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.

</details>
