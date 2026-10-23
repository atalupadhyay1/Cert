"""Case-study scenarios for the PL-300 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Wingfield Retail', """
Wingfield Retail runs 420 stores and an e-commerce site on a SQL data warehouse, with franchisee sales arriving as monthly Excel files.
Commercial analytics owns a certified semantic model for net sales, and finance rejects any second definition of the number.
Sixty analysts build pages from that model, and the nightly refresh must finish before the 7 a.m. trading call.
Buying also wants evidence on supplier concentration, and the warehouse still stores one wide sales table with a text amount column.
""")

c('Proseware Health', """
Proseware Health operates nine hospitals and 140 clinics on a single clinical warehouse that refreshes nightly.
The reporting team built one wide encounter table that repeats patient region, clinic, and payer on every row, and filters have become slow.
Quality reporting needs year-to-date admissions that stay correct on days with no recorded activity, plus bed-days that describe capacity at a point in time.
The data office insists on one agreed definition of length of stay before any page is published.
""")

c('Litware Financial', """
Litware Financial reports for 240 branches across 12 regions, with a small analytics team and a single imported model.
Regional managers rank branches every Monday, and the executive page needs a reset control because readers keep leaving filters applied.
The monthly pack compares each branch against a cost-to-income target, and the current chart makes a good month look flat by starting the axis above zero.
Nobody in the team has time to restyle forty visuals for each brand refresh.
""")

c('Thornbury Consulting', """
Thornbury Consulting has 4,000 consultants, a sales pipeline inDataverse, and a finance system on an on-premises SQL Server.
Its reporting workspace will serve two very different audiences: sales staff who need pipeline pages and finance staff who need utilisation pages.
The model must refresh from the on-premises server, and exported files carry client rate cards that must stay protected after they leave the workspace.
The platform team is small, so anything that needs per-user maintenance will not be sustained.
""")

c('Pinecrest Clinics', """
Pinecrest Clinics is a 60-clinic network that reports admissions from a shared electronic record system.
The analytics team must use the clinical model the data office certifies, because a second definition of length of stay caused a board dispute last year.
Encounter rows arrive at patient level, but the operations review needs one row per clinician per month.
Clinic names sit in a lookup table keyed on a composite of site and clinic code, and the relationship must handle that shape.
""")

c('Harborline Grocers', """
Harborline Grocers operates 300 stores and runs more than 400 promotions a year, several of them across many stores at once.
Its visit table repeats store name, region, and district on every row, and category filters have slowed to a crawl.
The sales fact holds every basket line and is slow to summarize, yet merchandisers still need to reach transaction detail when a number looks wrong.
Promotion analysis needs a relationship that respects the many-to-many pattern between promotions and stores.
""")

c('Cambria Insurance', """
Cambria Insurance reports on 1.2 million policies, and the monthly board pack must explain how opening policy counts became closing counts.
The pack runs to four pages, all filtered to the same policy period, and readers keep re-applying that filter on every page.
The retention team also wants to understand which factors are associated with lapses and to ask ad hoc questions without waiting for another page to be built.
The model is imported and refreshes nightly from the policy administration system.
""")

c('Solstice Energy', """
Solstice Energy reports outage and meter data for 2.1 million supply points, refreshed from an operational system every two hours.
A small team of authors publishes the reports, while field crews need to read them on a phone without changing anything.
The board asks for a monthly PDF snapshot of the outage report, and the service account used for refresh has a credential that expires every 90 days.
The team has been caught twice by a refresh that failed silently overnight.
""")

c('Northgate Bank', """
Northgate Bank reports trading and balance data from a core system that cannot accept analyst queries.
One query combines client balances with payroll data, and the team is worried the engine is folding values between the two sources.
The branch identifier arrives as a region prefix and a branch number in separate fields, but the report needs one combined code.
The trade table repeats counterparty name, sector, and rating on every row, and filters on 40 million rows have become unusable.
""")

c('Fairmont Assurance', """
Fairmont Assurance reports claims and reserves for a regulated insurance book.
Reserve balances are captured at end of day, and the current report sums them across months, producing a peak that means nothing.
The operations team must publish the claim-processing time below which 95 percent of claims are settled, not the average.
The claims report is also subject to an accessibility review, because staff who use screen readers must be able to read it.
""")

c('Brightwater Utilities', """
Brightwater Utilities models 3 million meters and publishes a board page plus an audit view.
One free-text location column holds almost unique values, and it dominates the size of what is otherwise a modest model.
The board page must explain the movement from opening to closing revenue across the quarter and show progress against the annual target.
Internal audit needs to read the outage reports without being able to change them, and without joining the authoring workspace.
""")

c('Coastline Logistics', """
Coastline Logistics runs depot operations across three countries, with the depot management system on an on-premises server.
Six hundred depot staff must see only their own depot's deliveries in one shared report, and the org chart changes every few weeks.
The data team wants the delivery model certified so that other teams reuse it instead of building their own.
Refresh must run overnight, and the service cannot reach the depot server directly.
""")

c('Redwood Mills', """
Redwood Mills runs four paper mills and receives sensor extracts from a third-party contractor with no data dictionary.
The production table repeats machine name, line, and plant on every row, and slicers on the operations page have become slow.
Unit cost must multiply quantity by rate before it is summed, and the yield ratio has to survive a denominator of zero when a line is idle.
Nobody can say how complete the contractor's extract is, and the last feed silently changed two column types.
""")

c('Skyline Transit', """
Skyline Transit reports ridership, fare revenue, and service punctuality for a metropolitan network.
Rolling ridership totals skip days when no service ran, and the running figure resets in a way nobody can explain.
Fare-card balances are recorded only when a passenger tops up, so month-end often lands on a day with no record.
The operations team must publish the delay below which 90 percent of trips fall, and the current average hides the tail entirely.
""")

c('Evergreen University', """
Evergreen University reports admissions, progression, and course performance across five faculties.
The report runs to five pages, all filtered to the same intake year, and staff re-apply that filter on every page they open.
Faculty want a root-cause page that lets them explore any dimension in any order, plus a way to ask questions in their own words.
External accreditors must be able to read the reports without editing anything, and they must not see another faculty's data.
""")

c('Lakeshore Library', """
Lakeshore Library runs 32 branches and reports loans, visits, and programme attendance.
Every branch page must match the same palette and typeface, and nobody wants to style forty visuals by hand each time a branch is added.
The branch manager wants a notification when daily loans fall below plan, delivered without opening the report.
The circulation fact covers four years and must refresh inside a short overnight window, with only recent weeks changing.
""")

c('Summit Retail Group', """
Summit Retail Group operates ten departments across several banners and reports revenue, margin, and returns.
A category manager must compare revenue across the departments, and the current pie chart with ten slices is unreadable.
Readers want sales, margin, and returns together when they hover a product, without another visual taking space on the page.
Store managers must see only their own store in the shared group report, while buyers see everything.
""")

c('Willow Creek Health', """
Willow Creek Health is a clinic network reporting visits, charges, and encounter detail.
Visits arrive at line level, but the operations page needs one row per clinic per day and a charge column that behaves as a decimal.
The encounter fact stores every line even though most reporting looks at daily totals, and the model has grown far beyond what the pages need.
Readers work across six pages and keep losing the clinic-network selection as they move between them.
""")

c('Granite Public Works', """
Granite Public Works reports road, water, and parks maintenance for a municipal authority.
A contractor submits a works-order file with no documentation, and nobody can say whether it is complete or which values are placeholders.
Rolling works-order totals skip days when no crew was scheduled, and the running figure looks wrong to the finance team.
The dashboard is published to the public website, so it must be usable by screen-reader users and must not expose address-level detail.
""")

c('Aurora Schools', """
Aurora Schools reports attendance and attainment across 90 schools in a regional trust.
Schools must be grouped by attendance pattern without anyone defining the groups in advance, and the trust wants to see which schools behave alike.
The principal wants the weekly attendance report as an email snapshot on Monday morning.
The attendance model refreshes every three hours from a cloud source, and the service account secret expires quarterly.
""")

c('Atlas Holdings', """
Atlas Holdings is a group of four businesses with different ERPs and one group data office.
The group analyst must report across all four using the model the data office certifies, because a second definition of group revenue is not acceptable.
A newly acquired business has just supplied its first extract, and nobody has inspected it.
Subsidiary transactions arrive at line level, but the consolidation needs one row per entity per month before it is loaded.
""")

c('Beacon Mutual', """
Beacon Mutual is a mutual insurer reporting group reserves, claims, and policy data.
Group reserve balances are captured at a point in time, and the current pack sums them across months into a meaningless peak.
The claims desk must publish the settlement time below which 90 percent of claims close, not an average that hides the tail.
Policy data is restricted: readers outside the actuarial function must not be able to download it from the report.
""")

c('Cedarline Foods', """
Cedarline Foods reports volume and revenue for four regional businesses and a group board.
The board must compare revenue across the regions, and the current chart mixes two measures on one axis.
Each region is measured against a volume plan, and the monthly chart has to show whether the plan was beaten without a second visual.
The commercial director wants the volume pack as an email snapshot on the first working day of the month.
""")

c('Pinnacle Services', """
Pinnacle Services is a professional services group with two business units that both keep their practice management system on premises.
The service cannot reach either system directly, and refresh has to run overnight for both.
Eight hundred consultants must see only their own engagements, and the mapping between person and engagement changes with every new project.
The group wants one engagement model certified so that every business unit reports margin the same way.
""")
