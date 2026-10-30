# Microsoft Exam PL-200: Full-Length Mock Exam 5 — Reviewer Study Key

**Theme:** Wealth Advisory & Insurance — Manual N:N Intersects, Form Component Controls, Dataverse Expand Query & Solution Checker  
**Credential:** Microsoft Certified: Power Platform Functional Consultant Associate  
**Study guide baseline:** December 26, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)  
**Lifecycle notice:** Exam PL-200 retired on August 31, 2026 and was replaced by Exam AB-410 (Microsoft Certified: Intelligent Applications Builder Associate).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`T5-Q076`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

If a junior underwriter attempts to save a `Surety Bond` with `PenalSum > $5,000,000` without `ReinsuranceApproved = Yes`, Dataverse must roll back the save inside the database transaction and display `"Reinsurance sign-off required above $5M"`. Which classic workflow configuration achieves this?

- **A.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create a `Real-time (synchronous)` classic workflow triggered `Before`/`After` create or field change that executes `Stop workflow` with status `Canceled` and the custom error message. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q002 (`T5-Q035`) — Create apps by using Microsoft Power Apps [2.3] · *Multi-Select (Select 2)*

You are auditing Dataverse Views on `Surety Bond` and `Claim` before UAT. Which TWO statements accurately describe Dataverse view capabilities? Select two.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **E.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). `Public` views support parent `N:1` related columns, multi-column sorting, and cross-table filters, while `Lookup`, `Associated`, and `Personal` views serve lookup pickers, Related-tab grids, and user-shared ad-hoc filters. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **E:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.

</details>

### Q003 (`T5-Q048`) — Create apps by using Microsoft Power Apps [2.9] · *Ordered Sequence (Multiple Choice)*

Pressing `Fetch OFAC Sanctions Score` in a wealth-onboarding Canvas app must trigger a solution cloud flow, return `SanctionsClearanceCode` synchronously into `varOut`, and keep 200 advisors as `Run-only users`. Put the build steps in exact order.

- **A.** Use a Scheduled Recurrence trigger first → Omit Respond to a Power App or flow → Hardcode FlowName.Run() before adding the flow to the app → Grant Co-owner rights to all 500 end users
- **B.** Remove all triggers from the cloud flow → Export the flow outside any Solution → Bind a Quick View form to the button → Expect synchronous values after 45-minute waits
- **C.** Build a solution flow with the Power Apps (V2) trigger & typed inputs → End with Respond to a Power App or flow → Add the flow in Canvas Studio Power Automate pane → Call Set(varOut, FlowName.Run(...)) & set Run-only users
- **D.** Create a classic Background Dataverse workflow → Embed an iframe pointing to flow.microsoft.com → Store maker passwords inside a Canvas text label → Poll Run History manually

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create a solution flow with `Power Apps (V2)` typed inputs, end with `Respond to a Power App or flow`, add it in Canvas Studio, and invoke `Set(varOut, FlowName.Run(...))` with `Run-only users`. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Scheduled flows cannot be invoked synchronously via FlowName.Run(), and end users need Run-only user permissions rather than Co-owner edit rights.
- **B:** Incorrect — Every cloud flow requires a trigger, and Respond to a Power App or flow must return within the synchronous HTTP timeout window (~120 seconds).
- **C:** Correct — Canvas-invoked flows define typed inputs on Power Apps (V2), return outputs via Respond to a Power App or flow, bind in Studio, and capture outputs via FlowName.Run(...).
- **D:** Incorrect — Canvas apps invoke cloud flows natively through the Power Apps (V2) trigger and FlowName.Run() connector bridge, never via iframes or plaintext credentials.

</details>

### Q004 (`T5-Q079`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

Two classic workflows update `CalculatedCommission` and `NetPremium` on `Surety Bond`, triggering each other repeatedly until `System Jobs` halts with a recursion-depth error (~8–16 runs within an hour). How should you break the loop?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **C.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **D.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Restrict each workflow’s `Record fields change` trigger to only its specific input column and wrap update steps in a `Check Condition` verifying the value actually needs changing. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **C:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **D:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.

</details>

### Q005 (`T5-Q059`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

Why does importing a Managed solution containing 12 cloud flows stay active and clean in Production when all 12 flows share two `Connection References` (`Dataverse` and `SharePoint`) instead of embedded personal maker connections?

- **A.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **D.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Target-environment service-principal connections bind once to the two `Connection References` at import/pipeline time without creating unmanaged edits on the flows. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **D:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.

</details>

### Q006 (`T5-Q093`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

If a faulty bulk Dataflow corrupts 40,000 rows in Production at 14:15 today, which PPAC operation restores Production to its exact point-in-time state at 14:00 without overwriting Production Directly in place?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **D.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Restore a continuous `System Backup` (available for up to 28 days on Production) into a `Sandbox` environment first (or restore/copy back cleanly per recovery runbook). [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **D:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.

</details>

### Q007 (`T5-Q069`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

In Power Automate, an automated compliance flow must associate an existing `Surety Bond` row with an existing `Reinsurance Treaty` row across a native `N:N` relationship. Complete the Dataverse connector action: ____.

- **A.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **B.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **C.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Use the Dataverse `Relate rows` action passing the `N:N` relationship schema name and target `@odata.id` (`OData Id`). [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **B:** Correct — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **C:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q008 (`T5-Q037`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

Underwriting managers want a multi-column side-by-side `Bond Collateral Calculator` dialog launched as a modal overlay from the `Surety Bond` command bar using Power Fx `Navigate()`. Which modern app component should you create?

- **A.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a solution-aware `Custom Page` using nested `Horizontal` and `Vertical` responsive containers and add it to the model-driven app in App Designer. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Correct — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q009 (`T5-Q034`) — Create apps by using Microsoft Power Apps [2.3] · *Single-Answer Multiple Choice*

When underwriters search inside the `Policyholder` Lookup field on `Surety Bond`, two companies named `Summit Holdings LLC` in Delaware and Nevada look indistinguishable. Which view on `Policyholder` must you edit so `IncorporationState` and `FEINLastFour` appear right inside the Lookup dropdown?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Edit the `Policyholder` table’s `Lookup View` and place `IncorporationState` and `FEINLastFour` among the top columns. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q010 (`T5-Q074`) — Create and manage logic and process automation [3.8] · *Ordered Sequence (Multiple Choice)*

Underwriters in the `Sanctions Check` stage of `Commercial Surety BPF` want an interactive `Run LexisNexis Check` button right inside the BPF stage flyout that runs a solution cloud flow. Put the setup steps in exact order.

- **A.** Create a solution Instant flow using When a flow step is run from a business process flow → Open the BPF designer in the same Solution → Add a Flow Step inside the target Stage & bind the flow → Validate, save, and Activate the BPF
- **B.** Add 12 stages across 9 unrelated tables in one BPF → Skip Lookup relationships between tables → Trigger an Unattended RPA flow directly without a gateway/machine → Save without validation
- **C.** Delete the BPF underlying Dataverse table → Record a desktop flow on a local laptop → Disable BPF security roles → Overwrite Active BPF instances manually in SQL
- **D.** Build a personal My Flows cloud flow outside any Solution → Use an Outlook email trigger → Paste the flow URL into a BPF text column → Leave the BPF in Draft state

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a solution Instant flow using `When a flow step is run from a business process flow`, open the BPF in the same Solution, add a Flow Step inside `Sanctions Check`, and Validate/Save/Activate the BPF. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Correct — To run a cloud flow from a BPF stage button, both the BPF and the flow (using the BPF flow-step trigger) must reside in a Solution before binding and activating.
- **B:** Incorrect — A Business Process Flow supports at most 30 stages and at most 5 related tables connected via 1:N relationships.
- **C:** Incorrect — Every BPF automatically maintains its own Dataverse table for stage tracking and requires security role enablement rather than SQL manipulation.
- **D:** Incorrect — Non-solution flows and non-BPF triggers cannot be bound as BPF Flow Steps, and Draft BPFs do not render for users.

</details>

### Q011 (`T5-Q039`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

Compliance policy requires prompting the supervisor with a native confirmation dialog (`"Dispatch this technician now?"`) before patching `Status` on `WorkOrders`. Complete the Power Fx command formula: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `ModelDrivenFormIntegration.Item`
- **C.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **D.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))` confirms user intent before executing `Patch`. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **C:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **D:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.

</details>

### Q012 (`T5-Q028`) — Configure Microsoft Dataverse [1.12] · *Single-Answer Multiple Choice*

Why does hiding `ClientPassportNumber` with a client-side `Business Rule` fail a FINRA security audit compared with configuring a `Column Security Profile`?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **C.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Business Rules only hide controls on rendered model-driven forms (and cannot hide tabs or secure API/Excel/View queries), whereas `Column Security Profiles` enforce server-side field security everywhere. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Incorrect — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **C:** Incorrect — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **D:** Correct — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q013 (`T5-Q089`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

In QA, importing Managed `MeridianFilingCore` `5.3.0.0` did not update a Business Rule because an admin edited that Business Rule directly inside QA’s Default Solution last quarter. How do you inspect and fix this without resetting QA?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Open `See solution layers` on the Business Rule in QA, verify the `Unmanaged (Active)` layer at Layer 1, and select `Remove Active Customizations`. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **C:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q014 (`T5-Q024`) — Configure Microsoft Dataverse [1.10] · *Multi-Select (Select 2)*

You are designing Dataverse RBAC for wealth-management teams synced from Microsoft Entra ID. Which TWO configurations follow official Microsoft guidance? Select two.

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Copy `Basic User` with `Member’s privilege inheritance = Direct User (Basic) access level and Team privileges`, and assign roles to `Microsoft Entra ID Security Group Teams` for automated group-driven provisioning. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q015 (`T5-Q081`) — Create and manage logic and process automation [3.11] · *Single-Answer Multiple Choice*

An Automated `Pre-operation` Dataverse Accelerator plug-in on surety `PremiumOrder` (`Create`) must reject commercial brokerage submissions if the policyholder’s `CreditHold` flag is active and `OrderTotal` is positive. Supply the server-side Power Fx validation rule: ____.

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **D.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))` aborts the save transactionally. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Correct — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **D:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.

</details>

### Q016 (`T5-Q050`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

External surety brokers signing into Sterling’s Power Pages portal need a `/my-bonds` grid with keyword search plus a button to submit a new `Bond Application` row into Dataverse. Which two Design Studio components should you configure?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a `List` (with search and a `Create` action button) paired with a `Basic Form` set to `Insert` mode (`Enable Table Permissions` checked). [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **D:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

## Case Study Vignette — Meridian Regulatory Filing

> [Scenario: Meridian Regulatory Filing governs Dev, QA, and Production environments under strict audit controls. Before importing any solution, admins review static-analysis performance/security severities in Solution Checker, bind stage-specific SEC filing URLs and Azure Key Vault secrets via Environment Variables, and block `Microsoft Dataverse` from pairing with consumer connectors via DLP.]

### Q017 (`T5-Q084`) — Manage environments [4.1] · *Single-Answer Multiple Choice*

Case study — Meridian Regulatory Filing: Before importing any release candidate into QA or Production, Meridian’s release board requires an automated static-analysis report grading plug-in, web-resource, and flow issues as `Critical`, `High`, `Medium`, or `Low` with remediation guidance. Which tool produces this report?

- **A.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Run `Solution Checker` on the solution (and optionally enforce `Solution Checker` import gates via `Managed Environments`). [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.

</details>

### Q018 (`T5-Q092`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

Case study — Meridian Regulatory Filing: Meridian must prevent any Canvas app or Power Automate flow in Production from combining `Microsoft Dataverse` with consumer social-media or personal webmail connectors, while copying Production metadata (without confidential client rows) into a clean `Dev-Hotfix` Sandbox. Which two PPAC features accomplish this?

- **A.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **B.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enforce a `Data Loss Prevention (DLP)` policy classifying `Microsoft Dataverse` as `Business` (blocking `Non-Business`/`Blocked` mixing), and run a `Minimal Copy` from Production to `Dev-Hotfix`. [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **B:** Incorrect — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.

</details>

### Q019 (`T5-Q095`) — Manage environments [4.5] · *Single-Answer Multiple Choice*

Case study — Meridian Regulatory Filing: Meridian’s cloud flows read a stage-specific `SEC_EDGAR_BaseUrl` string and an encrypted `EDGAR_SigningCertSecret` stored in Azure Key Vault. Which solution components externalize both values cleanly across Dev, QA, and Production?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create a `Text` `Environment Variable` for `SEC_EDGAR_BaseUrl` and a `Secret` `Environment Variable` (backed by Azure Key Vault) for `EDGAR_SigningCertSecret`, removing Dev `Current Values` prior to export. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q020 (`T5-Q025`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

For ultra-high-net-worth `M&A Liquidity Deals`, a lead advisor grants temporary Read/Write collaboration on a single `Deal` row to 4 bespoke tax and trust specialists without owning rows or modifying Entra groups. Which team type should you configure?

- **A.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure an `Access Team Template` on `Deal` with an Access Team subgrid on the Main form. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **B:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q021 (`T5-Q078`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

An audit of Dataverse storage reveals 9 million `Succeeded` classic background workflow rows inside `System Jobs` (`ProcessSession`). Which checkbox on the background workflow definition prevents succeeded logs from accumulating while keeping failed job logs intact?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable `Automatically delete completed workflow jobs (to save disk space)` on the background workflow definition. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Correct — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.

</details>

### Q022 (`T5-Q090`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

Meridian removed a deprecated `LegacyTelexCode` column from Dev Unmanaged `MeridianFilingCore` and exported Managed `5.3.0.0`. Proposed solution: Import `5.3.0.0` into Production choosing `Update` rather than `Upgrade` so `LegacyTelexCode` is removed automatically. Does `Update` remove `LegacyTelexCode`?

- **A.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). No—Managed `Update` never deletes removed components; you must choose `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) to delete retired components from Production. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **D:** Correct — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q023 (`T5-Q083`) — Create and manage logic and process automation [3.12] · *Multi-Select (Select 3)*

You are reviewing low-code logic standards for Sterling Surety Insurance. Which THREE statements are accurate? Select three.

- **A.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors
- **E.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **F.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, D` (`CSV: 1,2,4`)

Correct answers: A, B, and D (are correct). Business Rules run server-side at `Entity` scope or client-side on forms; Business Rules CANNOT hide Tabs/Sections or evaluate `MultiSelect Choice` columns; and solution-aware `Power Fx Functions` centralize reusable server formulas. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Correct — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.
- **B:** Correct — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.
- **E:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **F:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q024 (`T5-Q058`) — Create and manage logic and process automation [3.1] · *Multi-Select (Select 2)*

Underwriting architects want a clear decision matrix comparing synchronous server-side Dataverse logic against asynchronous Power Automate cloud flows. Which TWO statements are true? Select two.

- **A.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). `Automated`/`Scheduled`/`Instant` cloud flows run asynchronously outside the Dataverse SQL save transaction, whereas `Real-time classic workflows` and `Pre-operation Dataverse low-code plug-ins` can abort invalid saves transactionally. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Correct — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q025 (`T5-Q072`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

An `Underwriting Review` Business Process Flow spans `Lead` -> `Application` -> `Surety Bond` and includes two role-specific BPFs (`Commercial Surety BPF` vs `Fidelity Bond BPF`). How do you control which roles see each BPF and which BPF opens first when a user has both roles?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **D.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable specific `Security Roles` on each BPF and set default priority via `Order Process Flow`. [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **D:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.

</details>

### Q026 (`T5-Q098`) — Manage environments [4.6] · *Single-Answer Multiple Choice*

Relationship managers want to track client Outlook emails and calendar meetings directly to `Advisory Account` rows using `Dynamics 365 App for Outlook`. Which mailbox synchronization method and security role are mandatory?

- **A.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **D.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Each user’s Mailbox must use `Server-Side Synchronization` (tested and enabled = `Success`) and the user must hold the `Dynamics 365 App for Outlook User` security role. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Correct — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **D:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.

</details>

### Q027 (`T5-Q001`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

A wealth-advisory data modeler mistakenly created `Client Risk Assessment` with `Ownership = Organization`, imported 9,500 assessments, and now learns regional compliance officers must restrict row access by Business Unit. What is the only supported path forward?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Because table `Ownership` cannot be altered after creation, create a new `User or team`-owned table, migrate the 9,500 rows, repoint forms/flows, and retire the Organization-owned table. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.

</details>

### Q028 (`T5-Q013`) — Configure Microsoft Dataverse [1.5] · *Single-Answer Multiple Choice*

When a wealth advisor enters a partial client code into global Dataverse Search, which specific view’s `Find Columns`, `View Columns`, and filter clauses determine whether a table’s rows match and which fields display?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **C.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **D.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Each search-enabled table’s `Quick Find View` controls indexed `Find Columns`, returned `View Columns`, and row filter exclusions. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **C:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **D:** Incorrect — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.

</details>

### Q029 (`T5-Q021`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Private-wealth estate planners reside in the `National Trust` Business Unit (which must own estate plans they author), yet they co-advise households in `Pacific Wealth` and `Mid-Atlantic Wealth` Business Units without accessing `Institutional Trading`. Which feature enables this cleanly?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable `Modernized Business Units` and assign matrix Security Roles directly to the planners for `Pacific Wealth` and `Mid-Atlantic Wealth`. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **C:** Correct — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q030 (`T5-Q016`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

Your quantitative risk team needs continuous, low-latency replication of 15 million `Policy Transaction` Dataverse rows into Microsoft Fabric OneLake / Azure Synapse without impacting interactive underwriting users. Which feature should you enable?

- **A.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **B.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries
- **C.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure `Azure Synapse Link for Dataverse` (`Link to Microsoft Fabric`) for continuous analytical replication. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **B:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.
- **C:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q031 (`T5-Q040`) — Create apps by using Microsoft Power Apps [2.5] · *Multi-Select (Select 2)*

You are training Functional Consultants on building buttons with `Modern Commanding`. Which TWO platform behaviors apply? Select two.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **C.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Modern Commanding stores Power Fx button logic inside a managed `Component Library` and supports `Self.Selected.Item`, `Confirm()`, `Notify()`, and `Patch()` across `Main form`, `Main grid`, `Subgrid`, and `Associated` bars. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **C:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q032 (`T5-Q065`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

To conserve API capacity, an underwriting alert flow must NOT start a run unless `orc_permitstatus` equals `100000002` and `orc_district` equals `'Downtown'`. Complete the `Trigger Condition` expression: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))` suppresses non-matching runs at the trigger gate. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Correct — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **C:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q033 (`T5-Q070`) — Create and manage logic and process automation [3.6] · *Single-Answer Multiple Choice*

Before deploying a `Report Suspicious Wire to FinCEN` cloud flow, you need to verify that your error-handling `Scope` triggers properly if the external FinCEN gateway returns HTTP `500`, WITHOUT sending fake filings to the live FinCEN endpoint. Which built-in Power Automate test feature should you use?

- **A.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure `Static Result` on the HTTP/connector action to return a mocked `500` error status during test runs. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.

</details>

### Q034 (`T5-Q097`) — Manage environments [4.6] · *Ordered Sequence (Multiple Choice)*

Compliance inquiries sent to `FilingsDesk@meridianregulatory.example` in Exchange Online must route automatically into a `Private` Dataverse Queue via Server-Side Synchronization. Order the exact configuration steps.

- **A.** Create a Personal View on the Contact table → Upload a Word Template → Run Bulk Record Deletion on ActivityPointer → Share the Queue via Anonymous Web Role
- **B.** Install deprecated Dynamics 365 Email Router on a Windows 7 PC → Skip Approve Email and Test & Enable Mailbox → Expect unapproved mailboxes to sync automatically → Disable Queues
- **C.** Verify Exchange Online Email Server Profile & Server-Side Sync defaults in PPAC → Create a Dataverse Queue with the shared email → Open the Queue Mailbox & select Approve Email → Run Test & Enable Mailbox until status = Success
- **D.** Open Outlook in a browser on a developer laptop → Record mouse coordinates with Power Automate for desktop → Copy email text into Notepad → Import CSV nightly

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Verify the Exchange Online `Email Server Profile` and Server-Side Sync defaults in PPAC, create the `Private` Dataverse Queue with its email address, `Approve Email` on the Queue Mailbox, and run `Test & Enable Mailbox` until status = `Success`. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — Views, Word Templates, and Bulk Deletion do not configure Exchange Server-Side Synchronization or Queue mailboxes.
- **B:** Incorrect — The legacy Email Router is deprecated; Server-Side Synchronization requires mailbox approval (when configured) and Test & Enable Mailbox succeeding.
- **C:** Correct — Routing shared-inbox emails into a Dataverse Queue via Server-Side Sync requires an Email Server Profile, a Queue with email address, Email Approval, and Test & Enable Mailbox.
- **D:** Incorrect — Dataverse includes native Exchange Server-Side Synchronization and Dynamics 365 App for Outlook without brittle UI screen-scraping.

</details>

### Q035 (`T5-Q036`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

An `Escalate Field Audit` command button on `WorkOrder` opens a responsive `Custom Page` side pane passing the current record’s GUID in `recordId`. Complete the Power Fx `LookUp` expression inside the Custom Page: ____.

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))` converts `Param("recordId")` into a Dataverse GUID for `LookUp`. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Correct — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.

</details>

### Q036 (`T5-Q057`) — Create and manage logic and process automation [3.1] · *Single-Answer Multiple Choice*

When an underwriter sets `Surety Bond` status to `Bound`, Dataverse must synchronously abort the save inside the database transaction if `SignedIndemnityOnFile = No`, and once committed must asynchronously post the bound bond PDF to DocuSign and Teams. How should you combine platform tools?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enforce the pre-commit check synchronously via a `Real-time classic workflow` or `Automated Pre-operation low-code plug-in`, and orchestrate DocuSign + Teams asynchronously via an `Automated cloud flow`. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.

</details>

### Q037 (`T5-Q099`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Underwriters generate a standardized `Surety Bond Schedule.docx` Word Template from `Policyholder` listing account details plus a repeating table of active `Surety Bond` child rows (`1:N`). Complete the Word desktop XML mapping step: ____.

- **A.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **B.** `ModelDrivenFormIntegration.Item`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable the `Developer` tab, open `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`), and wrap the bond row in a `Repeating` content control. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **B:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **C:** Correct — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q038 (`T5-Q086`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

When Meridian customizes ONLY one new `SEC_CIKNumber` column and one `Regulatory View` on the standard `Account` table inside `MeridianFilingCore`, how do you prevent accidentally exporting 120 unmodified `Account` forms, views, and columns?

- **A.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Use a custom `Solution Publisher` (`mrf_` prefix) and add `Account` as a `Segmented` table—selecting ONLY `SEC_CIKNumber` and `Regulatory View` with `Include all objects` and `Include table metadata` left unchecked. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q039 (`T5-Q019`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Compliance requires blocking duplicate `PolicyNumber` values inside the database save transaction before commit. Proposed solution: Turn off Alternate Keys and rely exclusively on an asynchronous Automated Power Automate cloud flow (`When a row is added`) to flag duplicates minutes later. Does this block duplicate commits synchronously?

- **A.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No—an Automated cloud flow triggers asynchronously after SQL commit; use an `Alternate Key` or synchronous pre-operation plug-in/workflow to prevent committing duplicates. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **B:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.

</details>

### Q040 (`T5-Q045`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Before inspecting coastal floodgates with intermittent mobile coverage, an adjuster selects `ddDistrict` and caches matching `Valves` / floodgate asset rows into `colOfflineValves`. Complete the delegable Power Fx formula: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))` clears stale data and populates `colOfflineValves` via a delegable `Filter`. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Correct — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.

</details>

### Q041 (`T5-Q071`) — Create and manage logic and process automation [3.6] · *Multi-Select (Select 2)*

You are optimizing high-volume claims cloud flows for Pinnacle Claims Resolution. Which TWO practices reduce API consumption and speed troubleshooting? Select two.

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** The Dataverse connector supports `Change type`, `Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows` / `Unrelate rows`, bound/unbound actions, and reusable solution `Child Flows`
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Restrict triggers/queries with `Select columns`, `Filter rows`, `Expand Query`, and reusable `Child Flows`, and diagnose issues with `Flow Checker`, `Static Result`, and `28-day Run History` (`Resubmit`). [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Setting both `Select columns` and `Filter rows` on Dataverse triggers avoids firing flows when unrelated columns change.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

## Case Study Vignette — Pinnacle Claims Resolution

> [Scenario: Pinnacle Claims Resolution processes high-volume storm claims via Power Automate cloud flows and Dataverse. A daily settlement flow loops through 4,000 claim rows (`Apply to each` concurrency tuned while avoiding shared `Set variable` race bugs), expands parent Policy details in one `List rows` `Expand Query`, and shares an Instant canvas-triggered flow with 200 adjusters without exposing maker credentials.]

### Q042 (`T5-Q049`) — Create apps by using Microsoft Power Apps [2.9] · *Single-Answer Multiple Choice*

Case study — Pinnacle Claims Resolution: Pinnacle shares an Instant Canvas-triggered settlement-estimate cloud flow with 200 field adjusters and must ensure adjusters can execute the flow using a service-account connection WITHOUT editing flow steps or viewing maker credentials. How do you configure flow permissions?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **D.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Add the adjusters’ security group under `Run-only users` and set the connector to `Use this connection (<Service Account>)` instead of granting `Co-owner` rights. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Correct — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **D:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.

</details>

### Q043 (`T5-Q062`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

Case study — Pinnacle Claims Resolution: Pinnacle’s daily settlement flow loops through 4,000 `Claim` rows and suffered corrupted payout numbers when an admin enabled `Apply to each` `Concurrency Control = 30` while a top-level `Set variable` calculated deductibles inside the loop. Proposed solution: Remove the in-loop `Set variable` mutation and calculate each iteration’s deductible inside an immutable `Compose` action while keeping `Concurrency Control = 30`. Does this eliminate the race bug?

- **A.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes—`Compose` outputs are isolated per loop iteration, allowing `Concurrency Control = 30` to run in parallel without shared-variable overwrites. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q044 (`T5-Q068`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

Case study — Pinnacle Claims Resolution: Pinnacle’s daily settlement flow runs Dataverse `List rows` across 4,000 `Claim` rows and must pull `orc_policynumber` and `orc_deductible` from the parent `orc_PrimaryPolicyId` Lookup in the same single query rather than 4,000 `Get a row by ID` calls. Complete `Expand Query`: ____.

- **A.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)` expands parent Policy columns inline in one query. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **B:** Correct — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

### Q045 (`T5-Q002`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

Underwriters want a custom `Broker Phone Briefing` record that rolls up natively inside the unified `Timeline` control on `Policyholder` and `Surety Bond` alongside standard Emails and Appointments. Which table type must you create?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create `Broker Phone Briefing` as a custom `Activity` table so it inherits `Subject`, `Regarding`, `Timeline` display, and shared `Activity` privileges. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.

</details>

### Q046 (`T5-Q047`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Adjusters search a `420,000`-row `Surety Claim` Dataverse table using `Search(SuretyClaims, txtSearch.Text, "orc_claimsummary")` on a `Multiple Lines of Text` column or complex calculated expression and miss rows past row 2,000. Proposed solution: Rewrite the gallery `Items` formula to use delegable `Filter(SuretyClaims, StartsWith('Claim Number', txtSearch.Text) && 'Claim Status' = 'Claim Status'.Open)` on indexed columns. Does this push filtering server-side across all 420,000 rows?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes—`Filter` with `StartsWith` and `=` on standard indexed Dataverse columns is fully delegable, eliminating the 500/2,000 client truncation cap. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Correct — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q047 (`T5-Q061`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

In a `Wire Claim Settlement` cloud flow, if any banking connector step inside `Scope - Execute Wire` fails, is skipped, or times out, `Scope - Alert Treasury` must record an incident row and mark the flow run `Failed`. How do you configure `Scope - Alert Treasury`?

- **A.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Set `Configure run after` on `Scope - Alert Treasury` to `has failed`, `is skipped`, and `has timed out`, create the incident row, and end with `Terminate (Failed)`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **D:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

### Q048 (`T5-Q054`) — Create apps by using Microsoft Power Apps [2.12] · *Ordered Sequence (Multiple Choice)*

External brokers signing into the portal must view and edit `Surety Bond` rows linked to their brokerage `Account` while anonymous visitors see nothing. Order the exact Power Pages security steps.

- **A.** Enable Table Permissions on the Power Pages Basic Form or List → Create a Table Permission scoped to Contact/Account with required privileges → Assign it to a custom Web Role → Associate authenticated Contacts with that Web Role
- **B.** Share the internal Model-Driven App URL publicly → Disable SSL certificates in Set up workspace → Hardcode an API admin token in client JavaScript → Skip Page Access Rules
- **C.** Leave Enable Table Permissions unchecked → Assign Global Delete privilege to the Anonymous Users Web Role → Enable deprecated local password login → Publish to internet
- **D.** Assign Dataverse internal Security Roles directly to anonymous web visitors → Skip Web Roles entirely → Add a Business Rule on Form load → Restart the portal without syncing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Table Permissions on the Basic Form and List, create an `Account`-scoped `Table Permission` with needed privileges, assign it to a `Broker` Web Role, and associate authenticated Broker Contacts with that Web Role. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — Power Pages secures Dataverse Lists/Forms by enabling Table Permissions on the component, defining row-access scope (Global/Contact/Account/Parent/Self), and binding to Web Roles.
- **B:** Incorrect — Exposing admin tokens in browser JavaScript or sharing internal model-driven URLs violates Power Pages security architecture.
- **C:** Incorrect — Granting Global Delete to Anonymous Users exposes every Dataverse row to public deletion, and Microsoft recommends external IdPs (Entra External ID) over local auth.
- **D:** Incorrect — External Power Pages Contacts do not use internal Dataverse Security Roles; portal authorization uses Table Permissions mapped to Web Roles.

</details>

### Q049 (`T5-Q003`) — Configure Microsoft Dataverse [1.1] · *Multi-Select (Select 2)*

You are provisioning a new `Underwriting Referral` table in Dataverse that requires Business Unit row isolation, slide-out Quick Create entry, and routing referrals into underwriting queues. Which TWO settings must be enabled? Select two.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Enabling `Enable attachments (notes and files)`, `Leverage Quick-Create form`, `Can be added to a queue`, and `Track changes` activates Timeline notes, Quick Create, Queues, and delta sync
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Set `Ownership = User or team` at table creation, and enable `Leverage quick-create form if available` plus `Can be added to a queue` in table properties. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Correct — Functional Consultants toggle table-level flags carefully—several flags (such as queues or notes/attachments) cannot be disabled once saved.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q050 (`T5-Q082`) — Create and manage logic and process automation [3.12] · *Single-Answer Multiple Choice*

You build a Dataverse `Business Rule` setting `CollateralAmount` to `Business Required` when `BondCategory = HighRisk`. Why must you set `Scope = Entity` rather than `All Forms` if brokers also import bonds via Dataflows and Power Pages?

- **A.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **D.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting `Scope = Entity` runs the Business Rule server-side inside Dataverse across model-driven forms, Power Pages, Dataflows, Excel imports, and APIs, whereas form scopes run only in model-driven browsers. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **D:** Correct — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.

</details>

### Q051 (`T5-Q064`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

When formatting policy renewal notices in Power Automate, optional `orc_alternatedate` must format as `yyyy-MM-dd` when populated or fall back cleanly to `orc_primarydate` when null. Complete the WDL expression: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')` guards against null date inputs. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **C:** Correct — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q052 (`T5-Q031`) — Create apps by using Microsoft Power Apps [2.1] · *Multi-Select (Select 2)*

You are optimizing Kestrel’s model-driven onboarding workspace for speed and clarity. Which TWO capabilities are natively supported in the modern form designer? Select two.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **E.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Role-based `Main` forms with `Form Order` + `Fallback` tailor layouts per persona, while `Form Component Control` and `Editable Grid` enable inline editing of related Lookup records and subgrids. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **E:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.

</details>

### Q053 (`T5-Q008`) — Configure Microsoft Dataverse [1.3] · *Multi-Select (Select 2)*

You are auditing `1:N` cascading rules across `Policyholder`, `Surety Bond`, and `Bond Endorsement`. Which TWO relationship behaviors work as described? Select two.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). `Parental` cascades Assign, Share, Reparent, and Delete to all child endorsements, whereas `Custom` (`Assign = Cascade Active`, `Delete = Restrict`) scopes individual operations selectively. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q054 (`T5-Q066`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

Which WDL expression converts a Dataverse UTC `CreatedOn` timestamp string by adding `30` days for a regulatory response deadline while guarding null text fields with `coalesce()`?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `addDays(triggerOutputs()?['body/createdon'], 30, 'yyyy-MM-dd')` shifts ISO timestamps cleanly alongside `coalesce()` and `empty()` null checks. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Correct — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.

</details>

### Q055 (`T5-Q044`) — Create apps by using Microsoft Power Apps [2.7] · *Multi-Select (Select 2)*

You are reviewing a catastrophe-claims Canvas app before storm season. Which TWO Canvas architecture patterns follow Microsoft best practices? Select two.

- **A.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Use responsive auto-layout containers + `Component Libraries` for reusable UI, and pass screen-level record state via `Navigate(..., {locPermitId: ...})` or `App.Formulas` rather than sprawling global variables. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Correct — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.

</details>

### Q056 (`T5-Q063`) — Create and manage logic and process automation [3.3] · *Multi-Select (Select 2)*

You are reviewing storm-claim Power Automate cloud flows for Pinnacle Claims Resolution. Which TWO control-flow principles prevent silent skipped errors and race bugs? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Use `Scope` blocks with `Configure run after` (`failed`, `skipped`, `timed out`) + `Terminate`, and never mutate a shared `Set variable` inside a parallelized `Apply to each` loop. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q057 (`T5-Q017`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

A portfolio director exports an `Active High-Net-Worth Households` view as an Excel `Dynamic PivotTable` and emails the `.xlsx` file to a junior analyst in another Business Unit. When the analyst refreshes the workbook in Excel, which rows appear?

- **A.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dynamic PivotTables and Dynamic Worksheets authenticate the viewer against Dataverse and return ONLY rows permitted by that viewer’s own Dataverse Security Role. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.

</details>

### Q058 (`T5-Q067`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

Configure the Dataverse `Modified` trigger parameters so the flow triggers ONLY when `orc_permitstatus` or `orc_district` changes on active rows (`statecode eq 0`) where status equals `100000002`: ____.

- **A.** `ModelDrivenFormIntegration.Item`
- **B.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Populate `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **B:** Correct — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q059 (`T5-Q009`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

An `Annuity Application` can name either an institutional trust (`Account`) or a private individual (`Contact`) as the `Primary Policyholder` in one lookup field, and must compute `NetSurrenderValue` live on read using `Power Fx`. Which two column features fit?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule
- **C.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Use a polymorphic `Customer` column for the `Account`/`Contact` lookup and a `Power Fx Formula` column for live read-time calculation. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.
- **C:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q060 (`T5-Q011`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

Actuarial rating feeds upsert `Surety Bond` rows every hour using natural composite identifiers (`NAICCarrierCode` + `BondNumber`) without storing Dataverse GUIDs. Which Dataverse feature enforces composite uniqueness and supports natural-key upserts?

- **A.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **B.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure an `Alternate Key` spanning `NAICCarrierCode` and `BondNumber` and confirm the background index reaches `Active` status. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Correct — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **B:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **C:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q061 (`T5-Q015`) — Configure Microsoft Dataverse [1.6] · *Multi-Select (Select 3)*

You are documenting Dataverse governance and data-integration architecture for FINRA readiness. Which THREE statements are accurate? Select three.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **E.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **F.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, F` (`CSV: 2,4,6`)

Correct answers: B, D, and F (are correct). Three-tier Auditing writes change logs to `Log` capacity, `Dataflows` and `Azure Synapse Link` (`Fabric Link`) handle scheduled ETL and continuous analytics, and published `Duplicate Detection` rules warn on duplicate saves/imports. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **E:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **F:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.

</details>

### Q062 (`T5-Q018`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Onboarding specialists occasionally create duplicate `Client Contact` rows sharing the exact same `CRD_AdvisorCode` and `TaxpayerID`. Proposed solution: Create a Dataverse `Duplicate Detection Rule` on `Contact` matching exact `CRD_AdvisorCode` and `TaxpayerID`, save it, and select `Publish` (confirming `<= 5` published rules on `Contact`). Does this alert onboarding specialists during interactive saves?

- **A.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **B.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes—publishing the rule activates interactive duplicate warning prompts on create/update and during Data Import Wizard runs. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **B:** Correct — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **C:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.

</details>

### Q063 (`T5-Q088`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

Which native Power Platform capability lets makers initiate governed Dev -> QA -> Production Managed deployments inside Power Apps Maker Portal with pre-deployment approval flows and centralized deployment logs?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **C.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **D.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure `Power Platform pipelines` hosted in a central tools environment with `Managed Environments` enabled on targets. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **C:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **D:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.

</details>

### Q064 (`T5-Q055`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

All licensed producers employed by `Harborline Brokerage LLC` (`Account`) must view and update `Warranty Claim` / `Bond Claim` rows associated with `Harborline Brokerage LLC` on Power Pages. Complete the Table Permission setting: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure a `Table Permission` with `Access Type = Account` linked to the brokerage `Account` lookup relationship. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q065 (`T5-Q038`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

A modern command button `Dispatch Field Appraiser` on `WorkOrders` updates `Dispatch Status` to `Dispatched` on the selected record via Power Fx. Complete the command `OnSelect` formula: ____.

- **A.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})` updates `Self.Selected.Item` directly from the modern command bar. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

### Q066 (`T5-Q030`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

In Kestrel’s model-driven app Sitemap, you group tables under `Client Intake`, `AML Review`, and `Bond Issuance`, and notice compliance interns without `Read` privilege on `SAR Filing` never see the `SAR Filing` subarea link. Why?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Model-driven Sitemap table subareas automatically respect Dataverse Security Role `Read` privileges, hiding links to tables the signed-in user cannot read. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Correct — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.

</details>

## Case Study Vignette — Sterling Surety Insurance

> [Scenario: Sterling Surety Insurance models `Policyholder`, `Broker`, and `Surety Bond` tables in Dataverse. Each Broker can co-place many Surety Bonds and each Bond tracks `Commission Split %` and `Effective Role Date` per Broker link. Reassigning a Policyholder to a new Underwriter must automatically reassign only Active (not Closed) child Claim activities.]

### Q067 (`T5-Q004`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

Case study — Sterling Surety Insurance: Each `Broker` can co-place multiple `Surety Bond` policies, and each placement link must store `Commission Split %` and `Effective Role Date` on its own form and subgrid. How should you design this relationship in Dataverse?

- **A.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **B.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create a manual intersect table (`Bond Broker Placement`) with two `1:N` relationships to `Surety Bond` and `Broker` so custom columns, forms, and views exist on the link record. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **B:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.

</details>

### Q068 (`T5-Q007`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

Case study — Sterling Surety Insurance: When a `Policyholder` record is reassigned to a new regional underwriter, only open (`Active`) child `Claim` records should transfer ownership while settled historical claims preserve their original owner, and deleting a `Policyholder` with claims must be blocked. Complete the relationship configuration: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Set relationship behavior to `Custom` with `Assign = Cascade Active` and `Delete = Restrict`. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q069 (`T5-Q010`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

Case study — Sterling Surety Insurance: Sterling adds an `AggregateBondExposure` Rollup column on `Policyholder` summing `PenalSum` across active child `Surety Bond` rows. What should underwriters expect regarding automatic vs manual recalculation?

- **A.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **B.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Rollup columns recalculate asynchronously via a scheduled system job (12 hours default, configurable down to 1 hour minimum), though underwriters can manually refresh an individual `Policyholder` total on the form. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Correct — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **B:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q070 (`T5-Q043`) — Create apps by using Microsoft Power Apps [2.7] · *Single-Answer Multiple Choice*

Mobile catastrophe-claims adjusters run an inspection Canvas app on folding phones and 12-inch tablets, and 7 insurance apps share one centrally governed `Claim Header & SLA Timer` widget. How should you build the screens and shared widget?

- **A.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Turn off `Scale to fit`, nest `Horizontal` and `Vertical` auto-layout containers, and author `Claim Header & SLA Timer` inside a solution-aware `Component Library`. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q071 (`T5-Q073`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

Chief Risk Officers want an SLA dashboard measuring how long `Surety Bond` applications remain in the `Actuarial Pricing` BPF stage and triggering alerts when `Active Stage Started On` exceeds 48 hours. Which table stores those columns?

- **A.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **B.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The BPF’s automatically generated Dataverse table stores `Active Stage`, `Active Stage Started On`, and `Status` for views, charts, flows, and SLAs. [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **B:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.

</details>

### Q072 (`T5-Q020`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Market-quote feeds insert 200,000 transient `Intraday Price Tick` staging rows daily into Dataverse, and rows older than 7 days must be purged automatically every night at 01:00 without custom code. Which native job should you schedule?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **D.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure a daily recurring `Bulk Record Deletion` system job targeting `Intraday Price Tick` rows older than 7 days. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Correct — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **D:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.

</details>

### Q073 (`T5-Q042`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

Wealth advisors want an interactive `Power BI` `Asset Allocation Drift` report embedded directly on the `Wealth Portfolio` Main form filtered automatically to the currently open portfolio GUID. Is contextual form-level Power BI filtering supported natively?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** An embedded Canvas app on a Main form reads the live host record via `ModelDrivenFormIntegration.Item`, while Power BI dashboards, reports, and tiles embed as system dashboards or contextual form visuals
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes—embedding a Power BI report control on a model-driven Main form supports contextual JSON column filtering bound to the open record’s ID, alongside Power BI system/personal dashboards. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — `ModelDrivenFormIntegration.RefreshForm(false)` refreshes the host model-driven form after an embedded Canvas control commits changes.
- **D:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q074 (`T5-Q080`) — Create and manage logic and process automation [3.11] · *Ordered Sequence (Multiple Choice)*

Sterling’s low-code architects want an `Instant` Custom API (`CalculateSuretyRateTier`) and an `Automated` `Pre-operation` table validator authored in `Power Fx` without C#. Order the exact authoring steps.

- **A.** Turn off Dataverse database in PPAC → Create a classic 2010 workflow first → Convert the workflow into HTML → Upload as a Power Pages web file
- **B.** Write client-only Navigate() and Notify() UI calls inside an Automated Pre-operation plug-in → Skip Solution selection → Bind to an Excel file on OneDrive → Run offline
- **C.** Open Visual Studio 2022 & compile a C# .NET assembly → Register via Plug-in Registration Tool in Production Default Solution → Disable Power Fx → Reboot Dataverse
- **D.** Open the Dataverse Accelerator app → Select Instant (typed parameters) or Automated (table Create/Update/Delete Pre/Post-op) plug-in → Write the Power Fx formula & pick a Solution → Save and test in the Accelerator canvas or app/flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Open the `Dataverse Accelerator` app, select `Instant` or `Automated` (`Pre-operation`/`Post-operation`) plug-in, write the Power Fx expression and pick your Solution, then save and test. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — Low-code plug-ins require a Dataverse database and are stored as Custom APIs / plug-in steps, not Power Pages HTML files.
- **B:** Incorrect — Server-side Dataverse low-code plug-ins execute in the Dataverse event pipeline and cannot invoke client screen functions like Navigate().
- **C:** Incorrect — Low-code plug-ins use Power Fx inside the Dataverse Accelerator app rather than pro-code C# DLL compilation.
- **D:** Correct — Dataverse low-code plug-ins are authored in the Dataverse Accelerator app using Power Fx, saved into a Solution as Instant or Automated server-side plug-ins, and tested inline.

</details>

### Q075 (`T5-Q005`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

Why did a junior consultant hit a platform blocker after creating a native `N:N` relationship between `Investment Portfolio` and `Model Strategy` when asked to add `TargetAllocationPct` and `RebalanceFrequency` to the relationship?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Native `N:N` relationships generate a hidden system intersect table that cannot hold custom columns, custom forms, or workflows. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Correct — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **C:** Incorrect — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.

</details>

### Q076 (`T5-Q052`) — Create apps by using Microsoft Power Apps [2.11] · *Single-Answer Multiple Choice*

A commercial `Surety Bond Application` on Power Pages spans 5 screens (`Principal Info` -> `Project Contract` -> `Condition: PenalSum > 1000000` -> `Audited CPA Financials Upload to SharePoint` -> `Indemnitor E-Sign`). Which Power Pages component orchestrates multi-step conditional branching and SharePoint uploads?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **D.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a Power Pages `Multi-Step Form` with `Load Form` steps, a `Condition` branching step (`orc_penalsum > 1000000`), and a SharePoint document subgrid step. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **D:** Incorrect — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).

</details>

### Q077 (`T5-Q026`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

When a wealth advisor is removed from the `SG-Underwriters-West` security group in Microsoft Entra ID, how does a Dataverse `Microsoft Entra ID Security Group Team` revoke their Dataverse role privileges?

- **A.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse evaluates Entra group claims dynamically—removing the user from the Entra security group revokes privileges inherited from that Entra Group Team without manual Dataverse team administration. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.

</details>

### Q078 (`T5-Q056`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

Private wealth clients signing into an `Individual Beneficiary Portal` on Power Pages must view ONLY `Annuity Statement` rows linked directly to their own personal `Contact` record. Complete the Table Permission setting: ____.

- **A.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure a `Table Permission` with `Access Type = Contact` linked to the client `Contact` lookup relationship. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Correct — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q079 (`T5-Q077`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

Compliance requires preventing any `Wire Disbursement` row from saving if `DualApprovalSigned = No`. Proposed solution: Use only an asynchronous Automated Power Automate cloud flow (`When a row is added`) to inspect the row after save. Does this block saving an unapproved wire disbursement?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—asynchronous cloud flows execute post-commit after the row is already saved; enforce transactional blocking via a Real-time workflow, `Entity` Business Rule, or Pre-operation low-code plug-in. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **D:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q080 (`T5-Q023`) — Configure Microsoft Dataverse [1.10] · *Single-Answer Multiple Choice*

An underwriting assistant can create `Bond Endorsement` rows and read `Surety Bond` rows, yet gets `prvAppendToorc_suretybond` missing when selecting the parent `Surety Bond` Lookup on `Bond Endorsement`. Which privilege change fixes this?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Grant `Append To` on the parent `Surety Bond` table (paired with `Append` on the child `Bond Endorsement` table) in the assistant’s custom Security Role. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.

</details>

### Q081 (`T5-Q094`) — Manage environments [4.5] · *Ordered Sequence (Multiple Choice)*

Meridian is promoting `MeridianFilingCore` from Dev through QA to Production with stage-specific SEC EDGAR URLs, Key Vault secrets, and service-principal Connections. Put the release steps in exact order.

- **A.** Import an unvalidated solution into Production first → Run Solution Checker two weeks later → Create Environment Variables directly inside Production Default Solution → Skip publishing
- **B.** Export the entire Default Solution from Dev as Unmanaged → Import Unmanaged directly into Production → Hardcode Dev URLs inside flow steps → Share personal maker logins
- **C.** Clear Dev Current Values on Environment Variables & run Solution Checker → Publish all customizations & Export as Managed → Import the Managed `.zip` into UAT/Production → Bind target Connection References & Environment Variable values
- **D.** Delete the Managed solution in Production every Friday (removing custom table data!) → Recreate tables manually → Re-import CSV backups → Reassign all Security Roles

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Clear Dev `Current Values` from Environment Variables and run Solution Checker, Publish all customizations and Export as `Managed`, Import into QA/Production, and bind target Connection References and Environment Variable values. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Unpublished changes in Dev are excluded from exported solutions, and Solution Checker should gate packages before Production import.
- **B:** Incorrect — Never export the Default Solution or import Unmanaged solutions into Production; use segmented Managed solutions with Connection References and Environment Variables.
- **C:** Correct — Healthy ALM runs Solution Checker, publishes customizations, exports as Managed, and binds target-stage Connection References and Environment Variables at import.
- **D:** Incorrect — Deleting a Managed solution that defines custom tables permanently deletes those tables and their Production data; use Managed Upgrade (`Stage for upgrade`) instead.

</details>

### Q082 (`T5-Q053`) — Create apps by using Microsoft Power Apps [2.11] · *Multi-Select (Select 3)*

You are conducting a security and UX review for a broker-facing Power Pages portal. Which THREE statements accurately describe Power Pages capabilities? Select three.

- **A.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **E.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **F.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D, E` (`CSV: 1,4,5`)

Correct answers: A, D, and E (are correct). Authenticate external users via `Microsoft Entra External ID` / OIDC (avoiding deprecated local auth), bind `Lists` and `Basic Forms` to `Table Permissions` + `Web Roles`, and use `Multi-Step Forms` + `Power BI Embedded` with RLS for guided journeys and analytics. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **E:** Correct — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **F:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q083 (`T5-Q085`) — Manage environments [4.1] · *Multi-Select (Select 2)*

You are comparing `App Checker`, `Solution Checker`, and `Managed Environments` for Meridian’s audit committee. Which TWO statements are true? Select two.

- **A.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). `App Checker` inspects live Studio formulas, accessibility labels, and delegation warnings in one app, while `Solution Checker` scans full solutions and `Managed Environments` enforce import gates, sharing limits, and pipelines. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q084 (`T5-Q051`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

After an administrator adds custom JavaScript validation and `Basic Form Metadata` rules inside the `Power Pages Management` model-driven app, why must makers select `Sync` inside Power Pages Design Studio?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Selecting `Sync` pulls updated website configuration rows from Dataverse into Design Studio so subsequent Studio edits and previews reflect the Management app changes. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **C:** Correct — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.

</details>

### Q085 (`T5-Q100`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Meridian’s CISO asks whether confidential `SAR Suspicious Activity` PDF attachments should be stored in out-of-the-box `SharePoint Document Management` or in a Dataverse `File` column when row-level `Access Team` and `User` permissions MUST automatically restrict file access. What must you recommend?

- **A.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **B.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Use a Dataverse `File` column (or Timeline `Notes` in Dataverse `File` capacity), because native SharePoint Document Management does NOT replicate Dataverse row/Access Team security to SharePoint folders. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Correct — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **B:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q086 (`T5-Q027`) — Configure Microsoft Dataverse [1.12] · *Ordered Sequence (Multiple Choice)*

Only the `AML Sanctions Screening` team may view unmasked values or edit `ClientPassportNumber` on `Contact`, while relationship managers must see masked values across all forms, views, and exports. Put the setup steps in exact order.

- **A.** Create an Access Team Template first → Turn off Microsoft Entra authentication → Mark the column as Business Required in a Business Rule → Publish without a Column Security Profile
- **B.** Enable column security on the sensitive Dataverse column & save → Create a Column Security Profile in the solution/PPAC → Set Read, Read Unmasked, Update, and Create permissions → Add authorized teams or users to the profile
- **C.** Create a Blocked DLP policy in PPAC → Export table rows to SharePoint → Assign System Administrator to all clerks → Enable Duplicate Detection on the column
- **D.** Delete Organization Read from all Security Roles first → Add users to an empty Business Unit → Hide the column via JavaScript on one Main form → Leave Enable column security unchecked

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable column security on `ClientPassportNumber`, create a `Column Security Profile`, set Read/Read Unmasked/Update/Create permissions, and add the `AML Sanctions Screening` team. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect — Access Team Templates share record-level rows, whereas field-level masking and Read/Update control require Column Security Profiles.
- **B:** Correct — Securing a sensitive column requires enabling column security on the column definition, creating a Column Security Profile, configuring field permissions, and adding users/teams.
- **C:** Incorrect — DLP policies govern connectors rather than Dataverse field-level authorization, and System Administrator bypasses restrictions entirely.
- **D:** Incorrect — Hiding a field on a form does not secure API, Excel export, or view access; Enable column security + a Column Security Profile enforces server-side field security.

</details>

### Q087 (`T5-Q046`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

When an adjuster writes gauge pressure from `txtPsi` onto `Valves`, server-side validation failures must display `"Save failed: " & FirstError.Message` via `Notify(...)` without crashing the Canvas screen. Complete the Power Fx formula: ____.

- **A.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **B.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `ModelDrivenFormIntegration.Item`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))` catches runtime write errors cleanly. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **B:** Correct — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.

</details>

### Q088 (`T5-Q022`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Managing Directors supervise Senior Advisors who supervise Associate Advisors, and Managing Directors need Read/Write access on Senior Advisors’ client rows plus Read-only visibility on Associate Advisors’ rows without opening Business-Unit-wide access. Which security feature fits?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **C.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **D.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable `Manager` `Hierarchy Security` (`Depth = 2+`) alongside `User`-depth Security Roles. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **C:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **D:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.

</details>

### Q089 (`T5-Q014`) — Configure Microsoft Dataverse [1.6] · *Single-Answer Multiple Choice*

FINRA examiners require field-level change logs whenever `BeneficiaryAccountNumber` or `RiskToleranceTier` is modified on `Advisory Account`, stored in immutable audit logs with a 7-year retention rule. What must be configured?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable Environment `Start Auditing` (with a 7-year retention policy in PPAC), Table `Audit changes to its data` on `Advisory Account`, and Column `Enable auditing` on both columns. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.

</details>

## Case Study Vignette — Kestrel Client Onboarding

> [Scenario: Kestrel Client Onboarding uses a model-driven app for commercial underwriters. Senior Compliance Officers require a specialized `AML Deep-Dive` Main form while standard underwriters see only the `Standard Underwriting` Main form (with a fallback form enabled), plus inline editing of related `Beneficial Owner` rows directly inside a parent Main form tab via Form Component Control.]

### Q090 (`T5-Q029`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

Case study — Kestrel Client Onboarding: Senior Compliance Officers require an `AML Deep-Dive` Main form on `Onboarding Case`, standard underwriters use `Standard Underwriting` Main form, and operations auditors with neither role still need to open records cleanly. How should you configure Form Settings?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Assign Security Roles to `AML Deep-Dive` and `Standard Underwriting`, place `AML Deep-Dive` above `Standard Underwriting` in `Form Order`, and enable a general `Fallback` Main form. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q091 (`T5-Q032`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

Case study — Kestrel Client Onboarding: While reviewing an `Onboarding Case` Main form, compliance officers need to edit columns of the primary `Beneficial Owner` Lookup record (`OwnershipPercentage`, `PEPStatus`) inline inside an `Owner Verification` tab without leaving the host form. Which control should you add?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **D.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Bind the `Form Component Control` to the `Beneficial Owner` Lookup column configured with a `Beneficial Owner` Main form. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **D:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.

</details>

### Q092 (`T5-Q033`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

Case study — Kestrel Client Onboarding: Underwriters also need `Parent Holding Company Credit Rating` displayed strictly read-only on `Onboarding Case`, and want the `Assigned Reviewing Officer` Lookup picker filtered dynamically to officers licensed in the case’s `Jurisdiction State`. Which two features accomplish this?

- **A.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Place a `Quick View` form for the read-only parent fields and enable `Filter by related rows` on the `Assigned Reviewing Officer` Lookup control. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Correct — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q093 (`T5-Q060`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

Contrast how a native Dataverse trigger (`When a row is added, modified or deleted`) initiates a cloud flow versus a legacy polling connector trigger.

- **A.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **D.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Dataverse uses push `webhooks` firing immediately when matching pipeline events commit, whereas polling triggers query external endpoints periodically on a timer. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **D:** Correct — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.

</details>

### Q094 (`T5-Q087`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

Production runs `MeridianFilingCore` `5.2.0.0` (Managed), and you create Patch `5.2.1.0` via `Clone a Patch` to fix an urgent validation message. How do you later consolidate `5.2.0.0` and `5.2.1.0` so full development can resume on version `5.3.0.0`?

- **A.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Run `Clone to Solution` on the base Unmanaged solution `5.2.0.0` in Dev to roll all patches into `5.3.0.0`, then import `5.3.0.0` (Managed) into UAT/Production using `Upgrade`. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q095 (`T5-Q096`) — Manage environments [4.5] · *Multi-Select (Select 2)*

Why must enterprise solutions pair `Environment Variables` with `Connection References` during Managed deployments? Select two.

- **A.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **B.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). `Environment Variables` externalize URLs, JSON settings, SharePoint `Data Sources`, and Key Vault `Secrets`, while `Connection References` bind target service-account connections without turning flows off or creating unmanaged layers. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **B:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q096 (`T5-Q041`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

You embed an interactive `Monte Carlo Yield Simulator` Canvas app directly onto a tab of the `Wealth Portfolio` Main form. Which object inside the embedded Canvas app references the open `Wealth Portfolio` Dataverse row? Complete the reference: ____.

- **A.** `ModelDrivenFormIntegration.Item`
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `ModelDrivenFormIntegration.Item` exposes the host Main form record inside the embedded Canvas control. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Correct — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.

</details>

### Q097 (`T5-Q006`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

Sterling Surety wants Dataverse to prevent deleting any `Master Indemnity Agreement` parent row whenever one or more child `Surety Bond` rows still reference that agreement. Which `1:N` relationship behavior enforces this?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure `Referential, Restrict Delete` on the `Master Indemnity Agreement` -> `Surety Bond` relationship. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).

</details>

### Q098 (`T5-Q075`) — Create and manage logic and process automation [3.8] · *Single-Answer Multiple Choice*

When an underwriter advances out of the `Collateral Verification` BPF stage (`Stage Exit`), Dataverse must synchronously stamp `CollateralVerifiedDate` inside the transaction. Which automation binds natively to BPF `Stage Exit`?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A `Real-time (synchronous)` (or `Background`) classic Dataverse workflow binds directly to BPF `Stage Entry` or `Stage Exit` events. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **C:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q099 (`T5-Q091`) — Manage environments [4.3] · *Multi-Select (Select 2)*

You are auditing Meridian’s Production solution architecture. Which TWO rules preserve clean ALM layering? Select two.

- **A.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Author inside `Segmented` Unmanaged solutions in Dev using a custom `Solution Publisher`, and import strictly `Managed` packages into QA/Prod using `Upgrade` while stripping stray `Active` unmanaged layers. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q100 (`T5-Q012`) — Configure Microsoft Dataverse [1.5] · *Ordered Sequence (Multiple Choice)*

Wealth advisors want global Dataverse Search in the top navigation bar to match `BondNumber` and `CUSIPCode` on `Surety Bond` and show `PenalSum` and `ExpirationDate` in search results. Order the exact setup steps.

- **A.** Enable Dataverse Search in PPAC environment Features → Open the table Quick Find View in the solution → Add Find Columns (indexed) and View Columns (returned) → Save and publish all customizations
- **B.** Connect SSMS directly to Dataverse SQL → Create custom clustered T-SQL indexes on base tables → Restart IIS on the Dataverse server → Clear local browser cache
- **C.** Turn on Column-Level Security for every text column → Create a Bulk Record Deletion job → Configure a Business Rule on Form load → Share the Personal View
- **D.** Delete the table Quick Find View first → Disable Dataverse Search in PPAC → Add columns only to a Personal View → Export an Unmanaged solution without publishing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Dataverse Search in PPAC environment Features, open the `Surety Bond` Quick Find View in your solution, add `Find Columns` and `View Columns`, and publish all customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Correct — Dataverse Search requires enabling the environment feature in PPAC and configuring each table’s Quick Find View Find Columns (search index) and View Columns.
- **B:** Incorrect — Dataverse is SaaS-managed; makers cannot create raw T-SQL indexes or restart IIS—search indexing is governed through PPAC and Quick Find Views.
- **C:** Incorrect — Column Security, Bulk Deletion, and Business Rules do not index tables or fields for Dataverse Search.
- **D:** Incorrect — Personal views never control Dataverse Search indexing, and disabling Dataverse Search turns off Relevance Search across the environment.

</details>
