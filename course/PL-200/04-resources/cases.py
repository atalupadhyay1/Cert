"""24 original Functional Consultant case-study scenarios (4 per exam x 6 exams) for Exam PL-200.

Zero Microsoft fictional company names; each scenario brief stays <= 390 characters so embedded
stems in case-embedded-set-{1..6}.csv stay comfortably below Udemy's 1,000-character limit.
"""

CASES = {
    # Set 1: Commercial Real Estate & Property Leasing
    'Harborstone Property Group': (
        '[Scenario: Harborstone Property Group manages 180 commercial office towers across four regional Business Units. '
        'Leasing agents belong to their region BU yet occasionally co-broker suites in sibling regions without changing primary BU. '
        'Deleting a Building must be blocked while any active Suite child row still references it, and tenant Tax IDs require field masking.]'
    ),
    'Crestview Tenant Portals': (
        '[Scenario: Crestview Tenant Portals runs a Microsoft Power Pages site over Dataverse for commercial tenants and anonymous retail prospects. '
        'Anonymous visitors browse public suite listings, while signed-in Tenant Facility Managers must view and create Maintenance Tickets '
        'linked only to their own parent Account company and upload damage photos to SharePoint.]'
    ),
    'Vanguard Facility Maintenance': (
        '[Scenario: Vanguard Facility Maintenance dispatches HVAC technicians via a model-driven app and a companion Canvas app. '
        'Supervisors want a command-bar button on the Work Order Main form that confirms intent, stamps Status = Dispatched via Power Fx, '
        'opens a responsive Custom Page dialog passing the record GUID, and triggers a synchronous pre-save stock check.]'
    ),
    'Oakridge Lease Renewals': (
        '[Scenario: Oakridge Lease Renewals promotes its Leasing Solution from Dev through UAT to Production. '
        'Last month a contractor edited the Lease Main form directly in UAT Default Solution, blocking new Managed changes from appearing. '
        'Legal also needs one-button standardized Lease Renewal letters generated as `.docx` files showing up to 25 child Rent Escalation rows.]'
    ),

    # Set 2: Specialty Healthcare & Patient Referral Services
    'Clearpath Specialty Clinics': (
        '[Scenario: Clearpath Specialty Clinics operates 45 outpatient centers in Dataverse. '
        'Referral coordinators need fast typist-tolerant search across Patient, Referral, and Provider tables, '
        'column-level audit history on Narcotic Schedule changes, and nightly cleanup of unverified web inquiry rows older than 90 days without custom code.]'
    ),
    'MedBridge Referral Portal': (
        '[Scenario: MedBridge Referral Portal lets external referring physicians submit multi-page clinical referrals on Microsoft Power Pages. '
        'Step 1 captures patient demographics, Step 2 branches conditionally to Cardiology or Oncology questions based on Specialty, '
        'and external physicians authenticate via Microsoft Entra External ID while seeing only referrals they submitted (`Contact` scope).]'
    ),
    'Apex Medical Equipment': (
        '[Scenario: Apex Medical Equipment tracks infusion pumps in a model-driven app. '
        'Biomed engineers want inline editing of Calibration Logs inside a parent Pump Main form without opening child pages, '
        'an embedded Canvas calibration calculator reading the current host Pump record live, and a cross-table Business Process Flow spanning Triage to Repair Order.]'
    ),
    'Beacon Clinical Trials': (
        '[Scenario: Beacon Clinical Trials runs regulated Dataverse environments (`Dev`, `UAT Sandbox`, `Production`). '
        'To investigate a production flow bug without copying 400 GB of patient rows or firing live outbound webhooks, '
        'admins refresh a clean metadata-only Sandbox and route trial-coordinator emails from Exchange Online into a shared Dataverse Queue via Server-Side Sync.]'
    ),

    # Set 3: Regional Municipal & Utility Permitting
    'Rivergate Civic Permits': (
        '[Scenario: Rivergate Civic Permits tracks building applications in Dataverse. '
        'Ad-hoc project reviewers from Fire, Zoning, and Legal join individual high-profile Permit rows dynamically without creating new Microsoft Entra groups per permit '
        'or owning rows themselves, while duplicate parcel submissions matching Street Address + Parcel Code must prompt clerks on save.]'
    ),
    'MetroWater Field Operations': (
        '[Scenario: MetroWater Field Operations equips valve-inspection crews with a mobile Canvas app over Dataverse (`350,000` Valve rows). '
        'Crews filter valves by District without hitting the 500/2,000 non-delegable row cap, stage offline-ready edits in a local Collection, '
        'catch network write errors gracefully with `IfError`, and call a Power Automate flow that returns a work-order number.]'
    ),
    'Greenway Parks & Events': (
        '[Scenario: Greenway Parks & Events automates special-event permits in Power Automate and Dataverse. '
        'A cloud flow must fire ONLY when `PermitStatus` changes to Approved on rows in the `Downtown` district, '
        'format event dates safely even when `AlternateDate` is null, catch downstream SharePoint failures via `Scope` `Configure run after`, and roll back invalid fee saves synchronously.]'
    ),
    'Summit Transit Claims': (
        '[Scenario: Summit Transit Claims packages customizations under a custom Solution Publisher (`stc_`) in Dev and deploys Managed solutions to Test and Production. '
        'A retired `LegacyClaimNotes` column must be deleted cleanly from Production on the next deployment, '
        'while SharePoint folder structures organize claim photos automatically under parent Account -> Incident hierarchy.]'
    ),

    # Set 4: Industrial Manufacturing & Dealer Warranty
    'Ironclad Heavy Machinery': (
        '[Scenario: Ironclad Heavy Machinery integrates ERP dealer part orders into Dataverse every 15 minutes using natural external `ERPOrderNumber` strings instead of Dataverse GUIDs. '
        'Warranty managers manage up to four direct-report tiers of regional analysts without granting Business Unit-wide Read rights, '
        'and live ERP backorder stock is projected without copying rows into Dataverse.]'
    ),
    'GearGrid Dealer Portal': (
        '[Scenario: GearGrid Dealer Portal serves external equipment dealerships on Microsoft Power Pages. '
        'Dealership Warranty Clerks (Contacts under a Dealership Account) must view and edit all Warranty Claims submitted by ANY coworker at their same Dealership Account, '
        'view an embedded Power BI warranty-cost dashboard filtered by dealership via RLS, and never use deprecated local username/password sign-in.]'
    ),
    'Precision Quality Audits': (
        '[Scenario: Precision Quality Audits manages 8D supplier investigations in Dataverse. '
        'Quality directors need a four-stage Business Process Flow that branches to `Containment Lab` when `Severity = Critical`, '
        'launches an on-demand cloud flow button right inside Stage 3, and tracks how many hours each investigation spent inside each BPF stage on a chart.]'
    ),
    'Titan Spare Parts Supply': (
        '[Scenario: Titan Spare Parts Supply runs classic background Dataverse workflows alongside modern cloud flows and Dataverse low-code Power Fx plug-ins. '
        'Disk log storage spiked because millions of succeeded classic workflow `ProcessSession` logs were never purged, '
        'and makers want reusable server-side Power Fx validation invoked both on table `Update` and on demand from Canvas apps.]'
    ),

    # Set 5: Wealth Advisory & Insurance Underwriting
    'Sterling Surety Insurance': (
        '[Scenario: Sterling Surety Insurance models `Policyholder`, `Broker`, and `Surety Bond` tables in Dataverse. '
        'Each Broker can co-place many Surety Bonds and each Bond tracks `Commission Split %` and `Effective Role Date` per Broker link. '
        'Reassigning a Policyholder to a new Underwriter must automatically reassign only Active (not Closed) child Claim activities.]'
    ),
    'Kestrel Client Onboarding': (
        '[Scenario: Kestrel Client Onboarding uses a model-driven app for commercial underwriters. '
        'Senior Compliance Officers require a specialized `AML Deep-Dive` Main form while standard underwriters see only the `Standard Underwriting` Main form '
        '(with a fallback form enabled), plus inline editing of related `Beneficial Owner` rows directly inside a parent Main form tab via Form Component Control.]'
    ),
    'Pinnacle Claims Resolution': (
        '[Scenario: Pinnacle Claims Resolution processes high-volume storm claims via Power Automate cloud flows and Dataverse. '
        'A daily settlement flow loops through 4,000 claim rows (`Apply to each` concurrency tuned while avoiding shared `Set variable` race bugs), '
        'expands parent Policy details in one `List rows` `Expand Query`, and shares an Instant canvas-triggered flow with 200 adjusters without exposing maker credentials.]'
    ),
    'Meridian Regulatory Filing': (
        '[Scenario: Meridian Regulatory Filing governs Dev, QA, and Production environments under strict audit controls. '
        'Before importing any solution, admins review static-analysis performance/security severities in Solution Checker, '
        'bind stage-specific SEC filing URLs and Azure Key Vault secrets via Environment Variables, and block `Microsoft Dataverse` from pairing with consumer connectors via DLP.]'
    ),

    # Set 6: Higher Education & Global Nonprofit Grants
    'Westbrook University Admissions': (
        '[Scenario: Westbrook University Admissions tracks applicants, campus visits, emails, and phone calls in Dataverse. '
        'Admissions counselors want a custom `Campus Interview` table that appears inside the unified `Timeline` control alongside Emails and Tasks with `Regarding` lookup support, '
        'plus Microsoft Entra Security Group Teams that grant Security Roles dynamically from Entra group membership.]'
    ),
    'GlobalAid Grant Portal': (
        '[Scenario: GlobalAid Grant Portal runs a Microsoft Power Pages site where NGOs apply for humanitarian grants. '
        'Unauthenticated visitors can read `Grant Guidelines`, only `Verified Grantee` Web Role members can open the `/submit-budget` webpage via Page Access Control Rules, '
        'and NGOs upload audited PDF financial statements directly into SharePoint folders from a Power Pages Basic Form.]'
    ),
    'Horizon Alumni Engagement': (
        '[Scenario: Horizon Alumni Engagement uses a model-driven Donor app and Canvas event check-in app. '
        'Advancement officers want `Lifetime Giving Total` aggregated automatically across child `Donation` rows (`SUM`), '
        '`Days Since Last Gift` computed via Power Fx formula column, and a modern command-bar `Mark VIP` button visible only when `Lifetime Giving Total >= 50000`.]'
    ),
    'Atlas Field Scholarships': (
        '[Scenario: Atlas Field Scholarships coordinates regional reviewers across five continents. '
        'Before UAT cutover, Functional Consultants export a static vs dynamic Excel PivotTable of `Scholarship Applications` for finance, '
        'verify canvas screen-reader `AccessibleLabel` and delegation warnings in App Checker, and promote Managed upgrades via Power Platform pipelines.]'
    ),
}
