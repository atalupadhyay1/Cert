"""Case-study scenarios for the AB-620 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Contoso Field Service', """
Contoso Field Service built a Copilot Studio agent for 1,200 engineers who close about nine thousand jobs a week.
The agent must read the work order from an on-premises scheduling system that cannot accept inbound connections, and it must raise the parts request through a REST service that already has an OpenAPI definition.
Engineers sign in with Microsoft Entra ID, and the parts service must apply each engineer's own entitlement rather than a shared account.
Contoso promotes every change through development, test, and production, and the service desk wants a rolling measure of whether answers are still correct.
""")

c('Meridian Claims', """
Meridian Claims handles 40,000 motor claims a year and answers adjuster questions from a 60,000-document policy library in SharePoint.
Access is governed by claim team, and an adjuster must never see wording from another team's library, even when the wording is otherwise identical.
Adjusters also ask analytical questions such as which repairers exceeded their average cycle time last quarter.
Meridian runs three environments and needs to prove that a prompt change did not lower answer quality before it reaches production.
""")

c('Fabrikam Maintenance', """
Fabrikam Maintenance supports 300 technicians who still use a Windows desktop application for asset history, and the vendor will not publish an API this year.
The agent must open that application, look up an asset, and read the last five service events.
Technicians work from a shared workshop tablet that is signed in as the shift, not as an individual.
Fabrikam wants a supervisor to approve any parts order over 5,000 before the order is created.
""")

c('Northwind Commerce', """
Northwind Commerce runs a product-support agent on its public website for 90,000 monthly visitors, and the same agent is published inside Microsoft Teams for staff.
Product documentation lives in 12,000 pages across two SharePoint libraries and a legacy service that exposes only Power Platform connectors.
The staff experience must respect internal permissions while the public experience must answer only from published content.
Northwind ships weekly and wants a test set that runs on every deployment stage.
""")

c('Harborview Clinics', """
Harborview Clinics runs a scheduling assistant for 40 practices and answers questions about appointment policy.
Policy text lives in Dataverse and is updated weekly by practice managers, and the assistant must use the new wording the next morning.
The assistant must never give clinical advice, and questions outside scheduling are handed to a person.
Harborview wants the practice managers to see why an answer was refused.
""")

c('Tailwind Logistics', """
Tailwind Logistics built a shipment-status agent that answers from a Dataverse table of consignments and a Power Platform connector to the carrier network.
Drivers ask in short, misspelled sentences from a mobile app, and dispatchers ask the same questions inside Teams with a consignment number.
The carrier connector is throttled at 200 calls a minute, and a burst must degrade into a queued answer rather than an error.
Tailwind has four regions and a single production environment.
""")

c('Woodgrove Insurance', """
Woodgrove Insurance is replacing a call-centre script tool with a Copilot Studio agent for 700 agents.
The agent must quote policy wording from 8,000 documents and check the caller against an on-premises policy administration system.
Regulators require that every quoted sentence can be traced to the exact document version.
Woodgrove also wants a measured answer to whether the agent reduced average handling time.
""")

c('Alpine Retail Group', """
Alpine Retail Group runs a store-operations agent across 420 stores in three countries.
Store managers ask about opening procedures, promotions, and stock transfers, and the promotions change every Thursday.
Region managers need figures from a Fabric semantic model rather than document text.
Alpine wants one agent per country with shared behaviour, so a fix in one country does not have to be repeated three times.
""")

c('Beacon Financial', """
Beacon Financial built an advisor-support agent that reads 30,000 pages of product and compliance material.
Compliance insists that the agent refuse rather than improvise when the material does not contain an answer, and that every refusal is logged.
Advisors are licensed per product line, and the agent must not surface material for a line the advisor is not licensed to sell.
Beacon releases monthly and must show the regulator a tested, repeatable deployment process.
""")

c('Portside Utilities', """
Portside Utilities runs a field-outage agent for 250 engineers across a coastal region.
The agent must read outage tickets from an on-premises system, check the live network status through a REST API, and create a follow-up work order.
Storm days produce six times the normal volume, and the network API starts returning throttling responses.
Portside wants to know within minutes when a dependency starts failing.
""")

c('Litware Manufacturing', """
Litware Manufacturing runs a quality agent across four plants, each with its own line terminology.
Engineers ask how to handle a defect and expect the answer to cite the current standard.
Standard documents are revised quarterly, and the plant quality managers must be able to publish a revision without a developer.
Litware also wants a small evaluation set that runs whenever a standard changes.
""")

c('Salish Education', """
Salish Education runs a student-services agent for 30,000 students across three campuses.
It answers questions about enrolment, fees, and timetables from a student information system reached through Power Platform connectors.
Some answers include personal data, and a student must only ever see their own record.
Salish publishes to a public website and inside Microsoft Teams, and the two surfaces must behave identically.
""")

c('Kestrel Support', """
Kestrel Support runs a first-line support agent for a software vendor with 4,000 business customers.
The agent resolves password, licence, and billing questions from a knowledge base of 6,000 articles, and escalates the rest to a live agent.
Billing answers come from an API that occasionally returns a schema the agent has not seen.
Kestrel wants evidence that a new model does not increase escalations.
""")

c('Cobalt Bank', """
Cobalt Bank runs a treasury agent that must never act without a human decision.
Analysts ask about settlement status, and the agent can prepare a payment instruction but cannot submit it.
The settlement system sits in a locked-down network and exposes only a SOAP endpoint through an internal gateway.
Cobalt promotes changes through a pipeline and keeps the previous version for rollback.
""")

c('Trellis Media', """
Trellis Media runs a campaign agent for 200 account managers.
Campaign briefs, brand rules, and past performance sit in three different systems, and managers expect one answer that cites all three.
A brand rule change must take effect the same day.
Trellis wants to know which answers account managers rated badly, with the conversation attached.
""")

c('Redwood Public Works', """
Redwood Public Works runs a permit-status agent for residents and for internal reviewers.
Residents ask anonymously, and reviewers ask inside Teams with a case number.
Permit status comes from an on-premises system that must stay off the public internet.
The department must be able to show, for any answer, which record was read and by whom.
""")

c('Granite Health', """
Granite Health runs a referral agent for 60 clinics.
The agent summarizes referral packets, checks the patient's coverage through an API, and drafts a response for a clinician to approve.
Clinicians will not accept an agent that sends anything without their approval.
Granite must also prove that a model change did not alter how often the draft needed editing.
""")

c('Solstice Energy', """
Solstice Energy runs a grid-maintenance agent for 500 engineers and contractors.
Contractors are external identities, and they may see maintenance procedures but not incident reports.
The agent answers from a SharePoint library and an Azure AI Search index built from 200,000 procedure pages.
Solstice releases quarterly and reviews sample conversations every month.
""")

c('Northgate Bank', """
Northgate Bank is consolidating 14 department agents into one parent agent.
Each department keeps its own specialized agent, owned by a different team with its own release cycle.
The parent must route by intent and must not answer a compliance question itself.
Northgate wants a single place to see routing failures across the departments.
""")

c('Brightwater Water', """
Brightwater Water runs a leak-report agent for 1.2 million customers on a public website and a phone-adjacent chat channel.
Reports create a work order through a REST API, and the customer must be told the reference number immediately.
The API is rate-limited and occasionally unavailable during storms.
Brightwater wants to know how often the agent could not create a work order and why.
""")

c('Lakeshore Library', """
Lakeshore Library runs a catalogue agent across 40 branches.
It answers from a bibliographic index in Azure AI Search and from a lending system behind a connector.
Branches have different opening hours, and a branch change must take effect without a deployment.
The library measures success by how many questions are answered without a phone call.
""")

c('Skyline Transit', """
Skyline Transit built a service agent for 3 million passengers.
It answers disruption questions from a live operations feed and a policy library of 1,400 pages.
The operations feed fails several times a day, and passengers must still get a useful answer.
Skyline must also decide whether a cheaper model keeps answer quality acceptable.
""")

c('Evergreen University', """
Evergreen University runs an admissions agent for 80,000 applicants.
The agent answers questions about requirements, deadlines, and document status from a student information system.
Applicants are external users with no tenant account, and some answers include personal data.
The admissions office revises policy twice a year and needs to test the agent before each revision reaches applicants.
""")

c('Atlas Distribution', """
Atlas Distribution runs a supplier agent for 900 suppliers.
The agent answers questions about purchase orders, invoices, and delivery windows from Dataverse and a supplier portal API.
Suppliers must see only their own records, and the identity model must work for external accounts.
Atlas runs five environments and promotes changes through a pipeline with an approval before production.
""")
