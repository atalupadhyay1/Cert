# Microsoft Exam PL-200: Full-Length Mock Exam 6 — Reviewer Study Key

**Theme:** Higher Education & Global Grants — Custom Activity Tables, Entra Group Teams, Page Access Rules & Word XML Templates  
**Credential:** Microsoft Certified: Power Platform Functional Consultant Associate  
**Study guide baseline:** December 26, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)  
**Lifecycle notice:** Exam PL-200 retired on August 31, 2026 and was replaced by Exam AB-410 (Microsoft Certified: Intelligent Applications Builder Associate).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`T6-Q007`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

When an `Alumni Donor Household` (`Account`) transfers to a new `Major Gifts Officer`, only open (`Active`) child `Pledge Opportunity` rows must transfer to the new officer while fulfilled historical pledges retain their original officer, and deleting a Household with pledges must be blocked. Complete the relationship setting: ____.

- **A.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **B.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **C.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **D.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure `Custom` relationship behavior with `Assign = Cascade Active` and `Delete = Restrict`. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **B:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **C:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **D:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.

</details>

### Q002 (`T6-Q010`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

University registrar Dataflows sync `Student Contact` rows hourly using the natural `BannerStudentID` text column instead of Dataverse GUIDs and must prevent duplicate `BannerStudentID` values in SQL. What should you configure?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create an `Alternate Key` on `BannerStudentID` and verify its index status reaches `Active`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **C:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Correct — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.

</details>

### Q003 (`T6-Q022`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Across global regional offices, Country Directors supervise Program Managers who supervise Field Officers across multiple Business Units based on organizational job `Positions` rather than the HR `Manager` column. Which security feature grants hierarchical visibility across Business Units?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure `Position` `Hierarchy Security` mapping job positions in a custom tree across Business Units. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.

</details>

### Q004 (`T6-Q003`) — Configure Microsoft Dataverse [1.1] · *Multi-Select (Select 2)*

You are reviewing Dataverse table properties for Westbrook University’s `Campus Interview` and `Scholarship Application` tables. Which TWO statements are true? Select two.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Enabling `Enable attachments (notes and files)`, `Leverage Quick-Create form`, `Can be added to a queue`, and `Track changes` activates Timeline notes, Quick Create, Queues, and delta sync
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Custom `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support under shared `Activity` privileges, while standard tables enable `Attachments`, `Quick-Create`, `Queues`, and `Track changes` via table properties. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Functional Consultants toggle table-level flags carefully—several flags (such as queues or notes/attachments) cannot be disabled once saved.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q005 (`T6-Q005`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

An advancement analyst linked `Alumnus Contact` and `Affinity Club` via a native `N:N` relationship and now asks to add `ChapterOfficerTitle` and `DuesPaidThroughDate` directly onto the native `N:N` intersect entity. Why is that impossible?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **C.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Hidden system intersect tables behind native `N:N` relationships do not support custom columns, custom forms, or workflows—a manual intersect table with two `1:N` lookups is required. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Correct — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **C:** Incorrect — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **D:** Incorrect — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.

</details>

### Q006 (`T6-Q085`) — Manage environments [4.1] · *Multi-Select (Select 2)*

An international fellowship board enables `Managed Environments` across `Test` and `Production` to automate deployments and quality gates. Which TWO capabilities are provided by `Managed Environments` + `Solution Checker`? Select two.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Built-in `Power Platform pipelines` promote Managed packages with delegated approvals, and `Managed Environments` can enforce `Solution Checker` (`Warn` or `Block`) on import alongside Canvas sharing limits. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q007 (`T6-Q071`) — Create and manage logic and process automation [3.6] · *Multi-Select (Select 2)*

You are reviewing operational support procedures for Westbrook’s Power Automate flows. Which TWO practices are accurate? Select two.

- **A.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely
- **B.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Inspect payloads and re-run transient outages from `28-day Run History` (`Resubmit`) alongside `Flow Checker` / `Static Result`, and share button/Canvas flows via `Run-only users`. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.
- **B:** Correct — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q008 (`T6-Q082`) — Create and manage logic and process automation [3.12] · *Single-Answer Multiple Choice*

An admissions maker tries to build a Dataverse `Business Rule` that checks a `Campus Housing Preferences` (`Choices` Multi-Select) column and hides the entire `Meal Plan Tab` on the Main form. Why is a Business Rule unable to do this?

- **A.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors
- **D.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Business Rules do not support `Choices (Multi-Select)` columns and cannot show or hide whole form Tabs or Sections. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Incorrect — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.
- **B:** Correct — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.
- **D:** Incorrect — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.

</details>

### Q009 (`T6-Q037`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

Advancement officers want a guided `Gift Split & Matching Employer Lookup` wizard opened as a right-side pane inside their model-driven app using responsive Canvas containers and Power Fx. Which page artifact should you add to the model-driven app?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Build a solution-aware `Custom Page` with `Horizontal`/`Vertical` auto-layout containers and invoke it as a side pane or modal dialog via `Navigate()`. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Correct — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q010 (`T6-Q004`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

Each `Research Grant` can be co-funded by multiple `Donor Foundations` (`Account`), and each funding link must store `CommittedGrantShareUSD`, `ReportingCadence`, and `GrantAgreementSignedDate` on its own form and views. How should you model this in Dataverse?

- **A.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **B.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create a manual intersect table (`Grant Co-Funder Allocation`) with two `1:N` relationships to `Research Grant` and `Account`. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **B:** Correct — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Incorrect — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.

</details>

### Q011 (`T6-Q044`) — Create apps by using Microsoft Power Apps [2.7] · *Multi-Select (Select 2)*

You are reviewing Horizon’s `Alumni Gala Check-In` Canvas app against `280,000` `Alumni Contact` rows in Dataverse. Which TWO practices prevent UI distortion and silent 500-row search truncation? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **E.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Use responsive `Horizontal`/`Vertical` containers (`Scale to fit = Off`), and query Dataverse with delegable predicates (`Filter`, `LookUp`, `StartsWith`, `=`) plus `IfError()` error handling. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **E:** Correct — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).

</details>

### Q012 (`T6-Q081`) — Create and manage logic and process automation [3.11] · *Single-Answer Multiple Choice*

University procurement runs a server-side `Dataverse Accelerator` `Pre-operation` plug-in on `DepartmentRequisition` so campus lab orders roll back immediately whenever a vendor’s `CreditHold` boolean is true with a non-zero `OrderTotal`. Fill in the Power Fx expression: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))` aborts the Dataverse save transactionally. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Correct — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.

</details>

### Q013 (`T6-Q098`) — Manage environments [4.6] · *Single-Answer Multiple Choice*

Admissions counselors want `Admissions@westbrook.example` emails placed into a Dataverse Queue where ONLY the 8 members of the `International Admissions` unit can view Queue Items and `Pick`/`Release` items. How should you configure the Queue?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **C.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **D.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create the Dataverse Queue with `Type = Private` and add only the 8 `International Admissions` users (or their team) as Queue members. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **C:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **D:** Correct — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.

</details>

### Q014 (`T6-Q051`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

After configuring a `Page Access Control Rule` or `Table Permission` inside the `Power Pages Management` model-driven app, what must you select inside Power Pages Design Studio so the studio cache picks up the security metadata?

- **A.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **B.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **C.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Select `Sync` in the upper-right corner of Power Pages Design Studio before previewing the website. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Correct — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **B:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **C:** Incorrect — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q015 (`T6-Q078`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

Westbrook runs 22 classic background workflows that send routine applicant status updates, and `System Jobs` (`ProcessSession`) has ballooned to 14 million `Succeeded` rows consuming Dataverse storage. What workflow property prevents this buildup while keeping failed logs?

- **A.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **B.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable `Automatically delete completed workflow jobs (to save disk space)` on each background workflow definition. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **B:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q016 (`T6-Q086`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

When creating the `WestbrookAdmissions` solution, you configure a custom `Westbrook Publisher` (`wbu_` prefix) and add the standard `Contact` table to customize ONLY two columns and one Main form. Which option avoids unnecessary cross-solution dependencies?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **C.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Use a `Segmented Solution`—adding ONLY the two modified columns and one Main form while leaving `Include all objects` and `Include table metadata` unchecked. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **C:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

## Case Study Vignette — Westbrook University Admissions

> [Scenario: Westbrook University Admissions tracks applicants, campus visits, emails, and phone calls in Dataverse. Admissions counselors want a custom `Campus Interview` table that appears inside the unified `Timeline` control alongside Emails and Tasks with `Regarding` lookup support, plus Microsoft Entra Security Group Teams that grant Security Roles dynamically from Entra group membership.]

### Q017 (`T6-Q001`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

Case study — Westbrook University Admissions: Admissions counselors want a custom `Campus Interview` table that appears chronologically inside the unified `Timeline` wall on `Applicant Contact` and `Admission Application` alongside Emails and Phone Calls, supporting the polymorphic `Regarding` lookup. How must you create `Campus Interview`?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create `Campus Interview` as a custom `Activity` table at creation time—note that all custom Activity tables share the unified `Activity` row in Security Roles. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q018 (`T6-Q023`) — Configure Microsoft Dataverse [1.10] · *Single-Answer Multiple Choice*

Case study — Westbrook University Admissions: Westbrook assigns a custom `Admissions Counselor` Security Role exclusively to a `Microsoft Entra ID Security Group Team` (never directly to individual users), and counselors need `User`-depth ownership privileges on `Admission Application` rows they create themselves. Which setting on the custom Security Role enables this?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **D.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Set `Member’s privilege inheritance` on the Security Role to `Direct User (Basic) access level and Team privileges` (copied from `Basic User` with proper `Append`/`Append To` privileges). [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **D:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.

</details>

### Q019 (`T6-Q025`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

Case study — Westbrook University Admissions: Westbrook’s Central IT manages 350 admissions staff in Microsoft Entra security groups (`SG-Admissions-Undergrad`, `SG-Admissions-Grad`) and wants zero manual user-role assignments in Dataverse when staff join or leave groups. Which Dataverse team type meets this requirement?

- **A.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create `Microsoft Entra ID Security Group Teams` linked to each Entra group’s Object ID and assign custom Dataverse Security Roles to those teams. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **B:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.

</details>

### Q020 (`T6-Q006`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

A global NGO wants Dataverse to block deleting any `Country Program` parent row while active or historical `Field Grant Disbursement` child rows still reference that program. Which `1:N` relationship behavior enforces this?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors
- **D.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure `Referential, Restrict Delete` on the `Country Program` -> `Field Grant Disbursement` relationship. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).
- **D:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.

</details>

### Q021 (`T6-Q002`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

Westbrook also needs a static `Academic Term Calendar` table (`Fall 2026`, `Spring 2027`) readable across the entire university with zero User, Team, or Business Unit row ownership, plus a `Scholarship Application` table owned by regional admissions teams. How should `Ownership` be set at creation?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Set `Academic Term Calendar` to `Organization` ownership and `Scholarship Application` to `User or team` ownership at creation time, as neither can be changed afterward. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q022 (`T6-Q029`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

In your `Advancement & Grants` model-driven app, `Major Gifts Officers` use `Planned Giving Main Form`, `Grant Officers` use `Institutional Grant Main Form`, and general staff fall back to `General Donor Form`. Which configuration prevents lockouts if a user’s role changes?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Assign Security Roles to the specialized Main forms, rank them via `Form Order`, and ensure `General Donor Form` remains enabled for `Fallback`. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q023 (`T6-Q059`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

Your `GlobalAidGrants` solution contains 11 cloud flows calling Dataverse, SharePoint, and Office 365 Outlook, plus 3 reusable `Child Flows`. How should credentials be wired so UAT and Production pipelines never turn flows off or require maker passwords?

- **A.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **D.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Bind every connector action across parent and child flows to shared solution-aware `Connection References` mapped to target service-account connections during deployment. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **D:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.

</details>

### Q024 (`T6-Q039`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

Before dispatching an after-hours locksmith from the `WorkOrders` modern command bar, facilities coordinators must confirm `"Dispatch this technician now?"` in a native confirmation dialog. Complete the Power Fx formula: ____.

- **A.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **B.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **C.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **D.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))` prompts via `Confirm(...)` before patching. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **B:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **C:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **D:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.

</details>

### Q025 (`T6-Q014`) — Configure Microsoft Dataverse [1.6] · *Single-Answer Multiple Choice*

International grant-donor auditors require full before-and-after field history whenever `ApprovedGrantBudget` changes on `Grant Award`, yet turning on table and column auditing alone logged zero events. Which environment-level switch must an admin enable in PPAC?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable `Start Auditing` in Power Platform Admin Center environment Auditing settings—all three levels (Environment, Table, and Column) must be enabled concurrently. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.

</details>

### Q026 (`T6-Q095`) — Manage environments [4.5] · *Single-Answer Multiple Choice*

Which two `Environment Variable` data types should you select inside `GlobalAidGrants` to externalize (1) a SharePoint Online site/document library used by a Canvas app and (2) an encrypted banking webhook token stored in Azure Key Vault?

- **A.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Use `Data Source` (SharePoint connector) for the site/library and `Secret` (Azure Key Vault) for the encrypted webhook token. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q027 (`T6-Q026`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

For each confidential `Honorary Doctorate Nomination`, the Provost’s office hand-selects 5 faculty reviewers who need Read/Write access to that single nomination row without owning rows or modifying Entra groups. Which team model fits best?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable `Access Teams` on `Nomination`, create an `Access Team Template`, and add an Access Team subgrid to the Main form. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q028 (`T6-Q053`) — Create apps by using Microsoft Power Apps [2.11] · *Multi-Select (Select 3)*

You are finalizing the architecture of `GlobalAid Grant Portal` on Microsoft Power Pages. Which THREE design choices align with official Microsoft Learn guidance? Select three.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **E.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **F.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, E` (`CSV: 2,4,5`)

Correct answers: B, D, and E (are correct). Use `Page Access Control Rules` + `Table Permissions` + `Web Roles` + `Microsoft Entra External ID`, `Lists` and `Basic Forms` in Design Studio, and `Multi-Step Forms` + SharePoint document grids / Power BI RLS. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **E:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **F:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q029 (`T6-Q063`) — Create and manage logic and process automation [3.3] · *Multi-Select (Select 2)*

You are reviewing error handling and concurrency across 25 university cloud flows. Which TWO design rules prevent silent failures and race bugs? Select two.

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **D.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Structure `Try / Catch` blocks using `Scope` + `Configure run after` + `Terminate`, and use immutable `Compose` steps rather than `Set variable` inside concurrent `Apply to each` loops. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Correct — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **D:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q030 (`T6-Q073`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

University leadership wants a chart showing average days `Admission Application` rows spend in the `Faculty Committee Review` BPF stage. Where is that stage-tracking data stored in Dataverse?

- **A.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **B.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **C.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Every Business Process Flow creates its own dedicated Dataverse table tracking `Active Stage`, `Active Stage Started On`, and `Status`. [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **B:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **C:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q031 (`T6-Q041`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

You embed a `Seating Chart Picker` Canvas app directly onto a section of the `Alumni Gala Event` Main form. Complete the Power Fx reference inside the embedded Canvas app that reads the open `Alumni Gala Event` record: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `ModelDrivenFormIntegration.Item`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `ModelDrivenFormIntegration.Item` exposes the host Main form record to the embedded Canvas app. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Correct — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.

</details>

### Q032 (`T6-Q100`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

GlobalAid’s data-protection officer notes that whistleblower grant-fraud evidence PDFs uploaded on a restricted `Fraud Investigation` row MUST NOT be readable by general SharePoint site members who lack Dataverse `Fraud Investigation` Read privileges. Which critical `SharePoint Document Management` behavior must you explain?

- **A.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Out-of-the-box Dataverse SharePoint Document Management does NOT copy or enforce Dataverse row-level Security Roles on SharePoint folders—store sensitive attachments in Dataverse `File` columns / Timeline `Notes` (or implement explicit SharePoint ACL isolation). [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **B:** Incorrect — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **D:** Correct — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q033 (`T6-Q061`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

In a `Disburse Humanitarian Wire` cloud flow, if an action inside `Scope - Send SWIFT Message` fails or times out, `Scope - Notify Grants Treasury` must log an urgent Dataverse task and mark the flow run `Failed`. Which settings are required?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure `Configure run after` on `Scope - Notify Grants Treasury` to `has failed`, `is skipped`, and `has timed out`, create the task, and finish with `Terminate (Failed)`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.

</details>

### Q034 (`T6-Q017`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

Every night, a global scholarship foundation pulls JSON exchange-rate tables and CSV partner rosters, normalizes currency codes via `Power Query`, and upserts Dataverse `Currency Rate` and `Partner School` tables on a schedule. Which tool should you configure?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries
- **C.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure a scheduled `Power Platform Dataflow` (`Power Query`) mapping transformed outputs into Dataverse. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.
- **C:** Incorrect — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **D:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q035 (`T6-Q080`) — Create and manage logic and process automation [3.11] · *Ordered Sequence (Multiple Choice)*

GlobalAid’s functional team wants to author a server-side `Instant` Power Fx calculation (`ConvertGrantCurrency`) and an `Automated` `Pre-operation` budget-cap validator without Visual Studio C# code. Put the steps in exact order.

- **A.** Write client-only Navigate() and Notify() UI calls inside an Automated Pre-operation plug-in → Skip Solution selection → Bind to an Excel file on OneDrive → Run offline
- **B.** Open the Dataverse Accelerator app → Select Instant (typed parameters) or Automated (table Create/Update/Delete Pre/Post-op) plug-in → Write the Power Fx formula & pick a Solution → Save and test in the Accelerator canvas or app/flow
- **C.** Open Visual Studio 2022 & compile a C# .NET assembly → Register via Plug-in Registration Tool in Production Default Solution → Disable Power Fx → Reboot Dataverse
- **D.** Turn off Dataverse database in PPAC → Create a classic 2010 workflow first → Convert the workflow into HTML → Upload as a Power Pages web file

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Open the `Dataverse Accelerator` app, select `Instant` or `Automated` (`Pre-operation`/`Post-operation`) plug-in, write the Power Fx expression and pick your Solution, then save and test. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — Server-side Dataverse low-code plug-ins execute in the Dataverse event pipeline and cannot invoke client screen functions like Navigate().
- **B:** Correct — Dataverse low-code plug-ins are authored in the Dataverse Accelerator app using Power Fx, saved into a Solution as Instant or Automated server-side plug-ins, and tested inline.
- **C:** Incorrect — Low-code plug-ins use Power Fx inside the Dataverse Accelerator app rather than pro-code C# DLL compilation.
- **D:** Incorrect — Low-code plug-ins require a Dataverse database and are stored as Custom APIs / plug-in steps, not Power Pages HTML files.

</details>

### Q036 (`T6-Q068`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

A grant-audit flow uses Dataverse `List rows` on `Claim` / `Disbursement` rows and needs `orc_policynumber` and `orc_deductible` from the parent `orc_PrimaryPolicyId` Lookup in the same single API request. Complete `Expand Query`: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **C.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)` expands parent Lookup fields inline. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **C:** Correct — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q037 (`T6-Q075`) — Create and manage logic and process automation [3.8] · *Single-Answer Multiple Choice*

When you edit an active Business Process Flow to add a new stage step, how do classic workflows attached to `Stage Entry` / `Stage Exit` and the underlying BPF Dataverse table support governance?

- **A.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **B.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Classic workflows fire automatically on `Stage Entry` or `Stage Exit` transitions, and the BPF Dataverse table retains stage-instance rows for views, security roles, and audit reporting. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **B:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q038 (`T6-Q096`) — Manage environments [4.5] · *Multi-Select (Select 2)*

During a Production Managed import, you want zero hardcoded Dev URLs and zero flows turning off due to credential rebinding. Which TWO solution artifacts achieve this? Select two.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). `Environment Variables` (with Dev `Current Value` removed before export) and `Connection References` bound to Production service-account connections. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.

</details>

### Q039 (`T6-Q020`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Campus Wi-Fi check-in kiosks create 300,000 `Event Beacon Log` rows per semester in Dataverse, and logs older than 90 days must be purged automatically every month without writing code or looping in Power Automate. What should you configure?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Schedule a monthly recurring `Bulk Record Deletion` system job filtering `Event Beacon Log` rows older than 90 days. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **C:** Correct — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.

</details>

### Q040 (`T6-Q097`) — Manage environments [4.6] · *Ordered Sequence (Multiple Choice)*

GlobalAid’s donor-support desk wants incoming NGO messages addressed to `GrantsHelp@globalaid.example` converted into tracked Dataverse Queue Items without legacy Email Router software or client Outlook plugins. Sequence the Server-Side Synchronization deployment steps.

- **A.** Create a Personal View on the Contact table → Upload a Word Template → Run Bulk Record Deletion on ActivityPointer → Share the Queue via Anonymous Web Role
- **B.** Install deprecated Dynamics 365 Email Router on a Windows 7 PC → Skip Approve Email and Test & Enable Mailbox → Expect unapproved mailboxes to sync automatically → Disable Queues
- **C.** Open Outlook in a browser on a developer laptop → Record mouse coordinates with Power Automate for desktop → Copy email text into Notepad → Import CSV nightly
- **D.** Verify Exchange Online Email Server Profile & Server-Side Sync defaults in PPAC → Create a Dataverse Queue with the shared email → Open the Queue Mailbox & select Approve Email → Run Test & Enable Mailbox until status = Success

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Verify the Exchange Online `Email Server Profile` and Server-Side Sync defaults in PPAC, create the Dataverse `Queue` with its email address, `Approve Email` on the Queue Mailbox, and run `Test & Enable Mailbox` until status = `Success`. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — Views, Word Templates, and Bulk Deletion do not configure Exchange Server-Side Synchronization or Queue mailboxes.
- **B:** Incorrect — The legacy Email Router is deprecated; Server-Side Synchronization requires mailbox approval (when configured) and Test & Enable Mailbox succeeding.
- **C:** Incorrect — Dataverse includes native Exchange Server-Side Synchronization and Dynamics 365 App for Outlook without brittle UI screen-scraping.
- **D:** Correct — Routing shared-inbox emails into a Dataverse Queue via Server-Side Sync requires an Email Server Profile, a Queue with email address, Email Approval, and Test & Enable Mailbox.

</details>

### Q041 (`T6-Q036`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

When university housing staff open a side-pane `Custom Page` from the `WorkOrders` grid via `Navigate()`, the host screen passes the selected row’s string identifier inside `recordId`. Write the Power Fx formula that retrieves the matching `WorkOrders` row: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))` converts `Param("recordId")` via `GUID(...)` to fetch the target record. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Correct — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

## Case Study Vignette — Atlas Field Scholarships

> [Scenario: Atlas Field Scholarships coordinates regional reviewers across five continents. Before UAT cutover, Functional Consultants export a static vs dynamic Excel PivotTable of `Scholarship Applications` for finance, verify canvas screen-reader `AccessibleLabel` and delegation warnings in App Checker, and promote Managed upgrades via Power Platform pipelines.]

### Q042 (`T6-Q016`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

Case study — Atlas Field Scholarships: Atlas’s CFO wants an Excel `PivotTable` of `Scholarship Applications` that regional finance managers (who hold Dataverse licenses) can refresh live every Friday in desktop Excel while seeing ONLY their own region’s rows. Which export mode fits?

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Export as an Excel `Dynamic PivotTable`—each viewer authenticates to Dataverse on refresh and receives only rows authorized by their Security Role. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.

</details>

### Q043 (`T6-Q084`) — Manage environments [4.1] · *Single-Answer Multiple Choice*

Case study — Atlas Field Scholarships: Before UAT cutover, Atlas’s Functional Consultant wants to verify screen-reader `AccessibleLabel` properties and blue Dataverse delegation triangles inside the `Reviewer Scoring` Canvas app right inside Power Apps Studio. Which tool surfaces both checks interactively?

- **A.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)
- **B.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Open `App Checker` in Power Apps Studio (`Accessibility` and `Performance` categories), whereas `Solution Checker` runs static analysis across full Solutions. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.
- **B:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q044 (`T6-Q089`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

Case study — Atlas Field Scholarships: Atlas retired a legacy `PaperApplicationBarcode` column from Unmanaged Dev solution `AtlasScholarships` and promoted version `3.0.0.0` (Managed) via `Power Platform pipelines` to Production. Which Managed import behavior ensures `PaperApplicationBarcode` is deleted cleanly from Production?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Deploying as a Managed `Solution Upgrade` (`Stage for upgrade` -> `Apply upgrade`) removes components deleted from the new solution version while preserving remaining schema and data. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.

</details>

### Q045 (`T6-Q092`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

Westbrook wants to refresh its `Dev-Config` Sandbox from Production so functional consultants have the exact latest Production schema, forms, and views, WITHOUT copying 250,000 applicant FERPA records or sending live emails to students. Which PPAC operation should an admin run?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **D.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Run `Copy` from Production to `Dev-Config` selecting `Minimal Copy` (schema and customizations only, excluding business rows and keeping background processes/mailboxes disabled). [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **D:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.

</details>

### Q046 (`T6-Q076`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

If a Grant Officer tries to change `Grant Award` status to `Closed` while `FinalImpactReportSubmitted = No`, Dataverse must synchronously cancel the save inside the database transaction and display `"Cannot close grant before Final Impact Report is submitted"`. How do you build this without C#?

- **A.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a `Real-time (synchronous)` classic Dataverse workflow (or Pre-operation low-code plug-in) ending with `Stop workflow = Canceled` and the custom message. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.

</details>

### Q047 (`T6-Q046`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

When borehole engineers submit pressure readings from `txtPsi` onto `Valves`, satellite drops or validation errors must show a red `Notify` banner with `FirstError.Message`. Complete the Power Fx formula: ____.

- **A.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **B.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `ModelDrivenFormIntegration.Item`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))` catches runtime failures gracefully. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Correct — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **B:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.

</details>

### Q048 (`T6-Q066`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

Why is configuring a `@equals(...)` `Trigger Condition` in trigger settings superior to letting a cloud flow trigger on every row edit and immediately placing a `Condition` -> `Terminate` step on line 1?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A `Trigger Condition` prevents non-matching events from starting a flow run at all—saving Power Platform API requests and keeping 28-day Run History clean. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Correct — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q049 (`T6-Q077`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

Admissions policy forbids saving an `Admission Offer` row if `DeanSignatureVerified = No`. Proposed solution: Configure only a Background (asynchronous) classic workflow—or an Automated cloud flow—to check `DeanSignatureVerified` after save. Does this block saving an unsigned offer?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No—both Background classic workflows and Automated cloud flows execute post-commit and cannot abort the save transactionally. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **C:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q050 (`T6-Q054`) — Create apps by using Microsoft Power Apps [2.12] · *Ordered Sequence (Multiple Choice)*

Verified NGO grant managers signing into `GlobalAid Grant Portal` must view and edit `Grant Budget` rows belonging to their NGO while public visitors have zero access. Order the exact Power Pages data-security steps.

- **A.** Leave Enable Table Permissions unchecked → Assign Global Delete privilege to the Anonymous Users Web Role → Enable deprecated local password login → Publish to internet
- **B.** Share the internal Model-Driven App URL publicly → Disable SSL certificates in Set up workspace → Hardcode an API admin token in client JavaScript → Skip Page Access Rules
- **C.** Assign Dataverse internal Security Roles directly to anonymous web visitors → Skip Web Roles entirely → Add a Business Rule on Form load → Restart the portal without syncing
- **D.** Enable Table Permissions on the Power Pages Basic Form or List → Create a Table Permission scoped to Contact/Account with required privileges → Assign it to a custom Web Role → Associate authenticated Contacts with that Web Role

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable Table Permissions on the Basic Form and List, create an `Account`-scoped `Table Permission` with needed privileges, assign it to the `Verified Grantee` Web Role, and associate authenticated NGO Contacts with that Web Role. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — Granting Global Delete to Anonymous Users exposes every Dataverse row to public deletion, and Microsoft recommends external IdPs (Entra External ID) over local auth.
- **B:** Incorrect — Exposing admin tokens in browser JavaScript or sharing internal model-driven URLs violates Power Pages security architecture.
- **C:** Incorrect — External Power Pages Contacts do not use internal Dataverse Security Roles; portal authorization uses Table Permissions mapped to Web Roles.
- **D:** Correct — Power Pages secures Dataverse Lists/Forms by enabling Table Permissions on the component, defining row-access scope (Global/Contact/Account/Parent/Self), and binding to Web Roles.

</details>

### Q051 (`T6-Q047`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

A volunteer check-in Canvas app uses `Set(gblSelectedAttendee, ThisItem)` across 6 screens, causing accidental cross-screen overwrites when volunteers open a side lookup modal. Proposed solution: Pass attendee context explicitly to the detail screen using `Navigate(AttendeeDetailScreen, ScreenTransition.Fade, {locAttendee: ThisItem})` and manage single-screen modal flags with `UpdateContext(...)`. Does this isolate screen variables properly?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Yes—`Navigate` context records and `UpdateContext` scope variables strictly to the target screen rather than mutating global app state. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Correct — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.

</details>

### Q052 (`T6-Q087`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

You shipped `WestbrookAdmissions` `2.0.0.0` (Managed) to Production, then deployed hotfix Patches `2.0.1.0` and `2.0.2.0`. Now you need to unlock the parent solution in Dev and consolidate everything into version `2.1.0.0`. Which action in Dev accomplishes this?

- **A.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Select the base Unmanaged solution `WestbrookAdmissions` (`2.0.0.0`) and execute `Clone to Solution` (`2.1.0.0`). [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Incorrect — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q053 (`T6-Q079`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

Across 8 grant-processing cloud flows, you want to invoke a single governed Dataverse custom action / reusable sub-routine (`CalculateIndirectCostCap`) without duplicating 10 flow steps in all 8 flows. Which two native Dataverse/Power Automate capabilities fit?

- **A.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **B.** The Dataverse connector supports `Change type`, `Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows` / `Unrelate rows`, bound/unbound actions, and reusable solution `Child Flows`
- **C.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Invoke a solution `Child Flow` (`Run a Child Flow`) or call a Dataverse bound/unbound Custom API (`Perform a bound/unbound action`, including `Instant` low-code plug-ins). [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **B:** Correct — Setting both `Select columns` and `Filter rows` on Dataverse triggers avoids firing flows when unrelated columns change.
- **C:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q054 (`T6-Q070`) — Create and manage logic and process automation [3.6] · *Single-Answer Multiple Choice*

How can a Functional Consultant unit-test a cloud flow’s retry and `Catch` Scope behavior against simulated `429 Rate Limit` or `502 Bad Gateway` connector responses without hammering a partner university’s live REST server?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **C.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **D.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable `Static Result` on the connector action during testing to return simulated HTTP error codes and headers. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **C:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **D:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.

</details>

### Q055 (`T6-Q064`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

When emailing campus interview confirmations in Power Automate, optional `orc_alternatedate` must format as `yyyy-MM-dd` if populated, or fall back to `orc_primarydate` if null. Complete the WDL expression: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **C.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')` safely selects the first non-null date. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Correct — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **C:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q056 (`T6-Q067`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

Your humanitarian logistics cloud flow uses `When a row is added, modified or deleted` (`Modified`) and burns daily API quota on irrelevant updates; narrow the native Dataverse connector inputs to watch strictly `orc_permitstatus` and `orc_district` on active rows (`statecode eq 0`) matching choice `100000002`: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Set `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Correct — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **C:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q057 (`T6-Q048`) — Create apps by using Microsoft Power Apps [2.9] · *Ordered Sequence (Multiple Choice)*

Pressing `Issue Instant Tax Receipt PDF` in the `Alumni Gala Check-In` Canvas app must call a solution cloud flow, return `ReceiptNumber` synchronously into `varOut`, and keep 120 event volunteers as `Run-only users`. Put the steps in exact order.

- **A.** Create a classic Background Dataverse workflow → Embed an iframe pointing to flow.microsoft.com → Store maker passwords inside a Canvas text label → Poll Run History manually
- **B.** Use a Scheduled Recurrence trigger first → Omit Respond to a Power App or flow → Hardcode FlowName.Run() before adding the flow to the app → Grant Co-owner rights to all 500 end users
- **C.** Build a solution flow with the Power Apps (V2) trigger & typed inputs → End with Respond to a Power App or flow → Add the flow in Canvas Studio Power Automate pane → Call Set(varOut, FlowName.Run(...)) & set Run-only users
- **D.** Remove all triggers from the cloud flow → Export the flow outside any Solution → Bind a Quick View form to the button → Expect synchronous values after 45-minute waits

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Build a solution flow with `Power Apps (V2)` typed inputs, end with `Respond to a Power App or flow`, add it in Canvas Studio, and invoke `Set(varOut, FlowName.Run(...))` with `Run-only users`. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Canvas apps invoke cloud flows natively through the Power Apps (V2) trigger and FlowName.Run() connector bridge, never via iframes or plaintext credentials.
- **B:** Incorrect — Scheduled flows cannot be invoked synchronously via FlowName.Run(), and end users need Run-only user permissions rather than Co-owner edit rights.
- **C:** Correct — Canvas-invoked flows define typed inputs on Power Apps (V2), return outputs via Respond to a Power App or flow, bind in Studio, and capture outputs via FlowName.Run(...).
- **D:** Incorrect — Every cloud flow requires a trigger, and Respond to a Power App or flow must return within the synchronous HTTP timeout window (~120 seconds).

</details>

### Q058 (`T6-Q028`) — Configure Microsoft Dataverse [1.12] · *Single-Answer Multiple Choice*

Under `Manager` Hierarchy Security configured with `Depth = 2`, Dean Alvarez manages Director Chen (level 1), who manages Counselor Brooks (level 2). Can Dean Alvarez edit (`Write`) an `Admission Application` owned by Counselor Brooks?

- **A.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **B.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No—under `Manager` Hierarchy Security, Dean Alvarez receives Read/Write/Update/Append/Append To on direct report Director Chen (level 1), but strictly `Read-only` access on indirect report Counselor Brooks (level 2). [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **B:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q059 (`T6-Q045`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Field water-sanitation NGO engineers select `ddDistrict` before visiting remote village boreholes and cache matching `Valves` / pump records into `colOfflineValves`. Complete the delegable Power Fx formula: ____.

- **A.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))` clears old items and caches the delegable `Filter` result locally. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Correct — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

### Q060 (`T6-Q031`) — Create apps by using Microsoft Power Apps [2.1] · *Multi-Select (Select 2)*

You are selecting form types (`Main`, `Quick Create`, `Quick View`, `Card`) for the `Advancement & Grants` model-driven app. Which TWO statements accurately describe these form types? Select two.

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). `Main` forms support role-based `Form Order` + `Fallback`, `Quick Create` powers rapid slide-out creation, and `Quick View` renders read-only parent Lookup fields (whereas `Form Component Control` edits them inline). [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Correct — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q061 (`T6-Q093`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

University InfoSec mandates blocking the `HTTP` connector from ever sharing data with `Microsoft Dataverse` in the `Citizen Makers` environment while still allowing `HTTP` + `Dataverse` inside the dedicated `Integration Prod` environment. How do you scope `DLP` policies to achieve this?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **D.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create two environment-scoped `Data Loss Prevention (DLP)` policies in PPAC—excluding `Integration Prod` from the restrictive citizen DLP policy and applying a tailored integration DLP policy to `Integration Prod`. [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **D:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.

</details>

### Q062 (`T6-Q057`) — Create and manage logic and process automation [3.1] · *Single-Answer Multiple Choice*

When a Grant Officer sets `Grant Award` status to `Disbursed`, Dataverse must synchronously abort the save if `SanctionsCheckPassed = No`, while asynchronously sending a wire file to SAP and notifying Slack/Teams after commit. How should you architect this?

- **A.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **D.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enforce the pre-commit sanctions check synchronously via a `Real-time classic workflow` or `Pre-operation low-code plug-in`, and run the SAP + Teams integrations asynchronously via an `Automated cloud flow`. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **D:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.

</details>

### Q063 (`T6-Q011`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

A `Philanthropic Pledge` can be made either by a corporate sponsor (`Account`) or an individual alumnus (`Contact`) using a single lookup field on the pledge form. Which native column type supports both target tables?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **C.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **D.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Use a polymorphic `Customer` lookup column on `Philanthropic Pledge`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **C:** Incorrect — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **D:** Correct — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.

</details>

### Q064 (`T6-Q034`) — Create apps by using Microsoft Power Apps [2.3] · *Single-Answer Multiple Choice*

A scholarship coordinator builds a `Personal View` filtering `Scholarship Applications` to `FirstGenerationStudent = Yes` and wants the `STEM Review Team` to view and use her saved filter without giving them permission to modify or delete her view definition. How can she share it?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Open `Manage and share views`, select her `Personal View`, share it with `STEM Review Team`, and grant ONLY the `Read` permission (leaving `Write`, `Delete`, `Assign`, and `Share` unchecked). [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.

</details>

### Q065 (`T6-Q088`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

What is the functional purpose of the `Option Value Prefix` (`10000`–`99999`) configured on a custom `Solution Publisher` in Dataverse?

- **A.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **D.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). It stamps a unique leading integer range (such as `742050000`) on custom `Choice` / `Choices` option values created under that publisher, preventing integer collisions across independent solutions. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **D:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q066 (`T6-Q012`) — Configure Microsoft Dataverse [1.5] · *Ordered Sequence (Multiple Choice)*

Grant officers want global Dataverse Search in the model-driven header bar to match `NGO_RegistrationCode` and `GrantReferenceID` on `Grant Application` and return `RequestedAmount` and `Country` in search cards. Order the exact setup steps.

- **A.** Delete the table Quick Find View first → Disable Dataverse Search in PPAC → Add columns only to a Personal View → Export an Unmanaged solution without publishing
- **B.** Enable Dataverse Search in PPAC environment Features → Open the table Quick Find View in the solution → Add Find Columns (indexed) and View Columns (returned) → Save and publish all customizations
- **C.** Connect SSMS directly to Dataverse SQL → Create custom clustered T-SQL indexes on base tables → Restart IIS on the Dataverse server → Clear local browser cache
- **D.** Turn on Column-Level Security for every text column → Create a Bulk Record Deletion job → Configure a Business Rule on Form load → Share the Personal View

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable Dataverse Search in PPAC environment Features, open the `Grant Application` Quick Find View in your solution, add `Find Columns` and `View Columns`, and publish all customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Incorrect — Personal views never control Dataverse Search indexing, and disabling Dataverse Search turns off Relevance Search across the environment.
- **B:** Correct — Dataverse Search requires enabling the environment feature in PPAC and configuring each table’s Quick Find View Find Columns (search index) and View Columns.
- **C:** Incorrect — Dataverse is SaaS-managed; makers cannot create raw T-SQL indexes or restart IIS—search indexing is governed through PPAC and Quick Find Views.
- **D:** Incorrect — Column Security, Bulk Deletion, and Business Rules do not index tables or fields for Dataverse Search.

</details>

## Case Study Vignette — Horizon Alumni Engagement

> [Scenario: Horizon Alumni Engagement uses a model-driven Donor app and Canvas event check-in app. Advancement officers want `Lifetime Giving Total` aggregated automatically across child `Donation` rows (`SUM`), `Days Since Last Gift` computed via Power Fx formula column, and a modern command-bar `Mark VIP` button visible only when `Lifetime Giving Total >= 50000`.]

### Q067 (`T6-Q009`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

Case study — Horizon Alumni Engagement: Horizon configures a `Lifetime Giving Total` Rollup column (`SUM` of posted child `Donation` rows) AND a `Days Since Last Gift` Power Fx Formula column on `Donor Contact`. How do these two column types differ at runtime?

- **A.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **D.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Rollup` column aggregates child rows asynchronously via a background system job (minimum 1-hour schedule or manual form refresh), whereas the `Power Fx Formula` column computes live on read. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Correct — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **D:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.

</details>

### Q068 (`T6-Q040`) — Create apps by using Microsoft Power Apps [2.5] · *Multi-Select (Select 2)*

Case study — Horizon Alumni Engagement: Horizon wants a modern command-bar button `Mark VIP` on `Donor Contact` that appears ONLY when `Lifetime Giving Total >= 50000` and patches `VIPFlag = Yes` when clicked. Which TWO Modern Commanding facts apply? Select two.

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **E.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Set the button’s `Visible` property to Power Fx `Self.Selected.Item.'Lifetime Giving Total' >= 50000` (stored in the managed `Component Library`), and update the row in `OnSelect` via `Patch(...)` + `Notify(...)`. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **E:** Correct — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.

</details>

### Q069 (`T6-Q043`) — Create apps by using Microsoft Power Apps [2.7] · *Single-Answer Multiple Choice*

Case study — Horizon Alumni Engagement: Event volunteers run Horizon’s `Alumni Gala Check-In` Canvas app on phones at the door and landscape laptops at registration tables, sharing a branded `University Crest Header` across 4 event apps. What should you configure?

- **A.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **B.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Disable `Scale to fit`, arrange controls inside nested `Horizontal` and `Vertical` auto-layout containers, and build `University Crest Header` inside a solution-aware `Component Library`. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **B:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q070 (`T6-Q019`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Grant officers need Dataverse to reject saving duplicate `FederalUEINumber` values on `NGO Account` synchronously inside the SQL transaction. Proposed solution: Build only an asynchronous Automated Power Automate cloud flow (`When a row is added`) to check `FederalUEINumber` after save. Does this prevent committing duplicate rows at save time?

- **A.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No—Automated cloud flows execute asynchronously after commit; enforce database-level synchronous uniqueness with an `Alternate Key` (or Pre-operation low-code plug-in / Real-time workflow). [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q071 (`T6-Q013`) — Configure Microsoft Dataverse [1.5] · *Single-Answer Multiple Choice*

Admissions counselors report that withdrawn applications (`Status = Inactive`) clutter global Dataverse Search results for `Admission Application`. Where do you exclude withdrawn rows from Dataverse Search?

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Update the filter criteria on the `Admission Application` `Quick Find View` (`Status Equals Active`) and publish customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **D:** Correct — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

### Q072 (`T6-Q049`) — Create apps by using Microsoft Power Apps [2.9] · *Single-Answer Multiple Choice*

When calling a cloud flow from a Canvas app via `Set(varReceipt, IssueTaxReceipt.Run(ThisItem.ContactId))`, which action inside the cloud flow defines the named properties (for example `varReceipt.receiptnumber`) returned synchronously to Power Fx?

- **A.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The `Respond to a Power App or flow` action defines typed output properties returned synchronously to the calling Canvas formula. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Correct — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **B:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.

</details>

### Q073 (`T6-Q008`) — Configure Microsoft Dataverse [1.3] · *Multi-Select (Select 2)*

You are reviewing `1:N` relationship behaviors across `Grant Application`, `Budget Line Item`, and `Donor Account`. Which TWO configurations behave as described? Select two.

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). A `Parental` relationship on `Grant Application` -> `Budget Line Item` cascades Delete/Assign/Share to every budget line, while `Custom` (`Assign = Cascade Active`, `Delete = Restrict`) scopes cascading selectively. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q074 (`T6-Q069`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

When an `Applicant Contact` accepts admission, a cloud flow links that `Contact` to mandatory `First-Year Orientation Cohort` rows across a native `N:N` relationship. Complete the Dataverse connector step: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Use the Dataverse `Relate rows` action supplying the `N:N` relationship schema name and target `@odata.id` (`OData Id`). [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Correct — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.

</details>

### Q075 (`T6-Q015`) — Configure Microsoft Dataverse [1.6] · *Multi-Select (Select 3)*

Global scholarship finance and compliance leads are reviewing Dataverse auditing, analytics, and Excel export options across five continents. Which THREE statements are accurate? Select three.

- **A.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **E.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **F.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E, F` (`CSV: 1,5,6`)

Correct answers: A, E, and F (are correct). Three-tier Auditing logs deltas in `Log` storage, `Dynamic PivotTable`/`Dynamic Worksheet` exports refresh live rows per user’s Security Role (unlike `Static` snapshots), and `Dataflows` / `Fabric Link` handle ETL and continuous analytics. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **E:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **F:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.

</details>

### Q076 (`T6-Q090`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

An admin notices a `Grant Award` view in Production has an `Unmanaged (Active)` layer created during an emergency hotfix last year, masking Managed updates. Proposed solution: Re-import the Managed solution choosing `Update` without running `Remove Active Customizations`, expecting `Update` to delete both the unmanaged Active layer and retired columns. Why does this fail on BOTH counts?

- **A.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Managed `Update` neither removes `Unmanaged (Active)` top layers (`Remove Active Customizations` is required) nor deletes retired components (`Upgrade` is required). [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Correct — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.

</details>

### Q077 (`T6-Q060`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

Why does a Dataverse `When a row is added, modified or deleted` trigger consume zero wasted polling runs overnight when zero grant applications arrive?

- **A.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **B.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse triggers register push `webhooks` inside the server event pipeline, firing ONLY when matching database commits occur. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Correct — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **B:** Incorrect — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.

</details>

### Q078 (`T6-Q099`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Grant officers generate a `Grant Award Agreement.docx` Microsoft Word Template from `Grant Award` showing header terms plus a dynamic table of child `Milestone Tranche` rows (`1:N`). Complete the Word desktop XML mapping step: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `ModelDrivenFormIntegration.Item`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable the `Developer` tab, open `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`), and wrap the milestone row in a `Repeating` content control (up to `100` child rows). [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **C:** Correct — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.

</details>

### Q079 (`T6-Q091`) — Manage environments [4.3] · *Multi-Select (Select 2)*

You are documenting ALM governance standards for global nonprofit and university teams. Which TWO solution-layering rules are accurate? Select two.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **D.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **E.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, D` (`CSV: 3,4`)

Correct answers: C and D (are correct). Inspect `See solution layers` -> `Remove Active Customizations` to clear unmanaged drift in UAT/Prod, and use `Clone a Patch` / `Clone to Solution` + Managed `Upgrade` to roll out consolidated releases cleanly. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **D:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **E:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q080 (`T6-Q052`) — Create apps by using Microsoft Power Apps [2.11] · *Single-Answer Multiple Choice*

GlobalAid’s `Full Grant Proposal` wizard spans 4 sequential pages (`NGO Eligibility` -> `Condition: Region = ConflictZone` -> `Security Evacuation Plan` -> `Budget & SharePoint Audit PDFs`). Which Power Pages component provides conditional multi-page progress indicators and SharePoint integration?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **D.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure a Power Pages `Multi-Step Form` with `Load Form` steps, a `Condition` branching step, and a SharePoint document subgrid step. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **D:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.

</details>

### Q081 (`T6-Q042`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

University deans want an interactive `Power BI` `Annual Fund Campaign` dashboard accessible directly from the Dashboard picker inside the `Advancement` model-driven app. How do you surface it?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** An embedded Canvas app on a Main form reads the live host record via `ModelDrivenFormIntegration.Item`, while Power BI dashboards, reports, and tiles embed as system dashboards or contextual form visuals
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable Power BI visualization/dashboard embedding in PPAC environment settings and add a `Power BI Embedded` dashboard component inside your Solution and App Designer. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Correct — `ModelDrivenFormIntegration.RefreshForm(false)` refreshes the host model-driven form after an embedded Canvas control commits changes.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.

</details>

### Q082 (`T6-Q021`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Interdisciplinary `STEM Grant Specialists` belong to the `Provost Office` Business Unit (which must remain the owning BU of grants they create), yet they also evaluate applications inside the `School of Engineering` and `School of Medicine` Business Units without accessing `Law School` records. Which feature enables this?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable `Modernized Business Units` and assign roles scoped directly to `School of Engineering` and `School of Medicine` to those specialists. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **C:** Correct — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q083 (`T6-Q074`) — Create and manage logic and process automation [3.8] · *Ordered Sequence (Multiple Choice)*

In the `Due Diligence` stage of `Grant Lifecycle BPF`, reviewers want an on-demand `Verify Charity Registry` button inside the BPF stage flyout that runs a solution cloud flow. Put the configuration steps in exact order.

- **A.** Create a solution Instant flow using When a flow step is run from a business process flow → Open the BPF designer in the same Solution → Add a Flow Step inside the target Stage & bind the flow → Validate, save, and Activate the BPF
- **B.** Delete the BPF underlying Dataverse table → Record a desktop flow on a local laptop → Disable BPF security roles → Overwrite Active BPF instances manually in SQL
- **C.** Build a personal My Flows cloud flow outside any Solution → Use an Outlook email trigger → Paste the flow URL into a BPF text column → Leave the BPF in Draft state
- **D.** Add 12 stages across 9 unrelated tables in one BPF → Skip Lookup relationships between tables → Trigger an Unattended RPA flow directly without a gateway/machine → Save without validation

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Build a solution Instant flow using `When a flow step is run from a business process flow`, open the BPF in the same Solution, add a Flow Step in `Due Diligence`, and Validate/Save/Activate the BPF. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Correct — To run a cloud flow from a BPF stage button, both the BPF and the flow (using the BPF flow-step trigger) must reside in a Solution before binding and activating.
- **B:** Incorrect — Every BPF automatically maintains its own Dataverse table for stage tracking and requires security role enablement rather than SQL manipulation.
- **C:** Incorrect — Non-solution flows and non-BPF triggers cannot be bound as BPF Flow Steps, and Draft BPFs do not render for users.
- **D:** Incorrect — A Business Process Flow supports at most 30 stages and at most 5 related tables connected via 1:N relationships.

</details>

### Q084 (`T6-Q033`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

During scholarship committee meetings, reviewers want to edit scores and ranking notes directly inline across 30 child `Rubric Score` rows inside a subgrid on `Scholarship Application` without opening 30 separate child forms. Which control enables this?

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Add the `Editable Grid` control to the `Rubric Score` subgrid (and optionally use `Filter by related rows` on Lookup fields). [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q085 (`T6-Q035`) — Create apps by using Microsoft Power Apps [2.3] · *Multi-Select (Select 2)*

You are customizing views for `Donor Contact` and `Donation` inside your solution. Which TWO view behaviors are accurate? Select two.

- **A.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). `Lookup View` controls columns displayed in Lookup dropdown pickers while `Associated View` controls Related-tab grids, and `Public` views support adding parent `N:1` columns plus multi-column sorting. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q086 (`T6-Q065`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

A campus event-security flow must not start a flow run unless `orc_permitstatus` equals `100000002` and `orc_district` equals `'Downtown'`. Complete the `Trigger Condition` expression: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `ModelDrivenFormIntegration.Item`
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))` evaluates at the trigger gate before starting a run. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Correct — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **C:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q087 (`T6-Q058`) — Create and manage logic and process automation [3.1] · *Multi-Select (Select 2)*

Westbrook University’s COE is training new Functional Consultants on selecting the right process-automation engine. Which TWO statements are accurate? Select two.

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). `Business Process Flows` guide human users across up to `30` stages and `5` related tables, while `Cloud flows` handle async integrations and `Real-time workflows` / `Low-code plug-ins` enforce synchronous Dataverse rollbacks. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.

</details>

### Q088 (`T6-Q030`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

You configure a model-driven Sitemap with two `Areas` (`Admissions Office` and `Alumni Advancement`), each containing `Groups` and `Subareas`. What happens when a student worker whose role lacks `Read` privilege on `Major Gift` opens the app?

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **D.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Major Gift` table subarea is automatically hidden from the Sitemap navigation pane for that student worker. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Correct — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **D:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.

</details>

### Q089 (`T6-Q083`) — Create and manage logic and process automation [3.12] · *Multi-Select (Select 3)*

You are summarizing server-side vs client-side low-code logic options for university makers. Which THREE statements are true? Select three.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **E.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors
- **F.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E, F` (`CSV: 2,5,6`)

Correct answers: B, E, and F (are correct). Business Rules at `Entity` scope run server-side (while form scopes run on model-driven forms), `Power Fx Functions` centralize reusable server formulas, and `Dataverse Accelerator` low-code plug-ins execute `Instant` or `Automated` Power Fx server-side. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **E:** Correct — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.
- **F:** Correct — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.

</details>

## Case Study Vignette — GlobalAid Grant Portal

> [Scenario: GlobalAid Grant Portal runs a Microsoft Power Pages site where NGOs apply for humanitarian grants. Unauthenticated visitors can read `Grant Guidelines`, only `Verified Grantee` Web Role members can open the `/submit-budget` webpage via Page Access Control Rules, and NGOs upload audited PDF financial statements directly into SharePoint folders from a Power Pages Basic Form.]

### Q090 (`T6-Q050`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

Case study — GlobalAid Grant Portal: Unauthenticated visitors browsing `GlobalAid Grant Portal` read public `Open Grant Calls` from a Dataverse view, while authenticated NGOs open `/submit-budget` to create a `Grant Budget` row and attach audited PDFs to SharePoint. Which Design Studio components support this?

- **A.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **B.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **C.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Place a read-only `List` on the public page and an `Insert`/`Edit` `Basic Form` (with SharePoint document subgrid and `Enable Table Permissions` checked) on `/submit-budget`. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **B:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **C:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q091 (`T6-Q055`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

Case study — GlobalAid Grant Portal: GlobalAid wants the entire `/submit-budget` webpage (including its navigation menu link and static instructions) completely hidden and blocked from anonymous visitors and unverified users—accessible ONLY to Contacts holding the `Verified Grantee` Web Role. Which Power Pages feature restricts whole-webpage access?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create a `Page Access Control Rule` (`Restrict Read`) on the `/submit-budget` webpage and grant it exclusively to the `Verified Grantee` Web Role. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.

</details>

### Q092 (`T6-Q056`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

Case study — GlobalAid Grant Portal: Any finance officer `Contact` belonging to `CleanWater Kenya NGO` (`Account`) must view and update `Grant Budget` / `Warranty Claim` disbursement rows submitted by colleagues at that same NGO `Account`. Complete the Power Pages Table Permission setting: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure a `Table Permission` with `Access Type = Account` linked to the `NGO Account` lookup relationship (whereas individual student scholarship applicants use `Access Type = Contact` via ____ or Contact lookup). [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q093 (`T6-Q072`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

GlobalAid’s `Grant Lifecycle BPF` spans `Inquiry` -> `Application` -> `Due Diligence` -> `Grant Award` (`4` related tables) and branches into an `OFAC Enhanced Vetting` stage when `HighRiskRegion = Yes` in `Due Diligence`. What happens if an architect tries to span `6` distinct Dataverse tables in that single BPF?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). BPF validation blocks saving because a single Business Process Flow can span at most `5` related Dataverse tables (and up to `30` stages). [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q094 (`T6-Q094`) — Manage environments [4.5] · *Ordered Sequence (Multiple Choice)*

You are exporting `GlobalAidGrants` from Dev and importing it as Managed into Production where SharePoint NGO libraries, Key Vault API secrets, and service accounts differ per stage. Order the exact ALM steps.

- **A.** Import an unvalidated solution into Production first → Run Solution Checker two weeks later → Create Environment Variables directly inside Production Default Solution → Skip publishing
- **B.** Clear Dev Current Values on Environment Variables & run Solution Checker → Publish all customizations & Export as Managed → Import the Managed `.zip` into UAT/Production → Bind target Connection References & Environment Variable values
- **C.** Delete the Managed solution in Production every Friday (removing custom table data!) → Recreate tables manually → Re-import CSV backups → Reassign all Security Roles
- **D.** Export the entire Default Solution from Dev as Unmanaged → Import Unmanaged directly into Production → Hardcode Dev URLs inside flow steps → Share personal maker logins

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Clear Dev `Current Values` from Environment Variables and run Solution Checker, Publish all customizations and Export as `Managed`, Import into UAT/Production, and bind target Connection References and Environment Variable values. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Unpublished changes in Dev are excluded from exported solutions, and Solution Checker should gate packages before Production import.
- **B:** Correct — Healthy ALM runs Solution Checker, publishes customizations, exports as Managed, and binds target-stage Connection References and Environment Variables at import.
- **C:** Incorrect — Deleting a Managed solution that defines custom tables permanently deletes those tables and their Production data; use Managed Upgrade (`Stage for upgrade`) instead.
- **D:** Incorrect — Never export the Default Solution or import Unmanaged solutions into Production; use segmented Managed solutions with Connection References and Environment Variables.

</details>

### Q095 (`T6-Q024`) — Configure Microsoft Dataverse [1.10] · *Multi-Select (Select 2)*

You are reviewing Westbrook University’s Dataverse security architecture. Which TWO statements accurately describe Security Role privileges and Team types? Select two.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Populating a Lookup requires `Append` (child) + `Append To` (parent), and `Microsoft Entra ID Group Teams` grant role access dynamically from Entra groups while `Access Team Templates` handle lightweight per-row sharing. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q096 (`T6-Q062`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

A scholarship-scoring flow iterates through 1,500 `Application` rows inside `Apply to each` updating a top-level `Integer` variable `varWeightedScore` via `Set variable`. Proposed solution: Turn on `Apply to each` `Concurrency Control = 50` while keeping `Set variable` inside the loop to cut runtime from 20 minutes to 1 minute. Will scores remain accurate?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **C.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **D.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—parallel loop threads overwrite the shared `varWeightedScore` variable unpredictably; replace `Set variable` with an in-loop `Compose` expression before enabling parallel concurrency. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **C:** Incorrect — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **D:** Incorrect — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.

</details>

### Q097 (`T6-Q018`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

High-school applicants frequently submit duplicate `Applicant Contact` profiles matching `PersonalEmail` and `BirthDate`. Proposed solution: Create a Dataverse `Duplicate Detection Rule` on `Contact` matching exact `PersonalEmail` and `BirthDate`, save it, and select `Publish` while enabling Duplicate Detection on form save and import. Does this warn counselors and flag import duplicates?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **D.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes—explicitly publishing the rule activates interactive save warnings and import duplicate detection within the 5-published-rule per-table limit. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Correct — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **D:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.

</details>

### Q098 (`T6-Q027`) — Configure Microsoft Dataverse [1.12] · *Ordered Sequence (Multiple Choice)*

Only the `Financial Aid Verification` team may view unmasked values or update `ParentAdjustedGrossIncome` on `FAFSA Summary`, while admissions counselors who open `FAFSA Summary` must see masked values everywhere. Order the exact configuration steps.

- **A.** Enable column security on the sensitive Dataverse column & save → Create a Column Security Profile in the solution/PPAC → Set Read, Read Unmasked, Update, and Create permissions → Add authorized teams or users to the profile
- **B.** Delete Organization Read from all Security Roles first → Add users to an empty Business Unit → Hide the column via JavaScript on one Main form → Leave Enable column security unchecked
- **C.** Create a Blocked DLP policy in PPAC → Export table rows to SharePoint → Assign System Administrator to all clerks → Enable Duplicate Detection on the column
- **D.** Create an Access Team Template first → Turn off Microsoft Entra authentication → Mark the column as Business Required in a Business Rule → Publish without a Column Security Profile

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable column security on `ParentAdjustedGrossIncome`, create a `Column Security Profile`, set Read/Read Unmasked/Update/Create permissions, and add the `Financial Aid Verification` team. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct — Securing a sensitive column requires enabling column security on the column definition, creating a Column Security Profile, configuring field permissions, and adding users/teams.
- **B:** Incorrect — Hiding a field on a form does not secure API, Excel export, or view access; Enable column security + a Column Security Profile enforces server-side field security.
- **C:** Incorrect — DLP policies govern connectors rather than Dataverse field-level authorization, and System Administrator bypasses restrictions entirely.
- **D:** Incorrect — Access Team Templates share record-level rows, whereas field-level masking and Read/Update control require Column Security Profiles.

</details>

### Q099 (`T6-Q032`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

Grant reviewers working inside a `Grant Application` Main form need to edit `NGO Bank IBAN` and `ComplianceOfficerEmail` on the parent `NGO Account` Lookup directly inside a `Grantee Profile` tab without leaving `Grant Application`. Which control should you configure?

- **A.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **B.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **C.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure the `Form Component Control` bound to the `NGO Account` Lookup column pointing to a focused `Account` Main form. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **B:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **C:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q100 (`T6-Q038`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

On the Campus Facilities `WorkOrders` Main form modern command bar, pressing `Dispatch Crew` immediately updates `Dispatch Status` to `Dispatched` on the active record. Complete the Power Fx `OnSelect` formula: ____.

- **A.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **B.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})` patches `Self.Selected.Item` directly. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **B:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **C:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>
