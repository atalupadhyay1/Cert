# PL-300 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Litware Financial

Litware Financial reports for 240 branches across 12 regions, with a small analytics team and a single imported model. Regional managers rank branches every Monday, and the executive page needs a reset control because readers keep leaving filters applied. The monthly pack compares each branch against a cost-to-income target, and the current chart makes a good month look flat by starting the axis above zero. Nobody in the team has time to restyle forty visuals for each brand refresh.

Questions in this block

1. A regional manager must rank twelve branches by revenue. Which visual fits? _(A)_
2. Readers need a reset control that restores the default filters and visible visuals. What should be captured? _(C)_
3. A trend chart must show whether each month beat the target cost-to-income percentage. What should be added? _(D)_

### Case study — Proseware Health

Proseware Health operates nine hospitals and 140 clinics on a single clinical warehouse that refreshes nightly. The reporting team built one wide encounter table that repeats patient region, clinic, and payer on every row, and filters have become slow. Quality reporting needs year-to-date admissions that stay correct on days with no recorded activity, plus bed-days that describe capacity at a point in time. The data office insists on one agreed definition of length of stay before any page is published.

Questions in this block

1. A single encounter table repeats patient region, clinic, and payer on every row, and slicers are slow. What should be built? _(C)_
2. Year-to-date admission totals skip days when no activity was recorded, and the running figure resets oddly. What is missing? _(C)_
3. Bed-days available is being summed across months and shows a meaningless peak. What should the measure do instead? _(D)_

### Case study — Thornbury Consulting

Thornbury Consulting has 4,000 consultants, a sales pipeline inDataverse, and a finance system on an on-premises SQL Server. Its reporting workspace will serve two very different audiences: sales staff who need pipeline pages and finance staff who need utilisation pages. The model must refresh from the on-premises server, and exported files carry client rate cards that must stay protected after they leave the workspace. The platform team is small, so anything that needs per-user maintenance will not be sustained.

Questions in this block

1. One app must show sales pages to sales staff and finance pages to finance staff. What should be configured? _(C)_
2. The model refreshes from an on-premises SQL Server that the cloud service cannot reach. What is required? _(D)_
3. Exported files must retain their protection after they leave the workspace. What should be applied? _(A)_

### Case study — Wingfield Retail

Wingfield Retail runs 420 stores and an e-commerce site on a SQL data warehouse, with franchisee sales arriving as monthly Excel files. Commercial analytics owns a certified semantic model for net sales, and finance rejects any second definition of the number. Sixty analysts build pages from that model, and the nightly refresh must finish before the 7 a.m. trading call. Buying also wants evidence on supplier concentration, and the warehouse still stores one wide sales table with a text amount column.

Questions in this block

1. A new analyst must build a sales report without creating a second definition of net sales. Which action fits? _(B)_
2. A buying manager asks whether order values are dominated by a few large suppliers. Which evidence answers that? _(C)_
3. A transactional sales table must become one row per store per day, and the sales column must be numeric. Which two steps are required? Select two. _(C, E)_

## Exam 2

### Case study — Cambria Insurance

Cambria Insurance reports on 1.2 million policies, and the monthly board pack must explain how opening policy counts became closing counts. The pack runs to four pages, all filtered to the same policy period, and readers keep re-applying that filter on every page. The retention team also wants to understand which factors are associated with lapses and to ask ad hoc questions without waiting for another page to be built. The model is imported and refreshes nightly from the policy administration system.

Questions in this block

1. The board pack must explain how opening policy counts became closing counts across the month. Which visual fits? _(B)_
2. A chosen policy period must stay applied while readers move across four pages of the report. What should be configured? _(D)_
3. The team wants the factors associated with lapses and a way for managers to ask ad hoc questions. Which two features fit? Select two. _(A, B)_

### Case study — Harborline Grocers

Harborline Grocers operates 300 stores and runs more than 400 promotions a year, several of them across many stores at once. Its visit table repeats store name, region, and district on every row, and category filters have slowed to a crawl. The sales fact holds every basket line and is slow to summarize, yet merchandisers still need to reach transaction detail when a number looks wrong. Promotion analysis needs a relationship that respects the many-to-many pattern between promotions and stores.

Questions in this block

1. The visit table repeats store name, region, and district on every row, and filters are slow. What should be built? _(B)_
2. Promotions run across many stores and stores run many promotions, with a promotion-store table between them. Which relationship shape is required? _(C)_
3. The sales fact is slow to summarize but must stay available at transaction level. Which two actions fit? Select two. _(D, E)_

### Case study — Pinecrest Clinics

Pinecrest Clinics is a 60-clinic network that reports admissions from a shared electronic record system. The analytics team must use the clinical model the data office certifies, because a second definition of length of stay caused a board dispute last year. Encounter rows arrive at patient level, but the operations review needs one row per clinician per month. Clinic names sit in a lookup table keyed on a composite of site and clinic code, and the relationship must handle that shape.

Questions in this block

1. The analytics team must report on admissions without creating a second definition of length of stay. Which action fits? _(C)_
2. Encounter rows must become one row per clinician per month before loading. What should be used? _(D)_
3. The fact table must gain clinic name, and the relationship will be built on a composite of site and clinic codes. Which two choices fit? Select two. _(B, E)_

### Case study — Solstice Energy

Solstice Energy reports outage and meter data for 2.1 million supply points, refreshed from an operational system every two hours. A small team of authors publishes the reports, while field crews need to read them on a phone without changing anything. The board asks for a monthly PDF snapshot of the outage report, and the service account used for refresh has a credential that expires every 90 days. The team has been caught twice by a refresh that failed silently overnight.

Questions in this block

1. Authors must publish and edit reports, and field crews must read without editing. Which two roles fit? Select two. _(B, C)_
2. A board member wants a PDF snapshot of the outage report every month. What should be configured? _(A)_
3. The meter model must refresh every two hours, and the service account credential expires every 90 days. Which two settings matter? Select two. _(B, C)_

## Exam 3

### Case study — Brightwater Utilities

Brightwater Utilities models 3 million meters and publishes a board page plus an audit view. One free-text location column holds almost unique values, and it dominates the size of what is otherwise a modest model. The board page must explain the movement from opening to closing revenue across the quarter and show progress against the annual target. Internal audit needs to read the outage reports without being able to change them, and without joining the authoring workspace.

Questions in this block

1. The meter model is dominated by one text column with almost unique values. What should be done? _(A)_
2. The board page must explain the movement from opening to closing revenue and show progress against target. Which two visuals fit? Select two. _(B, D)_
3. Internal audit must read the outage reports without editing them. Which role fits? _(B)_

### Case study — Coastline Logistics

Coastline Logistics runs depot operations across three countries, with the depot management system on an on-premises server. Six hundred depot staff must see only their own depot's deliveries in one shared report, and the org chart changes every few weeks. The data team wants the delivery model certified so that other teams reuse it instead of building their own. Refresh must run overnight, and the service cannot reach the depot server directly.

Questions in this block

1. The depot extract lives on an on-premises server that the service cannot reach. What is required? _(B)_
2. Six hundred depot users must be filtered by a mapping table rather than one role per person. What should be used? _(C)_
3. One delivery model should become the standard that other teams can trust. What should be done? _(C)_

### Case study — Fairmont Assurance

Fairmont Assurance reports claims and reserves for a regulated insurance book. Reserve balances are captured at end of day, and the current report sums them across months, producing a peak that means nothing. The operations team must publish the claim-processing time below which 95 percent of claims are settled, not the average. The claims report is also subject to an accessibility review, because staff who use screen readers must be able to read it.

Questions in this block

1. End-of-day reserve balances are being summed across months and producing a meaningless peak. What should the measure do? _(C)_
2. The operations team must state the claim-processing time below which 95 percent of claims are settled. What should be used? _(D)_
3. The claims report must be usable by screen-reader users, and its visuals carry no descriptions. What must be added? _(D)_

### Case study — Northgate Bank

Northgate Bank reports trading and balance data from a core system that cannot accept analyst queries. One query combines client balances with payroll data, and the team is worried the engine is folding values between the two sources. The branch identifier arrives as a region prefix and a branch number in separate fields, but the report needs one combined code. The trade table repeats counterparty name, sector, and rating on every row, and filters on 40 million rows have become unusable.

Questions in this block

1. The query combines client balances with payroll data, and the engine is folding values between the two sources. Which setting stops that? _(B)_
2. The branch identifier is split across region and number, and the report needs one combined code. What should be added? _(D)_
3. The trade table repeats counterparty name, sector, and rating on every row, and filters lag. What should be built? _(A)_

## Exam 4

### Case study — Evergreen University

Evergreen University reports admissions, progression, and course performance across five faculties. The report runs to five pages, all filtered to the same intake year, and staff re-apply that filter on every page they open. Faculty want a root-cause page that lets them explore any dimension in any order, plus a way to ask questions in their own words. External accreditors must be able to read the reports without editing anything, and they must not see another faculty's data.

Questions in this block

1. A chosen intake year must stay applied across five pages of the report. What should be configured? _(A)_
2. A root-cause page must explore any dimension in any order, and faculty want to type questions. Which two features fit? Select two. _(B, C)_
3. External accreditors must read the reports but must not change them. Which role fits? _(D)_

### Case study — Lakeshore Library

Lakeshore Library runs 32 branches and reports loans, visits, and programme attendance. Every branch page must match the same palette and typeface, and nobody wants to style forty visuals by hand each time a branch is added. The branch manager wants a notification when daily loans fall below plan, delivered without opening the report. The circulation fact covers four years and must refresh inside a short overnight window, with only recent weeks changing.

Questions in this block

1. Every branch page must share one palette and font without individual styling. What should be applied? _(A)_
2. The branch manager must be notified when daily loans fall below plan. What should be created? _(B)_
3. The circulation fact spanning four years must refresh within the overnight window. Which two steps are required? Select two. _(B, D)_

### Case study — Redwood Mills

Redwood Mills runs four paper mills and receives sensor extracts from a third-party contractor with no data dictionary. The production table repeats machine name, line, and plant on every row, and slicers on the operations page have become slow. Unit cost must multiply quantity by rate before it is summed, and the yield ratio has to survive a denominator of zero when a line is idle. Nobody can say how complete the contractor's extract is, and the last feed silently changed two column types.

Questions in this block

1. A contractor supplies a sensor extract with no documentation, and its quality is unknown. What should be done first? _(D)_
2. The production table repeats machine name, line, and plant on every row, and slicers drag. What should be built? _(B)_
3. Unit cost must multiply quantity by rate before summing, and the yield ratio must survive a zero denominator. Which two functions fit? Select two. _(D, E)_

### Case study — Skyline Transit

Skyline Transit reports ridership, fare revenue, and service punctuality for a metropolitan network. Rolling ridership totals skip days when no service ran, and the running figure resets in a way nobody can explain. Fare-card balances are recorded only when a passenger tops up, so month-end often lands on a day with no record. The operations team must publish the delay below which 90 percent of trips fall, and the current average hides the tail entirely.

Questions in this block

1. Rolling ridership totals skip days when no service ran, and the running figure looks wrong. What is missing? _(C)_
2. Fare-card balance is recorded only when a top-up occurs, so month-end lands on a blank day. What should be used? _(C)_
3. The operations team must state the delay below which 90 percent of trips fall. What should be used? _(A)_

## Exam 5

### Case study — Aurora Schools

Aurora Schools reports attendance and attainment across 90 schools in a regional trust. Schools must be grouped by attendance pattern without anyone defining the groups in advance, and the trust wants to see which schools behave alike. The principal wants the weekly attendance report as an email snapshot on Monday morning. The attendance model refreshes every three hours from a cloud source, and the service account secret expires quarterly.

Questions in this block

1. Schools must be segmented by attendance pattern without a predefined scheme. What should be used? _(A)_
2. The principal wants the weekly attendance report as an email snapshot. What should be configured? _(D)_
3. The attendance model must refresh every three hours, and the service account secret expires quarterly. Which two settings matter? Select two. _(A, D)_

### Case study — Granite Public Works

Granite Public Works reports road, water, and parks maintenance for a municipal authority. A contractor submits a works-order file with no documentation, and nobody can say whether it is complete or which values are placeholders. Rolling works-order totals skip days when no crew was scheduled, and the running figure looks wrong to the finance team. The dashboard is published to the public website, so it must be usable by screen-reader users and must not expose address-level detail.

Questions in this block

1. A contractor sends a works-order file with no documentation, and its completeness is unknown. What should be done first? _(C)_
2. Rolling works-order totals skip days when no crew was scheduled, and the running figure looks wrong. What is missing? _(B)_
3. The public works dashboard must be usable by screen-reader users, and its visuals carry no descriptions. What must be added? _(B)_

### Case study — Summit Retail Group

Summit Retail Group operates ten departments across several banners and reports revenue, margin, and returns. A category manager must compare revenue across the departments, and the current pie chart with ten slices is unreadable. Readers want sales, margin, and returns together when they hover a product, without another visual taking space on the page. Store managers must see only their own store in the shared group report, while buyers see everything.

Questions in this block

1. A category manager must compare revenue across ten departments of the group. Which visual fits? _(A)_
2. A hover must show sales, margin, and returns together without adding visuals to the page. Which two actions deliver that? Select two. _(D, E)_
3. Store managers must see only their own store's rows in one shared group report. What should be created? _(B)_

### Case study — Willow Creek Health

Willow Creek Health is a clinic network reporting visits, charges, and encounter detail. Visits arrive at line level, but the operations page needs one row per clinic per day and a charge column that behaves as a decimal. The encounter fact stores every line even though most reporting looks at daily totals, and the model has grown far beyond what the pages need. Readers work across six pages and keep losing the clinic-network selection as they move between them.

Questions in this block

1. A visit table must become one row per clinic per day, and the charge column must be decimal. Which two steps are required? Select two. _(B, C)_
2. The encounter fact stores every line, but the report only ever looks at daily totals. What should be done? _(D)_
3. A chosen clinic network must stay applied across six report pages. What should be configured? _(C)_

## Exam 6

### Case study — Atlas Holdings

Atlas Holdings is a group of four businesses with different ERPs and one group data office. The group analyst must report across all four using the model the data office certifies, because a second definition of group revenue is not acceptable. A newly acquired business has just supplied its first extract, and nobody has inspected it. Subsidiary transactions arrive at line level, but the consolidation needs one row per entity per month before it is loaded.

Questions in this block

1. The group analyst must report across four businesses using the model the data office certifies. What should the analyst do? _(C)_
2. A newly acquired business supplies an extract nobody has inspected, and its quality is unknown. What should be done first? _(D)_
3. Subsidiary transaction rows must become one row per entity per month before loading. What should be used? _(C)_

### Case study — Beacon Mutual

Beacon Mutual is a mutual insurer reporting group reserves, claims, and policy data. Group reserve balances are captured at a point in time, and the current pack sums them across months into a meaningless peak. The claims desk must publish the settlement time below which 90 percent of claims close, not an average that hides the tail. Policy data is restricted: readers outside the actuarial function must not be able to download it from the report.

Questions in this block

1. Group reserve balances are being summed across months and producing a meaningless peak. What should the measure do? _(B)_
2. The claims desk must state the settlement time below which 90 percent of claims close. What should be used? _(B)_
3. Policy data must not be downloaded by readers outside the actuarial function. What should be configured? _(C)_

### Case study — Cedarline Foods

Cedarline Foods reports volume and revenue for four regional businesses and a group board. The board must compare revenue across the regions, and the current chart mixes two measures on one axis. Each region is measured against a volume plan, and the monthly chart has to show whether the plan was beaten without a second visual. The commercial director wants the volume pack as an email snapshot on the first working day of the month.

Questions in this block

1. The board must compare revenue across its four regional businesses. Which visual fits? _(D)_
2. A monthly chart must show whether each region beat its volume plan. What should be added? _(A)_
3. The commercial director wants the volume pack as an email snapshot on the first working day. What should be configured? _(D)_

### Case study — Pinnacle Services

Pinnacle Services is a professional services group with two business units that both keep their practice management system on premises. The service cannot reach either system directly, and refresh has to run overnight for both. Eight hundred consultants must see only their own engagements, and the mapping between person and engagement changes with every new project. The group wants one engagement model certified so that every business unit reports margin the same way.

Questions in this block

1. Two business units keep their practice system on-premises and the service cannot reach either. What is required? _(C)_
2. Eight hundred consultants must be filtered by a mapping table rather than a role per person. What should be used? _(B)_
3. The group wants one engagement model to become the standard every business can trust. What should be done? _(D)_
