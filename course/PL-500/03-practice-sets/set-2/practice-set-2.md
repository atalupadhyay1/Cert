# Microsoft Exam PL-500: Practice Exam 2 — Healthcare Citrix VDI, HL7 Labs & Hosted RPA — Reviewer Study Key

**Theme:** Citrix Virtual Desktop Agent, XML/XPath cloud flows, Windows Server RDSH concurrency, webpage JavaScript, and Hosted Machine Groups  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E2Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A developer placed `Wait 25` seconds before every screen in a 12-screen desktop flow, adding 5 unnecessary minutes to every claim run. Proposed solution: Replace fixed `Wait 25` steps with `Wait for window content` (`Timeout = 30s`) targeting each screen’s ready indicator. Does this speed up runs safely?

- **A.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — `Wait for window content` or `Wait for web page content` continues immediately once target UI elements render while failing predictably if the timeout elapses. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **B:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.

</details>

### Q002 (`E2Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A laboratory desktop bot needs to invoke an existing vendor-supplied Python 3.4 data-normalization snippet locally on the workstation and read stdout into `%PythonResult%`. Which Power Automate for desktop action family supports this?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **D.** Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run Python script` (and `Run DOS command` for CLI invocations) executes local Python scripts and captures output/error variables in Power Automate for desktop. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **D:** Correct — `Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.

</details>

### Q003 (`E2Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

A hospital accounts-payable team is adopting the Microsoft Document Automation Toolkit for medical-supply vendor invoices. Place the toolkit’s processing stages in the exact runtime order.

- **A.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows
- **B.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email
- **C.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **D.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Incoming invoice attachments are captured by cloud flows, extracted via AI Builder Document Processing, reviewed in the Canvas Validation Station when below confidence thresholds, and exported from Dataverse. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.
- **B:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.
- **C:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **D:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.

</details>

### Q004 (`E2Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

A VM previously registered to the `UAT` environment must be repurposed to join a Machine Group in the `Production` environment. Where do you switch the machine’s registered Power Platform environment?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Open the **Power Automate machine runtime** app on the VM, switch the selected Power Platform environment dropdown to `Production`, and join the target Machine Group. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Correct — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.

</details>

### Q005 (`E2Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A parent cloud flow invokes `Run a flow built with Power Automate for desktop` for a heavy surgical-supply reconciliation that legitimately runs for 90 minutes, and you want the cloud step to time out at 2 hours (`____`). Which ISO 8601 Timeout value should you set?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **C.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **D.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting `PT2H` (or `PT120M`) in the cloud action’s ISO 8601 `Timeout` field bounds the wait window cleanly at 2 hours. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **C:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **D:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.

</details>

### Q006 (`E2Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

A healthcare revenue-cycle architect is configuring nightly unattended claim-submission bots triggered from a scheduled cloud flow onto signed-out VMs. Which four-step execution lifecycle applies?

- **A.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text
- **B.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically
- **C.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **D.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Unattended execution requires zero active/locked human sessions on single-session VMs, opens a fresh Windows session via Machine Group credentials, runs the bot, and signs out cleanly. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.
- **B:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.
- **C:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **D:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.

</details>

### Q007 (`E2Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

During pharmacy claim adjudication, Bot A encounters `Win32 Window Not Found` (EHR crash), while Bot B reads `Rejection 79: Refill Too Soon` (valid payer business rule). Which two exception-handling responses are appropriate? Select two.

- **A.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **E.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). `Win32 Window Not Found` is a System Exception handled via `On block error` app recovery/requeue, whereas `Refill Too Soon` is a Business Exception logged immediately without UI retries. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **E:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.

</details>

### Q008 (`E2Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

A legacy hospital radiology service returns XML payloads from an internal endpoint, and makers want a Custom Connector to expose clean JSON properties to cloud flows without writing C# code. Which Custom Connector feature handles this?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Custom Connector `Convert XML to JSON` policy templates transform XML responses into JSON at runtime with zero custom code. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.

</details>

### Q009 (`E2Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A hospital’s patient-ledger API rejects parallel updates for the exact same database sequence, requiring a cloud flow to process incoming messages strictly one at a time in FIFO order (`Degree of Parallelism = ____`). Which setting enforces singleton execution?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enabling trigger `Concurrency Control` with `Degree of Parallelism = 1` serializes cloud flow executions to one active run at a time. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q010 (`E2Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

A revenue-cycle desktop flow ingests a `;`-delimited payer remittance CSV file, updates matching fee rows inside an `.xlsx` template, and serializes a summary `%CustomObject%` back to JSON text. Which three PAD action sets are needed? Select three.

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **C.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **E.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **F.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, E` (`CSV: 2,3,5`)

Correct answers: B, C, and E (are correct). `Read from CSV file` (producing a `Datatable`), `Launch Excel` / `Write to Excel worksheet`, and `Convert custom object to JSON` complete the local pipeline natively. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **C:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **E:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **F:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q011 (`E2Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

An operations lead notices a rogue loop queued 300 obsolete test desktop flow runs on `MG-Claims` and needs to abort all waiting runs immediately while promoting one valid hotfix run to the front. Where and how is this done?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Under `Monitor -> Machines -> [Machine Group] -> Run queue` in Power Automate portal, operators can `Cancel` queued/running items and apply `Change priority` / `Move to top`. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q012 (`E2Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

A radiology group automates a web-based PACS scheduling portal running in Microsoft Edge where frames and dynamic HTML tables must be inspected via DOM selectors. What must be installed in Edge on the bot workstation?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The Microsoft Power Automate browser extension connects Power Automate for desktop to Edge, Chrome, or Firefox for live DOM element inspection and interaction. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q013 (`E2Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A desktop flow polls a local instrument status file inside a `Loop condition` while `%Status% <> 'READY'`, and if `%ElapsedSeconds% > 120` it must break out of the loop immediately and continue to the alert step below the loop. Which action exits the loop cleanly?

- **A.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Exit loop` breaks out of the enclosing `Loop`, `Loop condition`, or `For each` block and continues execution at the first action after `End`. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **B:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).

</details>

### Q014 (`E2Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A clinical RPA architect is separating workloads between Power Automate cloud flows and Power Automate for desktop flows. Which two criteria justify choosing a cloud flow or an Instant cloud trigger? Select two.

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger
- **E.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). API-accessible cloud services belong in headless cloud flows, and on-demand clinician button presses map to Instant cloud flows. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Correct — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).
- **E:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q015 (`E2Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow downloads a 75 MB medical imaging archive via the `HTTP` action and fails unless message chunking is enabled on the action. Where do you configure `Allow chunking` and `Pagination` for REST transfers in cloud flows?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Cloud connector/HTTP action **Settings** control `Allow chunking` (for large payloads), `Pagination` + `Threshold`, `Timeout`, and `Retry Policy`. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.

</details>

### Q016 (`E2Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

A cloud flow needs to read incoming `.hl7` staging files from `\\fileserver.hosp.local\____` on an internal Windows file server that has no public IP. Which component enables the File System cloud connector to reach that share?

- **A.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). An On-Premises Data Gateway (deployed as a high-availability cluster) bridges the cloud File System / SQL Server connectors to internal network shares. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.

</details>

## Case Study Vignette — Clearview Regional Health

> [Scenario: Clearview Regional Health automates inpatient claim scrubbing inside a legacy WinForms billing client published over Citrix Virtual Apps. Because Citrix streams pixels by default, selectors failed until the team evaluated the Power Automate agent for virtual desktops vs OCR fallback, paired with `On block error` system-exception recovery.]

### Q017 (`E2Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — Clearview Regional Health: Why did standard local Win32 UI selectors fail against Clearview Regional Health’s Citrix-published WinForms billing client, and what restores true control-level UI selectors?

- **A.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **B.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **C.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Citrix streams remote bitmaps by default; installing the **Power Automate agent for virtual desktops** inside the Citrix VDA synchronizes real WinForms UI element selectors to PAD. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **B:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **C:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q018 (`E2Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — Clearview Regional Health: Clearview Regional Health wants all Citrix desktop flows, exception subflows, Connection References, and Key Vault Credentials versioned under publisher `crh_` for UAT/Prod promotion. Which container is required?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A Dataverse Solution with custom publisher `crh_` packages desktop flows, cloud flows, Connection References, and Credentials for enterprise ALM. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q019 (`E2Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — Clearview Regional Health: When Citrix experiences a transient session disconnect wrapped in `On block error`, Clearview wants the claim item returned to the Dataverse Work Queue with a 10-minute cooldown before another bot retries it. Proposed solution: Invoke `Requeue item with delay` (`10 minutes`) inside the recovery routine. Does this meet the goal?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — `Requeue item with delay` places the leased item back into `Queued` state invisible to bots until the 10-minute delay expires. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q020 (`E2Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

Inside a `Validate_Claim` subflow, when a claim already carries `PaidInFull = true`, the bot should skip the remaining steps of `Validate_Claim` and return control immediately to the `Main` flow’s `For each` loop to process the next claim. Which action should you use?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Exit subflow` returns execution immediately from the current subflow back to the calling step in `Main`, whereas `Stop flow` terminates the entire desktop flow. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.

</details>

### Q021 (`E2Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

A desktop bot on a hospital workstation queries an internal SQL database directly via OLE DB (`Provider=____;Server=sql01;Database=Claims;`) and stores returned rows in `%QueryResult%`. Which built-in PAD actions handle this?

- **A.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **B.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **C.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Open SQL connection`, `Execute SQL statement` (producing `%QueryResult%` Datatable), and `Close SQL connection` query databases directly from Power Automate for desktop. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **B:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **C:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q022 (`E2Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

A hospital security officer is reviewing sharing matrices for RPA artifacts. Which two permissions prevent makers or operators from modifying production bots or machine pools? Select two.

- **A.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **E.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Granting `User` (rather than `Co-owner`) on Desktop flows restricts users to running/viewing runs, and granting `User` on Machine Groups restricts connections to dispatching runs without pool admin rights. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **E:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q023 (`E2Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

An EHR modernization team automates three targets: a Citrix-published Win32 billing app (where admins can install agents on the Citrix VDA), a sealed third-party kiosk bitmap screen (no agents allowed), and an `IBM 5250` lab host. Which three interaction approaches match these targets? Select three.

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **E.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **F.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, E` (`CSV: 2,4,5`)

Correct answers: B, D, and E (are correct). The virtual desktop agent unlocks UI selectors over Citrix/RDP, image recognition/OCR handles sealed pixel-only screens, and terminal emulation drives `IBM 5250` hosts. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Correct — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **E:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **F:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q024 (`E2Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

A clinical integration developer is refactoring repeated FHIR token-validation steps out of 9 cloud flows into a single Child Cloud Flow. Which two requirements must be satisfied for `Run a Child Flow` to work? Select two.

- **A.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **B.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied
- **C.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **E.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). The child flow must reside in a Dataverse Solution with a synchronous response action (`Respond to a Power App or flow` / `Response`) and configure `Run only users` connections to `Use this connection`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **B:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.
- **C:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **E:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q025 (`E2Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A compliance officer prohibits arbitrary PowerShell execution on clinical bot VMs. Proposed solution: Package the audited HL7 helper as a signed `.NET Custom Action` `.cab` module and block the `PowerShell` desktop module via DLP. Does this satisfy enterprise governance?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — enterprise DLP policies can block raw `Run PowerShell script` actions across Production while permitting signed, audited `.cab` Custom Action modules. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q026 (`E2Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A hospital interoperability team needs to poll an external FHIR REST endpoint every 15 minutes and upsert patient appointment slots into Microsoft Dataverse with zero UI dependencies. Which flow type fits best?

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A Scheduled cloud flow executes headless API syncs on a 15-minute recurrence without consuming Windows VM licenses or desktop sessions. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.
- **D:** Correct — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q027 (`E2Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

While debugging step #84 of a 140-step desktop flow in Power Automate for desktop Designer, the target EHR screen is already open at the exact state required for step #84, and the developer wants to test from step #84 onward without re-running steps 1–83. Which Designer feature should they use?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run from here` in Power Automate for desktop Designer starts execution directly at the selected action (complemented by `Breakpoints`, `Run next action`, and `Run delay`). [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Incorrect — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **C:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q028 (`E2Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

While processing a Work Queue item in Power Automate for desktop, an external state immunization registry displays `Scheduled Maintenance — Retry in 45 minutes`. Which Work Queue action puts that item back into the queue without failing it permanently or re-leasing it immediately?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Requeue item with delay` (or updating delay/requeue status) returns the item to `Queued` state held back until the specified delay timestamp elapses. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q029 (`E2Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

A hospital runs legacy applications across both an `IBM 3270` mainframe admission screen and a Citrix-published WinForms revenue client. Which two Power Automate for desktop capabilities provide native control-level selectors rather than brittle pixel matching? Select two.

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **E.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Terminal emulation actions address `3270` screen fields directly, and the Power Automate agent for virtual desktops exposes real WinForms UI selectors inside Citrix/RDP sessions. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **E:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q030 (`E2Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

A clinic’s cloud flow processes HL7 webhook bursts that spike to 200 requests per second, overwhelming a downstream legacy API that supports at most 5 simultaneous calls. Which cloud trigger setting throttles active flow instances to 5?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enabling trigger `Concurrency Control` and setting `Degree of Parallelism` to `5` caps concurrent cloud flow runs while queuing excess events safely. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q031 (`E2Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

A healthcare QA lead is standardizing pre-release testing across cloud flows, desktop flows, and multi-environment configuration files. Which three practices belong in the QA checklist? Select three.

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **E.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **F.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, F` (`CSV: 1,2,6`)

Correct answers: A, B, and F (are correct). Mocking cloud HTTP errors with `Static Result`, stepping through PAD `Breakpoints` / `Variables` pane, and externalizing endpoints in Dataverse `Environment Variables` or JSON config files ensure clean releases. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **E:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **F:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

### Q032 (`E2Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A web-based state Medicaid portal occasionally flashes a transient `502 Bad Gateway` banner unless `Press link on web page` retries `2` times spaced `5` seconds apart. Proposed solution: Enable `Retry action if an error occurs` (`Times = 2`, `Interval = 5s`) in the action’s `On error` settings. Does this absorb the transient glitch?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — in the desktop action’s `On error` dialog, enabling `Retry action if an error occurs` (`Times = 2`, `Interval = 5` seconds) handles transient UI hiccups declaratively. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q033 (`E2Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow calls a payer eligibility API that occasionally returns transient `HTTP 503 Service Unavailable` spikes during morning clinic check-ins. Complete the action Retry Policy type that backs off progressively (`10s`, `20s`, `40s`): `____`. Which configuration applies?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **C.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configuring `Exponential Interval` in the cloud action’s `Retry Policy` spaces retries progressively to absorb transient `429`/`503` throttling. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **C:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q034 (`E2Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

A solution contains 14 cloud flows that all talk to Microsoft Dataverse and Desktop flows. To avoid prompting admins to authenticate 28 separate connections on deployment, how should Connection References be structured?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **D.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Reusing one shared Connection Reference per connector/identity inside the Solution lets all 14 flows bind to a single target Connection at import. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **D:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.

</details>

### Q035 (`E2Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

A desktop flow wraps 12 fragile Citrix billing screens inside an `On block error` container. When any UI action inside the block throws a system exception, the bot must capture `%LastError%`, run `Reset_Citrix_App`, and retry the entire block from the top. How should `On block error` be configured?

- **A.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **D.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `On block error` captures `%LastError%`, invokes `Run subflow` (`Reset_Citrix_App`), and sets `Continue flow run -> Go to beginning of block` (bounded by a retry counter). [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **D:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.

</details>

### Q036 (`E2Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

When a patient discharge row is updated in Dataverse, an automation must call an EHR cloud API, wait for a charge-nurse Teams approval, and then print a barcode wristband from a legacy Windows XP-era WinForms utility. Which design pattern should you recommend?

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A hybrid architecture lets a Dataverse-triggered cloud flow orchestrate APIs and Teams approvals before invoking a desktop flow for the legacy WinForms utility. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.

</details>

### Q037 (`E2Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

An architect creates a DLP Custom Connector URL pattern rule allowing `https://*.corp.health/*`, but a Custom Connector pointing to `http://legacy.corp.health/api` (unencrypted HTTP) is still blocked! Why?

- **A.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **B.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). DLP URL endpoint patterns match exact scheme (`https://` vs `http://`), host, and port rules, blocking unencrypted `http://` endpoints when only `https://` is permitted. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **B:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.

</details>

### Q038 (`E2Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

A hospital Work Queue architect wants a cloud flow to bulk-load nightly lab items while preventing duplicate `SpecimenBarcode` entries and automatically expiring unworked items at `____(utcNow(), 8)`. Which two capabilities handle both sides of the queue? Select two.

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **E.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Enqueuing sets `Unique reference` (`SpecimenBarcode`) and `ExpiresOn` (`addHours(utcNow(), 8)`), while `Process work queue items` + `Update work queue item` manage bot processing outcomes. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **E:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.

</details>

### Q039 (`E2Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

A desktop flow uses `Invoke web service` to POST JSON (`Content-type: application/json`, `Encode request body = ____`) to an internal HTTPS lab API with custom header `X-Lab-Key`, saving the output to `%ApiResponse%`. Which action family handles this?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Invoke web service` Advanced settings in Power Automate for desktop provide `Custom headers`, HTTP auth/client certs, `Ignore certificate errors` (for lab appliances), and `Encode request body = Off` for JSON. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q040 (`E2Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

During UAT debugging, a fast desktop bot outpaces legacy client animations only when Designer runs at full speed, and the developer wants to slow every action globally by `500 ms` inside Designer to observe focus transitions. Which PAD Designer control provides this?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Run delay` (ms) setting in Power Automate for desktop Designer throttles execution between actions during interactive debugging. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q041 (`E2Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

Why must Dev, UAT, and Production RPA environments each bind their `Desktop flows` Connection Reference to distinct Machine Groups and Credentials?

- **A.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Isolating Machine Groups and Credentials per stage prevents UAT test runs from mutating Production EHR terminals or sharing Production domain credentials. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **B:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.

</details>

## Case Study Vignette — SilverOak Specialty Pharmacy

> [Scenario: SilverOak Specialty Pharmacy validates prior-authorization portals using Power Automate for desktop. A portal calculates dynamic copay tables client-side inside shadow/DOM elements requiring `Run JavaScript function on web page`, stores parsed JSON tiers in a Desktop Custom Object, and marks patient DEA numbers as Sensitive variables.]

### Q042 (`E2Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — SilverOak Specialty Pharmacy: Why must SilverOak Specialty Pharmacy use `Run JavaScript function on web page` (`function ExecuteScript() { ... }`) to read dynamic copay calculations inside the payer portal?

- **A.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Only `Run JavaScript function on web page` runs inside the live browser tab’s DOM/shadow-DOM context to query client-side JavaScript state and return stringified JSON. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **B:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q043 (`E2Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — SilverOak Specialty Pharmacy: How does SilverOak Specialty Pharmacy ensure prescriber DEA numbers passed into the desktop flow are masked (`••••`) in PAD Designer and never written in plaintext to Dataverse `FlowSession` logs?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enabling `Mark as sensitive` (`Sensitive` variable flag) on the DEA Input and local variables redacts their values from Designer inspection and desktop run logs. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **D:** Correct — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.

</details>

### Q044 (`E2Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — SilverOak Specialty Pharmacy: SilverOak wraps an external PBM prior-auth REST API in a Custom Connector that needs OAuth 2.0 client authentication plus dynamic URL routing per payer region. Which Custom Connector features should they combine?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). OAuth 2.0 security paired with `Set host URL` / `Route request` policy templates routes Custom Connector requests dynamically per payer region without custom servers. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.

</details>

### Q045 (`E2Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

A junior developer can build cloud flows (`Environment Maker`) in UAT, but receives a Dataverse privilege error when trying to select a shared Machine Group in a `Desktop flows` connection. Which two identity/role concepts explain RPA access? Select two.

- **A.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **E.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). The maker needs the `Desktop Flows Machine User` Dataverse security role **and** `User` sharing permission on the target Machine Group. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **E:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.

</details>

### Q046 (`E2Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

One VM inside a 5-VM Machine Group shuts down unexpectedly for motherboard maintenance while 40 unattended runs are queued against the group. How does the Machine Group behave?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The Machine Group automatically routes queued runs across the remaining 4 healthy online VMs without failing queued runs waiting in the pool. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q047 (`E2Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

A compliance officer requires patient SSNs and EHR API keys to stay masked from Azure Key Vault retrieval through cloud orchestration into Power Automate for desktop logs. Which sequence satisfies the audit?

- **A.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs
- **B.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step
- **C.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log
- **D.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Using Key Vault-backed Credentials/Secret Env Vars, turning on Cloud `Secure Inputs` & `Secure Outputs`, and marking PAD variables `Sensitive` redacts sensitive values end to end. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.
- **B:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.
- **C:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.
- **D:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.

</details>

### Q048 (`E2Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

A lab automation engineer is deciding whether to place an HTTP REST call in a parent cloud flow or inside Power Automate for desktop’s `Invoke web service` action. Which two architectural facts apply? Select two.

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **D.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **E.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Desktop `Invoke web service` reaches `localhost` or isolated lab VLAN endpoints directly from the bot VM, whereas cloud `HTTP` runs headlessly from Microsoft’s cloud without occupying a bot VM. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **D:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **E:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

### Q049 (`E2Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

A developer writes a `Script : ScriptBase` class (`override async Task<HttpResponseMessage> ____()`) inside a Custom Connector to redact PHI regex patterns before returning JSON to cloud flows. Which two technical rules apply? Select two.

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **E.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). `ScriptBase` overrides `ExecuteAsync()`, must complete within `5 seconds` (`<= 1 MB` code), and works alongside the Custom Connector’s OAuth 2.0 / API Key security configuration. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **E:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.

</details>

### Q050 (`E2Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

A clinical trial intake portal needs a cloud flow to trigger automatically whenever a `ConsentForm` row’s `VerificationStatus` column changes in Dataverse, filtered via `Select columns` (`filteringattributes`). Which trigger architecture applies?

- **A.** Microsoft Dataverse custom/standard tables providing relational storage, security roles, and native triggers
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse’s native connector triggers immediately on row create/update/delete events and scopes execution to specific modified columns via `Select columns`. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Correct — Dataverse serves as the enterprise state store for Power Platform RPA metadata, Work Queues, audit logs, and business records.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q051 (`E2Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

An automated Azure DevOps Power Platform Build Tools pipeline imports a Managed RPA solution into Production non-interactively via `pac solution ____` (`create-settings`). Which artifact maps Connection References and Environment Variables to Production GUIDs and values?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **D.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A Power Platform **deployment settings JSON file** (`pac solution create-settings`) supplies target Connection Reference bindings and Environment Variable values during automated imports. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **D:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.

</details>

### Q052 (`E2Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

During morning clinic surges, `MG-Eligibility` (4 machines) receives 50 queued runs: 46 at `Normal` priority followed by 4 urgent emergency-room checks at `High` priority. Which run executes as soon as the first VM finishes its current job?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Machine Group run queues dispatch waiting `High` priority runs before any waiting `Normal` priority runs (in FIFO order within `High`). [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q053 (`E2Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

A clinical RPA DevOps team is promoting Solution `RpaClaims_1_3_0_0_managed.zip` from Dev through UAT to Production via Power Platform pipelines. Place the ALM steps in the proper order.

- **A.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts
- **B.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **C.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs
- **D.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Packaging all components in an Unmanaged Dev Solution, exporting Managed, verifying target Machine Groups/Credentials, and importing via Managed Upgrade with bound Connection References enforces clean ALM. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.
- **B:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **C:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.
- **D:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.

</details>

### Q054 (`E2Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

A night-shift unattended desktop flow keeps timing out after 60 minutes because a developer left a `Display input dialog` asking `Confirm payer override?` inside an exception branch. Proposed solution: Remove all interactive `Display input dialog` / `Display message` prompts and route exceptions to a Dataverse Work Queue or Teams approval in the parent cloud flow. Does this fix the unattended hang?

- **A.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — unattended background Windows sessions have no human operator to dismiss modal dialogs, so interactive UI prompts must never run in unattended mode. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.

</details>

### Q055 (`E2Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Hospital security mandates that unattended Windows domain service-account passwords rotate every 24 hours in **CyberArk** Enterprise Password Vault without breaking scheduled Power Automate desktop runs. Which Power Automate feature integrates natively with CyberArk?

- **A.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **B.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate `Credentials` support both CyberArk and Azure Key Vault secret stores to fetch rotated credentials dynamically at desktop flow runtime. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **B:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q056 (`E2Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

A hospital infrastructure team is registering six new VMware Windows VMs into a load-balanced `MG-RevenueCycle` Machine Group in Production. Which sequence is correct?

- **A.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **B.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference
- **C.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly
- **D.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Install PAD + Power Automate machine runtime, register each VM to Production, join `MG-RevenueCycle` using the group password/key, and share the group as `User` with Connection References. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **B:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.
- **C:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.
- **D:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.

</details>

### Q057 (`E2Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Case managers working inside a **Model-driven** Care Management app want a modern command bar button on `Referral` that updates a trigger column via Power Fx `____(Referrals, Self.Selected.Item, {TriggerSync: true})` to invoke a solution cloud flow. Which integration pattern applies?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Model-driven modern command bar buttons (via Power Fx `Patch` or Dataverse triggers) integrate cleanly with solution-aware cloud flows. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Correct — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q058 (`E2Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

A release engineer wants to deploy v2.0 of a Managed RPA Solution that deletes an obsolete helper cloud flow while preserving existing Dataverse `ClaimAudit` table rows and Work Queue items. Proposed solution: Delete the entire v1.0 Managed Solution in Production first, then import v2.0. Does this preserve `ClaimAudit` table data?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No — deleting a Managed Solution permanently drops its custom Dataverse tables and data! Use Managed `Stage for upgrade` -> `Apply upgrade` to remove obsolete flows while preserving table data. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q059 (`E2Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

An environment admin wants citizen makers in the Default environment barred from using `Desktop flows` entirely, while dedicated RPA environments allow `Desktop flows` paired with `Dataverse`. Where is this enforced?

- **A.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Environment-scoped DLP policies classify `Desktop flows` as `Blocked` in Default while placing `Desktop flows` and `Dataverse` together in `Business` for dedicated RPA environments. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **D:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.

</details>

### Q060 (`E2Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A medical-device RPA team wants C# developers to wrap a proprietary HL7 v2 checksum library into a signed custom action module governed by Power Platform DLP and Solutions. Which architecture should they design?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate Custom Actions SDK `.cab` packages signed with a trusted certificate upload to Dataverse as solution-aware, DLP-governed desktop flow modules. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q061 (`E2Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A SharePoint `When an item is created or modified` cloud flow should run ONLY when `ClaimStage` equals `'ReadyForBot'`, avoiding infinite update loops and wasted API calls: `____(triggerOutputs()?['body/ClaimStage/Value'], 'ReadyForBot')`. Which feature and expression applies?

- **A.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **B.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Adding `@equals(triggerOutputs()?['body/ClaimStage/Value'], 'ReadyForBot')` in **Trigger Conditions** suppresses runs when `ClaimStage` has any other value. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **B:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q062 (`E2Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

An automated deployment pipeline imports a solution whose parent cloud flows are owned by a headless Microsoft Entra **Service Principal**, while the `Desktop flows` connection logs into Windows Server VMs. Which credential pair is valid?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The Microsoft Entra Service Principal owns headless cloud flows/connections, while the `Desktop flows` connection uses an interactive AD / Entra user credential (via Key Vault/CyberArk) to sign into Windows sessions. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q063 (`E2Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

Before Production cutover, an architect inspects Solution Layers and pipeline configurations on the hospital’s RPA environment. Which two conditions confirm healthy Production ALM? Select two.

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **E.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Production should run exclusively Managed Solutions upgraded via pipelines/Build Tools with stage-mapped Connection References, Credentials, and Environment Variables. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **E:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q064 (`E2Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Clinic supervisors invoke an Instant cloud flow from SharePoint that triggers a downstream service-account desktop flow. How should you grant those 60 supervisors permission to run the cloud flow **without** sharing the underlying RPA VM Windows credentials with them?

- **A.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configuring the cloud flow’s **Run-only users** settings to `Use this connection` on the `Desktop flows` connection lets supervisors trigger the cloud flow without accessing VM credentials. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **B:** Incorrect — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.

</details>

### Q065 (`E2Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A hospital’s cloud `HTTP` connector and Custom Connectors must be allowed to call `https://fhir.clearviewhealth.org/*` (`Order 1: Allow`) and `https://edi.medicaid.gov/*` (`Order 2: Allow`), while blocking data exfiltration to any internet webhook (`Order 3: * -> Deny`). Which governance feature enforces this?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). DLP **Connector endpoint filtering** and **Custom connector URL patterns** evaluate ordered FQDN rules and block unapproved hosts via a catch-all `*` `Deny` rule. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.

</details>

### Q066 (`E2Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

In a cloud flow, you need to format `utcNow()` as `20261030` for an HL7 filename (`____(utcNow(), 'yyyyMMdd')`) and convert string `'42'` to integer `42` (`int('42')`). Which cloud logic capability evaluates these functions?

- **A.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **B.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **C.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers
- **D.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Workflow Definition Language (`WDL`) expressions (`formatDateTime()`, `int()`, `coalesce()`, `concat()`) transform data inline inside cloud flow inputs and variables. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **B:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **C:** Incorrect — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.
- **D:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.

</details>

## Case Study Vignette — BioPulse Reference Labs

> [Scenario: BioPulse Reference Labs ingests XML HL7 lab requisitions in a parent cloud flow, extracts specimen codes via `xpath(xml(...))`, enqueues items into a Dataverse Work Queue, and runs 8 concurrent unattended desktop sessions on a Windows Server 2022 RDSH host calling a local analyzer’s unauthenticated localhost HTTP port.]

### Q067 (`E2Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — BioPulse Reference Labs: BioPulse Reference Labs also receives scanned paper requisition forms by email from rural clinics that need AI Builder extraction plus clerk Validation Station review before hitting the lab queue. Which Microsoft accelerator fits?

- **A.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **B.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The Document Automation Toolkit provides prebuilt email capture, AI Builder Document Processing, Dataverse persistence, and the Canvas Validation Station app. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **B:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q068 (`E2Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — BioPulse Reference Labs: Inside BioPulse’s parent cloud flow (`xpath(xml(triggerBody()), '//OBR/SpecimenCode/text()')`), once specimen codes enter PAD on the Windows Server 2022 RDSH host as `%____%`, how do bots select dynamic analyzer rows safely?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dynamic `%SpecimenCode%` variables injected into UI selectors in Selector Builder target exact analyzer rows across concurrent RDSH sessions without screen-coordinate collisions. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q069 (`E2Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — BioPulse Reference Labs: Each RDSH bot session must POST specimen metadata to a local analyzer daemon listening ONLY on `http://127.0.0.1:9100/load` inside that Windows Server host. Why must `Invoke web service` in PAD be used instead of a cloud `HTTP` action?

- **A.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **B.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `127.0.0.1` (`localhost`) resolves strictly inside the bot VM’s network stack; Desktop `Invoke web service` executes locally on the RDSH host with `Encode request body` set `Off` for JSON. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **B:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **C:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q070 (`E2Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Four hospital billing bots consume claim items from a shared backlog where each claim has a 4-hour payer filing deadline (`ExpiresOn`) and duplicate `ClaimNumber` submissions must be rejected at enqueue time. Which Power Automate capability fits?

- **A.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse Work Queues enforce optional `Unique reference` deduplication keys, `ExpiresOn` timestamps, and prioritized multi-bot item leasing. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.

</details>

### Q071 (`E2Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

A clinical RPA developer is stabilizing a web selector on an insurance portal that injects session GUIDs into `<div id="pane_77f1a9">` on each login. Which four-step Selector Builder workflow hardens this element?

- **A.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field
- **B.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **C.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs
- **D.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Unchecking volatile GUID `id` attributes, matching stable attributes via `%Variable%` / `Contains` / `Regex`, and adding fallback selectors keeps web automation resilient. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.
- **B:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **C:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.
- **D:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).

</details>

### Q072 (`E2Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

A senior RPA engineer needs permission to add two replacement VMs to `MG-LabBots` and view all queued runs on the group. Which Machine Group permission level is required?

- **A.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **B.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Co-owner` permission on a Machine Group is required to add or remove member machines, manage group settings, and share the group (`User` only permits dispatching runs). [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **B:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.

</details>

### Q073 (`E2Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A clinical referrals inbox receives scanned multi-page fax PDFs with checkboxes and tables that must be turned into structured JSON fields with confidence scores in a cloud flow. Which AI option should you recommend?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **D.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). AI Builder Document Processing handles multi-page PDFs, checkboxes, and tables with per-field confidence scores inside cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **D:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.

</details>

### Q074 (`E2Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Front-desk intake nurses want an icon right on their Windows 11 desktop so they can launch an approved attended insurance-eligibility desktop flow locally without opening Power Automate Designer. Which built-in console feature provides this?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Create desktop shortcut` in the Power Automate for desktop console generates a `.lnk` launcher on the user’s desktop for local attended flows. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Correct — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **D:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q075 (`E2Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

In a parent cloud flow, a `Catch` `Scope` is placed immediately below a `Try` `Scope`, but when an action inside `Try` times out (`PT10M`), `Catch` never executes! What was omitted on the `Catch` `Scope`’s `Configure run after` settings?

- **A.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **B.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). By default, actions only run after `is successful`; `Catch` `Scope` must check `has failed`, `is skipped`, **and** `has timed out` in `Configure run after`. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **B:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q076 (`E2Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A desktop bot inspects a legacy Windows medical-imaging status bar that renders standard English Arial text with no UIA automation peers on offline Windows 11 workstations. Which fast built-in OCR engine requires zero external `.traineddata` downloads?

- **A.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Extract text with OCR` using the `Windows OCR engine` leverages native Windows OS language packs locally with fast execution. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **D:** Correct — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q077 (`E2Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

After calling `Convert JSON to custom object` on `{"patient":{"mrn":"44910","allergies":["Penicillin","Latex"]}}` storing `%PatientObj%`, complete the PAD expression for the first allergy: `%PatientObj['patient']['allergies'][____]%`. Which data-type indexing rule applies?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop Custom objects use key/property access (`['patient']`) and Lists use zero-based integer indexing (`[0]`). [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).

</details>

### Q078 (`E2Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

An HTTP action returns raw JSON `{"claimId":"C-900","lines":[{"cpt":"99213","fee":140}]}` as untyped string/object output, and makers want `claimId` and `cpt` listed in the cloud flow Dynamic Content picker. Which action should you add next?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Parse JSON` applies a JSON Schema (generated from sample payload) to surface typed properties in Dynamic Content. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q079 (`E2Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

A developer is connecting a parent HL7 cloud flow to a solution-aware desktop flow that returns `%AccessionNumber%` and `%PrintStatus%`. Select the valid implementation sequence.

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP
- **C.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **D.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Declaring Input/Output variables in the solution desktop flow and binding `Run a flow built with Power Automate for desktop` via a Machine/Group Connection Reference passes parameters and outputs cleanly. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.
- **C:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **D:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.

</details>

### Q080 (`E2Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

Incoming patient feedback messages in Dataverse must be tagged automatically into `Billing`, `Scheduling`, `Pharmacy`, or `Clinical Care` buckets inside an Automated cloud flow. Which AI Builder model type should you select?

- **A.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **B.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **C.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **D.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder Category Classification (custom or prebuilt text classification) categorizes unstructured text into defined business labels inside cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **B:** Incorrect — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **C:** Correct — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **D:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.

</details>

### Q081 (`E2Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

Inside a `Run PowerShell script` action in Power Automate for desktop, a developer wants to pass the PAD variable `%SpecimenFolder%` into `Get-ChildItem -Path "____"`. How does PAD inject desktop flow variables into script bodies?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **D.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate for desktop interpolates `%SpecimenFolder%` percent-notation variables directly inside `Run PowerShell script` and `Run VBScript` code blocks before execution (escaping literal `%` as `%%`). [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Correct — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **D:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.

</details>

### Q082 (`E2Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

A cloud flow invokes `Run a flow built with Power Automate for desktop` in `Unattended` mode while four `Normal` priority batch jobs are already queued on the target machine. How can this urgent STAT lab order jump ahead of `Normal` queued jobs automatically?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Setting the `Priority` parameter on `Run a flow built with Power Automate for desktop` to `High` schedules the STAT run ahead of `Normal` queued items. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Correct — Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q083 (`E2Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

An oncology registry web page nests lab result rows inside `<table class="obs-grid"><tbody><tr><td class="loinc">...</td></tr></tbody></table>`. Complete the CSS selector for all LOINC cells: `table.obs-grid > tbody > tr > ____`. Which web extraction approach applies?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). CSS selectors (`td.loinc`) in `Extract data from web page` and Web UI elements cleanly query structured DOM hierarchies without brittle positional indexes. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q084 (`E2Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

A health-tech ISV is packaging a HIPAA-compliant DICOM header anonymizer as a custom Power Automate for desktop action module for three hospital environments. Select the required build-and-deploy sequence.

- **A.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically
- **B.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop
- **C.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD
- **D.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Custom desktop actions inherit `ActionBase`, compile into a `.cab` archive signed with a trusted certificate, upload to Dataverse Custom actions, and deploy inside Solutions. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.
- **B:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).
- **C:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.
- **D:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.

</details>

### Q085 (`E2Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

A daily lab-director digest cloud flow filters an array of 800 specimen results down to `Abnormal == true` and formats the filtered rows as a downloadable `.csv` email attachment without `Apply to each`. Which two Data Operations should you chain? Select two.

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **E.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). `Filter array` subsets the abnormal rows in memory, and `Create CSV table` serializes the filtered array directly into CSV text for the email attachment. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **E:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.

</details>

### Q086 (`E2Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A cloud flow receives a SOAP XML payer acknowledgment and must count how many `<ClaimError>` nodes exist: `length(____(xml(outputs('SOAP_Body')), '//ClaimError'))`. Which WDL function completes this formula?

- **A.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **B.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `xpath(xml(...), '//ClaimError')` returns an array of matching XML nodes whose count is evaluated with `length(...)`. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **B:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **C:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q087 (`E2Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

A healthcare integration team is wrapping an internal RESTful MPI (Master Patient Index) service for both Canvas apps and cloud flows. Which two components are required in the Dataverse Solution? Select two.

- **A.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **E.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). A solution-aware Custom Connector defines the MPI REST operations and security, while a Connection Reference binds cloud flows to the environment-specific Connection. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **E:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.

</details>

### Q088 (`E2Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

At the end of every unattended EHR desktop run (including inside error-recovery routines), the bot must close open EHR windows cleanly or force-terminate hung `EhrClient.exe` processes so the next run starts clean. How should this be structured?

- **A.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **B.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Encapsulating graceful `Close window` / `Terminate process` cleanup inside a dedicated `Cleanup_Apps` subflow invoked from both `Main` completion and `On block error` keeps VMs clean. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **B:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>

### Q089 (`E2Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow reads 1,500 CPT fee rows into `%FeeTable%` and needs all rows where `Department == 'Cardiology'` extracted into `%CardioRows%` without launching Excel. Which built-in PAD variable action accomplishes this?

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Filter data table` (alongside `Find or replace in data table`) filters in-memory `Datatable` variables directly inside Power Automate for desktop. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **C:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

## Case Study Vignette — Beacon Care Network

> [Scenario: Beacon Care Network scales seasonal open-enrollment RPA spikes without maintaining physical servers by provisioning Power Automate Hosted Machine Groups from a custom Azure Compute Gallery VM image, enforcing custom connector host DLP rules, and separating headless Entra Service Principals from interactive Windows bot accounts.]

### Q090 (`E2Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — Beacon Care Network: How does Beacon Care Network absorb 10× open-enrollment RPA spikes from a custom golden VM image without maintaining physical hypervisors year-round?

- **A.** Attended run mode executing inside a signed-in user’s active desktop session
- **B.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate **Hosted Machine Groups** (`Hosted RPA`) pull custom VM images from **Azure Compute Gallery** and auto-scale unattended Azure bot VMs on demand. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **B:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q091 (`E2Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — Beacon Care Network: Beacon Care Network’s security team wants to ensure Custom Connectors in the enrollment environment can ONLY connect to `https://api.beaconcare.org/*` while blocking any other host. Which DLP feature enforces this?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). DLP **Custom connector URL pattern** / **Connector endpoint filtering** rules allow `https://api.beaconcare.org/*` and set the catch-all `*` rule to `Deny`. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q092 (`E2Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — Beacon Care Network: Beacon’s Ops Command Center monitors 60 enrollment bots in Power Automate portal to identify bottlenecked Hosted Machine Groups, queue wait durations, and top failure error codes across the last 24 hours. Which portal capability provides this?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Monitor -> Desktop flow runs`, `Machines`, and **Automation Center** provide cross-group queue wait analytics, machine utilization, action failure codes, and run history. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q093 (`E2Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

An unattended VM refuses to load a newly uploaded `.cab` Custom Action module at runtime with a digital signature verification failure. What must be true on every bot VM running that custom action?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Every target bot machine must trust the code-signing certificate chain (Root/Intermediate CA in Windows Certificate Store) used to sign the `.cab` Custom Action package. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q094 (`E2Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

A healthcare cloud architect is comparing self-managed Windows Server RDSH bot hosts against Microsoft **Hosted Machine Groups** (`Hosted RPA`). Which two statements are accurate? Select two.

- **A.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **E.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Hosted Machine Groups automatically provision and scale Azure VMs from default or Azure Compute Gallery images, while self-managed Windows Server RDSH hosts enable concurrent multi-session unattended runs. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **E:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q095 (`E2Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

After a tenant admin updates an environment DLP policy to block the `VBScript` and `Command line (DOS)` desktop flow modules, what happens to an existing Production desktop flow that contains a `Run VBScript` action?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate flags the violating desktop flow as non-compliant with DLP, suspends it, and blocks execution until the prohibited `Run VBScript` action is removed or exempted. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.

</details>

### Q096 (`E2Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

A parent cloud flow passes `{"mrn":"88412","facility":"West"}` to `Run a Child Flow` inside a Dataverse Solution. Which trigger types are supported inside the Child Cloud Flow?

- **A.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Child cloud flows use `Manually trigger a flow` (Instant) or `When an HTTP request is received` paired with `Respond to a Power App or flow` / `Response`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>

### Q097 (`E2Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

A hospital wants a single beefy Azure VM (`Standard_D8s_v5`) to execute **8 unattended desktop flows concurrently** under 8 distinct bot user accounts at the same time. Which Windows OS configuration supports high-density multi-session unattended RPA on one VM?

- **A.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Attended run mode executing inside a signed-in user’s active desktop session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Windows Server (2019/2022/2025) configured with **Remote Desktop Session Host (`RDSH`)** supports multiple concurrent unattended Windows sessions on a single registered machine. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.

</details>

### Q098 (`E2Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow calls a rate-limited pharmacy NDC lookup API returning `HTTP 429`. Proposed solution: Keep `Retry Policy` set to `Exponential Interval` (`Count: 4`, `Interval: PT15S`, `Minimum: PT10S`, `Maximum: PT2M`). Does this align with Power Automate resilience best practices?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — idempotent GET lookups encountering `HTTP 429` or `5xx` recover cleanly with bounded `Exponential Interval` retry policies. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q099 (`E2Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A payer web portal disables standard keyboard pasting on a date picker, requiring `document.querySelector('#serviceDate').value = '2026-10-30'` to execute inside the live Chrome tab. Why will the system `Run JavaScript` action fail here, and what should you use instead?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). System `Run JavaScript` runs offline in Windows Script Host with no `document`/`window` DOM; `Run JavaScript function on web page` executes directly inside the open browser tab. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q100 (`E2Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A legacy lab system posts CSV lines (`MRN,TestCode,Result`) in an email body, and a cloud flow splits lines on `\r\n` and fields on `,` while safely handling missing optional notes via `coalesce(...)`. Which WDL function category handles string/JSON null-safe parsing in cloud flows?

- **A.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). WDL string/JSON expressions (`split()`, `json()`, `coalesce()`, `?` null-conditional indexing) parse delimited and JSON payloads in cloud flows without failing on optional fields. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **B:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).

</details>
