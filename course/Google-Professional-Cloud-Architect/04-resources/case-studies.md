# PCA case study briefs

Every mock exam contains 4 case studies of 5 questions. The scenario below is the shared context;
the items that follow it are scored individually. Paste the relevant section into a practice-test description or a
downloadable resource when you want the scenario available before the questions.

## Exam 1

### Case study — Cobalt Retail Group

Cobalt Retail Group operates 640 stores and a checkout service that must respond in under 300 ms. Traffic is predictable Monday to Saturday and spikes on Black Friday to twelve times the normal rate. The current system runs on virtual machines in two on-premises data centres, and the board wants the peak moved to Google Cloud without rebuilding the applications. Store systems must reach the checkout service over a private path, and the chief financial officer has asked for a cost comparison between paying for peak capacity all year and paying for it four weeks a year. The company has no dedicated network engineers and relies on a small platform team.

Questions in this block

1. The board asks what success looks like before the peak moves to Google Cloud. What should be agreed first? _(D)_
2. The checkout service must scale for four weeks a year without rebuilding the application. What should be used? _(A)_
3. Peak capacity is needed for four weeks and idle for the rest of the year. What should the architect recommend? _(B)_
4. A new checkout version must be proven on real traffic before Black Friday. What should be used? _(A)_
5. Nobody knows whether the design survives twelve times normal concurrency. What should be run? _(A)_

### Case study — Helios Broadcasting

Helios Broadcasting streams live sport to 30 million viewers across Europe and North America. A premiere can raise concurrent viewers from 200,000 to 9 million in ten minutes, and the company is contractually required to keep the stream running through the loss of a single region. Video segments are written to a bucket in us-central1 and served to a global audience, and the packager runs on GKE. Advertising revenue is billed per delivered segment, so an outage has a direct financial cost. The board has asked for a design that survives one region failing without a manual decision, and finance has asked what the extra resilience costs per month.

Questions in this block

1. The stream must not stop when a region is lost, and no manual decision is allowed. What should the architecture provide? _(A)_
2. Segments are written once in us-central1 and fetched by a global audience. What should sit in front of the bucket? _(D)_
3. The segment archive must stay readable when one region is lost. Which bucket configuration meets that? _(B)_
4. The board will fund regional resilience only if the target is explicit and achievable. Which two inputs are required? Select two. _(A, D)_
5. The team must know whether viewers actually received a stable stream. What should be defined per region? _(B)_

### Case study — Meridian Health Systems

Meridian Health Systems runs a patient portal for 4.5 million members and must comply with HIPAA. Clinicians in twelve hospitals need single sign-on, and patients need to reach the portal from any device without a VPN. A recent audit found that one administrator could read every patient record, and the remediation plan must show that access is limited to the hospital a clinician works for. The portal runs on Cloud Run and reads records from Cloud SQL. The security team wants every administrative action recorded with the identity that performed it, retained for six years, and available to an auditor without a support ticket.

Questions in this block

1. An administrator can currently read every patient record. What should replace the broad grant? _(A)_
2. Clinicians need single sign-on without a VPN, and device posture must be judged. Which two controls apply? Select two. _(A, D)_
3. Administrative actions must be attributable and retained for six years. What should be enabled? _(B)_
4. The portal runs on Cloud Run and must reach a database on a private address. What should be attached? _(D)_
5. An auditor must obtain the evidence without opening a support ticket. What should be built? _(D)_

### Case study — Vantage Logistics

Vantage Logistics tracks 90,000 vehicles across South America. Each vehicle emits a position every five seconds, which is about 18,000 messages per second at peak, and the operations team needs a live map no more than fifteen seconds behind. Telemetry must be kept for five years for accident investigation, but only the last ninety days are queried frequently. Vehicle identifiers arrive out of order when a truck leaves coverage for several hours, and duplicate readings are common at cell boundaries. The company is opening in two new countries next year and wants the same pipeline to serve them without a redesign.

Questions in this block

1. 18,000 position messages per second must reach the live map within fifteen seconds. What should the producer publish to? _(C)_
2. Five years of telemetry must be retained cheaply after the hot window. What should hold it? _(A)_
3. Collectors at ninety depots will become VMs that are idle between shifts. How should they be provisioned? _(A)_
4. Before two new countries go live, the map must keep up under their message rate. What should be run? _(A)_
5. Operations cannot see per-depot lag today. What should be built first? _(D)_

## Exam 2

### Case study — Kestrel Airlines

Kestrel Airlines sells seats through a booking service that must stay available during the sale that opens twice a year. A sale can produce 40,000 seat requests per second for the first ten minutes, and two seats must never be sold twice even when the requests land in different regions. The booking database currently runs on PostgreSQL on premises and the loyalty programme runs on a separate mainframe that cannot be changed this year. The airline operates in twelve countries and each country has a currency and a tax rule that must be applied at the moment of booking rather than in a nightly batch.

Questions in this block

1. Two seats must never be sold twice across two regions during a sale. What should hold the inventory? _(B)_
2. Currency and tax must be applied at the moment of booking rather than overnight. What should the design use? _(A)_
3. The airline must show who changed a fare and when. What should be enabled? _(D)_
4. The twice-yearly sale must not fail on concurrency. What should be run beforehand? _(C)_
5. The sale opens at midnight and the response must not depend on who is awake. What should be published? _(A)_

### Case study — Lumen Analytics

Lumen Analytics sells a multi-tenant analytics product to 300 customers. Each customer expects its data to be isolated and its queries to run in under two seconds against a 40 GB dataset. The engineering team wants a single deployment that serves every tenant, with a per-tenant cost figure the sales team can quote. Customers are onboarding at roughly twenty a month, and the team has four engineers who are already on call for the serving layer. Tenants range from a five-person startup to a bank that requires a signed data-processing agreement and a named region.

Questions in this block

1. 300 tenants must share one deployment and idle tenants must cost nothing. What should be used? _(C)_
2. One tenant requires a signed agreement naming the region. What must the design fix? _(B)_
3. Each new tenant needs an isolated environment created the same way every time. What should be used? _(D)_
4. A bank tenant must reach the service privately from its own network. What should be published? _(A)_
5. The sales team quotes a two-second query target per tenant. How should it be monitored? _(B)_

### Case study — Quarry Manufacturing

Quarry Manufacturing runs twelve plants that each host a historian, a manufacturing execution system, and a local file share. Plant engineers need the telemetry from the plant floor inside Google Cloud within a second to drive a predictive maintenance model, and the plants have unreliable internet links that drop for minutes at a time. Corporate policy forbids any inbound connection from the internet to a plant network. The company wants the same architecture in every plant, deployed from one template, and it needs an operator at each site to see plant status even when the wide-area link is down.

Questions in this block

1. Twelve plants must be assessed before a single template is written. What should be used? _(D)_
2. Plant servers must stay patched although nobody is on site at night. What should be used? _(C)_
3. A plant collector stopped at 02:14 and nobody knows why. Where should the team look first? _(C)_
4. The same stack must be deployed identically at twelve sites from one template. What should be used? _(B)_
5. Operators must see plant status even when the wide-area link is down. What should the design include? _(A)_

### Case study — Sable Financial

Sable Financial Group has 40 subsidiaries, 300 projects, and a regulator who requires that production data cannot leave the European Union. Each subsidiary has its own engineering team, and last year one team created a public bucket that held customer statements for eleven days. The group wants a resource structure where a new project inherits the network, the logging destination, and the security controls without a ticket. Network address space is managed centrally, and subsidiaries must not be able to create their own routes to the internet. Terraform is the standard tool, and the platform team wants every environment change to be reviewed before it is applied.

Questions in this block

1. A subsidiary published customer statements in a public bucket last year. What should prevent a repeat in every future project? _(B)_
2. Subsidiaries need isolated environments but one centrally managed network. Which two constructs provide that? Select two. _(B, D)_
3. No subsidiary may create its own route to the internet. What should be applied above the projects? _(D)_
4. Every environment change must be reviewed before it is applied. What should the pipeline enforce? _(B)_
5. The public bucket was found eleven days later by an external researcher. What should follow the fix? _(D)_

## Exam 3

### Case study — Beacon Genomics

Beacon Genomics sequences human genomes for research hospitals in three countries. Each genome is about 200 GB and the archive grows by 40 TB a month. Raw reads are analysed for two weeks after sequencing and then kept for twenty years because consent agreements require it. Researchers in different countries must not be able to read each other cohorts, and the consent terms forbid moving data out of the country where it was collected. The research platform runs batch analysis on thousands of cores for a few days each month and is idle between studies.

Questions in this block

1. Twenty years of sequence data must be held cheaply after analysis. Which class fits? _(D)_
2. A new country cohort must be sized before the platform is extended. What should be used? _(A)_
3. Researchers must be able to prove they never opened another cohort. What should be enabled? _(D)_
4. Thousands of cores sit idle between studies. What should be reviewed first? _(A)_
5. The lab must see whether the last study finished within its window. What should be built first? _(B)_

### Case study — Fable Media Group

Fable Media Group runs a subscription news site with 8 million registered readers across the European Union and Brazil. The data protection officer has found that reader records contain email addresses, device identifiers, and in some cases payment details in free-text support notes. Marketing wants to run a churn model on the reader data, and the legal team wants proof that personal data is minimised before it reaches the model. Readers may request deletion, and the request must remove the record everywhere within thirty days. The engineering team uses BigQuery for analytics and Cloud Storage for exports.

Questions in this block

1. Marketing must model churn on readers without seeing direct identifiers. What should be applied? _(C)_
2. The deletion service on Cloud Run must reach an internal database. What should be attached? _(B)_
3. A deletion request must complete within thirty days under peak load. What should be run? _(C)_
4. A missed deletion is a reportable breach. Who must answer it on a Sunday? _(C)_
5. Brazilian readers must be processed in Brazil. What must the design fix? _(A)_

### Case study — Ironvale Bank

Ironvale Bank processes card payments and is audited against PCI DSS. Card numbers must never be readable by the analytics team, and the encryption keys must be rotated on a schedule the bank controls and must remain in the region where the data lives. A recent penetration test showed that a developer with read access to a bucket could copy a data export to a personal project. The regulators have asked for evidence that data cannot leave the approved services even when a principal has the permission to read it. The bank runs three environments and wants the same controls applied to every new project automatically.

Questions in this block

1. Card numbers must be unreadable without a key the bank can revoke. What should be used? _(C)_
2. A developer copied an export to a personal project. What would have blocked it? _(D)_
3. Card data exports must be undeletable for the audit period. What should be applied? _(C)_
4. The penetration test found the copy path. What should follow the remediation? _(C)_
5. Every new project must start with the approved controls. What should the pipeline enforce? _(B)_

### Case study — Summit Public Sector

Summit Public Sector delivers a citizen benefits portal for a national government. The workload handles identity documents, tax identifiers, and benefit payments, and the government requires that only personnel who are citizens and who have passed a background check may operate the platform. The portal must be available during a national election, when traffic is thirty times normal, and every administrative action must be attributable to a named individual. The government has its own identity provider, and it will not permit service account keys anywhere in the environment. A separate agency will audit the deployment twice a year.

Questions in this block

1. Only vetted staff on managed devices may operate the portal. What should be used? _(A)_
2. No project may be created outside the approved region. What should be enforced? _(C)_
3. Workloads must hold no service account keys at all. What should be enabled? _(C)_
4. The election-day promise is measured in successful logins. How should it be monitored? _(B)_
5. The platform team is small and cannot patch nodes. What should be chosen? _(C)_

## Exam 4

### Case study — Harborline Shipping

Harborline Shipping runs its booking and tracking platform in a single region and has a recovery objective of fifteen minutes for the booking service and four hours for the analytics warehouse. A fire in the primary data centre last year stopped bookings for nine hours. The board has approved a budget for resilience but not for running the entire estate twice. The booking database is 4 TB and the warehouse is 300 TB, and the network team has said a second region can be reached only through a new interconnect. The company must prove the recovery time in a rehearsal before the next board meeting.

Questions in this block

1. Booking can accept fifteen minutes of downtime and a smaller running copy. What fits? _(D)_
2. The document archive must stay readable if the primary region is lost. Which bucket configuration meets that? _(A)_
3. Recovery of the booking service depends on the data being available in the second region. What must the design provide? _(A)_
4. The board expects a proven recovery time, not a promise. What must be aligned with the vendor? _(D)_
5. The 4 TB booking database must move with a short cutover. What should be used? _(B)_

### Case study — Orchid Commerce

Orchid Commerce runs a marketplace with 12 million monthly shoppers. The analytics team spends EUR 90,000 a month on BigQuery and cannot explain which team or dashboard causes the spend. Dashboards refresh every ten minutes and scan the same three large tables each time, while a nightly machine learning job scans the same tables again for training. The finance team wants each product team to see its own cost, and the platform team wants the top ten queries by bytes scanned identified before any commitment is purchased. Traffic doubles in November, and the chief technology officer has refused a three-year commitment until the waste is removed.

Questions in this block

1. Dashboards refresh every ten minutes and rescan three large tables. What should absorb the repeated reads? _(C)_
2. The nightly job scans the same table as the dashboards. What should reduce that scan first? _(D)_
3. Nobody can say which team caused the EUR 90,000 bill. What should be configured? _(A)_
4. The team must know when checkout slows before customers complain. What should be defined? _(A)_
5. Each marketplace seller may read only its own order rows. What should be applied? _(C)_

### Case study — Pinecrest University

Pinecrest University has 200 developers across nine faculties who deploy research applications to a shared cluster. Each faculty currently creates projects by hand, and a review found that forty per cent of the projects had no owner and that several had public buckets. The university wants a paved road: a new project should arrive with the right folder placement, budget label, logging destination, and network attachment, and it must be impossible to create a public bucket. Deployments must be reproducible, and a faculty must not be able to change another faculty environment. The security team wants to see every environment change before it happens.

Questions in this block

1. A faculty must self-serve a compliant project without the platform team. What should be published? _(B)_
2. Forty per cent of projects had no owner and several buckets were public. What should prevent that in future projects? _(B)_
3. The programme must show whether the paved road actually reduced incidents. What should be recorded now? _(C)_
4. A public bucket was found and fixed, and the same mistake recurred. What is missing? _(D)_
5. Nine faculties must be inventoried before environments are standardized. What should be used? _(C)_

### Case study — Vertex Insurance

Vertex Insurance prices motor policies from telematics, claims history, and vehicle data. The pricing team retrains a gradient-boosted model every week, and the current process runs a notebook on an engineer laptop. Regulators require that any price quoted to a customer can be reproduced with the exact model version and input data that produced it. The claims stream arrives continuously and the pricing features must be refreshed daily. Two models run in production at once during a migration, and the team must be able to send five per cent of traffic to the new model before committing to it.

Questions in this block

1. Weekly retraining and daily scoring must use one feature definition. What should be used? _(C)_
2. Claims notes contain sensitive data, and the pricing assistant must resist manipulation. Which two controls apply? Select two. _(A, B)_
3. A price change may be caused by drift in the input data. What should be enabled? _(B)_
4. A quote took nine seconds and the team needs the call chain. What should be inspected? _(A)_
5. The team must see training and serving metrics in one place. What should be built first? _(A)_

## Exam 5

### Case study — Atlas Retail Cloud

Atlas Retail Cloud is moving 1,800 virtual machines and 60 databases from two data centres into Google Cloud over nine months. The estate includes a 12 TB Oracle database that supports the ordering system and a set of Windows file servers used by 400 stores. The business cannot accept more than a four-hour outage per application, and the migration must be sequenced so that dependencies move together. The team has three engineers who have never run a migration, and the chief information officer wants a plan that shows what moves in each wave and how a failed wave is reversed.

Questions in this block

1. 1,800 virtual machines must be sized before the nine-month plan is signed. What should be used? _(D)_
2. Store file servers must stay patched with no on-site staff. What should be used? _(C)_
3. A migration wave must be reviewed, and the tested build must reach production unchanged. Which two practices apply? Select two. _(C, E)_
4. A failed wave must be reversed inside a four-hour window. What must be aligned with the vendor? _(C)_
5. The CIO wants to know whether each wave actually reduced cost. What should be recorded before wave one? _(C)_

### Case study — Cedar Health Cloud

Cedar Health Cloud is consolidating three hospital groups onto one platform. Each group has its own identity provider and its own clinical application, and the clinicians must reach all three without a second login. Patient records must stay in the country of the hospital that created them, and a clinician in one group must see only the patients of that group unless a referral grants temporary access for seventy-two hours. The consolidation must complete before the next accreditation visit in eight months, and the groups refuse to change the clinical applications this year.

Questions in this block

1. Three hospital identity providers must be trusted without shared keys. What should be used? _(B)_
2. A consent service on Cloud Run must reach a clinical database privately. What should be attached? _(A)_
3. Clinical records need a fifteen-minute recovery objective at continuous cost. What fits? _(A)_
4. The accreditation visit follows an outage that was never reviewed. What should be produced now? _(D)_
5. The clinical database must fail over without an operator restart. What should be enabled? _(C)_

### Case study — Nimbus Games

Nimbus Games is launching a multiplayer title in four regions on the same day. The launch is expected to bring 2 million concurrent players in the first hour, and the game servers must be created in the region closest to each player. The studio has committed to a launch date that cannot move, and a previous launch failed because the quota for the region had never been raised. Infrastructure is defined in Terraform, and the team wants to rehearse the whole launch twice before the real one. The finance team has approved spend for launch week only, not for the year.

Questions in this block

1. Launch-week capacity is needed for seven days and then not at all. What should be used? _(B)_
2. The studio must rehearse two million concurrent players twice before launch. What should be run? _(D)_
3. Each region must be watched from the first minute of launch. What should be built first? _(C)_
4. Game servers must appear in the closest region and be replaced when unhealthy. What should be used? _(A)_
5. No region may be used that has not been approved for player data. What should be enforced? _(D)_

### Case study — Zephyr Payments

Zephyr Payments exposes a payment API to 900 merchants and processes 4 million calls a day. Merchants have different rate limits, and one merchant caused a 40-minute outage last quarter by retrying aggressively after a timeout. The API must never break a merchant integration, so the versioning and deprecation policy has to be explicit. The company wants to release several times a day and to be able to stop a bad release within a minute. Each release must be traceable to a commit and a passing test run, and the security team wants to know which images are running in production at any moment.

Questions in this block

1. Nine hundred merchants need individual quotas, and one retried through an outage. What should front the API? _(C)_
2. A bad release must be stopped within a minute without a rebuild. What should the release use? _(A)_
3. The security team asks what built the running image and from which commit. What should be recorded? _(B)_
4. Merchant success rate is the promise, not processor load. What should be defined? _(D)_
5. Merchants must never be locked into an integration they cannot leave. What must the design include? _(B)_

## Exam 6

### Case study — Everline Media

Everline Media publishes a news and video platform that 22 million people use each day. The product team has promised that article pages load in under one second for 99 per cent of requests and that video start time stays under two seconds for 99.5 per cent. Nobody can currently say whether either promise is met, and the last three incidents were found by readers on social media rather than by the team. The engineering organisation has 140 people across twelve teams, each with its own dashboards, and the chief technology officer wants one agreed definition of success per user journey.

Questions in this block

1. The team promised load and start-time targets but cannot say whether they are met. What should be defined first? _(D)_
2. The board asks how the platform could be replaced if the vendor relationship ended. What must the design include? _(C)_
3. Twelve teams deploy to one platform with no shared review gate. What should the pipeline enforce? _(C)_
4. Viewer data must not be copied outside the approved projects. What should be applied? _(A)_
5. Ad-delivery evidence must be undeletable for the audit period. What should be applied? _(D)_

### Case study — Granite Utilities

Granite Utilities operates the electricity distribution network for a region of 3 million homes. Smart meters send a reading every fifteen minutes, and the control room needs a live view of demand with an alert if a substation stops reporting. Regulatory reporting requires a defensible monthly settlement figure, and any correction to a past settlement must be traceable. The platform runs on Google Cloud and the operations team is on call twenty-four hours a day. A previous incident took four hours to diagnose because the alert fired on the wrong metric and the runbook was out of date.

Questions in this block

1. The control room must see substation telemetry with one agreed signal set. What should be built first? _(C)_
2. Readings arrive late when a concentrator reconnects and must still settle correctly. What should the pipeline use? _(B)_
3. A four-hour diagnosis followed an alert that fired on the wrong metric. Which two tools would have shortened it? Select two. _(C, E)_
4. A corrected settlement must show who changed it and when. What should be enabled? _(D)_
5. Settlement queries always filter by date, and the scan cost is rising. What should be applied first? _(D)_

### Case study — Solstice Travel

Solstice Travel runs a booking platform whose traffic is concentrated into three holiday peaks. Each peak is about eleven times the January baseline, and the company pays for peak capacity all year because the platform team has never had time to change it. The booking flow depends on seven services, and one slow service during the last peak caused a cascade that took the site down for forty minutes. The chief executive has asked for a plan that keeps the peak stable, lowers the annual bill, and shortens the time to diagnose the next cascade.

Questions in this block

1. The platform pays for peak capacity all year while the baseline is tiny. What should the architect recommend first? _(B)_
2. Seven services run on Kubernetes and the team is three engineers. What should be chosen? _(C)_
3. A regional loss must not stop bookings, and the data must be usable in the other region. What must the design provide? _(A)_
4. Booking can accept fifteen minutes of downtime and a smaller running copy. What fits? _(C)_
5. One slow service took the site down last peak. What should be run before the next one? _(C)_

### Case study — Union Foundry

Union Foundry runs a mixed estate: a Kubernetes platform for customer-facing services, a warehouse for financial reporting, and a machine learning team that builds demand forecasts. The company is preparing for an acquisition that will double its data volume and add two countries with different data residency rules. Leadership wants one operating model for all three workloads, a cost figure per business unit, and evidence that a regional failure would not stop customer-facing services. The security team has asked how the model weights and training data are protected, because the forecast is now considered a trade secret.

Questions in this block

1. The forecast must use the same features in training and serving across two countries. What should be used? _(B)_
2. The forecast model and its weights are a trade secret, and prompts must not leak them. What should be added? _(D)_
3. Two acquired countries must migrate with a short cutover and no data loss. What should be used? _(D)_
4. The acquisition brings new support obligations for customer-facing services. What should be aligned? _(C)_
5. The forecast must be reproducible after an audit question about a past demand figure. What should be used? _(A)_
