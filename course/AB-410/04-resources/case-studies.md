# AB-410 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Adatum Legal

Adatum Legal manages 40,000 matters across three regional practices. Each practice keeps its own intake spreadsheet, and partners cannot answer how many matters of a given type are open without asking an analyst. The firm is subject to an annual audit that requires proof of who changed a fee arrangement and when. Intake arrives by email, and a paralegal rekeys each matter into the system. The firm has Copilot Studio available but has never deployed an agent. Fee arrangements above a threshold need a second partner approval. Regional practice managers must see only their own region.

Questions in this block

1. A fee arrangement above a threshold must require a second partner field before saving. What should be configured? _(B)_
2. The fee amount must be hidden from assistants while the matter stays visible. What should be used? _(B)_
3. The audit asks who changed a fee arrangement and when. What must be enabled? _(A)_

### Case study — Fabrikam Manufacturing

Fabrikam Manufacturing has twelve plants and a quality team that owns the incident process. Operator reports arrive on paper at the end of each shift, and the quality manager transcribes them the next morning. A defect that recurs at three plants is invisible until someone notices the pattern by hand. Plant managers need a phone-friendly form, the quality team needs a desktop view with trends, and the corporate quality director wants a monthly package. The company runs Dataverse, has a premium Power Automate licence, and has asked for AI-generated incident summaries. There is a strict rule that plant staff may not see another plant's incidents.

Questions in this block

1. Each incident must get an AI summary stored on the record. What should be configured? _(A)_
2. Plant staff must see only their plant and must share one filtered list. Which two components apply? Select two. _(C, E)_
3. Operators report incidents from the plant floor on a handheld. Which layout fits? _(C)_

### Case study — Northwind Freight

Northwind Freight runs 1,800 daily shipments from six depots on a legacy dispatch system. Drivers report problems through phone calls, and depot supervisors rebuild the day on a whiteboard whenever weather closes a route. The operations director wants a single app for supervisors, an automated approval when a reroute costs more than 5,000 in local currency, and a weekly summary email. The company standardises on Dataverse, has one production environment, a development environment, and a test environment, and a governance team that reviews every release. Microsoft Copilot is licensed for all staff. Nothing is allowed to be built directly in production.

Questions in this block

1. Supervisors need the twelve fields they use without hunting. What should change? _(C)_
2. A reroute above 5,000 needs a recorded sign-off that pauses the process. Which two features apply? Select two. _(A, B)_
3. Supervisors have the app but see no depot records. What is missing? _(C)_

### Case study — Tailspin Toys

Tailspin Toys sells through 300 independent retailers and a small direct web store. Retailer orders arrive as emailed spreadsheets that two people reconcile by hand, and stock commitments are promised before the warehouse confirms them. The sales director wants retailer self-service for order status, an approval step when a discount exceeds the published band, and a warning when an order would take committed stock negative. The company has no dedicated developer, one maker who knows Power Apps well, and a compliance requirement that every discount decision be attributable to a named approver.

Questions in this block

1. The warehouse exposes a REST API behind a gateway. What should be built to call it? _(D)_
2. A discount band must come from an approved list and carry a currency. Which two column types apply? Select two. _(B, D)_
3. A discount beyond the published band needs a decision recorded against the order. What action fits? _(B)_

## Exam 2

### Case study — Contoso Real Estate

Contoso Real Estate lists 4,000 properties across five regions with photographs, inspections, and offers. Agents work from phones on site, and the back office works from desktops. Inspection reports are dictated and typed up days later, which delays listings. The marketing team wants AI-written listing descriptions reviewed by a person before publication. Every property has a responsible agent, and a regional manager must see every property in the region but may edit none of them. Offers above the asking price need a manager approval.

Questions in this block

1. Agents want a listing page drafted from a description. What should be used? _(C)_
2. Agents capture inspections on a phone at the property. Which layout fits? _(D)_
3. Listing data must sit in its own governed boundary. What decides the environment? _(B)_

### Case study — Litware Health

Litware Health operates 22 clinics and a central scheduling team. Patient intake is collected on paper, and clinic staff rekey it into a booking system that has no mobile interface. The clinical director wants a phone app for intake that works on poor connectivity, a desktop app for the scheduling team, and an automated reminder sequence. Patient contact details are regulated, and the compliance team requires field-level control over the national identifier. The organisation has Dataverse, Power Apps per-user licences, and a governance policy that forbids custom code in the first release.

Questions in this block

1. Clinic staff include a low-vision user on a tablet. What must be added? _(C)_
2. An appointment gallery must search a large table. What must the filter do? _(A)_
3. The national identifier must be hidden from reception staff. What should be used? _(B)_

### Case study — Proseware Consulting

Proseware Consulting sells fixed-fee engagements and tracks them in a dozen project spreadsheets. Partners want a single view of engagement profitability, computed from time entries and expenses, with the margin recalculated whenever a rate changes. Delivery managers need a weekly exception list of engagements running over budget. Finance needs a rollup of committed cost per client. The firm has Dataverse and Power BI, and its partners have asked repeatedly for a chatbot that answers questions about engagement status without training users on a new app.

Questions in this block

1. The same margin calculation appears on five screens. What should be used? _(D)_
2. Consultants shape a temporary set of engagements to sort in the app. What should be used? _(D)_
3. Partners want to ask about engagement status inside the app. What should be added? _(B)_

### Case study — Woodgrove Insurance

Woodgrove Insurance processes 12,000 claims a month through a claims centre and four regional offices. Adjusters record notes in a free-text field that has grown to a page per claim, and supervisors cannot tell which claims are stuck. Regulators require a claim decision to record the adjuster, the timestamp, and the information considered. The company wants an AI-generated summary of each claim for the supervisor view, a stage-based process with required information at each stage, and an approval when a settlement exceeds 25,000. Only the assigned adjuster may edit a claim; supervisors may read every claim in their region.

Questions in this block

1. Adjusters need the fields they use without scrolling. What should change? _(B)_
2. Supervisors can open the app but see no claims. What is missing? _(A)_
3. A long claim form must stay reachable and readable. Which two choices apply? Select two. _(A, B)_

## Exam 3

### Case study — Alpine Ski House

Alpine Ski House runs three resorts with seasonal staff, a central reservations team, and an equipment rental operation. Reservations arrive through a website, a call centre, and partner agencies, each in a different format. Peak season doubles the volume for eight weeks. Guests report equipment faults on paper forms that are collected nightly. The operations lead wants a unified reservation record, an automated equipment-fault workflow with a photo attachment, and a mobile app for the rental desk that works offline. The company has one production environment, no test environment, and a maker who has built canvas apps before but never a model-driven app.

Questions in this block

1. The resort group needs its own governed boundary. What decides the environment? _(D)_
2. Rental staff work from a handheld at the counter. Which layout fits? _(A)_
3. The fault workflow must run only for reported equipment faults. What should be added? _(D)_

### Case study — Blue Yonder Airlines

Blue Yonder Airlines manages crew availability across 60 aircraft and 1,200 crew. Crew members report unavailability by phone to a rostering team that maintains a spreadsheet, and a late change frequently leaves a flight without a qualified crew. The airline wants crew self-service on a phone, an approval when a change would break a qualification rule, and an alert when a flight has no qualified crew. Rostering data includes licence numbers that only the safety team may read. The airline has Copilot Studio and wants an agent that answers crew questions about their own roster.

Questions in this block

1. A qualification check takes two inputs and is called in several places. What should be used? _(C)_
2. Crew answers must cite the rostering rules. What should be attached? _(B)_
3. Two crew change types need different stages after the first. What should be used? _(C)_

### Case study — City of Riverside

The City of Riverside handles 60,000 service requests a year across parks, roads, and utilities. Residents report issues by phone and email, and the call centre rekeys each one. Departments cannot see each other's requests, so a pothole reported twice is worked twice. The city wants a public-facing form, internal routing by department, an escalation when a request is open beyond its service level, and a quarterly report for council. Personal data must be limited to what the department needs, and the city's security team requires role-based access with no exceptions.

Questions in this block

1. A department cannot see another department's requests. What partitions the data? _(D)_
2. A service-level list must be readable without opening each request. What must be chosen? _(C)_
3. An escalation above the service level needs a manager and then a director. What should be built? _(C)_

### Case study — Consolidated Courier

Consolidated Courier moves 90,000 parcels a day through 14 hubs. Hub supervisors track exceptions on clipboards, and the customer service team cannot tell a customer where a delayed parcel is without calling the hub. The company wants an exception record created from a scanner event, an automated customer notification when a parcel is delayed beyond a threshold, and a supervisor dashboard. The integration team insists that no custom connector be built in the first release. Parcel events arrive as JSON from the scanner platform.

Questions in this block

1. Each exception record needs an AI summary of the event. What should be configured? _(B)_
2. Customer service wants to ask about a parcel inside the app. What should be added? _(A)_
3. Scanner events arrive as JSON with no offered properties. What should be added? _(B)_

## Exam 4

### Case study — Coho Winery

Coho Winery sells to 900 restaurants and distributors across four states. Orders arrive by email and phone, and the sales team rebuilds a forecast every Monday from a spreadsheet. Distributor allocations are contested, and the winery promises volumes before bottling confirms them. The sales director wants a distributor portal, an allocation approval when a distributor requests more than its committed volume, and a weekly forecast view. The winery has Dataverse, a premium connector budget, and a two-person IT team that must support whatever is built. Nothing may be deployed without a test environment sign-off.

Questions in this block

1. A schema name must be right the first time. What must be decided before the first table? _(B)_
2. Sales reps check allocations on a phone in the field. Which layout fits? _(A)_
3. Order data lives in a premium-only service. What is justified? _(D)_

### Case study — Fourth Coffee

Fourth Coffee operates 140 cafés and a wholesale bean business. Store managers order supplies by phone to a central buyer, who keys the orders into a spreadsheet. Stockouts of the best-selling blend happen two or three times a month. The operations director wants a store ordering app, an approval when an order exceeds a store's monthly budget, a replenishment suggestion from recent sales, and a daily exception list of stores with an unfilled order. The company has one maker, Dataverse, and a policy that no store manager may see another store's financial data.

Questions in this block

1. The store manager's store must be available on every screen. What should be used? _(B)_
2. An order above the store budget needs a recorded decision. What action fits? _(A)_
3. The replenishment flow must run only for unfilled orders. What should be added? _(B)_

### Case study — Nod Publishers

Nod Publishers produces 1,500 titles a year and licenses content to libraries and retailers. Rights are tracked in contracts that live in three shared drives, and a title is occasionally sold in a territory where the rights have lapsed. The rights director wants a single rights record per title and territory, a warning when a deal would breach a lapsed right, an approval for exceptions, and a searchable view for the sales team. Contracts arrive as PDFs, and the team wants AI to extract the key terms into the rights record.

Questions in this block

1. Each rights record needs an AI summary of its contract terms. What should be configured? _(C)_
2. The rights form carries fields nobody uses. What should change? _(C)_
3. Extracted terms must be checked against the contract text. What should be attached? _(D)_

### Case study — Trey Research

Trey Research is a 400-person contract research organisation running 60 concurrent clinical studies. Study coordinators record participant visits on paper, and the quality team reconciles them monthly. A missed visit is a protocol deviation, so the sponsor requires evidence of every scheduled and completed visit. The organisation wants a coordinator app, an automated reminder, and a deviation record with an approval. Participant identifiers are sensitive, and the sponsor's auditors need read-only access to a study without seeing any other study.

Questions in this block

1. Two coordinators share one queue of visits. What should own the records? _(A)_
2. A coordinator list must show only today's scheduled visits. What decides that? _(D)_
3. A deviation must require a reason before it can be saved. What should be configured? _(C)_

## Exam 5

### Case study — Lakeshore Retail Group

Lakeshore Retail Group operates 60 stores and an e-commerce site. Customer service handles 5,000 contacts a month across phone, email, and chat, and agents cannot see a customer's order history without switching systems. The group wants a unified case record, an AI-drafted reply that an agent must review, a routing rule by contact reason, and a satisfaction survey after closure. The group has Copilot Studio, Dataverse, and a governance board that requires every AI feature to be reviewed before release.

Questions in this block

1. A case must point at its customer record. What should be added? _(A)_
2. Three apps share one service header. What should be used? _(B)_
3. AI-drafted replies must be affordable on every case. What should be chosen deliberately? _(C)_

### Case study — Margie Travel

Margie Travel books corporate travel for 200 client companies. Consultants email itineraries, and the finance team reconciles invoices against bookings by hand. Travellers need an approval before a booking above their policy limit, and clients want a portal showing their own bookings only. The agency has 40 staff, Dataverse, and a Power Automate premium licence. Consultants work from phones while travelling. The agency's insurer requires that every policy exception be recorded with the approver and the reason.

Questions in this block

1. Consultants must not see another client company's bookings. What partitions the data? _(B)_
2. Consultants book from phones while travelling. Which design obligation applies? _(B)_
3. A booking above the policy limit needs one named decision. Which approval type fits? _(C)_

### Case study — VanArsdel Manufacturing

VanArsdel Manufacturing builds industrial pumps to order. Each order runs through engineering review, costing, production, and shipping, and the handoffs happen by email. Costing frequently restarts because engineering changes a specification after the quote was issued. The operations director wants a stage-based order process with required fields, an approval when a costing change exceeds 10 percent, and a project dashboard. Engineering and costing are separate business units with separate managers. The company has Dataverse and has asked for an AI summary of each order's change history.

Questions in this block

1. An audit asks who changed a costing after the quote. What must be enabled? _(D)_
2. Users cannot find the costing area in the app. What should be configured? _(D)_
3. A costing change flow branches by change type. What should be used? _(C)_

### Case study — Wide World Importers

Wide World Importers distributes 8,000 SKUs to 3,000 retail accounts across two countries. Sales reps use a quoting spreadsheet that is emailed between the rep, the pricing team, and the customer. Quotes above a discount threshold need pricing approval, and reps frequently quote stock the warehouse does not hold. The company wants a rep app, an approval flow, a stock check against the warehouse system, and a quote PDF. The warehouse exposes a REST API behind a corporate gateway. The company is migrating from on-premises CRM to Dataverse and must keep historical quotes readable.

Questions in this block

1. Every rep must see the same open-quote list. What should be created? _(C)_
2. A quote queue must show only quotes awaiting pricing. What decides that? _(D)_
3. The warehouse API needs its own authentication. What should be built? _(B)_

## Exam 6

### Case study — Bellows College

Bellows College manages admissions for 18,000 applications a year across five faculties. Applications arrive through a portal as documents, and each faculty assesses with its own rubric. The registrar cannot produce a timely count of applications awaiting a decision. The college wants a reviewer app, a rubric per faculty, an approval when an offer is made below the published threshold, and a dashboard for the registrar. Applicant data is personal and must be visible only to the reviewing faculty. The college has Dataverse and Copilot Studio, and a policy that no AI may make an admission decision.

Questions in this block

1. Applicant contacts must reuse the fields staff already know. What should be used? _(A)_
2. A rubric score calculation takes three inputs. What should be used? _(A)_
3. A rejection reason must be required before the decision saves. What should be configured? _(A)_

### Case study — Munson Sporting Goods

Munson Sporting Goods sells team equipment to schools and clubs. Orders peak in August and January, and the current process is a shared mailbox monitored by four people. Quotes are built in a spreadsheet, and approvals happen in email threads that nobody can audit after the season. The company wants an order app, an approval chain that varies by order value, a quote document, and a seasonal dashboard. The finance director requires that every discount be attributable and that no order be fulfilled without an approved quote. The company has Dataverse and Power Apps per-app licences.

Questions in this block

1. A school district must not see another district's orders. What partitions the data? _(A)_
2. A seasonal trend must reuse the existing view filter. What should be created? _(D)_
3. A forecast model must be called from the flow and stored on the order. What should be used? _(A)_

### Case study — Relecloud Telecom

Relecloud Telecom handles 30,000 service tickets a month. Field engineers record work on paper and call the dispatch desk when they finish, which delays the next job assignment. The company wants a field app that works offline, automatic dispatch of the next job, and a customer notification when an engineer is en route. Engineers must not see billing information. The company has premium connectors and a security team that reviews any connector that leaves the tenant.

Questions in this block

1. A field app must search a large job table. What must the filter do? _(A)_
2. Dispatchers want a daily board drafted from a description. What should be used? _(A)_
3. A response contains forty job rows to update individually. What should be used? _(D)_

### Case study — Tahoma Winery Group

Tahoma Winery Group owns four wineries and a distribution arm. Each winery tracks cellar operations in its own workbook, and the group cannot compare production across sites. The group wants a shared cellar-operations model, a winery app for cellar hands on tablets, an approval for any wine movement between sites, and a group dashboard. The wineries must not see each other's cost data. The group has Dataverse, a Power BI estate, and a governance policy that requires solutions to move through development, test, and production with an audited deployment.

Questions in this block

1. Four wineries must deploy the same solution repeatably. What should be used? _(C)_
2. Every cellar hand must see the same movement list. What should be created? _(C)_
3. Moving wine between sites needs a recorded decision. What action fits? _(B)_
