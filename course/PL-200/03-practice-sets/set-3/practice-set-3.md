# Microsoft Exam PL-200: Full-Length Mock Exam 3 — Reviewer Study Key

**Theme:** Municipal & Utility Permitting — Access Team Templates, Canvas Delegation/IfError, WDL Trigger Conditions & Managed Upgrades  
**Credential:** Microsoft Certified: Power Platform Functional Consultant Associate  
**Study guide baseline:** December 26, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)  
**Lifecycle notice:** Exam PL-200 retired on August 31, 2026 and was replaced by Exam AB-410 (Microsoft Certified: Intelligent Applications Builder Associate).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`T3-Q015`) — Configure Microsoft Dataverse [1.6] · *Multi-Select (Select 3)*

You are documenting Dataverse administration settings for the City CIO. Which THREE platform statements are accurate? Select three.

- **A.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries
- **B.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **F.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, D` (`CSV: 1,2,4`)

Correct answers: A, B, and D (are correct). Dataverse Search indexes `Quick Find View` `Find Columns`, three-tier Auditing stores field deltas in `Log` storage, and Dataflows / `Azure Synapse Link` (`Fabric Link`) handle scheduled ETL imports and continuous analytics exports. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.
- **B:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **F:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q002 (`T3-Q013`) — Configure Microsoft Dataverse [1.5] · *Single-Answer Multiple Choice*

Clerks complain that typing a contractor’s license number into global Dataverse Search returns zero `Building Permit` matches even though `ContractorLicenseNo` appears as a column inside the `Building Permit` Quick Find View grid. What was missed?

- **A.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **B.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Adding a column to `View Columns` only displays it in results; you must ALSO add `ContractorLicenseNo` to `Find Columns` on the `Quick Find View` so Dataverse Search indexes and queries it. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Correct — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **B:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.

</details>

### Q003 (`T3-Q091`) — Manage environments [4.3] · *Multi-Select (Select 2)*

You are establishing ALM release standards for five city departments. Which TWO practices prevent layer drift and bloated deployments? Select two.

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **E.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Package changes in `Segmented Solutions` under custom `Solution Publishers`, and keep UAT/Production strictly `Managed`—using `See solution layers` (`Remove Active Customizations`) and `Solution Upgrade` to retire components. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **E:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).

</details>

### Q004 (`T3-Q024`) — Configure Microsoft Dataverse [1.10] · *Multi-Select (Select 2)*

You are auditing custom Security Roles and Team designs for municipal departments. Which TWO practices align with Microsoft Dataverse security recommendations? Select two.

- **A.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **B.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Clone `Basic User` to build least-privilege custom roles (`Direct User + Team privileges` inheritance), and use `Owner Teams` / `Entra ID Group Teams` for role-based access vs `Access Team Templates` for ad-hoc per-row sharing. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **B:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q005 (`T3-Q065`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

Greenway’s `Notify Downtown Police` cloud flow must fire ONLY when `orc_permitstatus` equals `100000002` (Approved) AND `orc_district` equals `'Downtown'`, without logging skipped flow runs. Complete the `Trigger Condition` expression: ____.

- **A.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **D.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))` evaluates at the trigger gate before a run starts. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **B:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Correct — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **D:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.

</details>

### Q006 (`T3-Q059`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

When a maker exports an Unmanaged solution containing 6 cloud flows built BEFORE `Connection References` were adopted (or created outside a Solution and imported manually), flows turn off or demand personal credentials in UAT. How do `Connection References` prevent this?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **C.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **D.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Each flow points to an abstract `Connection Reference` component in the Solution, and UAT/Prod import or pipelines bind that reference once to a target service connection while keeping flows turned on. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **C:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **D:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.

</details>

### Q007 (`T3-Q040`) — Create apps by using Microsoft Power Apps [2.5] · *Multi-Select (Select 2)*

You want a `Bulk Approve Permits` modern command button on the `Main grid` to appear ONLY when a supervisor selects 2 or more rows in the grid. Which TWO statements about Modern Commanding apply? Select two.

- **A.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **B.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Modern Commanding `Visible` rules can evaluate `CountRows(Self.Selected.AllItems) >= 2` in Power Fx inside its managed `Component Library`, and `OnSelect` can combine `Confirm()`, `ForAll()`/`Patch()`, and `Notify()`. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Correct — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **B:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q008 (`T3-Q005`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

When is a native `N:N` Dataverse relationship sufficient—and which action immediately forces refactoring to a manual intersect table?

- **A.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A native `N:N` works for pure tag-like associations, whereas attempting to add custom columns (such as `Split %` or `Effective Date`) onto the hidden system intersect table is unsupported and requires a manual intersect table. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **B:** Correct — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Incorrect — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.

</details>

### Q009 (`T3-Q038`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

On the `WorkOrders` Main grid command bar, a supervisor selects a single work order and presses `Instant Dispatch` to patch `Dispatch Status` to `Dispatched`. Complete the Power Fx `OnSelect` formula: ____.

- **A.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})` patches the selected `WorkOrders` record directly. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.

</details>

### Q010 (`T3-Q093`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

A city compliance rule states no citizen maker in the `Default` environment may connect `Microsoft Dataverse` or `SharePoint` in the same app/flow as `X (Twitter)` or `Personal Gmail`. Where do you enforce this across all apps and flows in that environment?

- **A.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create an environment- or tenant-scoped `Data Loss Prevention (DLP)` policy in PPAC separating `Business` connectors (`Dataverse`, `SharePoint`) from `Non-Business` / `Blocked` connectors. [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **B:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q011 (`T3-Q088`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

Why is exporting or customizing inside the environment `Default Solution` (`Common Data Services Default Solution`) considered a critical anti-pattern on Exam PL-200?

- **A.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **D.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Default Solution` contains every component in the environment using default publishers and cannot be exported as a clean segmented Managed package. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **D:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.

</details>

### Q012 (`T3-Q099`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Permitting clerks generate a `Final Inspection Certificate.docx` Word Template from `Building Permit` containing permit header fields plus a repeating table of child `Inspection Signoff` rows (`1:N`). Complete the Word desktop authoring step: ____.

- **A.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **D.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable the `Developer` tab, open `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`), and wrap the signoff row inside a `Repeating` content control. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Correct — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **D:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.

</details>

### Q013 (`T3-Q071`) — Create and manage logic and process automation [3.6] · *Multi-Select (Select 2)*

You are auditing flow governance across 40 municipal cloud flows. Which TWO operational practices are recommended? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Resolve `Flow Checker` warnings and test error paths via `Static Result` / `28-day Run History`, and share Instant/Canvas flows with field staff via `Run-only users` rather than `Co-owner`. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Correct — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q014 (`T3-Q021`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Environmental engineers belong to the `Stormwater Division` Business Unit (which must own every inspection they create), yet they also review permits owned by the `Harbor District` and `Hillside District` Business Units without gaining access to `Airport Authority`. What should you enable?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable `Modernized Business Units` and assign the engineers a Security Role scoped directly to `Harbor District` and `Hillside District`. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **C:** Correct — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q015 (`T3-Q054`) — Create apps by using Microsoft Power Apps [2.12] · *Ordered Sequence (Multiple Choice)*

Licensed electrical contractors signing in to the City portal must view and edit `Electrical Permit` rows linked to their company while unauthenticated visitors cannot read them. Order the exact Power Pages security configuration steps.

- **A.** Enable Table Permissions on the Power Pages Basic Form or List → Create a Table Permission scoped to Contact/Account with required privileges → Assign it to a custom Web Role → Associate authenticated Contacts with that Web Role
- **B.** Leave Enable Table Permissions unchecked → Assign Global Delete privilege to the Anonymous Users Web Role → Enable deprecated local password login → Publish to internet
- **C.** Share the internal Model-Driven App URL publicly → Disable SSL certificates in Set up workspace → Hardcode an API admin token in client JavaScript → Skip Page Access Rules
- **D.** Assign Dataverse internal Security Roles directly to anonymous web visitors → Skip Web Roles entirely → Add a Business Rule on Form load → Restart the portal without syncing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Table Permissions on the Basic Form/List, create the `Account`-scoped `Table Permission` with Read/Create/Write privileges, assign it to a custom `Web Role`, and link authenticated Contractor Contacts to that Web Role. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — Power Pages secures Dataverse Lists/Forms by enabling Table Permissions on the component, defining row-access scope (Global/Contact/Account/Parent/Self), and binding to Web Roles.
- **B:** Incorrect — Granting Global Delete to Anonymous Users exposes every Dataverse row to public deletion, and Microsoft recommends external IdPs (Entra External ID) over local auth.
- **C:** Incorrect — Exposing admin tokens in browser JavaScript or sharing internal model-driven URLs violates Power Pages security architecture.
- **D:** Incorrect — External Power Pages Contacts do not use internal Dataverse Security Roles; portal authorization uses Table Permissions mapped to Web Roles.

</details>

### Q016 (`T3-Q080`) — Create and manage logic and process automation [3.11] · *Ordered Sequence (Multiple Choice)*

Civic IT wants a governed server-side `Automated` Power Fx rule on `Permit` `Update` (`Pre-operation`) built without Visual Studio C# tooling. Arrange the Dataverse low-code plug-in steps in exact order.

- **A.** Write client-only Navigate() and Notify() UI calls inside an Automated Pre-operation plug-in → Skip Solution selection → Bind to an Excel file on OneDrive → Run offline
- **B.** Turn off Dataverse database in PPAC → Create a classic 2010 workflow first → Convert the workflow into HTML → Upload as a Power Pages web file
- **C.** Open Visual Studio 2022 & compile a C# .NET assembly → Register via Plug-in Registration Tool in Production Default Solution → Disable Power Fx → Reboot Dataverse
- **D.** Open the Dataverse Accelerator app → Select Instant (typed parameters) or Automated (table Create/Update/Delete Pre/Post-op) plug-in → Write the Power Fx formula & pick a Solution → Save and test in the Accelerator canvas or app/flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Open the `Dataverse Accelerator` app, select `Automated` (`Update`, `Pre-operation`), write the Power Fx validation/mutation expression and pick your Solution, then save and test. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — Server-side Dataverse low-code plug-ins execute in the Dataverse event pipeline and cannot invoke client screen functions like Navigate().
- **B:** Incorrect — Low-code plug-ins require a Dataverse database and are stored as Custom APIs / plug-in steps, not Power Pages HTML files.
- **C:** Incorrect — Low-code plug-ins use Power Fx inside the Dataverse Accelerator app rather than pro-code C# DLL compilation.
- **D:** Correct — Dataverse low-code plug-ins are authored in the Dataverse Accelerator app using Power Fx, saved into a Solution as Instant or Automated server-side plug-ins, and tested inline.

</details>

## Case Study Vignette — Greenway Parks & Events

> [Scenario: Greenway Parks & Events automates special-event permits in Power Automate and Dataverse. A cloud flow must fire ONLY when `PermitStatus` changes to Approved on rows in the `Downtown` district, format event dates safely even when `AlternateDate` is null, catch downstream SharePoint failures via `Scope` `Configure run after`, and roll back invalid fee saves synchronously.]

### Q017 (`T3-Q057`) — Create and manage logic and process automation [3.1] · *Single-Answer Multiple Choice*

Case study — Greenway Parks & Events: Greenway must synchronously block saving a `Special Event Permit` whenever `ParkCapacity < ExpectedAttendance` inside the Dataverse transaction, while asynchronously generating a SharePoint event packet and posting to Teams after approval. How should you split these responsibilities?

- **A.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **B.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Use a synchronous `Real-time classic workflow` or `Automated Pre-operation low-code plug-in` to block invalid saves pre-commit, and use an `Automated cloud flow` for the asynchronous SharePoint and Teams integrations. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **B:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q018 (`T3-Q061`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

Case study — Greenway Parks & Events: In Greenway’s `Build Event Packet` cloud flow, if SharePoint folder creation inside `Scope - Provision Packet` fails or times out, the flow must write an alert row to `Integration Log` and stop the run with `Failed` status. How do you configure the Catch scope?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **C.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **D.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Add `Scope - Catch Error` immediately below `Scope - Provision Packet` with `Configure run after` set to `has failed`, `is skipped`, and `has timed out`, log the row, and add `Terminate (Failed)`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **C:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **D:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.

</details>

### Q019 (`T3-Q064`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

Case study — Greenway Parks & Events: Greenway’s permit approval email formats `orc_alternatedate` as `yyyy-MM-dd` when provided by the applicant, or falls back to `orc_primarydate` when `orc_alternatedate` is null. Complete the WDL expression: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **C.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')` prevents null-input runtime crashes in `formatDateTime`. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Correct — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **C:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q020 (`T3-Q096`) — Manage environments [4.5] · *Multi-Select (Select 2)*

You are automating deployments across `Dev`, `Test`, and `Prod` using `Power Platform pipelines`. Which TWO component types allow stage-specific configuration without modifying Managed apps or flows? Select two.

- **A.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, `Secret`) and `Connection References` bind stage-specific endpoints and credentials cleanly during deployment. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q021 (`T3-Q009`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

On `Utility Connection Permit`, you need a `PermitSurcharge` column that calculates `If(MeterSizeInches > 2, BaseFee * 1.25, BaseFee)` instantly on read without waiting for hourly background jobs, plus a `Billed Party` lookup accepting either a business `Account` or resident `Contact`. Which column capabilities fit?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Use a `Power Fx Formula` column for live conditional arithmetic and a polymorphic `Customer` column to reference either `Account` or `Contact`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q022 (`T3-Q067`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

On the Dataverse `When a row is added, modified or deleted` (`Modified`) trigger for `Permit`, configure the native connector parameters so Dataverse fires ONLY when `orc_permitstatus` or `orc_district` changes on active rows (`statecode eq 0`) with status `100000002`: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `ModelDrivenFormIntegration.Item`
- **D.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Set `Select columns` to `orc_permitstatus,orc_district` and `Filter rows` to `orc_permitstatus eq 100000002 and statecode eq 0`. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **D:** Correct — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.

</details>

### Q023 (`T3-Q068`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

A transit-claims cloud flow runs Dataverse `List rows` on `Claim` and wants parent `orc_policynumber` and `orc_deductible` from `orc_PrimaryPolicyId` returned in the same HTTP call. Complete `Expand Query`: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **C.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **D.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)` expands only the two needed parent columns inline. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **C:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **D:** Correct — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.

</details>

### Q024 (`T3-Q012`) — Configure Microsoft Dataverse [1.5] · *Ordered Sequence (Multiple Choice)*

Permit clerks want global Dataverse Search to match `AssessorParcelNumber` and `ContractorLicenseNo` on the `Building Permit` table and display `PermitType` and `IssuedDate` in search cards. Order the exact configuration steps.

- **A.** Enable Dataverse Search in PPAC environment Features → Open the table Quick Find View in the solution → Add Find Columns (indexed) and View Columns (returned) → Save and publish all customizations
- **B.** Delete the table Quick Find View first → Disable Dataverse Search in PPAC → Add columns only to a Personal View → Export an Unmanaged solution without publishing
- **C.** Turn on Column-Level Security for every text column → Create a Bulk Record Deletion job → Configure a Business Rule on Form load → Share the Personal View
- **D.** Connect SSMS directly to Dataverse SQL → Create custom clustered T-SQL indexes on base tables → Restart IIS on the Dataverse server → Clear local browser cache

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Dataverse Search in PPAC environment Features, open the `Building Permit` Quick Find View in your solution, add `Find Columns` and `View Columns`, and publish all customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Correct — Dataverse Search requires enabling the environment feature in PPAC and configuring each table’s Quick Find View Find Columns (search index) and View Columns.
- **B:** Incorrect — Personal views never control Dataverse Search indexing, and disabling Dataverse Search turns off Relevance Search across the environment.
- **C:** Incorrect — Column Security, Bulk Deletion, and Business Rules do not index tables or fields for Dataverse Search.
- **D:** Incorrect — Dataverse is SaaS-managed; makers cannot create raw T-SQL indexes or restart IIS—search indexing is governed through PPAC and Quick Find Views.

</details>

### Q025 (`T3-Q078`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

After migrating 15 high-frequency status-notification rules to classic background workflows, Dataverse `Log`/`Database` storage grows by 2 GB per week due to millions of `Succeeded` rows in `System Jobs`. What is the standard fix?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Edit each background workflow (deactivate -> check `Automatically delete completed workflow jobs (to save disk space)` -> reactivate) and run a one-time `Bulk Record Deletion` job on old completed `System Jobs`. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **C:** Correct — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q026 (`T3-Q092`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

After a failed prototype experiment in a `Dev-Spike` Sandbox environment, you want to wipe the entire Sandbox back to a completely blank factory-fresh Dataverse state (not copying from Production) before starting a new project. Which PPAC operation should you run?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **D.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Use `Reset` on the `Dev-Spike` Sandbox environment in Power Platform Admin Center (taking a Backup first if anything is needed), as `Reset` is supported only on Sandbox environments. [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **D:** Incorrect — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.

</details>

### Q027 (`T3-Q066`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

Inside a Power Automate condition, you want to verify whether a string variable `varInspectorComments` is blank or null before appending text. Which WDL function tests directly for null or empty strings/arrays?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`
- **D.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Using `empty(variables('varInspectorComments'))` returns `true` whenever a string, array, or object is null or empty. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.
- **D:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.

</details>

### Q028 (`T3-Q097`) — Manage environments [4.6] · *Ordered Sequence (Multiple Choice)*

Public-records requests emailed to `FOIA@rivergatecity.example` in Exchange Online must route automatically into a Dataverse `FOIA Requests` Queue via Server-Side Synchronization. Order the exact configuration steps.

- **A.** Install deprecated Dynamics 365 Email Router on a Windows 7 PC → Skip Approve Email and Test & Enable Mailbox → Expect unapproved mailboxes to sync automatically → Disable Queues
- **B.** Verify Exchange Online Email Server Profile & Server-Side Sync defaults in PPAC → Create a Dataverse Queue with the shared email → Open the Queue Mailbox & select Approve Email → Run Test & Enable Mailbox until status = Success
- **C.** Create a Personal View on the Contact table → Upload a Word Template → Run Bulk Record Deletion on ActivityPointer → Share the Queue via Anonymous Web Role
- **D.** Open Outlook in a browser on a developer laptop → Record mouse coordinates with Power Automate for desktop → Copy email text into Notepad → Import CSV nightly

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Verify the Exchange Online `Email Server Profile` and Server-Side Sync defaults in PPAC, create the Dataverse `Queue` with `FOIA@rivergatecity.example`, `Approve Email` on the Queue Mailbox, and run `Test & Enable Mailbox` until status = `Success`. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — The legacy Email Router is deprecated; Server-Side Synchronization requires mailbox approval (when configured) and Test & Enable Mailbox succeeding.
- **B:** Correct — Routing shared-inbox emails into a Dataverse Queue via Server-Side Sync requires an Email Server Profile, a Queue with email address, Email Approval, and Test & Enable Mailbox.
- **C:** Incorrect — Views, Word Templates, and Bulk Deletion do not configure Exchange Server-Side Synchronization or Queue mailboxes.
- **D:** Incorrect — Dataverse includes native Exchange Server-Side Synchronization and Dynamics 365 App for Outlook without brittle UI screen-scraping.

</details>

### Q029 (`T3-Q060`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

Which trigger mechanism allows the Microsoft Dataverse connector (`When a row is added, modified or deleted`) to start a cloud flow immediately on database commit without polling every 1 to 5 minutes?

- **A.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **B.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **C.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Dataverse registers server-side event `webhooks` directly in the Dataverse event execution pipeline rather than polling on a timer. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **B:** Incorrect — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **C:** Correct — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q030 (`T3-Q011`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

County tax-assessor Dataflows synchronize `Parcel Master` rows nightly using the natural `CountyFIPSCode` + `AssessorParcelNumber` strings instead of Dataverse GUIDs. Which Dataverse feature enables natural-key upserts and enforces uniqueness?

- **A.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create an `Alternate Key` combining `CountyFIPSCode` and `AssessorParcelNumber` on `Parcel Master`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Correct — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q031 (`T3-Q050`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

Residents visiting the City’s Power Pages portal need a public `/open-hearings` page listing upcoming `Zoning Hearing` rows from a Dataverse Public View with keyword search and column sorting enabled, but zero create/edit buttons. What should you configure in Power Pages Design Studio?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Add a `List` component bound to the `Upcoming Zoning Hearings` Dataverse view, enable search, leave Create/Edit row actions off, and assign a `Global` `Read`-only Table Permission to `Anonymous Users` + `Authenticated Users`. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.

</details>

### Q032 (`T3-Q033`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

On the `Building Permit` Main form, examiners want `ZoningDistrictCode` and `FloodplainZone` from the parent `Parcel Master` displayed strictly read-only so no examiner can edit parcel master attributes accidentally. Which form component should you place on the form?

- **A.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **D.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Insert a `Quick View` form bound to the `Parcel Master` Lookup column (whereas `Form Component Control` would render an editable Main form). [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Correct — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **D:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.

</details>

### Q033 (`T3-Q006`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

When a draft `Street Excavation Application` is retired and deleted, its child `Traffic Detour Map` reference rows must remain in Dataverse with their `Excavation Application` Lookup column cleared to null rather than blocking deletion or deleting the maps. Which `1:N` relationship behavior accomplishes this?

- **A.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **D.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configuring `Referential` (`Remove Link` on delete) clears the child Lookup value to null when the parent record is deleted without deleting child rows. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **D:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.

</details>

### Q034 (`T3-Q019`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

A city developer wants Dataverse to reject duplicate `MeterSerialNumber` values instantaneously during high-concurrency API writes. Proposed solution: Rely solely on an asynchronous Power Automate cloud flow (`When a row is added`) to check for duplicates after save. Does this block duplicate commits synchronously?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No—asynchronous cloud flows fire post-commit after duplicates are already written to SQL; use an `Alternate Key` (or synchronous pre-operation logic) for guaranteed database-level uniqueness. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.

</details>

### Q035 (`T3-Q058`) — Create and manage logic and process automation [3.1] · *Multi-Select (Select 2)*

You are modernizing municipal automations inside a Dataverse Solution. Which TWO architecture rules apply to cloud flows vs synchronous Dataverse logic? Select two.

- **A.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks
- **B.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Package cloud flows inside Solutions with `Connection References` for async cross-service work, while keeping synchronous transactional rollbacks in `Real-time classic workflows` or `Low-code plug-ins`. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.
- **B:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q036 (`T3-Q002`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

Before saving a new `Code Enforcement Case` standard table, city inspectors require the top `+` global Quick Create menu to slide open a compact intake drawer and dispatchers require routing cases into neighborhood queues. Which two table properties must you enable?

- **A.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Enabling `Enable attachments (notes and files)`, `Leverage Quick-Create form`, `Can be added to a queue`, and `Track changes` activates Timeline notes, Quick Create, Queues, and delta sync
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable `Leverage quick-create form if available` and `Can be added to a queue` on the `Code Enforcement Case` table definition. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Functional Consultants toggle table-level flags carefully—several flags (such as queues or notes/attachments) cannot be disabled once saved.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q037 (`T3-Q032`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

Permit examiners want to edit child `Inspection Item` status and pass/fail notes directly inside the subgrid rows on the `Building Permit` Main form without opening each child row, while still firing client-side `Business Rules` attached to `Inspection Item`. Which control should you bind to the subgrid?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **C.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **D.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Add the `Editable Grid` control to the `Inspection Item` subgrid—it allows inline row editing while honoring supported Business Rules on the grid columns. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **C:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **D:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.

</details>

### Q038 (`T3-Q098`) — Manage environments [4.6] · *Single-Answer Multiple Choice*

Inspectors working inside a `Private` `Code Enforcement Triage` Queue want to claim sole responsibility for an incoming complaint item so fellow queue members see `Worked By = Maria Gomez` and do not duplicate work. Which native Queue command sets `Worked By`?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **C.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **D.** `ModelDrivenFormIntegration.Item`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Selecting `Pick` on the Queue Item assigns `Worked By` (and optionally moves/keeps it in the queue), while `Release` returns it to the unassigned pool for fellow Private Queue members. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Correct — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **C:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **D:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.

</details>

### Q039 (`T3-Q030`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

In App Designer, you add a Sitemap `Subarea` pointing to a `Custom Page` (`Permit Fee Calculator`) alongside table subareas under `Counter Operations`. Which statement about modern model-driven navigation is true?

- **A.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **B.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A model-driven Sitemap organizes `Areas` -> `Groups` -> `Subareas` linking natively to Dataverse tables, Dashboards, `Custom Pages`, Web Resources, or URLs. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Correct — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **B:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

### Q040 (`T3-Q007`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

When a `Senior Plan Examiner` retires and their parent `Parcel Master` records are reassigned, only open (`Active`) child `Building Permit` rows should transfer to the incoming examiner while closed historical permits keep the original examiner’s name, and deleting a `Parcel Master` with permits must be blocked. Complete the relationship configuration: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure `Custom` relationship behavior with `Assign = Cascade Active` and `Delete = Restrict`. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q041 (`T3-Q051`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

In Power Pages Design Studio, which four primary workspaces organize page authoring, CSS/theme palettes, Dataverse table/view/form modeling, and identity/deployment settings—and how do external Management app edits appear?

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, and clicking `Sync` pulls metadata edits saved in the `Power Pages Management` app. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Correct — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.

</details>

## Case Study Vignette — Summit Transit Claims

> [Scenario: Summit Transit Claims packages customizations under a custom Solution Publisher (`stc_`) in Dev and deploys Managed solutions to Test and Production. A retired `LegacyClaimNotes` column must be deleted cleanly from Production on the next deployment, while SharePoint folder structures organize claim photos automatically under parent Account -> Incident hierarchy.]

### Q042 (`T3-Q086`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

Case study — Summit Transit Claims: Summit packages customizations under its `Summit Transit Publisher` (`stc_` prefix). When adding the standard `Incident` (`Case`) table to add only `stc_BusRouteNumber` and one `Transit Claim` Main form, how should you add `Incident` to the solution?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **D.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Add `Incident` as a `Segmented` table—selecting ONLY `stc_BusRouteNumber` and `Transit Claim` form while leaving `Include all objects` and `Include table metadata` unchecked. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **D:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).

</details>

### Q043 (`T3-Q089`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

Case study — Summit Transit Claims: Summit removed the obsolete `stc_LegacyClaimNotes` column from Unmanaged Dev solution `SummitClaims` and exported Managed version `2.0.0.0`. How must you import `2.0.0.0` into Production so `stc_LegacyClaimNotes` is cleanly deleted while keeping all other `Incident` columns intact?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Import `SummitClaims_2_0_0_0_managed.zip` with `Upgrade (recommended)` (`Stage for upgrade` -> verify in Production -> `Apply upgrade`), which deletes components removed since the previous Managed version. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.

</details>

### Q044 (`T3-Q100`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Case study — Summit Transit Claims: Summit wants damage photos uploaded on `Incident` (`Claim`) rows in Dataverse to automatically organize inside SharePoint Online folders nested beneath the parent claimant `Account` folder (`Account/<AccountName>_<GUID>/Incident/<ClaimTitle>_<GUID>`), and also asks about Word Template child-row limits. Which two platform behaviors apply?

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enabling `Based on entity` (`Account`) folder structure in SharePoint Document Management nests `Incident` folders under `Account` (governed by SharePoint ACLs), and Word Templates export at most `100` related child rows per relationship. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q045 (`T3-Q036`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

A `Dispatch Emergency Crew` command button on `WorkOrder` launches a `Custom Page` dialog passing `recordId`. Complete the Power Fx formula inside the Custom Page to bind to that `WorkOrder` row: ____.

- **A.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **D.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))` converts `Param("recordId")` to a GUID and retrieves the exact Dataverse record. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **D:** Correct — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.

</details>

### Q046 (`T3-Q076`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

Why does `Execute as` (`The owner of the workflow` vs `The user who made changes to the record`) appear as a configurable option ONLY on `Real-time (synchronous)` classic workflows and NOT on `Background (asynchronous)` classic workflows?

- **A.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Background classic workflows always execute asynchronously under the `Workflow Owner` context, whereas Real-time synchronous workflows can execute as either the `Calling User` (enforcing user RBAC/audit identity) or `Workflow Owner`. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q047 (`T3-Q039`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

City safety policy requires a confirmation dialog (`"Dispatch this technician now?"`) before the `Instant Dispatch` modern command updates `WorkOrders`. Complete the Power Fx `OnSelect` formula: ____.

- **A.** `ModelDrivenFormIntegration.Item`
- **B.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **C.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **D.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))` guards the `Patch` behind `Confirm(...)`. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **B:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **C:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **D:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.

</details>

### Q048 (`T3-Q029`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

Your `Civic Permitting` model-driven app includes `Fire Marshal Form`, `Zoning Examiner Form`, and `General Permit Form`. If you restrict `Fire Marshal Form` and `Zoning Examiner Form` to specialist Security Roles and accidentally uncheck `Enable fallback` on `General Permit Form`, what risk arises?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Users whose Security Roles do not match any restricted Main form cannot open records cleanly—at least one Main form must always remain enabled as the `Fallback` form. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q049 (`T3-Q084`) — Manage environments [4.1] · *Single-Answer Multiple Choice*

Your municipal `Managed Environment` blocks importing `SummitPermits_1_4_0_0_managed.zip` into Test because static analysis detected synchronous `XMLHttpRequest` calls inside a form JavaScript web resource (`High` severity). Which engine detected and blocked that anti-pattern?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **C.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Solution Checker` enforcement rule configured on the target `Managed Environment` analyzed the solution package and blocked import on high-severity findings. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **C:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q050 (`T3-Q090`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

During Production deployment of `SummitClaims` `2.0.0.0`, an admin selects `Update` instead of `Upgrade` during Managed import and expects `stc_LegacyClaimNotes` to disappear from Production. Proposed solution: Keep using `Update` and wait 24 hours for background cleanup to remove `stc_LegacyClaimNotes`. Will `Update` ever remove the retired column?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **C.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—Managed `Update` adds and modifies components ONLY and NEVER removes deleted components, regardless of how long you wait; only `Upgrade` removes retired items. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **C:** Incorrect — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q051 (`T3-Q055`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

Every estimator employed by `Apex Electrical Contractors` (`Account`) must view and update `Warranty Claim` / `Permit Application` rows submitted by any colleague under that same `Account`. Complete the Power Pages Table Permission configuration: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure a `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **C:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q052 (`T3-Q081`) — Create and manage logic and process automation [3.11] · *Single-Answer Multiple Choice*

Inside an Automated `Pre-operation` low-code plug-in on `ContractorOrder`, you must block saving an order when `CreditHold` is `true` and `OrderTotal > 0`. Complete the Power Fx formula: ____.

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **D.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))` aborts the transaction cleanly. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Correct — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **D:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.

</details>

### Q053 (`T3-Q052`) — Create apps by using Microsoft Power Apps [2.11] · *Single-Answer Multiple Choice*

Contractors applying for a `Crane Rigging Permit` on Power Pages complete a 4-step wizard (`Applicant Info` -> `Crane Specs` -> `FAA Height Check` -> `Attach Insurance PDFs to SharePoint`) that saves intermediate step progress across browser sessions. Which Power Pages component provides this?

- **A.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **B.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). A Power Pages `Multi-Step Form` (`Web Form`) tracks session/step progress across multiple tabs or tables and supports SharePoint document subgrids. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **B:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q054 (`T3-Q079`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

Five different municipal cloud flows repeat the exact same 12-action `Calculate Tiered Impact Fee & Stamp Ledger` logic. How can you modularize those 12 actions inside your Dataverse Solution without duplicating steps across 5 flows?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **D.** The Dataverse connector supports `Change type`, `Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows` / `Unrelate rows`, bound/unbound actions, and reusable solution `Child Flows`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Extract the 12 actions into a solution-aware Instant `Child Flow` (ending with `Respond to a Power App or flow` / `Response`) and invoke it via `Run a Child Flow` using pre-bound `Run-only users` connections. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **D:** Correct — Setting both `Select columns` and `Filter rows` on Dataverse triggers avoids firing flows when unrelated columns change.

</details>

### Q055 (`T3-Q087`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

What happens to version numbers and solution editability when you run `Clone a Patch` on Unmanaged solution `SummitClaims` `1.2.0.0`, followed two weeks later by `Clone to Solution`?

- **A.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Running `Clone a Patch` creates `1.2.1.0` (incrementing the 3rd `Build` segment and locking `1.2.0.0`), and `Clone to Solution` rolls `1.2.0.0` + all patches into a clean unlocked `1.3.0.0` solution while deleting the old base/patch entries in Dev. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **B:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.

</details>

### Q056 (`T3-Q049`) — Create apps by using Microsoft Power Apps [2.9] · *Single-Answer Multiple Choice*

A Canvas app calls `GenerateWorkOrder.Run(ThisItem.ValveId)` expecting a synchronous `WorkOrderNumber` string back, yet `GenerateWorkOrder` triggers a 25-minute human approval inside Teams before reaching `Respond to a Power App or flow`. What happens in the Canvas app?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Synchronous `Respond to a Power App or flow` calls time out after roughly 120 seconds; long-running human approvals must run asynchronously while writing status updates back to Dataverse. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Correct — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q057 (`T3-Q063`) — Create and manage logic and process automation [3.3] · *Multi-Select (Select 2)*

You are conducting a peer review on complex Power Automate cloud flows for Parks & Events. Which TWO patterns prevent silent failures and parallel data corruption? Select two.

- **A.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Implement `Scope` Try/Catch blocks via `Configure run after` + `Terminate`, and replace in-loop `Set variable` actions with `Compose` before increasing `Apply to each` `Concurrency Control`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Correct — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q058 (`T3-Q085`) — Manage environments [4.1] · *Multi-Select (Select 2)*

You are configuring quality gates for citizen makers and Functional Consultants in `Managed Environments`. Which TWO statements accurately describe `App Checker`, `Solution Checker`, and `Managed Environments`? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **E.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). `App Checker` diagnoses single-app formula/delegation/accessibility issues in Studio while `Solution Checker` audits full solutions, and `Managed Environments` enable pipelines, sharing limits, and import-time Solution Checker gates. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **E:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.

</details>

### Q059 (`T3-Q023`) — Configure Microsoft Dataverse [1.10] · *Single-Answer Multiple Choice*

A Zoning Clerk has `Create` and `Write` privileges on `Variance Request` plus `Read` and `Append To` on `Parcel Master`, yet still receives a privilege error when populating the `Parcel Master` Lookup on `Variance Request`. Which missing privilege on `Variance Request` caused the failure?

- **A.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **B.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The clerk is missing the `Append` privilege on the child table (`Variance Request`)—populating a Lookup always requires `Append` on the child AND `Append To` on the parent. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **B:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q060 (`T3-Q053`) — Create apps by using Microsoft Power Apps [2.11] · *Multi-Select (Select 3)*

You are designing a public-sector citizen permitting portal on Microsoft Power Pages. Which THREE design choices align with official Power Pages architecture? Select three.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **E.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **F.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D, E` (`CSV: 2,4,5`)

Correct answers: B, D, and E (are correct). Use `Lists` and `Basic Forms` (`Insert`/`Edit`/`ReadOnly`) in Design Studio, `Multi-Step Forms` + portal search/Power BI Embedded for complex journeys, and `Table Permissions` + `Web Roles` + `Microsoft Entra External ID` for external security. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Correct — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **E:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **F:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q061 (`T3-Q094`) — Manage environments [4.5] · *Ordered Sequence (Multiple Choice)*

Your municipal ALM team is exporting `GreenwayPermits` from Dev and importing it as Managed into Production where GIS REST endpoints and SharePoint sites differ. Put the ALM steps in exact order.

- **A.** Import an unvalidated solution into Production first → Run Solution Checker two weeks later → Create Environment Variables directly inside Production Default Solution → Skip publishing
- **B.** Delete the Managed solution in Production every Friday (removing custom table data!) → Recreate tables manually → Re-import CSV backups → Reassign all Security Roles
- **C.** Export the entire Default Solution from Dev as Unmanaged → Import Unmanaged directly into Production → Hardcode Dev URLs inside flow steps → Share personal maker logins
- **D.** Clear Dev Current Values on Environment Variables & run Solution Checker → Publish all customizations & Export as Managed → Import the Managed `.zip` into UAT/Production → Bind target Connection References & Environment Variable values

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Clear Dev `Current Values` from Environment Variables and run Solution Checker, Publish all customizations and Export as `Managed`, Import into UAT/Production, and bind target Connection References and Environment Variables. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Unpublished changes in Dev are excluded from exported solutions, and Solution Checker should gate packages before Production import.
- **B:** Incorrect — Deleting a Managed solution that defines custom tables permanently deletes those tables and their Production data; use Managed Upgrade (`Stage for upgrade`) instead.
- **C:** Incorrect — Never export the Default Solution or import Unmanaged solutions into Production; use segmented Managed solutions with Connection References and Environment Variables.
- **D:** Correct — Healthy ALM runs Solution Checker, publishes customizations, exports as Managed, and binds target-stage Connection References and Environment Variables at import.

</details>

### Q062 (`T3-Q041`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

An interactive hydraulic-pressure gauge Canvas app is embedded onto a section of the `Water Pump Station` Main form. Which object inside the embedded Canvas app accesses the open `Water Pump Station` row? Complete the reference: ____.

- **A.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `ModelDrivenFormIntegration.Item`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `ModelDrivenFormIntegration.Item` exposes the bound host Main form record to the embedded Canvas app. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Correct — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.

</details>

### Q063 (`T3-Q095`) — Manage environments [4.5] · *Single-Answer Multiple Choice*

Which `Environment Variable` data type lets Power Automate cloud flows retrieve an encrypted GIS API client secret directly from `Azure Key Vault` at runtime without storing plaintext secrets inside Dataverse tables or flow JSON?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create an Environment Variable of data type `Secret` backed by `Azure Key Vault` (granting the `Dataverse` service principal `Key Vault Secrets User` access on the vault). [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.

</details>

### Q064 (`T3-Q072`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

Your `Commercial Building Permit` Business Process Flow attempts to place an `If/Else` conditional branch after Stage 3 evaluating a column that was ONLY added as a data step back in Stage 1 (not Stage 3), and BPF validation fails. Why?

- **A.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). In a Business Process Flow, an `If/Else` condition can evaluate ONLY columns included as steps inside the immediately preceding stage. [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q065 (`T3-Q042`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

After an embedded Canvas app updates a related child `Calibration Log` row via `Patch()`, how can the embedded Canvas app instruct the host model-driven Main form to refresh its data without losing focus?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** An embedded Canvas app on a Main form reads the live host record via `ModelDrivenFormIntegration.Item`, while Power BI dashboards, reports, and tiles embed as system dashboards or contextual form visuals
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Call `ModelDrivenFormIntegration.RefreshForm(false)` from the embedded Canvas control (while using embedded Power BI dashboards/reports for analytical visuals). [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — `ModelDrivenFormIntegration.RefreshForm(false)` refreshes the host model-driven form after an embedded Canvas control commits changes.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q066 (`T3-Q074`) — Create and manage logic and process automation [3.8] · *Ordered Sequence (Multiple Choice)*

Examiners in the `Final Certificate of Occupancy` BPF stage want a `Run GIS Address Check` button embedded directly as a step inside the BPF stage banner. Put the configuration steps in exact order.

- **A.** Delete the BPF underlying Dataverse table → Record a desktop flow on a local laptop → Disable BPF security roles → Overwrite Active BPF instances manually in SQL
- **B.** Build a personal My Flows cloud flow outside any Solution → Use an Outlook email trigger → Paste the flow URL into a BPF text column → Leave the BPF in Draft state
- **C.** Add 12 stages across 9 unrelated tables in one BPF → Skip Lookup relationships between tables → Trigger an Unattended RPA flow directly without a gateway/machine → Save without validation
- **D.** Create a solution Instant flow using When a flow step is run from a business process flow → Open the BPF designer in the same Solution → Add a Flow Step inside the target Stage & bind the flow → Validate, save, and Activate the BPF

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create a solution Instant flow with `When a flow step is run from a business process flow`, open the BPF in the same Solution, add a Flow Step in the stage, and Validate/Save/Activate the BPF. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Incorrect — Every BPF automatically maintains its own Dataverse table for stage tracking and requires security role enablement rather than SQL manipulation.
- **B:** Incorrect — Non-solution flows and non-BPF triggers cannot be bound as BPF Flow Steps, and Draft BPFs do not render for users.
- **C:** Incorrect — A Business Process Flow supports at most 30 stages and at most 5 related tables connected via 1:N relationships.
- **D:** Correct — To run a cloud flow from a BPF stage button, both the BPF and the flow (using the BPF flow-step trigger) must reside in a Solution before binding and activating.

</details>

## Case Study Vignette — MetroWater Field Operations

> [Scenario: MetroWater Field Operations equips valve-inspection crews with a mobile Canvas app over Dataverse (`350,000` Valve rows). Crews filter valves by District without hitting the 500/2,000 non-delegable row cap, stage offline-ready edits in a local Collection, catch network write errors gracefully with `IfError`, and call a Power Automate flow that returns a work-order number.]

### Q067 (`T3-Q043`) — Create apps by using Microsoft Power Apps [2.7] · *Single-Answer Multiple Choice*

Case study — MetroWater Field Operations: Valve-inspection crews carry both compact Android phones and landscape truck-mounted tablets. How should you structure the `MetroWater Valve Inspector` Canvas screens so controls reflow cleanly across screen widths?

- **A.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Disable `Scale to fit` in app settings and arrange galleries and forms inside nested `Horizontal` and `Vertical` auto-layout containers (`LayoutMinWidth`, `Fill portions`, `Wrap`). [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q068 (`T3-Q045`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Case study — MetroWater Field Operations: Before descending into an underground vault, a technician filters the `350,000`-row `Valves` table by the selected `ddDistrict` dropdown using a delegable `=` operator and caches the district’s valves into `colOfflineValves`. Complete the Power Fx formula: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **C.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))` executes a server-side delegable `Filter` on Dataverse and caches matching rows locally. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Correct — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **C:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q069 (`T3-Q046`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Case study — MetroWater Field Operations: When crews submit updated PSI readings from `txtPsi` on `Valves`, transient cellular drops or server validation errors must surface a clean red `Notify` banner using `FirstError.Message`. Complete the Power Fx formula: ____.

- **A.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `ModelDrivenFormIntegration.Item`
- **D.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))` handles write errors gracefully. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **D:** Correct — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.

</details>

### Q070 (`T3-Q020`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Smart-water SCADA gateways insert 80,000 `Hourly Telemetry` rows weekly into Dataverse, and rows older than 14 days with `AnomalyFlag = No` must be purged every night without consuming Power Automate API quotas. What should you configure?

- **A.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Schedule a recurring nightly `Bulk Record Deletion` system job targeting `Hourly Telemetry` rows older than 14 days where `AnomalyFlag = No`. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **B:** Correct — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.

</details>

### Q071 (`T3-Q034`) — Create apps by using Microsoft Power Apps [2.3] · *Single-Answer Multiple Choice*

When an inspector opens a `Parcel Master` record, selects the `Related` tab, and picks `Building Permits`, which specific Dataverse system view controls the columns and sort order displayed in that full-tab related list?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **D.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The `Building Permit` table’s `Associated View` controls grids opened from a parent record’s `Related` navigation tab. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **D:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.

</details>

### Q072 (`T3-Q035`) — Create apps by using Microsoft Power Apps [2.3] · *Multi-Select (Select 2)*

You are reviewing all five Dataverse view categories (`Public`, `Quick Find`, `Lookup`, `Associated`, `Personal`) before UAT. Which TWO statements are accurate? Select two.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Users create and share `Personal` views via `Manage and share views` without a solution deployment, while `Quick Find`, `Lookup`, and `Associated` system views control search/indexing, lookup dropdowns, and Related-tab lists. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.

</details>

### Q073 (`T3-Q010`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

A finance clerk configures a `TotalUnpaidFines` Rollup column on `Parcel Master` aggregating child `Citation` rows (`Status = Unpaid`) and asks why newly issued citations take up to an hour to appear in view totals unless an inspector refreshes the Rollup icon on the form. Why?

- **A.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **D.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Rollup columns execute asynchronously via a background system job (configurable down to a 1-hour minimum interval) rather than synchronously inside child saves. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **D:** Correct — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.

</details>

### Q074 (`T3-Q003`) — Configure Microsoft Dataverse [1.1] · *Multi-Select (Select 2)*

Your civic architecture board is evaluating Dataverse table types for `Site Inspection` activities, external `GIS Parcel` OData feeds, and `Building Permit` records. Which TWO statements are true? Select two.

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Table Ownership (`User or team` vs `Organization`) and `Activity` status are permanent creation-time choices, while `Activity` tables share Timeline/ActivityPointer security and `Virtual` tables project external data live. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q075 (`T3-Q044`) — Create apps by using Microsoft Power Apps [2.7] · *Multi-Select (Select 2)*

MetroWater maintains 6 field Canvas apps that must share an identical `Offline Sync Status Banner` header and pass `Permit` context cleanly between screens. Which TWO patterns should you apply? Select two.

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **E.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Build the shared banner inside a solution-aware `Component Library` with custom input/output properties, and pass screen context via `Navigate(..., {locPermitId: ...})` or `App.Formulas`. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **E:** Correct — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.

</details>

### Q076 (`T3-Q016`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

A newly annexed township hands you a one-time clean `.csv` spreadsheet of 1,400 `Hydrant Asset` rows with no ongoing sync requirement. What is the fastest native no-code way to map columns and load those 1,400 rows into Dataverse?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **D.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Use the built-in Dataverse `Import data from Excel / CSV` wizard (or download the table’s Data Import Excel template) for a one-time tabular load. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **D:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.

</details>

### Q077 (`T3-Q070`) — Create and manage logic and process automation [3.6] · *Single-Answer Multiple Choice*

Before enabling a `Send Emergency Boil-Water SMS` cloud flow in Production, how do you verify your flow logic without actually texting 90,000 city residents from the SMS connector action?

- **A.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **B.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable `Static Result` on the SMS connector action during testing so Power Automate returns a simulated `200 OK` (or `429 Too Many Requests`) payload without invoking the live SMS gateway. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **B:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q078 (`T3-Q047`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

A junior maker writes `Filter(Valves, "NORTH" in Upper(ValveCode))` against MetroWater’s `350,000`-row Dataverse `Valves` table and notices App Checker displays a blue delegation triangle. Proposed solution: Replace the formula with a delegable `Filter(Valves, StartsWith(ValveCode, "NORTH"))` predicate instead of relying on the client row limit. Does this query all 350,000 rows on the server?

- **A.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **B.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **C.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes—`StartsWith` on a Dataverse text column is fully delegable, pushing the query to Dataverse server-side past the 500/2,000 client row cap. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **B:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **C:** Correct — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q079 (`T3-Q069`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

When a new `Road Closure` row is approved, a cloud flow must link it to existing `Bus Route` rows across a native `N:N` relationship in Dataverse. Complete the connector action: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **C.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **D.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Use the Dataverse `Relate rows` action supplying the `N:N` relationship schema name and target `@odata.id` (`OData Id`). [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **C:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **D:** Correct — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.

</details>

### Q080 (`T3-Q008`) — Configure Microsoft Dataverse [1.3] · *Multi-Select (Select 2)*

You are reviewing `1:N` cascading behaviors for municipal permitting tables. Which TWO statements accurately contrast Dataverse relationship behaviors? Select two.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **E.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). `Parental` cascades Assign/Share/Delete to all children while `Referential, Restrict Delete` blocks parent deletion, and `Custom` (`Assign = Cascade Active`, `Delete = Restrict`) scopes individual rules cleanly. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **E:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.

</details>

### Q081 (`T3-Q077`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

A city ordinance requires blocking any `Demolition Permit` save if `AsbestosClearanceVerified = No`. Proposed solution: Build an Automated Power Automate cloud flow (`When a row is added or modified`) to send a warning email after save. Does this prevent committing an uncleared Demolition Permit?

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No—Automated cloud flows run asynchronously after database commit; block invalid saves synchronously via an `Entity`-scope Business Rule, Real-time workflow, or Pre-operation low-code plug-in. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q082 (`T3-Q022`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

In the Fire Marshal’s office, Battalion Chiefs supervise Captains who supervise Inspectors along a strict rank tree independent of Business Units, and Battalion Chiefs need automatic Read access to inspections two ranks below them. Which security model fits?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure `Hierarchy Security` (`Manager` or `Position` hierarchy with `Depth = 2+`), granting Read/Write/Update/Append on direct reports and Read-only on second-tier indirect reports. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.

</details>

### Q083 (`T3-Q073`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

City Council requests a dashboard chart showing average days permits spend in the `Environmental Review` stage and listing every permit currently active in that stage for more than 15 days. Which table should your view and chart query?

- **A.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **B.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Build the view and chart directly on the custom `Business Process Flow` Dataverse table created automatically when the BPF was saved (`Active Stage`, `Active Stage Started On`). [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **B:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.

</details>

### Q084 (`T3-Q056`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

For homeowner `Homestead Exemption` filings on Power Pages, each signed-in resident must access ONLY filings linked directly to their own personal `Contact` row. Complete the Power Pages Table Permission configuration: ____.

- **A.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a `Table Permission` with `Access Type = Contact` linked to the applicant `Contact` lookup relationship. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Correct — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q085 (`T3-Q001`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

A municipal GIS architect needs a `Zoning Fee Schedule` lookup table accessible uniformly to every city department with zero User, Team, or Business Unit ownership overhead, and confirms row security will never vary by department. Which table ownership setting fits?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Choose `Organization` ownership at table creation for citywide reference tables that never require User, Team, or Business Unit row isolation. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q086 (`T3-Q017`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

The City Treasurer wants an offline point-in-time `.xlsx` snapshot of `Q3 Issued Permits` emailed to an external bond-rating auditor who has NO Microsoft Entra account or Dataverse license in the city tenant. Which export option must you use?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Export as a `Static Worksheet`—unlike Dynamic Worksheets/PivotTables or Excel Online, a Static Worksheet embeds a standalone snapshot readable without Dataverse credentials. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.

</details>

### Q087 (`T3-Q026`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

Unlike an `Access Team`, which two Dataverse team types CAN directly own records in a Business Unit and have Dataverse Security Roles assigned directly to the team?

- **A.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Both `Owner Teams` and `Microsoft Entra ID Group Teams` (Security Group or Microsoft 365 Group teams) can hold Security Roles and own Dataverse records. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q088 (`T3-Q062`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

A municipal billing flow iterates over 1,200 `Water Meter` rows using `Apply to each` and accumulates tiered charges inside a shared `Decimal` variable `varTierTotal` via `Set variable`. Proposed solution: Enable `Concurrency Control = 40` on `Apply to each` without removing `Set variable` inside the loop. Will per-meter bills calculate accurately?

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **C.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`
- **D.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—concurrent loop iterations overwrite the shared `varTierTotal` variable unpredictably; refactor in-loop calculations into immutable `Compose` actions or keep `Concurrency Control` at `1`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **C:** Incorrect — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.
- **D:** Incorrect — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.

</details>

### Q089 (`T3-Q048`) — Create apps by using Microsoft Power Apps [2.9] · *Ordered Sequence (Multiple Choice)*

When a MetroWater crew flags a cracked main in the Canvas app, pressing `Create SAP Emergency Order` must call a solution cloud flow synchronously, return the generated `SAPOrderNumber` into `varOut`, and keep 180 technicians as `Run-only users`. Put the steps in exact order.

- **A.** Build a solution flow with the Power Apps (V2) trigger & typed inputs → End with Respond to a Power App or flow → Add the flow in Canvas Studio Power Automate pane → Call Set(varOut, FlowName.Run(...)) & set Run-only users
- **B.** Create a classic Background Dataverse workflow → Embed an iframe pointing to flow.microsoft.com → Store maker passwords inside a Canvas text label → Poll Run History manually
- **C.** Use a Scheduled Recurrence trigger first → Omit Respond to a Power App or flow → Hardcode FlowName.Run() before adding the flow to the app → Grant Co-owner rights to all 500 end users
- **D.** Remove all triggers from the cloud flow → Export the flow outside any Solution → Bind a Quick View form to the button → Expect synchronous values after 45-minute waits

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a solution flow with `Power Apps (V2)` typed inputs, end with `Respond to a Power App or flow`, add it via the Canvas Studio Power Automate pane, and call `Set(varOut, FlowName.Run(...))` with `Run-only users`. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Correct — Canvas-invoked flows define typed inputs on Power Apps (V2), return outputs via Respond to a Power App or flow, bind in Studio, and capture outputs via FlowName.Run(...).
- **B:** Incorrect — Canvas apps invoke cloud flows natively through the Power Apps (V2) trigger and FlowName.Run() connector bridge, never via iframes or plaintext credentials.
- **C:** Incorrect — Scheduled flows cannot be invoked synchronously via FlowName.Run(), and end users need Run-only user permissions rather than Co-owner edit rights.
- **D:** Incorrect — Every cloud flow requires a trigger, and Respond to a Power App or flow must return within the synchronous HTTP timeout window (~120 seconds).

</details>

## Case Study Vignette — Rivergate Civic Permits

> [Scenario: Rivergate Civic Permits tracks building applications in Dataverse. Ad-hoc project reviewers from Fire, Zoning, and Legal join individual high-profile Permit rows dynamically without creating new Microsoft Entra groups per permit or owning rows themselves, while duplicate parcel submissions matching Street Address + Parcel Code must prompt clerks on save.]

### Q090 (`T3-Q018`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Case study — Rivergate Civic Permits: Counter clerks must receive an interactive warning modal whenever submitting a new `Building Permit` whose `StreetAddress` (first 20 chars) and `ParcelCode` (exact) match an existing open permit. Proposed solution: Create and Publish a `Duplicate Detection Rule` on `Building Permit` for `StreetAddress` + `ParcelCode` and verify Duplicate Detection is enabled in PPAC Data Management settings. Does this meet the goal?

- **A.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes—publishing a Duplicate Detection Rule prompts interactive users with potential duplicates before saving while staying within the 5-published-rule per-table limit. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Correct — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Incorrect — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.

</details>

### Q091 (`T3-Q025`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

Case study — Rivergate Civic Permits: High-profile stadium and waterfront permits pull together a unique mix of 4 to 8 reviewers from Fire, Zoning, Transit, and Legal per individual `Building Permit` row, without owning rows or creating hundreds of Microsoft Entra groups. Which Dataverse team type should you configure?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable `Access Teams` on `Building Permit`, create an `Access Team Template` granting Read/Write/Append, and place an Access Team subgrid on the `Building Permit` Main form. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.

</details>

### Q092 (`T3-Q028`) — Configure Microsoft Dataverse [1.12] · *Single-Answer Multiple Choice*

Case study — Rivergate Civic Permits: Rivergate’s Chief Building Official asks whether hiding `ApplicantBankRoutingNumber` on one Main form via JavaScript protects the column when clerks export a Public View to Excel or query via Power BI. What should you explain?

- **A.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **D.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Form scripts run only inside the browser form—only `Column-Level Security` (`Column Security Profiles`) enforces server-side field masking across Views, Excel exports, Power BI, and OData APIs. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **D:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.

</details>

### Q093 (`T3-Q027`) — Configure Microsoft Dataverse [1.12] · *Ordered Sequence (Multiple Choice)*

City Critical-Infrastructure Homeland Liaisons must view and update `CriticalFacilityGateCode` on `Water Treatment Plant`, while field crews who read `Water Treatment Plant` rows must see `****` masked values everywhere. Order the exact setup steps.

- **A.** Enable column security on the sensitive Dataverse column & save → Create a Column Security Profile in the solution/PPAC → Set Read, Read Unmasked, Update, and Create permissions → Add authorized teams or users to the profile
- **B.** Create a Blocked DLP policy in PPAC → Export table rows to SharePoint → Assign System Administrator to all clerks → Enable Duplicate Detection on the column
- **C.** Create an Access Team Template first → Turn off Microsoft Entra authentication → Mark the column as Business Required in a Business Rule → Publish without a Column Security Profile
- **D.** Delete Organization Read from all Security Roles first → Add users to an empty Business Unit → Hide the column via JavaScript on one Main form → Leave Enable column security unchecked

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable column security on `CriticalFacilityGateCode`, create a `Column Security Profile`, set Read/Read Unmasked/Update/Create permissions, and add the Homeland Liaisons team. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Correct — Securing a sensitive column requires enabling column security on the column definition, creating a Column Security Profile, configuring field permissions, and adding users/teams.
- **B:** Incorrect — DLP policies govern connectors rather than Dataverse field-level authorization, and System Administrator bypasses restrictions entirely.
- **C:** Incorrect — Access Team Templates share record-level rows, whereas field-level masking and Read/Update control require Column Security Profiles.
- **D:** Incorrect — Hiding a field on a form does not secure API, Excel export, or view access; Enable column security + a Column Security Profile enforces server-side field security.

</details>

### Q094 (`T3-Q083`) — Create and manage logic and process automation [3.12] · *Multi-Select (Select 3)*

You are choosing between `Business Rules`, `Low-code plug-ins`, and `Form JavaScript` for permit form and server validations. Which THREE statements are accurate? Select three.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors
- **E.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **F.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D, E` (`CSV: 1,4,5`)

Correct answers: A, D, and E (are correct). `Entity`-scope Business Rules run server-side; Business Rules CANNOT hide whole Tabs/Sections or evaluate `MultiSelect Choice` columns; and `Dataverse Accelerator` low-code plug-ins execute server-side `Power Fx` in Pre/Post-operation stages. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Correct — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Correct — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.
- **E:** Correct — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **F:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q095 (`T3-Q004`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

A city `Public Works Project` involves multiple `Subcontractor Accounts`, and each subcontractor link must record `BondAmount`, `DBE_CertifiedPercentage`, and `InspectorSignOffDate` with its own audit history. How must you model this relationship?

- **A.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **B.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a manual intersect table (`Project Subcontractor`) with two `1:N` relationships to `Public Works Project` and `Account` so custom columns and auditing reside on the link record. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Correct — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **B:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

### Q096 (`T3-Q031`) — Create apps by using Microsoft Power Apps [2.1] · *Multi-Select (Select 2)*

You are designing intuitive single-screen workflows in the modern model-driven form designer for counter clerks. Which TWO capabilities reduce unnecessary tab-switching and navigation? Select two.

- **A.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Role-ordered `Main` forms (with a `Fallback` form) plus `Quick Create` drawers streamline entry, while `Form Component Control` and `Editable Grid` enable inline editing of parent Lookup records and child subgrids. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q097 (`T3-Q075`) — Create and manage logic and process automation [3.8] · *Single-Answer Multiple Choice*

When an examiner advances a permit out of the `Plan Check` BPF stage (`Stage Exit`), Dataverse must synchronously stamp `PlanCheckCompletedBy` and abort stage advancement if open `Correction Notice` rows remain. Which BPF stage automation supports synchronous rollback on `Stage Exit`?

- **A.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Triggering a `Real-time (synchronous)` classic Dataverse workflow on BPF `Stage Exit` executes inside the stage-transition transaction and rolls back advancement if canceled. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.

</details>

### Q098 (`T3-Q014`) — Configure Microsoft Dataverse [1.6] · *Single-Answer Multiple Choice*

State public-records auditors require a 7-year immutable log showing old and new values whenever `ZoningVarianceApproved` changes on `Building Permit`. Which Dataverse configuration satisfies both capture and retention?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **D.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Environment `Start Auditing` (with a 7-year audit retention policy in PPAC), Table `Audit changes to its data` on `Building Permit`, and Column `Enable auditing` on `ZoningVarianceApproved`. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **D:** Incorrect — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.

</details>

### Q099 (`T3-Q082`) — Create and manage logic and process automation [3.12] · *Single-Answer Multiple Choice*

Both your `Counter Kiosk` Canvas app and your `Nightly Billing` cloud flow need the exact same municipal stormwater runoff fee formula (`ImperviousSqFt * ZoneMultiplier - RainGardenCredit`). Which modern low-code Dataverse artifact centralizes this formula once in a Solution?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **C.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create a solution-aware `Power Fx Function` (or `Instant` low-code plug-in) with typed input parameters and invoke it from both the Canvas app and Power Automate. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **C:** Correct — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q100 (`T3-Q037`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

Dispatch supervisors want a side-pane checklist inside their model-driven app that slides open on the right edge (`Navigate(..., {Page: ..., Target: ...})` via client script/commanding) while keeping the `WorkOrder` form visible on the left. Which modern page type supports side panes and centered modals natively?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A model-driven `Custom Page` built with responsive Canvas containers supports full-page, centered modal dialog, and right-hand side-pane targets. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Correct — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>
