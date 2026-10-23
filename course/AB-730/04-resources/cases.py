"""Case-study scenarios for the AB-730 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Brightline Retail', """
Brightline Retail runs 210 stores and an online shop, and has just bought Microsoft 365 Copilot for 4,000 head-office and store-support staff.
The merchandising team keeps 1,900 planograms and supplier agreements in SharePoint, and site permissions have not been reviewed since a reorganization two years ago.
Category managers want a weekly summary of sales exceptions, while the legal team is worried that salary letters sit in the same document library as product guides.
The retail director wants the tool live before the peak season, which is six weeks away, and has asked for a plan that does not create a privacy incident.
""")

c('Harborview Claims', """
Harborview Claims is a regional insurer with 900 claims staff and a policy library of 12,000 documents that is revised every quarter.
Adjusters use Copilot to draft decision letters, and last month one letter quoted a clause that had been withdrawn, which the compliance team found during a sample review.
The claims director wants every generated letter checked before it is sent, and wants to know how to make that check fast enough for 3,000 letters a day.
A supplier has also uploaded a contract containing text that told the assistant to ignore its review rules.
""")

c('Cedar Health', """
Cedar Health is a hospital group with 11,000 clinical and administrative staff and a Microsoft 365 tenant shared with two partner clinics.
The workforce team wants to answer HR questions from policy documents while individual salary letters remain restricted to the people team.
Clinicians have started pasting patient summaries into Copilot prompts to shorten discharge letters, and the medical director has asked what should happen first.
The group also plans to enable Copilot on clinical SharePoint sites next month, and an access review has not been run for three years.
""")

c('Meridian Bank', """
Meridian Bank has 18,000 staff, a procurement function handling 7,000 supplier contracts a year, and a contact centre that answers 40,000 customer emails a month.
The bank wants Copilot to draft replies and summarize supplier risk, but group risk has refused to approve anything that could send customer data outside the tenant.
A pilot team has already built a custom agent on an unmanaged site, and the security team found it could answer from documents that ordinary staff cannot open.
The chief operating officer wants a single decision on what to enable this quarter and what has to wait.
""")

c('Larkspur Consulting', """
Larkspur Consulting is a 600-person advisory firm whose consultants work on four or five client engagements at once.
Each engagement has its own SharePoint site, a set of interview notes, and a deliverable deadline, and consultants rebuild the same context in chat every morning.
The firm has signed three client contracts that prohibit storing client content in any tool outside the client tenant, and the partners want the rule enforced in practice rather than in a policy document.
A junior consultant has been reusing one long chat for every client, and the quality lead cannot tell which source produced which recommendation.
""")

c('Wexford Legal', """
Wexford Legal is a 300-lawyer firm that drafts engagement letters, reviews supplier contracts, and prepares client briefings from large document sets.
The firm has 40,000 precedent documents in an on-premises system that Copilot cannot currently see, and partners want drafts grounded in those precedents rather than in general legal knowledge.
A client has asked for a cited review of case law, and the managing partner wants every citation opened by a lawyer before it reaches the client.
The firm also wants to stop each team inventing its own prompt wording for the same standard letter.
""")

c('Bluepeak Accounting', """
Bluepeak Accounting prepares audit files and management accounts for 1,200 small and mid-sized clients.
The audit team works across Word, Excel, and PowerPoint, and the same figures are restated in all three, which is where last year's review found most errors.
Partners want a pre-meeting brief before each client review and a reliable set of actions afterwards, and the operations director wants the weekly pipeline summary produced without anyone assembling it by hand.
The firm is also considering a custom agent for client onboarding, but no one has checked whether the standard Copilot experience already covers it.
""")

c('Halden Design', """
Halden Design is a 90-person brand and product studio that produces campaign concepts, imagery, and client presentations.
Designers generate images and mood boards with Copilot, and the studio has been asked by two clients to prove that generated assets do not breach usage rights or brand rules.
The studio works with freelancers who need access to project Pages but not to the client contract folder, and the studio manager wants collaboration to happen in one live document rather than in email attachments.
A new business team also wants a repeatable way to turn a discovery call into a creative brief.
""")

c('Calder Manufacturing', """
Calder Manufacturing runs three plants and a supply chain of 400 suppliers, with production, quality, and maintenance data spread across Excel workbooks and a legacy ERP.
Plant managers want Copilot to analyse downtime and produce charts for a Monday review, but the same asset is recorded with three different identifiers across the plants.
The quality director needs every generated figure reconciled with the source workbook before it reaches the operations board, and the board wants the weekly pack produced on a schedule rather than by request.
A maintenance team has also started experimenting with a custom agent that answers from machine manuals.
""")

c('Northline Freight', """
Northline Freight is a logistics operator with 2,500 drivers, 12 depots, and a customer service desk that handles 9,000 delivery exceptions a month.
Dispatchers want a multi-step assistant that can check a delivery, draft a customer update, and log the exception, and the operations director wants the plan reviewed before any customer message is sent.
The company has 30,000 delivery notes a month arriving as scans, and a customs rule set that changes by jurisdiction.
Drivers have been using Copilot on personal phones to summarize depot notices, which the transport manager has asked the security team to assess.
""")

c('Vantage Foods', """
Vantage Foods produces chilled meals for 700 retail stores and runs a quality team that handles supplier certificates, recall notices, and customer complaints.
The quality director wants a pre-meeting brief before each supplier review and an accurate record of decisions afterwards, because two recalls last year were traced to actions that were agreed but never logged.
Marketing wants Copilot to generate campaign images for a product launch, and the legal team wants the usage rights and brand rules checked before anything is published.
The company also wants a weekly summary of complaint trends, currently assembled by hand every Friday.
""")

c('Ironwood Energy', """
Ironwood Energy operates wind and solar assets across four regions and employs 1,400 people, many of them field engineers.
Engineers want Copilot to answer from maintenance manuals and work orders, and the asset director wants every answer to show which manual revision it came from.
The company has a regulatory obligation to retain records of maintenance decisions, and the legal team has asked how prompts and generated recommendations are stored.
A group of engineers has built a custom agent on a site that contains grid connection contracts, and the compliance team wants its access model reviewed before it is used more widely.
""")

c('Rowan Council', """
Rowan Council serves 300,000 residents and handles planning applications, social care case files, and freedom-of-information requests.
The council has bought Copilot for 2,200 staff, and the information governance team is worried about case files that contain personal data and about a statutory retention schedule that differs by record type.
Officers want help drafting committee briefs, and the monitoring officer wants every factual claim in a brief traced to a source before it is circulated to elected members.
The council also runs public consultations where responses arrive as long documents that need to be summarized without losing the substance of objections.
""")

c('Ashford University', """
Ashford University has 24,000 students, 3,500 staff, and a research office that manages grant applications and ethics approvals.
The university wants Copilot to help academics draft ethics submissions and summarize literature, and the research director wants citations checked by an academic before anything is submitted to a funder.
Student records sit in a separate system that Copilot cannot currently reach, and the registry wants a connector that respects the same access rules as the student system.
The library also wants a shared Notebook for each faculty research panel, so that analyses do not restart from a different source set each month.
""")

c('Metro Transit', """
Metro Transit operates 90 stations and 1,800 vehicles, and its operations team runs a daily control room with a shift handover at 06:00 and 18:00.
Shift supervisors want a reliable summary of what happened during the previous shift, and the operations director wants decisions and owners captured rather than buried in a transcript.
The agency holds safety investigation records that must be retained for seven years, and the legal team has asked where generated summaries are stored and for how long.
A pilot group has started using Copilot in meetings, and the accessibility team has asked that generated recap content be usable by staff who cannot attend live.
""")

c('Lakeshore Library', """
Lakeshore Library serves a city of 800,000 people through 40 branches and a large digital collection.
The library wants a public-facing assistant to answer questions about opening hours, borrowing rules, and programme schedules, while staff want Copilot to summarize community feedback and draft funding applications.
The digital collection includes licensed content whose terms restrict copying, and the library director wants the assistant grounded only in content the library is allowed to reuse.
A branch manager has proposed a custom agent that answers from local history archives, and the governance group wants to know how it would be kept accurate and who would own it.
""")

c('Trellis Media', """
Trellis Media is a digital publisher with 250 journalists, a subscriber base of 400,000, and a content archive going back 20 years.
Editors want Copilot to draft headlines, summarize interviews, and produce social variants, while the standards editor wants every published claim checked against the original source.
The archive sits in a third-party system that is not indexed by Microsoft 365, and the product team wants search and grounding to include it without copying 20 years of content into SharePoint.
The company also wants an image workflow that produces campaign visuals without breaching photographer contracts.
""")

c('Brightpath Agency', """
Brightpath Agency is a 120-person marketing agency that runs campaigns for 15 clients and produces a high volume of presentations, social copy, and creative concepts.
Account teams rebuild client context for every request, and the agency principal wants a repeatable way to start from a proven prompt rather than yesterday's chat.
Clients have asked for evidence that generated assets follow brand guidelines, and one client requires that no campaign material leave its own tenant.
The agency also wants a weekly summary of social listening themes, currently produced by an analyst every Monday morning.
""")

c('Solstice Foundation', """
Solstice Foundation is a grant-making charity with 180 staff, 900 active grants, and an application cycle that peaks twice a year.
Programme officers want help summarizing applications, drafting assessment notes, and preparing board papers, and the trustees want every claim in a board paper traced to an application or a report.
The foundation has a duty to retain grant decisions for ten years, and the finance team wants a clear answer on whether generated text counts as a record.
A regional team has created an agent that answers from applicant guidance, and the governance lead wants to know who is responsible for its accuracy after the guidance changes.
""")

c('Kestrel Events', """
Kestrel Events runs conferences and trade shows, with a team of 60 staff and up to 400 suppliers per event.
The operations team plans each event in a sequence of dependent steps, from venue booking to speaker confirmation to on-site logistics, and the managing director wants a plan reviewed before any supplier is committed.
Client calls produce decisions that are currently lost between the call and the brief, and the team wants a reliable way to turn a recorded call into agreed actions.
The company has also started generating event imagery for client proposals and needs to confirm rights before anything is sent.
""")

c('Highline Group', """
Highline Group is a diversified holding company with retail, logistics, and financial services divisions and 9,000 employees.
Each division has its own Microsoft 365 tenant data, its own risk appetite, and its own view of what Copilot should be allowed to do, and the group CIO has to approve one rollout plan.
The group has a regulatory obligation to retain certain records, a privacy programme that classifies data into four tiers, and a board that wants evidence of value before funding a wider rollout.
An internal audit has found three custom agents built without an owner, and the CIO wants a standard decision path for tools, prompts, and agents.
""")

c('Fairhaven Financial', """
Fairhaven Financial is a wealth manager with 1,300 staff and 60,000 client accounts.
Advisers want Copilot to summarize client meetings and draft follow-up letters, and compliance has ruled that no advice-related content may be produced without a named adviser reviewing it.
Client records include sensitive personal data, and the data protection officer wants prompts and outputs covered by the existing retention schedule.
The firm is also running an eight-week pilot of a delegated multi-step workflow that prepares a quarterly client review pack, and the head of operations wants checkpoints before any client-facing document is issued.
""")

c('Evergreen Pharma', """
Evergreen Pharma is a mid-sized pharmaceutical company with a research library, a medical affairs team, and a regulatory affairs group.
Medical affairs wants a cited review of published evidence for a product dossier, and regulatory affairs wants every statement in a submission traced to an approved source.
The company operates in a regulated environment where promotional content is reviewed before use and where certain documents must be retained for decades.
A research team has started experimenting with a custom agent that answers from internal study reports, and the compliance officer wants its sources and access model documented before it is shared.
""")

c('Atlas Distribution', """
Atlas Distribution is a wholesale distributor with 6,000 employees, 40 warehouses, and a customer service organisation that handles 25,000 orders and 4,000 exceptions a day.
The company is consolidating three legacy systems and wants Copilot to help staff find answers across contracts, operational procedures, and order history.
The CIO wants one decision framework for choosing between Copilot Chat, a prebuilt agent, a custom agent, and a delegated Cowork task, because different teams have started building in parallel.
Customer contracts include clauses that restrict where data may be processed, and the legal team wants that constraint reflected in what the assistants are allowed to use.
""")
