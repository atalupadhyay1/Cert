# Microsoft Exam PL-500 — Companion Case Study Scenarios (24 Vignettes)

Attach this document as a downloadable resource when uploading `practice-set-{1..6}.csv` (Option A), or upload `case-embedded-set-{1..6}.csv` (Option B) so every case-linked question embeds its full scenario brief inline inside the Udemy question prompt.

> All 24 organizations and scenarios below are 100% original fictional RPA Developer case studies authored for independent exam preparation. None reproduce Microsoft’s copyrighted exam case studies.

## Practice Exam 1 — Banking, Mainframe 3270 & Mortgage Servicing RPA — Mainframe terminal emulation, Key Vault credentials, Document Automation Toolkit, dynamic selectors, and run queue priority

### SummitVault ATM Logistics (Q017, Q018, Q019)

[Scenario: SummitVault ATM Logistics promotes RPA solutions from Dev through UAT to Production via Power Platform pipelines. Production enforces strict Desktop Flow DLP blocking PowerShell while allowing Excel and Web automation, and urgent cash-out dispatch bots must jump ahead of routine audit runs in the Machine Group Run Queue.]

### Crestline Mortgage Servicing (Q042, Q043, Q044)

[Scenario: Crestline Mortgage Servicing receives 3,500 scanned PDF escrow tax bills per day in an Exchange shared mailbox. Invoices require AI Builder extraction with human review for <85% confidence scores via Document Automation Toolkit, followed by unattended browser entry where dynamic CSS IDs change on every portal reload.]

### MeridianFirst Retail Bank (Q067, Q068, Q069)

[Scenario: MeridianFirst Retail Bank processes 14,000 nightly wire reconciliations against an IBM 3270 mainframe and an internal Win32 treasury app. Unattended bots must run without human sign-in across a 6-VM Machine Group, pull rotating Windows & mainframe secrets from Azure Key Vault, and distribute items safely via Dataverse Work Queues.]

### HarborTrust Custody Ops (Q090, Q091, Q092)

[Scenario: HarborTrust Custody Ops orchestrates hybrid cloud-and-desktop settlement flows inside a Managed Dataverse Solution. Sensitive SWIFT bearer tokens must never appear in Cloud Run History or Desktop variable logs, and an internal REST trade engine requires a Custom Connector rewriting headers and executing C# payload signing under 5 seconds.]

## Practice Exam 2 — Healthcare Citrix VDI, HL7 Labs & Hosted RPA — Citrix Virtual Desktop Agent, XML/XPath cloud flows, Windows Server RDSH concurrency, webpage JavaScript, and Hosted Machine Groups

### Clearview Regional Health (Q017, Q018, Q019)

[Scenario: Clearview Regional Health automates inpatient claim scrubbing inside a legacy WinForms billing client published over Citrix Virtual Apps. Because Citrix streams pixels by default, selectors failed until the team evaluated the Power Automate agent for virtual desktops vs OCR fallback, paired with `On block error` system-exception recovery.]

### SilverOak Specialty Pharmacy (Q042, Q043, Q044)

[Scenario: SilverOak Specialty Pharmacy validates prior-authorization portals using Power Automate for desktop. A portal calculates dynamic copay tables client-side inside shadow/DOM elements requiring `Run JavaScript function on web page`, stores parsed JSON tiers in a Desktop Custom Object, and marks patient DEA numbers as Sensitive variables.]

### BioPulse Reference Labs (Q067, Q068, Q069)

[Scenario: BioPulse Reference Labs ingests XML HL7 lab requisitions in a parent cloud flow, extracts specimen codes via `xpath(xml(...))`, enqueues items into a Dataverse Work Queue, and runs 8 concurrent unattended desktop sessions on a Windows Server 2022 RDSH host calling a local analyzer’s unauthenticated localhost HTTP port.]

### Beacon Care Network (Q090, Q091, Q092)

[Scenario: Beacon Care Network scales seasonal open-enrollment RPA spikes without maintaining physical servers by provisioning Power Automate Hosted Machine Groups from a custom Azure Compute Gallery VM image, enforcing custom connector host DLP rules, and separating headless Entra Service Principals from interactive Windows bot accounts.]

## Practice Exam 3 — Customs Brokerage, Freight Gateways & Custom Actions — On-Premises Data Gateway, Business vs System exceptions, ms-powerautomate URLs, signed .NET CAB custom actions, and VM session hygiene

### PacificHarbor Terminal (Q017, Q018, Q019)

[Scenario: PacificHarbor Terminal experienced intermittent `Cannot sign in to unlocked/active session` unattended RPA failures whenever support engineers closed RDP windows with `[X]` instead of signing out on target VMs. Admins are standardizing VM preparation, Machine Group sharing (`User` vs `Co-owner`), and Managed Solution upgrades.]

### IronRail Intermodal (Q042, Q043, Q044)

[Scenario: IronRail Intermodal runs attended yard-clerk desktop flows launched instantaneously from a Canvas tablet app and desktop `ms-powerautomate:` URLs, alongside unattended yard-gate SAP GUI bots packaged with a signed `.NET Framework` Custom Action CAB module (`Desktop Flow Module`) that calculates railcar check-digits offline.]

### AeroLink Cold Chain (Q067, Q068, Q069)

[Scenario: AeroLink Cold Chain polls cold-storage sensor APIs from a cloud flow using `@and(...)` Trigger Conditions, ISO 8601 `PT10M` timeouts, and exponential retry policies, then calls reusable solution Child Cloud Flows and subflow-modularized desktop flows that log temperature excursions into Excel and CSV manifests.]

### Portside Customs Brokerage (Q090, Q091, Q092)

[Scenario: Portside Customs Brokerage extracts multi-page ocean bills of lading using AI Builder and PDF table extraction, validates HS tariff codes against an on-premises SQL Server via an On-Premises Data Gateway in cloud flows, and flags mismatched container weights as Business Exceptions (`On hold`) without triggering 3x UI system retries.]

## Practice Exam 4 — Automotive AS/400 5250, COM Scripting & Custom Connectors — IBM 5250 terminal sessions, Datatables, VBScript/PowerShell COM automation, Custom Connector C# ScriptBase, and Portal Monitor telemetry

### Kestrel Precision Castings (Q017, Q018, Q019)

[Scenario: Kestrel Precision Castings built a Custom Connector wrapping an internal MES REST API with OAuth 2.0 authentication, a `Set HTTP header` policy template injecting plant routing codes, and a C# `ScriptBase` transform converting nested XML responses to JSON for downstream cloud and desktop flows.]

### VoltEdge Battery Systems (Q042, Q043, Q044)

[Scenario: VoltEdge Battery Systems runs high-frequency cell-grading cloud and desktop automations. Cloud flows enable `Trigger Concurrency Control = 20` and `Secure Outputs` on battery telemetry keys, while desktop flows invoke `Run VBScript` and `Run PowerShell script` actions to query local COM serial testers and capture `%ScriptError%`.]

### ForgeLine Stamping Corp (Q067, Q068, Q069)

[Scenario: ForgeLine Stamping Corp automates legacy green-screen AS/400 (`IBM 5250`) shop-floor schedules alongside modern web supplier portals. Bots connect via native Terminal Emulation actions, parse fixed-width & CSV production schedules into Desktop Datatables (`%ScheduleTable[row][col]%`), and filter defective lot rows without Excel installed.]

### Titan Drivetrain Assembly (Q090, Q091, Q092)

[Scenario: Titan Drivetrain Assembly governs 45 production bots across three plants in Power Automate Portal (`Monitor -> Desktop flow runs` & `Machines`). Plant leads inspect step-level failure screenshots, reprioritize `Line-Down` runs to `High` + `Move to top` in the run queue, and audit Desktop Flow DLP policies before importing new solutions.]

## Practice Exam 5 — Smart-Grid Work Queues, OCR Selectors & RPA Debugging — Dataverse Work Queues with SLAs/requeue, Tesseract OCR + regex fallback selectors, PAD Breakpoints/Static Result, and CyberArk/Solution Layers

### ClearCurrent Water & Gas (Q017, Q018, Q019)

[Scenario: ClearCurrent Water & Gas debugs complex multi-subflow desktop automations in Power Automate for desktop Designer using Breakpoints, `Run from here`, `Run delay` throttling, and Dataverse `Environment Variables` + JSON config files, while unit-testing parent cloud flows offline using mocked `Static Result` HTTP 429/500 responses.]

### SunGrid Retail Energy (Q042, Q043, Q044)

[Scenario: SunGrid Retail Energy processes 25,000 commercial meter switches per week using producer cloud flows that bulk-load Dataverse Work Queues with `ExpiresOn` SLAs and consumer desktop flows running `Process work queue items` across a 10-machine group, requeueing transient portal lockouts with a 30-minute delay.]

### Horizon Grid Compliance (Q067, Q068, Q069)

[Scenario: Horizon Grid Compliance enforces enterprise CyberArk / Azure Key Vault credential stores for unattended bots, assigns least-privilege `Desktop Flows Machine User` vs `Desktop Flows Machine Owner` security roles, and strips accidental Unmanaged Active layers in UAT before applying Managed Solution Upgrades.]

### PeakPower Tariff Co (Q090, Q091, Q092)

[Scenario: PeakPower Tariff Co automates legacy Delphi tariff calculators on Windows 11 Enterprise VMs. When Win32 controls lack accessible UI Automation trees, RPA developers combine `Extract text with OCR` (Tesseract language packs & scale multipliers) with fallback UI selectors using Regex/Contains operators and explicit `Wait for window content` gates.]

## Practice Exam 6 — Public-Sector Document Automation, DLP & Enterprise ALM — Raw JSON Invoke web service, multi-page CSS table scraping, solution Child Flows, Desktop Flow module DLP, and Managed pipeline upgrades

### Atlas Municipal Procurement (Q017, Q018, Q019)

[Scenario: Atlas Municipal Procurement scrapes paginated vendor bid tables across multi-frame government portals using Power Automate for desktop `Extract data from web page` CSS selectors, deduplicates vendor lists, merges Excel bid workbooks (`Get first free column/row`), and wraps fragile portal screens inside `On block error` -> `Run subflow` recovery blocks.]

### Vanguard Civic Cloud (Q042, Q043, Q044)

[Scenario: Vanguard Civic Cloud operates zero-footprint Azure Hosted Machine Groups alongside on-premises registered machines via Power Automate machine runtime. Security architects enforce environment DLP policies blocking `Run DOS command` and unapproved custom connector hosts while automating Dev -> Test -> Prod deployments with Connection References and Environment Variables.]

### Solstice Research Grants (Q067, Q068, Q069)

[Scenario: Solstice Research Grants orchestrates grant-disbursement parent cloud flows calling modular solution Child Flows, parsing XML/JSON federal award feeds, guarding secrets with `Secure Inputs`/`Secure Outputs`, and invoking attended desktop helper flows on grant officers’ laptops with `Run-only users` permissions.]

### CivicBridge Revenue Agency (Q090, Q091, Q092)

[Scenario: CivicBridge Revenue Agency processes scanned employer withholding forms using the Document Automation Toolkit, routing low-confidence forms to clerks in the Canvas Validation Station app and verified forms to unattended desktop bots that post entries via `Invoke web service` (`Encode request body = Off` for raw JSON) into an intranet ledger.]
