# AB-620 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Contoso Field Service

Contoso Field Service built a Copilot Studio agent for 1,200 engineers who close about nine thousand jobs a week. The agent must read the work order from an on-premises scheduling system that cannot accept inbound connections, and it must raise the parts request through a REST service that already has an OpenAPI definition. Engineers sign in with Microsoft Entra ID, and the parts service must apply each engineer's own entitlement rather than a shared account. Contoso promotes every change through development, test, and production, and the service desk wants a rolling measure of whether answers are still correct.

Questions in this block

1. The scheduling system refuses all inbound connections from the cloud. Which integration should the plan use for it? _(A)_
2. The parts service publishes an OpenAPI definition and must authorise each engineer individually. Which two steps connect it correctly? Select two. _(A, C)_
3. Development, test, and production each point at a different parts endpoint. What should carry the endpoint in the solution? _(D)_

### Case study — Fabrikam Maintenance

Fabrikam Maintenance supports 300 technicians who still use a Windows desktop application for asset history, and the vendor will not publish an API this year. The agent must open that application, look up an asset, and read the last five service events. Technicians work from a shared workshop tablet that is signed in as the shift, not as an individual. Fabrikam wants a supervisor to approve any parts order over 5,000 before the order is created.

Questions in this block

1. Fabrikam Maintenance technicians use a Windows desktop application that will have no API this year, and the agent must read asset history from it. Which capability fits? _(A)_
2. Approval is required before any parts order above the threshold is raised. What should the flow do? _(A)_
3. The desktop application sometimes takes too long to open, and the run currently ends with no message to the technician. Which change gives a usable outcome? _(D)_

### Case study — Meridian Claims

Meridian Claims handles 40,000 motor claims a year and answers adjuster questions from a 60,000-document policy library in SharePoint. Access is governed by claim team, and an adjuster must never see wording from another team's library, even when the wording is otherwise identical. Adjusters also ask analytical questions such as which repairers exceeded their average cycle time last quarter. Meridian runs three environments and needs to prove that a prompt change did not lower answer quality before it reaches production.

Questions in this block

1. Meridian Claims keeps 60,000 policy documents in SharePoint, governed by claim team membership. Which knowledge route preserves that access control? _(C)_
2. Meridian needs retrieval limited to the adjuster's claim team even when two teams hold identical wording. Where must that restriction be applied? _(D)_
3. Meridian must score 900 answers after each prompt change and show the result before production. Which method fits? _(B)_

### Case study — Northwind Commerce

Northwind Commerce runs a product-support agent on its public website for 90,000 monthly visitors, and the same agent is published inside Microsoft Teams for staff. Product documentation lives in 12,000 pages across two SharePoint libraries and a legacy service that exposes only Power Platform connectors. The staff experience must respect internal permissions while the public experience must answer only from published content. Northwind ships weekly and wants a test set that runs on every deployment stage.

Questions in this block

1. Northwind publishes the same agent to public visitors and to staff, and staff answers must respect internal permissions. What must the design enforce? _(A)_
2. The content is split across two indexed libraries and one system reachable only through connector operations. Which two routes fit? Select two. _(B, D)_
3. Northwind ships weekly, and acceptance evidence must be comparable between releases. What should be done with the test set? _(D)_

## Exam 2

### Case study — Alpine Retail Group

Alpine Retail Group runs a store-operations agent across 420 stores in three countries. Store managers ask about opening procedures, promotions, and stock transfers, and the promotions change every Thursday. Region managers need figures from a Fabric semantic model rather than document text. Alpine wants one agent per country with shared behaviour, so a fix in one country does not have to be repeated three times.

Questions in this block

1. Region managers want sales figures that match the finance semantic model exactly. Which approach answers that? _(B)_
2. One agent per country must share the same refund behaviour so a fix is made once. What should be built? _(B)_
3. Country agents move through stages before release. Which two controls supply release evidence? Select two. _(A, C)_

### Case study — Harborview Clinics

Harborview Clinics runs a scheduling assistant for 40 practices and answers questions about appointment policy. Policy text lives in Dataverse and is updated weekly by practice managers, and the assistant must use the new wording the next morning. The assistant must never give clinical advice, and questions outside scheduling are handed to a person. Harborview wants the practice managers to see why an answer was refused.

Questions in this block

1. Practice managers need to see why the assistant refused a question and what it said at the time. Which capability provides that evidence? _(B)_
2. Before release, Harborview must show that refusals were judged appropriate rather than merely counted. Which method gives defensible evidence? _(D)_
3. A patient asks for dosing advice and the scheduling content holds nothing relevant. Which behaviour must the answer configuration enforce? _(C)_

### Case study — Tailwind Logistics

Tailwind Logistics built a shipment-status agent that answers from a Dataverse table of consignments and a Power Platform connector to the carrier network. Drivers ask in short, misspelled sentences from a mobile app, and dispatchers ask the same questions inside Teams with a consignment number. The carrier connector is throttled at 200 calls a minute, and a burst must degrade into a queued answer rather than an error. Tailwind has four regions and a single production environment.

Questions in this block

1. Consignments come from Dataverse, and carrier status comes from connector operations that are throttled. Which route supplies the carrier status? _(A)_
2. Under a burst the carrier connector starts throttling. Which two flow behaviours keep the conversation honest? Select two. _(B, D)_
3. Drivers type short, misspelled sentences from a phone. Which test material matters most before release? _(D)_

### Case study — Woodgrove Insurance

Woodgrove Insurance is replacing a call-centre script tool with a Copilot Studio agent for 700 agents. The agent must quote policy wording from 8,000 documents and check the caller against an on-premises policy administration system. Regulators require that every quoted sentence can be traced to the exact document version. Woodgrove also wants a measured answer to whether the agent reduced average handling time.

Questions in this block

1. Callers must be checked against a policy administration system that stays inside the data centre. Which integration should be planned? _(C)_
2. Every quoted sentence must be traceable to an exact document version. What must the index carry? _(B)_
3. The business case rests on average handling time after launch. What should be tracked? _(A)_

## Exam 3

### Case study — Beacon Financial

Beacon Financial built an advisor-support agent that reads 30,000 pages of product and compliance material. Compliance insists that the agent refuse rather than improvise when the material does not contain an answer, and that every refusal is logged. Advisors are licensed per product line, and the agent must not surface material for a line the advisor is not licensed to sell. Beacon releases monthly and must show the regulator a tested, repeatable deployment process.

Questions in this block

1. Compliance requires that every refusal is logged with the question that triggered it. What should be enabled? _(C)_
2. Some advisors hold a licence for only one product line. Where must that restriction be applied to retrieved material? _(A)_
3. The regulator asks how the team knows answers are supported by the source material. Which measure answers that? _(B)_

### Case study — Litware Manufacturing

Litware Manufacturing runs a quality agent across four plants, each with its own line terminology. Engineers ask how to handle a defect and expect the answer to cite the current standard. Standard documents are revised quarterly, and the plant quality managers must be able to publish a revision without a developer. Litware also wants a small evaluation set that runs whenever a standard changes.

Questions in this block

1. Four plants share one defect-handling behaviour but need different endpoints. Which two practices apply? Select two. _(A, D)_
2. Quality standards live in a SharePoint library whose site permissions must keep applying. Which route fits? _(A)_
3. Standards are revised quarterly by quality managers. Which two controls protect answer quality? Select two. _(B, D)_

### Case study — Portside Utilities

Portside Utilities runs a field-outage agent for 250 engineers across a coastal region. The agent must read outage tickets from an on-premises system, check the live network status through a REST API, and create a follow-up work order. Storm days produce six times the normal volume, and the network API starts returning throttling responses. Portside wants to know within minutes when a dependency starts failing.

Questions in this block

1. During storms the network API starts failing and the team learns days later. What should be added? _(C)_
2. The work-order API response must be reshaped and retried before the agent uses it. Where should the call live? _(C)_
3. Storm days produce six times the normal volume and unusual requests. What should the test set include? _(B)_

### Case study — Salish Education

Salish Education runs a student-services agent for 30,000 students across three campuses. It answers questions about enrolment, fees, and timetables from a student information system reached through Power Platform connectors. Some answers include personal data, and a student must only ever see their own record. Salish publishes to a public website and inside Microsoft Teams, and the two surfaces must behave identically.

Questions in this block

1. Some answers contain personal data, and the agent must only ever show a student their own record. Which identity decision fits? _(A)_
2. The same agent must serve students from a public website and from Microsoft Teams. Which channel pair does the case describe? _(D)_
3. Two surfaces must behave identically, and every change is compared against the last release. What should the test set be? _(D)_

## Exam 4

### Case study — Cobalt Bank

Cobalt Bank runs a treasury agent that must never act without a human decision. Analysts ask about settlement status, and the agent can prepare a payment instruction but cannot submit it. The settlement system sits in a locked-down network and exposes only a SOAP endpoint through an internal gateway. Cobalt promotes changes through a pipeline and keeps the previous version for rollback.

Questions in this block

1. The agent may prepare a payment instruction but never submit one without a decision. Which pattern fits? _(D)_
2. The settlement system sits in a locked network and exposes only an internal SOAP endpoint. Which integration fits? _(D)_
3. Releases need per-stage settings and a quick reversal. Which two controls apply? Select two. _(B, E)_

### Case study — Kestrel Support

Kestrel Support runs a first-line support agent for a software vendor with 4,000 business customers. The agent resolves password, licence, and billing questions from a knowledge base of 6,000 articles, and escalates the rest to a live agent. Billing answers come from an API that occasionally returns a schema the agent has not seen. Kestrel wants evidence that a new model does not increase escalations.

Questions in this block

1. A password question returns an article from the billing library because the node searches everything. What should change? _(D)_
2. The billing API sometimes returns fields the agent has never seen, and the answer becomes raw JSON. What should be added? _(B)_
3. Escalation rates must be compared across model changes. What should the test set be? _(D)_

### Case study — Redwood Public Works

Redwood Public Works runs a permit-status agent for residents and for internal reviewers. Residents ask anonymously, and reviewers ask inside Teams with a case number. Permit status comes from an on-premises system that must stay off the public internet. The department must be able to show, for any answer, which record was read and by whom.

Questions in this block

1. The department must show which record was read for any answer. What should be enabled? _(D)_
2. Permit data must never be queried over the public internet. What should be configured? _(A)_
3. Answer-quality findings have no owner and never become changes. What should be introduced? _(B)_

### Case study — Trellis Media

Trellis Media runs a campaign agent for 200 account managers. Campaign briefs, brand rules, and past performance sit in three different systems, and managers expect one answer that cites all three. A brand rule change must take effect the same day. Trellis wants to know which answers account managers rated badly, with the conversation attached.

Questions in this block

1. Briefs, brand rules, and performance data sit in three systems with different access models. Which two routes fit? Select two. _(D, E)_
2. One brand-rule dialogue must serve three campaign agents and change once. What should be built? _(A)_
3. Account managers rate answers badly, and the team wants the transcript with the rating. What should be added? _(D)_

## Exam 5

### Case study — Brightwater Water

Brightwater Water runs a leak-report agent for 1.2 million customers on a public website and a phone-adjacent chat channel. Reports create a work order through a REST API, and the customer must be told the reference number immediately. The API is rate-limited and occasionally unavailable during storms. Brightwater wants to know how often the agent could not create a work order and why.

Questions in this block

1. The work-order API is unavailable during storms and the conversation ends silently. What should the flow provide? _(B)_
2. Storms produce unusual requests and six times the volume. What should the test set include? _(D)_
3. Success is measured by work orders created without a phone call. What should the team track on a dashboard? _(D)_

### Case study — Granite Health

Granite Health runs a referral agent for 60 clinics. The agent summarizes referral packets, checks the patient's coverage through an API, and drafts a response for a clinician to approve. Clinicians will not accept an agent that sends anything without their approval. Granite must also prove that a model change did not alter how often the draft needed editing.

Questions in this block

1. A clinician must approve and send every referral response personally. Which pattern fits? _(D)_
2. The coverage API must apply each clinician's rights and expose named fields. Which two controls apply? Select two. _(B, E)_
3. Granite must show that draft quality was judged by clinicians before release. Which method gives that evidence? _(C)_

### Case study — Northgate Bank

Northgate Bank is consolidating 14 department agents into one parent agent. Each department keeps its own specialized agent, owned by a different team with its own release cycle. The parent must route by intent and must not answer a compliance question itself. Northgate wants a single place to see routing failures across the departments.

Questions in this block

1. Fourteen department behaviours share common logic but need different endpoints. Which two practices apply? Select two. _(B, E)_
2. Fourteen department agents are being consolidated under one parent. What should each department keep? _(B)_
3. Routing failures are reported one at a time across departments. What should the parent team do? _(C)_

### Case study — Solstice Energy

Solstice Energy runs a grid-maintenance agent for 500 engineers and contractors. Contractors are external identities, and they may see maintenance procedures but not incident reports. The agent answers from a SharePoint library and an Azure AI Search index built from 200,000 procedure pages. Solstice releases quarterly and reviews sample conversations every month.

Questions in this block

1. Contractors outside the tenant need their own sign-in to reach the agent. Which identity decision fits? _(C)_
2. Contractors may read maintenance procedures but not incident reports in the same library. What must be enforced? _(A)_
3. The procedure index must never return an incident report to a contractor. Where must that be enforced? _(D)_

## Exam 6

### Case study — Atlas Distribution

Atlas Distribution runs a supplier agent for 900 suppliers. The agent answers questions about purchase orders, invoices, and delivery windows from Dataverse and a supplier portal API. Suppliers must see only their own records, and the identity model must work for external accounts. Atlas runs five environments and promotes changes through a pipeline with an approval before production.

Questions in this block

1. A supplier must only ever see its own purchase orders and invoices. What must the design enforce? _(D)_
2. The supplier portal API must apply each supplier's own access and return named fields. Which two controls apply? Select two. _(B, C)_
3. The agent must move through five environments. Which two packaging choices apply? Select two. _(B, C)_

### Case study — Evergreen University

Evergreen University runs an admissions agent for 80,000 applicants. The agent answers questions about requirements, deadlines, and document status from a student information system. Applicants are external users with no tenant account, and some answers include personal data. The admissions office revises policy twice a year and needs to test the agent before each revision reaches applicants.

Questions in this block

1. Applicants have no tenant account but must sign in to see their document status. Which identity decision fits? _(A)_
2. Document status comes from a student information system through connector operations. Which route fits? _(C)_
3. Policy is revised twice a year, and each revision must be tested before it reaches applicants. What should the pipeline include? _(B)_

### Case study — Lakeshore Library

Lakeshore Library runs a catalogue agent across 40 branches. It answers from a bibliographic index in Azure AI Search and from a lending system behind a connector. Branches have different opening hours, and a branch change must take effect without a deployment. The library measures success by how many questions are answered without a phone call.

Questions in this block

1. Forty branches share one catalogue dialogue that changes once a quarter. What should be built? _(B)_
2. The bibliographic index must filter by branch and return a citation. What should be designed first? _(C)_
3. A branch identifier change must take effect without rebuilding the agent. What should hold that value? _(A)_

### Case study — Skyline Transit

Skyline Transit built a service agent for 3 million passengers. It answers disruption questions from a live operations feed and a policy library of 1,400 pages. The operations feed fails several times a day, and passengers must still get a useful answer. Skyline must also decide whether a cheaper model keeps answer quality acceptable.

Questions in this block

1. The live operations feed fails several times a day and passengers see an error. What should the flow do? _(D)_
2. Disruption events produce unusual questions and traffic spikes. What should the test set include? _(B)_
3. When the feed is down the conversation simply stops, and the passenger is left waiting. What should the flow provide? _(C)_
