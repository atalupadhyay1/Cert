# Microsoft Exam PL-200 — Companion Case Study Scenarios (24 Vignettes)

Attach this document as a downloadable resource when uploading `practice-set-{1..6}.csv` (Option A), or upload `case-embedded-set-{1..6}.csv` (Option B) so every case-linked question embeds its full scenario brief inline inside the Udemy question prompt.

> All 24 organizations and scenarios below are 100% original fictional Functional Consultant case studies authored for independent exam preparation. None reproduce Microsoft’s copyrighted exam case studies.

## Full-Length Mock Exam 1 — Commercial Real Estate & Leasing — Matrix BUs, Power Pages Account Scope, Modern Commanding & Solution Layers

### Vanguard Facility Maintenance (Q017, Q018, Q019)

[Scenario: Vanguard Facility Maintenance dispatches HVAC technicians via a model-driven app and a companion Canvas app. Supervisors want a command-bar button on the Work Order Main form that confirms intent, stamps Status = Dispatched via Power Fx, opens a responsive Custom Page dialog passing the record GUID, and triggers a synchronous pre-save stock check.]

### Harborstone Property Group (Q042, Q043, Q044)

[Scenario: Harborstone Property Group manages 180 commercial office towers across four regional Business Units. Leasing agents belong to their region BU yet occasionally co-broker suites in sibling regions without changing primary BU. Deleting a Building must be blocked while any active Suite child row still references it, and tenant Tax IDs require field masking.]

### Oakridge Lease Renewals (Q067, Q068, Q069)

[Scenario: Oakridge Lease Renewals promotes its Leasing Solution from Dev through UAT to Production. Last month a contractor edited the Lease Main form directly in UAT Default Solution, blocking new Managed changes from appearing. Legal also needs one-button standardized Lease Renewal letters generated as `.docx` files showing up to 25 child Rent Escalation rows.]

### Crestview Tenant Portals (Q090, Q091, Q092)

[Scenario: Crestview Tenant Portals runs a Microsoft Power Pages site over Dataverse for commercial tenants and anonymous retail prospects. Anonymous visitors browse public suite listings, while signed-in Tenant Facility Managers must view and create Maintenance Tickets linked only to their own parent Account company and upload damage photos to SharePoint.]

## Full-Length Mock Exam 2 — Specialty Healthcare & Referrals — Dataverse Search, Multi-Step Forms, Embedded Canvas Apps & Minimal Sandbox Copy

### Beacon Clinical Trials (Q017, Q018, Q019)

[Scenario: Beacon Clinical Trials runs regulated Dataverse environments (`Dev`, `UAT Sandbox`, `Production`). To investigate a production flow bug without copying 400 GB of patient rows or firing live outbound webhooks, admins refresh a clean metadata-only Sandbox and route trial-coordinator emails from Exchange Online into a shared Dataverse Queue via Server-Side Sync.]

### MedBridge Referral Portal (Q042, Q043, Q044)

[Scenario: MedBridge Referral Portal lets external referring physicians submit multi-page clinical referrals on Microsoft Power Pages. Step 1 captures patient demographics, Step 2 branches conditionally to Cardiology or Oncology questions based on Specialty, and external physicians authenticate via Microsoft Entra External ID while seeing only referrals they submitted (`Contact` scope).]

### Apex Medical Equipment (Q067, Q068, Q069)

[Scenario: Apex Medical Equipment tracks infusion pumps in a model-driven app. Biomed engineers want inline editing of Calibration Logs inside a parent Pump Main form without opening child pages, an embedded Canvas calibration calculator reading the current host Pump record live, and a cross-table Business Process Flow spanning Triage to Repair Order.]

### Clearpath Specialty Clinics (Q090, Q091, Q092)

[Scenario: Clearpath Specialty Clinics operates 45 outpatient centers in Dataverse. Referral coordinators need fast typist-tolerant search across Patient, Referral, and Provider tables, column-level audit history on Narcotic Schedule changes, and nightly cleanup of unverified web inquiry rows older than 90 days without custom code.]

## Full-Length Mock Exam 3 — Municipal & Utility Permitting — Access Team Templates, Canvas Delegation/IfError, WDL Trigger Conditions & Managed Upgrades

### Greenway Parks & Events (Q017, Q018, Q019)

[Scenario: Greenway Parks & Events automates special-event permits in Power Automate and Dataverse. A cloud flow must fire ONLY when `PermitStatus` changes to Approved on rows in the `Downtown` district, format event dates safely even when `AlternateDate` is null, catch downstream SharePoint failures via `Scope` `Configure run after`, and roll back invalid fee saves synchronously.]

### Summit Transit Claims (Q042, Q043, Q044)

[Scenario: Summit Transit Claims packages customizations under a custom Solution Publisher (`stc_`) in Dev and deploys Managed solutions to Test and Production. A retired `LegacyClaimNotes` column must be deleted cleanly from Production on the next deployment, while SharePoint folder structures organize claim photos automatically under parent Account -> Incident hierarchy.]

### MetroWater Field Operations (Q067, Q068, Q069)

[Scenario: MetroWater Field Operations equips valve-inspection crews with a mobile Canvas app over Dataverse (`350,000` Valve rows). Crews filter valves by District without hitting the 500/2,000 non-delegable row cap, stage offline-ready edits in a local Collection, catch network write errors gracefully with `IfError`, and call a Power Automate flow that returns a work-order number.]

### Rivergate Civic Permits (Q090, Q091, Q092)

[Scenario: Rivergate Civic Permits tracks building applications in Dataverse. Ad-hoc project reviewers from Fire, Zoning, and Legal join individual high-profile Permit rows dynamically without creating new Microsoft Entra groups per permit or owning rows themselves, while duplicate parcel submissions matching Street Address + Parcel Code must prompt clerks on save.]

## Full-Length Mock Exam 4 — Industrial Manufacturing & Dealer Warranty — Alternate Keys, Hierarchy Security, Cross-Table BPFs & Low-Code Plug-ins

### Precision Quality Audits (Q017, Q018, Q019)

[Scenario: Precision Quality Audits manages 8D supplier investigations in Dataverse. Quality directors need a four-stage Business Process Flow that branches to `Containment Lab` when `Severity = Critical`, launches an on-demand cloud flow button right inside Stage 3, and tracks how many hours each investigation spent inside each BPF stage on a chart.]

### Titan Spare Parts Supply (Q042, Q043, Q044)

[Scenario: Titan Spare Parts Supply runs classic background Dataverse workflows alongside modern cloud flows and Dataverse low-code Power Fx plug-ins. Disk log storage spiked because millions of succeeded classic workflow `ProcessSession` logs were never purged, and makers want reusable server-side Power Fx validation invoked both on table `Update` and on demand from Canvas apps.]

### Ironclad Heavy Machinery (Q067, Q068, Q069)

[Scenario: Ironclad Heavy Machinery integrates ERP dealer part orders into Dataverse every 15 minutes using natural external `ERPOrderNumber` strings instead of Dataverse GUIDs. Warranty managers manage up to four direct-report tiers of regional analysts without granting Business Unit-wide Read rights, and live ERP backorder stock is projected without copying rows into Dataverse.]

### GearGrid Dealer Portal (Q090, Q091, Q092)

[Scenario: GearGrid Dealer Portal serves external equipment dealerships on Microsoft Power Pages. Dealership Warranty Clerks (Contacts under a Dealership Account) must view and edit all Warranty Claims submitted by ANY coworker at their same Dealership Account, view an embedded Power BI warranty-cost dashboard filtered by dealership via RLS, and never use deprecated local username/password sign-in.]

## Full-Length Mock Exam 5 — Wealth Advisory & Insurance — Manual N:N Intersects, Form Component Controls, Dataverse Expand Query & Solution Checker

### Meridian Regulatory Filing (Q017, Q018, Q019)

[Scenario: Meridian Regulatory Filing governs Dev, QA, and Production environments under strict audit controls. Before importing any solution, admins review static-analysis performance/security severities in Solution Checker, bind stage-specific SEC filing URLs and Azure Key Vault secrets via Environment Variables, and block `Microsoft Dataverse` from pairing with consumer connectors via DLP.]

### Pinnacle Claims Resolution (Q042, Q043, Q044)

[Scenario: Pinnacle Claims Resolution processes high-volume storm claims via Power Automate cloud flows and Dataverse. A daily settlement flow loops through 4,000 claim rows (`Apply to each` concurrency tuned while avoiding shared `Set variable` race bugs), expands parent Policy details in one `List rows` `Expand Query`, and shares an Instant canvas-triggered flow with 200 adjusters without exposing maker credentials.]

### Sterling Surety Insurance (Q067, Q068, Q069)

[Scenario: Sterling Surety Insurance models `Policyholder`, `Broker`, and `Surety Bond` tables in Dataverse. Each Broker can co-place many Surety Bonds and each Bond tracks `Commission Split %` and `Effective Role Date` per Broker link. Reassigning a Policyholder to a new Underwriter must automatically reassign only Active (not Closed) child Claim activities.]

### Kestrel Client Onboarding (Q090, Q091, Q092)

[Scenario: Kestrel Client Onboarding uses a model-driven app for commercial underwriters. Senior Compliance Officers require a specialized `AML Deep-Dive` Main form while standard underwriters see only the `Standard Underwriting` Main form (with a fallback form enabled), plus inline editing of related `Beneficial Owner` rows directly inside a parent Main form tab via Form Component Control.]

## Full-Length Mock Exam 6 — Higher Education & Global Grants — Custom Activity Tables, Entra Group Teams, Page Access Rules & Word XML Templates

### Westbrook University Admissions (Q017, Q018, Q019)

[Scenario: Westbrook University Admissions tracks applicants, campus visits, emails, and phone calls in Dataverse. Admissions counselors want a custom `Campus Interview` table that appears inside the unified `Timeline` control alongside Emails and Tasks with `Regarding` lookup support, plus Microsoft Entra Security Group Teams that grant Security Roles dynamically from Entra group membership.]

### Atlas Field Scholarships (Q042, Q043, Q044)

[Scenario: Atlas Field Scholarships coordinates regional reviewers across five continents. Before UAT cutover, Functional Consultants export a static vs dynamic Excel PivotTable of `Scholarship Applications` for finance, verify canvas screen-reader `AccessibleLabel` and delegation warnings in App Checker, and promote Managed upgrades via Power Platform pipelines.]

### Horizon Alumni Engagement (Q067, Q068, Q069)

[Scenario: Horizon Alumni Engagement uses a model-driven Donor app and Canvas event check-in app. Advancement officers want `Lifetime Giving Total` aggregated automatically across child `Donation` rows (`SUM`), `Days Since Last Gift` computed via Power Fx formula column, and a modern command-bar `Mark VIP` button visible only when `Lifetime Giving Total >= 50000`.]

### GlobalAid Grant Portal (Q090, Q091, Q092)

[Scenario: GlobalAid Grant Portal runs a Microsoft Power Pages site where NGOs apply for humanitarian grants. Unauthenticated visitors can read `Grant Guidelines`, only `Verified Grantee` Web Role members can open the `/submit-budget` webpage via Page Access Control Rules, and NGOs upload audited PDF financial statements directly into SharePoint folders from a Power Pages Basic Form.]
