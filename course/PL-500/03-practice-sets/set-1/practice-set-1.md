# Microsoft Exam PL-500: Practice Exam 1 — Banking, Mainframe 3270 & Mortgage Servicing RPA — Reviewer Study Key

**Theme:** Mainframe terminal emulation, Key Vault credentials, Document Automation Toolkit, dynamic selectors, and run queue priority  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E1Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

A bank’s RPA Center of Excellence is standardizing target-application interaction patterns across Windows desktops, web portals, green-screen hosts, and Citrix virtual apps. Which three capabilities align with Microsoft’s recommended architecture? Select three.

- **A.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **E.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **F.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, F` (`CSV: 1,3,6`)

Correct answers: A, C, and F (are correct). Native Windows UIA selectors, the Power Automate browser extension for live DOM access, and the Power Automate agent for virtual desktops on Citrix/RDP hosts provide resilient element-level automation. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Correct — UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **E:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **F:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.

</details>

### Q002 (`E1Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

A mortgage servicing architect is deploying the Microsoft Document Automation Toolkit to process thousands of emailed property-tax bills with human-in-the-loop verification. What is the correct end-to-end processing sequence?

- **A.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows
- **B.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **C.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream
- **D.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The Document Automation Toolkit ingests email attachments via cloud flows, runs AI Builder Document Processing, routes low-confidence items to the Canvas Validation Station, and exports verified Dataverse records. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.
- **B:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **C:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.
- **D:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.

</details>

### Q003 (`E1Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

A cloud flow receives a 2,000-element JSON array of daily ledger entries and must keep only debit rows while projecting `{AccountNumber, Amount}` in under 1 second without `Apply to each` variable bottlenecks. Which Data Operations pair should you use?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Filter array` followed by `Select` filters and reshapes JSON arrays in memory without slow loop-variable locking. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.
- **C:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q004 (`E1Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

An RPA developer is wiring a solution cloud flow to invoke an unattended wire-posting desktop flow and write its returned confirmation number into Dataverse. Which step sequence configures this cleanly?

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **C.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod
- **D.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Solution cloud flows exchange data with desktop flows through declared PAD Input/Output variables and the `Run a flow built with Power Automate for desktop` action. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **C:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.
- **D:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.

</details>

### Q005 (`E1Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A retail bank wants to synchronize newly approved loan rows from Microsoft Dataverse to a cloud-hosted treasury REST API with sub-second event latency and zero Windows VMs. Which automation type should you design?

- **A.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces
- **B.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). When both source and target systems expose modern cloud connectors or REST APIs, a headless Automated cloud flow eliminates VM maintenance and Windows session overhead. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.
- **B:** Correct — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q006 (`E1Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A desktop flow on a treasury workstation must query local Windows certificate thumbprints in `Cert:\LocalMachine\My` via WMI/.NET cmdlets and capture any runtime error into `%____%` (`%ScriptError%`). Which scripting action should you design?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **C.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run PowerShell script` executes local PowerShell cmdlets and .NET classes on the Windows host while returning stdout and `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Correct — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **C:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q007 (`E1Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

In C# using the Power Automate Custom Actions SDK (`Microsoft.PowerPlatform.PowerAutomate.Desktop.Actions.SDK`), complete the property attribute exposing an input parameter in PAD Designer: `[____(Order = 1, Required = true)] public string SwiftBic { get; set; }`. Which SDK construct applies?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Classes inheriting `ActionBase` decorate public properties with `[InputArgument]` and `[OutputArgument]` before CAB packaging and code signing. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q008 (`E1Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

A producer cloud flow loads items into a Dataverse Work Queue while unattended desktop flows dequeue and finalize them. Which two capabilities belong to native Power Automate Work Queues? Select two.

- **A.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **E.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Cloud flows enqueue items with `Priority`, `Unique reference`, and `ExpiresOn`, while desktop flows lease items via `Process work queue items` and record `Processed` / `Generic exception` / `On hold` or `Requeue item with delay`. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **E:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q009 (`E1Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A nightly card-dispute pipeline ingests 18,000 cases at 01:00 UTC that must be worked across eight unattended VMs with per-item SLA expiration timestamps, deduplication keys, and automatic requeueing. Which feature should you include in the design?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dataverse Work Queues decouple producer ingestion from multi-bot consumer execution while tracking item priority, `Unique reference` deduplication, and `ExpiresOn` SLAs. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q010 (`E1Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

After submitting a wire batch in a Win32 client, confirmation takes anywhere from 1 second to 25 seconds depending on mainframe load. Which desktop flow pattern avoids both premature failures and wasteful fixed 30-second sleeps?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Wait for window content` (or `Wait for web page content`) resumes immediately as soon as the confirmation control renders and errors cleanly if the timeout expires. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q011 (`E1Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A compliance cloud flow must summarize lengthy unstructured borrower hardship letters into a 3-bullet executive synopsis using generative AI instructions and safety filters. Which AI Builder capability fits best?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **C.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **D.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). AI Builder `Create text with GPT using a prompt` (`AI Prompts`) applies governed generative language models to summarize or transform unstructured text. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **C:** Incorrect — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **D:** Correct — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.

</details>

### Q012 (`E1Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

Inside Power Automate for desktop, a developer creates a variable `%WireConfirmationId%` inside `Main`, runs the flow from a cloud flow, and notices `WireConfirmationId` is missing from the cloud flow’s dynamic outputs. What must the developer configure?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Local variables inside `Main` remain private to the desktop run; only explicit `Output` variables (`Input/output variables` pane) return values to calling cloud flows. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Correct — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.

</details>

### Q013 (`E1Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

A banking identity architect is separating non-interactive cloud automation identities from interactive Windows bot session logins. Which two identity rules apply in Power Automate RPA? Select two.

- **A.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **B.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **E.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Headless cloud flows and ALM pipelines can run under a Microsoft Entra Service Principal, whereas unattended Windows OS desktop sessions require an interactive AD/Entra user account alongside least-privilege RPA Dataverse roles. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **B:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **E:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q014 (`E1Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

A DevOps engineer needs to register new Windows VMs into a UAT environment and create a Machine Group, without receiving full `System Administrator` rights across all business tables. Which built-in Dataverse security role grants machine registration/ownership?

- **A.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **B.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **C.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Desktop Flows Machine Owner` grants privileges to register machines and create/manage Machine Groups, whereas `Desktop Flows Machine User` allows running flows on shared machines. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **B:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **C:** Incorrect — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q015 (`E1Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

When a fatal vault connectivity check fails inside the `Login_Portal` subflow, the bot must abort the entire desktop flow immediately and surface error code `VAULT_DOWN` to the calling cloud flow rather than merely returning to `Main`. Which action should you use?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Stop flow` configured `With error message` terminates the entire desktop flow run immediately and reports failure details back to the parent cloud flow. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Correct — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **D:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.

</details>

### Q016 (`E1Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

A bank’s legacy core screen occasionally renders its `Submit Wire` button under an updated WPF toolbar hierarchy during phased branch rollouts. Which two Power Automate for desktop capabilities let one UI element handle both old and new layouts plus dynamic captions? Select two.

- **A.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **E.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Parameterized `%Variable%` / operator selectors handle dynamic captions, while multiple ranked fallback selectors on one UI element match both legacy and upgraded UI trees. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **E:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.

</details>

## Case Study Vignette — SummitVault ATM Logistics

> [Scenario: SummitVault ATM Logistics promotes RPA solutions from Dev through UAT to Production via Power Platform pipelines. Production enforces strict Desktop Flow DLP blocking PowerShell while allowing Excel and Web automation, and urgent cash-out dispatch bots must jump ahead of routine audit runs in the Machine Group Run Queue.]

### Q017 (`E1Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — SummitVault ATM Logistics: SummitVault ATM Logistics wants Microsoft to automatically provision and scale Azure unattended bot VMs up to 10 instances during holiday cash-demand peaks from a golden VM image. Which capability should they configure?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Hosted Machine Groups (`Hosted RPA`) automatically provision and scale Azure bot VMs from default images or custom Azure Compute Gallery images. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q018 (`E1Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — SummitVault ATM Logistics: How does SummitVault ATM Logistics block `Run PowerShell script` in Production while continuing to allow `Excel` and `Browser automation` actions in desktop flows?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Desktop flow module and action DLP settings in Power Platform Admin Center block `PowerShell` actions while leaving `Excel` and `Browser` modules allowed. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q019 (`E1Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — SummitVault ATM Logistics: Twenty-five routine `Normal`-priority audit runs are waiting in the Machine Group queue when an emergency ATM cash-out run is queued. Which two portal Run Queue operations ensure the emergency run executes next?

- **A.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Setting `Change priority` to `High` and invoking `Move to top` in the Machine Group Run Queue places the urgent run ahead of all waiting queued runs. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.

</details>

### Q020 (`E1Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

A developer hardcodes `DEV-BOT-VM01` and a developer’s personal domain password directly inside a flow exported to Production. Proposed solution: Replace personal credentials with environment-specific Power Automate `Credentials` backed by Azure Key Vault and bind the `Desktop flows` Connection Reference to the Prod Machine Group. Does this satisfy enterprise credential isolation?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — Key Vault-backed Power Automate Credentials paired with stage-bound Connection References isolate Dev, UAT, and Prod secrets and machines cleanly. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.

</details>

### Q021 (`E1Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

A treasury desktop flow must read structured tables out of digital PDF statements, parse a local XML routing directory via XPath, and deserialize an API response string into a `%CustomObject%`. Which three Power Automate for desktop action capabilities cover these tasks? Select three.

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **D.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **F.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, D` (`CSV: 1,3,4`)

Correct answers: A, C, and D (are correct). `Extract tables from PDF`, `Read XML from file` + `Execute XPath expression`, and `Convert JSON to custom object` (`%CustomObject%`) handle all three local parsing formats natively. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **D:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **F:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q022 (`E1Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

A network engineer asks whether the bank must deploy an On-Premises Data Gateway cluster solely to register Windows 11 RPA bot VMs to Power Automate cloud. Which component actually handles modern machine registration?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The `Power Automate machine runtime` app connects VMs directly to Power Automate cloud over outbound HTTPS without requiring the legacy On-Premises Data Gateway. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Correct — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.

</details>

### Q023 (`E1Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

A parent wire-orchestration cloud flow contains seven API and desktop actions that need centralized `Try` / `Catch` error alerting whenever any step fails, is skipped, or times out. How should you structure the cloud flow?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Placing actions in a `Try` `Scope` followed by a `Catch` `Scope` with `Configure run after` set to `has failed`, `is skipped`, and `has timed out` provides structured cloud exception handling. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.

</details>

### Q024 (`E1Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Fourteen cloud flows trigger the same unattended desktop flow simultaneously against a single Windows 11 Enterprise VM. Proposed solution: Rely on default single-session Windows 11 queuing so all 14 desktop runs execute in parallel at the exact same second on that one VM. Does this meet the simultaneous execution goal?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Single-session Windows 10/11 VMs serialize queued runs one at a time; true concurrent unattended sessions on one host require Windows Server with Remote Desktop Session Host (`RDSH`) or multiple VMs in a Machine Group. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q025 (`E1Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

A bank’s private SQL Server 2022 treasury database sits inside an isolated on-premises VLAN with no public endpoints, and a **cloud flow** must run stored procedures against it. Which infrastructure component bridges the cloud flow securely?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Cloud flows connect to private on-premises SQL Server, File System, and SharePoint Server resources through a clustered On-Premises Data Gateway over outbound TLS. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.

</details>

### Q026 (`E1Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

An escrow operations team receives wire confirmations in Exchange Online, requires a manager approval in Microsoft Teams, and then must key approved amounts into a 1998 Win32 ledger app that has no database or API access. Which architecture should you recommend?

- **A.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow
- **B.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **C.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **D.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Combining an Automated cloud flow (Exchange trigger + Teams approval) with an unattended desktop flow cleanly bridges modern APIs and legacy Win32 user interfaces. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.
- **B:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **C:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **D:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q027 (`E1Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

Six identically configured treasury VMs belong to `MG-WireBots`. When 30 unattended wire flows trigger at 08:00, how does Power Automate distribute the runs across the six VMs?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A Machine Group automatically queues incoming runs and dispatches each next run to the first available healthy machine in priority-then-FIFO order. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q028 (`E1Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

Before connecting to the live SWIFT gateway, a developer wants to unit-test a cloud flow’s `Catch` Scope by forcing the `HTTP` action to return `HTTP 429 Too Many Requests` and a `Retry-After: 30` header offline. Which cloud flow testing feature achieves this?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Static Result` mocks custom HTTP status codes, headers, and JSON bodies on cloud flow actions without sending live network traffic. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q029 (`E1Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

A bank provisions Azure Virtual Machines running Windows 11 Enterprise (single-session) for unattended wire bots, but runs fail with `Couldn't sign in: another user is currently signed in` after an admin closes their Remote Desktop window without signing out. What fixes this?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **C.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Closing RDP `[X]` leaves a disconnected active human session on single-session Windows 11; admins must fully `Sign out` (or enable Windows Server RDSH multi-session) for unattended sign-in. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **C:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q030 (`E1Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A maker imports a new Custom Connector into Production where the environment DLP policy sets the Default group for new connectors to `Blocked`. What must an admin do after reviewing the connector’s host URL so flows can pair it with `Dataverse` (`Business`)?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Moving the approved Custom Connector into the `Business` data group (alongside host endpoint rules) allows flows to combine it with `Dataverse`. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q031 (`E1Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

When adding a seventh VM to `MG-WireBots`, automated UI runs fail ONLY when dispatched to VM #7 because that VM was built without the treasury Win32 client and uses `150%` display scaling while VMs 1–6 use `100%`. What Machine Group rule was violated?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Because any queued run can land on any machine in a Machine Group, all member VMs must share identical target app versions, fonts, and compatible display scaling. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q032 (`E1Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A cloud flow parses optional borrower JSON fields where `middleName` is frequently omitted or `null`, so you write `____(body('Parse_JSON')?['middleName'], '')`. Which WDL expression pattern safely parses JSON and supplies `''` when null?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **D.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `json()` parses stringified JSON payloads while `coalesce(body('Parse_JSON')?['middleName'], '')` safely handles missing or null keys. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **D:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q033 (`E1Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Eight unattended bots run `Process work queue items` simultaneously against the `NightlyWires` Dataverse Work Queue. How does Power Automate prevent two bots from processing the exact same wire item at the same time?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Process work queue items` atomically transitions the leased item’s status from `Queued` to `Processing`, locking it from other concurrent bots until updated or expired. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q034 (`E1Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

Inside Power Automate for desktop, `%LedgerTable%` is a Datatable with columns `AccountId` and `Balance`. Complete the percent expression that reads the `Balance` column of the first row: `%LedgerTable[____]['Balance']%`. Which zero-based Datatable pattern applies?

- **A.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **B.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop Datatables use zero-based row indexing (`%LedgerTable[0]['Balance']%`) alongside `Filter data table` and `Find or replace in data table`. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **B:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q035 (`E1Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

An integration architect is documenting the relationship between Custom Connectors, Connections, and Connection References in a Dataverse Solution. Which two design statements are accurate? Select two.

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **E.** Environment-specific Connection storing authenticated credentials for a connector

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). A Custom Connector defines the OpenAPI schema/auth contract for a REST API, while a Connection stores the concrete authenticated credentials in a specific environment. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **E:** Correct — A Connection holds the concrete OAuth token, API key, or Windows/Key Vault credential inside a single Power Platform environment.

</details>

### Q036 (`E1Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

An RPA developer is troubleshooting a 200-step desktop flow in Power Automate for desktop Designer alongside its parent cloud flow. Which three built-in testing and configuration capabilities are natively supported? Select three.

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **E.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **F.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, E` (`CSV: 2,4,5`)

Correct answers: B, D, and E (are correct). PAD `Breakpoints` / `Run from here` / `Run delay` / `Variables` pane, Cloud `Static Result` mocking, and Dataverse `Environment Variables` / JSON config files streamline RPA testing. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **E:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **F:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q037 (`E1Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

A bank’s CISO allows RPA bots in Production to automate Microsoft Excel and Edge browsers, but strictly forbids any desktop flow from executing `Run PowerShell script` or `Run DOS command`. Which governance control enforces this automatically?

- **A.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Desktop flow module and action DLP rules let Power Platform admins block specific PAD modules or individual actions (`Run PowerShell script`, `Run DOS command`) and suspend non-compliant flows. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.
- **B:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **D:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.

</details>

### Q038 (`E1Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow `HTTP POST` submits an unkeyed instant wire transfer to a legacy gateway that lacks idempotency keys, meaning any automatic retry risks double-sending funds. Proposed solution: Set the HTTP action’s `Retry Policy` to `None` and route failures to an exception Scope for human verification. Does this prevent duplicate automatic wire submissions?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Setting `Retry Policy` to `None` disables automatic retries on non-idempotent POST operations so uncertain network timeouts are verified once rather than duplicated. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q039 (`E1Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

An infrastructure engineer is onboarding four clean Windows Server VMs into a new load-balanced Machine Group in Production without deploying legacy gateways. Which four-step sequence completes registration?

- **A.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference
- **B.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly
- **C.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **D.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). VMs register directly via Power Automate machine runtime, join the target Machine Group using its password/recovery key, and get shared as `User` with Connection References. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.
- **B:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.
- **C:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **D:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.

</details>

### Q040 (`E1Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Underwriting officers using a Power Apps Canvas tablet app need a button that triggers a flow synchronously and displays the calculated debt-to-income ratio returned within 4 seconds: `Set(varDTI, LoanCheckFlow.____(txtLoanId.Text).dti)`. Which method completes the Power Fx call?

- **A.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **B.** Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Canvas apps invoke Instant cloud flows via the Power Apps (V2) trigger (`FlowName.Run(...)`) and receive synchronous values from `Respond to a Power App or flow`. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **B:** Correct — Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q041 (`E1Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow invokes a synchronous regulatory batch endpoint and must abort the HTTP action if no response arrives within 20 minutes: `Timeout = ____`. Which ISO 8601 duration setting enforces a 20-minute timeout?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Cloud flow action Timeouts use ISO 8601 duration format where `PT20M` denotes 20 minutes (`PT15M` = 15 minutes, `P1D` = 1 day). [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

## Case Study Vignette — Crestline Mortgage Servicing

> [Scenario: Crestline Mortgage Servicing receives 3,500 scanned PDF escrow tax bills per day in an Exchange shared mailbox. Invoices require AI Builder extraction with human review for <85% confidence scores via Document Automation Toolkit, followed by unattended browser entry where dynamic CSS IDs change on every portal reload.]

### Q042 (`E1Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — Crestline Mortgage Servicing: Which Microsoft starter solution gives Crestline Mortgage Servicing prebuilt email PDF ingestion, AI Builder extraction, Dataverse tracking, and a Canvas human review app for `<85%` confidence tax bills?

- **A.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The Document Automation Toolkit combines intake cloud flows, AI Builder Document Processing, Dataverse tables, and the Canvas Validation Station for low-confidence human review. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q043 (`E1Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — Crestline Mortgage Servicing: When entering verified escrow bills into the municipal web portal whose CSS `id` attributes regenerate on every page reload, how should the RPA developer configure the Web UI element?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Unchecking volatile dynamic `id` attributes in Selector Builder and matching stable attributes with `%Variable%` / `Contains` / `Regex` operators keeps selectors stable across reloads. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.

</details>

### Q044 (`E1Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — Crestline Mortgage Servicing: After portal entry, the unattended desktop bot posts a raw JSON receipt (`{"loanId":"991","paid":true}`) via `Invoke web service` (`Content-type: application/json`), but the server returns `HTTP 400 Invalid JSON`. Which action toggle must be turned `Off`?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History
- **C.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Invoke web service` enables `Encode request body` by default, URL-encoding `{` and `:`; turning `Encode request body` `Off` transmits valid raw JSON. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.
- **C:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q045 (`E1Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A trade-finance cloud flow receives scanned PDF commercial invoices from 60 vendor layouts and must extract line-item tables, totals, and per-field confidence scores before posting to Dataverse. Which Microsoft AI capability should you choose?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **D.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). AI Builder Document Processing extracts structured fields, tables, and confidence scores from multi-layout PDFs and images natively in cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **D:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.

</details>

### Q046 (`E1Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

When promoting a banking RPA solution across Dev, UAT, and Production, architects want cloud and desktop flows to switch cleanly from sandbox accounts to production accounts without opening or editing flow definitions. Which component enables this indirection?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Environment-specific Connection storing authenticated credentials for a connector
- **D.** Solution-aware Connection Reference decoupling flows from environment-specific Connections

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Connection References are solution-aware pointers inside flows that bind to environment-specific Connections during solution import. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — A Connection holds the concrete OAuth token, API key, or Windows/Key Vault credential inside a single Power Platform environment.
- **D:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.

</details>

### Q047 (`E1Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

A commercial lending desktop flow must enter borrower figures into an internal Windows Presentation Foundation (`WPF`) credit workstation installed locally on the bot VM. Which interaction method provides the highest reliability?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Windows UI Automation (`UIA`) binds directly to native WPF control trees and automation IDs rather than fragile screen coordinates or bitmap templates. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.

</details>

### Q048 (`E1Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

A bank’s fraud team needs relational storage for 400,000 structured dispute records with row-level business-unit security, native audit history, and automatic server-side flow triggers when status columns change. Which data store should you include?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Microsoft Dataverse custom/standard tables providing relational storage, security roles, and native triggers
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Microsoft Dataverse provides enterprise relational tables, row/column security roles, auditing, and native `When a row is added, modified or deleted` triggers. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Correct — Dataverse serves as the enterprise state store for Power Platform RPA metadata, Work Queues, audit logs, and business records.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q049 (`E1Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A security architect approves a Custom Connector to call `https://api.treasury.meridianfirst.bank/*` (`Order 1: Allow`), and wants all other hosts denied (`Order 2: ____`). Which DLP capability enforces host-level filtering on Custom Connectors and HTTP?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). DLP Connector endpoint filtering and Custom Connector URL pattern rules evaluate ordered host rules (`Allow https://api.treasury.meridianfirst.bank/*` followed by catch-all `*` `Deny`). [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q050 (`E1Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

When saving a parent cloud flow that calls `Run a Child Flow`, Power Automate displays an error stating the child flow must live in a solution and use embedded connections. Which two configurations resolve this? Select two.

- **A.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **E.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Both parent and child flows must reside in Dataverse Solutions, and the child flow’s `Run only users` settings must be set to `Use this connection` rather than `Provided by run-only user`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **E:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q051 (`E1Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

After a overnight wire run fails at 03:14 UTC, a support lead needs to see which VM in the Machine Group picked up the run, how long it waited in the queue, which exact PAD action failed, and the failure screenshot. Where in Power Automate portal should they look?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Monitor -> Desktop flow runs` and `Machines` (plus Automation Center) show queue wait times, host VM assignment, action-level durations/errors, and failure screenshots. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.

</details>

### Q052 (`E1Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

A desktop flow developer is hardening a flaky Win32 loan-servicing selector whose window title appends today’s date and random process ID (`LoanDesk - 2026-10-30 [PID 4412]`). Which sequence builds a resilient UI element?

- **A.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors
- **B.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field
- **C.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **D.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Stripping volatile PID/date fragments, using `Starts with` / `Contains` / `%Variable%` in Selector Builder, and adding fallback selectors eliminates UI drift failures. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).
- **B:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.
- **C:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **D:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.

</details>

### Q053 (`E1Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Multiple banking RPA teams need a proprietary IBAN checksum and HSM encryption step exposed as a reusable, DLP-governed drag-free toolbox action inside Power Automate for desktop Designer. What should you design?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **C.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Custom actions built with the .NET Framework Custom Actions SDK, packaged as signed `.cab` modules, and uploaded to Dataverse appear natively inside Power Automate for desktop Designer. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **C:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q054 (`E1Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

A wire-room architect is designing an overnight cloud-triggered desktop flow that signs into a locked treasury VM with zero human presence. In which exact order does unattended execution run end to end?

- **A.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **B.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text
- **C.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse
- **D.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Unattended runs require signed-out target VMs, connect via Machine/Group credentials, dynamically open a background Windows session, run the bot, and sign out afterward. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **B:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.
- **C:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.
- **D:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.

</details>

### Q055 (`E1Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A developer has only 12 daily CSV rows to rename in a single folder on one VM with no multi-bot scaling or item-level SLAs. Proposed solution: Provision a multi-stage producer/consumer Dataverse Work Queue architecture solely to rename the single local file. Is a Work Queue required for this scenario?

- **A.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Work Queues shine for decoupled, multi-bot, transactional item backlogs; simple single-file local operations run directly via built-in file/CSV actions without queue overhead. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **B:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q056 (`E1Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

A desktop flow calls an internal SOAP 1.1 check-clearing service exposed solely via an intranet `.wsdl` contract (`https://clearing.intra/CheckService?wsdl`). Which Power Automate for desktop action invokes typed WSDL operations natively?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Invoke SOAP web service` imports WSDL definitions and constructs compliant XML SOAP requests directly from the bot workstation. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Correct — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q057 (`E1Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

Six banking parent cloud flows share identical SWIFT sanction-screening logic inside a Dataverse Solution. When you extract that logic into a reusable Child Cloud Flow, which final action is required so the parent flow doesn’t hang waiting for completion?

- **A.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Solution Child Cloud Flows must terminate with `Respond to a Power App or flow` or HTTP `Response` to return synchronous control and outputs to the parent flow. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q058 (`E1Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

A bank’s security audit requires zero exposure of rotating HSM PINs across Key Vault, parent cloud flows, and child unattended desktop flows. Which four-step sequence secures the secret end to end?

- **A.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing
- **B.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log
- **C.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs
- **D.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Combining Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable markings prevents secret leakage in logs. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.
- **B:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.
- **C:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.
- **D:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.

</details>

### Q059 (`E1Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A local anti-virus scanner occasionally locks newly downloaded settlement `.csv` files for up to 4 seconds, causing `Read from CSV file` to fail sporadically. Which action-level setting absorbs this brief file lock cleanly?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling `Retry action if an error occurs` (for example `3` retries every `2` seconds) in the action’s `On error` policy handles transient file or UI contention. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q060 (`E1Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

A bank’s internal FX-rate API requires an `X-Bank-Channel: RPA` HTTP header on every call without asking flow makers to type the header on each action. Which codeless Custom Connector feature injects this header at runtime?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Custom Connector `Set HTTP header` policy templates inject or overwrite static/dynamic headers transparently on every outbound request. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.

</details>

### Q061 (`E1Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

A platform engineering team is building a custom `.NET Framework` SWIFT-MT103 parser action for Power Automate for desktop and rolling it out to production bots. What is the valid lifecycle sequence?

- **A.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically
- **B.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand
- **C.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop
- **D.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Custom actions inherit `ActionBase` via the Custom Actions SDK, get packaged into a `.cab` archive signed with a trusted certificate, upload to Dataverse Custom actions, and ship inside Solutions. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.
- **B:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.
- **C:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).
- **D:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.

</details>

### Q062 (`E1Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

An RPA security architect must ensure all cloud flows, desktop flows, custom action modules, Connection References, and Key Vault Credentials deploy together under publisher prefix `mfb_`. Where must these artifacts be built?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Packaging all RPA artifacts inside a Dataverse Solution with a custom Publisher enables tracked dependencies, Connection References, and Managed ALM upgrades. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.

</details>

### Q063 (`E1Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

A bank stores its regional clearing-house base URL in a Dataverse Environment Variable `mfb_ClearingUrl` so both cloud flows and Power Automate for desktop flows read the stage-specific URL without hardcoding. Which configuration strategy does this implement?

- **A.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse Environment Variables are accessible natively in both cloud flows and solution desktop flows, separating stage configuration from code. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q064 (`E1Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A treasury cloud flow calls an internal Azure App Service API protected by Microsoft Entra ID without storing refresh tokens in flow variables. Which built-in `HTTP` action authentication mode should you configure?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings
- **C.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **D.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `ActiveDirectoryOAuth` or `Managed Identity` in the cloud `HTTP` action acquires Entra ID bearer tokens securely at runtime. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Correct — Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.
- **C:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **D:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.

</details>

### Q065 (`E1Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A credit-union desktop bot must drive SAP GUI for Windows using SAP’s recorded COM `GuiApplication` object model (`Set SapGuiAuto = ____("SapGuiAuto")`). Which built-in scripting action directly executes `.vbs` COM automation?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run VBScript` natively executes Visual Basic Script COM automation such as SAP GUI Scripting and returns `%VBScriptOutput%` and `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Correct — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Incorrect — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.

</details>

### Q066 (`E1Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A treasury architect is classifying incoming automation backlogs into cloud trigger categories before assigning RPA work. Which two scenarios match an Automated or Scheduled cloud flow rather than an Instant flow? Select two.

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Automated cloud flow triggered asynchronously by an external connector event
- **E.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Event-driven connector triggers (`Automated`) and time-cadence batch jobs (`Scheduled`) start without human button presses, whereas `Instant` flows wait for explicit manual or app invocation. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Incorrect — Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).
- **C:** Correct — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Correct — Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.
- **E:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

## Case Study Vignette — MeridianFirst Retail Bank

> [Scenario: MeridianFirst Retail Bank processes 14,000 nightly wire reconciliations against an IBM 3270 mainframe and an internal Win32 treasury app. Unattended bots must run without human sign-in across a 6-VM Machine Group, pull rotating Windows & mainframe secrets from Azure Key Vault, and distribute items safely via Dataverse Work Queues.]

### Q067 (`E1Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — MeridianFirst Retail Bank: Which Power Automate for desktop action family should MeridianFirst Retail Bank use to automate its `IBM 3270` green-screen wire reconciliation host with exact row/column field addressing?

- **A.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Built-in Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`, `Send key`) automate `IBM 3270` mainframes natively over HLLAPI or internal providers. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **B:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q068 (`E1Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — MeridianFirst Retail Bank: How should MeridianFirst Retail Bank supply rotating Windows OS and 3270 mainframe passwords to its 6-VM unattended Machine Group without editing flows when secrets rotate?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate `Credentials` backed by Azure Key Vault resolve the latest secret version from Key Vault at runtime whenever an unattended bot runs. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q069 (`E1Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — MeridianFirst Retail Bank: Which desktop flow loop action must each of the 6 unattended bots execute to atomically lease the next `Queued` wire reconciliation item from Dataverse without duplicate processing?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Process work queue items` atomically transitions each leased item from `Queued` to `Processing` across all 6 bots and pairs with `Update work queue item`. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q070 (`E1Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

A release pipeline service account needs to execute unattended desktop flows on the `Prod-Treasury-Pool` Machine Group, **without** permission to add/remove VMs or rotate the Machine Group key. Which Machine Group permission applies?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Sharing a Machine or Machine Group with `User` permission permits dispatching desktop flows onto the pool while reserving membership and key management for `Co-owner`. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.

</details>

### Q071 (`E1Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

In a Power Platform environment DLP policy, `Microsoft Dataverse` and `Desktop flows` are classified in `Business`, while `Dropbox` is classified in `Non-Business`. What happens when a maker saves a cloud flow combining `Dataverse`, `Desktop flows`, and `Dropbox`?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **C.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). DLP policies block any cloud or desktop orchestration that combines `Business` connectors with `Non-Business` connectors (or uses `Blocked` connectors/modules). [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **C:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q072 (`E1Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

An RPA governance lead is auditing access rights across cloud flows, desktop flows, and Machine Groups in Production. Which two least-privilege sharing configurations are accurate? Select two.

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **C.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **E.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Desktop flows distinguish `User` (run) from `Co-owner` (edit/share), and Machine Groups likewise distinguish `User` (dispatch runs) from `Co-owner` (administer machines). [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **C:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **E:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q073 (`E1Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A web portal regenerates random numeric `id` attributes on every login (`<input id="fld_91823" data-testid="wire-amount">`), so you target `input[____="wire-amount"]`. Which DOM strategy makes the web selector resilient?

- **A.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Targeting stable semantic DOM attributes via CSS selectors (such as `input[data-testid="wire-amount"]`) survives regenerated random element IDs. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q074 (`E1Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A Dataverse-triggered cloud flow should ONLY start when `cr88_wireamount` exceeds `50000` and `cr88_status` equals `2`. Complete the Trigger Condition: `@and(greater(triggerOutputs()?['body/cr88_wireamount'], 50000), ____(triggerOutputs()?['body/cr88_status'], 2))`. Which mechanism and WDL check applies?

- **A.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Adding `@and(greater(...), equals(...))` under Trigger Conditions filters non-qualifying Dataverse updates before any flow run starts. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **D:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q075 (`E1Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

A desktop flow appends daily exception rows to an existing multi-sheet `.xlsx` audit workbook at row `%____%` (`%FirstFreeRow%`) without overwriting prior days’ rows. Which Excel action sequence locates the exact append boundary?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **C.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Launch Excel` paired with `Get first free column/row from Excel worksheet` identifies `%FirstFreeRow%` so `Write to Excel worksheet` appends cleanly. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **C:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **D:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q076 (`E1Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

After importing Managed Solution `2.4.0.0` with updated UI selectors into UAT, the desktop flow still runs stale selectors from a one-off emergency edit someone made directly in UAT last month. What resolves this immediately?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Direct edits in UAT create an Unmanaged Active layer above Managed layers; running `Solution Layers -> Remove active customizations` exposes the updated Managed selectors. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q077 (`E1Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

A 350-action mortgage desktop flow is split into `Login_Portal`, `Post_Escrow`, and `Close_Apps` subflows. Proposed solution: Pass every variable across subflows via temporary `.txt` files on disk because `Post_Escrow` cannot read variables initialized in `Main`. Is that file workaround necessary?

- **A.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **B.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No workaround is needed because all subflows within a single Power Automate for desktop flow share one global variable namespace; `Run subflow` and `Exit subflow` access `%Main%` variables directly. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **B:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **C:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.

</details>

### Q078 (`E1Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

An RPA lead is comparing when to invoke an HTTP endpoint from a cloud flow versus from inside a Power Automate for desktop flow. Which two statements accurately distinguish the two approaches? Select two.

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Cloud HTTP actions execute from Microsoft’s cloud outbound network, whereas Desktop `Invoke web service` executes directly inside the bot VM’s local network/localhost context. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q079 (`E1Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A webhook sends an array of 50 wire transactions per HTTP POST, and the bank requires all 50 wires to be processed together inside a single cloud flow run rather than spawning 50 separate runs. Which trigger setting must you change?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **C.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Turning `Split On` to `Off` prevents Power Automate from de-batching an incoming array into separate individual flow instances. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **C:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **D:** Correct — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q080 (`E1Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

An infrastructure architect is evaluating unattended bot hosting options for bursty end-of-quarter mortgage reconciliations versus multi-bot on-premises Windows Server hosts. Which two platform capabilities accurately support unattended scaling? Select two.

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **E.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Hosted Machine Groups (`Hosted RPA`) auto-scale Azure VMs from Azure Compute Gallery images, while Windows Server RDSH supports multiple concurrent unattended Windows sessions per host. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **E:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.

</details>

### Q081 (`E1Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

A banking release lead is promoting an RPA solution containing cloud flows, desktop flows, custom connectors, and Environment Variables from Dev to Production. What is the recommended Managed ALM sequence?

- **A.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts
- **B.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows
- **C.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **D.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Exporting Managed solutions from Dev, verifying target Prod Machine Groups/Credentials, and importing via Pipeline/Upgrade while binding Connection References and Environment Variables preserves clean ALM. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.
- **B:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.
- **C:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **D:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.

</details>

### Q082 (`E1Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

An operations cloud flow fetches raw JSON text from an SFTP file, extracts typed dynamic tokens, and emails an HTML summary table to treasury supervisors. Which two Data Operation actions accomplish this cleanly? Select two.

- **A.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **D.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **E.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). `Parse JSON` exposes strongly typed schema properties as dynamic tokens, and `Create HTML table` / `Create CSV table` formats arrays for downstream reporting. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **D:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **E:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q083 (`E1Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow calls a core-banking OData REST API using the `HTTP` action, which returns only 100 accounts per page alongside an `@odata.nextLink` URL across 4,500 total accounts. Which setting retrieves all 4,500 items automatically?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enabling `Pagination` with a `Threshold` of `5000` in the `HTTP` action Settings instructs Power Automate to follow `@odata.nextLink` automatically. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.

</details>

### Q084 (`E1Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A desktop flow iterates over `%PendingWires%` using `For each`, and whenever `%CurrentItem['Status']% == 'SKIPPED'` it executes `____` (`Next loop`) to advance immediately to the next wire. Which loop-control action set should you use?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **D.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Next loop` skips the rest of the current iteration in Power Automate for desktop and advances directly to the next `For each` / `Loop` item, whereas `Exit loop` breaks out entirely. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **D:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.

</details>

### Q085 (`E1Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A cloud flow polls an asynchronous core-banking batch job endpoint until `@equals(body('Get_Batch')?['status'], 'Completed')`, capped at 30 checks or `Timeout = ____` (`PT15M`). Which cloud flow control structure implements this?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A cloud `Do until` container polls until its condition evaluates true while enforcing explicit `Count` and ISO 8601 `Timeout` guardrails. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q086 (`E1Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Operations supervisors need permission to trigger a solution desktop flow and inspect its run history on shared bots, **without** being able to edit actions, modify selectors, or delete the desktop flow. Which Desktop flow sharing permission should you grant?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Sharing a Desktop flow with `User` permission grants run and run-history access while withholding `Co-owner` edit/delete/re-share privileges. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **C:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.

</details>

### Q087 (`E1Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

A release engineer is configuring Power Platform pipelines to promote a bank’s RPA solution from Dev to UAT and Production while automatically removing two deprecated sub-flows. Which two ALM practices are required? Select two.

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **E.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Deploying Managed Solutions with `Stage for upgrade` / `Apply upgrade` removes deprecated components, and keeping target environments free of Unmanaged Active layers guarantees predictable behavior. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **E:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q088 (`E1Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Branch tellers need to launch a local attended desktop flow directly from an intranet HTML dashboard hyperlink while passing `BranchCode=042` as an input parameter: `____`. Which URI scheme completes the link?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop registers the `ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...` protocol handler to launch local attended flows with query inputs. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.

</details>

### Q089 (`E1Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

During mortgage closing calls, a loan officer stays signed into their laptop, watches a desktop bot pre-fill four disclosures, and supplies a verbal fee waiver reason mid-run when prompted. Which execution mode should you recommend?

- **A.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **B.** Attended run mode executing inside a signed-in user’s active desktop session
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Attended mode executes inside the human operator’s active signed-in Windows session and permits real-time human-in-the-loop prompts. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **B:** Correct — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.

</details>

## Case Study Vignette — HarborTrust Custody Ops

> [Scenario: HarborTrust Custody Ops orchestrates hybrid cloud-and-desktop settlement flows inside a Managed Dataverse Solution. Sensitive SWIFT bearer tokens must never appear in Cloud Run History or Desktop variable logs, and an internal REST trade engine requires a Custom Connector rewriting headers and executing C# payload signing under 5 seconds.]

### Q090 (`E1Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — HarborTrust Custody Ops: A custody web portal computes settlement net totals inside a client-side JavaScript closure not exposed in static HTML text. Which desktop action executes custom JS directly inside that open browser tab?

- **A.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { ... }` directly inside the live browser DOM and returns the computed value. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.

</details>

### Q091 (`E1Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — HarborTrust Custody Ops: In addition to enabling `Secure Inputs` and `Secure Outputs` in the parent cloud flow, what must HarborTrust Custody Ops configure in Power Automate for desktop so SWIFT bearer tokens never appear in PAD variable logs?

- **A.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs
- **B.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Marking the desktop Input and local token variables as `Sensitive` (`Mark as sensitive`) masks their values in PAD Designer and Dataverse `FlowSession` logs. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Correct — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.
- **B:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.

</details>

### Q092 (`E1Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — HarborTrust Custody Ops: Inside the Custom Connector for the internal REST trade engine, how should HarborTrust Custody Ops implement static header rewriting alongside `< 5-second` dynamic C# HMAC payload signing?

- **A.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Custom Connector policy templates rewrite headers codelessly while `Script : ScriptBase` (`ExecuteAsync()`) runs C# HMAC request signing within the 5-second / 1 MB limits. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **B:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.

</details>

### Q093 (`E1Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

During unattended loan entry, a wire request contains a closed beneficiary account code (`ERR-ACCT-CLOSED`). Proposed solution: Catch this business rule validation first, skip UI retries, update the Work Queue item to `On hold` with reason `ERR-ACCT-CLOSED`, and notify operations. Does this properly handle a Business Exception?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — deterministic domain rule rejections are Business Exceptions that should never trigger blind UI retries and instead route directly to business exception workflows. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **D:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q094 (`E1Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A cloud flow receives an ISO 20022 XML wire message in `Compose_ISO` and must extract all `<EndToEndId>` text values using Workflow Definition Language: `____(xml(outputs('Compose_ISO')), '//*[local-name()="EndToEndId"]/text()')`. Which WDL function completes this expression?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). In cloud flows, `xpath(xml(...), '...')` converts an XML string into an XML DOM node set and evaluates XPath queries. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q095 (`E1Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

An air-gapped desktop bot reads low-contrast Baltic-language characters off a legacy bitmap bond ticker where custom `.traineddata` dictionaries and a `2x` image width/height scale multiplier are required. Which OCR configuration should you recommend?

- **A.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **B.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **C.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop’s `Extract text with OCR` Tesseract engine supports custom `.traineddata` language paths and image width/height multipliers for tricky bitmaps. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **B:** Correct — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **C:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q096 (`E1Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

An RPA developer is distinguishing System Exceptions from Business Exceptions across Power Automate cloud and desktop flows. Which two patterns represent sound exception engineering? Select two.

- **A.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **E.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). `On block error` (`Get last error`, app restart subflow, `Continue flow run`) recovers transient System Exceptions, while conditional checks route Business Exceptions without pointless UI retries. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **E:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.

</details>

### Q097 (`E1Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

During automated pipeline promotion from Dev to UAT, how should a desktop flow switch from the Dev Machine Group and Dev Key Vault secret to the UAT Machine Group and UAT Key Vault secret without modifying flow logic?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Rebinding Connection References, Credentials, and Environment Variables per target stage via deployment settings or pipeline prompts keeps flow definitions immutable across environments. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q098 (`E1Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

An integration developer is configuring authentication and custom payload transformations inside a solution Custom Connector. Which two platform rules and capabilities apply? Select two.

- **A.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **B.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **E.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Custom Connectors support `OAuth 2.0` / `API Key` security and optional `Script : ScriptBase` C# transforms bounded by a strict `5-second` timeout and `1 MB` size limit. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **B:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **E:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.

</details>

### Q099 (`E1Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow scrapes 400 account numbers into `%RawAccounts%`, strips duplicate entries in place, and looks up branch routing metadata in a parsed JSON dictionary `%BranchMap['____']%`. Which variable types and actions fit?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **D.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Remove duplicate items from list` deduplicates `List` variables, while `Custom object` variables support key-based (`%BranchMap['NY01']%`) property lookups. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **D:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.

</details>

### Q100 (`E1Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A web-based collateral portal renders virtualized canvas rows whose values can only be read by invoking `window.gridApi.getSelectedRows()` inside the open Microsoft Edge tab: `function ____() { return JSON.stringify(window.gridApi.getSelectedRows()); }`. Which action and entry function signature applies?

- **A.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { ... }` directly inside the live browser tab DOM and returns serialized string values. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>
