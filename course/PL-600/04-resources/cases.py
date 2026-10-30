"""24 original Solution Architect Expert case-study scenarios (4 per exam x 6 exams) for Exam PL-600.

Zero Microsoft fictional company names; each scenario brief stays <= 420 characters so embedded
stems in case-embedded-set-{1..6}.csv stay comfortably below Udemy's 1,000-character limit.
"""

CASES = {
    1: {
        'SovereignCrest Private Bank': (
            'SovereignCrest Private Bank operates across Zurich, Frankfurt, and New York under strict Swiss/EU data-residency laws, '
            'replacing 14 Lotus Notes apps with Dynamics 365 Sales & Power Platform. Advisors need cross-BU wealth matrix visibility, '
            'column-masked net-worth fields, and Customer-Managed Keys (CMK) in Managed Environments.'
        ),
        'Alderbrook Commercial Leasing': (
            'Alderbrook Commercial Leasing is migrating 4.2 million historical lease, guarantor, and circular parent-child asset rows '
            'from Oracle into Dataverse over a 36-hour weekend cutover window. Initial UAT dry runs hit HTTP 429 Service Protection throttling '
            'and triggered 4.2M unintended welcome emails from active cloud flows.'
        ),
        'Vespera Wealth Portal': (
            'Vespera Wealth Portal serves 180,000 external retail investors submitting KYC renewals and viewing household portfolios online, '
            'alongside 350 external CPAs collaborating on institutional Dataverse rows. Architects must select external identity providers, '
            'prevent SharePoint document ACL leaks, and enforce strict DLP endpoint rules.'
        ),
        'Monarch Clearing Services': (
            'Monarch Clearing Services integrates Dataverse trade exceptions with an Azure-hosted risk engine inside a private Azure VNet '
            'with zero public endpoints. Currently, a synchronous C# plug-in calls an external credit API that occasionally stalls for 45 seconds, '
            'exhausting SQL locks and failing the 2-minute sandbox boundary.'
        ),
    },
    2: {
        'HavenBridge Health System': (
            'HavenBridge Health System is consolidating 9 regional hospital CRMs into one Power Platform tenant. '
            'Clinicians need real-time read-only visibility into 60 million HL7 lab rows stored in Azure SQL without duplicating PHI into Dataverse storage, '
            'while HIPAA auditors require three-tier Dataverse auditing and least-privilege Entra Group Teams.'
        ),
        'CareStride Home Nursing': (
            'CareStride Home Nursing equips 2,800 visiting nurses with iPads in rural dead zones lacking cellular signal for 6 hours at a time. '
            'Nurses need sub-second offline wound-care charting, barcode scanning, and conflict resolution on reconnect, '
            'paired with WCAG 2.1 AA accessibility and Power Platform Well-Architected reliability targets.'
        ),
        'MedVantage Imaging Services': (
            'MedVantage Imaging Services dispatches 900 MRI field engineers and tracks IoT helium-pressure alerts spiking to 15,000 telemetry events/minute. '
            'Architects must evaluate Dynamics 365 Field Service vs custom building, absorb high-velocity ephemeral telemetry without blowing Dataverse relational storage, '
            'and integrate SAP S/4HANA parts inventory.'
        ),
        'Aegis Clinical Trials': (
            'Aegis Clinical Trials promotes segmented Managed Solutions (`Core`, `Intake`, `Analytics`) across Dev, QA, UAT, and Prod via pipelines. '
            'During go-live rehearsal, an ad-hoc UAT form edit masked Managed v3.2 changes, and two bi-directional flows between Dataverse and CTMS '
            'entered an infinite update loop burning 500,000 daily API requests.'
        ),
    },
    3: {
        'StratosWing Aerospace': (
            'StratosWing Aerospace runs Dynamics 365 Supply Chain Management (`F&O`) alongside Dynamics 365 Sales & Power Platform for 1,400 defense suppliers. '
            'Near-real-time customer/quote synchronization between F&O and Dataverse is mandatory, while ITAR export-controlled drawings '
            'require defense-in-depth DLP, Customer Lockbox, and Entra Conditional Access.'
        ),
        'Kinetix Heavy Equipment': (
            'Kinetix Heavy Equipment supports 4,500 independent franchise dealerships submitting warranty claims and ordering parts. '
            'Dealership managers must see all claims filed by any technician at their own dealership (`Account` hierarchy) without seeing rival dealers, '
            'and legacy AS/400 warranty green screens still lack REST APIs.'
        ),
        'Vortex Turbine Aftermarket': (
            'Vortex Turbine Aftermarket executives demand unified analytics combining 1.2M Dataverse service orders with 8 TB of historical turbine sensor parquet files. '
            'Operational leads also want embedded contextual Power BI visuals filtered by the user’s Dataverse security role directly inside Model-driven forms '
            'without granting direct SQL table access.'
        ),
        'IronPeak Plant Rollout': (
            'IronPeak Plant Rollout is 72 hours from cutting over 6,000 plant users onto a new Canvas + Model-driven quality suite. '
            'Load testing revealed a Canvas gallery taking 28 seconds due to non-delegable `Filter(Search(...))` calls and N+1 `LookUp` formulas per row, '
            'plus background jobs interfering with final schema maintenance.'
        ),
    },
    4: {
        'MetroCivic Permitting Authority': (
            'MetroCivic Permitting Authority is replacing 22 siloed Access spreadsheets and paper zoning forms across 8 city departments. '
            'Stakeholders initially demanded "replicate every legacy 45-tab screen verbatim by next month." '
            'The Solution Architect must lead discovery, NFR capture, future-state process standardization, and MVP fit/gap scoping.'
        ),
        'Valor Disaster Relief Agency': (
            'Valor Disaster Relief Agency experiences 50x traffic surges within 2 hours of hurricane landfalls as 500,000 citizens apply for emergency grants. '
            'Backend grant verification must decouple public intake bursts from fragile legacy state mainframes, '
            'enforce strict RPO <= 15m / RTO <= 2h BCDR plans, and pool S2S API identities to avoid HTTP 429 limits.'
        ),
        'Keystone State Licensing': (
            'Keystone State Licensing discovered during a pre-go-live security review that makers built client-scoped Business Rules hiding SSNs and assumed '
            'API callers could no longer read SSNs, while a shared service account owned 100% of custom connector actions hiding individual user audit trails '
            'against an internal OAuth 2.0 registry API.'
        ),
        'CivicPulse Transit Network': (
            'CivicPulse Transit Network connects Power Platform cloud flows and Dataverse plug-ins to an on-premises fare-clearing SQL cluster over Azure ExpressRoute. '
            'Network architects asked whether ExpressRoute alone places Dataverse inside their private RFC1918 LAN without VNet integration or gateways, '
            'and Solution Checker flagged critical `RetrieveAllEntities` calls inside synchronous plug-ins.'
        ),
    },
    5: {
        'Luminary Luxury Retail': (
            'Luminary Luxury Retail operates 600 boutiques across EMEA, Americas, and APAC with clienteling associates using mobile apps on store Wi-Fi. '
            'VIP client profiles are Organization-wide reference records vs regional `User/Team` clienteling notes, '
            'and regional marketing leads occasionally co-sell on flagship VIP accounts without changing primary BU ownership.'
        ),
        'FreshBasket Grocery Chain': (
            'FreshBasket Grocery Chain processes 900,000 daily store-audit photos and PDF cold-chain receipts across 1,100 supermarkets. '
            'Storing raw 8 MB photos inside relational Dataverse columns exhausted expensive Database capacity within 60 days. '
            'Architects must redesign file/blob offloading, retention policies, and AI Builder receipt automation.'
        ),
        'OmniCart Fulfillment Hub': (
            'OmniCart Fulfillment Hub integrates Power Platform order exception handling with 12 third-party 3PL carrier webhooks and an ERP warehouse system. '
            'Out-of-order webhook deliveries (`Shipped` arriving before `Packed`) and duplicate carrier retries caused stale state overwrites in Dataverse '
            'until architects introduced optimistic concurrency (`ETag` / row version) and ordered messaging.'
        ),
        'Solstice Peak Commerce': (
            'Solstice Peak Commerce freezes schema changes two weeks before Black Friday and validates go-live readiness across 18 microservices and 9 Power Platform solutions. '
            'Architects are wiring Azure Application Insights (`dependencies`/`exceptions` KQL) to Dataverse & Canvas apps, '
            'sizing Power Platform Request add-ons, and resolving a circular dependency between two Managed Solutions.'
        ),
    },
    6: {
        'GridVantage Transmission': (
            'GridVantage Transmission manages 140,000 high-voltage transmission towers inspected by helicopter and ground crews using Dynamics 365 Field Service & Power Apps. '
            'Crews need Reusable PCF geospatial map controls across both Model-driven and Canvas screens, '
            'hierarchical asset rollups (`Substation -> Feeder -> Tower`), and SAP PM work-order synchronization.'
        ),
        'EcoLedger Carbon Exchange': (
            'EcoLedger Carbon Exchange tracks immutable carbon-credit retirement certificates across multinational corporate buyers, external verifiers, and internal traders. '
            'Auditors require tamper-evident audit retention, separation of duties via Microsoft Entra Privileged Identity Management (PIM), '
            'and zero unapproved SaaS exfiltration across 14 environments using CoE Starter Kit + Managed Environments.'
        ),
        'ApexGrid M&A Integration': (
            'Following an acquisition, ApexGrid M&A Integration must merge an acquired utility’s standalone Dataverse CRM (containing dirty duplicate customer TINs '
            'and conflicting option-set integer codes) into ApexGrid’s global Power Platform tenant while keeping legacy SCADA green-screen apps running via Hosted RPA + Work Queues.'
        ),
        'Boreal Hydro Operations': (
            'Boreal Hydro Operations experienced severe afternoon slowdowns in Production Model-driven views after going live with 18 million meter-ticket rows. '
            'Telemetry revealed wildcard `*4491` Quick Find searches scanning 14 unindexed text columns, 6 synchronous post-update plug-ins chaining external HTTP calls, '
            'and unmanaged hotfixes blocking emergency pipeline deployments.'
        ),
    },
}
