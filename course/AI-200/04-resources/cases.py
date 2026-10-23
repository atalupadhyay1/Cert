"""Case-study scenarios for the AI-200 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Northwind catalog', """
Northwind runs a product catalogue service on Azure Container Apps behind a queue of merchandising imports.
A ranking change is about to ship and must receive a small share of production traffic while the previous revision keeps serving the rest.
Workers idle overnight and back up during promotions, and operations has learned that queue length, not CPU, reflects the real work.
The container also calls a third-party enrichment API, and auditors must confirm the key is never stored in deployment settings.
""")

c('Fabrikam catalog', """
Fabrikam operates a multi-tenant catalogue for 40 suppliers on Azure Database for PostgreSQL with pgvector.
Retrieval has to return only the chunks a caller is entitled to see while still returning a full result set.
After the index grew past nine million vectors, similarity queries slowed down and the server began reporting memory pressure.
A latency-critical similarity lookup must avoid a round trip to the relational database entirely.
""")

c('Tailspin Retail', """
Tailspin Retail runs storefront services on Azure Container Apps across three environments.
The container needs a different currency list per environment, and merchandising changes it weekly without a redeploy.
A fraud check reads pricing documents and must never see a stale value, and the workload is single-region, so extra read latency is not worth paying for.
The team wants one place to see which setting each environment is actually running.
""")

c('Alpine Outfitters', """
Alpine Outfitters runs a catalogue enrichment pipeline that reacts to new images and documents.
Four enrichment processors must share change feed work, and each partition may be read by exactly one instance.
The team must react to blob creation in its catalogue storage account without writing and hosting a custom publisher.
A feature flag change has to reach running instances without a restart during peak season.
""")

c('ClaimsFlow', """
ClaimsFlow ingests claim documents for an insurer running AKS in a private network.
Inside the cluster the storage hostname resolves to a public address and connections are refused by the firewall.
A corrupt document repeatedly fails indexing, and the team must inspect it later without blocking the queue.
A secret reference fails at runtime even though the secret exists, and the application already has a managed identity.
""")

c('MedRec intake', """
MedRec intake processes clinical documents for a hospital group using PostgreSQL with pgvector and a Redis cache.
Extracted entities must be filtered by site and department and also searched by meaning in one statement.
A retrieval step must return only chunks from sites the caller is assigned to while still returning a complete result list.
Similar prior cases must be found in single-digit milliseconds, and the corpus fits comfortably in memory.
""")

c('Lakeview Clinic', """
Lakeview Clinic runs a document intake service for 40 practices.
A new extraction model must receive one tenth of intake traffic while the current model keeps the rest.
Intake workers must follow the number of unprocessed documents, and the queue is empty every night.
Every newly extracted document must start enrichment immediately without polling the container, and retrieval must still respect each clinician's department.
""")

c('Meridian Health', """
Meridian Health runs billing and coding services for a hospital group.
The billing subscriber must receive only document events whose type property is claim, while coding receives every document event.
Latency has to be split between the function itself and its SQL dependency for the same request.
A document with an unreadable encoding fails repeatedly and must be set aside for support without stalling the queue.
""")

c('PaymentsGate', """
PaymentsGate runs a payment API on AKS with a Redis cache and a Service Bus queue of settlement messages.
A pod reports ready but cannot reach the cache, and the same test succeeds from a jump host.
A message with an invalid schema is retried indefinitely and starves other work on the same worker.
A leaked credential must be replaced with no downtime, and the old value must stop working immediately.
""")

c('LedgerOne', """
LedgerOne is a ledger platform serving several banks from one shared deployment.
Rebuilding the fraud vector index on the ledger table blocked settlement writes for forty minutes last quarter.
Retrieval must return only chunks belonging to the calling bank and must still return five results.
Settlement, fraud, and notification must each receive every payment event with their own cursor, and the container stopped scaling after a connection string was removed.
""")

c('VaultTrust', """
VaultTrust is a treasury platform whose settlement pipeline feeds a fraud service and a reporting dashboard.
A poisoned settlement message is redelivered forever and occupies a worker each time.
The daily settlement dashboard aggregates ninety days of ledger logs and times out on every refresh.
Rebuilding the vector index for fraud detection blocks writes while it runs, which the business will not accept again.
""")

c('Fabrikam Plant', """
Fabrikam Plant runs a defect-inspection pipeline on AKS across two production lines.
Pods cannot open a connection to the storage account, though the same test succeeds from a workstation.
Only events for a specific production line should reach the maintenance handler.
An operator needs the slowest inspection operations in the last hour with their durations, without scanning a week of logs.
""")

c('Contoso Assembly', """
Contoso Assembly inspects assembled units at four plants and routes defects to plant-specific reviewers.
Reviewers must see only defects from their own plant while still receiving a full list of matches.
A corrupt image reference repeatedly fails inspection and must be preserved for analysis rather than discarded.
The quality team needs rejection counts per fifteen-minute interval during a shift.
""")

c('Ironworks Plant', """
Ironworks Plant runs three shifts of visual inspection across a large camera estate.
Station workers must follow the number of queued images, and the queue is empty between shifts.
Similar-defect search across a million historical images must answer in tens of milliseconds.
Images from one station must be processed in the order they were captured, which the current setup does not guarantee.
""")

c('Apex Motors', """
Apex Motors inspects vehicles at the end of four assembly lines and keeps every image for traceability.
Recall collapses when six inspection queries run at once because the index no longer fits in memory.
Retrieval must return only chunks from the requesting plant and must still return five passages.
The model call dominates inspection latency, but the transaction view shows no span for it.
""")

c('CityPortal', """
CityPortal is a municipal service portal running on AKS with a blob-triggered document pipeline.
A pod resolves the database hostname to a public address and the connection is refused.
A handler must react when an uploaded file is created in storage, with no polling.
A non-secret setting is stored centrally but its value must remain in the vault, and a slow request is logged without an exception.
""")

c('CityWorks Permits', """
CityWorks Permits reviews scanned permit applications for a city authority.
A new OCR model must take one tenth of review traffic before it replaces the current one.
Review workers must follow the number of pending scanned forms and shrink to zero at night.
Retrieval must return only documents the requester may see and must still return five passages.
""")

c('StateLibrary', """
StateLibrary runs a state-wide catalogue and enquiry service across 120 branches.
Catalogue records and embeddings must be filtered by collection and language beside a vector predicate in one statement.
A catalogue event must wait for the registry service to recover without burning delivery attempts.
A request loses its trace identifier the moment work is queued for OCR.
""")

c('StoreOps', """
StoreOps runs store fulfilment for a retail chain across two Azure regions.
Pods in one region fail to reach the cache while pods in another region succeed.
A message with a bad address repeatedly fails fulfilment and must be preserved for investigation.
An incident query over seven days is slow and expensive, and on-call needs it to return in seconds.
""")

c('GroupRetail', """
GroupRetail serves eight markets from one commerce platform, each with its own policy text.
Each market may see only its own policy text, and the result list must stay complete.
Visual product similarity must return from memory without a database round trip.
A price-rule change must notify subscribers even though it is not an Azure resource event.
""")

c('GlobalMart', """
GlobalMart runs a global storefront on AKS in four regions, fed by a shared product platform.
Storefront clusters pull the same large image on every scale-out, and pulls dominate cold start outside business hours.
Retrieval must return only chunks for the caller's market and must still fill the result count.
Pricing, inventory, and loyalty must each receive every product event with their own cursor.
""")

c('NovaRetail', """
NovaRetail runs product discovery and fulfilment for two million catalogue chunks.
Similar-product search must answer in tens of milliseconds.
A replayed payment event must never create a second fulfilment record, and the finance team checks this after every incident.
A ninety-day revenue-by-market aggregation times out whenever the dashboard refreshes.
""")

c('CampusDesk', """
CampusDesk runs the student document service for a large university.
A first implementation returned nearest neighbours and then hid rows the caller may not see, so the list came back short.
A document with an unreadable encoding fails repeatedly and must be set aside for support.
A non-secret setting is stored centrally, but its value must remain in the vault.
""")

c('FraudDesk', """
FraudDesk supports analysts investigating payments fraud across two regions.
Only cases the analyst is assigned to may appear in results, and the result count must stay complete.
A fraud model update must notify subscribers even though it is not an Azure resource change.
A leaked credential must be replaced with no downtime, and the old value must stop working immediately.
""")
