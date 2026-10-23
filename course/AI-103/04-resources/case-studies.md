# AI-103 case study briefs

Every mock exam contains four case studies of three questions. The scenario below is the shared context;
the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,
a downloadable resource, or the practice-test description when you want the scenario available before the questions.

## Exam 1

### Case study — Contoso support

Contoso runs a customer support operation of 600 agents handling billing disputes for a subscription product. A Foundry Agent Service agent answers tier-one billing questions and must carry the case number across a long conversation. Agents can issue credits up to $50 on their own authority; anything larger needs a supervisor. Quality review has found the assistant answering confidently from memory when the retrieved billing policy says something different.

Questions in this block

1. A Foundry Agent Service agent answers billing questions and must retain a case number across turns. Which capability preserves that context? _(B)_
2. The same agent gives confident answers that are not supported by the retrieved billing policy. Which metric should be monitored? _(A)_
3. The agent may issue credits up to $50 but must not exceed that amount without review. What control is required? _(D)_

### Case study — Fabrikam claims

Fabrikam is an insurer whose claims analysts work through scanned packets from four regions. Packets mix multi-page tables, handwriting, and layouts that differ by region, and analysts need typed fields plus markdown they can reason over. Auditors must be able to verify every answer the retrieval assistant gives, without seeing another region's claims. The same claim form carries local-language legal terms that three different translators have rendered three different ways.

Questions in this block

1. Scanned claim packets contain multi-page tables, handwriting, and differing layouts across regions. Analysts need typed fields and markdown for downstream reasoning. Which Content Understanding configuration should be evaluated? _(A)_
2. A retrieval assistant answers from the claim packets, and auditors must verify each answer without exposing another region's claims. Which two controls are required? Select two. _(C, D)_
3. The same claim form uses local-language legal terms that are repeatedly translated inconsistently. What should be added? _(A)_

### Case study — Tailspin Retail

Tailspin Retail publishes store procedures on an intranet that merchandising edits every week. Store managers ask questions through an assistant and must be able to click through to the page an answer came from. Operations wants to be paged within minutes if the assistant starts refusing questions it used to answer. When a procedure is withdrawn, its text has to disappear from search results almost immediately, not at the next monthly rebuild.

Questions in this block

1. Answers must reflect an intranet that changes weekly and must cite the source page. Which approach fits? _(D)_
2. Operations must be paged within minutes when refusal rates spike. What should be configured? _(C)_
3. A withdrawn document must disappear from search results within minutes. What must be implemented? _(D)_

### Case study — Wingtip Insurance

Wingtip Insurance produces patient-facing illustrations of medical procedures for its communications team. Legal requires every generated illustration to be screened for unsafe or misleading depictions before publication. Analysts also want a fast topical index of what each complaint in the backlog is actually about. On long policy questions the retrieved evidence crowds out the instructions, and the model drifts away from what was asked.

Questions in this block

1. A generated illustration of a medical procedure must be screened for unsafe depictions before publication. Which control applies? _(B)_
2. Analysts want a quick topical index of what each complaint covers. Which capability applies? _(A)_
3. Long retrieved passages crowd out the instructions and the model drifts off the question. What should be configured? _(D)_

## Exam 2

### Case study — BillingBot

BillingBot handles patient billing enquiries for a regional health system in three languages. Translated statements keep mangling approved plan names, which has produced complaints to the regulator. Standard Explanation of Benefits forms arrive in a consistent layout with stable fields, and volumes are high. Extracted amounts occasionally disagree with the scanned value, and finance will not post a figure a person has not seen.

Questions in this block

1. Translated statements keep mangling approved plan names. What should be added? _(D)_
2. Standard Explanation of Benefits forms arrive in a well-known layout with stable fields. What should be used first? _(A)_
3. Extracted amounts occasionally disagree with the scanned value. What should route those fields to a person? _(B)_

### Case study — ClinDoc

ClinDoc is a clinical documentation assistant used by 2,000 clinicians across a hospital group. It summarizes encounters, and the safety committee wants a standing measure of summaries that mention medications no source note contains. Before answering, the assistant must confirm whether a patient has an appointment tomorrow, and some requests need records, scheduling, and billing expertise at once. Anything it states has to be traceable to a note a clinician can open.

Questions in this block

1. After go-live, summaries sometimes state medications that no source note contains. Which signal should be monitored? _(B)_
2. The assistant must confirm whether a patient has an appointment tomorrow before answering. Which capability performs that check? _(B)_
3. One request may need records, scheduling, and billing expertise. Which pattern should coordinate them? _(D)_

### Case study — Lakeview Clinic

Lakeview Clinic is a 40-practice primary care network running a patient-facing scheduling agent. The agent calls a lookup tool with a patient identifier, and the tool keeps rejecting the value because the schema is loose. Patients return to the same conversation ten minutes later and expect their earlier answer to still be in scope. One request fails only when the agent needs two tool calls in sequence, and nobody can see which call broke.

Questions in this block

1. The agent keeps sending an unformatted patient identifier to the lookup tool. What should be tightened first? _(C)_
2. A patient asks a follow-up question ten minutes after the first, and the earlier answer must still be in scope. Which capability provides that? _(A)_
3. A request fails only when the agent needs two tool calls in sequence. What should be inspected? _(D)_

### Case study — Meridian Health

Meridian Health operates a multi-site hospital group with dictation, complaints, and inbound fax. Dictation accuracy is poor for local drug names, and the team has several hundred hours of labelled audio already. Reviewers need a quick topical index of what each complaint packet covers before they read it. Amounts extracted from faxed forms are sometimes misread, and a clinician must see those values before they are used.

Questions in this block

1. Dictation accuracy is poor for local drug names and the team has labelled audio. What should be trained? _(C)_
2. Reviewers need a quick topical index of what each complaint packet covers. Which capability applies? _(B)_
3. Extracted amounts are sometimes misread from faxed forms. What should route those values to a person? _(A)_

## Exam 3

### Case study — FraudDesk

FraudDesk supports investigators at a payments company operating in two regulatory regions. Investigators in one region must never see the other region's case notes, and that separation is audited quarterly. The team is comparing two retrieval configurations and needs groundedness scores it can defend side by side. Some requests fail only after the second tool call, and the investigators only report that "it didn't work".

Questions in this block

1. Investigators in two regions must not see each other's case notes. Which control enforces that separation? _(D)_
2. The team needs comparable groundedness scores for two retrieval configurations. What should they run? _(D)_
3. A request fails only after the second tool call. What should be inspected first? _(C)_

### Case study — LedgerOne

LedgerOne is an accounting platform whose auditors reconcile thousands of extracted invoice lines. An auditor asks for totals across two thousand line items, and text-based arithmetic has already produced two wrong figures. A payment request fails only after the second tool call, and the support desk cannot reproduce it. Newly generated client letters must be searchable within seconds of being written.

Questions in this block

1. An auditor asks for totals across two thousand extracted line items, and text-based arithmetic is unreliable. Which tool is required? _(A)_
2. A payment request fails only after the second tool call. What should be inspected? _(B)_
3. Newly generated client letters must be searchable within seconds. What should the application use? _(A)_

### Case study — LoanDocs

LoanDocs processes lending decisions for a consumer finance provider. Applicants may ask for their decision letter to be read aloud over the phone, and the provider has committed to that in its accessibility policy. Scanned letters use regional abbreviations the extraction prompt ignores, so dates and statuses come back wrong. One lender uses its own proprietary application form with no standard equivalent, and its volume justifies dedicated work.

Questions in this block

1. Applicants may request that decision letters be read aloud over the phone. Which capability applies? _(C)_
2. Scanned letters use regional abbreviations that the extraction prompt ignores. What should be added? _(C)_
3. A lender receives its own proprietary application form with no standard equivalent. What should be built? _(B)_

### Case study — VaultTrust

VaultTrust is a wealth adviser platform used by 900 advisers. Advisers return to a client file the next day and expect the assistant to still know the case reference. Dictation misreads product codes, and a misheard code is a compliance event rather than an inconvenience. Scanned amounts from legacy statements are sometimes misread, and an adviser must confirm them before they reach the client record.

Questions in this block

1. An adviser returns to the same client file the next day and the assistant must recall the case reference. Which capability is required? _(A)_
2. Adviser dictation misreads product codes that matter for compliance. What should be trained? _(D)_
3. Scanned amounts are sometimes misread. What should route those values to a person? _(D)_

## Exam 4

### Case study — Apex Motors

Apex Motors assembles vehicles on four lines and tracks every component for traceability. A technician resumes the same line issue after lunch and needs the assistant to recall the machine tag from the morning. Voice reporting misreads part numbers, and a wrong part number breaks the traceability record. Scanned measurements from paper gauges are sometimes misread, and an engineer must confirm them.

Questions in this block

1. A technician resumes the same line issue after lunch and the assistant must recall the machine tag. Which capability is required? _(A)_
2. Voice reporting misreads part numbers that are critical for traceability. What should be trained? _(B)_
3. Scanned measurements are sometimes misread. What should route those values to a person? _(D)_

### Case study — Fabrikam Plant

Fabrikam Plant is a heavy-equipment site with contractor access, controlled manuals, and its own inspection paperwork. The plant uses a proprietary inspection form that no prebuilt model covers, and the volume justifies a custom model. Contractors must only retrieve documents approved for the plant they are working in. Each indexed manual has to gain extracted entities and a generated summary as part of ingestion.

Questions in this block

1. The plant uses a proprietary inspection form with no standard equivalent. What should be built? _(D)_
2. Contractors must only retrieve documents approved for their plant. What should be enforced? _(D)_
3. Each indexed manual must gain extracted entities and a generated summary. What performs that work? _(B)_

### Case study — Ironworks Plant

Ironworks Plant runs three shifts and reports yield from handwritten shift records. An engineer needs yield percentages computed across those extracted records, and text-based arithmetic has been unreliable. A work-order request fails only after the second tool call, and the maintenance team cannot tell whether the agent or the connector broke. Newly generated inspection reports must be searchable within seconds of being issued.

Questions in this block

1. An engineer needs yield percentages computed across extracted shift records, and text arithmetic is unreliable. Which tool is required? _(D)_
2. A work-order request fails only after the second tool call. What should be inspected? _(D)_
3. Newly generated inspection reports must be searchable within seconds. What should the application use? _(A)_

### Case study — LineSight

LineSight runs continuous visual inspection on a production line that operates 24 hours a day. The workload is steady and cannot tolerate throttling during a shift, and a missed defect stops the line. A defect request fails only after the second tool call, and the engineering team needs to see where it broke. The agent must also keep the work-order number across turns while it checks status.

Questions in this block

1. A plant runs continuous 24-hour inspection inference with steady volume and cannot tolerate throttling. Which capacity option should be evaluated? _(B)_
2. A defect request fails only after the second tool call. What should be inspected first? _(A)_
3. The agent must keep the work-order number across turns while checking status. Which capability is required? _(D)_

## Exam 5

### Case study — CampusDesk

CampusDesk supports a university's grant office, where staff process applications on a proprietary council form. No prebuilt model covers that form, and the finance office rejects any figure a person has not checked. Extracted amounts from scanned forms are sometimes misread, so uncertainty has to route to a person. Every indexed regulation must gain extracted entities and a summary during ingestion.

Questions in this block

1. The council uses a proprietary grant form that no prebuilt model covers. What should be built? _(C)_
2. Extracted amounts are sometimes misread from scanned forms. Which two controls route uncertain values to people? Select two. _(A, D)_
3. Every indexed regulation must gain extracted entities and a summary. Which component defines those steps? _(B)_

### Case study — CityHelp

CityHelp is a resident-facing portal for a metropolitan council covering housing, waste, and benefits. After launch, answers began citing services that do not appear in the retrieved pages at all. The portal must call only the deployments approved for one Foundry project, and security has to see that in configuration. A general enquiry often belongs to a specialist team, and the handoff must keep the resident's context.

Questions in this block

1. After launch, answers cite services that do not appear in the retrieved pages. Which signal should be monitored? _(D)_
2. The portal must call only the deployments approved for one Foundry project. What should it be configured with? _(D)_
3. A general assistant must transfer a housing issue to a specialist while keeping context. Which pattern fits? _(D)_

### Case study — MetroPermits

MetroPermits issues parking and trade permits for a city authority. Staff need fee totals computed across extracted application lines, and text arithmetic has produced two wrong invoices. A permit request fails only after the second tool call, and the counter staff cannot tell which system refused. Newly issued determinations must appear in search within seconds of being signed.

Questions in this block

1. Staff need fee totals computed across extracted application lines, and text arithmetic is unreliable. Which tool is required? _(C)_
2. A permit request fails only after the second tool call. What should be inspected? _(B)_
3. Newly issued determinations must be searchable within seconds. What should the application use? _(C)_

### Case study — StateLibrary

StateLibrary runs a state-wide enquiry service across 120 branches and a digitized collection. A student returns to the same enquiry after a break and expects the assistant to recall the programme discussed. Call transcripts misread local place names, which misroutes calls to the wrong branch. Scanned application values are sometimes misread, and a librarian must confirm them before a record changes.

Questions in this block

1. A student returns to the same enquiry after a break and the assistant must recall the programme discussed. Which capability is required? _(C)_
2. Call transcripts misread local place names that matter for routing. What should be trained? _(A)_
3. Scanned application values are sometimes misread. What should route those values to a person? _(D)_

## Exam 6

### Case study — GlobalMart

GlobalMart is a retailer whose category managers reconcile supplier invoices and monitor order status. A manager needs margin percentages computed across extracted supplier lines, where text arithmetic has already failed once. An order status request fails only after the second tool call, and nobody can say which call was refused. Newly generated supplier notices must be searchable within seconds of being issued.

Questions in this block

1. A category manager needs margin percentages computed across extracted supplier lines. Which tool is required? _(D)_
2. An order status request fails only after the second tool call. What should be inspected? _(D)_
3. Newly generated supplier notices must be searchable within seconds. What should the application use? _(A)_

### Case study — GroupAssist

GroupAssist is the shared assistant for a group with nine subsidiaries and one policy library. One subsidiary runs continuous, predictable volume and cannot tolerate throttling during its business day. Auditors must verify each answer against an approved policy page rather than accept a summary. Long policy evidence crowds out the question on complex enquiries, and the model starts drifting.

Questions in this block

1. One subsidiary runs continuous, predictable volume and cannot tolerate throttling. Which capacity option should be evaluated? _(C)_
2. Auditors must verify each answer against an approved policy page. Which capability makes that possible? _(B)_
3. Long policy evidence crowds out the question and the model starts drifting. What should be configured? _(B)_

### Case study — NovaRetail

NovaRetail is a franchise network where store staff file warranty claims by phone. A franchisee returns to the same claim after a break and expects the assistant to recall the claim number. Store call transcripts misread local product codes, which then drive warranty routing the wrong way. Scanned supplier values are sometimes misread, and a store manager must confirm them before a claim is filed.

Questions in this block

1. A franchisee returns to the same claim after a break and the assistant must recall the claim number. Which capability is required? _(C)_
2. Store call transcripts misread local product codes that drive warranty routing. What should be trained? _(A)_
3. Scanned supplier values are sometimes misread. What should route those values to a person? _(D)_

### Case study — WarrantyDesk

WarrantyDesk handles warranty claims for a consumer electronics manufacturer. The agent must keep a case number across turns and check that case in the claims system before it answers. One subsidiary uses a proprietary claim form that no prebuilt model covers. Every indexed policy must gain extracted entities and a summary as part of ingestion, and the index has to stay current.

Questions in this block

1. A warranty agent must keep a case number across turns and check it in a claims system. Which two capabilities are required? Select two. _(C, E)_
2. One subsidiary uses a proprietary claim form that no prebuilt model covers. What should be built? _(B)_
3. Every indexed policy must gain extracted entities and a summary during ingestion. Which component defines those steps? _(C)_
