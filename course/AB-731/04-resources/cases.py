"""Case-study scenarios for the AB-731 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Fabrikam Retail', """
Fabrikam Retail runs 300 stores plus an online business, with sales history in a warehouse and merchandising decisions taken weekly.
Store operations wants next quarter's demand per store from three years of transactions, and the buying team wants 400 seasonal policy questions answered on the returns portal.
The merchandising team edits the assistant prompt every week and cannot say whether answers improved.
Marketing budget is under review, so every capability has to justify its cost against a defined business outcome.
""")

c('Northwind Insurance', """
Northwind Insurance processes 20,000 supplier invoices a month as PDFs and employs a claims shared service of 120 people.
The claims assistant answers from a policy library that is revised quarterly, and adjusters have seen it invent a clause when nothing relevant was retrieved.
Twelve thousand notifications a month are routine, while 600 cases need genuine judgement.
The claims director wants automation where volume is high and human attention where the consequence is a payment decision.
""")

c('Contoso Health', """
Contoso Health is a hospital group with a clinical workforce of 14,000 and a Microsoft 365 tenant used for rosters and HR administration.
A workforce assistant will answer from HR files that include individual salary letters alongside policy documents.
The quality team also wants a triage assistant that recommends which patients receive a follow-up call, where an error changes clinical priority.
Copilot is due to be enabled across clinical SharePoint sites next month, and permissions have not been reviewed for years.
""")

c('Adatum Bank', """
Adatum Bank is a retail and commercial bank with 22,000 staff and a procurement function that handles 9,000 supplier contracts.
A procurement assistant summarizes uploaded contracts, and one supplier document contained text instructing the model to ignore its rules.
Separately, a screening assistant shortlisted candidates for branch roles, and the review found it favoured one demographic.
The bank is also about to pilot an assistant that will affect how credit applications are prioritized, and group risk wants that assessed before launch.
""")

c('Cedar Ridge Health', """
Cedar Ridge Health is a regional hospital network with 900 beds and a clinical documentation backlog.
Discharge teams need a plain-language summary of each stay written from clinician notes, and the audit team reads 400 pages per case to find decisions, dates, and follow-ups.
The laboratory service receives results and consent forms as scans and must post named fields into the record system.
Clinicians will only accept output they can check, so the design has to keep the source visible and a person accountable.
""")

c('Brookfield Clinics', """
Brookfield Clinics is a primary care network of 45 practices serving 300,000 patients.
It needs a patient FAQ assistant within a month and has no annotated dataset, while the scheduling team handles 9,000 rescheduling requests a month and rarely reaches the clinical queue.
The assistant still quotes a guideline that was withdrawn two months ago, and the medical director has flagged that as the single biggest risk.
Anything that touches patient contact has to sit inside the protected tenant boundary.
""")

c('BioNova Labs', """
BioNova Labs is a life-sciences organisation with a research library, a grants office, and a shared laboratory estate.
The strategy group needs a cited review of published approaches to virtual wards, drawn from many public sources.
A department wants a step-by-step equipment request process that writes into the asset system, and the group needs one relevance-ranked index of protocols that several assistants can query.
Anything customer-facing or clinical has to be reviewed by the scientific director before release.
""")

c('CareFirst Payer', """
CareFirst Payer is a health insurer covering 1.8 million members with a large analytics estate.
Its readmission model performs measurably worse for members whose first language is not English, and the medical director wants that addressed before any expansion.
The payer also wants to pilot an assistant that summarizes behavioural-health consultations, which raises consent and retention questions.
For enablement, 12,000 staff need protected chat, but only 800 need the full in-app experience.
""")

c('Kingsmere Bank', """
Kingsmere Bank is a mid-sized bank with a credit function, a compliance help desk, and a payments operation.
The credit committee must digest 200 pages per application and only needs the exposure, covenants, and exceptions.
Fifteen thousand staff ask the compliance desk the same 300 questions every month, and the bank processes 30,000 routine payment investigations alongside 300 complex fraud cases.
The regulator has asked how the bank documents model limits, so every capability needs a defensible rationale.
""")

c('Silverline Insurance', """
Silverline Insurance handles motor and property claims across four countries.
The claims operation receives 90,000 forms a month as scans and must post policy numbers and amounts into the claims system.
Thirty thousand adjuster notes consistently use a legally reviewed tone the insurer must preserve, and the motor team must verify that photographed damage matches the submitted vehicle details.
Assessors make the settlement decision, and the insurer will not delegate that to a model.
""")

c('Aurelian Capital', """
Aurelian Capital is an investment manager with a trading desk, a research team, and a risk function.
The trading desk's assistant bill doubled after three teams started using it, and no one can attribute the increase to a team or a task.
Retrieval misses exact instrument codes that appear in queries but finds conceptually similar documents instead.
The fraud model validated at 95 percent on last year's cases and underperforms on this year's, and the model risk committee wants to understand why.
""")

c('Fairgate Payments', """
Fairgate Payments is a payments processor serving 4,000 merchant clients across Europe.
Its investment committee spends 90 minutes after each meeting reconstructing decisions and owners.
The complaints team answers 500 regulatory letters a month, and each must open with the right acknowledgement before any substantive response.
A disputes agent must check a transaction in the core banking system before it replies, and the team wants that action governed rather than improvised.
""")

c('Calder Works', """
Calder Works operates a steel plant with four furnaces and a quality function that handles returns from automotive customers.
The plant wants to predict the yield of each furnace batch from five years of process measurements, and quality must route each returned component into one of seven disposition codes before an engineer reviews it.
The safety team writes 400 incident reports a month, each of which must follow the same regulatory structure.
Every assistant on site has to keep a qualified person accountable for any decision that affects production or safety.
""")

c('Helios Energy', """
Helios Energy runs 240 wind turbines across three sites and maintains a controlled procedure library.
The operator wants early warning of turbine behaviour that differs from two years of normal operation.
Field technicians must confirm that a safety instruction came from the current procedure before acting on it, and three revisions of the same lockout procedure currently coexist in the library.
The engineering director has made clear that a wrong instruction is a safety incident, not a quality defect.
""")

c('Northline Logistics', """
Northline Logistics is a freight forwarder handling customs clearance and last-mile distribution.
The control tower must apply a fixed customs rule set and route each exception to the right desk, and the distributor receives 50,000 delivery notes a month as scans that must be posted into the ERP.
Retrieval currently returns whole 80-page equipment manuals, so answers cite the wrong section.
Customs rules change by jurisdiction, and the operations director wants the reasoning behind each routed exception to be checkable.
""")

c('Vantage Motors', """
Vantage Motors is a commercial vehicle manufacturer with a field-service network of 200 engineers.
A field engineer must read 300 pages of maintenance history before each site visit, and the dispatch assistant must answer within two seconds during the 6 a.m. shift change.
The engineering team needs an agent that answers from the maintenance manual and opens a work order in the CMMS.
Any advice that affects a vehicle's roadworthiness has to be traceable to an approved procedure.
""")

c('Harborview Permits', """
Harborview Permits is a city licensing service handling planning, parking, and trade permits.
The council receives 70,000 resident enquiries a month and must route each one to the right service team.
A planning inspector must read 500 pages per application and only needs the objections, dates, and conditions, while the revenue office receives 30,000 paper forms a month that must be posted into the billing system.
Residents can appeal any decision, so every answer given to them has to be defensible and reviewable.
""")

c('Metro Transit', """
Metro Transit operates a metropolitan bus and rail network with four years of tap-in data.
The authority must forecast weekday passenger numbers for service planning, and its parking service needs a step-by-step permit process that writes to the permits system.
The meeting service needs searchable transcripts and captions for recorded board sessions.
Anything published to the public must meet accessibility standards and must not expose personal travel data.
""")

c('Rowan University', """
Rowan University is a large public university with an admissions office, a progression board, and 30,000 students.
The university wants a plain-language explanation of each applicant's progression decision, and it holds 18,000 edited admissions letters that consistently follow its approved wording.
The student assistant keeps chat transcripts indefinitely, including details about disabilities.
Students can request their records, so retention and disclosure have to be decided before the assistant scales.
""")

c('Ashford Library', """
Ashford Library is a state library service with 60 branches and a digitized archive.
The service needs a catalogue assistant within a month and has no annotated data, while the archive holds 40 years of scanned minutes that return almost no answers even though the pages exist.
A policy team is researching how other countries regulate short-term rentals and needs cited public sources.
The library answers to a public-records law, so anything retained has to be discoverable and defensible.
""")

c('Kestrel Group', """
Kestrel Group is a diversified group with nine brands, a shared services centre, and 40,000 employees.
The centre routes 200,000 supplier emails a month, applies fixed payment-terms policy, and drafts replies, while the group holds 30,000 policy pages that answer the same questions in every brand.
The group bill rose fourfold in one quarter and no business unit can explain its share.
Group counsel also requires one consistent legal disclaimer across brands, which each brand has so far written for itself.
""")

c('Brightpath Services', """
Brightpath Services is a professional services firm with an audit practice, an executive committee, and 3,000 consultants.
The audit function must read 800 pages per entity and only needs the exceptions and their owners.
The executive committee loses an hour after each meeting reconstructing decisions and owners, and procurement needs an agent that answers from the category handbook and opens a sourcing request in the ERP.
The firm's clients require evidence of who saw which AI-generated advice about their engagement.
""")

c('Highline Foods', """
Highline Foods is a food manufacturer operating in four markets with a large customer-service function.
The group holds 50,000 edited customer letters that consistently use its approved multilingual tone.
Every recommendation in its planning pack must end with risk, owner, and date, but the model keeps writing prose instead of that structure.
The finance analyst works from a 120,000-row consolidation file and must explain a margin movement to the board.
""")

c('Fairhaven Mutual', """
Fairhaven Mutual is a mutual insurer with a general counsel, a shared services function, and a three-year-old churn model.
General counsel will only accept an answer that can be checked against the source clause.
Shared services leadership accepts an assistant that prepares decisions but not one that makes them.
Nobody can state which data trained the churn model, when it was last validated, or whether it still beats the campaign targeting it replaced.
""")
