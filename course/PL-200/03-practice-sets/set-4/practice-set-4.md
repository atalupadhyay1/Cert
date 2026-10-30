# Microsoft Exam PL-200: Full-Length Mock Exam 4 — Reviewer Study Key

**Theme:** Industrial Manufacturing & Dealer Warranty — Alternate Keys, Hierarchy Security, Cross-Table BPFs & Low-Code Plug-ins  
**Credential:** Microsoft Certified: Power Platform Functional Consultant Associate  
**Study guide baseline:** December 26, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200)  
**Lifecycle notice:** Exam PL-200 retired on August 31, 2026 and was replaced by Exam AB-410 (Microsoft Certified: Intelligent Applications Builder Associate).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`T4-Q086`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

When creating a brand-new `IroncladWarranty` solution, why must you create or select an `Ironclad Publisher` (`icm_` prefix, custom option-value prefix) BEFORE creating any custom tables, columns, or global choices?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A component’s schema prefix (`icm_`) and choice integer prefix are stamped permanently at creation time from the solution’s `Publisher` and cannot be renamed later without recreating components. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).

</details>

### Q002 (`T4-Q050`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

Dealers visiting `GearGrid Dealer Portal` want a `/submit-claim` page to create new `Warranty Claim` rows in Dataverse with CAPTCHA/validation and attachment upload. Which Power Pages component and mode should you add in Design Studio?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **C.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Add a `Basic Form` bound to a Dataverse `Warranty Claim` form with `Mode = Insert` (and `Enable Table Permissions` checked). [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **C:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q003 (`T4-Q075`) — Create and manage logic and process automation [3.8] · *Single-Answer Multiple Choice*

Besides on-demand cloud flow steps, where in a Business Process Flow stage can a Functional Consultant attach a classic Dataverse workflow (`Real-time` or `Background`) to fire automatically without user button presses?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **D.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Attach classic Dataverse workflows to BPF `Stage Entry` or `Stage Exit` triggers (or global `Process Applied` / `Process Status Changes`). [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **D:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.

</details>

### Q004 (`T4-Q076`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

When a dealer clerk saves a `Part Return` row with `RestockingFeeWaived = Yes`, Dataverse must synchronously verify inside the SQL transaction whether the signed-in clerk holds the `Senior Warranty Approver` role context—rolling back the save with a custom message `"Manager approval required to waive restocking fee"` if invalid. How do you configure this without C#?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Configure a `Real-time (synchronous)` classic workflow (`Execute as = The user who made changes to the record`) or Pre-operation low-code plug-in that aborts with `Stop workflow = Canceled` and the custom message. [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q005 (`T4-Q022`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

A specialized `Marine Engine Tiger Team` belongs to the `North America HQ` Business Unit yet must create and edit warranty claims inside `EMEA Marine` and `APAC Marine` Business Units while keeping `North America HQ` as their owning user BU. What should you enable?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable `Modernized Business Units` and assign the Tiger Team members Security Roles scoped directly to `EMEA Marine` and `APAC Marine`. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Correct — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.

</details>

### Q006 (`T4-Q024`) — Configure Microsoft Dataverse [1.10] · *Multi-Select (Select 2)*

You are troubleshooting Security Role privilege errors and manager visibility for Ironclad’s warranty analysts. Which TWO security mechanics are accurate? Select two.

- **A.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **E.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Setting a Lookup requires `Append` on the child + `Append To` on the parent (and `Direct User + Team` inheritance for team roles), while `Manager Hierarchy Security` grants Read/Write on direct reports and Read-only on deeper tiers up to configured depth. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **E:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q007 (`T4-Q093`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

When a `Sandbox` environment is placed in `Administration mode` during or after a Production copy, which users can sign in while connections and endpoints are safely re-pointed?

- **A.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **D.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Only `System Administrators` and `System Customizers` can sign in while `Administration mode` is enabled (and optionally background operations remain disabled). [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **D:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.

</details>

### Q008 (`T4-Q041`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

You embed a visual `Torque Curve Analyzer` Canvas app onto a tab of the `Engine Assembly` Main form. Complete the Power Fx object reference inside the embedded Canvas app that reads the open `Engine Assembly` record: ____.

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** `ModelDrivenFormIntegration.Item`
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `ModelDrivenFormIntegration.Item` provides live access to the host model-driven form’s Dataverse record. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Correct — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q009 (`T4-Q087`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

You deployed `IroncladWarranty` `4.0.0.0` (Managed) to Production and later shipped Patches `4.0.1.0` and `4.0.2.0`. Now Sprint 14 is ready to merge the base solution and both patches into a clean consolidated release `4.1.0.0`. Which command in Dev merges all patches into the new minor version?

- **A.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Select the base Unmanaged solution `IroncladWarranty` (`4.0.0.0`) and run `Clone to Solution` (`4.1.0.0`), which rolls all child patches into `4.1.0.0`. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **D:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q010 (`T4-Q007`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

When a `Dealership Account` transfers to a new `Territory Warranty Manager`, only open (`Active`) child `Field Service Bulletin` rows should reassign to the new manager while closed historical bulletins keep their original owner, and deleting a Dealership with bulletins must be blocked. Complete the relationship configuration: ____.

- **A.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure `Custom` relationship behavior with `Assign = Cascade Active` and `Delete = Restrict`. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.

</details>

### Q011 (`T4-Q028`) — Configure Microsoft Dataverse [1.12] · *Single-Answer Multiple Choice*

When `Position` Hierarchy Security is chosen instead of `Manager` Hierarchy Security in Dataverse, how can a regional Warranty Lead supervise analysts located in a DIFFERENT Business Unit?

- **A.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). A custom `Position` hierarchy links users to job `Positions` across any Business Unit without requiring the HR `Manager` lookup to sit inside the same Business Unit. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **B:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q012 (`T4-Q091`) — Manage environments [4.3] · *Multi-Select (Select 2)*

You are coaching new Functional Consultants on Dataverse solution layering and upgrade semantics. Which TWO statements are true? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **E.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). `Remove Active Customizations` clears unmanaged top layers in UAT/Prod while `Stage for upgrade` -> `Apply upgrade` safely deletes retired components, and `Clone a Patch` -> `Clone to Solution` manages hotfix lifecycles. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **E:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.

</details>

### Q013 (`T4-Q018`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

Dealers occasionally submit the same `Warranty Claim` twice for the same `EquipmentSerialNumber` + `FailureDate` + `FailedPartCode`. Proposed solution: Create and Publish a Dataverse `Duplicate Detection Rule` on `Warranty Claim` matching exact `EquipmentSerialNumber`, `FailureDate`, and `FailedPartCode` (verifying total published rules on `Warranty Claim` `<= 5`). Does this warn analysts on interactive save and data import?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria
- **D.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes—publishing the rule within the 5-published-rule per-table cap triggers duplicate detection warnings on interactive saves and imports. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Correct — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.
- **D:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.

</details>

### Q014 (`T4-Q092`) — Manage environments [4.4] · *Single-Answer Multiple Choice*

Ironclad wants to test a massive data-migration script against an exact replica of Production’s 180 GB of `Warranty Claim` rows inside a `UAT-Full` Sandbox while ensuring background flows/mailboxes start disabled in administrative mode until admins review connections. Which PPAC operation should you run?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Execute a `Full Copy` from Production to `UAT-Full` Sandbox—it copies all business data plus customizations/schema while placing the refreshed Sandbox into administrative mode with background operations initially disabled. [PL-200 Manage environments — Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments | Ref: Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/copy-environment)]

- **A:** Correct — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.

</details>

### Q015 (`T4-Q008`) — Configure Microsoft Dataverse [1.3] · *Multi-Select (Select 2)*

You are auditing `1:N` cascading behaviors between `Dealership Account`, `Warranty Claim`, and `Claim Line Item`. Which TWO relationship behaviors operate as described? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). A `Parental` relationship between `Warranty Claim` and `Claim Line Item` cascades Delete/Assign/Share to all line items, while `Custom` (`Assign = Cascade Active`, `Delete = Restrict`) scopes cascading on `Dealership` -> `Warranty Claim`. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Correct — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.
- **C:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q016 (`T4-Q098`) — Manage environments [4.6] · *Single-Answer Multiple Choice*

Territory sales managers want `Set Regarding` inside Microsoft Outlook so dealer emails link directly to `Dealership Account` or `Warranty Claim` rows in Dataverse, and want to insert reusable Dataverse `Email Templates` right from Outlook. Which native add-in provides this?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **C.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **D.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Deploy `Dynamics 365 App for Outlook` backed by Exchange Online `Server-Side Synchronization` and the `Dynamics 365 App for Outlook User` security role. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Correct — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Incorrect — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **C:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **D:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.

</details>

## Case Study Vignette — Precision Quality Audits

> [Scenario: Precision Quality Audits manages 8D supplier investigations in Dataverse. Quality directors need a four-stage Business Process Flow that branches to `Containment Lab` when `Severity = Critical`, launches an on-demand cloud flow button right inside Stage 3, and tracks how many hours each investigation spent inside each BPF stage on a chart.]

### Q017 (`T4-Q072`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

Case study — Precision Quality Audits: Precision’s four-stage `8D Supplier Investigation` Business Process Flow must dynamically branch after Stage 2 (`Symptom Assessment`) into an extra `Containment Lab` stage whenever `Severity = Critical`, and otherwise skip straight to `Root Cause`. What rule must be met for `Severity` in Stage 2?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **D.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). The `Severity` column evaluated by the `If/Else` condition MUST be present as a data step inside Stage 2 (the immediately preceding stage). [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **D:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.

</details>

### Q018 (`T4-Q073`) — Create and manage logic and process automation [3.7] · *Single-Answer Multiple Choice*

Case study — Precision Quality Audits: Quality directors want a native model-driven bar chart tracking how many hours each open `8D Investigation` has spent in its current BPF stage. Where do you build that chart?

- **A.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts
- **B.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **C.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a Public View and Chart directly on the `8D Supplier Investigation` BPF’s auto-generated Dataverse table using `Active Stage` and `Active Stage Started On`. [PL-200 Create and manage logic and process automation — Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering) | Ref: Create and configure a Business Process Flow in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview)]

- **A:** Correct — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.
- **B:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **C:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q019 (`T4-Q074`) — Create and manage logic and process automation [3.8] · *Ordered Sequence (Multiple Choice)*

Case study — Precision Quality Audits: Inside Stage 3 of the `8D Supplier Investigation` BPF, engineers need an on-demand `Notify Supplier Portal` button rendered as a step inside the BPF stage flyout. Order the exact configuration steps.

- **A.** Add 12 stages across 9 unrelated tables in one BPF → Skip Lookup relationships between tables → Trigger an Unattended RPA flow directly without a gateway/machine → Save without validation
- **B.** Delete the BPF underlying Dataverse table → Record a desktop flow on a local laptop → Disable BPF security roles → Overwrite Active BPF instances manually in SQL
- **C.** Create a solution Instant flow using When a flow step is run from a business process flow → Open the BPF designer in the same Solution → Add a Flow Step inside the target Stage & bind the flow → Validate, save, and Activate the BPF
- **D.** Build a personal My Flows cloud flow outside any Solution → Use an Outlook email trigger → Paste the flow URL into a BPF text column → Leave the BPF in Draft state

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create a solution Instant flow using `When a flow step is run from a business process flow`, open the BPF in the same Solution, add a Flow Step inside Stage 3, and Validate/Save/Activate the BPF. [PL-200 Create and manage logic and process automation — Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table | Ref: Add instant/action flows and classic workflows to BPFs and manage the BPF table (https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow)]

- **A:** Incorrect — A Business Process Flow supports at most 30 stages and at most 5 related tables connected via 1:N relationships.
- **B:** Incorrect — Every BPF automatically maintains its own Dataverse table for stage tracking and requires security role enablement rather than SQL manipulation.
- **C:** Correct — To run a cloud flow from a BPF stage button, both the BPF and the flow (using the BPF flow-step trigger) must reside in a Solution before binding and activating.
- **D:** Incorrect — Non-solution flows and non-BPF triggers cannot be bound as BPF Flow Steps, and Draft BPFs do not render for users.

</details>

### Q020 (`T4-Q067`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

Configure the Dataverse `Modified` trigger so it executes ONLY when `orc_permitstatus` or `orc_district` is modified on active records (`statecode eq 0`) whose status equals `100000002`: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **C.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **D.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Set `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **C:** Incorrect — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **D:** Correct — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.

</details>

### Q021 (`T4-Q044`) — Create apps by using Microsoft Power Apps [2.7] · *Multi-Select (Select 2)*

You are auditing a shop-floor Canvas app connected to a `900,000`-row `Serial Part` Dataverse table. Which TWO design rules ensure responsive UI and complete query results? Select two.

- **A.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Build responsive layouts with `Horizontal`/`Vertical` containers (`Scale to fit = Off`), and use delegable Dataverse functions (`Filter`, `LookUp`, `=`, `StartsWith`) plus `IfError()` error handling. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Correct — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q022 (`T4-Q045`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

Field mechanics select their assigned `District` in `ddDistrict` at the depot each morning to load matching `Valves` rows into a local collection `colOfflineValves`. Complete the Power Fx formula: ____.

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))` clears old entries and loads filtered Dataverse rows into `colOfflineValves`. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Correct — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q023 (`T4-Q036`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

A `Launch RMA Return Wizard` command button on `WorkOrder` opens a `Custom Page` modal dialog passing the open record’s GUID in `recordId`. Complete the Power Fx `LookUp` inside the Custom Page: ____.

- **A.** `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`
- **B.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **C.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **D.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))` converts `Param("recordId")` via `GUID(...)` to retrieve the Dataverse record. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Correct — When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.
- **B:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **C:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **D:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.

</details>

### Q024 (`T4-Q059`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

During UAT import of `IroncladWarranty_Managed.zip`, the deployment pipeline prompts once for a `SAP ERP` Connection Reference and once for a `Microsoft Dataverse` Connection Reference, binding 14 cloud flows automatically without editing any flow. Why does this work?

- **A.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **B.** Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). All 14 solution-aware cloud flows reference shared `Connection Reference` components rather than hardcoded personal maker connections. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **B:** Correct — Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

### Q025 (`T4-Q004`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

Each `Authorized Dealership` (`Account`) carries certifications for multiple `Product Lines`, and each link must store `CertificationTier` (`Gold`/`Silver`), `AuthorizedTechnicianCount`, and `RecertificationDueDate`. How should you configure the data model?

- **A.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows
- **B.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **C.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Create a manual intersect table (`Dealership Product Certification`) with two `1:N` relationships to `Account` and `Product Line` so custom columns, forms, and workflows live on the link table. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.
- **B:** Correct — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **C:** Incorrect — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q026 (`T4-Q043`) — Create apps by using Microsoft Power Apps [2.7] · *Single-Answer Multiple Choice*

Shop-floor inspectors run a `Receiving Quality Check` Canvas app on both handheld barcode scanners and 24-inch bay monitors, and 5 plant apps share a `Safety Lockout Header` control. How should you build the layout and shared header?

- **A.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Disable `Scale to fit`, use nested `Horizontal` and `Vertical` auto-layout containers, and publish `Safety Lockout Header` inside a solution-aware `Component Library`. [PL-200 Create apps by using Microsoft Power Apps — Describe Canvas app structure, responsive containers, galleries, forms, themes, and components | Ref: Build responsive canvas apps with layout containers, galleries, forms, and components (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout)]

- **A:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.

</details>

### Q027 (`T4-Q057`) — Create and manage logic and process automation [3.1] · *Single-Answer Multiple Choice*

When a supplier quality engineer sets `8D Investigation` status to `Closed`, Dataverse must synchronously block the save if `PermanentCorrectiveAction` is blank or if zero `Verification Test` child rows exist, and then asynchronously email the supplier PDF report via Outlook. Which tools should you pair?

- **A.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **B.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **C.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enforce the pre-commit child-row check synchronously via a `Real-time classic workflow` or `Pre-operation low-code plug-in`, and send the Outlook PDF email asynchronously via an `Automated cloud flow`. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **B:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **C:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.

</details>

### Q028 (`T4-Q027`) — Configure Microsoft Dataverse [1.12] · *Ordered Sequence (Multiple Choice)*

Only the `Supplier Cost Accounting` team may view or edit `InternalManufacturingUnitCost` on `Spare Part`, while warranty clerks who read `Spare Part` rows must see masked values everywhere. Order the exact configuration steps.

- **A.** Create an Access Team Template first → Turn off Microsoft Entra authentication → Mark the column as Business Required in a Business Rule → Publish without a Column Security Profile
- **B.** Enable column security on the sensitive Dataverse column & save → Create a Column Security Profile in the solution/PPAC → Set Read, Read Unmasked, Update, and Create permissions → Add authorized teams or users to the profile
- **C.** Delete Organization Read from all Security Roles first → Add users to an empty Business Unit → Hide the column via JavaScript on one Main form → Leave Enable column security unchecked
- **D.** Create a Blocked DLP policy in PPAC → Export table rows to SharePoint → Assign System Administrator to all clerks → Enable Duplicate Detection on the column

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable column security on `InternalManufacturingUnitCost`, create a `Column Security Profile`, grant Read/Read Unmasked/Update/Create permissions, and add the `Supplier Cost Accounting` team. [PL-200 Configure Microsoft Dataverse — Configure Column Security Profiles and Hierarchy Security (Manager vs Position) | Ref: Column-level security to control access and Hierarchy security (Manager vs Position) (https://learn.microsoft.com/en-us/power-platform/admin/field-level-security)]

- **A:** Incorrect — Access Team Templates share record-level rows, whereas field-level masking and Read/Update control require Column Security Profiles.
- **B:** Correct — Securing a sensitive column requires enabling column security on the column definition, creating a Column Security Profile, configuring field permissions, and adding users/teams.
- **C:** Incorrect — Hiding a field on a form does not secure API, Excel export, or view access; Enable column security + a Column Security Profile enforces server-side field security.
- **D:** Incorrect — DLP policies govern connectors rather than Dataverse field-level authorization, and System Administrator bypasses restrictions entirely.

</details>

### Q029 (`T4-Q003`) — Configure Microsoft Dataverse [1.1] · *Multi-Select (Select 2)*

An industrial equipment manufacturer is comparing Dataverse `Standard`, `Activity`, and `Virtual` table properties. Which TWO statements are accurate? Select two.

- **A.** Enabling `Enable attachments (notes and files)`, `Leverage Quick-Create form`, `Can be added to a queue`, and `Track changes` activates Timeline notes, Quick Create, Queues, and delta sync
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **E.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). `Enable attachments`, `Leverage Quick-Create`, `Queues`, and `Track changes` activate Timeline files, slide-out Quick Create, Queue routing, and delta sync, while `Virtual` tables project external rows live without local storage. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Correct — Functional Consultants toggle table-level flags carefully—several flags (such as queues or notes/attachments) cannot be disabled once saved.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **E:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q030 (`T4-Q083`) — Create and manage logic and process automation [3.12] · *Multi-Select (Select 3)*

You are designing Titan’s low-code business-logic reference architecture. Which THREE capabilities are supported natively? Select three.

- **A.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **E.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps
- **F.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E, F` (`CSV: 1,5,6`)

Correct answers: A, E, and F (are correct). `Entity`-scope Business Rules enforce simple field validations/defaults server-side, `Power Fx Functions` provide reusable server formulas across apps/flows, and `Dataverse Accelerator` low-code plug-ins run `Instant` or `Automated` Power Fx server-side. [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Correct — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **E:** Correct — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.
- **F:** Correct — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.

</details>

### Q031 (`T4-Q063`) — Create and manage logic and process automation [3.3] · *Multi-Select (Select 2)*

You are troubleshooting intermittent calculation bugs and unhandled timeouts in dealer cloud flows. Which TWO Power Automate mechanics must makers understand? Select two.

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **E.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Uncaught action failures skip downstream steps unless caught by a `Scope` with `Configure run after` (`failed`/`skipped`/`timed out`), and `Set variable` inside concurrent `Apply to each` loops causes race overwrites. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **E:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q032 (`T4-Q047`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

A Canvas developer sets `App.OnStart` to run 14 sequential `Set()` lookups blocking app startup for 9 seconds. Proposed solution: Move read-only reference lookups and current-user profile expressions into declarative `App.Formulas` (`Named Formulas`) so Power Apps evaluates them lazily on demand, and use `UpdateContext` for screen-only toggles. Does this improve startup performance and maintainability?

- **A.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **B.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **C.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **D.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes—`App.Formulas` (`Named Formulas`) evaluate only when referenced without blocking `OnStart`, and `UpdateContext` isolates single-screen state cleanly. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **B:** Correct — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **C:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **D:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q033 (`T4-Q033`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

On `Claim Line Item`, selecting `Failed Component` in Lookup B must list ONLY components belonging to the `Machine Model` already chosen in Lookup A on the same form, while displaying `Engine Horsepower` from `Machine Model` read-only. Which two native features handle this?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **C.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **D.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Configure `Filter by related rows` on Lookup B and embed a `Quick View` form on Lookup A. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **C:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **D:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.

</details>

### Q034 (`T4-Q005`) — Configure Microsoft Dataverse [1.2] · *Single-Answer Multiple Choice*

A maker connects `Machine Model` and `Compatible Attachment` with a native `N:N` relationship and then asks how to place a custom `HydraulicAdapterCode` column directly onto the `N:N` intersect record. What must you tell the maker?

- **A.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Adding custom columns onto a native `N:N` hidden system intersect table is unsupported; replace it with a manual intersect table linked via two `1:N` lookups. [PL-200 Configure Microsoft Dataverse — Determine and implement 1:N and N:N (native vs manual intersect) relationships | Ref: Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships)]

- **A:** Incorrect — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **B:** Correct — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.
- **D:** Incorrect — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.

</details>

### Q035 (`T4-Q058`) — Create and manage logic and process automation [3.1] · *Multi-Select (Select 2)*

You are advising Ironclad’s COE on choosing between `Scheduled cloud flows`, `Instant cloud flows`, `Business Process Flows`, and `Real-time workflows`. Which TWO pairings match the right tool to the requirement? Select two.

- **A.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **D.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority
- **E.** `Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Use `Business Process Flows` for guided multi-stage UI chevron workflows (`<= 30` stages, `<= 5` tables) and `Scheduled`/`Instant` cloud flows for recurring batch jobs or button-triggered cross-service automations. [PL-200 Create and manage logic and process automation — Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case | Ref: Compare cloud flows, Business Process Flows, and classic Dataverse workflows (https://learn.microsoft.com/en-us/power-automate/flow-types)]

- **A:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **D:** Correct — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.
- **E:** Correct — Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.

</details>

### Q036 (`T4-Q051`) — Create apps by using Microsoft Power Apps [2.10] · *Single-Answer Multiple Choice*

Where in Power Pages Design Studio do you configure custom brand color palettes, Google/custom typography, and H1/button CSS styles without hand-editing raw Bootstrap files—and how do Management app edits sync?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **C.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **D.** Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Use the `Styling` workspace in Design Studio for themes/CSS palettes, and select `Sync` whenever portal metadata is edited in `Power Pages Management`. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces | Ref: Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages (https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **C:** Correct — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **D:** Incorrect — When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.

</details>

### Q037 (`T4-Q100`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

An external auditor asks what happens to `Warranty Claim` inspection PDFs uploaded via out-of-the-box `SharePoint Document Management` when a user has SharePoint Site Member access to the document library even though their Dataverse Security Role restricts `Warranty Claim` Read to their own Business Unit. Which warning must you highlight?

- **A.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **D.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Native SharePoint Document Management does NOT synchronize Dataverse row/BU permissions to SharePoint—anyone with SharePoint library Read access can open the files in SharePoint unless custom permission management or Dataverse `File` columns are used. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **B:** Correct — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **D:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.

</details>

### Q038 (`T4-Q079`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

A background classic workflow enters `Waiting` status on 50,000 rows using a `Timeout until 90 days after ShipDate` step, and Titan’s admin asks what happens if they deactivate and edit that workflow template tomorrow. How do already-waiting instances behave?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **C.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Already-running (`Waiting`) classic workflow instances continue executing using the workflow definition snapshot active when they started; edits apply only to newly triggered instances. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **C:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **D:** Correct — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q039 (`T4-Q090`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

In Production, a contractor opened `Default Solution` and tweaked a `Warranty Claim` form label, creating an `Unmanaged (Active)` layer above your Managed solution. Proposed solution: Re-import the exact same Managed solution selecting `Update` without removing `Active` customizations on that form, expecting Managed `Update` to overwrite the top `Active` unmanaged layer. Will Managed `Update` override an `Active` unmanaged layer?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **C.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **D.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—an `Unmanaged (Active)` layer ALWAYS sits above `Managed` layers (`Update` or `Upgrade` only updates the Managed layer underneath); you must run `See solution layers` -> `Remove Active Customizations` on that form. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Correct — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **C:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **D:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.

</details>

### Q040 (`T4-Q016`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

Every 4 hours, Ironclad extracts dirty supplier defect spreadsheets from SharePoint folders, unpivots columns and trims part numbers using `Power Query`, and loads normalized rows into Dataverse `Supplier Defect`. Which native tool handles scheduled `Power Query` ETL into Dataverse?

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC
- **C.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **D.** Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Build a scheduled `Power Platform Dataflow` mapping transformed `Power Query` tables into Dataverse. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.
- **C:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **D:** Correct — Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.

</details>

### Q041 (`T4-Q038`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

On the `WorkOrders` Main form modern command bar, pressing `Dispatch Technician` must immediately set `Dispatch Status` to `Dispatched` on the current record. Complete the Power Fx `OnSelect` formula: ____.

- **A.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **B.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})` updates `Self.Selected.Item` directly. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **B:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **C:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

## Case Study Vignette — Titan Spare Parts Supply

> [Scenario: Titan Spare Parts Supply runs classic background Dataverse workflows alongside modern cloud flows and Dataverse low-code Power Fx plug-ins. Disk log storage spiked because millions of succeeded classic workflow `ProcessSession` logs were never purged, and makers want reusable server-side Power Fx validation invoked both on table `Update` and on demand from Canvas apps.]

### Q042 (`T4-Q078`) — Create and manage logic and process automation [3.10] · *Single-Answer Multiple Choice*

Case study — Titan Spare Parts Supply: Titan’s Dataverse `Log`/`Database` capacity spiked because 12 million succeeded classic background workflow `ProcessSession` (`System Jobs`) rows accumulated over 18 months. Which configuration prevents new succeeded runs from accumulating while keeping failed job logs for diagnostics?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Deactivate each background workflow, enable `Automatically delete completed workflow jobs (to save disk space)`, reactivate, and schedule a `Bulk Record Deletion` job for historical succeeded `System Jobs`. [PL-200 Create and manage logic and process automation — Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention | Ref: Monitor and manage background and real-time classic workflow processes and logs (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Correct — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.

</details>

### Q043 (`T4-Q080`) — Create and manage logic and process automation [3.11] · *Ordered Sequence (Multiple Choice)*

Case study — Titan Spare Parts Supply: Titan wants makers to author reusable server-side Power Fx validation rules (`Automated` on table `Update` AND `Instant` callable from Canvas apps) without writing C# plug-in assemblies. Put the authoring steps in exact order.

- **A.** Open Visual Studio 2022 & compile a C# .NET assembly → Register via Plug-in Registration Tool in Production Default Solution → Disable Power Fx → Reboot Dataverse
- **B.** Open the Dataverse Accelerator app → Select Instant (typed parameters) or Automated (table Create/Update/Delete Pre/Post-op) plug-in → Write the Power Fx formula & pick a Solution → Save and test in the Accelerator canvas or app/flow
- **C.** Write client-only Navigate() and Notify() UI calls inside an Automated Pre-operation plug-in → Skip Solution selection → Bind to an Excel file on OneDrive → Run offline
- **D.** Turn off Dataverse database in PPAC → Create a classic 2010 workflow first → Convert the workflow into HTML → Upload as a Power Pages web file

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Open the `Dataverse Accelerator` app, choose `Instant` or `Automated` (`Pre-operation`/`Post-operation`) plug-in, write the Power Fx expression and select a custom Solution, then save and test. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — Low-code plug-ins use Power Fx inside the Dataverse Accelerator app rather than pro-code C# DLL compilation.
- **B:** Correct — Dataverse low-code plug-ins are authored in the Dataverse Accelerator app using Power Fx, saved into a Solution as Instant or Automated server-side plug-ins, and tested inline.
- **C:** Incorrect — Server-side Dataverse low-code plug-ins execute in the Dataverse event pipeline and cannot invoke client screen functions like Navigate().
- **D:** Incorrect — Low-code plug-ins require a Dataverse database and are stored as Custom APIs / plug-in steps, not Power Pages HTML files.

</details>

### Q044 (`T4-Q081`) — Create and manage logic and process automation [3.11] · *Single-Answer Multiple Choice*

Case study — Titan Spare Parts Supply: In Titan’s Automated `Pre-operation` low-code Power Fx plug-in on `DealerPartOrder`, orders must abort synchronously with a clear message whenever `CreditHold = true` and `OrderTotal > 0`. Complete the Power Fx formula: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))` aborts the transaction server-side. [PL-200 Create and manage logic and process automation — Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator) | Ref: Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **C:** Correct — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.

</details>

### Q045 (`T4-Q037`) — Create apps by using Microsoft Power Apps [2.4] · *Single-Answer Multiple Choice*

When adding a new `Custom Page` to a model-driven app that must query both Dataverse `Warranty Claim` rows and an external `FedEx RMA Label` connector on a responsive split screen, why is a `Custom Page` ideal?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Custom Pages run inside the model-driven shell (full page, modal dialog, or side pane), use responsive Canvas containers, and bind connectors alongside Dataverse in a Solution. [PL-200 Create apps by using Microsoft Power Apps — Configure Custom Pages in model-driven apps (responsive containers & Param("recordId")) | Ref: Overview of custom pages for model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Correct — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.

</details>

### Q046 (`T4-Q040`) — Create apps by using Microsoft Power Apps [2.5] · *Multi-Select (Select 2)*

Your team is migrating command buttons on `Warranty Claim` to `Modern Commanding`. Which TWO technical facts apply to Modern Commanding? Select two.

- **A.** `Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Modern Commanding saves Power Fx formulas (`Patch`, `Confirm`, `Notify`, `Self.Selected.Item`) inside a solution `Component Library`, while legacy classic system ribbon buttons remain read-only in modern command designer. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Correct — Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.

</details>

### Q047 (`T4-Q064`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

When generating dealer parts-shipment notices, `orc_alternatedate` should be formatted as `yyyy-MM-dd` when present, falling back to `orc_primarydate` whenever `orc_alternatedate` is null. Complete the WDL expression: ____.

- **A.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **B.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **C.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **D.** `Patch(WorkOrders, Self.Selected.Item, {'Dispatch Status': 'Dispatch Status'.Dispatched})`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')` handles null optional dates cleanly. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **B:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **C:** Correct — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **D:** Incorrect — `Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.

</details>

### Q048 (`T4-Q084`) — Manage environments [4.1] · *Single-Answer Multiple Choice*

Which Power Platform quality tool evaluates an entire Dataverse Solution—scanning plug-ins, custom workflow activities, JavaScript web resources, and Power Automate flows—and categorizes performance, security, and reliability defects by `Critical`, `High`, `Medium`, and `Low` severity?

- **A.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **B.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)
- **C.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Running `Solution Checker` performs multi-component static analysis across the entire Solution (whereas `App Checker` checks formulas/accessibility/delegation in a single open Studio app). [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **B:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.
- **C:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q049 (`T4-Q061`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

In an `Issue Dealer Credit Memo` cloud flow, if calling SAP inside `Scope - Post Credit` fails, is skipped, or times out, `Scope - Rollback & Alert` must mark the Dataverse claim `ERP Sync Failed` and end the flow run as `Failed`. How should `Scope - Rollback & Alert` be configured?

- **A.** `Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure `Configure run after` on `Scope - Rollback & Alert` with `has failed`, `is skipped`, and `has timed out` checked, update the Dataverse row, and append `Terminate (Failed)`. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.
- **B:** Incorrect — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q050 (`T4-Q020`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

IoT vibration gateways write `Spindle Diagnostics` staging rows into Dataverse continuously, and resolved rows older than 60 days must be purged weekly without developer code. Which feature should you schedule?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** `Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state
- **C.** Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create a weekly recurring `Bulk Record Deletion` job targeting `Spindle Diagnostics` rows older than 60 days. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Correct — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Incorrect — Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.
- **C:** Incorrect — Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q051 (`T4-Q006`) — Configure Microsoft Dataverse [1.3] · *Single-Answer Multiple Choice*

Ironclad wants Dataverse to forbid deleting any `Equipment Serial Asset` parent row while historical `Warranty Claim` child rows still reference that serial asset. Which `1:N` relationship behavior enforces this server-side?

- **A.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **B.** `Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors
- **C.** `Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure `Referential, Restrict Delete` on the `Equipment Serial Asset` -> `Warranty Claim` `1:N` relationship. [PL-200 Configure Microsoft Dataverse — Configure table relationship behaviors and cascading rules | Ref: Configure table relationship behavior and cascading rules in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior)]

- **A:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **B:** Incorrect — Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).
- **C:** Correct — Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q052 (`T4-Q034`) — Create apps by using Microsoft Power Apps [2.3] · *Single-Answer Multiple Choice*

Quality analysts want a system `Public View` on `Warranty Claim` that displays `Claim Number`, `Claim Total`, AND the parent `Equipment Serial Asset`’s `ManufacturingPlant` column, sorted first by `ManufacturingPlant` ascending and then by `Claim Total` descending, filtered only to plants in `Ohio`. Can View Designer build this without code?

- **A.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable
- **B.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes—modern View Designer natively adds columns from parent `N:1` Lookup tables, configures multi-column sorting, and filters across related parent table columns. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.
- **B:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q053 (`T4-Q096`) — Manage environments [4.5] · *Multi-Select (Select 2)*

You are configuring end-to-end zero-touch Managed deployments for Ironclad. Which TWO platform features eliminate hardcoded Dev endpoints and manual Production imports? Select two.

- **A.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **E.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, D` (`CSV: 1,4`)

Correct answers: A and D (are correct). Use `Environment Variables` (`Data Source`, `Secret`, `JSON`, `Text`) with cleared Dev `Current Values`, deployed via `Power Platform pipelines` in `Managed Environments`. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **B:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **E:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q054 (`T4-Q012`) — Configure Microsoft Dataverse [1.5] · *Ordered Sequence (Multiple Choice)*

Warranty analysts want global Dataverse Search to match `SerialNumber`, `VIN`, and `EngineBlockCode` on `Equipment Serial Asset` and return `ModelYear` and `DealerName` in search results. Order the exact configuration steps.

- **A.** Delete the table Quick Find View first → Disable Dataverse Search in PPAC → Add columns only to a Personal View → Export an Unmanaged solution without publishing
- **B.** Connect SSMS directly to Dataverse SQL → Create custom clustered T-SQL indexes on base tables → Restart IIS on the Dataverse server → Clear local browser cache
- **C.** Turn on Column-Level Security for every text column → Create a Bulk Record Deletion job → Configure a Business Rule on Form load → Share the Personal View
- **D.** Enable Dataverse Search in PPAC environment Features → Open the table Quick Find View in the solution → Add Find Columns (indexed) and View Columns (returned) → Save and publish all customizations

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable Dataverse Search in PPAC environment Features, open the `Equipment Serial Asset` Quick Find View in your solution, add `Find Columns` and `View Columns`, and publish all customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Incorrect — Personal views never control Dataverse Search indexing, and disabling Dataverse Search turns off Relevance Search across the environment.
- **B:** Incorrect — Dataverse is SaaS-managed; makers cannot create raw T-SQL indexes or restart IIS—search indexing is governed through PPAC and Quick Find Views.
- **C:** Incorrect — Column Security, Bulk Deletion, and Business Rules do not index tables or fields for Dataverse Search.
- **D:** Correct — Dataverse Search requires enabling the environment feature in PPAC and configuring each table’s Quick Find View Find Columns (search index) and View Columns.

</details>

### Q055 (`T4-Q068`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

In a dealer settlement flow, Dataverse `List rows` retrieves `Claim` rows and must include `orc_policynumber` and `orc_deductible` from the parent `orc_PrimaryPolicyId` Lookup in one round-trip. Complete `Expand Query`: ____.

- **A.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **B.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **C.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **D.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)` expands parent Lookup fields inline. [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Correct — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **B:** Incorrect — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **C:** Incorrect — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **D:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.

</details>

### Q056 (`T4-Q042`) — Create apps by using Microsoft Power Apps [2.6] · *Single-Answer Multiple Choice*

Plant executives want a system dashboard inside the `Warranty Operations` model-driven app displaying a live `Power BI` `First-Time Fix Rate` dashboard without switching browser tabs. What must an admin enable first?

- **A.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **B.** An embedded Canvas app on a Main form reads the live host record via `ModelDrivenFormIntegration.Item`, while Power BI dashboards, reports, and tiles embed as system dashboards or contextual form visuals
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Turn on `Enable Power BI quick reports / Power BI visualization embedding` in Power Platform Admin Center environment Features and add a `Power BI Embedded` system dashboard to the solution and app. [PL-200 Create apps by using Microsoft Power Apps — Embed a Canvas app in a model-driven form and add Power BI dashboards and reports | Ref: Embed a canvas app on a model-driven form and add Power BI reports/dashboards (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form)]

- **A:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **B:** Correct — `ModelDrivenFormIntegration.RefreshForm(false)` refreshes the host model-driven form after an embedded Canvas control commits changes.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.

</details>

### Q057 (`T4-Q070`) — Create and manage logic and process automation [3.6] · *Single-Answer Multiple Choice*

Your `Submit Warranty Claim to SAP` cloud flow exhibits a red dot in `Flow Checker` warning that an action’s `Filter rows` parameter is blank on a `500,000`-row table, and you also want to mock SAP’s response during unit testing. Which two built-in Power Automate tools address design-time lint warnings and mock action testing?

- **A.** `Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Use `Flow Checker` to resolve performance/infinite-loop/DLP design warnings and `Static Result` to mock connector outputs during tests. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Correct — Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q058 (`T4-Q054`) — Create apps by using Microsoft Power Apps [2.12] · *Ordered Sequence (Multiple Choice)*

Warranty clerks signing into `GearGrid Dealer Portal` need access to `Warranty Claim` Lists and Basic Forms scoped to their Dealership Account. Order the exact Power Pages security setup steps.

- **A.** Enable Table Permissions on the Power Pages Basic Form or List → Create a Table Permission scoped to Contact/Account with required privileges → Assign it to a custom Web Role → Associate authenticated Contacts with that Web Role
- **B.** Leave Enable Table Permissions unchecked → Assign Global Delete privilege to the Anonymous Users Web Role → Enable deprecated local password login → Publish to internet
- **C.** Assign Dataverse internal Security Roles directly to anonymous web visitors → Skip Web Roles entirely → Add a Business Rule on Form load → Restart the portal without syncing
- **D.** Share the internal Model-Driven App URL publicly → Disable SSL certificates in Set up workspace → Hardcode an API admin token in client JavaScript → Skip Page Access Rules

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enable Table Permissions on the Basic Form and List, create an `Account`-scoped `Table Permission` with Read/Create/Write/Append/Append To, assign it to a `Dealer Clerk` Web Role, and associate authenticated Contacts with that Web Role. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Correct — Power Pages secures Dataverse Lists/Forms by enabling Table Permissions on the component, defining row-access scope (Global/Contact/Account/Parent/Self), and binding to Web Roles.
- **B:** Incorrect — Granting Global Delete to Anonymous Users exposes every Dataverse row to public deletion, and Microsoft recommends external IdPs (Entra External ID) over local auth.
- **C:** Incorrect — External Power Pages Contacts do not use internal Dataverse Security Roles; portal authorization uses Table Permissions mapped to Web Roles.
- **D:** Incorrect — Exposing admin tokens in browser JavaScript or sharing internal model-driven URLs violates Power Pages security architecture.

</details>

### Q059 (`T4-Q032`) — Create apps by using Microsoft Power Apps [2.2] · *Single-Answer Multiple Choice*

Inside the `Warranty Claim` Main form, analysts want to update `DealerServiceManagerEmail` and `LaborRateTier` on the parent `Dealership Account` inline inside a `Dealer Details` tab without navigating away from the claim. Which control should you configure?

- **A.** A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing
- **B.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **C.** `Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Bind the `Form Component Control` to the `Dealership Account` Lookup column pointing to a streamlined `Account` Main form. [PL-200 Create apps by using Microsoft Power Apps — Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids) | Ref: Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control)]

- **A:** Incorrect — Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.
- **B:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **C:** Correct — Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.

</details>

### Q060 (`T4-Q077`) — Create and manage logic and process automation [3.9] · *Single-Answer Multiple Choice*

Engineers must be blocked from changing `Machine Safety Status` to `Released for Shipment` if `HighVoltageTestPassed = No`. Proposed solution: Use an Automated Power Automate cloud flow (`When a row is modified`) to check `HighVoltageTestPassed` and send a Teams message after save. Does this block the shipment release save?

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`
- **C.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`
- **D.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). No—Automated cloud flows execute asynchronously after the database commit has already succeeded; use synchronous server validation (`Entity` Business Rule, Real-time workflow, or Pre-op low-code plug-in). [PL-200 Create and manage logic and process automation — Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows | Ref: Configure real-time (synchronous) and background classic Dataverse workflows (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows)]

- **A:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Incorrect — Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.
- **C:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.
- **D:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.

</details>

### Q061 (`T4-Q019`) — Configure Microsoft Dataverse [1.8] · *Single-Answer Multiple Choice*

A manufacturing architect notes that `Duplicate Detection Rules` allow an interactive user to select `Save` anyway on the warning dialog, and wants to strictly forbid duplicate `SerialNumber` values at the database constraint layer. Proposed solution: Keep only an asynchronous Automated cloud flow (`When a row is added`) instead of an `Alternate Key`. Does an async cloud flow enforce database-level constraint blocking?

- **A.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **B.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** `Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). No—an asynchronous Automated cloud flow runs post-commit and cannot block duplicate saves at commit time; configure an `Alternate Key` (or synchronous pre-op validation) to enforce strict uniqueness. [PL-200 Configure Microsoft Dataverse — Configure duplicate detection rules and scheduled bulk record deletion jobs | Ref: Detect duplicate data and remove bulk amounts of data with bulk deletion jobs (https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean)]

- **A:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **B:** Correct — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.

</details>

### Q062 (`T4-Q046`) — Create apps by using Microsoft Power Apps [2.8] · *Single-Answer Multiple Choice*

When mechanics save hydraulic test pressure from `txtPsi` onto `Valves`, any Dataverse validation or low-code plug-in error must surface cleanly via `Notify(...)`. Complete the Power Fx formula: ____.

- **A.** `ModelDrivenFormIntegration.Item`
- **B.** `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`
- **C.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))` traps write errors cleanly. [PL-200 Create apps by using Microsoft Power Apps — Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling | Ref: Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)]

- **A:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **B:** Correct — `IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.
- **C:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **D:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q063 (`T4-Q049`) — Create apps by using Microsoft Power Apps [2.9] · *Single-Answer Multiple Choice*

If a maker mistakenly adds 400 shop-floor mechanics as `Co-owners` instead of `Run-only users` on a `Power Apps (V2)` cloud flow, what unintended capabilities do those mechanics gain?

- **A.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **B.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **C.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Co-owners can edit or delete the cloud flow, view all 28-day Run History payloads from other users, and manage connections/triggers. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **B:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **C:** Correct — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q064 (`T4-Q097`) — Manage environments [4.6] · *Ordered Sequence (Multiple Choice)*

Dealer claim emails sent to `WarrantyDesk@ironcladmachinery.example` in Exchange Online must route automatically into a Dataverse `Warranty Claims Queue` via Server-Side Synchronization. Order the exact configuration steps.

- **A.** Install deprecated Dynamics 365 Email Router on a Windows 7 PC → Skip Approve Email and Test & Enable Mailbox → Expect unapproved mailboxes to sync automatically → Disable Queues
- **B.** Verify Exchange Online Email Server Profile & Server-Side Sync defaults in PPAC → Create a Dataverse Queue with the shared email → Open the Queue Mailbox & select Approve Email → Run Test & Enable Mailbox until status = Success
- **C.** Create a Personal View on the Contact table → Upload a Word Template → Run Bulk Record Deletion on ActivityPointer → Share the Queue via Anonymous Web Role
- **D.** Open Outlook in a browser on a developer laptop → Record mouse coordinates with Power Automate for desktop → Copy email text into Notepad → Import CSV nightly

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Verify the Exchange Online `Email Server Profile` and Server-Side Sync defaults in PPAC, create the Dataverse `Queue` with its email address, `Approve Email` on the Queue Mailbox, and run `Test & Enable Mailbox` until status = `Success`. [PL-200 Manage environments — Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook) | Ref: Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook (https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization)]

- **A:** Incorrect — The legacy Email Router is deprecated; Server-Side Synchronization requires mailbox approval (when configured) and Test & Enable Mailbox succeeding.
- **B:** Correct — Routing shared-inbox emails into a Dataverse Queue via Server-Side Sync requires an Email Server Profile, a Queue with email address, Email Approval, and Test & Enable Mailbox.
- **C:** Incorrect — Views, Word Templates, and Bulk Deletion do not configure Exchange Server-Side Synchronization or Queue mailboxes.
- **D:** Incorrect — Dataverse includes native Exchange Server-Side Synchronization and Dynamics 365 App for Outlook without brittle UI screen-scraping.

</details>

### Q065 (`T4-Q071`) — Create and manage logic and process automation [3.6] · *Multi-Select (Select 2)*

You are establishing enterprise standards for solution-aware Dataverse cloud flows at Ironclad. Which TWO rules apply? Select two.

- **A.** The Dataverse connector supports `Change type`, `Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows` / `Unrelate rows`, bound/unbound actions, and reusable solution `Child Flows`
- **B.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **E.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). Use `Select columns`, `Filter rows`, `Expand Query`, bound/unbound actions, and `Child Flows` on the Dataverse connector, and share manual/Canvas flows via `Run-only users`. [PL-200 Create and manage logic and process automation — Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows | Ref: Manage, share, test with static results, and troubleshoot cloud flows (https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)]

- **A:** Correct — Setting both `Select columns` and `Filter rows` on Dataverse triggers avoids firing flows when unrelated columns change.
- **B:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **E:** Correct — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.

</details>

### Q066 (`T4-Q094`) — Manage environments [4.5] · *Ordered Sequence (Multiple Choice)*

You are ready to export `IroncladWarranty` from Dev and promote it as Managed into Production with stage-specific SAP URLs, SharePoint libraries, and service accounts. Order the exact ALM steps.

- **A.** Clear Dev Current Values on Environment Variables & run Solution Checker → Publish all customizations & Export as Managed → Import the Managed `.zip` into UAT/Production → Bind target Connection References & Environment Variable values
- **B.** Delete the Managed solution in Production every Friday (removing custom table data!) → Recreate tables manually → Re-import CSV backups → Reassign all Security Roles
- **C.** Import an unvalidated solution into Production first → Run Solution Checker two weeks later → Create Environment Variables directly inside Production Default Solution → Skip publishing
- **D.** Export the entire Default Solution from Dev as Unmanaged → Import Unmanaged directly into Production → Hardcode Dev URLs inside flow steps → Share personal maker logins

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Clear Dev `Current Values` on Environment Variables and run Solution Checker, Publish all customizations and Export as `Managed`, Import into UAT/Production, and bind target Connection References and Environment Variable values. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Correct — Healthy ALM runs Solution Checker, publishes customizations, exports as Managed, and binds target-stage Connection References and Environment Variables at import.
- **B:** Incorrect — Deleting a Managed solution that defines custom tables permanently deletes those tables and their Production data; use Managed Upgrade (`Stage for upgrade`) instead.
- **C:** Incorrect — Unpublished changes in Dev are excluded from exported solutions, and Solution Checker should gate packages before Production import.
- **D:** Incorrect — Never export the Default Solution or import Unmanaged solutions into Production; use segmented Managed solutions with Connection References and Environment Variables.

</details>

## Case Study Vignette — Ironclad Heavy Machinery

> [Scenario: Ironclad Heavy Machinery integrates ERP dealer part orders into Dataverse every 15 minutes using natural external `ERPOrderNumber` strings instead of Dataverse GUIDs. Warranty managers manage up to four direct-report tiers of regional analysts without granting Business Unit-wide Read rights, and live ERP backorder stock is projected without copying rows into Dataverse.]

### Q067 (`T4-Q001`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

Case study — Ironclad Heavy Machinery: Ironclad’s SAP ERP exposes 12 million live `Backorder Inventory` rows via an OData v4 endpoint, and warranty analysts must view real-time warehouse stock inside model-driven forms without copying or syncing rows into Dataverse database capacity. Which table type should you create?

- **A.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version
- **B.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops
- **C.** `Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage
- **D.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create a `Virtual table` using the OData v4 / virtual connector provider so Dataverse projects live ERP inventory on demand with zero local row storage. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.
- **B:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.
- **C:** Correct — Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.
- **D:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q068 (`T4-Q009`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

Case study — Ironclad Heavy Machinery: Ironclad’s 15-minute ERP integration upserts `Dealer Part Order` rows using the external natural string `ERPOrderNumber` rather than querying Dataverse GUIDs first, and duplicate `ERPOrderNumber` values must be rejected by the database index. What should you configure?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Define an `Alternate Key` on the `ERPOrderNumber` text column and confirm its background index status becomes `Active`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.

</details>

### Q069 (`T4-Q021`) — Configure Microsoft Dataverse [1.9] · *Single-Answer Multiple Choice*

Case study — Ironclad Heavy Machinery: Warranty VPs oversee Regional Directors -> Senior Analysts -> Junior Analysts -> Trainees (`4` direct-report tiers) and must inspect rows across their management chain WITHOUT granting broad Business-Unit-wide Read privileges on sibling managers’ analysts. Which Dataverse feature fits?

- **A.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user
- **D.** `Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Enable `Hierarchy Security` (`Manager` hierarchy with `Depth = 4`) while keeping the `Warranty Analyst` Security Role’s `Read` privilege at `User` depth. [PL-200 Configure Microsoft Dataverse — Manage Business Units and Modernized Business Units (matrix data access) | Ref: Security concepts in Microsoft Dataverse and Modernized Business Units (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)]

- **A:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.
- **D:** Correct — Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.

</details>

### Q070 (`T4-Q085`) — Manage environments [4.1] · *Multi-Select (Select 2)*

Before exporting `IroncladWarranty` for UAT deployment, which TWO pre-export checks belong on every Functional Consultant’s release checklist? Select two.

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **C.** Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** `App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Verify only modified subcomponents are included (`Segmented Solution` under a custom `Solution Publisher`), and run `Solution Checker` (plus `Publish all customizations`) to resolve `Critical`/`High` findings. [PL-200 Manage environments — Describe use cases and findings for App Checker and Solution Checker | Ref: Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **C:** Correct — `Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Correct — Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.

</details>

### Q071 (`T4-Q025`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

Ironclad’s IAM team manages global plant engineers in Microsoft Entra ID security groups and wants Dataverse Security Roles granted on-demand at sign-in without pre-creating manual Owner Team memberships. Which team type should you configure?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **C.** Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions
- **D.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create `Microsoft Entra ID Security Group Teams` in Dataverse linked to each Entra group’s Object ID and assign Security Roles to those teams. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **C:** Incorrect — `Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.
- **D:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.

</details>

### Q072 (`T4-Q011`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

A `Field Rental Contract` can be leased either to a corporate construction `Account` or an independent farmer `Contact`. Which single Dataverse column type lets a lookup point to either `Account` or `Contact`?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **C.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule
- **D.** BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Create a polymorphic `Customer` column on `Field Rental Contract`. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **C:** Correct — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.
- **D:** Incorrect — Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.

</details>

### Q073 (`T4-Q089`) — Manage environments [4.3] · *Single-Answer Multiple Choice*

After importing `IroncladWarranty_4_1_0_0_managed.zip` using `Stage for upgrade` in Production, an admin wants to verify that a new migration flow populates a replacement column BEFORE executing `Apply upgrade` (which deletes the retired column). Why is `Stage for upgrade` valuable here?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Staging for upgrade installs `4.1.0.0` side-by-side (`IroncladWarranty_Upgrade` holding solution) so admins can run data migration steps before `Apply upgrade` drops retired schema components. [PL-200 Manage environments — Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update | Ref: Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Correct — Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.
- **D:** Incorrect — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q074 (`T4-Q095`) — Manage environments [4.5] · *Single-Answer Multiple Choice*

A Canvas app and 3 cloud flows inside `IroncladWarranty` connect to a `Dealer Schematics` SharePoint Online site/list that differs across `Dev`, `UAT`, and `Prod`. Which specific `Environment Variable` data type binds SharePoint sites and lists cleanly across environments?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create `Data Source` Environment Variables (`SharePoint` connector parameter type: one for `Site` and one for `List`) and reference them inside both the Canvas app and cloud flows. [PL-200 Manage environments — Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines | Ref: Use Environment Variables, Connection References, and Power Platform pipelines in ALM (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Correct — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.

</details>

### Q075 (`T4-Q060`) — Create and manage logic and process automation [3.2] · *Single-Answer Multiple Choice*

On the Dataverse `When a row is added, modified or deleted` trigger, what does setting `Scope` (`Row scope`) to `Business Unit` instead of `Organization` accomplish alongside its webhook architecture?

- **A.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **B.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **C.** Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Setting trigger `Scope = Business Unit` fires the event webhook ONLY for rows owned within the flow owner’s Business Unit rather than every Business Unit across the organization. [PL-200 Create and manage logic and process automation — Describe connector triggers, actions, polling/webhooks, and Connection References | Ref: Connectors, triggers, actions, and Connection References in Power Automate (https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation)]

- **A:** Correct — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **B:** Incorrect — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **C:** Incorrect — When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.

</details>

### Q076 (`T4-Q010`) — Configure Microsoft Dataverse [1.4] · *Single-Answer Multiple Choice*

On `Equipment Serial Asset`, you configure a `TotalWarrantySpend` Rollup column summing approved child `Warranty Claim` totals (`SUM`) and a `RemainingCoverageDays` Power Fx Formula column (`DateDiff(Today(), WarrantyEndDate, TimeUnit.Days)`). How do their recalculation timings differ?

- **A.** `Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **D.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). The `Power Fx Formula` column evaluates immediately on read, whereas the `Rollup` column recalculates asynchronously on a background timer (minimum 1-hour interval) or when manually refreshed on the form. [PL-200 Configure Microsoft Dataverse — Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns | Ref: Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)]

- **A:** Correct — Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **D:** Incorrect — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.

</details>

### Q077 (`T4-Q099`) — Manage environments [4.7] · *Single-Answer Multiple Choice*

Ironclad generates a `Dealer Credit Memo.docx` Word Template from `Warranty Claim` displaying header details plus a dynamic table of approved `Claim Line Item` child rows (`1:N`). Complete the Word desktop XML mapping step: ____.

- **A.** `ModelDrivenFormIntegration.Item`
- **B.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **C.** `Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row
- **D.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Enable the `Developer` tab, open `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`), and insert a `Repeating` content control around the line-item row. [PL-200 Manage environments — Configure SharePoint Document Management and Microsoft Word Templates | Ref: Configure SharePoint Document Management and Microsoft Word Templates in Power Platform (https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365)]

- **A:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **B:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **C:** Correct — Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.
- **D:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.

</details>

### Q078 (`T4-Q088`) — Manage environments [4.2] · *Single-Answer Multiple Choice*

Ironclad wants citizen and functional makers to deploy solutions from `Dev` to `UAT` and `Prod` via delegated service-principal identity without granting makers `System Administrator` rights in `UAT` or `Prod`. Which built-in platform capability supports delegated deployments?

- **A.** `Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests
- **B.** Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history
- **C.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Configure `Power Platform pipelines` (with `Managed Environments`), enabling delegated service-principal Managed deployments with approval workflows. [PL-200 Manage environments — Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones) | Ref: Solutions overview, custom publishers, segmented tables, and patches in Power Platform (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)]

- **A:** Correct — Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.
- **B:** Incorrect — Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.
- **C:** Incorrect — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.

</details>

### Q079 (`T4-Q065`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

A regional dispatch flow must suppress execution completely unless `orc_permitstatus` equals `100000002` and `orc_district` equals `'Downtown'`. Complete the `Trigger Condition` expression: ____.

- **A.** `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))`
- **B.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **C.** `ModelDrivenFormIntegration.Item`
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `@and(equals(triggerOutputs()?['body/orc_permitstatus'], 100000002), equals(triggerOutputs()?['body/orc_district'], 'Downtown'))` blocks non-matching runs at the trigger gate. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Correct — Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.
- **B:** Incorrect — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **C:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q080 (`T4-Q035`) — Create apps by using Microsoft Power Apps [2.3] · *Multi-Select (Select 2)*

You are configuring views on `Spare Part` and `Warranty Claim` in your solution. Which TWO view behaviors are accurate? Select two.

- **A.** `Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **E.** `Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, E` (`CSV: 1,5`)

Correct answers: A and E (are correct). The `Lookup View` controls columns displayed inside Lookup dropdowns while `Quick Find View` controls search/indexing, and `Public` views appear in table view selectors while `Personal` views are user-created and shareable. [PL-200 Create apps by using Microsoft Power Apps — Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal) | Ref: Create and edit public, system, Quick Find, Lookup, and Associated views (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)]

- **A:** Correct — Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **E:** Correct — View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.

</details>

### Q081 (`T4-Q029`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

In your `Warranty Operations` model-driven app, `Quality Engineers` need an `8D Root-Cause Main Form` while `Claims Clerks` need a `Fast-Track Reimbursement Main Form`, and general executives need a clean `Executive Summary Main Form` as fallback. How do you configure this?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely
- **C.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **D.** Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Assign `Quality Engineer` and `Claims Clerk` Security Roles to their respective Main forms, set `Form Order`, and enable `Fallback` on `Executive Summary Main Form`. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.
- **C:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **D:** Incorrect — Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.

</details>

### Q082 (`T4-Q015`) — Configure Microsoft Dataverse [1.6] · *Multi-Select (Select 3)*

You are reviewing data governance, integration keys, and reporting exports for Ironclad Heavy Machinery. Which THREE statements are accurate? Select three.

- **A.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **B.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **C.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage
- **D.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **E.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy
- **F.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, E` (`CSV: 2,3,5`)

Correct answers: B, C, and E (are correct). Three-tier Auditing writes field history to `Log` capacity, `Alternate Keys` enforce natural-key uniqueness/upserts, and `Dynamic Excel` exports refresh live rows per viewer’s Security Role while `Static` exports save fixed snapshots. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **B:** Correct — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **C:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.
- **D:** Incorrect — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **E:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.
- **F:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.

</details>

### Q083 (`T4-Q017`) — Configure Microsoft Dataverse [1.7] · *Single-Answer Multiple Choice*

A regional warranty supervisor opens the `Pending Claims Under $5,000` Public View and wants to bulk-edit `ReviewerComments` and `ApprovalCode` across 60 rows right inside the browser tab without downloading or re-uploading files. Which option should he choose?

- **A.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **B.** `ModelDrivenFormIntegration.Item`
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** `Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Select `Export to Excel` -> `Open in Excel Online`, edit the 60 rows inline, and select `Save` to commit changes back to Dataverse. [PL-200 Configure Microsoft Dataverse — Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link) | Ref: Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export)]

- **A:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **B:** Incorrect — Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Correct — Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.

</details>

### Q084 (`T4-Q023`) — Configure Microsoft Dataverse [1.10] · *Single-Answer Multiple Choice*

When creating a least-privilege `Dealer Auditor` custom Security Role from scratch rather than copying `Basic User`, makers frequently omit core environment/metadata `Read` privileges (`prvReadPluginAssembly`, `prvReadAppModule`), causing model-driven apps to fail on load. What is Microsoft’s recommended practice?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Always create custom Security Roles by copying `Basic User` (or the closest minimal baseline role) so essential platform metadata privileges remain intact, then add custom table privileges. [PL-200 Configure Microsoft Dataverse — Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance) | Ref: Security roles and privileges (Append vs Append To, inheritance) in Dataverse (https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.
- **C:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Incorrect — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

### Q085 (`T4-Q014`) — Configure Microsoft Dataverse [1.6] · *Single-Answer Multiple Choice*

ISO-9001 quality auditors require tracking who changed `ApprovedReimbursementAmount` on `Warranty Claim`, along with before-and-after currency values and timestamps. Which three switches must ALL be enabled?

- **A.** Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier
- **B.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **C.** `Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`
- **D.** Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Environment `Start Auditing` in PPAC, Table `Audit changes to its data` on `Warranty Claim`, and Column `Enable auditing` on `ApprovedReimbursementAmount`. [PL-200 Configure Microsoft Dataverse — Manage environment, table, and column-level auditing and retention | Ref: Manage Dataverse auditing (environment, table, column, and log retention) (https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)]

- **A:** Incorrect — The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.
- **B:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **C:** Incorrect — Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.
- **D:** Correct — If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.

</details>

### Q086 (`T4-Q002`) — Configure Microsoft Dataverse [1.1] · *Single-Answer Multiple Choice*

You are designing a `Dealer Warranty Claim` table where regional warranty teams must own claims per Business Unit, track notes/photos on Timeline, and sync delta changes to an Azure data warehouse. Which creation-time and table settings should you select?

- **A.** Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled
- **B.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes
- **C.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **D.** Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Select `Ownership = User or team` at creation time and enable `Enable attachments (notes and files)` plus `Track changes` on the table properties. [PL-200 Configure Microsoft Dataverse — Create or modify standard, activity, or virtual tables and configure table properties | Ref: Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview)]

- **A:** Incorrect — Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.
- **B:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.
- **C:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **D:** Correct — Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.

</details>

### Q087 (`T4-Q030`) — Create apps by using Microsoft Power Apps [2.1] · *Single-Answer Multiple Choice*

You add a `Dealer Scorecards` Power BI dashboard subarea and a `Recall Command Center` Custom Page subarea under a new `Quality Leadership` Area in the model-driven Sitemap. Where do users switch between `Warranty Desk` and `Quality Leadership`?

- **A.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **B.** Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies
- **C.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **D.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Users switch between Sitemap `Areas` using the area switcher in the bottom-left corner of the left navigation pane. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **B:** Incorrect — `Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.
- **C:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **D:** Correct — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.

</details>

### Q088 (`T4-Q048`) — Create apps by using Microsoft Power Apps [2.9] · *Ordered Sequence (Multiple Choice)*

Pressing `Validate VIN Warranty` in a dealer Canvas app must call a solution cloud flow passing `VIN`, query SAP synchronously, and return `CoverageTier` to the Canvas app while keeping 400 mechanics as `Run-only users`. Put the steps in exact order.

- **A.** Create a classic Background Dataverse workflow → Embed an iframe pointing to flow.microsoft.com → Store maker passwords inside a Canvas text label → Poll Run History manually
- **B.** Use a Scheduled Recurrence trigger first → Omit Respond to a Power App or flow → Hardcode FlowName.Run() before adding the flow to the app → Grant Co-owner rights to all 500 end users
- **C.** Remove all triggers from the cloud flow → Export the flow outside any Solution → Bind a Quick View form to the button → Expect synchronous values after 45-minute waits
- **D.** Build a solution flow with the Power Apps (V2) trigger & typed inputs → End with Respond to a Power App or flow → Add the flow in Canvas Studio Power Automate pane → Call Set(varOut, FlowName.Run(...)) & set Run-only users

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Create a solution flow with `Power Apps (V2)` typed inputs, end with `Respond to a Power App or flow`, add it in Canvas Studio, and invoke `Set(varOut, FlowName.Run(...))` with `Run-only users`. [PL-200 Create apps by using Microsoft Power Apps — Call Microsoft Power Automate cloud flows from a Canvas app and handle responses | Ref: Start a Power Automate cloud flow from a canvas app and return values (https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows)]

- **A:** Incorrect — Canvas apps invoke cloud flows natively through the Power Apps (V2) trigger and FlowName.Run() connector bridge, never via iframes or plaintext credentials.
- **B:** Incorrect — Scheduled flows cannot be invoked synchronously via FlowName.Run(), and end users need Run-only user permissions rather than Co-owner edit rights.
- **C:** Incorrect — Every cloud flow requires a trigger, and Respond to a Power App or flow must return within the synchronous HTTP timeout window (~120 seconds).
- **D:** Correct — Canvas-invoked flows define typed inputs on Power Apps (V2), return outputs via Respond to a Power App or flow, bind in Studio, and capture outputs via FlowName.Run(...).

</details>

### Q089 (`T4-Q013`) — Configure Microsoft Dataverse [1.5] · *Single-Answer Multiple Choice*

After enabling Dataverse Search, warranty analysts notice retired `Scrapped` assets (`Status = Inactive`) clutter global search results for `Equipment Serial Asset`. Where do you exclude inactive assets from Dataverse Search?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)
- **C.** `Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values
- **D.** Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Edit the filter criteria on the `Equipment Serial Asset` table’s `Quick Find View` (`Status Equals Active`) and publish customizations. [PL-200 Configure Microsoft Dataverse — Configure Dataverse search, Quick Find views, and search index columns | Ref: Configure Dataverse search to improve search results and performance (https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Incorrect — Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.
- **C:** Incorrect — Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.
- **D:** Correct — Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.

</details>

## Case Study Vignette — GearGrid Dealer Portal

> [Scenario: GearGrid Dealer Portal serves external equipment dealerships on Microsoft Power Pages. Dealership Warranty Clerks (Contacts under a Dealership Account) must view and edit all Warranty Claims submitted by ANY coworker at their same Dealership Account, view an embedded Power BI warranty-cost dashboard filtered by dealership via RLS, and never use deprecated local username/password sign-in.]

### Q090 (`T4-Q052`) — Create apps by using Microsoft Power Apps [2.11] · *Single-Answer Multiple Choice*

Case study — GearGrid Dealer Portal: GearGrid wants each signed-in Dealership Principal to view an interactive `Power BI` `Warranty Cost & Chargeback` dashboard embedded on a portal webpage, automatically filtered so each dealership sees ONLY its own data. How is this configured?

- **A.** Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production
- **B.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **C.** `Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs
- **D.** `Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Enable `Power BI Embedded` service in Power Pages `Set up` workspace, pass the signed-in portal user context via Power BI `Row-Level Security (RLS)` (`username()`/`customdata()`), and embed with the `powerbi` Liquid tag / Studio component. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.
- **B:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **C:** Incorrect — Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.
- **D:** Incorrect — While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.

</details>

### Q091 (`T4-Q053`) — Create apps by using Microsoft Power Apps [2.11] · *Multi-Select (Select 3)*

Case study — GearGrid Dealer Portal: You are finalizing authentication, forms, and analytics for `GearGrid Dealer Portal`. Which THREE architectural choices meet GearGrid’s requirements? Select three.

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS
- **C.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **D.** Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries
- **E.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **F.** Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E, F` (`CSV: 2,5,6`)

Correct answers: B, E, and F (are correct). Disable deprecated local username/password login in favor of `Microsoft Entra External ID` / OIDC, secure `Lists`/`Basic Forms` via `Account`-scoped `Table Permissions` + `Web Roles`, and embed `Power BI` with `RLS` alongside `Multi-Step Forms`. [PL-200 Create apps by using Microsoft Power Apps — Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI) | Ref: Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages (https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.
- **C:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **D:** Incorrect — Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.
- **E:** Correct — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **F:** Correct — `Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.

</details>

### Q092 (`T4-Q055`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

Case study — GearGrid Dealer Portal: Every Warranty Clerk `Contact` employed under `Midwest Tractor Co.` (`Account`) must view and edit `Warranty Claim` rows submitted by ANY coworker at `Midwest Tractor Co.`, while seeing zero claims from rival dealerships. Complete the Power Pages security setting: ____.

- **A.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **D.** Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a `Table Permission` with `Access Type = Account` linked to the `Dealership Account` lookup relationship on `Warranty Claim`. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Correct — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **D:** Incorrect — Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.

</details>

### Q093 (`T4-Q069`) — Create and manage logic and process automation [3.5] · *Single-Answer Multiple Choice*

When an `8D Investigation` confirms a batch defect, a cloud flow links that `8D Investigation` row to affected `Supplier Shipment` rows across a native `N:N` relationship. Complete the Dataverse connector action: ____.

- **A.** Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)
- **B.** `formatDateTime(coalesce(triggerOutputs()?['body/orc_alternatedate'], triggerOutputs()?['body/orc_primarydate']), 'yyyy-MM-dd')`
- **C.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **D.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Use the Dataverse `Relate rows` action with the `N:N` relationship name and target row `@odata.id` (`OData Id`). [PL-200 Create and manage logic and process automation — Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows) | Ref: Use the Microsoft Dataverse connector in Power Automate cloud flows (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Correct — Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.
- **B:** Incorrect — `coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.
- **C:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **D:** Incorrect — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.

</details>

### Q094 (`T4-Q082`) — Create and manage logic and process automation [3.12] · *Single-Answer Multiple Choice*

A warranty analyst wants to hide the entire `Hazardous Core Return` Main form Tab whenever a `Hazard Classifications` (`Choices` Multi-Select) column excludes `Lithium Battery`. Why can a Dataverse `Business Rule` NOT perform this?

- **A.** Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook
- **B.** Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors
- **C.** Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps
- **D.** `Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Business Rules neither evaluate `Choices (Multi-Select)` columns nor show/hide whole form Tabs or Sections (use a tiny form JavaScript `setVisible` handler instead). [PL-200 Create and manage logic and process automation — Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions | Ref: Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule)]

- **A:** Correct — Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.
- **B:** Incorrect — Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.
- **C:** Incorrect — Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.
- **D:** Incorrect — Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.

</details>

### Q095 (`T4-Q066`) — Create and manage logic and process automation [3.4] · *Single-Answer Multiple Choice*

In Power Automate, why should makers access optional JSON properties using the safe-navigation question-mark operator (`triggerOutputs()?['body/orc_dealercomments']`) paired with `coalesce(..., '')` instead of strict bracket indexing (`['body']['orc_dealercomments']`)?

- **A.** Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)
- **B.** WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`
- **C.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **D.** Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Safe-navigation `?` returns `null` instead of throwing a `Property doesn't exist` runtime error when Dataverse omits null columns from trigger payloads, allowing `coalesce()` to supply a clean fallback. [PL-200 Create and manage logic and process automation — Implement Dynamic Content, WDL expressions, and Trigger Conditions | Ref: Reference guide for Workflow Definition Language expressions in Power Automate (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.
- **B:** Correct — Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.
- **C:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **D:** Incorrect — Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.

</details>

### Q096 (`T4-Q056`) — Create apps by using Microsoft Power Apps [2.12] · *Single-Answer Multiple Choice*

GearGrid also offers an `Individual Technician Exam Voucher` portal form where each mechanic must see ONLY voucher requests linked to their own personal `Contact` row, hidden even from coworkers at the same dealership. Complete the Power Pages setting: ____.

- **A.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`
- **B.** `orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`
- **C.** `Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship
- **D.** `If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure a `Table Permission` with `Access Type = Contact` linked to the `Technician (Contact)` lookup relationship. [PL-200 Create apps by using Microsoft Power Apps — Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication | Ref: Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages (https://learn.microsoft.com/en-us/power-pages/security/security-overview)]

- **A:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.
- **B:** Incorrect — Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.
- **C:** Correct — In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.
- **D:** Incorrect — In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.

</details>

### Q097 (`T4-Q026`) — Configure Microsoft Dataverse [1.11] · *Single-Answer Multiple Choice*

For catastrophic `Root-Cause Recall Investigations`, the lead engineer invites 5 temporary cross-plant metallurgists to edit one specific `Recall Case` row without owning records or modifying Security Roles. Which team model avoids role-cache bloat?

- **A.** Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role
- **B.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals
- **C.** `Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles
- **D.** Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Configure an `Access Team Template` on `Recall Case` with an Access Team subgrid on the Main form. [PL-200 Configure Microsoft Dataverse — Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams | Ref: Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams (https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)]

- **A:** Incorrect — Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.
- **B:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.
- **C:** Correct — Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.
- **D:** Incorrect — Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.

</details>

### Q098 (`T4-Q062`) — Create and manage logic and process automation [3.3] · *Single-Answer Multiple Choice*

A nightly warranty-reimbursement flow processes 2,500 claim lines inside `Apply to each` and currently takes 48 minutes at default sequential concurrency. Proposed solution: Replace an in-loop `Set variable` tax calculation with an immutable `Compose` action inside the loop and enable `Apply to each` `Concurrency Control` (`Degree of Parallelism = 25`). Will this accelerate the loop safely without cross-iteration variable corruption?

- **A.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **B.** `Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)
- **C.** `Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`
- **D.** Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Yes—removing shared `Set variable` mutations in favor of `Compose` allows parallel `Apply to each` threads (`Concurrency Control = 25`) to run safely without race conditions. [PL-200 Create and manage logic and process automation — Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables) | Ref: Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **B:** Correct — Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.
- **C:** Incorrect — Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.
- **D:** Incorrect — Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.

</details>

### Q099 (`T4-Q031`) — Create apps by using Microsoft Power Apps [2.1] · *Multi-Select (Select 2)*

You are reviewing a model-driven app in App Designer before publishing to Production. Which TWO behaviors are true? Select two.

- **A.** Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship
- **B.** Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table
- **C.** Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege
- **D.** Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction
- **E.** Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C, E` (`CSV: 3,5`)

Correct answers: C and E (are correct). Adding only the specific forms, views, and dashboards needed in the app keeps the app picker uncluttered (requiring one Fallback Main form), and table-bound Sitemap subareas auto-hide when users lack table `Read` privilege. [PL-200 Create apps by using Microsoft Power Apps — Create and configure model-driven sitemaps and multiple form types (form order & fallback) | Ref: Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order) (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms)]

- **A:** Incorrect — Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.
- **B:** Incorrect — Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.
- **C:** Correct — Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.
- **D:** Incorrect — Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.
- **E:** Correct — At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.

</details>

### Q100 (`T4-Q039`) — Create apps by using Microsoft Power Apps [2.5] · *Single-Answer Multiple Choice*

Before dispatching a heavy-crane field technician from the modern command bar on `WorkOrders`, supervisors must confirm `"Dispatch this technician now?"` in a native modal. Complete the Power Fx formula: ____.

- **A.** `Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`
- **B.** `ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`
- **C.** `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`
- **D.** `Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))` prompts with `Confirm(...)` before patching. [PL-200 Create apps by using Microsoft Power Apps — Configure Modern Commanding by using Power Fx and Component Libraries | Ref: Use Power Fx with modern commanding in model-driven apps (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx)]

- **A:** Incorrect — On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.
- **B:** Incorrect — `ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.
- **C:** Correct — `Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.
- **D:** Incorrect — In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.

</details>
