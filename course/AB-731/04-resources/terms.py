"""Original AB-731 alternative labels and explanatory definitions."""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: AI types, selection, and models ------------------------------
t('gentext', 'Use a generative model to draft and summarize narrative content',
  'Generative models produce new text, summaries, or images on request. Fluent output can still be wrong, so it needs grounding and review.')
t('classify', 'Use a trained classifier to route items into fixed categories',
  'Classification predicts a label from historical examples. It is cheap and consistent at volume, but it cannot write an explanation or handle a case outside its labels.')
t('regress', 'Use a regression or forecasting model on historical numeric data',
  'Regression estimates a numeric outcome from past observations. It needs clean history and cannot respond to a free-form request.')
t('rules', 'Encode the decision as deterministic business rules',
  'Rules are predictable and easy to audit, but they are brittle when cases vary and they cannot generalize from examples.')
t('anomaly', 'Use anomaly detection on measurements and events',
  'Anomaly detection flags patterns that differ from the norm. It surfaces outliers without explaining them or recommending an action.')
t('hybridai', 'Combine a generative model with a classifier for routing and a rules layer for policy',
  'A combined design uses each technique where it is strongest. It costs more integration and testing than a single technique.')

t('assistchat', 'Deploy an assistant that answers questions from approved documents',
  'A grounded assistant answers from a curated corpus rather than general memory. Its value depends on the corpus being complete and current.')
t('draftdocs', 'Generate first drafts of routine documents for human editing',
  'Drafting removes the blank-page step while a person keeps editorial control. It suits high-volume, low-risk documents.')
t('summarizecase', 'Summarize long case files into a structured brief',
  'Summarization compresses material a person would otherwise read in full. The brief must be checked against the file for omissions.')
t('extractform', 'Extract fields from forms into a system of record',
  'Extraction turns documents into structured data. Accuracy must be measured per field before the output is trusted downstream.')
t('ideate', 'Generate options and variations for a creative brief',
  'Idea generation widens the option set a team starts from. Output is a starting point, not a finished creative decision.')
t('converse', 'Support a multi-turn customer conversation without an agent',
  'Conversational automation handles repeated intents at volume. It needs escalation paths for anything outside the designed intents.')

t('pretrained', 'Start with a pretrained general-purpose model and add grounding',
  'A pretrained model already knows language and general concepts. Grounding supplies your facts without training, and it is the fastest route to a first release.')
t('finetune', 'Fine-tune a model on labelled examples of the house style',
  'Fine-tuning adapts behaviour and tone to examples you own. It needs a labelled set, a retraining process, and a way to retest after each change.')
t('fromscratch', 'Train a domain-specific model from scratch on internal text',
  'Training from scratch demands a large curated corpus, specialist skills, and ongoing evaluation. It is rarely the first step for a business team.')
t('distill', 'Distil a smaller model from a larger teacher model',
  'Distillation moves much of a large model\'s behaviour into a cheaper one. It requires machine-learning engineering and a representative evaluation set.')
t('openweight', 'Host an open-weight model inside your own subscription',
  'Self-hosting gives control over placement and cost at scale. It shifts patching, capacity, and quality evaluation onto your team.')

t('tokenbudget', 'Set a token budget per request and report consumption per team',
  'Prompts and responses are billed in tokens, so a per-request budget plus per-team reporting makes cost visible while usage is still small.')
t('shortprompt', 'Trim prompts and cap response length',
  'Shorter prompts and capped output reduce tokens per call. Taken too far they remove context the answer needs.')
t('cacheanswer', 'Cache repeated answers and reuse them for identical requests',
  'Caching removes repeated inference for the same question. It needs invalidation so a changed policy does not keep an old answer alive.')
t('batchoff', 'Batch non-urgent work into off-peak runs',
  'Batching smooths demand and can use cheaper capacity. It is unsuitable when the user is waiting for the answer.')
t('provisioned', 'Reserve provisioned capacity for predictable peaks',
  'Reserved capacity protects latency during known peaks. It is wasted spend when demand is spiky or unproven.')
t('payg', 'Stay on pay-as-you-go and absorb a variable monthly bill',
  'Pay-as-you-go costs nothing when idle and needs no forecast. It becomes hard to budget once usage is large and steady.')
t('roimetric', 'Define ROI as hours saved against total licence, token, and support cost',
  'A defensible ROI compares measured time saved with every cost of running the solution. It prevents a pilot from being justified by enthusiasm.')
t('pilotcost', 'Instrument cost during the pilot before committing to scale',
  'Pilot telemetry shows real cost per task rather than a vendor estimate. Scaling decisions built on it survive finance review.')
t('seatcost', 'Compare per-seat licence cost with per-use consumption cost',
  'Per-seat pricing suits constant users while consumption suits occasional use. The comparison decides the licensing model, not the model quality.')

t('cite', 'Require citations to the source passage in every answer',
  'Citations let a reviewer check the claim in seconds. They also expose gaps when retrieval finds nothing relevant.')
t('humanreview', 'Route low-confidence answers to a human reviewer',
  'A review queue catches the cases the system should not decide alone. It only works if the confidence signal is meaningful.')
t('evalset', 'Test against a fixed set of representative questions before release',
  'A stable evaluation set turns quality into a number you can compare across changes. It must be refreshed as the business changes.')
t('redteam', 'Red-team the solution for biased, unsafe, or manipulative output',
  'Red-teaming deliberately probes for harmful behaviour before customers find it. Findings need an owner and a fix date.')
t('fallback', 'Return a refusal or a handoff when retrieval finds nothing relevant',
  'A defined fallback prevents a confident answer from no evidence. It trades coverage for trustworthiness.')
t('feedbackloop', 'Capture user feedback and review flagged answers weekly',
  'A feedback loop turns everyday use into a defect list. It needs a routine that triages the flags rather than a dashboard nobody reads.')

t('volumeautomation', 'Automate the high-volume repetitive step and keep experts on exceptions',
  'Automation pays back where volume is high and variation is low. Experts then spend their time on the cases that need judgement.')
t('timesaved', 'Measure minutes saved per task before claiming a benefit',
  'A per-task saving is the unit that scales into a business case. It has to be measured, not assumed from the demo.')
t('capacity', 'Reallocate freed capacity to higher-value work',
  'Freed time is only a benefit if it is deliberately redirected. Without a plan the saving disappears into slack.')
t('augment', 'Augment staff decisions rather than replacing the decision',
  'Augmentation keeps a person accountable while speeding the work. It is easier to govern and adopt than autonomous decisions.')
t('scaleburst', 'Design for seasonal peaks instead of peak staffing',
  'Elastic capacity handles demand spikes that would otherwise need temporary staff. It requires load testing before the season.')

t('fewshot', 'Supply two or three approved examples in the prompt',
  'Examples show the model the shape and tone you want. They consume tokens and must be updated when the standard changes.')
t('rolecontext', 'State the role, audience, and purpose in the prompt',
  'Context steers vocabulary and level of detail. Vague context produces generic output that a reviewer must rewrite.')
t('outputformat', 'Specify the required structure and length of the output',
  'A stated format makes output predictable enough to review or automate. It does not guarantee factual accuracy.')
t('chainsteps', 'Ask for the reasoning steps before the conclusion',
  'Step-by-step output exposes where an answer went wrong. It also increases token use and can produce plausible but invented reasoning.')
t('iterate', 'Iterate the prompt with users and version it',
  'Prompt quality comes from repeated review with real users. Versioning lets you tell whether a change helped.')
t('systemprompt', 'Centralize the standard prompt in a governed template',
  'A shared template keeps tone, disclaimers, and constraints consistent across teams. It still allows approved local additions.')
t('moreinstructions', 'Keep adding instructions until the output improves',
  'Very long prompts blur priorities and raise cost. More instruction is not the same as better instruction.')

t('ragretrieval', 'Retrieve relevant passages and include them in the prompt',
  'Retrieval grounds an answer in your own content without retraining. Its quality depends on what has been indexed and how it is chunked.')
t('permissions', "Enforce the user's existing permissions in retrieval",
  'Permission-aware retrieval returns only what the user may already see. Without it, grounding becomes a data leak.')
t('freshness', 'Reindex on a schedule so answers reflect the current policy',
  'Freshness keeps a grounded answer from quoting a retired policy. The reindex cadence should match how often the source changes.')
t('chunk', 'Split documents into passages that match the question granularity',
  'Chunk size decides whether retrieval returns a usable passage or a fragment. It is a quality setting, not a storage detail.')
t('hybridsearch', 'Combine keyword and vector retrieval',
  'Hybrid retrieval covers exact identifiers and paraphrased meaning together. It adds tuning work and must be measured against a baseline.')
t('biggerinstead', 'Increase the model size instead of adding retrieval',
  'A larger model does not know your internal policy. It raises cost without closing a grounding gap.')

t('cleansed', 'Clean and de-duplicate the source documents first',
  'Duplicates and stale copies produce contradictory answers. Cleaning is unglamorous and usually the highest-value step.')
t('representative', 'Check that test samples represent the real case mix',
  'A test set drawn from easy cases flatters the system. Sampling the real distribution exposes the hard ones.')
t('labelquality', 'Use consistent human labelling for the evaluation set',
  'Inconsistent labels make quality scores meaningless. A short labelling guide improves agreement.')
t('piimask', 'Remove or mask personal data before indexing',
  'Minimizing personal data reduces privacy risk and the impact of a leak. It can also remove detail the answer needs, so scope it deliberately.')
t('extractable', 'Confirm documents are text-extractable rather than scanned images',
  'Scanned pages need optical character recognition before retrieval can use them. Skipping it produces silently empty answers.')
t('datavolume', 'Check the corpus is large enough to answer the questions asked',
  'A thin corpus produces a confident guess. Coverage should be tested with real questions before launch.')

t('dlp', 'Apply sensitivity labels and data loss prevention to generated content',
  'Labels travel with generated content so existing protections still apply. They only work if the source is labelled too.')
t('rbac', 'Restrict access with existing identity and role assignments',
  'Reusing identity and roles avoids a second permission model. It requires the source system roles to be accurate.')
t('promptinjection', 'Treat retrieved content as untrusted and guard against injected instructions',
  'Documents can contain text that tries to redirect the model. The design must separate instructions from content.')
t('audit', 'Log prompts, sources, and outputs for audit and investigation',
  'Audit records make an incident reconstructable. They also create a retention obligation that privacy review must accept.')
t('residency', 'Keep processing inside the approved region',
  'Residency commitments are contractual, not technical preferences. The model and data services must both be in scope.')
t('keyless', 'Use managed identities instead of embedded keys',
  'Identity-based access removes secrets from configuration. It requires role assignments and a rotation-free design.')

t('mlwhen', 'Use machine learning when the pattern is stable and examples are plentiful',
  'Learning from examples works when the relationship persists and history is representative. Otherwise the model learns noise.')
t('mlnotwhen', 'Keep the decision as a rule when policy must be exact and auditable',
  'Some decisions must be identical for every case and explainable on demand. A rule is then the correct tool.')
t('lifecycle', 'Manage data preparation, training, evaluation, deployment, and monitoring as one lifecycle',
  'A lifecycle view keeps the model tied to the data and checks that produced it. Treating deployment as the end of the project causes silent decay.')
t('drift', 'Monitor inputs and outcomes for drift after deployment',
  'Drift monitoring catches a model whose world has changed. It needs a labelled outcome feed to be meaningful.')
t('retrain', 'Schedule retraining when drift or new cases appear',
  'Retraining restores accuracy as behaviour shifts. It needs a repeatable evaluation so a retrain cannot silently regress.')
t('baseline', 'Compare the model against the current process baseline',
  'A model is only useful if it beats what the team does today. The baseline also makes the benefit measurable.')

# --- Domain 2: Microsoft AI apps and services -------------------------------
t('meetingsum', 'Summarize meetings and capture actions in Teams',
  'Meeting recap reduces note-taking and follow-up drift. It depends on the meeting being recorded or transcribed with consent.')
t('inbox', 'Draft replies and summarize long email threads',
  'Drafting in the mail client saves typing time and keeps context. A person still decides what is sent.')
t('deckdraft', 'Draft slides from an approved document outline',
  'Presentation drafting turns existing content into a first deck. The narrative and the numbers still need a human check.')
t('excelsum', 'Analyze a spreadsheet and explain the trends',
  'Spreadsheet analysis answers questions about the data in place. It inherits every quality problem in the workbook.')
t('policyqa', 'Answer policy questions from approved intranet content',
  'Intranet-grounded answers respect existing permissions. Coverage depends on the pages being current and well structured.')
t('crmfollow', 'Draft follow-ups from customer records through a connector',
  'Connector-based drafting reaches business systems beyond Microsoft 365. It needs connector governance and a data-flow review.')

t('m365copilot', 'License Microsoft 365 Copilot per user for in-app and work-data grounding',
  'The per-user licence grounds answers in the tenant and works inside the apps people already use. It is priced per seat, so targeting matters.')
t('copilotchat', 'Use Copilot Chat for web-grounded answers with enterprise data protection',
  'Chat covers general questions and file uploads inside a protected boundary. It is not the full in-app experience for licensed users.')
t('consumer', 'Use the free consumer Copilot for personal tasks',
  'The consumer offering is fine for individual experimentation but is not governed by the organization\'s compliance controls.')
t('copilotpro', 'Use a personal Copilot Pro subscription for individual productivity',
  'A personal subscription sits outside organizational identity and audit. It does not solve a team-level requirement.')
t('studio', 'Build a scoped agent in Microsoft Copilot Studio',
  'Copilot Studio builds an agent for a defined process with governed knowledge and connectors. It fits a repeatable task rather than general assistance.')

t('chatmobile', 'Answer questions on mobile between meetings',
  'Mobile chat supports quick lookups away from a desk. It suits short questions rather than long document work.')
t('chatfile', 'Upload a file to Copilot Chat for a quick summary',
  'File upload gives chat temporary context without changing the tenant index. It is a one-off convenience, not a grounded knowledge base.')
t('chatweb', 'Ground answers in public web content with citations',
  'Web grounding is useful for external topics and shows its sources. It is not authoritative for internal policy.')
t('chatboundary', "Keep chat traffic inside the tenant's data protection boundary",
  'The enterprise chat experience keeps prompts and responses inside existing compliance commitments. This distinction decides whether staff may use it for work content.')

t('worddraft', 'Draft and rewrite sections in Word with the document as context',
  'In-app drafting works from the open document, which keeps tone and terminology consistent. It still needs an editorial pass.')
t('outlookdraft', 'Summarize a long thread and draft a reply in Outlook',
  'Thread summaries recover context quickly and the reply starts in the right voice. Confidentiality markings still depend on the label.')
t('teamsrecap', 'Recap a Teams meeting with decisions, actions, and owners',
  'A recap turns a recording into a usable record. Transcription quality and consent determine whether it can be used.')
t('excelanalysis', 'Analyze a workbook and produce a chart with commentary',
  'In-app analysis keeps the work next to the data and its formulas. The commentary must be checked against the underlying numbers.')
t('pptbuild', 'Build a first draft deck from a Word document',
  'Converting a document into slides saves formatting time. The story still needs a human editor.')
t('loopcoauthor', 'Co-author a shared page and summarize decisions in Loop',
  'Collaborative pages keep working notes and decisions in one place. They are not a records-management system.')

t('topic', 'Author explicit topics with trigger phrases in Copilot Studio',
  'Topics give deterministic answers for known intents. They are predictable but need maintenance as processes change.')
t('knowledge', 'Connect approved SharePoint or website knowledge to the agent',
  'Knowledge sources let a low-code agent answer from content the business already owns. Retrieval quality depends on the source.')
t('connector', 'Call a business system through a Power Platform connector',
  'Connectors let an agent read or act on line-of-business data. Each connector adds a data-flow and permission review.')
t('publish', 'Publish the agent to Teams for a restricted audience',
  'A restricted audience keeps a young agent with a tolerant group while it improves. It is a rollout control, not a security boundary by itself.')
t('analytics', 'Review session transcripts and unresolved questions monthly',
  'Transcript review shows what the agent could not answer. It is the cheapest source of improvement ideas.')
t('lowcode', 'Keep the agent low-code so the business can maintain it',
  'Business ownership keeps content and topics current. Complex integrations may still need professional development.')

t('graphconnector', 'Index an external system through a Microsoft Graph connector',
  'A Graph connector brings third-party content into the same search and grounding surface. It requires mapping identities and permissions correctly.')
t('semindex', 'Rely on the Microsoft 365 semantic index for work content',
  'The semantic index makes tenant content retrievable by meaning. It only knows what has been indexed and permitted.')
t('graphperm', 'Honor Microsoft 365 permissions in grounding',
  'Permission trimming prevents an answer from revealing a document the user cannot open. It is the core control for grounded assistants.')
t('graphapi', 'Query organizational relationships through Microsoft Graph',
  'Graph exposes people, org charts, and files as structured data. It is a platform interface, not an end-user product.')

t('oneboundary', 'Keep identity, compliance, and DLP inside one Microsoft 365 boundary',
  'One boundary means existing controls apply to AI output without a parallel governance model. It is the main argument for an integrated suite.')
t('auditunified', 'Use unified audit logs across apps and agents',
  'Unified audit shortens investigation because events sit together. It depends on the relevant workloads being enabled.')
t('sensitivity', 'Let sensitivity labels protect generated content automatically',
  'Inherited labels keep protection on output derived from protected input. Unlabelled sources get no protection.')
t('banonly', 'Ban unsanctioned AI tools without offering an approved alternative',
  'A ban without an alternative pushes usage to personal accounts outside governance. It reduces visibility rather than risk.')

t('researcher', 'Use Researcher for a multi-source investigation brief',
  'Researcher plans and gathers across sources to produce a cited brief. It suits open-ended analysis where speed matters more than a fixed template.')
t('analyst', 'Use Analyst to analyze a dataset and produce a chart',
  'Analyst works on data with calculations and produces visual output. It is for quantitative questions, not narrative research.')
t('quickopinion', 'Ask a chat model for a one-paragraph opinion instead',
  'A quick opinion gives no traceable evidence. It is unsuitable when the output must be defended.')

t('buy', 'Buy licences for a standard process with no unique requirement',
  'Buying is fastest when the need matches the product. It is the wrong choice when the process depends on a system the product cannot reach.')
t('extend', 'Extend Copilot with a declarative agent and a Graph connector',
  'Extension adds your data and instructions to the existing assistant. It keeps the suite experience while closing a specific gap.')
t('build', 'Build a custom agent in Copilot Studio with connectors and topics',
  'Building gives full control of the conversation and the systems it reaches. It carries ownership and maintenance cost.')
t('customapp', 'Commission a custom application with a model API',
  'A custom application is justified when the workflow does not resemble an assistant at all. It is the most expensive option to operate.')
t('declarative', 'Declare instructions and knowledge without writing custom code',
  'Declarative agents configure behaviour and sources rather than code. They are quick to ship and limited to the platform\'s capabilities.')

t('foundry', 'Host models and agents in Microsoft Foundry',
  'Foundry provides model choice, evaluation, and agent hosting in one project. It is a platform decision, not a user-facing product.')
t('azurevision', 'Use Azure Vision in Foundry Tools for image analysis',
  'Vision services read images and video for objects, text, and captions. Accuracy depends on image quality and the task.')
t('aisearch', 'Use Azure AI Search for enterprise retrieval with semantic ranking',
  'AI Search indexes your content and ranks results for relevance. It becomes the retrieval layer under a grounded application.')
t('docintel', 'Use document intelligence to extract structured fields',
  'Field extraction turns forms into data with per-field confidence. It needs a labelled sample to prove accuracy.')
t('speech', 'Use speech services for transcription and captions',
  'Speech services convert audio to text and back. Accents, noise, and domain vocabulary drive quality.')
t('contentund', 'Use Content Understanding for multimodal extraction',
  'Content Understanding combines text, layout, and images into structured output. It suits complex documents that defeat simple extraction.')

t('smallmodel', 'Choose a small, fast model for high-volume, low-complexity drafting',
  'A small model is cheaper and faster for routine work. It degrades on multi-step reasoning and long context.')
t('largest', 'Choose the largest model for every request to maximize quality',
  'The largest model raises cost and latency on every call. It is rarely justified for simple, repetitive tasks.')
t('reasoning', 'Choose a reasoning-capable model for multi-step analysis',
  'Reasoning models spend more compute on planning and analysis. They fit complex decisions, not short lookups.')
t('multimodal', 'Choose a multimodal model when input includes images or scanned pages',
  'Multimodal models read images alongside text. They are unnecessary when the input is already clean text.')
t('capacityfit', 'Match model capacity to expected concurrency and latency targets',
  'Capacity planning keeps latency predictable under load. It requires a load test rather than an estimate.')
t('opensourcemodel', 'Choose an open-weight model for portability and cost control',
  'Open weights can reduce lock-in and unit cost at scale. They add hosting and evaluation responsibility.')

# --- Domain 3: responsible AI and adoption ---------------------------------
t('fairness', 'Test outcomes across customer groups for disparate impact',
  'Fairness testing compares outcomes by group to find systematic disadvantage. It needs enough labelled cases per group.')
t('reliability', 'Validate the system against realistic inputs before launch',
  'Reliability testing uses messy, real inputs rather than curated demos. It finds the failures customers would find.')
t('privacy', 'Minimize personal data and apply retention limits',
  'Data minimization reduces what a leak or misuse could expose. Retention limits stop old prompts becoming a permanent record.')
t('inclusiveness', 'Test with assistive technology and diverse users',
  'Inclusive testing finds barriers that a homogeneous pilot misses. It is cheaper before launch than after.')
t('transparency', 'Publish what the system does and where it is used',
  'Disclosure lets customers and staff calibrate trust. It also forces the team to describe limits in plain language.')
t('accountability', 'Name a human owner for each AI system',
  'A named owner makes decisions and incidents actionable. Shared ownership in practice means none.')
t('safety', 'Add layered controls for harmful content',
  'Layered controls catch harms at input, output, and review. Each layer has false positives that need an escalation path.')
t('raipriority', 'Treat responsible AI as a condition of adoption, not a compliance afterthought',
  'Adoption stalls when trust breaks, and trust is built by design choices. Treating responsible AI as a gate protects the programme.')

t('council', 'Stand up an AI council with legal, security, data, and business representation',
  'A cross-functional council sets priorities and resolves conflicts once. It needs decision rights, not just a meeting.')
t('decisionrights', 'Publish which body approves high-risk use cases',
  'Clear decision rights stop teams from shopping for a friendly reviewer. They also shorten approval for low-risk work.')
t('crossfunc', 'Rotate council membership across functions',
  'Rotation spreads literacy and reduces a single team\'s bottleneck. It costs continuity, so the charter must outlast individuals.')
t('escalation', 'Define an escalation path for harmful or disputed output',
  'A defined path gets a serious case to the right owner quickly. Without it, incidents are handled ad hoc.')

t('impactassessment', 'Complete an impact assessment before the pilot',
  'An assessment records who is affected and what could go wrong. It turns a vague risk discussion into named controls.')
t('oversight', 'Keep a human decision point for consequential outcomes',
  'Human oversight is required where an error changes someone\'s rights, money, or safety. The reviewer needs the evidence, not just the output.')
t('modelcard', 'Document the model, data, and known limits in a model card',
  'A model card tells a future team what the system can and cannot do. It is only useful if it is updated with the system.')
t('incidentregister', 'Track incidents and corrective actions in a register',
  'A register shows whether the same failure keeps happening. It converts individual fixes into programme learning.')
t('reviewcadence', 'Review high-risk systems on a fixed cadence',
  'Scheduled review catches drift in behaviour and in the business context. It also keeps documentation current.')
t('redteamgov', 'Commission an independent review of the highest-risk use case',
  'Independent review challenges assumptions the delivery team cannot see. It is most valuable before a public launch.')

t('adoptionteam', 'Name an adoption lead with protected time',
  'Adoption work competes badly with delivery work unless someone owns it. Protected time makes the role real.')
t('champions', 'Recruit champions in each business unit',
  'Champions answer peer questions faster than a central team can. They need training and a route to escalate problems.')
t('community', 'Run a monthly community of practice',
  'A community shares patterns and prevents duplicated mistakes. It sustains itself only with a light, regular format.')
t('training', 'Deliver role-based training with approved scenarios',
  'Training built on the learner\'s own tasks transfers better than generic feature tours. It also sets the boundary of approved use.')
t('officehours', 'Offer weekly office hours for questions',
  'Office hours give a low-friction route for the awkward questions that block use. Attendance is a useful adoption signal.')
t('successstories', 'Publish measured wins from early teams',
  'A measured story persuades a sceptical manager better than a feature list. Unmeasured enthusiasm does the opposite.')

t('fear', 'Address job-loss concerns with a clear role-change plan',
  'Unspoken fear drives quiet resistance. A concrete plan for how roles change reduces it more than reassurance.')
t('skillsgap', 'Provide hands-on practice, not only awareness sessions',
  'Awareness explains what is possible; practice changes what people do. Without practice, licences go unused.')
t('unclearvalue', 'Tie the pilot to one measurable business metric',
  'A single metric keeps the pilot honest and gives the sponsor something to defend. Too many metrics dilute the result.')
t('policylag', 'Publish an acceptable-use policy before the rollout',
  'Staff need to know what is allowed before they experiment. A late policy turns early enthusiasm into rework.')
t('shadowai', 'Offer an approved alternative to unsanctioned tools',
  'People adopt shadow tools when the approved path is slow or missing. A usable alternative brings the work back inside governance.')
t('sponsor', 'Secure an executive sponsor who removes blockers',
  'A sponsor resolves policy and funding conflicts the team cannot. Without one, adoption stalls at the first obstacle.')
t('pilotgroup', 'Start with a willing team that has clean data',
  'An early win needs a group motivated to change and data that works. A hostile pilot proves nothing about the tool.')

t('oversharing', 'Fix oversharing in SharePoint before enabling Copilot',
  'Grounding surfaces whatever the user can already open, including files that should not be broadly visible. Permissions cleanup is a prerequisite.')
t('retention', 'Confirm retention and residency obligations for prompts and outputs',
  'Prompts and responses are records under some regimes. Retention rules must be decided before the data exists.')
t('costvisibility', 'Allocate licence and consumption cost to business units',
  'Cost allocation turns AI spend into a business decision per unit. Unallocated spend invites an across-the-board cut.')
t('capacityplan', 'Forecast licence demand from active-user data',
  'Active-use data prevents buying seats for people who never open the tool. It also shows where enablement is failing.')
t('privacyreview', 'Complete a privacy review for personal data in prompts',
  'Prompts can contain personal data that no system of record tracks. A review decides what may be entered.')
t('dataclassify', 'Classify the data before deciding what may be processed',
  'Classification tells you which content may enter which service. It is the input to every other control decision.')

t('peruser', 'Buy per-user Microsoft 365 Copilot licences for full-time users',
  'Per-user licensing fits people who use the assistant daily inside the apps. It is expensive for occasional users.')
t('includedchat', 'Rely on the Copilot Chat entitlement included with Microsoft 365 for occasional use',
  'The included chat covers light, web-grounded use inside a protected boundary. It does not include the full in-app experience.')
t('paygstudio', 'Use pay-as-you-go consumption for Copilot Studio agents with variable demand',
  'Consumption pricing follows actual agent use. It becomes expensive and hard to forecast at steady high volume.')
t('monthlycommit', 'Buy a monthly commitment for a stable, growing agent workload',
  'A commitment lowers unit cost when usage is predictable. It wastes money if the agent is not adopted.')
t('limitedpilot', 'Pilot with a limited number of licences before a broad purchase',
  'A small purchase tests adoption and value before a large commitment. It needs a decision date, or the pilot becomes the plan.')
t('avoidover', 'Avoid premium licences for users who only need chat',
  'Matching licence to usage keeps cost proportional to value. Over-licensing hides the true cost per active user.')

t('paygfoundry', 'Start Foundry Tools on pay-as-you-go',
  'Consumption pricing keeps the first workload cheap to test. It is unpredictable once traffic is steady.')
t('commitment', 'Move predictable Foundry usage to a commitment tier',
  'A commitment tier discounts predictable volume. It requires a usage baseline from a real period.')
t('reservation', 'Reserve capacity only after measuring steady usage',
  'Reservations pay off against measured baselines. Buying before measurement locks in an estimate.')
t('chargeback', 'Charge consumption back to the owning team',
  'Chargeback makes the team that benefits pay for the usage. It changes behaviour far more than a central budget.')

# --- Ordering sequences -----------------------------------------------------
t('seqadoptok', 'Frame the business problem → record baseline metrics → pilot with a control group → measure outcomes → scale or stop',
  'The problem and baseline come first, the pilot compares against them, and the decision follows the measurement.')
t('seqadoptbad1', 'Pilot with a control group → frame the business problem → measure outcomes → record baseline metrics → scale or stop',
  'A pilot cannot be designed before the problem and baseline exist.')
t('seqadoptbad2', 'Scale to every team → pilot with a control group → frame the business problem → record baseline metrics → measure outcomes',
  'Scaling before the pilot inverts the whole sequence.')
t('seqadoptbad3', 'Measure outcomes → record baseline metrics → frame the business problem → pilot with a control group → scale or stop',
  'Outcomes cannot be measured before a baseline and a pilot exist.')

t('seqpromptok', 'Describe the task and audience → supply approved examples → state the output format and constraints → review the output with users → version the prompt',
  'Task, examples, and constraints set the request, review validates it, and versioning preserves what worked.')
t('seqpromptbad1', 'State the output format → describe the task and audience → version the prompt → review the output with users → supply approved examples',
  'The format cannot precede the task description, and versioning cannot precede review.')
t('seqpromptbad2', 'Version the prompt → review the output with users → describe the task and audience → supply approved examples → state the output format',
  'A prompt cannot be versioned before it is written and reviewed.')
t('seqpromptbad3', 'Review the output with users → describe the task and audience → supply approved examples → version the prompt → state the output format',
  'Review needs an output, which needs the task, examples, and format first.')

t('seqragok', 'Define the business question → confirm the authoritative sources → index with permissions applied → retrieve passages into the prompt → review answers for accuracy',
  'Question and sources come before indexing, indexing before retrieval, and accuracy review comes last.')
t('seqragbad1', 'Index with permissions applied → define the business question → retrieve passages into the prompt → review answers for accuracy → confirm the authoritative sources',
  'Indexing before the question and sources risks indexing the wrong content.')
t('seqragbad2', 'Retrieve passages into the prompt → index with permissions applied → define the business question → confirm the authoritative sources → review answers for accuracy',
  'Retrieval cannot happen before the index exists.')
t('seqragbad3', 'Review answers for accuracy → retrieve passages into the prompt → define the business question → index with permissions applied → confirm the authoritative sources',
  'There are no answers to review before retrieval and indexing.')

t('seqgovernok', 'Inventory the AI use cases → classify each by risk → assign an accountable reviewer → record the controls in a register → review on a fixed cadence',
  'Inventory and risk classification decide the reviewer, the register records controls, and the cadence keeps them current.')
t('seqgovernbad1', 'Assign an accountable reviewer → inventory the AI use cases → classify each by risk → review on a fixed cadence → record the controls in a register',
  'A reviewer cannot be assigned before the use cases and their risk are known.')
t('seqgovernbad2', 'Record the controls in a register → inventory the AI use cases → assign an accountable reviewer → classify each by risk → review on a fixed cadence',
  'Controls cannot be recorded before the risk classification decides them.')
t('seqgovernbad3', 'Review on a fixed cadence → classify each by risk → inventory the AI use cases → assign an accountable reviewer → record the controls in a register',
  'A review cadence presupposes a register and assigned owners.')

t('seqcopilotok', 'Identify the process step → confirm the content is in Microsoft 365 with correct permissions → choose the Copilot experience → pilot with one team → measure time saved',
  'The step and the content come first, then the experience and the pilot, with measurement at the end.')
t('seqcopilotbad1', 'Choose the Copilot experience → identify the process step → measure time saved → confirm the content is in Microsoft 365 → pilot with one team',
  'The experience cannot be chosen before the process and its content are understood.')
t('seqcopilotbad2', 'Pilot with one team → identify the process step → choose the Copilot experience → confirm the content is in Microsoft 365 → measure time saved',
  'A pilot without a defined process or experience is not a controlled test.')
t('seqcopilotbad3', 'Measure time saved → pilot with one team → identify the process step → confirm the content is in Microsoft 365 → measure time saved',
  'There is no baseline to save time against before the pilot runs.')

t('seqagentok', "Define the agent's job → connect approved knowledge → test with real questions → publish to a restricted audience → review sessions and update knowledge",
  'Scope and knowledge precede testing, testing precedes publishing, and review closes the loop.')
t('seqagentbad1', 'Connect approved knowledge → define the agent\'s job → publish to a restricted audience → test with real questions → review sessions and update knowledge',
  'Knowledge is connected to serve a job that has not been defined, and publishing precedes testing.')
t('seqagentbad2', 'Publish to a restricted audience → test with real questions → define the agent\'s job → connect approved knowledge → review sessions and update knowledge',
  'Publishing then testing exposes users to an unvalidated agent.')
t('seqagentbad3', 'Review sessions and update knowledge → publish to a restricted audience → define the agent\'s job → connect approved knowledge → test with real questions',
  'There are no sessions to review before the agent is published.')

t('seqdataok', 'Classify the data → apply sensitivity labels → restrict the index to entitled users → enable audit logging → review access on a schedule',
  'Classification drives labelling, labelling drives the index scope, and audit plus review keep it true over time.')
t('seqdatabad1', 'Restrict the index to entitled users → classify the data → apply sensitivity labels → review access on a schedule → enable audit logging',
  'The index scope cannot be decided before classification and labelling.')
t('seqdatabad2', 'Enable audit logging → restrict the index to entitled users → classify the data → apply sensitivity labels → review access on a schedule',
  'Audit before classification records activity against the wrong boundary.')
t('seqdatabad3', 'Review access on a schedule → enable audit logging → classify the data → restrict the index to entitled users → apply sensitivity labels',
  'Scheduled review needs an existing scope and audit trail.')

t('seqlicenceok', 'Model the usage demand → compare licence options → run a paid pilot → review cost per active user → commit to a licence mix',
  'Demand modelling and comparison shape the pilot, and the commitment follows measured cost per active user.')
t('seqlicencebad1', 'Commit to a licence mix → model the usage demand → compare licence options → run a paid pilot → review cost per active user',
  'Committing before the pilot locks in an untested assumption.')
t('seqlicencebad2', 'Run a paid pilot → commit to a licence mix → model the usage demand → compare licence options → review cost per active user',
  'A pilot cannot be designed without demand modelling and an option comparison.')
t('seqlicencebad3', 'Review cost per active user → run a paid pilot → model the usage demand → compare licence options → commit to a licence mix',
  'Cost per active user cannot exist before a paid pilot.')

t('seqincidentok', 'Detect the harmful output → disable the affected feature → notify the accountable owner → correct the knowledge or prompt → record the incident and the prevention',
  'Containment precedes notification, the fix follows, and the record captures what prevents a repeat.')
t('seqincidentbad1', 'Notify the accountable owner → detect the harmful output → record the incident and the prevention → disable the affected feature → correct the knowledge or prompt',
  'Notification cannot precede detection, and the record cannot precede the fix.')
t('seqincidentbad2', 'Correct the knowledge or prompt → detect the harmful output → disable the affected feature → record the incident and the prevention → notify the accountable owner',
  'A correction without detection is guesswork, and the owner learns last.')
t('seqincidentbad3', 'Record the incident and the prevention → correct the knowledge or prompt → notify the accountable owner → detect the harmful output → disable the affected feature',
  'The record and the fix precede the detection they depend on.')

t('seqmodelok', 'Describe the task and data → shortlist candidate models → evaluate on representative samples → compare cost and latency → deploy the smallest model that passes',
  'Requirements drive the shortlist, evaluation drives the comparison, and the cheapest passing model is deployed.')
t('seqmodelbad1', 'Deploy the smallest model that passes → describe the task and data → evaluate on representative samples → compare cost and latency → shortlist candidate models',
  'Deployment cannot precede the evaluation that proves the model passes.')
t('seqmodelbad2', 'Compare cost and latency → shortlist candidate models → describe the task and data → deploy the smallest model that passes → evaluate on representative samples',
  'Cost comparison needs evaluated candidates, which need the task definition first.')
t('seqmodelbad3', 'Shortlist candidate models → deploy the smallest model that passes → describe the task and data → evaluate on representative samples → compare cost and latency',
  'The shortlist and the choice of model require the task definition.')

t('seqmlok', 'Frame the business question → prepare and label representative data → train the model → evaluate against the current baseline → deploy and monitor for drift',
  'The question and data precede training, evaluation precedes deployment, and monitoring continues after it.')
t('seqmlbad1', 'Train the model → frame the business question → prepare and label representative data → deploy and monitor for drift → evaluate against the current baseline',
  'Training without a framed question or prepared data produces an unusable model.')
t('seqmlbad2', 'Evaluate against the current baseline → train the model → frame the business question → prepare and label representative data → deploy and monitor for drift',
  'Evaluation requires a trained model and a baseline from the current process.')
t('seqmlbad3', 'Deploy and monitor for drift → evaluate against the current baseline → frame the business question → train the model → prepare and label representative data',
  'Deployment cannot come before training and evaluation.')

t('seqchampionsok', 'Recruit champions from each function → train them on approved scenarios → give them a channel to raise problems → publish measured wins → expand the network',
  'Recruitment and training build capability, the channel fixes blockers, and published wins justify expansion.')
t('seqchampionsbad1', 'Publish measured wins → recruit champions from each function → train them on approved scenarios → expand the network → give them a channel to raise problems',
  'There are no wins to publish before champions are trained and working.')
t('seqchampionsbad2', 'Expand the network → recruit champions from each function → publish measured wins → train them on approved scenarios → give them a channel to raise problems',
  'Expansion before recruitment and training spreads an unready programme.')
t('seqchampionsbad3', 'Give them a channel to raise problems → expand the network → recruit champions from each function → train them on approved scenarios → publish measured wins',
  'A channel and expansion cannot precede the champions they serve.')
