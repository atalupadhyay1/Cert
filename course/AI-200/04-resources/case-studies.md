# AI-200 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Alpine Outfitters

Alpine Outfitters runs a catalogue enrichment pipeline that reacts to new images and documents. Four enrichment processors must share change feed work, and each partition may be read by exactly one instance. The team must react to blob creation in its catalogue storage account without writing and hosting a custom publisher. A feature flag change has to reach running instances without a restart during peak season.

Questions in this block

1. Four enrichment processors must share change feed work, and each partition must be read by exactly one instance. What coordinates the split? _(B)_
2. The team must react to blob creation in its catalog storage account without writing and hosting a custom publisher. What should be used? _(B)_
3. A feature flag change must reach running instances without a restart or a redeploy during peak season. What should be enabled? _(A)_

### Case study — Fabrikam catalog

Fabrikam operates a multi-tenant catalogue for 40 suppliers on Azure Database for PostgreSQL with pgvector. Retrieval has to return only the chunks a caller is entitled to see while still returning a full result set. After the index grew past nine million vectors, similarity queries slowed down and the server began reporting memory pressure. A latency-critical similarity lookup must avoid a round trip to the relational database entirely.

Questions in this block

1. Retrieval must return only chunks the caller is entitled to see while still returning a full result set. What should the query do? _(D)_
2. Vector queries became slow after the index grew, and the server shows heavy memory pressure. What should be addressed? _(A)_
3. A latency-critical similarity lookup must avoid a round trip to the relational database. What should be used? _(A)_

### Case study — Northwind catalog

Northwind runs a product catalogue service on Azure Container Apps behind a queue of merchandising imports. A ranking change is about to ship and must receive a small share of production traffic while the previous revision keeps serving the rest. Workers idle overnight and back up during promotions, and operations has learned that queue length, not CPU, reflects the real work. The container also calls a third-party enrichment API, and auditors must confirm the key is never stored in deployment settings.

Questions in this block

1. A new ranking service must receive a small share of production traffic while the previous version keeps serving the rest. Which capability provides that split? _(D)_
2. Workers are idle overnight and back up during promotions, and the queue length is the true measure of work. What should drive replica count? _(C)_
3. The container needs a third-party API key, and auditors must confirm it is never stored in deployment settings. What should the app configuration use? _(D)_

### Case study — Tailspin Retail

Tailspin Retail runs storefront services on Azure Container Apps across three environments. The container needs a different currency list per environment, and merchandising changes it weekly without a redeploy. A fraud check reads pricing documents and must never see a stale value, and the workload is single-region, so extra read latency is not worth paying for. The team wants one place to see which setting each environment is actually running.

Questions in this block

1. The storefront container needs a different currency list per environment, and merchandising changes it weekly without a release. What should supply the value? _(B)_
2. The fraud check reads pricing documents and must never see a stale value, and the workload is single-region so extra read latency is acceptable. Which consistency choice fits? _(A)_
3. Order events must reach the recommendation, inventory, and loyalty services independently, and each service keeps its own cursor. What should be used? _(D)_

## Exam 2

### Case study — ClaimsFlow

ClaimsFlow ingests claim documents for an insurer running AKS in a private network. Inside the cluster the storage hostname resolves to a public address and connections are refused by the firewall. A corrupt document repeatedly fails indexing, and the team must inspect it later without blocking the queue. A secret reference fails at runtime even though the secret exists, and the application already has a managed identity.

Questions in this block

1. Inside the cluster, the storage hostname resolves to a public address and connections are refused by the firewall. What should be checked? _(D)_
2. A corrupt document repeatedly fails indexing, and the team must inspect it later without blocking the queue. What should be used? _(A)_
3. The secret reference fails at runtime even though the secret exists. The app already has a managed identity. What is missing? _(B)_

### Case study — Lakeview Clinic

Lakeview Clinic runs a document intake service for 40 practices. A new extraction model must receive one tenth of intake traffic while the current model keeps the rest. Intake workers must follow the number of unprocessed documents, and the queue is empty every night. Every newly extracted document must start enrichment immediately without polling the container, and retrieval must still respect each clinician's department.

Questions in this block

1. A new extraction model must receive one tenth of intake traffic while the current model keeps the rest. What should be used? _(B)_
2. Intake workers must follow the number of unprocessed documents, and the queue is empty every night. What should drive replicas? _(B)_
3. Retrieval must return only chunks from the requesting clinician's department and still fill the result count. What should the query do? _(D)_

### Case study — MedRec intake

MedRec intake processes clinical documents for a hospital group using PostgreSQL with pgvector and a Redis cache. Extracted entities must be filtered by site and department and also searched by meaning in one statement. A retrieval step must return only chunks from sites the caller is assigned to while still returning a complete result list. Similar prior cases must be found in single-digit milliseconds, and the corpus fits comfortably in memory.

Questions in this block

1. Extracted clinical entities must be filtered by site and department and also searched by meaning in one statement. What should be used? _(C)_
2. A retrieval step must return only chunks from sites the caller is assigned to, while still returning a complete result set. Where should the scope condition be applied? _(A)_
3. Similar prior cases must be found in single-digit milliseconds, and the case corpus fits in memory. What should be used? _(D)_

### Case study — Meridian Health

Meridian Health runs billing and coding services for a hospital group. The billing subscriber must receive only document events whose type property is claim, while coding receives every document event. Latency has to be split between the function itself and its SQL dependency for the same request. A document with an unreadable encoding fails repeatedly and must be set aside for support without stalling the queue.

Questions in this block

1. Every newly extracted document must start enrichment immediately without polling the container. What should be implemented? _(C)_
2. The billing subscriber must receive only document events whose type property is claim, while coding receives every document. What should be configured? _(B)_
3. Latency must be split between the function itself and its SQL dependency for the same request. What should the query do? _(A)_

## Exam 3

### Case study — FraudDesk

FraudDesk supports analysts investigating payments fraud across two regions. Only cases the analyst is assigned to may appear in results, and the result count must stay complete. A fraud model update must notify subscribers even though it is not an Azure resource change. A leaked credential must be replaced with no downtime, and the old value must stop working immediately.

Questions in this block

1. Only cases the analyst is assigned to may appear in results, and the result count must stay complete. What should the query do? _(D)_
2. A fraud model update must notify subscribers even though it is not an Azure resource change. What should be published? _(D)_
3. A leaked credential must be replaced with no downtime, and the old value must stop working immediately. What should be done? _(C)_

### Case study — LedgerOne

LedgerOne is a ledger platform serving several banks from one shared deployment. Rebuilding the fraud vector index on the ledger table blocked settlement writes for forty minutes last quarter. Retrieval must return only chunks belonging to the calling bank and must still return five results. Settlement, fraud, and notification must each receive every payment event with their own cursor, and the container stopped scaling after a connection string was removed.

Questions in this block

1. After the connection string was removed, the container app stopped scaling and its scale rule reports an authorization failure. What should be granted? _(A)_
2. Retrieval must return only chunks belonging to the calling bank and must still return five results. What should the query do? _(B)_
3. Settlement, fraud, and notification must each receive every payment event with their own cursor. What should be used? _(A)_

### Case study — PaymentsGate

PaymentsGate runs a payment API on AKS with a Redis cache and a Service Bus queue of settlement messages. A pod reports ready but cannot reach the cache, and the same test succeeds from a jump host. A message with an invalid schema is retried indefinitely and starves other work on the same worker. A leaked credential must be replaced with no downtime, and the old value must stop working immediately.

Questions in this block

1. A pod reports ready but cannot reach the Redis cache, and the same test works from a jump host. What should be verified? _(C)_
2. A message with an invalid schema is retried indefinitely and starves other work. What should be configured? _(C)_
3. On-call needs a fast alert on request failure rate without paying for repeated log scans. What should be used? _(B)_

### Case study — VaultTrust

VaultTrust is a treasury platform whose settlement pipeline feeds a fraud service and a reporting dashboard. A poisoned settlement message is redelivered forever and occupies a worker each time. The daily settlement dashboard aggregates ninety days of ledger logs and times out on every refresh. Rebuilding the vector index for fraud detection blocks writes while it runs, which the business will not accept again.

Questions in this block

1. Rebuilding the fraud vector index on the ledger table blocks settlement writes for forty minutes. What should the build use? _(A)_
2. A poisoned settlement message is redelivered forever and occupies a worker each time. What should be configured? _(D)_
3. The daily settlement dashboard aggregates ninety days of ledger logs and times out on every refresh. What should be used? _(D)_

## Exam 4

### Case study — Apex Motors

Apex Motors inspects vehicles at the end of four assembly lines and keeps every image for traceability. Recall collapses when six inspection queries run at once because the index no longer fits in memory. Retrieval must return only chunks from the requesting plant and must still return five passages. The model call dominates inspection latency, but the transaction view shows no span for it.

Questions in this block

1. Recall collapses when six inspection queries run at once because the index no longer fits in memory. What should be addressed? _(A)_
2. Retrieval must return only chunks from the requesting plant and must still return five passages. What should the query do? _(B)_
3. The model call dominates inspection latency, but the transaction view shows no span for it. What should be added? _(D)_

### Case study — Contoso Assembly

Contoso Assembly inspects assembled units at four plants and routes defects to plant-specific reviewers. Reviewers must see only defects from their own plant while still receiving a full list of matches. A corrupt image reference repeatedly fails inspection and must be preserved for analysis rather than discarded. The quality team needs rejection counts per fifteen-minute interval during a shift.

Questions in this block

1. Reviewers must see only defects from their own plant while still receiving a full list of matches. What should the query do? _(D)_
2. A corrupt image reference repeatedly fails inspection and must be preserved for analysis. What should happen to it? _(D)_
3. The team needs rejection counts per fifteen-minute interval during a shift. Which construct should be used? _(B)_

### Case study — Fabrikam Plant

Fabrikam Plant runs a defect-inspection pipeline on AKS across two production lines. Pods cannot open a connection to the storage account, though the same test succeeds from a workstation. Only events for a specific production line should reach the maintenance handler. An operator needs the slowest inspection operations in the last hour with their durations, without scanning a week of logs.

Questions in this block

1. Pods cannot open a connection to the storage account, though the same test succeeds from a workstation. What should be verified? _(D)_
2. Only events for a specific production line should reach the maintenance handler. What should be configured? _(D)_
3. An operator needs the slowest inspection operations in the last hour with their durations. Which tool should be used? _(A)_

### Case study — Ironworks Plant

Ironworks Plant runs three shifts of visual inspection across a large camera estate. Station workers must follow the number of queued images, and the queue is empty between shifts. Similar-defect search across a million historical images must answer in tens of milliseconds. Images from one station must be processed in the order they were captured, which the current setup does not guarantee.

Questions in this block

1. Station workers must follow the number of queued images, and the queue is empty between shifts. What should drive replicas? _(B)_
2. Similar-defect search across a million historical images must answer in tens of milliseconds. Which index fits? _(A)_
3. Images from one station must be processed in the order they were captured. What should be enabled? _(D)_

## Exam 5

### Case study — CampusDesk

CampusDesk runs the student document service for a large university. A first implementation returned nearest neighbours and then hid rows the caller may not see, so the list came back short. A document with an unreadable encoding fails repeatedly and must be set aside for support. A non-secret setting is stored centrally, but its value must remain in the vault.

Questions in this block

1. A first implementation returns nearest neighbours and then hides rows the caller may not see, and the list comes back short. What is wrong? _(B)_
2. A document with an unreadable encoding fails repeatedly and must be set aside for support. What should happen? _(C)_
3. A non-secret setting is stored centrally but its value must remain in the vault. What should be used? _(B)_

### Case study — CityPortal

CityPortal is a municipal service portal running on AKS with a blob-triggered document pipeline. A pod resolves the database hostname to a public address and the connection is refused. A handler must react when an uploaded file is created in storage, with no polling. A non-secret setting is stored centrally but its value must remain in the vault, and a slow request is logged without an exception.

Questions in this block

1. A pod resolves the database hostname to a public address and the connection is refused. What should be checked? _(D)_
2. A handler must react when an uploaded file is created in storage, with no polling. What should it subscribe to? _(D)_
3. A slow request is logged without an exception, and the team suspects a downstream call. Which query shape helps? _(D)_

### Case study — CityWorks Permits

CityWorks Permits reviews scanned permit applications for a city authority. A new OCR model must take one tenth of review traffic before it replaces the current one. Review workers must follow the number of pending scanned forms and shrink to zero at night. Retrieval must return only documents the requester may see and must still return five passages.

Questions in this block

1. A new OCR model must take one tenth of review traffic before it replaces the current model. What should be used? _(C)_
2. Review workers must follow the number of pending scanned forms and must shrink to zero at night. What should drive replicas? _(B)_
3. Retrieval must return only documents the requester may see and must still return five passages. What should the query do? _(C)_

### Case study — StateLibrary

StateLibrary runs a state-wide catalogue and enquiry service across 120 branches. Catalogue records and embeddings must be filtered by collection and language beside a vector predicate in one statement. A catalogue event must wait for the registry service to recover without burning delivery attempts. A request loses its trace identifier the moment work is queued for OCR.

Questions in this block

1. Catalog records and embeddings must be filtered by collection and language beside a vector predicate. How should the table be modeled? _(C)_
2. A catalogue event must wait for the registry service to recover without burning delivery attempts. What should the handler do? _(A)_
3. A request loses its trace identifier the moment work is queued for OCR. What must cross the hop? _(D)_

## Exam 6

### Case study — GlobalMart

GlobalMart runs a global storefront on AKS in four regions, fed by a shared product platform. Storefront clusters pull the same large image on every scale-out, and pulls dominate cold start outside business hours. Retrieval must return only chunks for the caller's market and must still fill the result count. Pricing, inventory, and loyalty must each receive every product event with their own cursor.

Questions in this block

1. Storefront clusters in four regions pull the same large image on every scale-out, and pulls dominate cold start outside the primary region. What should be configured? _(B)_
2. Retrieval must return only chunks for the caller's market and must still fill the result count. What should the query do? _(D)_
3. Pricing, inventory, and loyalty must each receive every product event with their own cursor. What should be used? _(D)_

### Case study — GroupRetail

GroupRetail serves eight markets from one commerce platform, each with its own policy text. Each market may see only its own policy text, and the result list must stay complete. Visual product similarity must return from memory without a database round trip. A price-rule change must notify subscribers even though it is not an Azure resource event.

Questions in this block

1. Each market may see only its own policy text, and the result list must stay complete. What should the query do? _(A)_
2. Visual product similarity must return from memory without a database round trip. What should be used? _(C)_
3. A price-rule change must notify subscribers even though it is not an Azure resource event. What should be published? _(B)_

### Case study — NovaRetail

NovaRetail runs product discovery and fulfilment for two million catalogue chunks. Similar-product search must answer in tens of milliseconds. A replayed payment event must never create a second fulfilment record, and the finance team checks this after every incident. A ninety-day revenue-by-market aggregation times out whenever the dashboard refreshes.

Questions in this block

1. Similar-product search across two million chunks must answer in tens of milliseconds. Which index fits? _(B)_
2. A replayed payment event must never create a second fulfilment record. What should the handler use? _(C)_
3. A ninety-day revenue-by-market aggregation times out whenever the dashboard refreshes. What should be used? _(A)_

### Case study — StoreOps

StoreOps runs store fulfilment for a retail chain across two Azure regions. Pods in one region fail to reach the cache while pods in another region succeed. A message with a bad address repeatedly fails fulfilment and must be preserved for investigation. An incident query over seven days is slow and expensive, and on-call needs it to return in seconds.

Questions in this block

1. Pods in one region fail to reach the cache while pods in another region succeed. What should be checked first on the failing side? _(D)_
2. A message with a bad address repeatedly fails fulfilment and must be preserved for investigation. What should happen? _(B)_
3. An incident query over seven days is slow and expensive. What should be changed first? _(C)_
