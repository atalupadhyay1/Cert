"""Original AI-500 learning questions: six scenarios for each of 100 objectives.
Concepts recur intentionally across sets. No actual/recalled exam content.
"""
TERMS = {}
ITEMS = []
OVERRIDES = {}
def term(key, label, explanation):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, explanation)
def item(domain, keys, reason, prompts, task, correct=1):
    questions = [p.strip() for p in prompts.strip().splitlines() if p.strip()]
    assert len(questions) == 6, (keys, len(questions))
    ITEMS.append(dict(domain=domain, keys=keys.split(), reason=reason,
                      prompts=questions, task=task, correct=correct, ref=None))

term('decompose','Decompose the goal into bounded agent responsibilities and tools','Defines who performs each task and which deterministic operations are exposed, instead of giving every agent the whole problem.')
term('monolith','Use one broadly autonomous agent for the entire workflow','Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.')
term('moreagents','Increase the number of agents without changing responsibilities','Adds coordination work without resolving unclear ownership, contracts, or workflow design.')
term('finetune','Fine-tune the underlying model','Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.')
term('persona','Specify each agent persona, scope, and escalation rules','Defines role, allowable behavior, autonomy, and boundaries, while enforcement still requires application controls.')
term('rbac','Apply narrowly scoped Azure RBAC assignments','Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.')
term('approval','Insert a human approval gate before the consequential action','Allows a qualified person to approve, reject, or amend a proposed action before it causes an external effect.')
term('audit','Record structured audit events','Supports accountability after and during execution but does not by itself stop an unapproved action.')
term('sequential','Use sequential orchestration','Passes work through dependent stages where later tasks require earlier outputs.')
term('parallel','Use parallel orchestration with a controlled join','Runs independent branches concurrently and combines their results after completion.')
term('handoff','Use a controlled handoff between specialist agents','Transfers task responsibility to the appropriate specialist with explicit context and termination rules.')
term('hub','Use hub-and-spoke coordination','Centralizes dispatch and aggregation through a coordinator while specialists handle bounded work.')
term('peer','Use peer-to-peer coordination with bounded protocols','Allows agents to communicate directly, but requires explicit ownership, convergence, and safety controls.')
term('shortmemory','Use session-scoped short-term state','Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.')
term('longmemory','Use governed long-term memory','Persists approved information beyond a session with access, retention, deletion, and relevance controls.')
term('teamstate','Use versioned shared workflow state','Provides a controlled authoritative state for collaborating agents, with concurrency and ownership rules.')
term('summary','Compact context into a validated summary','Reduces active context size but can omit details; important facts need preservation and verification.')
term('tiers','Separate session state, shared team state, and long-term memory','Assigns each state class suitable persistence, consistency, isolation, and lifecycle controls.')
term('vector','Use an embedding-based retrieval index','Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.')
term('mcp','Use Model Context Protocol (MCP)','Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.')
term('a2a','Use Agent2Agent (A2A) interoperability','Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.')
term('rest','Expose a task-specific REST API','Provides a conventional HTTP contract but does not inherently implement a requested agent or MCP interoperability standard.')
term('modelmatch','Benchmark models against task capability and operational constraints','Matches measured reasoning, modality, context, latency, cost, and deployment requirements instead of choosing only by size.')
term('largest','Select the largest available model for every task','May increase cost and latency and does not establish that capability, geography, or quality requirements are met.')
term('cheapest','Select only by lowest token price','Ignores quality, retry cost, tool reliability, latency, and other business constraints.')
term('computematch','Select compute using workload, scaling, network, and reliability requirements','Evaluates hosting constraints and operational needs rather than assuming a single compute type fits every agent.')
term('functions','Use Azure Functions for a suitable event-driven tool','Fits bounded event-driven operations when execution, hosting, networking, and scaling limits meet the workload.')
term('containerapps','Use Azure Container Apps for suitable containerized services','Provides managed container hosting and supported scaling features, subject to runtime and connectivity requirements.')
term('aks','Use Azure Kubernetes Service when cluster-level control is required','Provides Kubernetes control and ecosystem flexibility with additional operational responsibility.')
term('observability','Propagate trace context across agents and tools','Correlates spans across service boundaries to reconstruct an end-to-end execution path.')
term('metrics','Collect aggregate operational metrics','Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.')
term('replay','Capture versioned replay inputs and sanitized execution events','Supports reproducible investigation by recording necessary inputs, versions, and tool outcomes without exposing prohibited data.')
term('alerts','Configure actionable health and quality alerts','Detects defined conditions and triggers response but does not itself retain all evidence required for deterministic investigation.')
term('zerotrust','Use distinct scoped identities and verify every boundary','Reduces lateral movement by treating each agent and service interaction as an independently authorized access decision.')
term('sharedidentity','Use one highly privileged identity for all agents','Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.')
term('hax','Design clear AI disclosure, user control, and recovery paths','Supports the human-AI experience by communicating limits and allowing correction, cancellation, and escalation.')
term('safetyfilter','Apply content safety filters','Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.')
term('devcontainer','Use a versioned development container and dependency lock','Improves environment reproducibility; it does not by itself determine production architecture or access policies.')
term('instructions','Maintain reviewed repository AI instructions','Communicates coding conventions and boundaries to development assistants; it is not a runtime authorization system.')
term('logsall','Log every raw prompt and credential without filtering','Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.')
term('unbounded','Allow unlimited autonomous retries and spawning','Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.')
term('lifecycle','Define retention, deletion, and tenant-isolation rules for state','Establishes who may use stored information and for how long, instead of assuming persistence implies permission.')
term('contracts','Define typed inputs, outputs, and responsibility ownership','Makes exchanges testable and reduces ambiguity at agent boundaries; runtime validation remains necessary.')

A1='design-logical-architecture-for-multi-agent-solutions'
A2='specify-technology-components-to-include-in-a-multi-agent-solution'
item(1,'decompose monolith moreagents finetune','Independent responsibilities and deterministic tools should be identified before adding autonomous workers.', '''A procurement solution needs evidence gathering, policy checking, and approved purchasing. Which design step best establishes specialist boundaries?
Three agents repeatedly redo the same analysis because their responsibilities overlap. Which architectural change addresses the root cause?
A team proposes adding agents before identifying the tasks each must own. What should the architect do first?
A workflow mixes creative research with deterministic invoice calculations. Which design activity helps separate responsibilities?
A migration starts with a business goal but no agent or tool boundaries. Which architecture decision should come first?
A system delegates every task to every agent and gets contradictory results. Which redesign most directly clarifies ownership?''', A1)
item(1,'persona rbac finetune metrics','Behavioral scope and escalation must be specified for each role; resource permissions alone do not define its purpose.', '''A support agent keeps giving legal advice beyond its intended role. Which architecture artifact should define its limits?
A triage agent needs clear rules for when to answer and when to escalate. What should the design specify?
Two specialists disagree about which one may issue recommendations. Which specification should clarify their authority?
An architect must define a research agent's autonomy and prohibited behaviors. Which design choice fits?
A new agent has access permissions but no defined task scope. What additional specification is needed?
A domain assistant must stay within approved advisory functions. Which design artifact sets that behavioral boundary?''', A1)
item(1,'approval audit safetyfilter summary','A pre-action approval gate controls consequential autonomy; recording the action afterward is insufficient.', '''An agent proposes a large supplier payment that must be authorized by a finance officer. Which design control fits?
A medical scheduling assistant proposes an exceptional action requiring clinician review. Which workflow element is needed?
A production agent may recommend account deletion but must not execute it alone. Which design control fits?
A purchasing assistant must pause before submitting a high-value order. Which control should the architect include?
An operations agent proposes a risky infrastructure change that needs operator consent. Which workflow element fits?
A service bot may draft refunds above a threshold but a person must authorize release. Which design control fits?''', A1)
item(1,'sequential parallel peer hub','Later stages require validated outputs from earlier stages, making a dependency-ordered flow appropriate.', '''An analysis agent needs extracted facts before writing, and a reviewer needs the draft afterward. Which orchestration fits?
A compliance check must finish before an agent can prepare an approved transaction. Which workflow pattern fits?
A report workflow requires extraction, then reconciliation, then narrative generation. Which pattern fits?
An agent cannot select a remedy until another agent has classified the incident. Which orchestration fits?
A design must ensure document validation completes before downstream summarization begins. Which pattern fits?
A proposal writer requires the research result, and an editor requires the completed proposal. Which orchestration fits?''', A1)
item(1,'parallel sequential handoff monolith','Independent tasks can run concurrently; join logic should combine their completed outputs.', '''Three agents independently review security, cost, and accessibility before a final decision. Which orchestration fits?
A travel planner can check weather, local events, and hotel availability independently. Which pattern fits?
A due-diligence workflow has several independent evidence checks followed by aggregation. Which orchestration fits?
Separate agents can summarize different documents without sharing intermediate results. Which pattern fits?
An architecture has independent regional analyses that must all finish before synthesis. Which pattern fits?
A reviewer needs independent legal and technical assessments before combining them. Which orchestration fits?''', A1)
item(1,'hub peer sequential handoff','A single coordinator responsible for dispatch and aggregation is characteristic of hub-and-spoke.', '''A central agent assigns work to specialists and combines their responses. Which coordination topology is this?
Specialists report only to a dispatcher that owns the workflow outcome. Which architecture pattern fits?
An enterprise wants centralized routing instead of unrestricted specialist-to-specialist conversations. Which topology fits?
A coordinator selects subagents and merges their results into a final response. Which pattern is this?
An architecture gives one orchestrator responsibility for dispatch, progress, and synthesis. Which topology fits?
A manager agent sends bounded tasks to workers that return to the manager. Which orchestration pattern fits?''', A1)
item(1,'shortmemory longmemory vector finetune','Temporary interaction state should be scoped to the session instead of being persisted as general memory.', '''An agent needs details only until the current booking conversation ends. Which memory scope fits?
A troubleshooting flow must remember its current diagnostic step without retaining it across unrelated sessions. Which state fits?
A form-filling agent needs temporary answers while one application is completed. Which memory design fits?
An architect must store active conversation context but avoid unnecessary future reuse. Which memory class fits?
A one-time incident workflow needs intermediate decisions only during the active run. Which state scope fits?
A customer assistant needs the current shopping conversation, not a permanent customer profile. Which memory design fits?''', A1)
item(1,'longmemory shortmemory summary finetune','Approved persistent knowledge or preferences need governed long-term memory rather than reliance on an active context window.', '''An agent should remember an approved communication preference across future sessions. Which memory class fits?
A company wants reusable lessons from completed workflows with controlled retention. Which memory design fits?
An assistant must retrieve approved prior project decisions after its original session expires. Which memory class fits?
A recurring research agent needs a governed store of validated findings across runs. Which state class fits?
An architecture must preserve authorized user preferences beyond a single interaction. Which memory design fits?
A project assistant needs approved historical decisions weeks after the conversation ends. Which memory class fits?''', A1)
item(1,'tiers vector shortmemory monolith','Different state classes need distinct persistence, consistency, access, and lifecycle policies.', '''A solution has ephemeral conversations, shared workflow status, and persistent semantic knowledge. Which state architecture best fits?
Agents put all conversation and transactional state into one vector index and lose reliable status updates. Which redesign fits?
An enterprise needs different retention rules for sessions and long-lived knowledge. Which architecture fits?
A multi-agent system must distinguish team coordination data from reusable historical memories. Which design fits?
An architect must separately govern active sessions, collaborative state, and durable knowledge. Which storage strategy fits?
A solution needs both authoritative run status and similarity-based recall without conflating them. Which state design fits?''', A2)
item(1,'mcp a2a rest finetune','The requirement is a standard tool-resource interface, not delegation to another independent agent.', '''An existing tool server must expose compatible resources and tool descriptions to several AI clients. Which protocol fits?
An architect needs a standard interface for agents to discover and call external tools. Which protocol fits?
A knowledge service should expose resources to compatible AI applications using a tool-oriented protocol. Which standard fits?
A company wants to avoid a different tool integration format for each compatible client. Which protocol fits?
A design calls for standardized access to server-provided tools, resources, and prompts. Which protocol fits?
A developer must select an interoperability protocol for a tool server consumed by compatible agent clients. Which one fits?''', A1)
item(1,'a2a mcp vector devcontainer','Collaborating with a remote agent through an agent-facing contract calls for A2A rather than treating every peer as a raw resource server.', '''Two independently hosted compatible agents need to delegate tasks through an agent interoperability protocol. Which standard fits?
A solution must integrate an existing remote specialist as an agent peer rather than a raw database tool. Which protocol fits?
An architect needs a compatible agent-to-agent collaboration interface across hosting boundaries. Which protocol fits?
A remote specialist already exposes an A2A-compatible endpoint. Which integration choice preserves its agent-facing contract?
A coordinator should send tasks to an independent compatible agent using its agent collaboration protocol. Which standard fits?
An enterprise must choose between tool-resource interoperability and direct compatible remote-agent collaboration. Which protocol serves the latter?''', A1)
item(1,'modelmatch largest cheapest finetune','Model choice requires task-specific evidence and operational fit rather than a single price or size ranking.', '''A vision reasoning agent and a short text router have different capability and cost needs. How should models be selected?
A procurement team wants to choose models solely by parameter count. Which selection strategy is more defensible?
A regulated workflow needs acceptable quality, processing location, and latency. Which model-selection approach fits?
An agent model is cheap per token but fails tools and retries often. Which selection approach addresses total suitability?
An architect must choose models for several distinct specialist roles. Which approach best matches their demands?
A model has strong benchmark publicity but poor performance on the actual workflow. Which selection strategy should replace assumption-based choice?''', A1)
item(1,'computematch functions containerapps aks','Compute selection must follow execution and operational constraints; naming one service without those requirements is insufficient.', '''A platform team must choose hosting for stateful and event-driven agent components with different operational needs. Which approach fits?
An architecture review has not established runtime duration, scaling, or private-network requirements. How should compute be selected?
A proposed hosting platform cannot meet an agent's runtime constraints. Which design approach should guide reconsideration?
A company compares managed containers, functions, and Kubernetes for its agent services. Which selection basis is appropriate?
A multi-agent workload has bursty traffic, long operations, and isolation requirements. Which compute-design approach fits?
An architect must balance reliability, security, cost, and operating effort for agent hosting. Which approach fits?''', A2)
item(1,'observability metrics alerts vector','Cross-service trace context is needed to connect individual agent and tool operations into one execution.', '''A workflow spans five services, but operators cannot connect their events to one user request. Which architecture control is missing?
An architect needs to follow a task from coordinator to specialist to tool. Which observability design fits?
Logs exist in every component but cannot be joined by execution. Which tracing decision addresses this?
An agent workflow crosses hosting boundaries and needs end-to-end investigation. Which telemetry architecture fits?
A team needs to identify which downstream tool call belongs to a failed user task. Which correlation design fits?
A platform must reconstruct interactions across agent services rather than only see aggregate rates. Which design control fits?''', A2)
item(1,'hax safetyfilter audit finetune','Human-AI experience includes understandable boundaries and user control, not only technical filtering.', '''Users cannot tell when an agent is acting autonomously or how to stop it. Which experience design addresses this?
A recommendation interface offers no way to correct misunderstood input. Which human-AI design practice fits?
An assistant makes decisions without explaining limits or giving users a recovery path. Which design choice fits?
An architect must make an agent workflow understandable and interruptible for users. Which practice fits?
Users need clear AI disclosures and a way to escalate disputed recommendations. Which experience design fits?
A workflow exposes users to automated decisions but provides no cancellation or correction mechanism. Which design practice fits?''', A1)
item(1,'devcontainer instructions containerapps finetune','A reproducible development environment and dependency lock reduce local setup drift; production hosting solves a different problem.', '''Python agent developers have incompatible local environments and dependency versions. Which development setup best addresses this?
A new contributor cannot reproduce a colleague's agent development environment. Which SDLC component fits?
A team needs consistent local tooling across developer machines and CI. Which environment practice fits?
An agent project behaves differently because developers install unpinned dependency versions. Which setup should be standardized?
A platform team wants a reproducible VS Code-compatible development environment for agent work. Which approach fits?
A repository needs a repeatable environment for contributors rather than merely coding guidance. Which SDLC choice fits?''', A2)
item(1,'zerotrust lifecycle sharedidentity logsall unbounded','Select TWO. Scoped identities constrain access, while state lifecycle and isolation policies constrain persistent data use.', '''An architect designs a regulated, multi-tenant agent platform. Which TWO foundations address identity isolation and governed state? (Select TWO.)
A multi-agent system must prevent lateral movement and inappropriate memory reuse. Which TWO design controls fit? (Select TWO.)
An enterprise needs separate agent authority and tenant-isolated retained knowledge. Which TWO foundations fit? (Select TWO.)
A platform review finds shared credentials and undefined memory retention. Which TWO architectural corrections fit? (Select TWO.)
A solution must limit each agent's authority and define how stored state is used. Which TWO controls fit? (Select TWO.)
A regulated agent deployment needs per-boundary access checks and controlled persistent state. Which TWO design principles fit? (Select TWO.)''', A2, correct=2)
item(1,'replay contracts metrics moreagents largest','Select TWO. Versioned sanitized evidence supports replay, and typed contracts make boundary behavior explicit and testable.', '''A team needs reproducible debugging and unambiguous exchanges between agents. Which TWO design controls fit? (Select TWO.)
A workflow produces inconsistent results and unclear agent handoffs. Which TWO architectural artifacts improve investigation and interface clarity? (Select TWO.)
An audit requires traceable execution evidence and clearly defined inter-agent data contracts. Which TWO controls fit? (Select TWO.)
A platform must support replay investigation and independently testable agent boundaries. Which TWO design choices fit? (Select TWO.)
A multi-agent design needs reviewable execution inputs and explicit ownership of exchanged data. Which TWO practices fit? (Select TWO.)
Developers cannot reproduce incidents or determine the expected schema at a handoff. Which TWO design improvements fit? (Select TWO.)''', A2, correct=2)
term('examples','Add curated input-output examples to the prompt','Demonstrates desired behavior in context without modifying learned model weights.')
term('dynamic','Inject relevant authorized context at request time','Supplies current task information during inference without treating it as permanently learned knowledge.')
term('defensive','Separate trusted instructions from untrusted content','Reduces instruction confusion by treating retrieved or user-supplied material as data; enforcement still needs layered controls.')
term('promptversion','Version prompts and evaluate changes before promotion','Makes instruction changes reproducible, comparable, and reversible.')
term('tuningplan','Use a supported fine-tuning strategy with curated data and held-out evaluation','Adapts learned behavior when justified, with defined data quality, refresh triggers, and regression checks.')
term('rag','Retrieve authorized current evidence for generation','Grounds answers in external content at inference time without inherently updating weights.')
term('accumulate','Assemble only relevant state, evidence, and tool results','Builds useful request context within a token budget instead of forwarding every prior message.')
term('entity','Maintain stable entity IDs and validated factual state','Preserves identity and critical facts across summaries and agent transitions rather than relying on ambiguous names alone.')
term('ttl','Apply purpose-based memory retention and deletion','Expires or deletes retained information according to policy rather than assuming all remembered content remains authorized forever.')
term('transformers','Use Hugging Face Transformers for compatible model capabilities','Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.')
term('langgraph','Use explicit state transitions and checkpoints in a graph workflow','Supports stateful orchestration and controlled resumption; checkpointed state must still be secured and external side effects made safe.')
term('langchain','Use LangChain components for supported application integrations','Provides composable model, retrieval, and tool integration abstractions, but does not automatically establish durable state or authorization.')
term('agentframework','Implement a controlled agent workflow with explicit review and resume','Coordinates agent steps and human intervention in a framework-supported workflow, with durable correlation and revalidation before action.')
term('chunk','Chunk documents into coherent retrievable passages','Controls retrieval granularity; excessive size wastes context, while tiny isolated chunks can lose meaning.')
term('hybrid','Combine lexical and vector retrieval','Can match both exact identifiers and semantic paraphrases; it still needs relevance evaluation and permissions.')
term('rerank','Rerank retrieved candidates before context selection','Improves ordering within a candidate set; it cannot recover a document never retrieved.')
term('filter','Apply server-side tenant and permission filters to retrieval','Constrains candidate documents using trusted identity and access metadata rather than allowing the model to decide access.')
term('embeddings','Re-embed content with a consistent compatible embedding configuration','Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.')
term('mcpserver','Implement an MCP server with explicit tool schemas and authorization','Exposes supported tools and resources through MCP while validating arguments and enforcing caller permissions.')
term('mcpclient','Implement an MCP client that discovers and invokes permitted tools','Consumes the server interface and handles tool results under application policy; discovery is not permission to execute every tool.')
term('logicapps','Use Azure Logic Apps for suitable connector-based workflows','Coordinates supported connectors and integration steps, including approval patterns where configured; it is not a model-training library.')
term('apim','Place appropriate policies at Azure API Management','Provides an API governance layer for authentication, traffic management, and policies; it does not by itself grant downstream data permissions.')
term('functioncall','Execute a validated function call in application code','The model proposes structured tool arguments, while trusted code authorizes and performs the operation.')
term('toolvalidate','Validate tool results against schema and domain constraints','Checks structure, types, ranges, and semantic consistency before downstream use; HTTP success alone is insufficient.')
term('retry','Use bounded retries with backoff and jitter for transient failures','Limits repeat attempts and avoids synchronized retry storms; non-idempotent operations require duplicate protection.')
term('idempotency','Use a stable idempotency key and durable result tracking','Prevents repeated requests for the same logical action from producing duplicate external effects.')
term('timeout','Apply deadlines, cancellation, and a safe fallback','Bounds stalled work and defines a failure path instead of allowing dependent steps to wait indefinitely.')
term('promptcache','Use supported prompt-prefix caching','Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.')
term('semanticcache','Use a governed semantic response cache','Can reuse meaning-equivalent responses only when permissions, tenant scope, freshness, and task semantics allow it.')
term('responsecache','Use an exact-input response cache','Reuses prior results for a matching cache key when authorization and freshness permit, rather than matching approximate meaning.')
term('concurrency','Bound concurrent agent and tool execution','Limits simultaneous work according to capacity and downstream quotas instead of spawning unbounded tasks.')
term('middleware','Use reusable middleware for cross-cutting controls','Centralizes concerns such as authorization, trace enrichment, and exception handling without duplicating them in every agent.')
term('budget','Enforce per-run token, tool-call, and spawn budgets','Creates explicit termination and cost boundaries across the whole workflow, including delegated work.')
term('cancel','Propagate cancellation through dependent branches','Stops unnecessary downstream work after a user cancels, a deadline expires, or the workflow reaches a terminal condition.')
term('authremote','Authenticate remote endpoints and authorize delegated operations','Checks the identity, audience, and scope of agent or tool calls instead of trusting interoperability alone.')
term('sanitize','Validate and treat remote results as untrusted input','Checks returned structure and content and prevents remote output from overriding trusted instructions or permissions.')
term('testtuning','Keep independent evaluation data and gate model changes','Measures generalization and regression without using the same examples to train and certify a change.')
term('refreshfacts','Refresh the knowledge source and retrieval index','Addresses changing external facts without repeatedly training those facts into model weights.')
D1='design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions'
D2='design-and-implement-agent-memory-context-management-and-knowledge-integration'
D3='build-and-integrate-tool-ecosystems'
D4='implement-multi-agent-orchestration'
item(2,'examples tuningplan largest promptcache','A few demonstrations in context can clarify expected behavior without a training job.', '''A model needs three examples of the required extraction format without changing weights. Which technique fits?
An agent misunderstands a rare output convention, and the team has a few approved demonstrations. Which prompt change fits?
A team wants to show the desired answer style inside each request rather than retrain. Which approach fits?
A routing agent needs examples of boundary cases supplied at inference time. Which technique fits?
An assistant should imitate a format demonstrated by several approved input-output pairs. Which prompt technique fits?
A developer wants to improve task behavior using a handful of demonstrations in the request. Which approach fits?''', D1)
item(2,'dynamic finetune promptcache summary','Task-specific current information should be injected at inference after authorization, not assumed to exist in model weights.', '''An agent needs today's approved exchange rate in its response context. Which prompt strategy fits?
A workflow must use the current authorized account status for each user request. Which context strategy fits?
A policy assistant needs newly published approved terms during generation. Which strategy fits?
An orchestrator should provide each specialist only the latest relevant task facts. Which context approach fits?
An assistant must use a live tool result when drafting an answer without retraining. Which strategy fits?
A contextual recommendation changes with the user's current permitted project data. Which inference strategy fits?''', D1)
item(2,'defensive finetune audit promptcache','Untrusted documents should not acquire instruction authority merely because they appear in a model context.', '''A retrieved manual contains instructions to ignore application policy. Which prompt design principle should be applied?
An agent summarizes emails that may contain hostile commands. Which context treatment is appropriate?
A document asks a model to reveal credentials while the model is only supposed to extract facts. Which defense fits?
An assistant receives external text that attempts to redefine its role. Which instruction design principle fits?
A knowledge source includes malicious behavioral directions. Which prompt-layer defense is appropriate?
A system mixes tool results with trusted policy instructions without distinction. Which design correction fits?''', D1)
item(2,'promptversion finetune moreagents metrics','Prompt changes require identifiable versions and evaluation so regressions can be attributed and rolled back.', '''An instruction edit harms tool selection and the team cannot identify the prior working revision. Which practice is needed?
Two deployments use different prompts but share the same label, preventing comparison. Which lifecycle control fits?
A team needs reproducible tests and rollback for agent instructions. Which prompt-management practice fits?
An auditor asks which instruction revision produced a particular agent run. Which practice supplies this evidence?
A developer edits a live prompt without running regression cases. Which lifecycle improvement fits?
A platform must compare candidate instructions before they are released to all users. Which practice fits?''', D1)
item(2,'tuningplan refreshfacts promptcache moreagents','Persistent task behavior may justify supported fine-tuning; the decision needs curated examples, refresh triggers, and independent evaluation.', '''An agent repeatedly fails a stable specialized task despite prompt work, and high-quality labeled examples exist. Which adaptation strategy should be evaluated?
A team wants to adapt model behavior with curated task demonstrations and defined retraining triggers. Which strategy fits?
A supported model needs learned domain output conventions rather than daily factual updates. Which approach fits?
An adaptation project needs to specify training data quality, update frequency, and regression gates. Which strategy fits?
A model must learn persistent task-specific behavior and the team can evaluate a supported customization job. Which approach fits?
A company considers changing model weights for a stable narrow task. Which plan best addresses responsible implementation?''', D1)
item(2,'accumulate largest unbounded longmemory','Useful context is selected and budgeted, not built by blindly forwarding every conversation and tool result.', '''An agent request exceeds its context limit because every prior tool response is included. Which context strategy fits?
A specialist needs only relevant case facts, but receives the entire team transcript. Which context design should replace this?
A coordinator should prepare a bounded context packet for each subagent. Which implementation practice fits?
A workflow accumulates irrelevant messages and loses focus. Which context-management change fits?
An agent needs selected evidence and current state rather than raw historical chatter. Which approach fits?
A team wants to preserve useful inputs while staying below request token limits. Which context strategy fits?''', D2)
item(2,'summary longmemory finetune moreagents','Compaction reduces active context while requiring validation of important facts and links to authoritative state.', '''A long interaction must fit the context window while retaining key decisions. Which operation should be applied carefully?
A team wants to shorten accumulated context without discarding all earlier facts. Which technique fits?
An agent reaches its request-size limit but needs a concise representation of prior progress. Which context operation fits?
A multi-step workflow needs to replace verbose history with a verified concise account. Which technique fits?
A project assistant needs bounded context after many interactions. Which operation reduces history size while preserving checked facts?
A coordinator must pass a compact but verified history to a new specialist. Which context technique fits?''', D2)
item(2,'entity summary vector largest','Stable identifiers and verified factual state prevent confusion when similar entities appear across handoffs.', '''Two customers share the same display name and an agent merges their records. Which context practice addresses this?
A summary refers to it ambiguously and the next agent updates the wrong order. Which state design fits?
An assistant loses track of which invoice belongs to which supplier after handoff. Which practice fits?
A workflow must distinguish several similarly named projects across compacted history. Which state design fits?
A coordinator hands a case to another agent that confuses the user with a referenced contact. Which practice fits?
An entity's attributes are overwritten by a similarly named entity during a long run. Which design correction fits?''', D2)
item(2,'transformers mcp apim logicapps','The requested capability is compatible model and pipeline tooling, not API policy or integration-protocol hosting.', '''A Python developer needs pretrained model and tokenizer tooling from Hugging Face for a compatible local inference component. Which library fits?
An agent solution needs a supported Hugging Face model pipeline rather than a new communication protocol. Which tooling fits?
A specialist implementation requires compatible tokenizer and model classes from the Hugging Face ecosystem. Which library fits?
A team wants to add a compatible transformer model capability to its Python agent application. Which tooling fits?
A developer needs Hugging Face architecture-specific model loading for an advanced specialist. Which library fits?
An application must use a compatible pretrained transformer pipeline inside a controlled agent workflow. Which library fits?''', D4)
item(2,'ttl finetune promptcache embeddings','Persisted memory remains subject to approved purpose and retention; storage does not create indefinite permission.', '''An agent remembers personal information after the approved retention period. Which memory policy must be enforced?
A user requests deletion of eligible retained preferences. Which memory lifecycle capability fits?
A team stores every past conversation indefinitely despite purpose restrictions. Which lifecycle correction fits?
A memory store contains old project data that policy requires expiring. Which control fits?
An assistant should stop reusing personal details when their approved retention ends. Which memory design fits?
A long-term memory record outlives its lawful business purpose. Which lifecycle action fits?''', D2)
item(2,'chunk finetune promptcache rbac','Retrievable passage size and boundaries determine whether evidence is both focused and sufficiently contextual.', '''A retriever embeds entire manuals and returns too much unrelated text. Which ingestion choice should be reconsidered?
A RAG system splits every sentence into an isolated unit and loses necessary surrounding context. Which design choice needs review?
An ingestion pipeline must choose useful passage boundaries before embedding. Which operation is this?
A knowledge index needs smaller coherent units rather than whole books. Which preprocessing step fits?
An agent's evidence passages are either huge or too fragmented to answer questions. Which configuration should be tuned?
A team balances evidence granularity against context completeness during ingestion. Which design step is this?''', D2)
item(2,'hybrid vector summary finetune','Exact identifiers benefit from lexical matching, while paraphrases benefit from semantic matching.', '''A support index must find exact error codes and semantically similar descriptions. Which retrieval approach fits?
A product assistant needs both SKU matching and natural-language similarity search. Which strategy fits?
A RAG pipeline misses literal clause IDs when using vectors alone. Which retrieval combination should be evaluated?
A knowledge assistant must handle precise names and conceptual questions in the same corpus. Which approach fits?
An enterprise search system should retain keyword precision while supporting paraphrases. Which retrieval method fits?
A workflow needs both exact policy identifiers and meaning-based evidence retrieval. Which retrieval approach fits?''', D2)
item(2,'rerank chunk finetune promptcache','A relevance rescoring stage can reorder candidates that were already retrieved.', '''Relevant evidence appears in the candidate set but is ranked below unrelated passages. Which retrieval step could help?
A RAG pipeline retrieves 40 passages and needs a more relevant final five. Which stage fits?
An agent receives weakly ordered search results although the right document is present. Which enhancement fits?
A retrieval team wants a second relevance assessment before context assembly. Which technique fits?
A search result includes useful evidence too low to enter the prompt. Which stage could improve selection?
An application needs to rescore candidate passages against the query before generation. Which technique fits?''', D2)
item(2,'filter summary safetyfilter finetune','Access constraints must be enforced by trusted retrieval controls before restricted content reaches a model.', '''A shared search index contains multiple tenants' documents. Which retrieval control prevents cross-tenant evidence exposure?
An agent must search only the user's permitted projects. Which enforcement approach fits?
A company proposes telling the model to ignore unauthorized documents after retrieval. Which stronger retrieval control fits?
A knowledge service needs to prevent users receiving passages they cannot access. Which implementation fits?
A multi-agent RAG workflow must preserve document permissions across specialists. Which retrieval control fits?
A search API serves several organizations from one index. Which control should limit candidate content?''', D2)
item(2,'embeddings rerank summary promptcache','Query and document vectors need a compatible embedding space; changing the model may require reindexing.', '''A team changes the query embedding model but keeps incompatible document vectors. Which correction addresses relevance failure?
Two indexes accidentally mix vectors produced by incompatible model versions. Which remediation fits?
A new embedding configuration changes dimensions and semantic space. What should happen to indexed content used with it?
A retrieval rollout updates only the query encoder and matching quality collapses. Which correction fits?
An index migration must keep document and query representations compatible. Which action fits?
A developer assumes all same-length vectors from different embedding models are interchangeable. Which corrective practice fits?''', D2)
item(2,'mcpserver mcpclient a2a promptcache','The provider side exposes capabilities through MCP while enforcing contracts and access.', '''A Python service must expose approved business operations to compatible MCP clients. Which component must be built?
An enterprise wants its data service to publish MCP tools with validated arguments. Which component fits?
A team owns the provider that serves tools and resources through MCP. Which side of the integration is this?
A tool owner needs to publish schemas and reject unauthorized MCP invocations. Which component fits?
A service should offer compatible AI clients a controlled MCP interface. Which implementation fits?
An Azure-hosted provider must expose permitted resources and tool descriptions through MCP. Which component is needed?''', D3)
item(2,'mcpclient mcpserver a2a finetune','The consumer side discovers and invokes permitted MCP capabilities, handling responses under application policy.', '''An agent application must consume tools exposed by an existing MCP server. Which component must it implement?
A developer owns the caller that discovers MCP tools and invokes authorized operations. Which side is this?
An assistant should connect to a remote MCP provider and process returned tool results. Which component fits?
A tool server already exists; the new agent must act as its protocol consumer. Which implementation fits?
A coordinator needs to list permitted server tools and call one with validated inputs. Which MCP component fits?
An application integrates a published MCP service rather than exposing its own tools. Which side must it build?''', D3)
item(2,'logicapps transformers embeddings devcontainer','A supported connector-based integration workflow suits Logic Apps when its triggers, actions, and operational limits fit.', '''A tool workflow must coordinate several supported enterprise connectors and an approval step. Which Azure capability fits?
A business integration needs low-code orchestration across supported SaaS connectors. Which service fits?
An agent action should trigger a configured connector-based approval process. Which Azure service fits?
A team wants a supported workflow integration rather than writing every SaaS connector itself. Which service fits?
An agent must invoke a business process composed of supported managed connectors. Which capability fits?
A solution needs a configured multi-step integration flow with available enterprise connectors. Which Azure service fits?''', D3)
item(2,'apim functions transformers vector','API policy enforcement and request governance are gateway responsibilities, separate from model training and tool execution.', '''Several agent tools need a common API gateway for authentication policies and traffic control. Which Azure service fits?
An enterprise wants centrally managed policies in front of tool APIs. Which service fits?
A platform needs a governed API facade for external tool endpoints. Which Azure capability fits?
An architect wants rate-limiting and authentication policy at the API entry layer. Which service fits?
A business exposes tool APIs through a managed policy gateway. Which Azure service is appropriate?
A tool ecosystem needs shared request policy enforcement without putting all policy logic in each model prompt. Which service fits?''', D3)
item(2,'functioncall examples finetune summary','A model-produced tool request is a proposal; authorized application code must validate and execute it.', '''A model emits arguments for checking an order, but no actual lookup occurs. What application behavior is required?
An assistant claims it issued a refund after merely generating a tool-call object. What implementation step is missing?
A function-call response names a tool and arguments. Which trusted action should follow before treating the operation as complete?
A developer assumes a model's JSON tool proposal executes the API automatically. Which correction fits?
A workflow must convert a permitted structured model tool request into a real operation. Which step fits?
An agent needs to call an external calculator rather than invent a result. Which implementation behavior fits?''', D3)
item(2,'toolvalidate audit promptcache largest','Successful transport does not prove the payload is well-formed, plausible, or safe for downstream decisions.', '''A tool returns HTTP 200 but a negative inventory count outside its contract. Which control should reject the result?
An API response has the right transport status but missing required fields. Which validation fits?
A tool returns a malformed date that a downstream agent would treat as valid. Which control is needed?
A specialist receives a tool payload with contradictory totals. Which check should occur before use?
A remote service returns an unexpected schema after an update. Which agent integration control fits?
A tool result contains values outside permitted domain ranges despite no network error. Which safeguard fits?''', D3)
item(2,'retry unbounded finetune moreagents','Transient failures may justify limited retries with backoff, not unlimited repeats or changes to model weights.', '''A read-only API occasionally returns a transient failure. Which retry approach best limits cascading load?
Several agents synchronize immediate retries after throttling and worsen the incident. Which retry policy fits?
A network glitch causes a safe read operation to fail briefly. Which handling approach should be evaluated?
An integration needs resilience without overwhelming a recovering downstream service. Which retry strategy fits?
A tool provider reports retryable errors and asks callers to slow down. Which bounded handling approach fits?
An agent should tolerate transient read failures while preserving a finite attempt limit. Which strategy fits?''', D3)
item(2,'idempotency retry audit promptcache','When an operation may already have committed, a stable logical-action identifier prevents duplicate effects on retry.', '''A payment API times out after possibly committing the charge. Which integration design prevents duplicate charges on retry?
An order-creation tool is called again after a lost response. Which protection prevents duplicate orders?
A resumed workflow repeats the same external booking operation. Which design makes repeated requests safe?
A message is delivered twice to a purchase tool. Which mechanism should prevent a second purchase?
An agent retry must not create another support case for the same logical request. Which protection fits?
A non-read-only operation may complete even when the caller sees a timeout. Which design reduces duplicate side effects?''', D3)
item(2,'timeout unbounded largest promptcache','A deadline and safe failure path bound work that cannot complete in time.', '''A downstream tool hangs and blocks the entire agent workflow indefinitely. Which control fits?
A user cancels a task but dependent tool calls continue running. Which execution control is needed?
An interactive assistant must stop a stalled dependency within its time budget. Which design fits?
A slow service consumes all workflow time without a defined failure path. Which control fits?
A coordinator waits forever for an unresponsive specialist. Which execution policy fits?
A workflow needs to stop work after its deadline and communicate a safe fallback. Which control fits?''', D3)
item(2,'langgraph promptcache finetune embeddings','Explicit graph state and checkpoints support controlled continuation, while side effects and access still require separate safeguards.', '''A LangGraph workflow must resume after a restart without losing its defined state transitions. Which implementation strategy fits?
A multi-step graph needs recoverable progress instead of keeping all state only in process memory. Which design fits?
A stateful graph orchestration must support a durable investigation of where a run paused. Which implementation fits?
An agent graph loses progress when its host restarts. Which state-management capability is needed?
A developer needs explicit state transitions and a resumable graph workflow. Which approach fits?
An application must preserve graph execution state across interruptions with controlled resumption. Which strategy fits?''', D4)
item(2,'agentframework examples promptcache audit','A human checkpoint must pause action, preserve correlation, and resume only after a valid decision and authorization check.', '''A Microsoft Agent Framework workflow must pause for operator approval and resume the correct pending action. Which design fits?
A reviewer approves one case, but the application resumes a different run. Which workflow implementation should replace this?
A team needs durable human intervention in an agent orchestration, including rejection. Which design fits?
An approval step should survive process restarts and validate that the request is still actionable. Which workflow design fits?
A specialist needs to suspend a consequential action until a named reviewer decides. Which implementation fits?
An agent flow must accept an authorized override and then continue from the right state. Which design fits?''', D4)
item(2,'promptcache responsecache semanticcache finetune','Repeated eligible prompt prefixes can benefit from provider-supported processing reuse; this does not imply final-answer reuse.', '''Many calls share the same long instruction prefix but different user questions. Which supported caching feature targets repeated prefix processing?
A team wants to reduce processing of unchanged initial prompt content without reusing complete answers. Which cache fits?
An application repeatedly sends eligible identical reference instructions before varying requests. Which caching approach should be evaluated?
A provider supports reusing processing for a repeated prompt prefix. Which cache type is this?
An agent pipeline has costly repeated static prompt content but different outputs each time. Which cache targets that repetition?
A developer distinguishes model prefix-processing reuse from response-result reuse. Which mechanism serves the former?''', D4)
item(2,'semanticcache responsecache promptcache finetune','Meaning-equivalent response reuse needs a governed similarity cache with strict access and freshness boundaries.', '''An assistant may reuse approved answers for equivalent wording within one authorized tenant and freshness window. Which cache fits?
A team wants to match paraphrased questions to eligible prior responses while preserving permissions. Which cache type fits?
A support system can reuse some validated answers for meaning-equivalent queries. Which cache should be evaluated with safeguards?
A lookup should reuse eligible responses when question wording differs but intent is equivalent. Which cache fits?
An application needs similarity-based response reuse rather than exact key matching. Which governed cache fits?
A team can safely cache selected nonvolatile answers across equivalent requests in the same access scope. Which mechanism fits?''', D4)
item(2,'concurrency unbounded largest finetune','A semaphore or worker limit should constrain simultaneous work to available capacity and downstream quotas.', '''A Python fan-out creates thousands of tasks and overwhelms a tool API. Which execution control fits?
An agent system hits downstream quotas because too many workers run at once. Which control should be implemented?
A coordinator needs a maximum number of simultaneous specialist calls. Which scaling mechanism fits?
A workload must avoid exhausting connections during multi-agent fan-out. Which control fits?
A developer considers using a semaphore around tool calls to manage load. Which strategy does this implement?
An orchestrator should increase throughput without exceeding provider concurrency limits. Which control is needed?''', D4)
item(2,'middleware examples finetune vector','Reusable cross-cutting behavior belongs in controlled middleware rather than being duplicated or entrusted only to model text.', '''Every agent repeats logging, authorization, and exception-handling code. Which reusable implementation pattern fits?
A platform wants consistent trace enrichment across all supported agent requests. Which design component fits?
Authorization checks must run consistently around tool execution rather than depend on each prompt. Which implementation pattern fits?
A team needs centralized error handling for its agent pipeline. Which reusable capability fits?
Multiple specialists require identical request-correlation and policy hooks. Which implementation pattern fits?
A workflow framework supports interception around agent calls for shared controls. Which design approach fits?''', D4)
item(2,'budget cancel largest moreagents promptcache','Select TWO. Global work budgets and cancellation propagation control runaway delegation across the whole run.', '''A coordinator recursively spawns agents and continues work after cancellation. Which TWO controls directly address runaway execution? (Select TWO.)
A workflow exceeds its tool-call allocation and keeps downstream branches alive after termination. Which TWO controls fit? (Select TWO.)
An agent platform needs bounded total work and prompt shutdown of dependent tasks. Which TWO mechanisms fit? (Select TWO.)
A multi-agent run consumes unlimited tokens and ignores user stop requests. Which TWO execution controls fit? (Select TWO.)
A solution must cap delegated work and stop unnecessary child tasks when a deadline ends. Which TWO controls fit? (Select TWO.)
A workflow should enforce a global action budget and honor cancellation throughout its branches. Which TWO controls fit? (Select TWO.)''', D4, correct=2)
item(2,'authremote sanitize sharedidentity logsall finetune','Select TWO. Protocol compatibility does not establish caller permission or make remote outputs trustworthy.', '''A team integrates an existing agent using A2A and tools using MCP. Which TWO security practices remain necessary? (Select TWO.)
A remote specialist is protocol-compatible but crosses an organizational trust boundary. Which TWO integration controls fit? (Select TWO.)
A coordinator consumes tools and agents from external providers. Which TWO controls should surround interoperability? (Select TWO.)
An existing agent endpoint returns task results to a sensitive workflow. Which TWO practices protect the integration? (Select TWO.)
A platform adopts standard protocols and assumes no further trust checks are needed. Which TWO controls correct that assumption? (Select TWO.)
A multi-agent application must integrate compatible third-party capabilities safely. Which TWO practices fit? (Select TWO.)''', D4, correct=2)
item(2,'testtuning promptversion largest unbounded moreagents','Select TWO. Independent evaluation and versioned instructions make behavioral changes measurable and reversible.', '''A team changes model behavior and prompts together. Which TWO controls support meaningful regression assessment and rollback? (Select TWO.)
An adaptation project needs independent evidence and traceable instructions before rollout. Which TWO practices fit? (Select TWO.)
A developer trains and tests on the same examples while editing unversioned prompts. Which TWO changes fit? (Select TWO.)
A workflow update must preserve a trustworthy quality gate and identifiable prompt revisions. Which TWO practices fit? (Select TWO.)
A platform needs to compare model adaptation results without losing the instruction history. Which TWO controls fit? (Select TWO.)
An agent release changes learned behavior and prompt wording. Which TWO lifecycle practices improve assessment and reproducibility? (Select TWO.)''', D1, correct=2)
term('humanreview','Use qualified human reviewers with a shared rubric','Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.')
term('memoryeval','Evaluate memory retention, retrieval, isolation, and forgetting','Tests whether relevant authorized facts are recalled and prohibited or expired information is not reused.')
term('retrievaleval','Measure relevance of retrieved evidence against labeled queries','Evaluates whether search returns useful source material separately from whether generation uses it correctly.')
term('groundedness','Evaluate whether generated claims are supported by supplied evidence','Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.')
term('tooleval','Evaluate tool choice, arguments, outcomes, and side effects','Tests whether the right authorized operation was invoked correctly and produced the intended result.')
term('prompteval','Run a representative held-out prompt regression suite','Compares instruction or model changes on independent realistic cases, including difficult and safety-relevant inputs.')
term('judge','Calibrate LLM-as-a-judge against expert-labeled cases','Measures agreement, bias, and failure modes of automated judging rather than treating judge output as unquestionable truth.')
term('synthetic','Generate and validate diverse synthetic evaluation cases','Expands test coverage while checking labels, realism, duplicates, and gaps; generated examples are not automatically valid.')
term('feedback','Analyze user feedback with verified task outcomes','Turns real-world signals into reviewed improvements instead of equating popularity or raw engagement with correctness.')
term('criticalpath','Optimize the dependent critical path and parallelize independent work','Focuses on steps determining end-to-end duration while respecting task dependencies and resource constraints.')
term('ratelimits','Coordinate concurrency, rate budgets, and backoff','Controls request pressure on limited services; unconstrained parallelism can increase throttling and latency.')
term('amnesia','Diagnose sliding-window amnesia','Identifies loss of earlier information as it drops out of active context; this is distinct from a model weight update.')
term('summarydrift','Diagnose summary drift','Identifies accumulated distortion when repeated summarization alters or omits important facts.')
term('vectorrecall','Supplement vector recall with authoritative structured lookup','Addresses exact facts, dates, counts, or entity relationships that semantic similarity alone may fail to recover reliably.')
term('health','Monitor agent health and workflow failure patterns','Separates worker availability and recurrent failure conditions from content-quality scoring alone.')
term('slo','Measure end-to-end service-level indicators against objectives','Checks availability, latency, and successful completion from the workflow perspective rather than relying only on component uptime.')
term('trace','Inspect correlated spans with version and token metadata','Connects latency, usage, prompts, and tool execution to a particular run, subject to privacy controls.')
term('tokenlimits','Inspect token use and enforce loop and tool-call termination','Locates repeated generation or delegation and applies finite execution budgets rather than treating cost as only model price.')
term('chargeback','Attribute usage to tenants, projects, and workflow runs','Enables quotas, allocations, and chargeback using governed usage metadata instead of inferring all costs from one shared total.')
term('qualityregression','Compare quality against a stable versioned baseline','Detects worsened task outcomes after changes; a healthy process or fast response does not establish answer quality.')
term('drift','Monitor changes in task inputs and agent behavior over time','Detects shifts in operating conditions or behavioral patterns that can require investigation and reassessment.')
term('failureeval','Evaluate recovery, safe failure, and task completion under faults','Tests behavior under unavailable tools and partial failures, not just successful-path answers.')
term('smaller','Benchmark a smaller adequate model for selected tasks','May reduce inference cost and latency if measured quality, safety, and tool reliability remain acceptable.')
term('trim','Remove irrelevant context while preserving necessary evidence','Reduces wasted tokens and can improve focus, but must not discard required facts or policy constraints.')
term('sanitizeobs','Redact and access-control sensitive telemetry','Preserves useful investigation evidence while avoiding unnecessary exposure of prompts, personal information, and secrets.')
term('remediate','Define alerts with bounded remediation and escalation','Links detection to a controlled response with limits and human handoff rather than unchecked restart or retry loops.')
E1='design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions'
E2='optimize-prompt-and-model-performance-for-multi-agent-solutions'
E3='design-and-implement-observability-and-monitoring-for-multi-agent-solutions'
item(3,'humanreview metrics cheapest promptcache','Nuanced evaluations require a consistent rubric and qualified judgment; operational statistics alone cannot assess them.', '''A legal drafting assistant needs assessment of nuanced usefulness and appropriateness. Which evaluation method fits?
A team wants experts to score whether agent recommendations meet business expectations. Which evaluation approach fits?
Automated overlap metrics miss serious context-dependent errors. Which evaluation method should complement them?
An agent's tone and risk-sensitive advice need domain judgment. Which evaluation process fits?
Several reviewers disagree because no scoring criteria are defined. Which evaluation process should be established?
An enterprise needs a reviewable expert assessment of complex multi-agent outputs. Which evaluation approach fits?''', E1)
item(3,'memoryeval retrievaleval groundedness tooleval','Memory needs tests for correct recall and prohibited reuse, not only tests of current document retrieval.', '''An assistant should recall approved preferences but forget expired personal information. Which evaluation suite fits?
A team must test whether one tenant's remembered facts can leak into another tenant's session. Which evaluation is needed?
An agent recalls stale information after deletion requests. Which evaluation area should be targeted?
A platform needs evidence that approved facts persist and unauthorized memories remain inaccessible. Which test category fits?
A workflow uses persistent user context and must prove its forgetting behavior. Which evaluation strategy fits?
An agent loses relevant stored facts while retaining irrelevant private details. Which evaluation should diagnose this?''', E1)
item(3,'retrievaleval groundedness humanreview metrics','Search relevance is evaluated independently of whether a generator faithfully uses the retrieved evidence.', '''The correct policy exists in the corpus but never reaches the model context. Which evaluation should come first?
A RAG workflow supplies irrelevant passages to otherwise capable agents. Which component evaluation fits?
A team wants to know whether the search stage returns useful evidence for labeled questions. Which evaluation fits?
A knowledge assistant misses answer-bearing documents before generation begins. Which evaluation targets the failure?
A retriever returns the wrong product version even though the intended version is indexed. Which evaluation area fits?
An experiment measures how useful selected source passages are for answering each query. Which evaluation is this?''', E1)
item(3,'groundedness retrievaleval metrics cheapest','Relevant retrieval does not guarantee the final answer is supported; generated claims need evidence checking.', '''A workflow retrieves the right policy but invents an exception in the final answer. Which evaluation dimension targets this?
An agent cites a source that does not support its claim. Which quality check is needed?
The source context is accurate, but the summary adds unsupported facts. Which evaluation fits?
A multi-agent synthesis includes statements absent from all supplied evidence. Which dimension should be assessed?
An evaluator checks each output claim against the context available to the agent. Which quality dimension is this?
A final response contradicts the tool evidence despite successful retrieval. Which content evaluation fits?''', E1)
item(3,'tooleval groundedness retrievaleval humanreview','A tool workflow needs outcome and side-effect checks; a plausible final explanation can hide an incorrect operation.', '''An assistant produces a fluent response but invokes the wrong business operation. Which evaluation is essential?
A tool-using agent chooses the correct API but supplies a wrong customer ID. Which evaluation area targets this?
A system claims success even though the external action failed. Which evaluation should check this?
An agent calls a prohibited tool and still produces an acceptable-looking final paragraph. Which evaluation fits?
A task benchmark must verify that the intended authorized action actually occurred once. Which evaluation is needed?
A workflow's natural-language answer is correct but its tool arguments are not. Which evaluation should expose this?''', E1)
item(3,'prompteval examples finetune largest','A versioned independent test suite reveals regressions across representative cases rather than only author-selected examples.', '''A new prompt fixes one case but breaks several previously correct workflows. Which evaluation practice should gate release?
A team wants to compare prompt revisions on realistic cases not used to write the changes. Which evaluation fits?
A developer tests only the example that motivated an instruction edit. Which broader practice should be added?
An agent update must preserve prior correctness and safety behavior across tasks. Which test suite fits?
A platform needs repeatable comparison of instruction versions against independent cases. Which evaluation fits?
A team must detect prompt regressions before production rather than after user complaints. Which evaluation strategy fits?''', E1)
item(3,'judge largest metrics promptcache','Automated judges can be biased or wrong; calibration and ongoing audits are required.', '''An LLM judge consistently favors verbose but incorrect answers. Which evaluation practice should address this?
A team wants to use automated model judging for high-volume evaluation. What validation is needed first?
Two judge models disagree sharply with expert ratings. Which improvement process fits?
A model-based scorer is assumed to be ground truth without comparison to humans. Which correction fits?
A judge may be vulnerable to flattering instructions inside candidate outputs. Which evaluation governance practice fits?
An organization wants evidence that its automated evaluator tracks domain-expert judgments. Which strategy fits?''', E2)
item(3,'synthetic promptcache largest unbounded','Generated tests expand coverage only after validation; synthetic labels and examples can introduce new errors or blind spots.', '''A team lacks examples of rare tool-failure cases and wants to expand its evaluation dataset. Which approach fits?
An agent evaluation suite needs more diverse edge cases without assuming generated labels are correct. Which practice fits?
A project uses generated test scenarios but must screen unrealistic and duplicate items. Which data strategy fits?
An evaluation team wants synthetic examples covering underrepresented workflow paths. Which approach is appropriate?
A platform needs broader adversarial and recovery cases while maintaining label quality. Which test-data practice fits?
A team wants to scale scenario coverage and preserve independent review of generated cases. Which approach fits?''', E2)
item(3,'feedback metrics largest promptcache','User signals should be connected to verified outcomes and reviewed before they drive changes.', '''Users like an agent's tone but report that actions fail. Which improvement signal should be analyzed?
A product team wants to convert production feedback into verified workflow improvements. Which practice fits?
An assistant receives positive ratings for confident but incorrect answers. Which feedback process is more reliable?
A team needs to prioritize issues using user reports and confirmed task outcomes. Which approach fits?
A deployed agent has failures absent from its offline suite. Which feedback practice should inform new cases?
An optimization loop must avoid treating engagement alone as correctness. Which reviewed signal approach fits?''', E2)
item(3,'criticalpath moreagents largest unbounded','Only independent work can be safely overlapped; dependent stages still determine the critical path.', '''A report runs three independent checks serially and waits before synthesis. Which duration-optimization approach fits?
A workflow's slowest dependency chain dominates latency while unrelated work is also serialized. Which analysis fits?
A team wants to speed execution without violating ordering requirements. Which optimization strategy fits?
An agent graph contains independent branches that can overlap before a required join. Which performance approach fits?
A pipeline is slow because all tasks run one at a time even when inputs are independent. Which redesign fits?
A coordinator needs to identify which sequence of dependent calls determines total task duration. Which optimization focus fits?''', E2)
item(3,'ratelimits unbounded largest finetune','Excess concurrency can increase throttling, so throughput optimization must respect downstream rate budgets.', '''Parallelizing every agent call increases 429 responses and makes completion slower. Which correction fits?
A coordinator launches more workers than its provider quota can sustain. Which performance strategy fits?
A tool dependency has strict request limits shared across agents. Which scheduling approach fits?
A pipeline needs higher throughput without causing synchronized throttling retries. Which control fits?
An operator observes longer latency after raising concurrency far beyond service limits. Which optimization fits?
Multiple agents compete for the same limited downstream capacity. Which coordination strategy fits?''', E2)
item(3,'amnesia summarydrift drift finetune','Facts can disappear when older messages leave the active window even if no memory summary has changed.', '''An agent forgets an early requirement once old messages fall outside its active context. Which issue is this?
A sliding history window drops an important instruction from the beginning of a session. Which diagnosis fits?
A long conversation loses facts exactly when old turns are removed from the prompt. Which context issue fits?
An assistant fails to recall earlier details that are no longer supplied to the model. Which context limitation is illustrated?
A workflow keeps only recent messages and misses a necessary earlier constraint. Which diagnosis fits?
A bounded context strategy discards initial facts without retaining them elsewhere. Which issue results?''', E2)
item(3,'summarydrift amnesia drift finetune','Repeated compaction can distort retained facts; authoritative state and summary checks help detect this.', '''A budget value changes slightly after each round of history summarization. Which issue is this?
An assistant's compacted history gradually alters an earlier approved decision. Which failure mode fits?
Repeated summaries omit qualifications until a conditional statement becomes absolute. Which diagnosis fits?
A workflow's stored summaries increasingly disagree with its original event history. Which issue is this?
An agent retains a summary but it no longer faithfully represents the approved facts. Which context failure fits?
A multi-agent handoff uses several generations of summaries that progressively distort source details. Which diagnosis fits?''', E2)
item(3,'vectorrecall rerank largest promptcache','Exact relationships and authoritative facts may require structured lookup rather than nearest-neighbor similarity alone.', '''An agent retrieves similar records but cannot reliably identify the exact active contract for a customer. Which correction fits?
A memory system finds related events but fails to answer an exact date-and-ID question. Which retrieval improvement fits?
An assistant needs authoritative account balances, but vector similarity returns approximate past descriptions. Which correction fits?
A team relies only on semantic recall to reconstruct precise entity relationships. Which stronger lookup design fits?
A workflow must distinguish the latest approved value from semantically similar historical values. Which approach fits?
A vector-only memory retrieves relevant prose but misses exact structured facts. Which retrieval strategy should supplement it?''', E2)
item(3,'entity summarydrift promptcache finetune','Entity continuity requires stable identity and factual state across transitions, not merely more similar text.', '''An agent swaps attributes between two similarly named suppliers after a handoff. Which continuity control fits?
A workflow must keep customer and dependent identities separate across context compaction. Which state practice fits?
A long-running assistant loses the link between project IDs and approved decisions. Which correction fits?
Several agents use inconsistent references for the same account. Which continuity control should be introduced?
An assistant confuses a user with another person mentioned in the conversation. Which state practice fits?
A resumed workflow assigns an old order's attributes to a new order with a similar description. Which control fits?''', E2)
item(3,'health groundedness examples cheapest','Availability and repeated operational failures need health and failure-pattern telemetry, not only language-quality evaluation.', '''An agent worker repeatedly crashes before producing any output. Which monitoring focus is primary?
Several workflow runs stall because a specialist process is unhealthy. Which telemetry should be examined?
A platform needs to detect recurrent worker failures and failed orchestration steps. Which monitoring category fits?
A tool connector repeatedly disconnects while generated text quality remains high. Which monitoring focus fits?
A service must identify agents that stop responding during execution. Which reliability monitoring fits?
An operations team needs visibility into agent restarts and repeated workflow failure modes. Which category fits?''', E3)
item(3,'slo metrics promptcache humanreview','Successful end-to-end outcomes matter; individually healthy components can still form an unreliable workflow.', '''Every service reports uptime, but only 85% of user workflows complete. Which reliability measurement should be prioritized?
A multi-agent system meets component availability targets but violates user response-time commitments. Which monitoring view fits?
An operations team must check its workflow against an agreed completion-time objective. Which measurement fits?
A platform needs to monitor customer-perceived reliability across several services. Which indicator strategy fits?
A dependency is healthy, but orchestration failures harm the overall service. Which measurement should expose the problem?
A team wants evidence of availability and latency commitments for the complete agent solution. Which monitoring strategy fits?''', E3)
item(3,'trace metrics examples largest','Correlated spans connect a particular run to its latency, version, tokens, and tool steps.', '''One request is unusually expensive, and operators need to identify its model and tool calls. Which telemetry should they inspect?
A workflow regression appears only for one prompt revision and tool sequence. Which diagnostic evidence fits?
An agent run has a long unexplained delay between two services. Which telemetry supports investigation?
A developer needs the token usage and execution path of a specific failed task. Which evidence fits?
A platform must correlate an individual output with its prompt revision and downstream calls. Which telemetry fits?
An operator wants to follow execution IDs through model calls and tool spans. Which diagnostic approach fits?''', E3)
item(3,'tokenlimits cheapest largest moreagents','Repeated generation and tool loops can dominate cost even when unit token price is low.', '''A task loops between two agents and consumes far more tokens than expected. Which monitoring and control focus fits?
An assistant keeps re-planning the same tool call without finishing. Which optimization directly addresses wasted work?
A cost spike is caused by repeated delegation rather than a model price change. Which control fits?
A workflow has no termination rule and generates dozens of redundant follow-up calls. Which remediation fits?
An operations team must identify why per-run tool calls and tokens are unbounded. Which focus fits?
An agent repeatedly asks a specialist the same question after receiving an answer. Which execution control fits?''', E3)
item(3,'chargeback metrics largest promptcache','Usage attribution needs trusted tenant and project metadata to support budgets and fair allocations.', '''A shared agent platform needs to allocate model and tool costs to individual business units. Which approach fits?
An operator sees a total bill but cannot identify the tenant causing a cost spike. Which instrumentation is needed?
A company needs per-project quotas and internal chargeback for agent usage. Which design fits?
A workflow platform wants each run's consumption associated with its authorized tenant. Which cost-management practice fits?
A finance team asks which teams consumed shared agent capacity. Which attribution strategy fits?
An enterprise needs budget enforcement and usage reporting across tenants. Which telemetry strategy fits?''', E3)
item(3,'qualityregression health metrics promptcache','A versioned baseline detects a change in task quality even when availability and response speed are unchanged.', '''A new prompt deploys successfully but reduces correct tool selection on the same evaluation set. Which monitoring comparison identifies this?
An agent remains fast and healthy but gives more wrong answers after an update. Which monitoring focus fits?
A release changes model behavior and worsens outcomes on stable reference tasks. Which detection approach fits?
A platform must distinguish successful deployment from preserved task quality. Which assessment fits?
An instruction update passes liveness checks but fails known business cases. Which comparison is needed?
A team wants to detect degraded reasoning after a model version change. Which baseline-based monitor fits?''', E3)
item(3,'failureeval groundedness examples largest','A production evaluation must test recovery and partial failure, not just correct answers when every dependency succeeds.', '''An agent works in demonstrations but fails dangerously when a tool is unavailable. Which evaluation should be added?
A workflow must prove it handles partial specialist failure without claiming unsupported success. Which evaluation fits?
A team needs to test the agent when a dependency times out or returns malformed data. Which evaluation strategy fits?
A platform passes happy-path tests but has no evidence of safe fallback behavior. Which evaluation fits?
An enterprise wants to validate that outages do not cause repeated unsafe actions. Which evaluation fits?
A multi-agent release needs evidence that interrupted workflows terminate or recover appropriately. Which test category fits?''', E1)
item(3,'smaller trim largest moreagents unbounded','Select TWO. Model fit and context efficiency can reduce cost, but both changes must preserve measured quality and safety.', '''A multi-agent workflow is too costly while carrying irrelevant context into a large model. Which TWO changes are reasonable to evaluate? (Select TWO.)
A platform wants lower inference cost without abandoning quality criteria. Which TWO optimization experiments fit? (Select TWO.)
An assistant uses its largest model for simple tasks and forwards unnecessary history. Which TWO improvements should be tested? (Select TWO.)
A team must reduce waste in model size and prompt tokens while preserving evidence. Which TWO actions fit? (Select TWO.)
An agent's expense comes from oversized models and irrelevant context. Which TWO candidate optimizations fit? (Select TWO.)
A solution needs economical responses with retained correctness and safety. Which TWO changes merit controlled evaluation? (Select TWO.)''', E2, correct=2)
item(3,'sanitizeobs remediate logsall unbounded largest','Select TWO. Useful monitoring requires protected telemetry and controlled incident response rather than unrestricted logs or loops.', '''A platform needs operational investigations without exposing sensitive prompts or triggering endless restarts. Which TWO controls fit? (Select TWO.)
An agent system logs personal data and responds to every alert with unlimited retries. Which TWO corrections fit? (Select TWO.)
An enterprise wants privacy-aware traces and a bounded response to recurring failures. Which TWO practices fit? (Select TWO.)
A reliability design must protect telemetry and specify safe escalation from alerts. Which TWO controls fit? (Select TWO.)
A team needs actionable monitoring while preventing sensitive-data exposure and remediation storms. Which TWO practices fit? (Select TWO.)
An operator wants useful incident evidence and limited automated recovery with human handoff. Which TWO controls fit? (Select TWO.)''', E3, correct=2)
term('managedidentity','Use an Azure managed identity where supported','Lets an Azure workload obtain identity-based access without embedding a long-lived application secret; resource authorization is still required.')
term('obo','Use an on-behalf-of flow for delegated downstream access','Exchanges a user assertion through the middle tier for an appropriate downstream token, preserving delegated user context where supported.')
term('oauth','Validate OAuth access tokens and enforce audience and scopes','Checks that a token is valid for the receiving API and the requested operation; possession of any token is not sufficient.')
term('apikey','Use an API key with secure storage and rotation','Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.')
term('vault','Store and retrieve secrets through Azure Key Vault','Centralizes supported secrets, keys, and certificates with controlled access and lifecycle management.')
term('rotation','Rotate secrets and update dependent applications safely','Changes credentials through a tested lifecycle with controlled overlap or rollout where supported, rather than retaining a leaked value.')
term('privateendpoint','Use supported private endpoints and correct private DNS','Provides private connectivity to supported services when network routes, DNS, and public-access settings are configured consistently.')
term('toolguard','Authorize and validate the proposed tool action before execution','Checks caller authority, arguments, target, and domain restrictions before an external effect occurs.')
term('inputguard','Inspect and constrain user input before agent processing','Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.')
term('resultguard','Validate and screen tool responses before reuse','Checks external output structure and policy and treats embedded instructions as untrusted before it reaches another agent.')
term('outputguard','Validate and screen the final response before delivery','Applies final output controls but cannot undo an unauthorized side effect that has already occurred.')
term('customguard','Implement deterministic domain-specific policy checks','Enforces explicit business constraints such as allowed amounts or prohibited operations in trusted code rather than relying only on generic toxicity filters.')
term('redteam','Run adversarial testing early and throughout the lifecycle','Uses challenging and misuse-oriented tests, including supported Foundry red-teaming capabilities, to discover risks before and after release.')
term('dtap','Promote through development, test, acceptance, and production','Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.')
term('bluegreen','Maintain separate blue and green environments and switch traffic','Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.')
term('canary','Release to a limited traffic cohort with health and quality gates','Limits initial exposure and expands only after measured outcomes meet criteria.')
term('rollback','Restore a known-good compatible release and verify recovery','Requires versioned artifacts and configuration, state compatibility, and operational checks; a prompt-only revert may be insufficient.')
term('iac','Deploy versioned infrastructure as code through reviewed automation','Makes environment configuration reproducible and auditable, with environment-specific identity and policy settings.')
term('unittest','Use isolated unit tests for deterministic components','Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.')
term('integrationtest','Test interactions with configured external dependencies','Verifies real contracts, authentication, networking, and service behavior across component boundaries.')
term('regressiontest','Run regression tests and automated agent evaluations','Checks that previously accepted behavior and quality are preserved after prompt, model, tool, or code changes.')
term('pipeline','Gate CI/CD on reviewed artifacts, security checks, and evaluations','Automates build and release evidence while preventing failed checks from silently promoting a release.')
term('immutable','Promote the same immutable versioned artifacts across environments','Reduces unreviewed differences by tracking code, prompt, model, tool schema, and deployment configuration versions.')
term('isolateenv','Use separate environment identities and configuration','Prevents development or test access from inheriting production authority and reduces accidental cross-environment effects.')
term('leastsecret','Grant only required secret access to each workload','Limits the scope of credential retrieval rather than allowing every agent to read all stored secrets.')
term('sharedkey','Embed one shared long-lived credential in every prompt','Exposes a powerful secret across model interactions and removes per-workload access separation.')
term('publicnet','Enable unrestricted public access to bypass private networking','May bypass a connection problem by removing intended isolation, but does not satisfy a private-only design.')
term('directprod','Deploy changes directly to all production users without gates','Removes staged evidence and increases exposure to unreviewed errors.')
S1='design-and-implement-security-for-multi-agent-solutions'
S2='design-and-implement-guardrails-for-multi-agent-solutions'
S3='deploy-multi-agent-solutions-to-azure'
item(4,'managedidentity apikey sharedidentity summary','Supported workload identity avoids embedding application credentials, while a separate authorization assignment still limits resource access.', '''An Azure-hosted agent needs supported resource access without storing an application password. Which identity approach fits?
A platform wants to remove embedded credentials from an Azure workload calling a compatible service. Which design fits?
A tool service should authenticate to supported Azure resources without shipping a client secret. Which approach fits?
An application needs identity-based access from Azure compute without a long-lived credential in code. Which option fits?
A team wants to use a supported Azure workload identity instead of copying secrets into every agent. Which approach fits?
An agent host should obtain tokens for supported services without managing its own application password. Which identity choice fits?''', S1)
item(4,'obo managedidentity apikey sharedidentity','When downstream authorization must reflect the signed-in user, a supported delegated OBO flow differs from app-only identity.', '''A middle-tier agent API must call a downstream API using the signed-in user's delegated authority. Which flow fits?
A tool must respect the caller's delegated permissions rather than run only as the application. Which authentication flow fits?
An enterprise assistant receives a user token and needs a suitable downstream token in that user's context. Which flow fits?
A multi-tier service should preserve delegated user context for a compatible downstream API. Which authentication pattern fits?
An application cannot replace user-specific authorization with a shared service key. Which supported delegated flow fits?
An agent API acts as a middle tier between an authenticated user and a delegated downstream service. Which flow fits?''', S1)
item(4,'oauth audit promptversion apikey','A receiving API must verify token validity and intended audience and enforce permissions for the operation.', '''An agent presents a token intended for another API. Which receiving-service control should reject it?
A tool accepts any bearer token without checking its audience or scopes. Which control is missing?
A remote API must distinguish a valid token from one authorized for a particular action. Which enforcement fits?
A platform receives expired or wrongly targeted access tokens at tool endpoints. Which validation is required?
An agent tries an operation outside the token's permitted scopes. Which API control should stop it?
A security review finds that token presence alone grants tool access. Which correction fits?''', S1)
item(4,'vault sharedkey promptcache vector','Secrets need governed storage and authorized retrieval rather than inclusion in prompts, source files, or semantic memory.', '''A third-party tool requires a secret that must not be placed in prompts or code. Which Azure service should manage it?
An agent application needs controlled storage for a service credential and certificate. Which service fits?
A team currently stores API secrets in repository configuration. Which managed secret store fits?
An enterprise needs centralized credential lifecycle management for agent tools. Which Azure service fits?
A tool uses a credential that only authorized workloads may retrieve. Which service fits?
A platform must manage supported secrets, keys, and certificates outside model context. Which Azure service fits?''', S1)
item(4,'rotation audit finetune promptcache','Credential lifecycle changes require coordinated application updates and revocation, not just a log entry or model change.', '''A tool credential may be compromised and applications must move to a replacement safely. Which process fits?
A policy requires periodic secret changes without avoidable service interruption. Which lifecycle approach fits?
A platform needs to replace a service password and update authorized consumers. Which operation fits?
An expiring certificate used by a tool integration must be replaced through a tested rollout. Which process fits?
A leaked API key must stop being usable while applications adopt a new credential. Which lifecycle process fits?
A tool connector needs a tested credential update path rather than an indefinite static secret. Which practice fits?''', S1)
item(4,'privateendpoint publicnet safetyfilter finetune','Private connectivity requires consistent endpoint, DNS, route, and access configuration rather than merely a private-looking URL.', '''An agent must reach a supported Azure service over private connectivity with public access restricted. Which design fits?
A private endpoint is created, but callers still resolve the public service path. Which network design should be completed?
A regulated deployment requires supported service traffic to stay on the approved private path. Which approach fits?
An agent host cannot reach a private-only dependency because name resolution is misconfigured. Which design area should be corrected?
A platform needs network isolation for supported tool and knowledge services. Which connectivity pattern fits?
A team wants to fix private-service access without opening unrestricted public access. Which network approach fits?''', S1)
item(4,'rbac persona safetyfilter audit','Resource access must be granted at the necessary principal and scope; behavioral instructions do not enforce Azure permissions.', '''A research agent should read one approved resource but must not manage the subscription. Which authorization approach fits?
An Azure workload has excessive contributor permissions for a read-only task. Which control should narrow its authority?
A tool service needs only specific supported data operations at a limited resource scope. Which access control fits?
An application prompt says read only, but its identity has broad management rights. Which enforcement should correct this?
A platform must separate supported resource permissions for several agent identities. Which Azure control fits?
A security review needs to minimize the resource actions each agent principal can perform. Which authorization approach fits?''', S1)
item(4,'inputguard outputguard audit promptcache','Input-side intervention can reject or constrain risky incoming requests before they drive agent processing.', '''A workflow needs a first intervention point for risky user requests before invoking agents. Which control fits?
An assistant should apply configured request screening before constructing its execution plan. Which guardrail fits?
A user submits content that violates the application's intake policy. Which intervention stage is directly relevant?
A platform wants to reject prohibited requests before they reach specialist agents. Which control fits?
A team needs an intake boundary in its layered guardrail design. Which intervention fits?
An incoming request should be checked before tools or model processing are scheduled. Which guardrail stage fits?''', S2)
item(4,'toolguard outputguard audit promptcache','Authorization and business validation must occur before the external action; final text screening is too late.', '''An agent proposes sending a payment to an unapproved account. Which guardrail must act before execution?
A tool call requests deletion of a record outside the user's permission scope. Which control should stop it?
A model proposes an order amount above an enforceable business limit. Which intervention is needed?
A refund action needs validation of identity, target, and amount before the API call. Which guardrail fits?
A specialist emits plausible tool arguments for a prohibited action. Which execution-stage check fits?
A platform must prevent unauthorized side effects even if the final answer would be harmless. Which control fits?''', S2)
item(4,'resultguard inputguard promptcache audit','External tool responses form a separate trust boundary and need checks before they influence later decisions.', '''A tool response embeds instructions to disclose secrets. Which intervention should handle it before reuse?
An external API returns unsafe text that would enter the next agent's context. Which guardrail fits?
A remote result includes malformed fields and hostile instructions. Which boundary should validate it?
A search tool returns content that attempts to override the system's policy. Which intervention fits?
A specialist consumes external tool output without checking schema or content. Which guardrail should be added?
A retrieved tool result crosses into an internal planning context. Which intervention stage needs policy checks?''', S2)
item(4,'outputguard inputguard promptcache audit','Final delivery is its own intervention point, though it does not replace controls before tool effects.', '''A final response contains sensitive personal information that policy forbids exposing. Which last-stage control fits?
An assistant's generated answer violates response policy despite safe tool execution. Which guardrail fits?
A platform must screen the completed user-facing answer before release. Which intervention fits?
An agent produces unsupported or disallowed content in its final message. Which final boundary should inspect it?
A workflow needs validation immediately before delivering generated text to a user. Which control fits?
A final synthesis may expose restricted content and needs screening at delivery. Which guardrail stage fits?''', S2)
item(4,'customguard safetyfilter examples finetune','Explicit business constraints require trusted domain checks; a generic content category filter does not enforce numeric or transactional policy.', '''A purchasing agent must never approve orders above a defined amount without review. Which guardrail implements that exact constraint?
A workflow must reject tool actions outside an allowlisted set of destinations. Which domain control fits?
A finance assistant needs deterministic validation of allowed transaction limits. Which guardrail fits?
A generic toxicity filter does not enforce a legal filing deadline rule. Which additional control fits?
An agent should enforce a business-specific combination of account status and action type. Which guardrail fits?
A tool API must apply explicit permitted amount and product rules regardless of model output. Which control fits?''', S2)
item(4,'redteam directprod promptcache largest','Adversarial evaluation should begin before release and continue as the system changes; it does not establish an absolute safety guarantee.', '''A team wants to find prompt-injection and misuse paths before production. Which security practice fits?
A project postpones all adversarial testing until after launch. Which shift-left improvement fits?
A workflow needs challenging tests of guardrail bypass attempts using supported Foundry capabilities. Which approach fits?
An enterprise wants to probe agent-tool attack paths throughout development. Which security practice fits?
A new agent release needs evidence from misuse-oriented tests before exposure. Which evaluation approach fits?
A platform must test how agents react to hostile users and compromised content early in the lifecycle. Which practice fits?''', S1)
item(4,'dtap directprod bluegreen promptcache','Environment stages separate development from progressively validated production promotion.', '''A team must separate development, test, acceptance, and production with promotion gates. Which release methodology fits?
An agent project currently treats a developer demonstration as production acceptance. Which staged approach fits?
A regulated platform requires explicit validation in separate lifecycle environments before release. Which methodology fits?
An enterprise needs a formal path from development through acceptance to production. Which environment strategy fits?
A solution should prove readiness in test and acceptance stages before users receive it. Which lifecycle pattern fits?
A release process requires distinct development, test, acceptance, and production responsibilities. Which methodology fits?''', S3)
item(4,'bluegreen canary dtap directprod','Two prepared environments with traffic switching characterize blue/green; partial cohort exposure is a different strategy.', '''A platform maintains two prepared production environments and switches traffic to the new one. Which release strategy is this?
An agent service needs fast traffic reversion to an intact prior environment. Which deployment pattern fits?
A team deploys a full replacement environment before moving users from the old environment. Which strategy fits?
A release plan uses separate blue and green instances and a controlled routing switch. Which pattern is this?
An enterprise wants to validate a new prepared environment before changing active traffic. Which release approach fits?
A deployment keeps the old environment available while routing traffic to a complete new environment. Which strategy fits?''', S3)
item(4,'canary bluegreen directprod dtap','A limited initial traffic cohort reduces exposure and allows measured expansion based on defined outcomes.', '''A new prompt-model combination should initially serve only a small user cohort. Which release strategy fits?
A platform wants to increase traffic gradually only if task quality and error rates remain acceptable. Which strategy fits?
An agent update should expose 5% of requests first and use monitored gates before expansion. Which rollout fits?
A risky change needs limited initial exposure rather than an immediate full traffic switch. Which deployment approach fits?
An enterprise wants to compare early production outcomes for a small release cohort. Which strategy fits?
A workflow update should reach a small percentage of users before broader rollout. Which release pattern fits?''', S3)
item(4,'rollback promptversion audit promptcache','Recovery must restore a compatible set of components and verify service behavior, not only change one instruction string.', '''A failed release changes code, prompt, tool schema, and state format. Which recovery plan is appropriate?
A prompt revert does not fix a release because the tool contract also changed. Which recovery approach fits?
A platform needs a tested way to return to an earlier compatible agent deployment. Which release capability fits?
An agent rollout harms production, and the team must restore known-good artifacts and configuration. Which action fits?
A recovery plan must account for model, prompt, code, and state compatibility. Which capability fits?
A team needs to reverse a release without breaking persisted workflow state. Which release strategy should be planned?''', S3)
item(4,'iac directprod promptversion examples','Reviewed infrastructure definitions improve reproducibility across environments and make deployment configuration auditable.', '''Manually configured agent environments drift apart and deployments are not reproducible. Which approach fits?
A team must review and version Azure resource definitions alongside application releases. Which deployment practice fits?
An enterprise wants predictable environment provisioning with recorded configuration changes. Which approach fits?
A platform needs repeatable identity, network, and resource configuration through automation. Which deployment practice fits?
An agent deployment depends on undocumented portal settings. Which practice should replace this?
A release pipeline must provision approved infrastructure consistently across environments. Which approach fits?''', S3)
item(4,'unittest integrationtest redteam canary','Isolated deterministic logic can be tested with controlled dependencies; this does not replace live integration checks.', '''A developer needs to verify a deterministic argument-validation function without calling external services. Which test fits?
A team wants fast isolated tests for a routing rule using mocked dependencies. Which test type fits?
A tool wrapper's input normalization needs direct verification of boundary values. Which test fits?
A utility that constructs permission filters should be checked independently of the live search service. Which test fits?
A workflow contains deterministic budget logic that can be exercised without a model call. Which test fits?
A developer needs isolated tests of a schema-validation function before broader service tests. Which test category fits?''', S3)
item(4,'integrationtest unittest examples promptcache','Real component boundaries need contract, identity, networking, and dependency tests beyond isolated mocks.', '''Unit tests pass, but a deployed tool fails because its token audience is wrong. Which test type should catch this?
An agent connector's mocks pass while the real API schema is incompatible. Which testing layer fits?
A workflow needs verification of live authentication and network connectivity to its dependencies. Which test fits?
A team must test actual interaction between its agent service and configured search endpoint. Which category fits?
A tool wrapper works locally but fails against the configured service contract. Which test layer fits?
A release requires evidence that several real components interoperate under environment configuration. Which testing strategy fits?''', S3)
item(4,'regressiontest unittest promptcache moreagents','Release checks should preserve previously accepted agent behavior across code, model, prompt, and tool changes.', '''A tool-schema update breaks previously accepted agent tasks. Which test suite should gate release?
A new model version improves one workflow but harms prior supported cases. Which release check fits?
A team needs to ensure prompt edits preserve previously validated task outcomes. Which testing practice fits?
An agent release must rerun accepted behavior cases and automated quality checks. Which test category fits?
A code refactor changes tool choice even though isolated functions still pass. Which broader test practice fits?
A platform needs repeatable evidence that an update does not break established multi-agent capabilities. Which release testing fits?''', S3)
item(4,'pipeline directprod audit examples','CI/CD should require reviewed artifacts and passing checks before promotion rather than treating successful packaging as acceptance.', '''A release pipeline deploys despite failed security and agent-quality checks. Which CI/CD change fits?
A team wants automated builds with enforced test and evaluation gates before production. Which pipeline strategy fits?
An agent release reaches users even when integration checks fail. Which process correction fits?
A platform must record and enforce required evidence before promoting an artifact. Which CI/CD approach fits?
A project needs security, test, and quality failures to block agent deployment. Which pipeline control fits?
An enterprise wants a reproducible release process that does not silently bypass failed evaluations. Which approach fits?''', S3)
item(4,'toolguard resultguard outputguard promptcache audit','Select TWO. The requested controls apply immediately around tool execution, not only to final user-facing text.', '''A guardrail design needs checks immediately before a tool action and immediately after its response. Which TWO controls fit? (Select TWO.)
A platform must enforce pre-action policy and screen external results before agents reuse them. Which TWO interventions fit? (Select TWO.)
An agent workflow cannot rely only on final answer screening for tool safety. Which TWO tool-boundary controls fit? (Select TWO.)
A tool ecosystem needs authorization before side effects and validation of returned content. Which TWO guardrails fit? (Select TWO.)
A business action should be checked before execution and its result treated as untrusted afterward. Which TWO controls fit? (Select TWO.)
A team is implementing the two guardrail boundaries surrounding each external tool operation. Which TWO interventions fit? (Select TWO.)''', S2, correct=2)
item(4,'immutable isolateenv directprod sharedidentity unbounded','Select TWO. Identifiable artifacts and separate environment authority reduce release drift and accidental production effects.', '''A multi-environment rollout needs reproducible artifacts and separation of production authority. Which TWO practices fit? (Select TWO.)
An enterprise wants to avoid rebuilding untracked variants and sharing production credentials with test. Which TWO controls fit? (Select TWO.)
A release strategy must preserve artifact identity while isolating environment permissions. Which TWO practices fit? (Select TWO.)
A platform's staging and production builds differ unexpectedly and use one privileged identity. Which TWO corrections fit? (Select TWO.)
A regulated deployment needs reviewable version promotion and distinct environment access. Which TWO controls fit? (Select TWO.)
An agent CI/CD process must reduce unreviewed deployment differences and cross-environment access. Which TWO practices fit? (Select TWO.)''', S3, correct=2)
item(4,'leastsecret rotation sharedkey logsall sharedidentity','Select TWO. Secret access must be scoped and credentials managed through a tested replacement lifecycle.', '''A tool credential is accessible to all agents and never changes. Which TWO security improvements fit? (Select TWO.)
A platform needs limited credential retrieval and a tested process for replacing credentials. Which TWO practices fit? (Select TWO.)
An enterprise must reduce secret exposure and manage credential lifetime. Which TWO controls fit? (Select TWO.)
A solution stores secrets centrally but grants all workloads broad retrieval and ignores rotation. Which TWO corrections fit? (Select TWO.)
An agent tool ecosystem needs least-privilege secret use and safe credential renewal. Which TWO practices fit? (Select TWO.)
A security review finds excessive secret permissions and stale static credentials. Which TWO controls address these issues? (Select TWO.)''', S1, correct=2)
# Set-specific implementation/calculation cases replace selected base prompts.
def case(set_number, objective, question, choices, reason):
    base = ITEMS[objective - 1]
    assert base['correct'] == 1 and len(choices) == 4
    keys = []
    for n, (label, explanation) in enumerate(choices):
        key = f'case_{set_number}_{objective}_{n}'
        term(key, label, explanation)
        keys.append(key)
    OVERRIDES[(set_number, objective)] = {**base, 'keys': keys, 'reason': reason,
                                         'prompts': [question] * 6}

case(1,47,'Python review: jobs are launched with await asyncio.gather(*(call_tool(x) for x in inputs)). The inputs can contain thousands of entries. Which modification bounds active tool calls without serializing all work?',[
 ('Wrap each call in async with a shared asyncio.Semaphore(limit)','A shared semaphore permits at most the configured number of active protected calls.'),
 ('Construct a new semaphore inside every call','A separate semaphore per call does not impose a shared concurrency limit.'),
 ('Add time.sleep(1) inside each coroutine','Blocking sleep stalls the event loop and does not establish a shared active-call bound.'),
 ('Increase the number of gathered coroutines','More scheduled work can increase pressure rather than enforce a limit.')],
 'Use one shared limiter around the protected asynchronous operation. Also enforce rate budgets because concurrency and requests per minute are different constraints.')
case(2,42,'Python review: a remote read is awaited indefinitely. Which pattern directly adds a caller-side timeout to that await, without claiming the remote operation is rolled back?',[
 ('await asyncio.wait_for(remote_read(), timeout=5)','wait_for bounds the local await and raises a timeout condition; application handling and remote cancellation semantics still matter.'),
 ('await remote_read() followed by checking elapsed time','A check after an indefinitely blocked await cannot enforce its deadline.'),
 ('time.sleep(5) before await remote_read()','Sleeping before the call delays work but does not bound the later await.'),
 ('Retry remote_read() forever','Unlimited retry can extend work indefinitely and increase load.')],
 'Bound the local await, handle the timeout, and determine remote status before retrying side-effecting operations. Local cancellation does not prove a remote operation did not commit.')
case(3,41,'A queue delivers the same purchase message twice. Which pseudocode design best prevents duplicate purchases while allowing recovery after a worker restart?',[
 ('Use the message logical-action ID as a provider idempotency key and persist the result','A stable ID and durable outcome allow repeated delivery to map to one logical operation, subject to provider guarantees.'),
 ('Generate a new random idempotency key on every retry','Different keys make the provider treat retries as distinct operations.'),
 ('Track completed IDs only in a local Python set','Process-local state is lost on restart and is not a shared durable duplicate boundary.'),
 ('Log the purchase after sending it and ignore duplicates','Logging alone does not prevent repeated external effects or handle a crash between the effect and the log.')],
 'Duplicate protection must survive retries and restarts and align with the external side-effect boundary. Do not assume at-least-once delivery means exactly-once execution.')
case(4,32,'Code review: a search filter uses tenant_id taken directly from request JSON. A signed-in user changes that JSON to another tenant. What is the most important correction?',[
 ('Derive the allowed tenant scope from trusted identity and enforce it in the server-side query','The security boundary must use an authenticated authorization context rather than caller-controlled ownership claims.'),
 ('Ask the model to ignore results belonging to other tenants','Unauthorized content would already have reached the model and the instruction is not an access control.'),
 ('Use a larger embedding model','Embedding quality does not establish tenant authorization.'),
 ('Filter the final answer only for tenant names','Removing names cannot reliably remove restricted facts or prevent retrieval exposure.')],
 'Trusted authorization must constrain retrieval before restricted evidence enters model context. A user-supplied tenant parameter is not proof of permission.')
case(5,39,'Pseudocode accepts a tool response when status == 200. The JSON has amount="unknown" where the contract requires a non-negative decimal. What should the wrapper do?',[
 ('Reject or safely handle the response using schema and domain validation before downstream use','The payload violates both expected type and business constraints despite successful transport.'),
 ('Convert unknown to zero and proceed silently','Silent substitution fabricates a business value and can cause incorrect actions.'),
 ('Treat HTTP 200 as proof of a valid amount','Transport success does not validate payload semantics.'),
 ('Ask the next agent to infer the missing amount','An inferred financial value is not an authoritative tool result.')],
 'Validate required fields, types, and domain constraints. A malformed value should follow a defined failure path rather than become a guessed business fact.')
case(6,48,'A framework permits wrapping every tool execution. Where should reusable authorization and trace-correlation checks be placed so they run regardless of the prompt wording?',[
 ('In trusted middleware around the execution boundary','A controlled execution hook can enforce checks consistently before invoking the operation.'),
 ('Only in each agent persona paragraph','Natural-language role text does not enforce execution permissions.'),
 ('Only in the final answer formatter','Final formatting happens after tool side effects may already have occurred.'),
 ('In the model training corpus alone','Training cannot replace request-specific runtime authorization.')],
 'Cross-cutting checks should execute in trusted code at the appropriate boundary. Prompts can describe policy but must not be its sole enforcement mechanism.')

case(1,61,'Three independent checks take 4, 7, and 5 seconds. A 3-second synthesis must wait for all three. Ignoring overhead and contention, what is the minimum end-to-end duration with concurrent checks?',[
 ('10 seconds','The independent stage takes max(4,7,5)=7 seconds, followed by 3 seconds of synthesis.'),
 ('19 seconds','This sums all checks and synthesis as though the checks were sequential.'),
 ('7 seconds','This omits the dependent 3-second synthesis stage.'),
 ('3 seconds','The synthesis cannot begin before the checks finish.')],
 'Respect dependencies: concurrent independent branches take the longest branch duration, then the dependent stage adds its duration. Real scheduling and network overhead can increase this lower bound.')
case(2,62,'Each task makes exactly 3 calls to a shared service limited to 90 calls per minute. Ignoring bursts and all other limits, what is the upper bound on sustained completed tasks per minute?',[
 ('30 tasks per minute','The service budget permits 90/3=30 tasks per minute in this simplified workload.'),
 ('90 tasks per minute','That treats one task as one call instead of three.'),
 ('270 tasks per minute','Multiplying by calls per task reverses the required calculation.'),
 ('Unlimited tasks if enough agents run','Additional workers do not remove the service rate limit.')],
 'Divide the available request budget by calls per task. In practice, retries, burst policies, and other shared consumers reduce usable capacity.')
case(3,68,'An end-to-end completion objective is 99% over 10,000 eligible runs. Under a simple count-based definition, how many unsuccessful runs can occur while meeting the objective exactly?',[
 ('100 unsuccessful runs','A 1% unsuccessful fraction of 10,000 is 100.'),
 ('10 unsuccessful runs','Ten failures would correspond to a 0.1% unsuccessful fraction, not the full 1% allowance.'),
 ('1,000 unsuccessful runs','A thousand unsuccessful runs would leave only 90% successful completion.'),
 ('Zero unsuccessful runs','A 99% objective allows a limited unsuccessful fraction under this definition.')],
 'The count-based error allowance is (1-0.99) times 10,000. Real SLO definitions must specify eligible events, windows, and exclusions.')
case(4,70,'A workflow averages 8,000 input tokens and 2,000 output tokens per run. It executes 120 runs. Ignoring caching and retries, how many total model tokens are processed?',[
 ('1,200,000 tokens','Each run uses 10,000 tokens, so 120 runs use 1,200,000.'),
 ('960,000 tokens','This counts only the input tokens.'),
 ('240,000 tokens','This counts only the output tokens.'),
 ('10,000 tokens','This counts one run rather than all 120.')],
 'Aggregate both input and output token volumes across runs. Monetary cost still depends on their separate prices and any applicable caching or other usage rules.')
case(5,54,'For one labeled query, 4 of the top 5 retrieved passages are relevant. What is precision at 5 for this query?',[
 ('0.8','Precision at 5 is relevant retrieved items divided by 5, so 4/5=0.8.'),
 ('0.2','This is the irrelevant fraction, 1/5.'),
 ('4.0','The count of relevant passages is not a fraction-based precision score.'),
 ('Cannot be computed without the total relevant corpus size','That total is needed for recall, not for this precision-at-5 calculation.')],
 'Retrieval precision measures how much of the returned set is relevant. It does not prove answer groundedness or establish recall across the full corpus.')
case(6,72,'A fixed benchmark has 200 cases. The baseline completes 180 correctly; a candidate completes 170 correctly. What is the candidate accuracy change in percentage points?',[
 ('A decrease of 5 percentage points','Baseline accuracy is 90%; candidate accuracy is 85%; the difference is minus 5 percentage points.'),
 ('A decrease of 10 percentage points','Ten is the difference in correct-case counts, not the difference in percentage points.'),
 ('An increase of 5 percentage points','The candidate has fewer correct completions, so the direction is a decrease.'),
 ('No change because both use 200 cases','An equal denominator does not imply equal performance.')],
 'Distinguish counts, percentage points, and relative percentage change. Review case severity and confidence as well as the aggregate score before promotion.')

case(1,78,'A tool API receives a cryptographically valid token whose audience names a different API. What should the receiving API do?',[
 ('Reject the request because the token is not intended for this API','Signature validity alone does not establish that the receiving API is an authorized audience.'),
 ('Accept it because the signature is valid','This omits the intended recipient and operation authorization checks.'),
 ('Ask the model whether the caller seems trustworthy','A model judgment is not token validation.'),
 ('Ignore audience validation when traffic uses a private endpoint','Network location does not replace application authentication and authorization.')],
 'Validate issuer, signature, expiry, audience, and appropriate authorization requirements. Private routing is not a reason to accept a token intended for another recipient.')
case(2,82,'A read-only retrieval agent is assigned Contributor at subscription scope. Which change most directly reduces its resource authorization blast radius?',[
 ('Replace the broad role with only necessary supported data access at the narrowest suitable scope','The role and scope should match the actual permitted operations.'),
 ('Keep Contributor and add read-only wording to the prompt','The identity retains the same enforceable permissions despite the wording.'),
 ('Keep Contributor and hide management actions from the UI','Hidden UI controls do not remove API authority.'),
 ('Share the identity with all specialists','Sharing broad authority extends the exposure rather than reducing it.')],
 'Permissions are enforced by identity and access policy, not user-interface visibility or behavioral instructions. Distinguish management-plane and data-plane roles for the target service.')
case(3,91,'A canary passes HTTP health checks but its evaluated task-success rate drops below the release gate. What should the rollout controller do?',[
 ('Stop expansion and apply the defined rollback or investigation policy','Task quality is a release condition even when the service process remains healthy.'),
 ('Expand because successful HTTP responses prove acceptable quality','Transport availability does not prove correct task outcomes.'),
 ('Disable the quality gate until the rollout finishes','Bypassing the gate defeats the purpose of limiting initial exposure.'),
 ('Route every user to the canary to obtain more data immediately','Expanding exposure after a failed gate increases user risk.')],
 'A production gate should include relevant quality and safety outcomes as well as health. Follow the pre-approved response policy instead of silently redefining acceptance.')
case(4,92,'A release changes a tool schema from v1 to v2 and persists v2 workflow state. Reverting only the prompt still fails. What should the rollback plan have included?',[
 ('A compatible artifact set and an explicit state compatibility or migration plan','Code, prompt, tool contract, and durable state must work together during recovery.'),
 ('Only the previous prompt text','The observed failure involves additional incompatible components.'),
 ('Only a larger context window','More context does not restore a broken tool or state contract.'),
 ('Only disabling logs','Removing evidence does not repair compatibility and harms investigation.')],
 'Rollback is a system operation, not necessarily a single-file revert. Test recovery with persisted in-flight state and external side effects before relying on it.')
case(5,95,'A connector test replaces the real API with a mock that never validates tokens. Production later fails because of the configured token audience. Which additional test is most direct?',[
 ('An environment integration test against the configured API authentication boundary','It verifies the actual service contract and token validation rather than the mock assumption.'),
 ('Another unit test using the same permissive mock','The same mock cannot expose a validation rule it does not model.'),
 ('A grammar check of the agent answer','Output language quality does not test API authentication.'),
 ('A larger model benchmark','Model capacity does not correct a misconfigured token audience.')],
 'Mocks support isolated tests but do not prove environment integration. Use scoped test credentials and safe operations when checking real authentication boundaries.')
case(6,79,'An agent retrieves a secret from Key Vault correctly but then inserts its value into a model prompt for convenience. Which correction is most important?',[
 ('Keep the secret in trusted execution code and expose only a scoped tool capability to the model','The model can request a permitted operation without receiving the raw credential.'),
 ('Keep putting the secret in prompts because Key Vault stored it originally','Secure storage does not make every later disclosure safe.'),
 ('Encode the secret with Base64 before adding it to the prompt','Base64 is reversible encoding, not an access boundary.'),
 ('Ask the model not to repeat the secret','A behavioral request does not remove the secret from context or guarantee non-disclosure.')],
 'Secret governance extends beyond storage. Retrieve only where necessary, keep credentials out of model context and telemetry, and authorize the operation in trusted code.')
