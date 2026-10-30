# Microsoft Exam PL-500: Practice Exam 6 — Public-Sector Document Automation, DLP & Enterprise ALM — Reviewer Study Key

**Theme:** Raw JSON Invoke web service, multi-page CSS table scraping, solution Child Flows, Desktop Flow module DLP, and Managed pipeline upgrades  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E6Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

Federal `Grants.gov` feeds deliver XML award notices `<Award><UEI>ZK9918273612</UEI></Award>`, and Solstice’s cloud flow extracts the UEI text via `____(xml(outputs('Award_XML')), 'string(//Award/UEI/text())')`. Which WDL function completes this?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `xpath(xml(...), 'string(//Award/UEI/text())')` parses XML payloads and evaluates XPath queries natively in cloud flows. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q002 (`E6Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

An agency infrastructure team shares `MG-TaxFilingPool` with the Production pipeline’s connection identity so it can run unattended bots on the pool without adding/removing VMs. Which Machine Group permission should be granted?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Grant **User** permission (not `Co-owner`) on `MG-TaxFilingPool`. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q003 (`E6Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

Atlas collects scraped vendor TINs into `%VendorTinList%`, removes duplicate TINs via `Remove duplicate items from list`, and reads threshold rules from `%ConfigObj['maxBid']%`. Which PAD variable types are used?

- **A.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A Power Automate for desktop `List` (`%VendorTinList%`) and a `Custom object` (`%ConfigObj%`). [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **B:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q004 (`E6Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

An agency Custom Connector routes `/v1/permits` calls to `https://permits.civic.gov` and `/v1/inspections` calls to `https://inspections.civic.gov` without custom code. Which Custom Connector **Policy template** routes sub-paths to different backend hosts?

- **A.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Route request` (and `Set host URL`) policy templates route Custom Connector operations to distinct backend endpoints codelessly. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **B:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q005 (`E6Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

An agency cloud flow calls a state treasury Azure API Management gateway secured by Microsoft Entra ID OAuth 2.0 (`Audience = api://state-treasury`). Which built-in `HTTP` action Authentication type handles token acquisition natively?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `ActiveDirectoryOAuth` (or `Managed Identity`) in the cloud `HTTP` action acquires Entra bearer tokens natively without custom token flows. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Correct — Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.

</details>

### Q006 (`E6Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

Which two design patterns together provide resilient cloud-and-desktop exception management across an agency RPA solution? Select two.

- **A.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **E.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Cloud `Try`/`Catch` `Scope` blocks (`Configure run after`: failed/skipped/timed out) catch orchestration errors, while PAD `On block error` blocks recover local UI system faults. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **E:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.

</details>

### Q007 (`E6Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

Solstice Research Grants calls a reusable solution Child Cloud Flow `Verify_SAM_Exclusion` from 11 parent award flows. Which action at the end of `Verify_SAM_Exclusion` passes `{IsExcluded: false, CageCode: "8A1B2"}` back to the parent flow?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **C.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **D.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Respond to a Power App or flow` or the HTTP `Response` action returns synchronous structured outputs from a Child Cloud Flow. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **C:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **D:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.

</details>

### Q008 (`E6Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Vanguard Civic Cloud’s security baseline blocks `Run DOS command`, `Run PowerShell script`, and `Run VBScript` across all Production desktop flows while permitting `Browser`, `UI automation`, `PDF`, and `Excel`. Which governance feature enforces this?

- **A.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Desktop flow module and action DLP** governance in Power Platform Admin Center. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **B:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q009 (`E6Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

Atlas structures its 380-action bid-evaluation bot into `Main`, `Scrape_Portal`, `Merge_Workbooks`, and `Recover_Portal` Subflows. Which PAD action invokes `Merge_Workbooks` from `Main` and returns to the very next step in `Main` when finished?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **C.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **D.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run subflow` invokes `Merge_Workbooks` (and `Exit subflow` returns early if needed) while sharing variables globally across the desktop flow. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **C:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **D:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.

</details>

### Q010 (`E6Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

An unattended desktop flow checks whether the warning text `'SESSION TIMED OUT'` appears on a non-accessible legacy Java applet window using built-in Windows 11 English OCR (`Engine = ____`). Which fast local OCR option requires zero external files?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop OCR actions (`Extract text with OCR` / `If text on screen (OCR)`) configured with the **Windows OCR engine** leverage native OS language packs locally. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Correct — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.

</details>

### Q011 (`E6Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

Which two built-in security/identity constructs enforce least privilege for registering vs using RPA machines in Dataverse? Select two.

- **A.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **E.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Separate `Desktop Flows Machine Owner` (register/manage machines) from `Desktop Flows Machine User` (use shared machines), and separate Entra Service Principals from interactive Windows bot accounts. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **E:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.

</details>

### Q012 (`E6Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

An agency developer opens a 250-action desktop flow in PAD Designer, sets a `1000 ms` **Run delay**, places **Breakpoints** before each portal submission, and watches `%BidTable%` populate in the **Variables** pane. Which capability set is used?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop Designer’s built-in debugging suite (`Breakpoints`, `Run delay`, `Run from here`, `Run next action`, `Variables` pane). [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.

</details>

### Q013 (`E6Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A procurement desktop flow iterates through `%BidTable%` rows with `For each` (`%CurrentRow%`), skipping withdrawn bids via `Next loop` and stopping early if a disqualifying court injunction flag appears via `____` (`Exit loop`). Which PAD module provides these controls?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop’s **Loops** module (`For each`, `Loop`, `Loop condition`, `Next loop`, `Exit loop`). [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **D:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.

</details>

### Q014 (`E6Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A public-works inbox receives unstructured citizen pothole and storm-drain emails, and a cloud flow must extract structured JSON (`StreetAddress`, `HazardType`, `Urgency`) or draft a polite acknowledgment using GPT instructions. Which AI Builder option fits?

- **A.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **B.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **C.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). AI Builder `Create text with GPT using a prompt` (`AI Prompts`) extracts structured entities or drafts grounded responses in cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Correct — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **B:** Incorrect — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **C:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **D:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q015 (`E6Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A grant-disbursement cloud flow polls a treasury ACH batch status endpoint inside a `Do until` loop (`Count = 30`, `Timeout = PT30M`) and formats settlement dates via WDL `formatDateTime(utcNow(), 'yyyy-MM-dd')`. Which cloud control + expression pair applies?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Cloud `Do until` loops with explicit `Count`/`Timeout` guardrails paired with WDL `formatDateTime()` expressions. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q016 (`E6Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

Grant officers trigger a parent cloud flow that runs an **Attended** helper desktop flow on each officer’s own workstation (`Run-only users -> Provided by run-only user` on the Desktop flows connection). Why is `Attended` mode required here instead of `Unattended`?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Attended run mode executing inside a signed-in user’s active desktop session
- **C.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **D.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The flow runs interactively on the signed-in grant officer’s active laptop session while they watch and collaborate, which requires `Attended` mode. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **C:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **D:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.

</details>

## Case Study Vignette — Atlas Municipal Procurement

> [Scenario: Atlas Municipal Procurement scrapes paginated vendor bid tables across multi-frame government portals using Power Automate for desktop `Extract data from web page` CSS selectors, deduplicates vendor lists, merges Excel bid workbooks (`Get first free column/row`), and wraps fragile portal screens inside `On block error` -> `Run subflow` recovery blocks.]

### Q017 (`E6Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — Atlas Municipal Procurement: Atlas also receives scanned PDF subcontractor insurance certificates by email where procurement clerks review `< 90%` confidence fields in a Canvas Validation Station app. Which Microsoft solution starter provides this?

- **A.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **B.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The **Microsoft Document Automation Toolkit** combines email capture, AI Builder Document Processing, Dataverse tables, and the Canvas Validation Station app. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **B:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q018 (`E6Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — Atlas Municipal Procurement: Atlas’s government bid portals change dynamic row `id` attributes on every pagination step while keeping stable `<tr data-bid-row="...">` tags. How should Atlas configure its Web UI selectors in PAD?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Uncheck volatile `id` attributes in Selector Builder and match stable `data-bid-row` / CSS attributes with `%Variable%`, `Contains`, or `Regex` operators. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q019 (`E6Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — Atlas Municipal Procurement: After merging bid workbooks (`Get first free column/row`), Atlas’s bot posts raw JSON award summaries (`{"rfp":"MUNI-44","awarded":true}`) via `Invoke web service` (`Encode request body = Off`) to an intranet registry. Why must `Encode request body` be `Off`?

- **A.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **D.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Leaving `Encode request body` enabled URL-encodes `{` and `:` characters in raw JSON bodies; switching it `Off` sends valid unencoded JSON. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **D:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q020 (`E6Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A security-hardened workstation bot queries Windows Event Log ID `4625` via `Get-WinEvent` in Power Automate for desktop and returns JSON text in `%PowershellOutput%`. Which PAD action runs this PowerShell query?

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`
- **C.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run PowerShell script` runs local PowerShell cmdlets and `.NET` calls while interpolating `%Variable%` tokens. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Correct — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.
- **C:** Incorrect — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q021 (`E6Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

An agency maker only needs to concatenate three strings and write 15 lines to a single local `.txt` log inside an existing desktop flow on one VM. Should you build a custom `.NET` `.cab` SDK module and a Dataverse Work Queue for that task?

- **A.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No — standard built-in PAD Text/File actions handle simple local string/file tasks directly; reserve Work Queues for multi-bot transactional backlogs and Custom Actions for reusable `.NET` domain SDKs. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q022 (`E6Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

An agency desktop bot automates legacy Word/COM mail-merge templates via `CreateObject("Word.Application")` inside `Run VBScript` and checks `%____%` (`%ScriptError%`) for COM errors. Which scripting action executes `.vbs` code?

- **A.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Run VBScript` executes Windows COM automation scripts locally and outputs `%VBScriptOutput%` and `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Correct — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q023 (`E6Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A federal grants REST feed returns 200 awards per page (`@odata.nextLink`) across 7,400 active grants. Proposed solution: Enable `Pagination` on the cloud `HTTP` action and set `Threshold = 10000`. Does this fetch all 7,400 grants automatically?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — enabling `Pagination` with `Threshold >= 7400` follows continuation links automatically until all pages are retrieved. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q024 (`E6Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

An agency developer configures a Custom Connector with Microsoft Entra ID OAuth 2.0 and adds a `Script : ScriptBase` C# transform (`ExecuteAsync()`) to normalize legacy date strings. Which two platform rules apply? Select two.

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **D.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`
- **E.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). OAuth 2.0 secures backend API calls, and `ScriptBase` C# code must execute in `<= 5 seconds` with `<= 1 MB` maximum code size. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **D:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.
- **E:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q025 (`E6Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

Why do government ALM standards require every solution cloud flow to connect to `Dataverse`, `SharePoint`, and `Desktop flows` via **Connection References** rather than embedded personal Connections?

- **A.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Connection References allow Managed Solutions to rebind cleanly to agency service-account Connections in UAT and Production without modifying flow definitions or creating Unmanaged Active layers. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q026 (`E6Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Atlas Municipal Procurement scrapes paginated `<table class="bids"><tbody><tr><td data-field="vendor_tin">...</td></tr></tbody></table>` grids across portal pages using CSS selector `table.bids tbody tr td[____="vendor_tin"]`. Which web automation approach applies?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Extract data from web page` configured with CSS attribute selectors (`td[data-field="vendor_tin"]`) and a Next-page pager extracts multi-page HTML tables reliably. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q027 (`E6Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

In addition to Custom Connector URL patterns, an admin restricts the built-in `SQL Server` and `HTTP` connectors in Production so makers can ONLY connect to `sql-prod.civic.gov` and `https://ledger.civic.gov/*`. Which DLP feature accomplishes this?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Connector endpoint filtering** in Power Platform DLP policies restricts allowed server/host endpoints on `HTTP`, `SQL Server`, `Dataverse`, `SharePoint`, `Blob`, and `SMTP` connectors. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q028 (`E6Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

During tax-withholding validation, a filing lists an invalid 7-digit EIN (`ERR_INVALID_EIN_FORMAT`). Proposed solution: Immediately treat `ERR_INVALID_EIN_FORMAT` as a **Business Exception**, skip all UI retries, update the Work Queue item to `On hold` with reason `ERR_INVALID_EIN_FORMAT`, and notify a tax examiner. Is this correct?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — malformed taxpayer data is a deterministic Business Exception that will never self-heal via UI retries and belongs in human exception review. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.

</details>

### Q029 (`E6Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

When configuring `Verify_SAM_Exclusion` as a solution Child Cloud Flow, which two platform requirements must be met so `Run a Child Flow` saves without error? Select two.

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied
- **C.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **E.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Package both flows inside a Dataverse Solution and configure the child flow’s `Run only users` settings to `Use this connection`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.
- **C:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **E:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q030 (`E6Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

CivicBridge Revenue Agency is deploying the Microsoft Document Automation Toolkit for employer tax forms. Place the four processing stages in exact runtime order.

- **A.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream
- **B.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **C.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows
- **D.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Email intake cloud flows capture PDFs, AI Builder Document Processing extracts fields & confidence scores, clerks validate low-confidence forms in Canvas Validation Station, and verified Dataverse rows flow downstream. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.
- **B:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **C:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.
- **D:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.

</details>

### Q031 (`E6Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

When 60 quarterly tax-reconciliation runs enter `MG-CivicLedger` (`6` VMs) at `Normal` priority and a statutory court-ordered refund bot is triggered at `High` priority, how does the Machine Group handle load balancing and priority?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `MG-CivicLedger` distributes runs across all 6 healthy VMs and dispatches the waiting `High` priority refund run to the very next VM that becomes free. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q032 (`E6Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

Vanguard Civic Cloud’s RPA Center of Excellence mandates externalized stage settings and thorough offline/interactive testing before UAT sign-off. Which three capabilities enforce this? Select three.

- **A.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **E.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **F.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, D` (`CSV: 2,3,4`)

Correct answers: B, C, and D (are correct). Dataverse `Environment Variables` & JSON config files, PAD Designer debugging tools, and cloud `Static Result` action mocking. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **B:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **D:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **E:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **F:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q033 (`E6Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

A state agency automates three distinct systems: a local Win32 caseworker client, a federal grants portal in Google Chrome, and an app streamed over Microsoft Remote Desktop (`RDP`) where agency IT installs the virtual desktop agent on the RDS host. Which three interaction capabilities apply? Select three.

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **C.** Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **E.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **F.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, F` (`CSV: 2,3,6`)

Correct answers: B, C, and F (are correct). Windows UIA automates local Win32 apps, the Chrome Power Automate extension exposes DOM nodes, and the Power Automate agent for virtual desktops enables UI selectors over RDP/Citrix. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **C:** Correct — UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **E:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **F:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q034 (`E6Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Caseworkers use an internal agency intranet web directory that launches a local attended redaction helper bot via hyperlink: `ms-powerautomate:/console/flow/run?environmentid=____&workflowid=____`. Which desktop flow execution method is this?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate console URLs (`ms-powerautomate:/console/flow/run?...`) invoke local attended desktop flows directly from links, scripts, or Task Scheduler. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Correct — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **D:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q035 (`E6Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

Which two technical requirements prevent common unattended desktop flow session failures across single-session Windows 11 VMs and multi-session Windows Server hosts? Select two.

- **A.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **B.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **E.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Keep all human RDP sessions completely **signed out** on single-session VMs (or enable RDSH on Windows Server) and eliminate all interactive modal dialogs in `Unattended` mode. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Correct — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **B:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **E:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q036 (`E6Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Eight unattended bots process 30,000 quarterly employer wage filings that require statutory filing SLAs (`ExpiresOn`), priority boosts for amended returns, and duplicate `EIN_Quarter` rejection. Which Power Automate capability should you design?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dataverse **Work Queues** enforce `Unique reference` deduplication, `ExpiresOn` SLAs, priority ordering, and multi-bot concurrent item leasing. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q037 (`E6Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

Solstice Research Grants receives federal award JSON feeds, validates schema tokens, and emails finance directors an HTML summary grid. Which two Data Operations should the cloud flow use? Select two.

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **C.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). `Parse JSON` generates typed schema tokens and `Create HTML table` formats the award array into an HTML table. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **C:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q038 (`E6Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

When Vanguard Civic Cloud retires an old desktop sub-bot in `CivicTaxRPA` v2.2 and deploys via pipeline to Production, which import mode removes the retired desktop flow while keeping all Dataverse `TaxAudit` rows intact?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Managed Solution **Upgrade** (`Stage for upgrade` -> `Apply upgrade`) deletes retired solution components cleanly without dropping retained tables. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.

</details>

### Q039 (`E6Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

Atlas Municipal Procurement merges 18 vendor Excel bid sheets into a master workbook by opening `MasterBids.xlsx` and calling `____` (`Get first free column/row from Excel worksheet`) before each `Write to Excel worksheet`. Which PAD action set applies?

- **A.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Launch Excel`, `Get first free column/row from Excel worksheet` (`%FirstFreeRow%`), `Write to Excel worksheet`, and `Close Excel` merge workbooks cleanly. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **D:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q040 (`E6Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

A grants-management developer is wiring a parent solution cloud flow to run an attended/unattended desktop flow and consume `%VoucherId%` in Dataverse. Select the four-step implementation sequence.

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **C.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod
- **D.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Declare Input/Output variables in the solution desktop flow, add `Run a flow built with Power Automate for desktop`, bind Machine/Group Connection Reference & Inputs, and reference Output tokens. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **C:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.
- **D:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.

</details>

### Q041 (`E6Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

When authoring a `.NET Framework` Custom Action for Power Automate for desktop, what archive file format (`*.____`) is produced by the CAB packaging step before `signtool` digital signing and portal upload?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **D.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Custom action assemblies and manifests are packaged into a signed **`.cab`** archive uploaded as a Dataverse `Desktop Flow Module`. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **D:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

## Case Study Vignette — Vanguard Civic Cloud

> [Scenario: Vanguard Civic Cloud operates zero-footprint Azure Hosted Machine Groups alongside on-premises registered machines via Power Automate machine runtime. Security architects enforce environment DLP policies blocking `Run DOS command` and unapproved custom connector hosts while automating Dev -> Test -> Prod deployments with Connection References and Environment Variables.]

### Q042 (`E6Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — Vanguard Civic Cloud: How does Vanguard Civic Cloud run zero-footprint elastic Azure bot VMs that auto-scale from a hardened agency VM image without managing hypervisors alongside its on-premises `Power Automate machine runtime` machines?

- **A.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **D.** Attended run mode executing inside a signed-in user’s active desktop session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Provisioning Power Automate **Hosted Machine Groups** (`Hosted RPA`) backed by a custom image in **Azure Compute Gallery**. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **D:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.

</details>

### Q043 (`E6Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — Vanguard Civic Cloud: Vanguard’s security architects enforce environment DLP rules blocking `Run DOS command` in desktop flows AND blocking unapproved Custom Connector hosts. Which DLP capability blocks `Run DOS command` inside Power Automate for desktop?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Desktop flow module and action DLP** governance blocking the `Command line (DOS)` module/actions in Power Platform Admin Center. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q044 (`E6Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — Vanguard Civic Cloud: During live grant-deadline surges, Vanguard’s operations center monitors Hosted Machine Group queue depth, promotes statutory deadline runs (`High` + `Move to top`), and reviews failure screenshots in Power Automate portal. Which portal area provides run history and machine analytics?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Monitor -> Desktop flow runs`, `Machines`, and **Automation Center** in Power Automate portal. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q045 (`E6Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Solstice Research Grants lets 40 grant officers trigger an Instant parent cloud flow that invokes an attended helper desktop flow on each officer’s laptop, **without** granting officers `Co-owner` rights to edit the desktop flow logic. Which sharing configuration fits?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Share the Desktop flow with **User** permission (not `Co-owner`) and expose the parent cloud flow via **Run-only users**. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.

</details>

### Q046 (`E6Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A Dataverse `GrantApplication` cloud flow must ONLY fire when `RequestedAmount >= 100000` and `Stage == 'FinalReview'`: `@and(greaterOrEquals(triggerOutputs()?['body/cr77_requestedamount'], 100000), ____(triggerOutputs()?['body/cr77_stage'], 'FinalReview'))`. Which trigger feature applies?

- **A.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **B.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **C.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Trigger Conditions (`@and(greaterOrEquals(...), equals(...))`) filter non-matching updates before any cloud flow run starts. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **B:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **C:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **D:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q047 (`E6Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

Solstice Research Grants requires federal treasury API secrets to stay protected in Key Vault and masked across both parent cloud Run History and PAD variable logs. Select the four-step implementation sequence.

- **A.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs
- **B.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step
- **C.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing
- **D.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Store secrets in Key Vault Credentials / Secret Env Vars, enable Cloud `Secure Inputs/Outputs`, mark PAD variables `Sensitive`, and verify redaction in logs. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.
- **B:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.
- **C:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.
- **D:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.

</details>

### Q048 (`E6Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

How do on-premises agency VMs register to a specific Power Platform environment today without deploying the legacy On-Premises Data Gateway?

- **A.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **D.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Install Power Automate for desktop and register the host directly to the target environment inside the **Power Automate machine runtime** app. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **D:** Correct — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.

</details>

### Q049 (`E6Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

CivicBridge’s desktop bot calls a legacy state SOAP 1.1 tax-lien registry (`https://liens.gov.intra/LienService?wsdl`) from the bot VM. Which built-in PAD action imports the WSDL and invokes SOAP operations?

- **A.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Invoke SOAP web service` imports WSDL definitions and sends typed XML SOAP envelopes directly from Power Automate for desktop. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Correct — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **B:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q050 (`E6Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

An agency processes 4,000 scanned PDF W-9 and employer withholding forms daily in cloud flows, requiring table/field extraction plus field-level confidence scores. Which Microsoft AI model type should you choose?

- **A.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). AI Builder **Document Processing** extracts structured form fields, checkboxes, and tables with confidence scores in cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **D:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q051 (`E6Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A legacy treasury ledger deadlocks whenever more than **3** cloud flows write voucher batches simultaneously. Setting trigger `Concurrency Control = On` and `Degree of Parallelism = ____` (`3`) throttles active runs safely. Which setting is this?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Trigger `Concurrency Control` (`Degree of Parallelism = 3`) caps concurrent cloud flow runs at 3 while queuing overflow triggers in order. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).

</details>

### Q052 (`E6Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A municipal web portal occasionally drops an AJAX table page load once every 200 clicks due to brief load-balancer resets. Configuring `Retry action if an error occurs` (`Times = ____`, `Interval = 3s`) on the web action’s `On error` policy recovers automatically. Which capability is this?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Action-level `On error` retry policies in Power Automate for desktop re-attempt transient UI/network glitches declaratively before escalating. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q053 (`E6Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A public-sector RPA architect is categorizing agency automation intake requests. Which two scenarios map to an **Automated** cloud flow and a **Scheduled** cloud flow respectively? Select two.

- **A.** Automated cloud flow triggered asynchronously by an external connector event
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **E.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Triggering immediately when a citizen document arrives in SharePoint is `Automated`, whereas running every Friday at 22:00 to archive court dockets is `Scheduled`. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **E:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q054 (`E6Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

A county treasury clerk office still reconciles property-tax rolls on an `IBM 3270` mainframe host alongside a local WPF cashiering app. Which two-part interaction capability in Power Automate for desktop avoids pixel scraping on the mainframe?

- **A.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Built-in Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) automate `IBM 3270` green screens natively by row/column coordinates. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **B:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q055 (`E6Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A state cryptography unit wants agency RPA developers to validate digital court-seal signatures inside Power Automate for desktop using a signed `.NET Framework` `.cab` toolbox package (`Desktop Flow Module`). What feature is this?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Custom actions built with the Power Automate Custom Actions SDK (`ActionBase`), packaged as signed `.cab` archives, and uploaded to Dataverse Custom actions. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q056 (`E6Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

Vanguard Civic Cloud promotes Managed RPA Solutions (`CivicTaxRPA`) from Dev through Test to Production via Power Platform pipelines. Select the compliant four-step ALM sequence.

- **A.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **B.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts
- **C.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs
- **D.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Package artifacts in an Unmanaged Dev Solution, clear Dev values & export Managed, verify target Prod Machine Groups/Credentials, and deploy Managed Upgrade binding stage references. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **B:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.
- **C:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.
- **D:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.

</details>

### Q057 (`E6Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

An agency inspector checks Production before approving an RPA release. Which two findings confirm clean enterprise ALM? Select two.

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **E.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). All RPA solutions in Production are **Managed** (upgraded via pipelines) and zero flows carry overriding **Unmanaged Active layers**. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **E:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q058 (`E6Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

A cloud flow receives a 4,000-row JSON vendor array and needs ONLY rows where `Debarred == false`, reshaped into `{TIN, LegalName}` with zero `Apply to each` actions. Which two-action Data Operation pipeline achieves this?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Filter array` followed by `Select` filters and projects JSON arrays in memory without loop overhead. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **C:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q059 (`E6Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

Atlas Municipal Procurement wraps fragile multi-frame bid-portal scraping actions inside `On block error`. When a portal frame crashes, `On block error` captures `%LastError%`, invokes subflow `Recover_Portal`, and sets `Continue flow run -> Go to beginning of block` (up to 2 attempts). Which exception class is this handling?

- **A.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Transient portal crashes and broken frames are **System Exceptions** recovered cleanly via `On block error` + `Run subflow`. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q060 (`E6Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Field housing inspectors use a Power Apps Canvas app to upload inspection checklists and synchronously display the generated case number: `UpdateContext({locCaseNo: CreateInspectionFlow.____(JSON(colChecklist)).caseno})`. Which trigger pattern applies?

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Canvas apps call solution-aware Instant cloud flows via `FlowName.Run(...)` (Power Apps V2 trigger) paired with `Respond to a Power App or flow`. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Correct — Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.

</details>

### Q061 (`E6Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

An agency auditor requests proof of every unattended desktop flow run over the past 30 days, including start/end timestamps, executing machine name, queue wait duration, and action-level error details. Where in Power Automate portal is this inspected?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **C.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Monitor -> Desktop flow runs`, `Machines`, and **Automation Center** (backed by Dataverse `FlowSession` tables). [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **C:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q062 (`E6Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

If `Scrape_Portal` detects that the statutory bid-opening embargo timestamp has not yet arrived (`%EmbargoActive% = True`), the bot must abort the entire desktop flow run immediately with error `'EMBARGO_ACTIVE'`. Which PAD action should execute?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **D.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Stop flow` configured `With error message` (`'EMBARGO_ACTIVE'`) immediately terminates the entire desktop flow and reports failure to the caller. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Correct — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **D:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.

</details>

### Q063 (`E6Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A public procurement portal renders bid totals inside a shadow-DOM custom widget, requiring `function ____() { return document.querySelector('bid-summary').shadowRoot.textContent; }` inside the active browser tab. Which PAD action executes this?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run JavaScript function on web page` executes `ExecuteScript()` inside the live browser tab DOM. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Incorrect — `Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.

</details>

### Q064 (`E6Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

During peak tax day, 150 runs accumulate in `MG-CivicLedger`’s queue, and 12 duplicate runs were accidentally triggered for an obsolete batch. Which portal Run Queue capability lets an operator abort those 12 queued runs immediately before they consume bot minutes?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Open `Monitor -> Machines -> MG-CivicLedger -> Run queue` and select **Cancel** on the 12 obsolete queued runs (alongside `Change priority` / `Move to top` for urgent items). [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.

</details>

### Q065 (`E6Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

A civic-tech architect compares calling a public federal SAM.gov REST API from a cloud flow versus calling an air-gapped municipal vault service at `http://127.0.0.1:8440/sign` on a bot workstation. Which two HTTP action choices fit? Select two.

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **E.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Call public federal APIs headlessly via the cloud `HTTP` action, and call `127.0.0.1` workstation-local services via PAD `Invoke web service`. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **E:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q066 (`E6Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A state revenue agency captures tax-clearance requests via Microsoft Forms, routes supervisor sign-off in Teams, and then enters clearance stamps into a 1999 Win32 tax-lien desktop client that has no API or direct SQL write support. Which architecture fits?

- **A.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **B.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **C.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow
- **D.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A hybrid design combines an Automated cloud flow (Forms trigger + Teams approval) with an unattended desktop flow driving the legacy Win32 tax-lien client. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **B:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **C:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.
- **D:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

## Case Study Vignette — Solstice Research Grants

> [Scenario: Solstice Research Grants orchestrates grant-disbursement parent cloud flows calling modular solution Child Flows, parsing XML/JSON federal award feeds, guarding secrets with `Secure Inputs`/`Secure Outputs`, and invoking attended desktop helper flows on grant officers’ laptops with `Run-only users` permissions.]

### Q067 (`E6Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — Solstice Research Grants: A federal grants reporting portal computes indirect-cost caps inside `window.calcIndirectCap()` in the open browser tab rather than static HTML elements. Which PAD action executes `function ExecuteScript() { return window.calcIndirectCap(); }` directly on the page?

- **A.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **D.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run JavaScript function on web page` executes JavaScript directly inside the active browser tab’s DOM context. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **D:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.

</details>

### Q068 (`E6Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — Solstice Research Grants: Solstice passes federal award API keys and sensitive grantee tax IDs across parent cloud flows, Child Cloud Flows, and desktop helper flows. Which cloud action Settings switches mask those values in Cloud Run History?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enabling **Secure Inputs** and **Secure Outputs** in cloud flow action Settings (paired with `Sensitive` variables in PAD). [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.

</details>

### Q069 (`E6Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — Solstice Research Grants: Solstice wraps a federal grant-verification feed in a Custom Connector that needs `< 5-second` C# XML-to-JSON normalization and checksum verification (`public class Script : ____`). Which Custom Connector capability applies?

- **A.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **B.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Custom Connector C# code (`Script : ScriptBase`, overriding `ExecuteAsync()`) executing within the `5-second` and `1 MB` limits. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **B:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **C:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q070 (`E6Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

An agency queues 24 unattended records-request desktop flows at 18:00 targeting a Machine Group of **4 single-session Windows 11 Enterprise VMs**. Proposed solution: Expect 4 runs to execute concurrently across the 4 VMs while the remaining 20 wait in FIFO/priority order in the Machine Group queue. Is this how Machine Group concurrency works?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — each single-session Windows 11 VM runs 1 unattended session at a time (`4` concurrent runs across `4` VMs), while queued runs dispatch automatically as VMs finish. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q071 (`E6Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

An agency sysadmin is registering six hardened on-premises Windows VMs into `MG-CivicLedger` in Production using Power Automate machine runtime. Place the four steps in exact order.

- **A.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference
- **B.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests
- **C.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **D.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create `MG-CivicLedger` in Portal, register each VM to Production via Power Automate machine runtime, join `MG-CivicLedger` using the group password/key, and share as `User` with Connection References. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.
- **B:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.
- **C:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **D:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.

</details>

### Q072 (`E6Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

Proposed solution: Share a single `DEV\rpa-bot-shared` Windows account and Machine Group across Dev, Test, and Production so developers never have to configure Connection References on import. Does this comply with Power Platform environment isolation?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No — sharing credentials and Machine Groups across Dev and Production violates least-privilege isolation and risks test flows mutating Production data; isolate Credentials and Machine Groups per stage. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q073 (`E6Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

A municipal IT team wraps an internal OpenAPI 3.0 parcel-assessment REST service for use across 15 solution cloud flows. Which two solution components are required? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **E.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Build a solution-aware **Custom Connector** from the OpenAPI definition and bind cloud flows through a **Connection Reference**. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **E:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.

</details>

### Q074 (`E6Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

Which two sharing distinctions protect Production RPA flows and Machine Groups from unauthorized structural edits? Select two.

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **E.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Assign `User` instead of `Co-owner` on Desktop flows for execution-only access, and `User` instead of `Co-owner` on Machine Groups for run-dispatch connections. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **E:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q075 (`E6Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

A revenue-agency desktop flow extracts tables from digital PDF tax schedules, reads an XML municipal-code directory via XPath, and reads a comma-delimited vendor master CSV into a Datatable. Which three PAD capabilities cover all three tasks? Select three.

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **E.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **F.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, E` (`CSV: 2,3,5`)

Correct answers: B, C, and E (are correct). `Extract tables from PDF`, `Read XML from file` + `Execute XPath expression`, and `Read from CSV file` into a `Datatable`. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **C:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **E:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **F:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q076 (`E6Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

During in-person benefits interviews, an eligibility specialist stays signed into their agency laptop, runs a helper bot to pull three state wage screens, and types an applicant’s verbal explanation when prompted. Which run mode applies?

- **A.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Attended** mode executes inside the caseworker’s active signed-in Windows session and supports interactive human collaboration. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Correct — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.

</details>

### Q077 (`E6Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

An agency maker tries to combine `Microsoft Dataverse` (`Business` DLP group) and `Gmail` (`Non-Business` DLP group) inside a parent RPA cloud flow. What happens when the maker saves the cloud flow?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Platform DLP blocks saving/activating the flow because connectors in `Business` cannot share a flow with `Non-Business` connectors. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Correct — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.

</details>

### Q078 (`E6Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

An agency runs 6 concurrent unattended bots on one on-premises VM (`Windows Server 2022` with `RDSH`) and also wants zero-footprint cloud VMs that scale down to 0 idle VMs overnight when tax season ends. Which cloud capability complements the RDSH server?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Attended run mode executing inside a signed-in user’s active desktop session
- **C.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate **Hosted Machine Groups** (`Hosted RPA`) dynamically provision and scale Azure bot VMs from default or **Azure Compute Gallery** images. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **C:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **D:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q079 (`E6Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

A municipal court producer cloud flow adds docket filings into a Dataverse Work Queue with `Priority = High` for emergency injunctions and `Unique reference = CaseDocketId`. Which capability prevents duplicate docket items while prioritizing injunctions?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Dataverse **Work Queue** item properties (`Priority`, `Unique reference`, `ExpiresOn`) govern priority ordering, deduplication, and SLAs natively. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q080 (`E6Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A municipal permitting agency wants newly submitted online building-permit rows in Microsoft Dataverse to call a cloud zoning GIS API and email fee receipts automatically without provisioning Windows VMs. Which automation type should you recommend?

- **A.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). When all systems expose cloud connectors or REST APIs, an Automated cloud flow executes headlessly with zero desktop VM overhead. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Correct — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.

</details>

### Q081 (`E6Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

How does Vanguard Civic Cloud deploy the exact same `CivicTaxRPA_2_2_0_0_managed.zip` package into `Test` and `Production` while pointing each stage at its own Hosted Machine Group, Key Vault Credential, and portal base URL?

- **A.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import
- **B.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Stage-specific **deployment settings** bind **Connection References**, **Credentials**, and **Environment Variables** during pipeline import. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.
- **B:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q082 (`E6Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Vanguard Civic Cloud stores rotating unattended Windows bot credentials in **Azure Key Vault** (`Microsoft.KeyVault` resource provider registered in Azure + `Key Vault Secrets User` RBAC granted to the `Dataverse` service principal). Which Power Automate artifact links to those Key Vault secrets?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Power Automate **Credentials** backed by Azure Key Vault (or CyberArk) bind unattended connections to centrally rotated secrets. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q083 (`E6Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

After submitting a vendor TIN search on a slow state portal, results render between 1 and 35 seconds later. Proposed solution: Use `Wait for web page content` (`Contain text` / `Contain element`, `Timeout = 45s`) instead of `Wait 45`. Does this minimize bot idle time safely?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes — `Wait for web page content` continues immediately once results render while enforcing a 45-second upper timeout. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.

</details>

### Q084 (`E6Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

Atlas Municipal Procurement scrapes vendor bid rows into `%BidTable%` (`Datatable`) and filters bids where `TotalBid <= 250000` in memory via `Filter data table`. How do you reference column `'VendorName'` of row `0` in PAD?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops
- **D.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `%BidTable[0]['VendorName']%` accesses row `0` (zero-based) and column `'VendorName'` on a PAD `Datatable`. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.
- **D:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.

</details>

### Q085 (`E6Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

An agency cloud flow calls a synchronous document-stamping microservice and must time out after 90 seconds (`Timeout = ____`) so fallback queuing triggers promptly. Which ISO 8601 Timeout value represents 90 seconds?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `PT90S` (or `PT1M30S`) in the cloud action’s ISO 8601 `Timeout` property enforces a 90-second upper bound. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **D:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.

</details>

### Q086 (`E6Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

A public-records division triggers overnight unattended FOIA redaction bots from a scheduled cloud flow onto locked/signed-out agency VMs. Place the four unattended execution stages in order.

- **A.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse
- **B.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text
- **C.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **D.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Target single-session VMs must have zero active human sessions so Power Automate creates a background Windows session, executes the flow, and signs out cleanly. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.
- **B:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.
- **C:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **D:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.

</details>

### Q087 (`E6Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

Vanguard Civic Cloud configures Custom Connector URL patterns in DLP: `Order 1: Allow https://api.civic.gov/*`, `Order 2: Deny *`. Proposed solution: Rely on this ordered DLP rule to prevent any Custom Connector in the environment from calling unapproved external hosts. Does this block unapproved Custom Connector hosts?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes — DLP Custom Connector URL pattern rules enforce approved scheme/host patterns and deny all other hosts via the catch-all `*` rule. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.

</details>

### Q088 (`E6Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Procurement officers working inside a **Model-driven** Vendor Management app press a modern command bar button `Verify Debarment`, updating a Dataverse row or calling a solution flow. Which integration pattern connects Model-driven apps cleanly to Power Automate?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Model-driven modern command bar buttons and Dataverse `When a row is added, modified or deleted` triggers integrate directly with solution cloud flows. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Correct — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q089 (`E6Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

Before pointing a grant-disbursement cloud flow at the live federal payment gateway, QA enables `____` (`Static Result`) on the `HTTP` action to simulate both `200 OK` and `503 Service Unavailable` responses during automated tests. Which cloud feature is this?

- **A.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Cloud action **Static Result** returns mocked status codes, headers, and bodies without sending live external requests. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **B:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

## Case Study Vignette — CivicBridge Revenue Agency

> [Scenario: CivicBridge Revenue Agency processes scanned employer withholding forms using the Document Automation Toolkit, routing low-confidence forms to clerks in the Canvas Validation Station app and verified forms to unattended desktop bots that post entries via `Invoke web service` (`Encode request body = Off` for raw JSON) into an intranet ledger.]

### Q090 (`E6Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — CivicBridge Revenue Agency: For rare legacy municipal mainframe screens (`IBM 3270`) that supplement CivicBridge’s intranet ledger, which PAD action group interacts with terminal fields natively without pixel coordinates?

- **A.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **B.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Power Automate for desktop’s **Terminal emulation** actions (`Open terminal session`, `Get/Set text on terminal session`). [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **B:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q091 (`E6Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — CivicBridge Revenue Agency: How should CivicBridge package its Document Automation intake flows, Validation Station customizations, unattended ledger desktop flows, Connection References, and Environment Variables for governed promotion?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **D.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Package all cloud flows, desktop flows, apps, Connection References, and Environment Variables inside a **Dataverse Solution** with a custom publisher. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **D:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.

</details>

### Q092 (`E6Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — CivicBridge Revenue Agency: Verified withholding forms are placed into a Dataverse Work Queue so multiple unattended ledger bots process them concurrently. Which PAD action leases the next `Queued` form atomically and updates its completion status?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Process work queue items` paired with `Update work queue item` (`Processed` / `On hold` / `Generic exception`). [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q093 (`E6Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

An intake webhook passes `"applicantAddress": null` for PO-box filers, and a cloud flow safely substitutes `'PO_BOX_ONLY'` via `coalesce(triggerBody()?['applicantAddress'], 'PO_BOX_ONLY')`. Which WDL expression family prevents null property crashes?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Null-conditional `?` operators paired with `coalesce()` and `json()` handle optional or stringified JSON fields safely in cloud flows. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.

</details>

### Q094 (`E6Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

An agency cloud flow queries an on-premises IBM DB2 / SQL Server mainframe staging database inside a county datacenter where inbound firewall ports are closed. Which component bridges the cloud flow securely?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **C.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **D.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A clustered **On-Premises Data Gateway** relays cloud flow SQL/DB2 queries over outbound TLS (`443`). [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **C:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **D:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.

</details>

### Q095 (`E6Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

An agency security architect configures headless ALM imports and parent cloud flows under a Microsoft Entra **Service Principal**, while unattended bots sign into agency-joined Windows 11 VMs. Which credential model is required for the VM login?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A dedicated interactive **AD / Microsoft Entra user service account** stored in Key Vault/CyberArk Credentials is required for Windows OS session login (Service Principals cannot log into interactive Windows desktops). [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.

</details>

### Q096 (`E6Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

Unattended revenue bots lease filings via `Process work queue items`. Which two actions update completed items versus temporarily deferred items when a downstream state ledger enters a 15-minute maintenance window? Select two.

- **A.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`
- **D.** Interactive manual execution from the Power Automate for desktop console or Designer
- **E.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Use `Update work queue item` (`Processed` or `On hold` for business exceptions) and `Requeue item with delay` (`15 minutes`) for temporary downstream maintenance windows. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.
- **D:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **E:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q097 (`E6Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

A municipal licensing desktop bot automates a Win32 cashier window whose title includes `%CounterNumber%` and whose `Post Payment` button uses two slightly different control paths across legacy and patched PCs. Which two PAD selector features handle both? Select two.

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **E.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Dynamic `%CounterNumber%` variables parameterize window titles while multiple fallback selectors on one UI element match both legacy and patched control trees. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **E:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.

</details>

### Q098 (`E6Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

A civic-cloud engineering team is authoring, code-signing, uploading, and solution-packaging a `.NET Framework` FIPS-140 hash custom action for Power Automate for desktop. Place the four steps in exact order.

- **A.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD
- **B.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically
- **C.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop
- **D.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Build the `ActionBase` class with Custom Actions SDK, package & sign the `.cab` with a trusted certificate, upload under Custom actions in Portal, and package inside a Solution. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.
- **B:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.
- **C:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).
- **D:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.

</details>

### Q099 (`E6Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

An agency RPA developer is fixing a fragile procurement web selector that broke when dynamic session tokens appeared in `<div id="bid_sess_09f2a">`. Choose the resilient four-step Selector Builder sequence.

- **A.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs
- **B.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field
- **C.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **D.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Capture the UI element, uncheck volatile session `id` attributes in Selector Builder, apply `%Variable%` / `Contains` / `Regex` on stable attributes, and add a fallback selector. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.
- **B:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.
- **C:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **D:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).

</details>

### Q100 (`E6Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow `HTTP POST` issues an irrevocable treasury check print command to a non-idempotent legacy print server. Why should you set `Retry Policy` to `None` on that specific HTTP action?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **D.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Setting `Retry Policy = None` prevents automatic network-timeout retries from double-printing duplicate checks on non-idempotent endpoints. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **D:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.

</details>
