"""Case-study scenarios for the AI-300 practice exams.

Each scenario is the shared context for one block of three questions. The name
must match the `Case study — <Name>:` prefix used in questions/*.txt.
"""

CASES = {}


def c(name, text):
    if name in CASES:
        raise ValueError(f'Duplicate case study: {name}')
    CASES[name] = ' '.join(text.split())


c('Fabrikam Retail AI', """
Fabrikam Retail runs demand forecasting for 300 stores from three years of transaction data and wants the training pipeline reproducible.
The data team consists of four engineers who currently create workspaces in the portal, name resources by hand, and store the storage account key in the job YAML.
A new regulatory requirement says the training data must stay on the private network and every production model must be traceable to the exact data asset and commit that produced it.
The forecasting model is retrained weekly and currently takes two days of manual effort per release.
""")

c('Contoso Foundry', """
Contoso runs a customer-support assistant on Microsoft Foundry for 1,200 agents across three regions.
The assistant retrieves from a 40,000-document knowledge base that the content team updates every weekday, and the team has noticed answers quoting a policy that was withdrawn four months ago.
Two teams share a single Foundry project and the same model connection, and last month one team changed a deployment setting that silently degraded the other team's latency.
Monthly spend has tripled since launch and nobody can attribute it to a feature or a team.
""")

c('Tailwind Logistics', """
Tailwind Logistics operates a route-optimization model that scores 900,000 shipments a night and a real-time ETA endpoint that answers 4,000 requests per second at peak.
The nightly scoring job currently loops over the online endpoint one record at a time and takes nine hours, which no longer fits the overnight window.
The ETA endpoint runs on a fixed instance count that is sized for the peak and sits idle for sixteen hours a day.
Twice this quarter a new model version was promoted directly to production and had to be withdrawn the same evening.
""")

c('Meridian Bank', """
Meridian Bank deploys a document-extraction model for mortgage applications and must satisfy an internal audit that asks how each model version was approved.
The bank has separate development, test, and production subscriptions, and a single service principal with Contributor on all three is used by every pipeline.
Audit found that a model version was overwritten in the registry last year, so the artifact that produced an approved decision can no longer be reproduced.
The bank also wants every deployment to be reversible within five minutes.
""")

c('Northwind MLOps', """
Northwind runs machine learning operations for a manufacturing group and is under pressure to cut model-release effort.
Engineers train in notebooks on a compute instance, copy the resulting model file to a share, and ask a platform engineer to deploy it by hand.
The group has six production models, no experiment tracking, and no agreement on which environment image a job should use, so two runs of the same script have produced different results.
The platform team wants one repeatable path from commit to deployment, with an approval step before production.
""")

c('Harborview Health', """
Harborview Health runs a clinical summarization service on Foundry that drafts discharge summaries from 400,000 encounters a year.
Clinicians report that the service occasionally states a medication dose that appears nowhere in the record, and the quality team cannot reproduce the failures because prompts and completions are not retained.
A recent red-team exercise found that a scanned document containing hidden instructions could make the assistant ignore its safety rules.
The compliance office requires evidence that each released change was evaluated, and the evaluation must not be produced by the same prompt it is testing.
""")

c('Alpine Manufacturing', """
Alpine Manufacturing operates a predictive-maintenance model on 4,000 sensors across three plants.
The model was trained on eighteen months of data and its accuracy has fallen from 0.91 to 0.74 since a production line was retooled, though the aggregate dashboard still looks acceptable because two other lines improved.
The data science team monitors only the accuracy reported at deployment and has no baseline for the new sensor distributions.
Plant engineers want an alert before a failure, and the platform team wants to know whether the fix is a retrain or something else.
""")

c('Woodgrove Insurance', """
Woodgrove Insurance runs a claims triage model and a generative assistant that explains the triage decision to adjusters.
The assistant is grounded in a policy index that is rebuilt monthly, and adjusters have started escalating answers that cite an expired endorsement.
The insurer must retain evidence of each model version and each evaluation result for seven years, and a regulator has asked how the triage model is monitored after deployment.
A pilot team has proposed fine-tuning a model on the policy corpus instead of maintaining the index.
""")

c('Litware Analytics', """
Litware Analytics builds retrieval-augmented assistants for enterprise clients and is standardizing its GenAIOps practice.
Each client engagement currently copies a prompt file into a notebook, edits it in place, and deploys the flow to a shared endpoint whose connection string is stored in the flow repository.
Client contracts require that content access follow the client's own entitlement model, and two clients have asked for evidence that a change to the prompt was evaluated before release.
The team wants to compare two prompt strategies for the same task without maintaining parallel forks.
""")

c('Portside Utilities', """
Portside Utilities runs a customer assistant that answers questions about tariffs, outages, and meter readings from a document set that changes daily during storm season.
During the last storm the assistant confidently quoted an outdated outage number for six hours, and the operations team only learned about it from social media.
The utility has a small platform team, a fixed monthly budget for model spend, and a requirement that no customer account data leave its tenant.
The team also wants the assistant to stop answering when the retrieved content does not support an answer.
""")

c('Skyline Media', """
Skyline Media publishes a news archive of twenty years and wants a research assistant for its journalists.
The archive sits in a third-party system, and the retrieval index is built from summaries rather than full text, so journalists report that quoted passages cannot be found.
A standards editor requires that every published claim be traceable to a source document, and a recent incident involved an assistant inventing a plausible quotation.
The publisher also wants to compare two retrieval configurations on the same set of historical queries before committing.
""")

c('Beacon Financial', """
Beacon Financial operates an agent that helps analysts assemble quarterly research notes by calling internal tools for prices, filings, and estimates.
The agent has access to fourteen tools, including a trade-execution stub that should never be called from a research workflow, and an analyst discovered it could reach the stub by phrasing the request unusually.
The firm needs a record of which tools the agent called for each note, and compliance wants a review before any new tool is exposed.
Latency has also doubled since the tool list grew.
""")

c('Cedar Ridge Health', """
Cedar Ridge Health is deploying a generative assistant for care-coordination staff and has been asked by its safety committee to prove the system is ready.
The committee wants evidence about harmful output, resistance to instruction-override attempts, and whether the system can be traced when a clinician disputes an answer.
The team has a 300-case evaluation set built from last year's queries and no agreed rubric for grading answers.
A vendor has offered a jailbreak test suite, and the team is unsure whether running it once before launch is sufficient.
""")

c('Northgate Bank', """
Northgate Bank runs a document question-answering assistant over loan files, and internal audit has asked for a control that proves answers are supported by the retrieved evidence.
The bank has two evaluation approaches: a similarity score against a reference answer and a groundedness score against retrieved passages, and the team disagrees about which one governs release.
Audit also wants to know how a wrong answer is investigated six months after the fact.
The bank has a strict retention policy: prompts may be stored for 90 days, and customer identifiers must be redacted before storage.
""")

c('Brightwater Water', """
Brightwater Water operates a network-fault assistant for field crews and wants to reduce the cost of running it.
The assistant sends a 6,000-token system prompt on every request, retrieves twelve passages per answer, and routes every question to the largest available model.
Monthly spend is now four times the forecast, and the finance team wants a reduction within one quarter without a drop in answer quality.
Crews have complained that the first token takes eight seconds on a slow connection, which matters more than total generation time in the field.
""")

c('Lakeshore Council', """
Lakeshore Council runs a public-facing assistant that answers questions about services, permits, and bin collection.
The council's content team updates pages weekly, and residents have reported answers based on guidance that was replaced after a service change.
The council must publish an accessibility statement and must not return content that the requesting user could not access in the source system.
A local journalist has begun testing the assistant with adversarial prompts and publishing the results.
""")

c('Evergreen Pharma', """
Evergreen Pharma runs a medical-information assistant that summarizes approved product documentation for field staff.
The assistant must never answer outside approved content, must cite the document and revision it used, and must be evaluated before every release because promotional material is regulated.
The company has a validated quality process that requires a documented change record for each model or prompt change.
Field staff have asked for faster answers, and the current release cycle takes three weeks because evaluation is run by hand.
""")

c('Cobalt Retail', """
Cobalt Retail runs a product-description generator that produces 40,000 descriptions a month across three languages.
The team wants to reduce cost per description, improve factual accuracy against supplier specifications, and cut the time from prompt change to release.
Two experiments are planned: a smaller model for simple categories and provisioned throughput for the steady volume.
The merchandising team refuses any change that lowers factual accuracy, and there is no written definition of what accuracy means for a description.
""")

c('Redwood Manufacturing', """
Redwood Manufacturing operates a quality-inspection model at the end of three production lines and a batch reporting job that runs every shift.
The model was trained on images from one plant and is being extended to two more with different lighting, and the platform team expects data drift.
The inspection endpoint must answer within 120 milliseconds, and the reporting job must finish before the shift handover.
The team currently deploys with a fixed instance count and has no rollback procedure beyond redeploying the previous image by hand.
""")

c('Granite University', """
Granite University runs a research assistant over licensed journal content and its own thesis repository.
The licences restrict where the content may be stored, so the assistant must query the publisher system in place rather than copy it into the university's own index.
Researchers want citations, and the library wants to know which passages an answer relied on when a claim is challenged.
The university also runs its own evaluation and has asked for a way to compare retrieval configurations before the academic year starts.
""")

c('Kestrel Group', """
Kestrel Group is consolidating four business units onto a single AI platform and has inherited four different practices.
One unit deploys models from notebooks, one uses infrastructure as code with a manual approval gate, one has no experiment tracking, and one runs generative workloads with the API key in a flow repository.
The group CIO wants a single standard for infrastructure, promotion, and evaluation, and has asked for a plan that shows where each unit is out of compliance.
Group audit also wants a register of every deployed model and agent with its owner.
""")

c('Fairhaven Mutual', """
Fairhaven Mutual runs a client-service assistant and a claims-summary model and is preparing for a regulatory review.
The regulator has asked three questions: how the firm detects degradation, how it proves a change did not reduce quality, and how it would withdraw a model within an hour.
The firm has telemetry in Application Insights but no alerting, an evaluation set that was written by the same team that wrote the prompt, and a deployment process that rebuilds the container image for every model version.
The platform team wants a plan it can execute before the review.
""")

c('Atlas Distribution', """
Atlas Distribution operates 40 warehouses and runs generative assistants for shift planning and supplier correspondence.
Warehouse connectivity is unreliable, so perceived latency matters more than total response time, and supervisors often wait for the first visible token.
The operations team wants a single decision framework for choosing between a fine-tuned model, a retrieved grounding approach, and a larger general model for each task.
Spend is reviewed monthly by the CFO, who wants to know which workloads justify provisioned capacity and which should stay on pay-as-you-go.
""")

c('Solstice Energy', """
Solstice Energy runs a field-maintenance assistant grounded in equipment manuals and work orders across four regions.
Manual revisions change quarterly, and engineers have been given answers quoting a superseded torque specification, which the safety team treats as a serious defect.
The company must retain maintenance records for seven years and must be able to show which manual revision an answer relied on.
A vendor has proposed fine-tuning the model on the manuals to improve accuracy, and the platform team is unsure whether that addresses the problem.
""")
