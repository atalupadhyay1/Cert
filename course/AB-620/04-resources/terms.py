"""Original AB-620 alternative labels and explanatory definitions."""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: plan and configure agent solutions ---------------------------
# 1.1 Enterprise integration and solution planning
t('entgateway', 'Mediate the on-premises call through an on-premises data gateway',
  'A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor.')
t('entvirtual', 'Expose the system through a virtual table or connector view that the agent can read',
  'A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries.')
t('entdirect', 'Call the internal endpoint straight from the topic over HTTP',
  'Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides.')
t('entfabric', 'Mirror the source into Microsoft Fabric and query it with a Fabric data agent',
  'Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data.')
t('entdump', 'Copy the records nightly into Dataverse and answer from the copy',
  'A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation.')
t('entbatch', 'Batch the requests and post them to the source system on a schedule',
  'Batching suits bulk work, not a conversation that expects an answer in seconds.')

# 1.2 Identity strategy and authentication
t('identra', 'Require Microsoft Entra ID sign-in for the agent and pass the user token downstream',
  'User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection.')
t('idobo', 'Use the on-behalf-of flow so the agent calls the API as the signed-in user',
  'On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client.')
t('idsvc', 'Give every conversation a single shared service account credential for the API',
  'One shared account is easy to set up and destroys per-user accountability and least privilege.')
t('idanonymous', 'Allow anonymous access to the agent and authenticate only at the API',
  'Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API.')
t('idapikey', 'Store one API key in a topic variable and reuse it for every user',
  'A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person.')
t('idexternal', 'Authenticate partners through external identities rather than internal tenant accounts',
  'External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms.')
t('idmanaged', 'Use the agent managed identity for Azure resources and keep user identity for business data',
  'Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant.')

# 1.3 Channels, deployment, and audience design
t('chanteams', 'Publish to Microsoft Teams and keep the agent inside the tenant',
  'Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account.')
t('chanweb', 'Publish to a public website with authenticated sign-in',
  'The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision.')
t('chanm365', 'Publish the agent into Microsoft 365 Copilot so it appears alongside other agents',
  'Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls.')
t('chanomni', 'Add the channel for omni-channel engagement so external support queues can route to it',
  'Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent.')
t('chandirectline', 'Embed the agent in a custom application through the Direct Line channel',
  'Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in.')
t('chanemail', 'Publish to email and answer asynchronously',
  'Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well.')

# 1.4 Responsible AI, security, and governance
t('govdlp', 'Apply a data loss prevention policy that blocks unapproved connectors in the environment',
  'Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service.')
t('govenv', 'Separate development and production environments with environment security groups',
  'Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout.')
t('govrbac', 'Restrict who can author and publish with Copilot Studio security roles',
  'Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group.')
t('govaudit', 'Turn on audit logging and retain agent conversation records',
  'Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever.')
t('govinject', 'Constrain the tools the agent may call, validate tool output, and limit autonomous actions',
  'Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions.')
t('govacl', 'Enforce the source system’s permissions in the knowledge layer so answers respect access',
  'An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt.')

# 1.5 Reusable agent components and solutions
t('reusecomponent', 'Extract the shared logic into a reusable component or child agent and reference it',
  'One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed.')
t('reusecopy', 'Copy the topics into each agent so every team can edit its own copy',
  'Copies diverge quickly, and a fix has to be repeated in every agent that holds one.')
t('reusesolution', 'Package the shared topics, flows, and connection references in a solution',
  'A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components.')
t('reuseenvvar', 'Parameterize environment-specific values with environment variables',
  'Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault.')
t('reuseduplicate', 'Rebuild the same topic in each agent to avoid a shared dependency',
  'Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers.')
t('reusecustomconnector', 'Expose the shared integration as a custom connector any agent can add as a tool',
  'A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once.')

# 1.6 Agent flows, actions, and connectors
t('flowmanual', 'Create an agent flow with a manual trigger that the topic calls with inputs',
  'A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic.')
t('flowautomated', 'Use an automated cloud flow triggered by an event and have the agent wait for it',
  'Event flows are right for background work, but a conversation cannot block on an event that may never arrive.')
t('flowconnector', 'Create the flow with the connector action the agent needs and return the result',
  'The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling.')
t('flowparams', 'Define typed input and output parameters on the flow and bind them from the topic',
  'Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure.')
t('flowaction', 'Add the capability as a connector action so the agent can call it without a flow',
  'A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description.')
t('flowerror', 'Wrap the calls in a scope with a parallel error branch that returns a structured failure',
  'Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes.')

# 1.7 Human-in-the-loop agent flows
t('hitlapproval', 'Send an approval request and pause the flow until a person responds',
  'Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome.')
t('hitlcard', 'Post an adaptive card to Teams and wait for the human decision before continuing',
  'A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection.')
t('hitlauto', 'Let the agent complete the action and notify a person afterwards',
  'Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action.')
t('hitlhandoff', 'Hand the conversation off to a live agent with the context attached',
  'A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval.')
t('hitldraft', 'Have the agent draft the action and require a person to submit it in the source system',
  'Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail.')
t('hitltimeout', 'Set a response timeout and route to a fallback owner when nobody answers',
  'A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live.')

# 1.8 Flow parameters, error handling, and monitoring
t('monrunhistory', 'Review the flow run history and its action-level inputs and outputs',
  'Run history shows which action failed and what it received. It is the fastest first stop for a failing flow.')
t('monappinsights', 'Send flow telemetry to Application Insights and query the traces',
  'Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent.')
t('monalert', 'Configure an alert on failed runs and route it to the owning team',
  'An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly.')
t('monretry', 'Configure a retry policy and terminate with a failure code the topic can read',
  'Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation.')
t('monanalytics', 'Use the Copilot Studio analytics view for session and topic outcomes',
  'Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace.')
t('moncomment', 'Add a comment step to the flow describing the expected failure',
  'A comment documents intent for the next author but changes nothing about how the run behaves.')

# 1.9 Topics, response formatting, and variables
t('topredirect', 'Configure the topic as a redirect target with its own trigger phrases',
  'Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered.')
t('topscope', 'Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns',
  'Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations.')
t('topglobal', 'Store the value in a global variable so later topics can read it',
  'Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic.')
t('topformat', 'Configure the message node to send a formatted message with the fields the user needs',
  'A message node can send structured text without a card. It is the lightest way to make a list readable.')
t('topcard', 'Return an adaptive card so the data renders in labelled fields',
  'Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them.')
t('topplain', 'Return the raw flow output as plain text',
  'Raw output is quick to build and hard to read, especially when a field is empty or very long.')

# 1.10 Custom prompts, adaptive cards, and generative answers
t('genknowledge', 'Point the generative answers node at the specific knowledge source for the question',
  'Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content.')
t('genprompt', 'Configure a custom prompt that fixes the tone, structure, and citation behaviour',
  'Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it.')
t('genfallback', 'Add a fallback topic for low-confidence answers that hands off to a person',
  'A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure.')
t('cardschema', 'Design the adaptive card schema and bind the flow outputs to its fields',
  'The schema is the contract between the flow and the card. Binding by name keeps the card stable when the flow adds fields.')
t('cardimage', 'Return an image with the card so the response looks richer',
  'Images can help recognition but add nothing when the question is about a value or a status.')
t('gengrounded', 'Require the answer to cite retrieved passages and refuse when none are found',
  'Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable.')

# --- Domain 2: integrate and extend agents ----------------------------------
# 2.1 Copilot and Power Platform connectors
t('conncopilot', 'Connect the source through a Copilot connector so its content is indexed for answers',
  'A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge.')
t('connpp', 'Connect through a Power Platform connector and query it from a tool or flow',
  'A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text.')
t('connaisearch', 'Index the content in Azure AI Search and use it as the knowledge source',
  'AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable.')
t('connupload', 'Upload the documents as file knowledge on the agent',
  'File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself.')
t('connsharepoint', 'Add the SharePoint site as a knowledge source and rely on item-level permissions',
  'SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope.')
t('connsql', 'Register the database as a knowledge source so the agent can query it directly',
  'Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping.')

# 2.2 Azure AI Search grounding
t('srchindex', 'Create the index with the fields, vector profile, and semantic configuration the agent needs',
  'The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later.')
t('srchfilter', 'Apply a security filter on the query before the agent composes an answer',
  'Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers.')
t('srchsemantic', 'Enable semantic ranking and let the agent use the reranked results',
  'Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota.')
t('srchhybrid', 'Use hybrid retrieval with vector and keyword queries',
  'Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost.')
t('srchrecreate', 'Recreate the index on every publish so it never goes stale',
  'Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users.')
t('srchprivate', 'Connect to the search service over a private endpoint with managed identity',
  'Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live.')

# 2.3 Computer use agents
t('cudesktop', 'Configure a computer use tool against the legacy desktop application',
  'Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored.')
t('cumachine', 'Provision a machine or machine group and run the tool there with a dedicated account',
  'The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable.')
t('cuapi', 'Replace the screen automation with an API once the application exposes one',
  'An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure.')
t('cumonitor', 'Monitor computer use runs and capture step screenshots for review',
  'Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules.')
t('cuunattended', 'Run the tool unattended on a dedicated machine with a vaulted credential',
  'Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on.')
t('cuunchecked', 'Record the click path once and reuse it without validating each run',
  'An unvalidated click path will eventually click the wrong control after an application update.')

# 2.4 MCP tools
t('mcpserver', 'Add an MCP server as a tool and let the agent discover the tools it exposes',
  'MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent.')
t('mcpcustom', 'Wrap the internal API as MCP tools and register the server endpoint with the agent',
  'Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation.')
t('mcpauth', 'Configure the MCP server connection with the authentication the server requires',
  'Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails.')
t('mcphttp', 'Use a streamable HTTP MCP server so the agent can reach it over the network',
  'Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client.')
t('mcpstdio', 'Embed the MCP server as a local process inside the agent',
  'A local process transport does not exist in a hosted agent, so the server must be reachable over the network.')
t('mcpscope', 'Expose only the MCP tools the task needs and review their descriptions',
  'Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate.')

# 2.5 Custom connectors and REST APIs
t('restopenapi', 'Create a custom connector from the OpenAPI definition and add it as a tool',
  'An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents.')
t('resttopic', 'Call the REST API from a topic with a Send HTTP request action',
  'Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling.')
t('restflow', 'Call the API from an agent flow and return the parsed response to the topic',
  'A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping.')
t('restauth', 'Configure connector authentication so each call uses the caller’s identity',
  'Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key.')
t('resthardcode', 'Hard-code the endpoint URL and key inside the topic',
  'Credentials in a topic are visible to every maker in the environment and cannot be rotated safely.')
t('restschema', 'Define the response schema so the agent can reason over the returned fields',
  'A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer.')

# 2.6 Multi-agent design
t('machild', 'Split the work into a parent agent that delegates to specialist child agents',
  'Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies.')
t('maone', 'Build one large agent with every topic so there is a single place to change',
  'One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour.')
t('mainstructions', 'Write the parent’s instructions to describe when each child should be used',
  'Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating.')
t('macontract', 'Give each child a clear input and output contract and keep shared state in the parent',
  'Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth.')
t('maroute', 'Route by intent in the parent and pass only the context the child needs',
  'Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding.')
t('masharedkb', 'Give every child the same knowledge source so answers stay consistent',
  'A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally.')

# 2.7 Foundry agent integration
t('foundryagent', 'Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent',
  'A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing.')
t('foundrymodel', 'Deploy the model in Foundry and point the custom prompt at that deployment',
  'Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn.')
t('foundryeval', 'Evaluate the Foundry agent against the same test set before it is connected',
  'A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer.')
t('foundryendpoint', 'Expose the Foundry agent through its endpoint and authenticate with the agent’s identity',
  'Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary.')
t('foundryrebuild', 'Re-implement the Foundry agent’s logic as topics in Copilot Studio',
  'Rebuilding duplicates work that already exists and drifts as soon as either side changes.')
t('foundryground', 'Ground the Foundry agent in the same indexed knowledge so both layers answer consistently',
  'Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect.')

# 2.8 Connected and existing agents
t('existconnect', 'Add the existing agent as a connected agent and let the parent delegate to it',
  'Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it.')
t('existdup', 'Copy its topics into the new agent so both can be edited separately',
  'A copy forks the behaviour and doubles the maintenance from the first day.')
t('existconnector', 'Call the partner’s published API through a custom connector when delegation is unavailable',
  'A connector gives the parent a callable tool even when the other organisation will not expose a connected agent. The parent then owns retries and error handling.')
t('existdesc', 'Write a precise name and description for the connected agent so routing works',
  'The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures.')
t('existauth', 'Confirm the caller’s identity and permissions flow through to the connected agent',
  'Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context.')
t('existretire', 'Retire the duplicate standalone agent once the parent covers its use cases',
  'Leaving two entry points invites divergence and doubles the testing burden.')
t('existversion', 'Pin the connected agent’s published version that the parent was tested against',
  'An unpinned dependency can change behaviour between your test run and your release.')

# 2.9 Fabric data agents
t('fabricagent', 'Create a Fabric data agent over the semantic model and connect it to Copilot Studio',
  'A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures.')
t('fabricdax', 'Query the lakehouse directly from the agent with a SQL tool',
  'Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed.')
t('fabricperms', 'Grant the data agent’s identity read access to the semantic model only',
  'Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant.')
t('fabricmeasure', 'Define the measures in the semantic model so the data agent answers consistently',
  'Measures encode the agreed definition. Without them every question invites a new interpretation of revenue.')
t('fabricexport', 'Export the data nightly into files the agent can search',
  'A nightly export adds staleness and a second definition of the numbers the warehouse already owns.')
t('fabriccap', 'Check the data agent’s answer scope and add instructions for questions it must refuse',
  'Knowing the boundary prevents an analytical agent from improvising on operational questions it cannot answer.')

# 2.10 A2A protocol solutions
t('a2acard', 'Publish an agent card that describes the remote agent’s skills and endpoint',
  'The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded.')
t('a2askill', 'Model the remote capability as an A2A skill the agent can discover and invoke',
  'Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it.')
t('a2aauth', 'Configure authentication between the agents so calls are authorized',
  'Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door.')
t('a2alocal', 'Rebuild the remote agent’s functionality locally instead of using the protocol',
  'Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned.')
t('a2atask', 'Track the remote task state and surface long-running results back into the conversation',
  'A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running.')
t('a2atrust', 'Define which remote agents are trusted and restrict the skills exposed to them',
  'Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider.')

# 2.11 Foundry model catalog and custom prompts
t('modelselect', 'Choose a model from the catalog that meets quality, latency, and residency needs',
  'Model choice is a trade between answer quality, response time, cost, and where the data may be processed.')
t('modeldeploy', 'Deploy the chosen model and reference the deployment from the custom prompt',
  'A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable.')
t('modeleval', 'Compare candidate models on a sample of real cases before switching',
  'A side-by-side run on real questions is the only evidence that a cheaper model is still good enough.')
t('modeldefault', 'Keep the default model because it is already configured',
  'A default is a starting point, not a decision about quality or cost.')
t('modelquota', 'Provision enough quota and throughput for peak conversation volume',
  'Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average.')
t('modelregion', 'Deploy the model in a region that satisfies the data residency requirement',
  'Residency is a legal constraint, so region choice precedes price comparison.')

# 2.12 Application Insights monitoring
t('aiconnect', 'Connect the agent to Application Insights and emit conversation and tool telemetry',
  'Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt.')
t('aikql', 'Query conversation and tool spans in Application Insights with KQL',
  'KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers.')
t('aitrace', 'Correlate a failed answer with the tool call and knowledge retrieval behind it',
  'Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency.')
t('aisample', 'Sample telemetry so volume stays affordable while errors are always kept',
  'Sampling keeps cost predictable, and keeping errors makes the rare failure still visible.')
t('aialert', 'Alert on failed tool calls and answer-quality regressions',
  'An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise.')
t('ailogall', 'Log full conversation transcripts indefinitely without retention limits',
  'Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy.')

# --- Domain 3: test and manage agents ---------------------------------------
# 3.1 Test set design
t('testreal', 'Build the test set from real anonymized conversations plus the cases that must never fail',
  'Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys.')
t('testsynth', 'Generate synthetic cases from the topics and intents the agent supports',
  'Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language.')
t('testedge', 'Include adversarial and edge cases such as out-of-scope and injection attempts',
  'Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess.')
t('testsmall', 'Test with a handful of happy-path questions before release',
  'Happy-path-only testing passes almost any agent and predicts almost nothing about production.')
t('testholdout', 'Hold part of the set out of prompt tuning so results stay honest',
  'Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left.')
t('testversion', 'Version the test set and rerun it for every change',
  'A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression.')

# 3.2 Evaluation methods
t('evalgrader', 'Use model-based grading against a rubric and review a human sample',
  'Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated.')
t('evalhuman', 'Have subject-matter experts score a sample against the rubric',
  'Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader.')
t('evalkeyword', 'Score answers with keyword matching against expected phrases',
  'Keyword matching is cheap and blind to a correct answer phrased differently.')
t('evalgrounded', 'Measure groundedness by checking each claim against the retrieved passage',
  'Groundedness catches the failure that matters most in an enterprise agent: a fluent answer the source does not support.')
t('evaltopic', 'Measure topic-trigger accuracy separately from answer quality',
  'A right answer to the wrong intent still fails the user. Separating the measures tells you which layer to fix.')
t('evalmanual', 'Rely on the builder trying a few questions in the test pane',
  'The test pane is for development feedback, not for evidence about release quality.')

# 3.3 Reviewing and acting on results
t('rescluster', 'Group failures by topic and root cause instead of fixing items one at a time',
  'Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable.')
t('resregression', 'Compare the new run against the previous baseline before publishing',
  'A regression check catches the fix that repairs one case and breaks three.')
t('resthreshold', 'Set a pass threshold per category and block release below it',
  'Category thresholds stop a strong average from hiding a weak high-risk path.')
t('resignore', 'Publish when the overall average looks acceptable',
  'An average hides the cases that matter most, and it moves when the mix of cases changes.')
t('reslog', 'Keep failed cases in the test set so they cannot regress',
  'A fixed failure becomes a permanent test. Removing it invites the same defect back.')
t('resowner', 'Assign each failure cluster to the owner of the topic, prompt, or connector',
  'Ownership converts findings into changes. An unowned backlog does not improve the agent.')

# 3.4 Solution packaging for agents
t('solcreate', 'Create a solution and add the agent and its dependencies to it',
  'Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package.')
t('sollayer', 'Keep the agent in an unmanaged solution in development and ship a managed solution',
  'Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites.')
t('solpublisher', 'Set the publisher prefix before creating components so names stay consistent',
  'The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment.')
t('solexport', 'Export the managed solution and import it into the target environment',
  'Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival.')
t('solzip', 'Send the agents topic files to the administrator by email',
  'Topic files are not a supported deployment unit and carry no dependencies or version record.')
t('soldepend', 'Confirm every connection reference and environment variable is included before export',
  'A missing connection reference fails at import or, worse, at first use in production.')

# 3.5 Environment variables and configuration
t('envdef', 'Define an environment variable for the endpoint and set a value per environment',
  'Environment variables are how one solution behaves differently per environment without code changes.')
t('envsecret', 'Store the secret in a vault and reference it from the environment variable',
  'A vault-backed variable keeps the value out of the solution export and the design surface.')
t('envhard', 'Hard-code the production endpoint in the topic and change it after import',
  'Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review.')
t('envcurrent', 'Use the current value in production and a default value for development',
  'Current and default values cover the common two-environment split and are set explicitly per stage.')
t('envdeploy', 'Set the environment variable values as part of the pipeline deployment step',
  'Setting values during deployment removes the manual edit that people forget before a release.')
t('envdoc', 'Record the required values in the deployment notes for each environment',
  'Documentation helps a human but does not stop a deployment with a missing value.')

# 3.6 Power Platform pipelines
t('pipecreate', 'Create a pipeline with development, test, and production stages',
  'A staged pipeline makes promotion a recorded operation instead of a manual import.')
t('pipedeploy', 'Deploy the solution through the pipeline stages instead of importing manually',
  'Pipeline deployment carries the version history and the approvals with it.')
t('pipepre', 'Add a pre-deployment step that runs the agent test set and blocks on failure',
  'Testing before promotion is what turns a pipeline into a gate rather than a courier.')
t('pipeapprove', 'Require approval before the production stage runs',
  'An approval records who accepted the risk of the release. It must be a person who can read the test results.')
t('pipemanual', 'Import the solution by hand into production for each release',
  'Manual imports skip validation and leave no reliable record of what was deployed when.')
t('pipeeval', 'Use the pipeline analytics to see which stage failed and why',
  'Stage-level results shorten the loop between a failed run and the person who can fix it.')

# 3.7 Extending pipelines and deployment controls
t('pipexstep', 'Add a custom pipeline step that calls the validation job',
  'Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands.')
t('pipexvar', 'Pass environment-specific values through pipeline configuration rather than editing the solution',
  'Configuration belongs with the stage, not in the artefact, or every environment needs its own build.')
t('pipexrollback', 'Keep the previous managed solution version so you can roll back',
  'A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan.')
t('pipexschedule', 'Deploy on a fixed schedule regardless of readiness',
  'A schedule deploys whatever is in the source stage, including unfinished work.')
t('pipexnotify', 'Notify the owning team with the deployment result and the failed step',
  'A notification with the failing step is what lets the team respond in minutes rather than at the next standup.')
t('pipexscope', 'Deploy only the components that changed when the pipeline supports it',
  'Scoped deployment shortens the window and reduces the blast radius of a bad release.')

# 3.8 Production quality and continuous evaluation
t('prodmonitor', 'Sample production conversations and score them against the rubric on a schedule',
  'Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling.')
t('prodfeedback', 'Capture user feedback in the conversation and route negative cases to review',
  'Thumbs-down is a cheap signal that something is wrong, and the transcript says what.')
t('proddrift', 'Watch for knowledge-source changes and re-run the evaluation after they land',
  'Most answer regressions arrive with a document, not with a model change.')
t('prodalert', 'Alert on rising fallback and handoff rates',
  'Fallback and handoff rates move before anyone files a ticket. A trend alert buys time.')
t('prodonce', 'Test once before launch and assume behaviour stays stable',
  'Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly.')
t('proddashboard', 'Track containment, resolution, and escalation metrics on a dashboard',
  'Operational metrics show whether the agent is helping. They are the business case for the next release.')

# --- Sequencing alternatives (rendered as candidate orders) -----------------
t('seqtestok', 'Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change',
  'Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning.')
t('seqtest1', 'Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change',
  'Scoring cannot happen before there are questions to score.')
t('seqtest2', 'Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent',
  'The failure log depends on scoring, and classification defines the categories the log uses.')
t('seqtest3', 'Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set',
  'Classification needs the questions, and the rerun is the last step, not the first.')

t('seqalmok', 'Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline',
  'Packaging precedes configuration, and configuration precedes promotion.')
t('seqalm1', 'Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables',
  'There is nothing to export before the solution exists and holds the components.')
t('seqalm2', 'Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies',
  'Configuration applies to components that must already be in a solution.')
t('seqalm3', 'Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream',
  'Adding to a solution requires the solution, and the pipeline runs after the export.')

t('seqmaok', 'Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear',
  'Instructions and children precede testing, and tuning follows evidence from the test.')
t('seqma1', 'Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent',
  'There is no misroute to tune before the children exist and routing has been tested.')
t('seqma2', 'Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions',
  'Testing requires the children and the instructions already in place.')
t('seqma3', 'Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions',
  'Tuning before testing guesses at failures the test would reveal.')

t('seqmcpok', 'Identify the tools the agent needs → deploy the MCP server and configure its authentication → register the server with the agent → restrict the exposed tools → verify each tool call',
  'Need comes first, the server must exist and be secured before registration, and exposure is narrowed before verification.')
t('seqmcp1', 'Register the server with the agent → identify the tools the agent needs → verify each tool call → deploy the MCP server and configure its authentication → restrict the exposed tools',
  'A server cannot be registered before it is deployed and authenticated.')
t('seqmcp2', 'Verify each tool call → restrict the exposed tools → identify the tools the agent needs → deploy the MCP server and configure its authentication → register the server with the agent',
  'Verification requires a registered server with tools already exposed.')
t('seqmcp3', 'Deploy the MCP server and configure its authentication → verify each tool call → identify the tools the agent needs → register the server with the agent → restrict the exposed tools',
  'Tool selection is a design decision that precedes deployment and verification.')

t('seqcuok', 'Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes',
  'The API check justifies the approach, the host comes before recording, and monitoring follows the first run.')
t('seqcu1', 'Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record',
  'A run cannot precede the host and the recorded steps.')
t('seqcu2', 'Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes',
  'Recording happens on the prepared machine, after the API check.')
t('seqcu3', 'Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record',
  'Monitoring a tool that has never run and has no host is not possible.')

t('seqconnok', 'Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions',
  'Inventory precedes choice, choice precedes connection, and access testing follows connection.')
t('seqconn1', 'Test answers with users of different access → inventory the sources and their permissions → choose the connector or index for each → review unsupported questions → connect and scope the knowledge',
  'Access testing requires connected sources.')
t('seqconn2', 'Connect and scope the knowledge → choose the connector or index for each → inventory the sources and their permissions → test answers with users of different access → review unsupported questions',
  'The connector cannot be chosen before the inventory describes the sources.')
t('seqconn3', 'Review unsupported questions → test answers with users of different access → connect and scope the knowledge → inventory the sources and their permissions → choose the connector or index for each',
  'There is nothing to review before the knowledge is connected and tested.')

t('seqpipeok', 'Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval',
  'Packaging and configuration come before the pipeline, and the gate runs inside the deployment.')
t('seqpipe1', 'Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step',
  'A deployment cannot run before there is a pipeline and something to deploy.')
t('seqpipe2', 'Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage',
  'A pipeline with no solution and unset variables deploys nothing useful.')
t('seqpipe3', 'Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval',
  'The test step runs against a solution that must exist and be configured first.')

t('seqhitlok', 'The agent gathers the request → the flow validates the required fields → an approval card goes to the owning manager → the flow resumes with the decision → the agent confirms the outcome to the user',
  'Gather, validate, decide, resume, confirm is the only order that keeps the human decision before the action.')
t('seqhitl1', 'The flow resumes with the decision → the agent gathers the request → an approval card goes to the owning manager → the agent confirms the outcome to the user → the flow validates the required fields',
  'The flow cannot resume before the request exists and has been approved.')
t('seqhitl2', 'An approval card goes to the owning manager → the agent gathers the request → the flow validates the required fields → the agent confirms the outcome to the user → the flow resumes with the decision',
  'Approval without a validated request asks the manager to approve nothing.')
t('seqhitl3', 'The agent confirms the outcome to the user → the flow resumes with the decision → the agent gathers the request → an approval card goes to the owning manager → the flow validates the required fields',
  'Confirming the outcome before the decision is made is exactly the failure mode HITL avoids.')

t('seqevalok', 'Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release',
  'The rubric comes first, the human sample calibrates the grader, and the full run follows calibration.')
t('seqeval1', 'Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores',
  'A full run without a rubric or a calibrated grader measures nothing consistently.')
t('seqeval2', 'Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand',
  'The grader cannot be adjusted before it is compared with human scores produced under a rubric.')
t('seqeval3', 'Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores',
  'Hand scoring without a rubric produces judgements that cannot be compared with the grader.')

t('seqfabricok', 'Model the measures in the semantic model → create the Fabric data agent over it → grant the data agent read access → connect it to Copilot Studio → test the questions it must refuse',
  'Measures precede the agent, permissions precede connection, and boundary testing comes last.')
t('seqfabric1', 'Connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it → test the questions it must refuse → grant the data agent read access',
  'Connection without permissions produces an agent that cannot read its own model.')
t('seqfabric2', 'Test the questions it must refuse → grant the data agent read access → connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it',
  'Nothing can be tested before the agent exists and is connected.')
t('seqfabric3', 'Grant the data agent read access → create the Fabric data agent over it → model the measures in the semantic model → connect it to Copilot Studio → test the questions it must refuse',
  'Access is granted to an agent that must already exist over a modelled source.')

t('seqmonitorok', 'Connect the agent to Application Insights → publish a change to a test environment → reproduce a failed answer → query the trace for the tool and retrieval spans → fix and re-run the test set',
  'Telemetry precedes the incident, and the fix follows the evidence from the trace.')
t('seqmonitor1', 'Reproduce a failed answer → connect the agent to Application Insights → query the trace for the tool and retrieval spans → fix and re-run the test set → publish a change to a test environment',
  'There is no trace to query before telemetry is connected.')
t('seqmonitor2', 'Query the trace for the tool and retrieval spans → fix and re-run the test set → connect the agent to Application Insights → publish a change to a test environment → reproduce a failed answer',
  'Tracing requires connected telemetry and an incident that produced data.')
t('seqmonitor3', 'Fix and re-run the test set → reproduce a failed answer → publish a change to a test environment → connect the agent to Application Insights → query the trace for the tool and retrieval spans',
  'Fixing before reproducing and tracing is guesswork.')
