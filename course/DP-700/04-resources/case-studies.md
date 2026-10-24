# DP-700 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Adventure Works Cycles

Adventure Works Cycles sells bicycles through 900 dealers and a direct web store. Orders, returns, and inventory snapshots arrive nightly as CSV extracts from three regional ERPs, and the files land in an ADLS Gen2 container the company already owns. The data engineering team has built a lakehouse with bronze, silver, and gold layers, and analysts read the gold tables through the SQL analytics endpoint. A nightly run takes five hours and rewrites every table in full. The finance team has asked for order history that shows what the dealer price was on the day the order was placed, not what it is today. The platform team owns a single Fabric capacity and wants every deployment to be reproducible from source control.

Questions in this block

1. A release currently means exporting and importing items by hand. What should be created? _(B)_
2. Finance data must carry a classification that every consumer inherits. What should be applied? _(A)_
3. The restricted folder must stay unreadable to the analytics workspace and to its Contributors. Which two controls apply? Select two. _(D, E)_

### Case study — Contoso Energy

Contoso Energy operates 2.4 million smart meters and receives about 40,000 readings per second during peak hours. The readings must be queryable within two minutes of arrival for outage detection, and the regulator requires seven years of retention for daily aggregates. The company is moving from an on-premises time-series platform to Fabric Real-Time Intelligence. A separate batch process already loads billing data into a warehouse once a day. The data engineering team has one Fabric capacity and has been told not to add another. Meter identifiers arrive with occasional duplicates and readings sometimes arrive up to six hours late when a concentrator reconnects.

Questions in this block

1. Forty thousand readings per second must be queryable within two minutes. Where should they land? _(D)_
2. A regulator and a dashboard both read the same daily total. What should be created? _(D)_
3. A concentrator reconnects six hours late with readings already counted. What should be done? _(B)_

### Case study — Fabrikam Logistics

Fabrikam Logistics moves 60,000 parcels a day and receives a scan event from every depot gate. Events arrive through an event hub and are currently landed as JSON files that a nightly notebook parses. Operations wants a live board of parcels stuck at a depot for more than four hours, and the finance team wants a daily invoice line for each parcel by service level. Scans are occasionally duplicated when a gate retries, and a depot that loses connectivity can replay several hours of events in a burst. The company standardises on OneLake and has four workspaces: landing, engineering, analytics, and operations. Nothing may be copied into a second storage account.

Questions in this block

1. A depot gate retries and the same scan arrives twice. What should be applied? _(D)_
2. Operations wants a live board with no batch job in the path. What should be used? _(A)_
3. The daily invoice line is built from the landed events. What should be used? _(C)_

### Case study — Litware Retail

Litware Retail runs 320 stores and keeps its point-of-sale transactions in an Azure SQL database that the store systems write to directly. Analysts want near-real-time sales by store, and the finance team needs a governed monthly close that reconciles to the general ledger. The database team refuses to allow any read workload that competes with store transactions. Transaction rows can be corrected after the fact when a cashier voids a sale. The company has a Fabric capacity, a purview account, and a policy that all finance data must carry a sensitivity label. The engineering team has no licence for a second database and cannot enable change tracking on the source tables.

Questions in this block

1. The reconciliation query fails with a conversion error after a schema change. What identifies the fault? _(A)_
2. A failed load is discovered by the finance team the next morning. What should be configured? _(B)_
3. The month-end join slowed sharply as the volume grew. What should be updated first? _(D)_

## Exam 2

### Case study — Alpine Ski House

Alpine Ski House runs six resorts and a central analytics team. Each resort has its own workspace, and all six workspaces share one capacity. The engineering team has a development workspace, a test workspace, and a production workspace, and today a release means exporting items by hand and importing them again. Two resorts are on a different data source than the other four and must keep their own connection after any promotion. The team has just adopted Git and wants every change reviewed before it reaches production. A previous release overwrote a production parameter and pointed the nightly load at a test database for two days before anyone noticed.

Questions in this block

1. Every new notebook must inherit the approved libraries. What should be configured? _(B)_
2. Two resorts must keep their own connection after promotion. What should be configured? _(A)_
3. A release must be reviewable before it reaches production. What should be configured? _(B)_

### Case study — Northwind Traders

Northwind Traders imports specialty food from 40 suppliers and sells to 4,000 restaurants. The warehouse must hold a star schema with one fact table for order lines, conformed product, customer, and date dimensions, and a supplier dimension that changes slowly. Product categories are reorganized roughly twice a year, and the analysis must still attribute last year sales to the category the product belonged to at the time. The nightly load runs at 02:00 and must finish before the 06:00 replenishment report. Two source systems disagree about the spelling of customer names, and the sales team has asked to see both spellings reconciled into one row.

Questions in this block

1. Sales must be attributed to the category a product had at the time. What should be built? _(D)_
2. Two systems spell the same customer differently. What should the warehouse key on? _(A)_
3. A corrected row must replace the earlier version. What should be used? _(A)_

### Case study — Proseware Media

Proseware Media streams video to 12 million viewers and emits a playback event for every session start, stop, and quality change. The events arrive through an event hub at up to 90,000 per second during a live finale. The analytics team wants a rolling count of concurrent viewers per channel with five-minute granularity, and the operations team wants an alert when error rates exceed a threshold for ten minutes. The events must also be joined to a slowly changing subscriber dimension to attribute viewing to a subscription tier. The company has one eventhouse and a lakehouse, and the chief data officer has forbidden a second copy of the raw events.

Questions in this block

1. A streaming notebook fails on one transformation. What shows the exception? _(C)_
2. Two years of events are retained but only a day is queried. What should be set? _(D)_
3. An error rate must notify the team within ten minutes. What should be configured? _(D)_

### Case study — Woodgrove Bank

Woodgrove Bank loads transaction and customer data into a Fabric warehouse for a regulatory reporting team. The data includes account numbers, national identifiers, and balances. Only the financial crime team may see the full national identifier; analysts may see the rest of the row. Branch managers may see only their own branch transactions, while head office sees everything. The regulator requires a record of who accessed which report and when, retained for seven years. The bank has assigned a sensitivity label of Highly Confidential to all customer data, and auditors have asked how a label applied in Fabric prevents a copied table from escaping the classification.

Questions in this block

1. Every customer table must carry a classification that survives a copy. What should be applied? _(D)_
2. Branch managers may see only their own branch transactions. What should be defined? _(C)_
3. The regulator asks who accessed a report and when. Where is that recorded? _(B)_

## Exam 3

### Case study — Beacon Health

Beacon Health monitors 4,000 patients at home with connected devices that emit a reading every minute. The clinical team needs an alert within five minutes when a reading crosses a personalised threshold, and the compliance team needs every reading retained for six years. Readings sometimes arrive out of order when a device reconnects, and a device can emit a duplicate reading for the same minute. Clinicians may see only the patients on their own caseload, and the data carries a sensitivity label that must not be lost. The organisation has an eventhouse and a warehouse and wants the alerting path separated from the reporting path.

Questions in this block

1. Clinicians may see only their own caseload patients. What should be defined? _(A)_
2. A patient reading must carry its classification into every derived table. What should be applied? _(A)_
3. Every access to a patient record must be attributable. Where is that recorded? _(C)_

### Case study — Consolidated Courier

Consolidated Courier receives a parcel scan from 1,100 depots and 90 line-haul hubs. Each scan carries a parcel identifier, a location, a scan type, and a device timestamp. The network team wants a live count of parcels at each hub, and the customer service team wants a per-parcel status that is no more than one minute old. Some depots batch their scans and upload them every fifteen minutes, so the event time and the arrival time differ. A parcel can be scanned more than once at the same location because a handheld is re-synchronised. The company has strict latency targets and cannot afford a batch job in the path.

Questions in this block

1. A quarter of delivery history must be kept for analysis. What should be configured? _(B)_
2. Scans stop appearing at one hub during a burst. What shows the blocked side? _(D)_
3. A hub stops forwarding scans and nobody notices for an hour. What should be configured? _(B)_

### Case study — Riverside Transit

Riverside Transit operates 700 buses and receives a GPS position every ten seconds from each vehicle. The operations centre needs a map of vehicle positions no more than 30 seconds old, and the planning team needs a monthly on-time performance report per route. Positions are broadcast through an event hub, and the same vehicle can appear twice in a batch when a driver swaps terminals. The transit authority publishes the on-time report to the public, so the numbers must be reproducible and the query definitions must be reviewable. The authority has one Fabric capacity that is shared with the finance department.

Questions in this block

1. Position batches must be moved and then transformed in order. What should be used? _(B)_
2. The same vehicle appears twice when a driver swaps terminals. What should be applied? _(B)_
3. Positions must reach the map with no batch job in the path. What should be used? _(A)_

### Case study — Tailspin Toys

Tailspin Toys manufactures toys in four plants, and every machine emits a telemetry record every five seconds. The plants have inconsistent time zones and one plant clock drifts by up to 90 seconds. The reliability team wants to detect a machine that exceeds a temperature threshold for ten consecutive readings, and the quality team wants a daily defect rate by line. Telemetry must be available for three years, but only the last 30 days are queried interactively. A plant that loses network connectivity buffers locally and replays its events when the link returns, sometimes out of order by several hours.

Questions in this block

1. Nobody can say which plant pipeline failed last night. Where should the team look? _(B)_
2. A machine must be flagged after ten consecutive readings above threshold. What should be used? _(D)_
3. One plant sends most of the telemetry and one task dominates. What should be applied? _(A)_

## Exam 4

### Case study — Coho Winery

Coho Winery sells to distributors in nine countries and has grown by acquiring three smaller wineries. Each acquisition brought its own workspace, its own naming convention, and its own capacity. The board wants one governed model of shipments, inventory, and distributor orders, and the legal team needs each country data to stay in its own region. The engineering team has adopted Git and deployment pipelines but has not yet assigned workspaces to domains. Two acquisitions still load their data through Dataflow Gen2 that nobody owns, and the audit committee wants to know which items are certified and which are not.

Questions in this block

1. Three acquisitions sit in workspaces nobody can find. What should be configured? _(B)_
2. Every release is still an export and an import. What should be created? _(C)_
3. The audit committee asks which items are approved. What should be applied? _(D)_

### Case study — Fourth Coffee Roasters

Fourth Coffee Roasters franchises 1,400 cafes in six countries. Each franchisee uploads a daily sales file in a slightly different format, and the central team currently fixes the differences by hand. Coffee prices change quarterly, and the royalty calculation must use the price that applied on the transaction date. The finance team needs a monthly statement per franchisee, and the operations team needs a daily exception list of stores that did not upload. The company has a lakehouse and a warehouse, and the data engineering team has asked whether the files should be loaded through pipelines, dataflows, or a notebook.

Questions in this block

1. A failed daily load is noticed only when a store complains. What should be configured? _(D)_
2. The team must see every franchisee upload and its status. Where should they look? _(B)_
3. A franchisee that did not upload must be told the same morning. What should be configured? _(C)_

### Case study — Nod Publishers

Nod Publishers distributes 30,000 titles to libraries and retailers and tracks reading events from its e-book platform. Events land as JSON in OneLake, and the warehouse holds a title catalogue, a library dimension, and a monthly fact table of loans. The catalogue changes constantly as rights expire and are renewed. The analytics team wants a report that shows loans by title and by the rights status the title had on the loan date. A rights dispute requires the team to reconstruct the catalogue exactly as it stood on a date eighteen months ago. The company also wants to stop copying the raw event files into the warehouse.

Questions in this block

1. Loans must be attributed to the rights status the title had on the loan date. What should be built? _(D)_
2. The catalogue and monthly loans must be joined and updated transactionally. What should hold them? _(A)_
3. The raw event files must be read without another copy. What should be created? _(D)_

### Case study — Trey Research

Trey Research runs clinical trials for pharmaceutical clients and must keep each trial data isolated from every other trial. The data engineering team builds a lakehouse per trial and shares one capacity across forty trials. Each trial defines its own schema, and a trial can be paused and resumed months later. Client contracts require that an engineer working on one trial cannot read another trial data, even accidentally, and that every access is auditable. The team wants to reuse one notebook template across all trials without copying it forty times. A recent audit found a shortcut that exposed one trial folder to the whole engineering workspace.

Questions in this block

1. A shortcut exposed one trial folder to the whole workspace. What should be configured? _(C)_
2. An engineer must see only their own trial rows. What should be defined? _(D)_
3. Each trial contract requires proof of every access. What records it? _(B)_

## Exam 5

### Case study — Lakeshore Retail Group

Lakeshore Retail Group operates four brands, each with its own product hierarchy and its own definition of a sale. The board wants one consolidated revenue number, and each brand wants its own detail. The engineering team has built one lakehouse per brand plus a shared gold layer, and the shared layer is rebuilt in full every night. Query performance on the shared layer has degraded as the brands added columns, and a recent load failed silently for three days because nobody watched the pipeline. The company has a Fabric capacity, a deployment pipeline, and an audit requirement that every revenue figure be reproducible from the gold layer alone.

Questions in this block

1. Each brand must keep its own source after promotion. What should be configured? _(A)_
2. One revenue figure must be provably the approved one. What should be applied? _(D)_
3. The audit requires evidence that every revenue figure was reviewed. Where is it recorded? _(D)_

### Case study — Margie Travel

Margie Travel books 90,000 trips a day through a web front end and a partner API. Booking events land in OneLake as JSON, and a notebook builds a warehouse fact table every hour. The finance team reconciles the warehouse against the payment provider nightly, and a mismatch of even one booking is escalated. The current load sometimes inserts the same booking twice when a partner retries a request. The engineering team wants the hourly load to finish in under ten minutes, and the reconciliation report identifies bookings by a partner reference that is not unique across partners.

Questions in this block

1. A partner retries and the load inserts the booking twice. What should be applied? _(B)_
2. The partner reference is not unique across partners. What should the warehouse use? _(B)_
3. A corrected booking must replace the earlier version. What rule should be applied? _(A)_

### Case study — VanArsdel Manufacturing

VanArsdel Manufacturing collects 11,000 sensor readings per second across nine plants and writes them into an eventhouse. The reliability dashboards query the last 24 hours, and a compliance report queries the last two years once a month. The eventstream that feeds the eventhouse drops events during shift changes, when the volume spikes. Queries that aggregate the last 24 hours have become slower every month even though the daily volume is flat. The team has one capacity, and the manufacturing director has asked for a plan that keeps the dashboard responsive without deleting the two-year history.

Questions in this block

1. Events are dropped during shift changes. What shows the constrained side? _(C)_
2. Two years must be kept for compliance but only a day is queried. What should be set? _(A)_
3. Day queries have slowed as the table grew. What should be set? _(D)_

### Case study — Wide World Importers

Wide World Importers holds 9 billion order-line rows in a Fabric lakehouse and reports on them through the SQL analytics endpoint. The nightly load writes about 240,000 small files, and a report that filters on order date and customer takes eleven minutes. The team has already confirmed that the query is not limited by the capacity and that the join to the customer dimension is not the bottleneck. The load itself now takes longer than the reporting window, and the team suspects that one customer accounts for a fifth of all rows. The company has one capacity and cannot add another before the next quarter.

Questions in this block

1. The nightly load writes 240,000 small files. What should be run first? _(C)_
2. One customer holds a fifth of the order lines. What should be applied? _(A)_
3. The load now exceeds the reporting window and no capacity can be added. What should be reviewed first? _(C)_

## Exam 6

### Case study — Bellows College

Bellows College has 14,000 students, six faculties, and a data platform built by a team of three. Each faculty keeps its own spreadsheet of admissions, enrolment, and results, and the registrar needs one authoritative student record. The college has adopted Fabric with a lakehouse per faculty and a shared warehouse. Student records carry personal data that only the registrar may see in full, while faculty staff may see their own students. The academic year ends with a statutory return that must reconcile exactly to the student record system, and the college cannot afford a data engineer on call overnight.

Questions in this block

1. A faculty keeps its orchestration as a Python DAG. What should be used? _(D)_
2. A faculty may see only its own students. What should be defined? _(B)_
3. Only the registrar may read the full personal identifier. What should be applied? _(B)_

### Case study — Granite Peak Outfitters

Granite Peak Outfitters sells outdoor equipment online in four countries and runs a seasonal business in which traffic triples for six weeks each year. Orders, inventory, and clickstream events all land in OneLake, and a warehouse serves the finance and merchandising teams. The data engineering team has one capacity that is sized for the quiet season. Last year the nightly load missed its window throughout the peak, and the merchandising dashboards timed out. The team wants a plan that keeps the load inside its window in the peak season without paying for a second capacity all year, and the finance team needs a monthly revenue figure that can be reproduced from the gold layer.

Questions in this block

1. The peak season triples traffic on one capacity. What should be changed first? _(D)_
2. A burst of four jobs must not be throttled. What should be enabled? _(A)_
3. The peak load writes far more small files. What should be run? _(D)_

### Case study — Munson Sporting Goods

Munson Sporting Goods supplies 2,600 independent sports retailers and runs its own warehouse. Orders arrive through an API, a dealer portal, and a legacy EDI feed. The data engineering team has one lakehouse, one warehouse, one eventhouse, and one capacity. The supply chain director wants a single order-status view across all three channels, the finance team wants a month-end close that reconciles to the ERP, and the operations team wants an alert when an order sits unshipped for more than a day. The team has adopted Git, deployment pipelines, and sensitivity labels, and a recent audit asked for evidence that every promotion was reviewed and that no engineer could read another team data.

Questions in this block

1. Three channels arrive as files that must be moved before transform. What should be used? _(D)_
2. A channel retries and the same order appears twice. What should be applied? _(B)_
3. Finance needs one row per channel-day. What should be produced? _(A)_

### Case study — Relecloud Telecom

Relecloud Telecom serves 3.8 million mobile subscribers and generates 140,000 network events per second at peak. The network operations team needs an alert within two minutes of a cell tower degradation, and the regulatory team needs call detail records retained for two years. Events arrive from three vendors with different schemas and different timestamp precisions. The company runs one eventhouse and one lakehouse on a single capacity that is already at 80 percent utilisation during peak hours. A previous attempt to store every event in the lakehouse proved too slow to query, and a previous attempt to keep everything in the eventhouse proved too expensive to retain.

Questions in this block

1. Nobody can say which pipeline failed in the peak. Where should the team look? _(C)_
2. A tower degradation must be flagged within two minutes. What should be used? _(C)_
3. Queries slow down as more towers are monitored. What should be increased? _(A)_
