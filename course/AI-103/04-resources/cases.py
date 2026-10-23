"""Case-study scenarios for the AI-103 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Contoso support', """
Contoso runs a customer support operation of 600 agents handling billing disputes for a subscription product.
A Foundry Agent Service agent answers tier-one billing questions and must carry the case number across a long conversation.
Agents can issue credits up to $50 on their own authority; anything larger needs a supervisor.
Quality review has found the assistant answering confidently from memory when the retrieved billing policy says something different.
""")

c('Fabrikam claims', """
Fabrikam is an insurer whose claims analysts work through scanned packets from four regions.
Packets mix multi-page tables, handwriting, and layouts that differ by region, and analysts need typed fields plus markdown they can reason over.
Auditors must be able to verify every answer the retrieval assistant gives, without seeing another region's claims.
The same claim form carries local-language legal terms that three different translators have rendered three different ways.
""")

c('Tailspin Retail', """
Tailspin Retail publishes store procedures on an intranet that merchandising edits every week.
Store managers ask questions through an assistant and must be able to click through to the page an answer came from.
Operations wants to be paged within minutes if the assistant starts refusing questions it used to answer.
When a procedure is withdrawn, its text has to disappear from search results almost immediately, not at the next monthly rebuild.
""")

c('Wingtip Insurance', """
Wingtip Insurance produces patient-facing illustrations of medical procedures for its communications team.
Legal requires every generated illustration to be screened for unsafe or misleading depictions before publication.
Analysts also want a fast topical index of what each complaint in the backlog is actually about.
On long policy questions the retrieved evidence crowds out the instructions, and the model drifts away from what was asked.
""")

c('ClinDoc', """
ClinDoc is a clinical documentation assistant used by 2,000 clinicians across a hospital group.
It summarizes encounters, and the safety committee wants a standing measure of summaries that mention medications no source note contains.
Before answering, the assistant must confirm whether a patient has an appointment tomorrow, and some requests need records, scheduling, and billing expertise at once.
Anything it states has to be traceable to a note a clinician can open.
""")

c('BillingBot', """
BillingBot handles patient billing enquiries for a regional health system in three languages.
Translated statements keep mangling approved plan names, which has produced complaints to the regulator.
Standard Explanation of Benefits forms arrive in a consistent layout with stable fields, and volumes are high.
Extracted amounts occasionally disagree with the scanned value, and finance will not post a figure a person has not seen.
""")

c('Lakeview Clinic', """
Lakeview Clinic is a 40-practice primary care network running a patient-facing scheduling agent.
The agent calls a lookup tool with a patient identifier, and the tool keeps rejecting the value because the schema is loose.
Patients return to the same conversation ten minutes later and expect their earlier answer to still be in scope.
One request fails only when the agent needs two tool calls in sequence, and nobody can see which call broke.
""")

c('Meridian Health', """
Meridian Health operates a multi-site hospital group with dictation, complaints, and inbound fax.
Dictation accuracy is poor for local drug names, and the team has several hundred hours of labelled audio already.
Reviewers need a quick topical index of what each complaint packet covers before they read it.
Amounts extracted from faxed forms are sometimes misread, and a clinician must see those values before they are used.
""")

c('FraudDesk', """
FraudDesk supports investigators at a payments company operating in two regulatory regions.
Investigators in one region must never see the other region's case notes, and that separation is audited quarterly.
The team is comparing two retrieval configurations and needs groundedness scores it can defend side by side.
Some requests fail only after the second tool call, and the investigators only report that "it didn't work".
""")

c('LoanDocs', """
LoanDocs processes lending decisions for a consumer finance provider.
Applicants may ask for their decision letter to be read aloud over the phone, and the provider has committed to that in its accessibility policy.
Scanned letters use regional abbreviations the extraction prompt ignores, so dates and statuses come back wrong.
One lender uses its own proprietary application form with no standard equivalent, and its volume justifies dedicated work.
""")

c('LedgerOne', """
LedgerOne is an accounting platform whose auditors reconcile thousands of extracted invoice lines.
An auditor asks for totals across two thousand line items, and text-based arithmetic has already produced two wrong figures.
A payment request fails only after the second tool call, and the support desk cannot reproduce it.
Newly generated client letters must be searchable within seconds of being written.
""")

c('VaultTrust', """
VaultTrust is a wealth adviser platform used by 900 advisers.
Advisers return to a client file the next day and expect the assistant to still know the case reference.
Dictation misreads product codes, and a misheard code is a compliance event rather than an inconvenience.
Scanned amounts from legacy statements are sometimes misread, and an adviser must confirm them before they reach the client record.
""")

c('LineSight', """
LineSight runs continuous visual inspection on a production line that operates 24 hours a day.
The workload is steady and cannot tolerate throttling during a shift, and a missed defect stops the line.
A defect request fails only after the second tool call, and the engineering team needs to see where it broke.
The agent must also keep the work-order number across turns while it checks status.
""")

c('Fabrikam Plant', """
Fabrikam Plant is a heavy-equipment site with contractor access, controlled manuals, and its own inspection paperwork.
The plant uses a proprietary inspection form that no prebuilt model covers, and the volume justifies a custom model.
Contractors must only retrieve documents approved for the plant they are working in.
Each indexed manual has to gain extracted entities and a generated summary as part of ingestion.
""")

c('Ironworks Plant', """
Ironworks Plant runs three shifts and reports yield from handwritten shift records.
An engineer needs yield percentages computed across those extracted records, and text-based arithmetic has been unreliable.
A work-order request fails only after the second tool call, and the maintenance team cannot tell whether the agent or the connector broke.
Newly generated inspection reports must be searchable within seconds of being issued.
""")

c('Apex Motors', """
Apex Motors assembles vehicles on four lines and tracks every component for traceability.
A technician resumes the same line issue after lunch and needs the assistant to recall the machine tag from the morning.
Voice reporting misreads part numbers, and a wrong part number breaks the traceability record.
Scanned measurements from paper gauges are sometimes misread, and an engineer must confirm them.
""")

c('CityHelp', """
CityHelp is a resident-facing portal for a metropolitan council covering housing, waste, and benefits.
After launch, answers began citing services that do not appear in the retrieved pages at all.
The portal must call only the deployments approved for one Foundry project, and security has to see that in configuration.
A general enquiry often belongs to a specialist team, and the handoff must keep the resident's context.
""")

c('CampusDesk', """
CampusDesk supports a university's grant office, where staff process applications on a proprietary council form.
No prebuilt model covers that form, and the finance office rejects any figure a person has not checked.
Extracted amounts from scanned forms are sometimes misread, so uncertainty has to route to a person.
Every indexed regulation must gain extracted entities and a summary during ingestion.
""")

c('MetroPermits', """
MetroPermits issues parking and trade permits for a city authority.
Staff need fee totals computed across extracted application lines, and text arithmetic has produced two wrong invoices.
A permit request fails only after the second tool call, and the counter staff cannot tell which system refused.
Newly issued determinations must appear in search within seconds of being signed.
""")

c('StateLibrary', """
StateLibrary runs a state-wide enquiry service across 120 branches and a digitized collection.
A student returns to the same enquiry after a break and expects the assistant to recall the programme discussed.
Call transcripts misread local place names, which misroutes calls to the wrong branch.
Scanned application values are sometimes misread, and a librarian must confirm them before a record changes.
""")

c('GroupAssist', """
GroupAssist is the shared assistant for a group with nine subsidiaries and one policy library.
One subsidiary runs continuous, predictable volume and cannot tolerate throttling during its business day.
Auditors must verify each answer against an approved policy page rather than accept a summary.
Long policy evidence crowds out the question on complex enquiries, and the model starts drifting.
""")

c('WarrantyDesk', """
WarrantyDesk handles warranty claims for a consumer electronics manufacturer.
The agent must keep a case number across turns and check that case in the claims system before it answers.
One subsidiary uses a proprietary claim form that no prebuilt model covers.
Every indexed policy must gain extracted entities and a summary as part of ingestion, and the index has to stay current.
""")

c('GlobalMart', """
GlobalMart is a retailer whose category managers reconcile supplier invoices and monitor order status.
A manager needs margin percentages computed across extracted supplier lines, where text arithmetic has already failed once.
An order status request fails only after the second tool call, and nobody can say which call was refused.
Newly generated supplier notices must be searchable within seconds of being issued.
""")

c('NovaRetail', """
NovaRetail is a franchise network where store staff file warranty claims by phone.
A franchisee returns to the same claim after a break and expects the assistant to recall the claim number.
Store call transcripts misread local product codes, which then drive warranty routing the wrong way.
Scanned supplier values are sometimes misread, and a store manager must confirm them before a claim is filed.
""")
