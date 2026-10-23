# Google Cloud Professional Agentic Architect (PAA) — Practice Set 2

Custom Agents: Models, ADK, Memory, RAG, and Retrieval

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded five-domain review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A task requires nuanced multi-document reasoning and tolerance for ambiguity. Which model class should be evaluated first?

Domain: Developing Custom Agents

- A. Use an open model where portability and control matter
- B. Use a tuned model where specialized behavior justifies it
- C. Use a smaller model for a narrow, high-volume task
- D. Use a large model for complex reasoning or broad language work

### 2. A high-volume classifier handles short, well-bounded messages with strict latency limits. Which option should be tested?

Domain: Developing Custom Agents

- A. Use a proprietary model where supported capability matters
- B. Use a smaller model for a narrow, high-volume task
- C. Use a managed model service under the applicable terms
- D. Use a large model for complex reasoning or broad language work

### 3. A cheaper model produces more retries and human corrections than a stronger one. What should decide selection?

Domain: Developing Custom Agents

- A. Select and deploy supported models through Model Garden
- B. Compare total cost per successful task
- C. Set an end-to-end latency budget
- D. Use a tuned model where specialized behavior justifies it

### 4. A voice agent needs a response within a strict time window including retrieval and tools. What should be designed first?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Set an end-to-end latency budget
- C. Use a smaller model for a narrow, high-volume task
- D. Fit retrieved evidence within the model's usable context

### 5. A regulated workload requires model execution inside a controlled network boundary. What should be evaluated?

Domain: Developing Custom Agents

- A. Use an open model where portability and control matter
- B. Host the model on infrastructure you control
- C. Select and deploy supported models through Model Garden
- D. Use a managed model service under the applicable terms

### 6. A startup wants minimal operational burden for a new agent with variable demand. What option fits best?

Domain: Developing Custom Agents

- A. Use a tuned model where specialized behavior justifies it
- B. Host the model on infrastructure you control
- C. Use a managed model service under the applicable terms
- D. Use an open model where portability and control matter

### 7. A repetitive extraction task has abundant labeled examples and a stable schema. What approach may improve consistency?

Domain: Developing Custom Agents

- A. Use a smaller model for a narrow, high-volume task
- B. Use a large model for complex reasoning or broad language work
- C. Select and deploy supported models through Model Garden
- D. Use a tuned model where specialized behavior justifies it

### 8. A team needs weight-level customization and portability across environments. What should it consider?

Domain: Developing Custom Agents

- A. Use an open model where portability and control matter
- B. Use a managed model service under the applicable terms
- C. Use a proprietary model where supported capability matters
- D. Host the model on infrastructure you control

### 9. A workflow depends on a vendor capability that is only available in a managed proprietary model. What is the trade-off to document?

Domain: Developing Custom Agents

- A. Host the model on infrastructure you control
- B. Use an open model where portability and control matter
- C. Use a proprietary model where supported capability matters
- D. Use a smaller model for a narrow, high-volume task

### 10. A team wants to compare multiple supported models without building separate integrations. What should it use?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Select and deploy supported models through Model Garden
- C. Bundle related skills, tools, and configuration as a plugin
- D. Publish an Agent Card describing capabilities and endpoints

### 11. A team needs code-level control over an agent's tools, callbacks, and orchestration. What should it use?

Domain: Developing Custom Agents

- A. Define an LLM-backed agent with instructions and scoped tools
- B. Run agents in a fixed sequence
- C. Build the agent with the Agent Development Kit
- D. Run independent agents concurrently

### 12. A single agent must answer questions using three approved tools. What should be defined?

Domain: Developing Custom Agents

- A. Run agents in a fixed sequence
- B. Route a request to the most suitable specialist agent
- C. Define an LLM-backed agent with instructions and scoped tools
- D. Use a graph workflow for branching dependencies

### 13. A tool sometimes receives a malformed date from the model. What should the tool do?

Domain: Developing Custom Agents

- A. Return structured tool errors that guide recovery
- B. Expose a typed function as a tool
- C. Publish an Agent Card describing capabilities and endpoints
- D. Define a narrow tool schema with a clear description

### 14. A broad tool accepts arbitrary SQL from the model. What is the main design problem?

Domain: Developing Custom Agents

- A. Define a narrow tool schema with a clear description
- B. Use MCP for standardized tool and resource access
- C. Publish an Agent Card describing capabilities and endpoints
- D. Expose a typed function as a tool

### 15. A downstream API returns a transient 503 during a read operation. What should the tool wrapper do?

Domain: Developing Custom Agents

- A. Return structured tool errors that guide recovery
- B. Expose a typed function as a tool
- C. Require human approval before a consequential action
- D. Enforce a policy check before a consequential action

### 16. A team wants to redact sensitive fields before any model sees tool output. Where should that happen?

Domain: Developing Custom Agents

- A. Expose a typed function as a tool
- B. Run deterministic logic when a lifecycle event fires
- C. Enforce a policy check before a consequential action
- D. Use callbacks for validation, logging, or guardrails

### 17. A workflow must always run extraction, then validation, then drafting. What orchestration pattern fits?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Run agents in a fixed sequence
- C. Repeat work until a defined stop condition is met
- D. Run independent agents concurrently

### 18. Three independent research queries must complete before synthesis. What pattern reduces latency?

Domain: Developing Custom Agents

- A. Repeat work until a defined stop condition is met
- B. Run agents in a fixed sequence
- C. Run independent agents concurrently
- D. Route a request to the most suitable specialist agent

### 19. An agent must poll a job until it completes or a limit is reached. What must the loop include?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Use a graph workflow for branching dependencies
- C. Run agents in a fixed sequence
- D. Repeat work until a defined stop condition is met

### 20. A workflow branches on document type and later rejoins for review. What pattern expresses this?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Use a graph workflow for branching dependencies
- C. Run agents in a fixed sequence
- D. Run independent agents concurrently

### 21. A conversation must retain the user's current order draft across turns. What should hold it?

Domain: Developing Custom Agents

- A. Store durable user or domain memory in Memory Bank
- B. Pass files and large outputs as artifacts
- C. Store task-scoped state deliberately
- D. Persist conversation and task state in a session

### 22. An assistant should remember a user's stated accessibility preference across future conversations. What capability fits?

Domain: Developing Custom Agents

- A. Persist conversation and task state in a session
- B. Store durable user or domain memory in Memory Bank
- C. Store task-scoped state deliberately
- D. Pass files and large outputs as artifacts

### 23. An agent stores every intermediate tool output in session state. What problem should be addressed?

Domain: Developing Custom Agents

- A. Store durable user or domain memory in Memory Bank
- B. Fit retrieved evidence within the model's usable context
- C. Store task-scoped state deliberately
- D. Persist conversation and task state in a session

### 24. A memory feature could retain health details indefinitely. What should be defined?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Persist conversation and task state in a session
- C. Define what may be remembered, for how long, and why
- D. Store durable user or domain memory in Memory Bank

### 25. A generated 40-page report must be available to later turns without repeated prompting. What should be used?

Domain: Developing Custom Agents

- A. Pass files and large outputs as artifacts
- B. Store durable user or domain memory in Memory Bank
- C. Persist conversation and task state in a session
- D. Store task-scoped state deliberately

### 26. Sessions must survive instance restarts and scale across replicas. What should be used?

Domain: Developing Custom Agents

- A. Persist conversation and task state in a session
- B. Use Memorystore for Redis for fast shared ephemeral state
- C. Store task-scoped state deliberately
- D. Persist sessions in a durable managed store

### 27. A team wants personalized continuity without changing model weights. What should it evaluate?

Domain: Developing Custom Agents

- A. Store durable user or domain memory in Memory Bank
- B. Choose an embedding model suited to the domain and language
- C. Use a tuned model where specialized behavior justifies it
- D. Use RAG Engine for managed retrieval pipeline components

### 28. Two users share one agent deployment and one global state object. What risk arises?

Domain: Developing Custom Agents

- A. Persist conversation and task state in a session
- B. Store durable user or domain memory in Memory Bank
- C. Pass files and large outputs as artifacts
- D. Store task-scoped state deliberately

### 29. A user asks what the agent remembers about them. What must the design support?

Domain: Developing Custom Agents

- A. Define what may be remembered, for how long, and why
- B. Record agent actions and tool calls in audit logs
- C. Redact or de-identify sensitive data before model exposure
- D. Apply purpose limitation and consent to personal data

### 30. A long-running session accumulates outdated constraints. What should the agent do?

Domain: Developing Custom Agents

- A. Fit retrieved evidence within the model's usable context
- B. Pass files and large outputs as artifacts
- C. Persist conversation and task state in a session
- D. Store durable user or domain memory in Memory Bank

### 31. A knowledge base mixes long policies and short FAQs. What should be designed carefully?

Domain: Developing Custom Agents

- A. Choose an embedding model suited to the domain and language
- B. Use similarity scoring to retrieve candidate passages
- C. Rerank retrieved passages before generation
- D. Choose chunk size and overlap for retrieval

### 32. Queries use internal acronyms that a generic embedding model does not represent well. What should be evaluated?

Domain: Developing Custom Agents

- A. Choose chunk size and overlap for retrieval
- B. Combine keyword and semantic retrieval
- C. Choose an embedding model suited to the domain and language
- D. Rerank retrieved passages before generation

### 33. Initial retrieval returns many loosely related passages. What can improve precision before generation?

Domain: Developing Custom Agents

- A. Rerank retrieved passages before generation
- B. Ground the response in cited retrieved evidence
- C. Deduplicate near-identical retrieved chunks
- D. Use similarity scoring to retrieve candidate passages

### 34. Users search for exact policy numbers and paraphrased concepts. What retrieval approach fits?

Domain: Developing Custom Agents

- A. Choose an embedding model suited to the domain and language
- B. Combine keyword and semantic retrieval
- C. Ground the response in cited retrieved evidence
- D. Choose chunk size and overlap for retrieval

### 35. A corpus contains documents from several regions with different validity dates. What should retrieval apply?

Domain: Developing Custom Agents

- A. Preserve source and chunk identifiers through the pipeline
- B. Filter retrieval by the requesting user's authorization
- C. Filter retrieval using trusted metadata
- D. Deduplicate near-identical retrieved chunks

### 36. The same paragraph appears in many documents and dominates the context. What should be done?

Domain: Developing Custom Agents

- A. Deduplicate near-identical retrieved chunks
- B. Choose chunk size and overlap for retrieval
- C. Use similarity scoring to retrieve candidate passages
- D. Rerank retrieved passages before generation

### 37. A generated answer cites a document that does not contain the claim. What pipeline change helps?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Rerank retrieved passages before generation
- C. Preserve source and chunk identifiers through the pipeline
- D. Use similarity scoring to retrieve candidate passages

### 38. Auditors must trace an answer back to the exact source passage. What must be preserved?

Domain: Developing Custom Agents

- A. Preserve source and chunk identifiers through the pipeline
- B. Rerank retrieved passages before generation
- C. Store embeddings in a managed vector index
- D. Choose an embedding model suited to the domain and language

### 39. Retrieved evidence exceeds the model context. What should be done?

Domain: Developing Custom Agents

- A. Deduplicate near-identical retrieved chunks
- B. Rerank retrieved passages before generation
- C. Choose chunk size and overlap for retrieval
- D. Fit retrieved evidence within the model's usable context

### 40. A policy was withdrawn, but the index still returns it. What must be verified?

Domain: Developing Custom Agents

- A. Choose an embedding model suited to the domain and language
- B. Ground the response in cited retrieved evidence
- C. Check index freshness and reindexing behavior
- D. Deduplicate near-identical retrieved chunks

### 41. A team wants a managed vector index for semantic retrieval at scale. What should it use?

Domain: Developing Custom Agents

- A. Use RAG Engine for managed retrieval pipeline components
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Store embeddings in a managed vector index
- D. Use BigQuery for governed analytical access to enterprise data

### 42. A team wants managed components for ingestion, indexing, and retrieval. What should it evaluate?

Domain: Developing Custom Agents

- A. Use Cloud SQL for relational state and transactions
- B. Store embeddings in a managed vector index
- C. Use RAG Engine for managed retrieval pipeline components
- D. Use Agent Retrieval and Vector Search for agent-oriented retrieval

### 43. An agent workflow needs retrieval over enterprise content with managed ranking. What should it evaluate?

Domain: Developing Custom Agents

- A. Use RAG Engine for managed retrieval pipeline components
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Connect approved enterprise content through Agent Search
- D. Store embeddings in a managed vector index

### 44. A team wants managed search over indexed enterprise documents without operating an index. What should it evaluate?

Domain: Developing Custom Agents

- A. Use BigQuery for governed analytical access to enterprise data
- B. Connect approved enterprise content through Agent Search
- C. Store embeddings in a managed vector index
- D. Use RAG Engine for managed retrieval pipeline components

### 45. Retrieved chunks include content the requesting user cannot open. What must happen before generation?

Domain: Developing Custom Agents

- A. Limit connected sources to the approved audience and purpose
- B. Filter retrieval using trusted metadata
- C. Constrain access with a principal access boundary policy
- D. Filter retrieval by the requesting user's authorization

### 46. A connector indexes an entire drive for an agent serving one department. What should be corrected?

Domain: Developing Custom Agents

- A. Filter retrieval by the requesting user's authorization
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Apply purpose limitation and consent to personal data
- D. Limit connected sources to the approved audience and purpose

### 47. A tenant identifier is missing from some chunk metadata. What is the safe response?

Domain: Developing Custom Agents

- A. Filter retrieval using trusted metadata
- B. Filter retrieval by the requesting user's authorization
- C. Use similarity scoring to retrieve candidate passages
- D. Rerank retrieved passages before generation

### 48. A retrieval result cannot be tied to its source document after transformation. What is the defect?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Preserve source and chunk identifiers through the pipeline
- C. Deduplicate near-identical retrieved chunks
- D. Rerank retrieved passages before generation

### 49. A source system updates hourly, but the index refreshes weekly. What should be reviewed?

Domain: Developing Custom Agents

- A. Check index freshness and reindexing behavior
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Store embeddings in a managed vector index
- D. Use RAG Engine for managed retrieval pipeline components

### 50. Near-duplicate boilerplate outranks the single relevant clause. What should be adjusted?

Domain: Developing Custom Agents

- A. Use similarity scoring to retrieve candidate passages
- B. Rerank retrieved passages before generation
- C. Deduplicate near-identical retrieved chunks
- D. Choose chunk size and overlap for retrieval

### 51. A task requires understanding scanned forms with tables and handwriting. What model capability should be tested first?

Domain: Developing Custom Agents

- A. Use a smaller model for a narrow, high-volume task
- B. Select and deploy supported models through Model Garden
- C. Use a tuned model where specialized behavior justifies it
- D. Use a large model for complex reasoning or broad language work

### 52. A routing classifier must decide among five intents in under 200 milliseconds. What should guide model choice?

Domain: Developing Custom Agents

- A. Use a managed model service under the applicable terms
- B. Use a smaller model for a narrow, high-volume task
- C. Use a large model for complex reasoning or broad language work
- D. Set an end-to-end latency budget

### 53. A team wants to avoid depending on one provider for a critical workflow. What should it design?

Domain: Developing Custom Agents

- A. Use a proprietary model where supported capability matters
- B. Select and deploy supported models through Model Garden
- C. Host the model on infrastructure you control
- D. Use an open model where portability and control matter

### 54. A complex agent succeeds more often with a stronger model but costs four times more. What analysis is needed?

Domain: Developing Custom Agents

- A. Use a tuned model where specialized behavior justifies it
- B. Use a large model for complex reasoning or broad language work
- C. Compare total cost per successful task
- D. Set an end-to-end latency budget

### 55. A team wants to fine-tune a model on sensitive internal data. What deployment question arises?

Domain: Developing Custom Agents

- A. Use a proprietary model where supported capability matters
- B. Host the model on infrastructure you control
- C. Use an open model where portability and control matter
- D. Use a managed model service under the applicable terms

### 56. A multi-step agent adds model calls at each stage. What should be measured end to end?

Domain: Developing Custom Agents

- A. Run agents in a fixed sequence
- B. Run independent agents concurrently
- C. Use a smaller model for a narrow, high-volume task
- D. Set an end-to-end latency budget

### 57. A team wants the model to learn a proprietary response format. What approach may fit better than retrieval?

Domain: Developing Custom Agents

- A. Use a tuned model where specialized behavior justifies it
- B. Use RAG Engine for managed retrieval pipeline components
- C. Choose an embedding model suited to the domain and language
- D. Select and deploy supported models through Model Garden

### 58. A model is deprecated with a short notice period. What should the architecture include?

Domain: Developing Custom Agents

- A. Use a proprietary model where supported capability matters
- B. Host the model on infrastructure you control
- C. Use a smaller model for a narrow, high-volume task
- D. Use an open model where portability and control matter

### 59. A team needs a documented inventory of approved models and versions. What should it maintain?

Domain: Developing Custom Agents

- A. Bundle related skills, tools, and configuration as a plugin
- B. Select and deploy supported models through Model Garden
- C. Publish an Agent Card describing capabilities and endpoints
- D. Register agents and capabilities in Agent Registry

### 60. A high-volume agent has variable task difficulty. What routing strategy may reduce cost?

Domain: Developing Custom Agents

- A. Provision capacity for peak concurrency and quotas
- B. Use a large model for complex reasoning or broad language work
- C. Use a smaller model for a narrow, high-volume task
- D. Compare total cost per successful task

### 61. A team needs a code-defined agent with typed tools and lifecycle validation. What should it use?

Domain: Developing Custom Agents

- A. Expose a typed function as a tool
- B. Use callbacks for validation, logging, or guardrails
- C. Define an LLM-backed agent with instructions and scoped tools
- D. Build the agent with the Agent Development Kit

### 62. A tool returns unstructured text that the agent must parse. What should improve reliability?

Domain: Developing Custom Agents

- A. Define a narrow tool schema with a clear description
- B. Expose a typed function as a tool
- C. Register agents and capabilities in Agent Registry
- D. Publish an Agent Card describing capabilities and endpoints

### 63. A team wants to log every model request and response for debugging. Where should that occur?

Domain: Developing Custom Agents

- A. Enforce a policy check before a consequential action
- B. Run deterministic logic when a lifecycle event fires
- C. Use callbacks for validation, logging, or guardrails
- D. Screen prompts and responses with Model Armor

### 64. An ADK workflow needs a fixed two-step pipeline. What should it use?

Domain: Developing Custom Agents

- A. Repeat work until a defined stop condition is met
- B. Use a graph workflow for branching dependencies
- C. Run independent agents concurrently
- D. Run agents in a fixed sequence

### 65. An ADK workflow needs to run three independent searches. What should it use?

Domain: Developing Custom Agents

- A. Run agents in a fixed sequence
- B. Use a graph workflow for branching dependencies
- C. Run independent agents concurrently
- D. Repeat work until a defined stop condition is met

### 66. An ADK workflow must retry a step until a validator passes. What should bound it?

Domain: Developing Custom Agents

- A. Repeat work until a defined stop condition is met
- B. Run agents in a fixed sequence
- C. Run independent agents concurrently
- D. Use a graph workflow for branching dependencies

### 67. A coordinator must choose among three specialists based on intent. What pattern fits?

Domain: Developing Custom Agents

- A. Define an LLM-backed agent with instructions and scoped tools
- B. Delegate a scoped task to a specialized agent
- C. Transfer control with explicit context and state
- D. Route a request to the most suitable specialist agent

### 68. An ADK agent can issue refunds. What should gate the tool call?

Domain: Developing Custom Agents

- A. Expose a typed function as a tool
- B. Require human approval before a consequential action
- C. Gate the action on explicit, attributable approval
- D. Enforce a policy check before a consequential action

### 69. A tool returns a 429 rate-limit response. What should the wrapper do?

Domain: Developing Custom Agents

- A. Inspect spans across agent, model, and tool calls
- B. Expose a typed function as a tool
- C. Set timeouts and bounded retries for tool calls
- D. Return structured tool errors that guide recovery

### 70. A callback must persist a validated intermediate result. What should it use?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Pass files and large outputs as artifacts
- C. Use callbacks for validation, logging, or guardrails
- D. Persist conversation and task state in a session

### 71. A returning user expects continuity but no recollection of a sensitive prior issue. What should memory policy define?

Domain: Developing Custom Agents

- A. Store durable user or domain memory in Memory Bank
- B. Pass files and large outputs as artifacts
- C. Store task-scoped state deliberately
- D. Persist conversation and task state in a session

### 72. A session state object grows to include every retrieved document. What should change?

Domain: Developing Custom Agents

- A. Fit retrieved evidence within the model's usable context
- B. Store durable user or domain memory in Memory Bank
- C. Persist conversation and task state in a session
- D. Store task-scoped state deliberately

### 73. A user withdraws consent for personalization. What must happen?

Domain: Developing Custom Agents

- A. Apply purpose limitation and consent to personal data
- B. Redact or de-identify sensitive data before model exposure
- C. Record agent actions and tool calls in audit logs
- D. Define what may be remembered, for how long, and why

### 74. A team confuses durable user memory with document retrieval. What distinction matters?

Domain: Developing Custom Agents

- A. Store durable user or domain memory in Memory Bank
- B. Use RAG Engine for managed retrieval pipeline components
- C. Register agents and capabilities in Agent Registry
- D. Store embeddings in a managed vector index

### 75. Multiple workers must see the same conversation state. What should be used?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Persist conversation and task state in a session
- C. Use Memorystore for Redis for fast shared ephemeral state
- D. Persist sessions in a durable managed store

### 76. An agent generates a large PDF for later steps. What should it store?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Pass files and large outputs as artifacts
- C. Persist conversation and task state in a session
- D. Store durable user or domain memory in Memory Bank

### 77. Long-term memory contains an outdated address. What should the design support?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Store durable user or domain memory in Memory Bank
- C. Redact or de-identify sensitive data before model exposure
- D. Define what may be remembered, for how long, and why

### 78. A conversation has run for hours and context is near its limit. What should the agent do?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Fit retrieved evidence within the model's usable context
- C. Persist conversation and task state in a session
- D. Store durable user or domain memory in Memory Bank

### 79. Session identifiers are sequential and guessable across tenants. What risk arises?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Constrain access with a principal access boundary policy
- C. Filter retrieval using trusted metadata
- D. Filter retrieval by the requesting user's authorization

### 80. A team wants personalization without retraining a model. What should it evaluate?

Domain: Developing Custom Agents

- A. Bundle related skills, tools, and configuration as a plugin
- B. Use a tuned model where specialized behavior justifies it
- C. Choose an embedding model suited to the domain and language
- D. Store durable user or domain memory in Memory Bank

### 81. A document's answer spans two adjacent sections. What chunking concern matters?

Domain: Developing Custom Agents

- A. Rerank retrieved passages before generation
- B. Choose chunk size and overlap for retrieval
- C. Choose an embedding model suited to the domain and language
- D. Combine keyword and semantic retrieval

### 82. A first-stage retriever returns 100 candidates and the model can use 5. What should happen between?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Use similarity scoring to retrieve candidate passages
- C. Deduplicate near-identical retrieved chunks
- D. Rerank retrieved passages before generation

### 83. A corpus includes drafts and approved documents with the same title. What should retrieval use?

Domain: Developing Custom Agents

- A. Filter retrieval by the requesting user's authorization
- B. Check index freshness and reindexing behavior
- C. Filter retrieval using trusted metadata
- D. Preserve source and chunk identifiers through the pipeline

### 84. Users search for exact invoice numbers and conceptual descriptions. What should be combined?

Domain: Developing Custom Agents

- A. Combine keyword and semantic retrieval
- B. Choose an embedding model suited to the domain and language
- C. Use similarity scoring to retrieve candidate passages
- D. Rerank retrieved passages before generation

### 85. A response synthesizes three sources but cites only one. What should grounding require?

Domain: Developing Custom Agents

- A. Rerank retrieved passages before generation
- B. Deduplicate near-identical retrieved chunks
- C. Ground the response in cited retrieved evidence
- D. Preserve source and chunk identifiers through the pipeline

### 86. A PDF contains tables that lose meaning when split by characters. What should the pipeline do?

Domain: Developing Custom Agents

- A. Store embeddings in a managed vector index
- B. Use RAG Engine for managed retrieval pipeline components
- C. Choose an embedding model suited to the domain and language
- D. Choose chunk size and overlap for retrieval

### 87. A policy search returns an archived version before the current one. What should be enforced?

Domain: Developing Custom Agents

- A. Deduplicate near-identical retrieved chunks
- B. Check index freshness and reindexing behavior
- C. Filter retrieval using trusted metadata
- D. Combine keyword and semantic retrieval

### 88. A query is ambiguous and retrieves two unrelated topics. What should happen before answering?

Domain: Developing Custom Agents

- A. Rerank retrieved passages before generation
- B. Use similarity scoring to retrieve candidate passages
- C. Choose chunk size and overlap for retrieval
- D. Ground the response in cited retrieved evidence

### 89. A multilingual corpus must serve queries in several languages. What should be evaluated?

Domain: Developing Custom Agents

- A. Choose chunk size and overlap for retrieval
- B. Combine keyword and semantic retrieval
- C. Rerank retrieved passages before generation
- D. Choose an embedding model suited to the domain and language

### 90. Retrieved passages conflict with each other. What should the response do?

Domain: Developing Custom Agents

- A. Rerank retrieved passages before generation
- B. Deduplicate near-identical retrieved chunks
- C. Fit retrieved evidence within the model's usable context
- D. Ground the response in cited retrieved evidence

### 91. A team must rebuild an index after changing embedding models. What should the plan include?

Domain: Developing Custom Agents

- A. Use BigQuery for governed analytical access to enterprise data
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Store embeddings in a managed vector index
- D. Use RAG Engine for managed retrieval pipeline components

### 92. An agent needs low-latency retrieval over approved enterprise content. What should it evaluate?

Domain: Developing Custom Agents

- A. Connect approved enterprise content through Agent Search
- B. Use Cloud SQL for relational state and transactions
- C. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- D. Store embeddings in a managed vector index

### 93. A vector index has no tenant field, but serves multiple tenants. What should be done?

Domain: Developing Custom Agents

- A. Filter retrieval using trusted metadata
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Constrain access with a principal access boundary policy
- D. Filter retrieval by the requesting user's authorization

### 94. A retrieval workload has bursty query volume. What should be planned?

Domain: Developing Custom Agents

- A. Use RAG Engine for managed retrieval pipeline components
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Use Memorystore for Redis for fast shared ephemeral state
- D. Store embeddings in a managed vector index

### 95. A team wants to avoid operating index infrastructure. What should it evaluate?

Domain: Developing Custom Agents

- A. Use Cloud Storage for large artifacts and source documents
- B. Store embeddings in a managed vector index
- C. Use BigQuery for governed analytical access to enterprise data
- D. Use Cloud SQL for relational state and transactions

### 96. Deleted documents remain in the index for weeks. What should be fixed?

Domain: Developing Custom Agents

- A. Check index freshness and reindexing behavior
- B. Filter retrieval using trusted metadata
- C. Preserve source and chunk identifiers through the pipeline
- D. Deduplicate near-identical retrieved chunks

### 97. The same content is indexed under three URLs. What should retrieval do?

Domain: Developing Custom Agents

- A. Use similarity scoring to retrieve candidate passages
- B. Deduplicate near-identical retrieved chunks
- C. Rerank retrieved passages before generation
- D. Preserve source and chunk identifiers through the pipeline

### 98. A team needs managed search with relevance tuning over enterprise documents. What should it evaluate?

Domain: Developing Custom Agents

- A. Store embeddings in a managed vector index
- B. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- C. Connect approved enterprise content through Agent Search
- D. Use RAG Engine for managed retrieval pipeline components

### 99. A retrieval filter uses user-editable metadata to enforce access. Why is this unsafe?

Domain: Developing Custom Agents

- A. Apply purpose limitation and consent to personal data
- B. Filter retrieval by the requesting user's authorization
- C. Constrain access with a principal access boundary policy
- D. Filter retrieval using trusted metadata

### 100. Embedding generation for a large corpus is expensive to repeat. What should the design include?

Domain: Developing Custom Agents

- A. Use Cloud Storage for large artifacts and source documents
- B. Use Memorystore for Redis for fast shared ephemeral state
- C. Use RAG Engine for managed retrieval pipeline components
- D. Store embeddings in a managed vector index

---

## Answer key and explanations

### Question 1 — D

Answer: Use a large model for complex reasoning or broad language work. A large model is the natural candidate for complex reasoning, subject to cost and evaluation. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: A large model is the natural candidate for complex reasoning, subject to cost and evaluation.
- **B:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: A large model is the natural candidate for complex reasoning, subject to cost and evaluation.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: A large model is the natural candidate for complex reasoning, subject to cost and evaluation.
- **D:** Correct. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: A large model is the natural candidate for complex reasoning, subject to cost and evaluation.

### Question 2 — B

Answer: Use a smaller model for a narrow, high-volume task. A smaller model can meet narrow, high-volume needs if evaluation confirms sufficient quality. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: A smaller model can meet narrow, high-volume needs if evaluation confirms sufficient quality.
- **B:** Correct. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: A smaller model can meet narrow, high-volume needs if evaluation confirms sufficient quality.
- **C:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: A smaller model can meet narrow, high-volume needs if evaluation confirms sufficient quality.
- **D:** Incorrect for this question. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: A smaller model can meet narrow, high-volume needs if evaluation confirms sufficient quality.

### Question 3 — B

Answer: Compare total cost per successful task. Compare total cost per successful task, including retries and review. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: Compare total cost per successful task, including retries and review.
- **B:** Correct. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. In this case: Compare total cost per successful task, including retries and review.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Compare total cost per successful task, including retries and review.
- **D:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Compare total cost per successful task, including retries and review.

### Question 4 — B

Answer: Set an end-to-end latency budget. An end-to-end latency budget that allocates time across every step. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: An end-to-end latency budget that allocates time across every step.
- **B:** Correct. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: An end-to-end latency budget that allocates time across every step.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: An end-to-end latency budget that allocates time across every step.
- **D:** Incorrect for this question. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: An end-to-end latency budget that allocates time across every step.

### Question 5 — B

Answer: Host the model on infrastructure you control. A self-hosted or otherwise approved in-boundary deployment that meets the requirement. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: A self-hosted or otherwise approved in-boundary deployment that meets the requirement.
- **B:** Correct. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: A self-hosted or otherwise approved in-boundary deployment that meets the requirement.
- **C:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: A self-hosted or otherwise approved in-boundary deployment that meets the requirement.
- **D:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: A self-hosted or otherwise approved in-boundary deployment that meets the requirement.

### Question 6 — C

Answer: Use a managed model service under the applicable terms. A managed model service reduces infrastructure and scaling work. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: A managed model service reduces infrastructure and scaling work.
- **B:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: A managed model service reduces infrastructure and scaling work.
- **C:** Correct. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: A managed model service reduces infrastructure and scaling work.
- **D:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: A managed model service reduces infrastructure and scaling work.

### Question 7 — D

Answer: Use a tuned model where specialized behavior justifies it. Tuning can help a well-defined pattern, but it still requires evaluation and held-out data. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Tuning can help a well-defined pattern, but it still requires evaluation and held-out data.
- **B:** Incorrect for this question. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Tuning can help a well-defined pattern, but it still requires evaluation and held-out data.
- **C:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: Tuning can help a well-defined pattern, but it still requires evaluation and held-out data.
- **D:** Correct. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Tuning can help a well-defined pattern, but it still requires evaluation and held-out data.

### Question 8 — A

Answer: Use an open model where portability and control matter. An open model may support the required control, subject to licensing and operational capacity. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: An open model may support the required control, subject to licensing and operational capacity.
- **B:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: An open model may support the required control, subject to licensing and operational capacity.
- **C:** Incorrect for this question. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: An open model may support the required control, subject to licensing and operational capacity.
- **D:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: An open model may support the required control, subject to licensing and operational capacity.

### Question 9 — C

Answer: Use a proprietary model where supported capability matters. Capability and integration benefits come with lifecycle and data-handling dependencies. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: Capability and integration benefits come with lifecycle and data-handling dependencies.
- **B:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: Capability and integration benefits come with lifecycle and data-handling dependencies.
- **C:** Correct. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: Capability and integration benefits come with lifecycle and data-handling dependencies.
- **D:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Capability and integration benefits come with lifecycle and data-handling dependencies.

### Question 10 — B

Answer: Select and deploy supported models through Model Garden. A model catalog or Model Garden can support evaluation across supported options. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A model catalog or Model Garden can support evaluation across supported options.
- **B:** Correct. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: A model catalog or Model Garden can support evaluation across supported options.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A model catalog or Model Garden can support evaluation across supported options.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: A model catalog or Model Garden can support evaluation across supported options.

### Question 11 — C

Answer: Build the agent with the Agent Development Kit. The Agent Development Kit supports programmatic agent construction and orchestration. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. In this case: The Agent Development Kit supports programmatic agent construction and orchestration.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: The Agent Development Kit supports programmatic agent construction and orchestration.
- **C:** Correct. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. In this case: The Agent Development Kit supports programmatic agent construction and orchestration.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: The Agent Development Kit supports programmatic agent construction and orchestration.

### Question 12 — C

Answer: Define an LLM-backed agent with instructions and scoped tools. An LLM-backed agent with instructions and a narrow set of tools. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: An LLM-backed agent with instructions and a narrow set of tools.
- **B:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: An LLM-backed agent with instructions and a narrow set of tools.
- **C:** Correct. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. In this case: An LLM-backed agent with instructions and a narrow set of tools.
- **D:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: An LLM-backed agent with instructions and a narrow set of tools.

### Question 13 — B

Answer: Expose a typed function as a tool. Return a structured error describing the expected format so the agent can recover. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Return a structured error describing the expected format so the agent can recover.
- **B:** Correct. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Return a structured error describing the expected format so the agent can recover.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Return a structured error describing the expected format so the agent can recover.
- **D:** Incorrect for this question. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: Return a structured error describing the expected format so the agent can recover.

### Question 14 — A

Answer: Define a narrow tool schema with a clear description. The tool surface is too permissive; expose constrained operations with validated parameters. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: The tool surface is too permissive; expose constrained operations with validated parameters.
- **B:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: The tool surface is too permissive; expose constrained operations with validated parameters.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: The tool surface is too permissive; expose constrained operations with validated parameters.
- **D:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: The tool surface is too permissive; expose constrained operations with validated parameters.

### Question 15 — A

Answer: Return structured tool errors that guide recovery. Apply a bounded retry with backoff and surface a clear error if it persists. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Apply a bounded retry with backoff and surface a clear error if it persists.
- **B:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Apply a bounded retry with backoff and surface a clear error if it persists.
- **C:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Apply a bounded retry with backoff and surface a clear error if it persists.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Apply a bounded retry with backoff and surface a clear error if it persists.

### Question 16 — D

Answer: Use callbacks for validation, logging, or guardrails. In the tool boundary or callback before the content enters model context. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: In the tool boundary or callback before the content enters model context.
- **B:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: In the tool boundary or callback before the content enters model context.
- **C:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: In the tool boundary or callback before the content enters model context.
- **D:** Correct. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. In this case: In the tool boundary or callback before the content enters model context.

### Question 17 — B

Answer: Run agents in a fixed sequence. A sequential pipeline enforces the dependency order. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A sequential pipeline enforces the dependency order.
- **B:** Correct. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A sequential pipeline enforces the dependency order.
- **C:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A sequential pipeline enforces the dependency order.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A sequential pipeline enforces the dependency order.

### Question 18 — C

Answer: Run independent agents concurrently. Run the independent queries in parallel, then join results for synthesis. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Run the independent queries in parallel, then join results for synthesis.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Run the independent queries in parallel, then join results for synthesis.
- **C:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Run the independent queries in parallel, then join results for synthesis.
- **D:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Run the independent queries in parallel, then join results for synthesis.

### Question 19 — D

Answer: Repeat work until a defined stop condition is met. A stop condition, maximum attempts, and a failure path. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A stop condition, maximum attempts, and a failure path.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A stop condition, maximum attempts, and a failure path.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A stop condition, maximum attempts, and a failure path.
- **D:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A stop condition, maximum attempts, and a failure path.

### Question 20 — B

Answer: Use a graph workflow for branching dependencies. A graph workflow represents branching and joins explicitly. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: A graph workflow represents branching and joins explicitly.
- **B:** Correct. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A graph workflow represents branching and joins explicitly.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A graph workflow represents branching and joins explicitly.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A graph workflow represents branching and joins explicitly.

### Question 21 — D

Answer: Persist conversation and task state in a session. Session-scoped state with a defined lifetime and access policy. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Session-scoped state with a defined lifetime and access policy.
- **B:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Session-scoped state with a defined lifetime and access policy.
- **C:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Session-scoped state with a defined lifetime and access policy.
- **D:** Correct. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Session-scoped state with a defined lifetime and access policy.

### Question 22 — B

Answer: Store durable user or domain memory in Memory Bank. Durable memory with consent, retention, and correction controls. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Durable memory with consent, retention, and correction controls.
- **B:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Durable memory with consent, retention, and correction controls.
- **C:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Durable memory with consent, retention, and correction controls.
- **D:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Durable memory with consent, retention, and correction controls.

### Question 23 — C

Answer: Store task-scoped state deliberately. State bloat can crowd context and retain unnecessary sensitive data. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: State bloat can crowd context and retain unnecessary sensitive data.
- **B:** Incorrect for this question. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: State bloat can crowd context and retain unnecessary sensitive data.
- **C:** Correct. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: State bloat can crowd context and retain unnecessary sensitive data.
- **D:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: State bloat can crowd context and retain unnecessary sensitive data.

### Question 24 — C

Answer: Define what may be remembered, for how long, and why. What may be stored, why, for how long, and how it can be deleted. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: What may be stored, why, for how long, and how it can be deleted.
- **B:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: What may be stored, why, for how long, and how it can be deleted.
- **C:** Correct. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: What may be stored, why, for how long, and how it can be deleted.
- **D:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: What may be stored, why, for how long, and how it can be deleted.

### Question 25 — A

Answer: Pass files and large outputs as artifacts. Store the report as an artifact and pass a reference. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Store the report as an artifact and pass a reference.
- **B:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Store the report as an artifact and pass a reference.
- **C:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Store the report as an artifact and pass a reference.
- **D:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Store the report as an artifact and pass a reference.

### Question 26 — D

Answer: Persist sessions in a durable managed store. A durable managed session store rather than in-process memory. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: A durable managed session store rather than in-process memory.
- **B:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A durable managed session store rather than in-process memory.
- **C:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: A durable managed session store rather than in-process memory.
- **D:** Correct. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A durable managed session store rather than in-process memory.

### Question 27 — A

Answer: Store durable user or domain memory in Memory Bank. A managed long-term memory service with explicit memory policy. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: A managed long-term memory service with explicit memory policy.
- **B:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: A managed long-term memory service with explicit memory policy.
- **C:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: A managed long-term memory service with explicit memory policy.
- **D:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: A managed long-term memory service with explicit memory policy.

### Question 28 — D

Answer: Store task-scoped state deliberately. Cross-user state leakage; state must be partitioned by session and identity. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Cross-user state leakage; state must be partitioned by session and identity.
- **B:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Cross-user state leakage; state must be partitioned by session and identity.
- **C:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Cross-user state leakage; state must be partitioned by session and identity.
- **D:** Correct. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Cross-user state leakage; state must be partitioned by session and identity.

### Question 29 — A

Answer: Define what may be remembered, for how long, and why. Inspection, correction, and deletion under the applicable memory policy. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: Inspection, correction, and deletion under the applicable memory policy.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Inspection, correction, and deletion under the applicable memory policy.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Inspection, correction, and deletion under the applicable memory policy.
- **D:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Inspection, correction, and deletion under the applicable memory policy.

### Question 30 — A

Answer: Fit retrieved evidence within the model's usable context. Summarize verified current state and discard superseded details under policy. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: Summarize verified current state and discard superseded details under policy.
- **B:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Summarize verified current state and discard superseded details under policy.
- **C:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Summarize verified current state and discard superseded details under policy.
- **D:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Summarize verified current state and discard superseded details under policy.

### Question 31 — D

Answer: Choose chunk size and overlap for retrieval. Chunking strategy that respects document structure and expected query granularity. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Chunking strategy that respects document structure and expected query granularity.
- **B:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Chunking strategy that respects document structure and expected query granularity.
- **C:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Chunking strategy that respects document structure and expected query granularity.
- **D:** Correct. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Chunking strategy that respects document structure and expected query granularity.

### Question 32 — C

Answer: Choose an embedding model suited to the domain and language. An embedding model suited to the domain, or hybrid retrieval that includes exact terms. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: An embedding model suited to the domain, or hybrid retrieval that includes exact terms.
- **B:** Incorrect for this question. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: An embedding model suited to the domain, or hybrid retrieval that includes exact terms.
- **C:** Correct. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: An embedding model suited to the domain, or hybrid retrieval that includes exact terms.
- **D:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: An embedding model suited to the domain, or hybrid retrieval that includes exact terms.

### Question 33 — A

Answer: Rerank retrieved passages before generation. Rerank the candidates against the query using a stronger relevance model. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Rerank the candidates against the query using a stronger relevance model.
- **B:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Rerank the candidates against the query using a stronger relevance model.
- **C:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Rerank the candidates against the query using a stronger relevance model.
- **D:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Rerank the candidates against the query using a stronger relevance model.

### Question 34 — B

Answer: Combine keyword and semantic retrieval. Combine exact-term and semantic retrieval so identifiers and paraphrased concepts are both covered. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Combine exact-term and semantic retrieval so identifiers and paraphrased concepts are both covered.
- **B:** Correct. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Combine exact-term and semantic retrieval so identifiers and paraphrased concepts are both covered.
- **C:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Combine exact-term and semantic retrieval so identifiers and paraphrased concepts are both covered.
- **D:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Combine exact-term and semantic retrieval so identifiers and paraphrased concepts are both covered.

### Question 35 — C

Answer: Filter retrieval using trusted metadata. Trusted metadata filters for region and effective date. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Trusted metadata filters for region and effective date.
- **B:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Trusted metadata filters for region and effective date.
- **C:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Trusted metadata filters for region and effective date.
- **D:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Trusted metadata filters for region and effective date.

### Question 36 — A

Answer: Deduplicate near-identical retrieved chunks. Deduplicate near-identical chunks before ranking so repeated boilerplate does not dominate the evidence. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Deduplicate near-identical chunks before ranking so repeated boilerplate does not dominate the evidence.
- **B:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Deduplicate near-identical chunks before ranking so repeated boilerplate does not dominate the evidence.
- **C:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Deduplicate near-identical chunks before ranking so repeated boilerplate does not dominate the evidence.
- **D:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Deduplicate near-identical chunks before ranking so repeated boilerplate does not dominate the evidence.

### Question 37 — A

Answer: Ground the response in cited retrieved evidence. Require claim-level grounding with retrievable chunk identifiers. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Require claim-level grounding with retrievable chunk identifiers.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Require claim-level grounding with retrievable chunk identifiers.
- **C:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Require claim-level grounding with retrievable chunk identifiers.
- **D:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Require claim-level grounding with retrievable chunk identifiers.

### Question 38 — A

Answer: Preserve source and chunk identifiers through the pipeline. Stable source and chunk identifiers through retrieval and generation. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Stable source and chunk identifiers through retrieval and generation.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Stable source and chunk identifiers through retrieval and generation.
- **C:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Stable source and chunk identifiers through retrieval and generation.
- **D:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Stable source and chunk identifiers through retrieval and generation.

### Question 39 — D

Answer: Fit retrieved evidence within the model's usable context. Select and order the most relevant evidence within the context budget. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Select and order the most relevant evidence within the context budget.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Select and order the most relevant evidence within the context budget.
- **C:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Select and order the most relevant evidence within the context budget.
- **D:** Correct. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: Select and order the most relevant evidence within the context budget.

### Question 40 — C

Answer: Check index freshness and reindexing behavior. Index updates and deletion propagation for the source system. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Index updates and deletion propagation for the source system.
- **B:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Index updates and deletion propagation for the source system.
- **C:** Correct. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Index updates and deletion propagation for the source system.
- **D:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Index updates and deletion propagation for the source system.

### Question 41 — C

Answer: Store embeddings in a managed vector index. A managed vector search service appropriate to the corpus and access model. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: A managed vector search service appropriate to the corpus and access model.
- **B:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: A managed vector search service appropriate to the corpus and access model.
- **C:** Correct. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: A managed vector search service appropriate to the corpus and access model.
- **D:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: A managed vector search service appropriate to the corpus and access model.

### Question 42 — C

Answer: Use RAG Engine for managed retrieval pipeline components. RAG Engine for supported managed retrieval pipeline components. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: RAG Engine for supported managed retrieval pipeline components.
- **B:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: RAG Engine for supported managed retrieval pipeline components.
- **C:** Correct. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: RAG Engine for supported managed retrieval pipeline components.
- **D:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: RAG Engine for supported managed retrieval pipeline components.

### Question 43 — B

Answer: Use Agent Retrieval and Vector Search for agent-oriented retrieval. Agent Retrieval and Vector Search for agent-oriented retrieval. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Agent Retrieval and Vector Search for agent-oriented retrieval.
- **B:** Correct. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: Agent Retrieval and Vector Search for agent-oriented retrieval.
- **C:** Incorrect for this question. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Agent Retrieval and Vector Search for agent-oriented retrieval.
- **D:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Agent Retrieval and Vector Search for agent-oriented retrieval.

### Question 44 — B

Answer: Connect approved enterprise content through Agent Search. Agent Search for managed enterprise content search. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: Agent Search for managed enterprise content search.
- **B:** Correct. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Agent Search for managed enterprise content search.
- **C:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Agent Search for managed enterprise content search.
- **D:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Agent Search for managed enterprise content search.

### Question 45 — D

Answer: Filter retrieval by the requesting user's authorization. Authorization filtering must remove inaccessible content before it enters the model context. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. In this case: Authorization filtering must remove inaccessible content before it enters the model context.
- **B:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Authorization filtering must remove inaccessible content before it enters the model context.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Authorization filtering must remove inaccessible content before it enters the model context.
- **D:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Authorization filtering must remove inaccessible content before it enters the model context.

### Question 46 — D

Answer: Limit connected sources to the approved audience and purpose. Limit the indexed corpus and access scope to the department's approved content. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Limit the indexed corpus and access scope to the department's approved content.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Limit the indexed corpus and access scope to the department's approved content.
- **C:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Limit the indexed corpus and access scope to the department's approved content.
- **D:** Correct. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. In this case: Limit the indexed corpus and access scope to the department's approved content.

### Question 47 — A

Answer: Filter retrieval using trusted metadata. Exclude unlabeled chunks from cross-tenant retrieval until metadata is corrected. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Exclude unlabeled chunks from cross-tenant retrieval until metadata is corrected.
- **B:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Exclude unlabeled chunks from cross-tenant retrieval until metadata is corrected.
- **C:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Exclude unlabeled chunks from cross-tenant retrieval until metadata is corrected.
- **D:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Exclude unlabeled chunks from cross-tenant retrieval until metadata is corrected.

### Question 48 — B

Answer: Preserve source and chunk identifiers through the pipeline. Provenance was lost; preserve identifiers and source references through the pipeline. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Provenance was lost; preserve identifiers and source references through the pipeline.
- **B:** Correct. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Provenance was lost; preserve identifiers and source references through the pipeline.
- **C:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Provenance was lost; preserve identifiers and source references through the pipeline.
- **D:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Provenance was lost; preserve identifiers and source references through the pipeline.

### Question 49 — A

Answer: Check index freshness and reindexing behavior. Reindexing frequency and freshness requirements for the use case. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Reindexing frequency and freshness requirements for the use case.
- **B:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: Reindexing frequency and freshness requirements for the use case.
- **C:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Reindexing frequency and freshness requirements for the use case.
- **D:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Reindexing frequency and freshness requirements for the use case.

### Question 50 — C

Answer: Deduplicate near-identical retrieved chunks. Deduplication and reranking so diverse relevant evidence is preserved. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Deduplication and reranking so diverse relevant evidence is preserved.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Deduplication and reranking so diverse relevant evidence is preserved.
- **C:** Correct. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Deduplication and reranking so diverse relevant evidence is preserved.
- **D:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Deduplication and reranking so diverse relevant evidence is preserved.

### Question 51 — D

Answer: Use a large model for complex reasoning or broad language work. Multimodal extraction quality on representative scans before considering cost. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Multimodal extraction quality on representative scans before considering cost.
- **B:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: Multimodal extraction quality on representative scans before considering cost.
- **C:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Multimodal extraction quality on representative scans before considering cost.
- **D:** Correct. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Multimodal extraction quality on representative scans before considering cost.

### Question 52 — B

Answer: Use a smaller model for a narrow, high-volume task. Measured accuracy and latency on representative utterances. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: Measured accuracy and latency on representative utterances.
- **B:** Correct. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Measured accuracy and latency on representative utterances.
- **C:** Incorrect for this question. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Measured accuracy and latency on representative utterances.
- **D:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Measured accuracy and latency on representative utterances.

### Question 53 — B

Answer: Select and deploy supported models through Model Garden. An abstraction and fallback path with evaluated alternative models. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: An abstraction and fallback path with evaluated alternative models.
- **B:** Correct. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: An abstraction and fallback path with evaluated alternative models.
- **C:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: An abstraction and fallback path with evaluated alternative models.
- **D:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: An abstraction and fallback path with evaluated alternative models.

### Question 54 — C

Answer: Compare total cost per successful task. Cost per successful task, including retries and human review. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Cost per successful task, including retries and human review.
- **B:** Incorrect for this question. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Cost per successful task, including retries and human review.
- **C:** Correct. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. In this case: Cost per successful task, including retries and human review.
- **D:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Cost per successful task, including retries and human review.

### Question 55 — C

Answer: Use an open model where portability and control matter. Whether training and hosting occur within an approved boundary. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: Whether training and hosting occur within an approved boundary.
- **B:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: Whether training and hosting occur within an approved boundary.
- **C:** Correct. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: Whether training and hosting occur within an approved boundary.
- **D:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: Whether training and hosting occur within an approved boundary.

### Question 56 — D

Answer: Set an end-to-end latency budget. Cumulative latency across retrieval, tools, and every model turn. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Cumulative latency across retrieval, tools, and every model turn.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Cumulative latency across retrieval, tools, and every model turn.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Cumulative latency across retrieval, tools, and every model turn.
- **D:** Correct. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Cumulative latency across retrieval, tools, and every model turn.

### Question 57 — A

Answer: Use a tuned model where specialized behavior justifies it. Tuning on representative examples when the knowledge is a stable style or pattern. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Tuning on representative examples when the knowledge is a stable style or pattern.
- **B:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Tuning on representative examples when the knowledge is a stable style or pattern.
- **C:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Tuning on representative examples when the knowledge is a stable style or pattern.
- **D:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: Tuning on representative examples when the knowledge is a stable style or pattern.

### Question 58 — A

Answer: Use a proprietary model where supported capability matters. A tested replacement path and version pinning with migration checks. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: A tested replacement path and version pinning with migration checks.
- **B:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: A tested replacement path and version pinning with migration checks.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: A tested replacement path and version pinning with migration checks.
- **D:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: A tested replacement path and version pinning with migration checks.

### Question 59 — B

Answer: Select and deploy supported models through Model Garden. A model catalog entry with owner, version, and evaluation status. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A model catalog entry with owner, version, and evaluation status.
- **B:** Correct. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: A model catalog entry with owner, version, and evaluation status.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: A model catalog entry with owner, version, and evaluation status.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A model catalog entry with owner, version, and evaluation status.

### Question 60 — B

Answer: Use a large model for complex reasoning or broad language work. Send simple cases to a smaller model and escalate uncertain ones. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Send simple cases to a smaller model and escalate uncertain ones.
- **B:** Correct. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Send simple cases to a smaller model and escalate uncertain ones.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Send simple cases to a smaller model and escalate uncertain ones.
- **D:** Incorrect for this question. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. In this case: Send simple cases to a smaller model and escalate uncertain ones.

### Question 61 — D

Answer: Build the agent with the Agent Development Kit. The Agent Development Kit with tool definitions and callbacks. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: The Agent Development Kit with tool definitions and callbacks.
- **B:** Incorrect for this question. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. In this case: The Agent Development Kit with tool definitions and callbacks.
- **C:** Incorrect for this question. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. In this case: The Agent Development Kit with tool definitions and callbacks.
- **D:** Correct. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. In this case: The Agent Development Kit with tool definitions and callbacks.

### Question 62 — B

Answer: Expose a typed function as a tool. Return a defined structured schema instead of free text. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: Return a defined structured schema instead of free text.
- **B:** Correct. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Return a defined structured schema instead of free text.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Return a defined structured schema instead of free text.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Return a defined structured schema instead of free text.

### Question 63 — C

Answer: Use callbacks for validation, logging, or guardrails. In a model callback or platform logging layer with redaction. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: In a model callback or platform logging layer with redaction.
- **B:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: In a model callback or platform logging layer with redaction.
- **C:** Correct. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. In this case: In a model callback or platform logging layer with redaction.
- **D:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: In a model callback or platform logging layer with redaction.

### Question 64 — D

Answer: Run agents in a fixed sequence. A sequential workflow agent enforces the fixed two-step order without extra orchestration. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A sequential workflow agent enforces the fixed two-step order without extra orchestration.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A sequential workflow agent enforces the fixed two-step order without extra orchestration.
- **C:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A sequential workflow agent enforces the fixed two-step order without extra orchestration.
- **D:** Correct. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A sequential workflow agent enforces the fixed two-step order without extra orchestration.

### Question 65 — C

Answer: Run independent agents concurrently. A parallel workflow agent with a later aggregation step. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A parallel workflow agent with a later aggregation step.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A parallel workflow agent with a later aggregation step.
- **C:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A parallel workflow agent with a later aggregation step.
- **D:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A parallel workflow agent with a later aggregation step.

### Question 66 — A

Answer: Repeat work until a defined stop condition is met. A loop with a maximum iteration count and failure path. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A loop with a maximum iteration count and failure path.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A loop with a maximum iteration count and failure path.
- **C:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A loop with a maximum iteration count and failure path.
- **D:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A loop with a maximum iteration count and failure path.

### Question 67 — A

Answer: Define an LLM-backed agent with instructions and scoped tools. A coordinator agent that routes to the appropriate specialist. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. In this case: A coordinator agent that routes to the appropriate specialist.
- **B:** Incorrect for this question. A subagent can isolate context and permissions for a focused job. Clear ownership, tool scope, and returned evidence are still required. In this case: A coordinator agent that routes to the appropriate specialist.
- **C:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: A coordinator agent that routes to the appropriate specialist.
- **D:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: A coordinator agent that routes to the appropriate specialist.

### Question 68 — A

Answer: Expose a typed function as a tool. A policy check and approval requirement before execution. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: A policy check and approval requirement before execution.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: A policy check and approval requirement before execution.
- **C:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: A policy check and approval requirement before execution.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: A policy check and approval requirement before execution.

### Question 69 — D

Answer: Return structured tool errors that guide recovery. Retry with backoff within a bound and report exhaustion. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Retry with backoff within a bound and report exhaustion.
- **B:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Retry with backoff within a bound and report exhaustion.
- **C:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Retry with backoff within a bound and report exhaustion.
- **D:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Retry with backoff within a bound and report exhaustion.

### Question 70 — C

Answer: Use callbacks for validation, logging, or guardrails. Session or state storage with a defined schema. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Session or state storage with a defined schema.
- **B:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Session or state storage with a defined schema.
- **C:** Correct. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. In this case: Session or state storage with a defined schema.
- **D:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Session or state storage with a defined schema.

### Question 71 — A

Answer: Store durable user or domain memory in Memory Bank. Which categories may persist and which must be excluded. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Which categories may persist and which must be excluded.
- **B:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Which categories may persist and which must be excluded.
- **C:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Which categories may persist and which must be excluded.
- **D:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Which categories may persist and which must be excluded.

### Question 72 — D

Answer: Store task-scoped state deliberately. Store references and selected evidence rather than full corpora. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: Store references and selected evidence rather than full corpora.
- **B:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Store references and selected evidence rather than full corpora.
- **C:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Store references and selected evidence rather than full corpora.
- **D:** Correct. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Store references and selected evidence rather than full corpora.

### Question 73 — D

Answer: Define what may be remembered, for how long, and why. Stop using and delete affected memory under the retention policy. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Stop using and delete affected memory under the retention policy.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Stop using and delete affected memory under the retention policy.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Stop using and delete affected memory under the retention policy.
- **D:** Correct. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: Stop using and delete affected memory under the retention policy.

### Question 74 — A

Answer: Store durable user or domain memory in Memory Bank. Memory stores user-specific state; retrieval supplies source evidence. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Memory stores user-specific state; retrieval supplies source evidence.
- **B:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Memory stores user-specific state; retrieval supplies source evidence.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Memory stores user-specific state; retrieval supplies source evidence.
- **D:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Memory stores user-specific state; retrieval supplies source evidence.

### Question 75 — B

Answer: Persist conversation and task state in a session. A shared external session store with concurrency controls. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: A shared external session store with concurrency controls.
- **B:** Correct. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: A shared external session store with concurrency controls.
- **C:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A shared external session store with concurrency controls.
- **D:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A shared external session store with concurrency controls.

### Question 76 — B

Answer: Pass files and large outputs as artifacts. An artifact reference rather than embedding the file in the prompt. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: An artifact reference rather than embedding the file in the prompt.
- **B:** Correct. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: An artifact reference rather than embedding the file in the prompt.
- **C:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: An artifact reference rather than embedding the file in the prompt.
- **D:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: An artifact reference rather than embedding the file in the prompt.

### Question 77 — B

Answer: Store durable user or domain memory in Memory Bank. Correction and supersession with an audit trail. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Correction and supersession with an audit trail.
- **B:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Correction and supersession with an audit trail.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Correction and supersession with an audit trail.
- **D:** Incorrect for this question. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: Correction and supersession with an audit trail.

### Question 78 — C

Answer: Persist conversation and task state in a session. Summarize verified current state and continue with selected context. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Summarize verified current state and continue with selected context.
- **B:** Incorrect for this question. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: Summarize verified current state and continue with selected context.
- **C:** Correct. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Summarize verified current state and continue with selected context.
- **D:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Summarize verified current state and continue with selected context.

### Question 79 — A

Answer: Store task-scoped state deliberately. Cross-tenant session access; identifiers and authorization must be robust. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Cross-tenant session access; identifiers and authorization must be robust.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Cross-tenant session access; identifiers and authorization must be robust.
- **C:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Cross-tenant session access; identifiers and authorization must be robust.
- **D:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Cross-tenant session access; identifiers and authorization must be robust.

### Question 80 — D

Answer: Store durable user or domain memory in Memory Bank. A managed memory service with explicit retention controls. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A managed memory service with explicit retention controls.
- **B:** Incorrect for this question. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: A managed memory service with explicit retention controls.
- **C:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: A managed memory service with explicit retention controls.
- **D:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: A managed memory service with explicit retention controls.

### Question 81 — B

Answer: Choose chunk size and overlap for retrieval. Overlap and section boundaries that preserve the complete answer. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Overlap and section boundaries that preserve the complete answer.
- **B:** Correct. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Overlap and section boundaries that preserve the complete answer.
- **C:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Overlap and section boundaries that preserve the complete answer.
- **D:** Incorrect for this question. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Overlap and section boundaries that preserve the complete answer.

### Question 82 — D

Answer: Rerank retrieved passages before generation. Rerank and select the most relevant candidates for the context. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Rerank and select the most relevant candidates for the context.
- **B:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Rerank and select the most relevant candidates for the context.
- **C:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Rerank and select the most relevant candidates for the context.
- **D:** Correct. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Rerank and select the most relevant candidates for the context.

### Question 83 — C

Answer: Filter retrieval using trusted metadata. A trusted status field to exclude drafts from answers. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: A trusted status field to exclude drafts from answers.
- **B:** Incorrect for this question. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: A trusted status field to exclude drafts from answers.
- **C:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: A trusted status field to exclude drafts from answers.
- **D:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: A trusted status field to exclude drafts from answers.

### Question 84 — A

Answer: Combine keyword and semantic retrieval. Keyword matching for identifiers and semantic retrieval for concepts. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Keyword matching for identifiers and semantic retrieval for concepts.
- **B:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Keyword matching for identifiers and semantic retrieval for concepts.
- **C:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Keyword matching for identifiers and semantic retrieval for concepts.
- **D:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Keyword matching for identifiers and semantic retrieval for concepts.

### Question 85 — C

Answer: Ground the response in cited retrieved evidence. Citations for each material claim, tied to the supporting chunks. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Citations for each material claim, tied to the supporting chunks.
- **B:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Citations for each material claim, tied to the supporting chunks.
- **C:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Citations for each material claim, tied to the supporting chunks.
- **D:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Citations for each material claim, tied to the supporting chunks.

### Question 86 — D

Answer: Choose chunk size and overlap for retrieval. Preserve table structure and split on logical boundaries. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Preserve table structure and split on logical boundaries.
- **B:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Preserve table structure and split on logical boundaries.
- **C:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Preserve table structure and split on logical boundaries.
- **D:** Correct. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Preserve table structure and split on logical boundaries.

### Question 87 — B

Answer: Check index freshness and reindexing behavior. Effective-date and status filtering with current-version preference. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Effective-date and status filtering with current-version preference.
- **B:** Correct. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Effective-date and status filtering with current-version preference.
- **C:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Effective-date and status filtering with current-version preference.
- **D:** Incorrect for this question. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Effective-date and status filtering with current-version preference.

### Question 88 — A

Answer: Rerank retrieved passages before generation. Clarify the intent or retrieve with a disambiguated query. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Clarify the intent or retrieve with a disambiguated query.
- **B:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Clarify the intent or retrieve with a disambiguated query.
- **C:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Clarify the intent or retrieve with a disambiguated query.
- **D:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Clarify the intent or retrieve with a disambiguated query.

### Question 89 — D

Answer: Choose an embedding model suited to the domain and language. Embedding and retrieval quality per language, not only in aggregate. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Embedding and retrieval quality per language, not only in aggregate.
- **B:** Incorrect for this question. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Embedding and retrieval quality per language, not only in aggregate.
- **C:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Embedding and retrieval quality per language, not only in aggregate.
- **D:** Correct. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Embedding and retrieval quality per language, not only in aggregate.

### Question 90 — C

Answer: Fit retrieved evidence within the model's usable context. Surface the conflict and cite both sources rather than choose silently. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Surface the conflict and cite both sources rather than choose silently.
- **B:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Surface the conflict and cite both sources rather than choose silently.
- **C:** Correct. More retrieved text is not always better. Select and order evidence to preserve the facts needed for the task. In this case: Surface the conflict and cite both sources rather than choose silently.
- **D:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Surface the conflict and cite both sources rather than choose silently.

### Question 91 — C

Answer: Store embeddings in a managed vector index. A full re-embedding and evaluation of retrieval quality before cutover. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: A full re-embedding and evaluation of retrieval quality before cutover.
- **B:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: A full re-embedding and evaluation of retrieval quality before cutover.
- **C:** Correct. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: A full re-embedding and evaluation of retrieval quality before cutover.
- **D:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: A full re-embedding and evaluation of retrieval quality before cutover.

### Question 92 — C

Answer: Use Agent Retrieval and Vector Search for agent-oriented retrieval. A managed retrieval service with the required latency and access controls. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: A managed retrieval service with the required latency and access controls.
- **B:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A managed retrieval service with the required latency and access controls.
- **C:** Correct. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: A managed retrieval service with the required latency and access controls.
- **D:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: A managed retrieval service with the required latency and access controls.

### Question 93 — D

Answer: Filter retrieval by the requesting user's authorization. Add trusted tenant metadata and filter before retrieval results are used. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Add trusted tenant metadata and filter before retrieval results are used.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Add trusted tenant metadata and filter before retrieval results are used.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Add trusted tenant metadata and filter before retrieval results are used.
- **D:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Add trusted tenant metadata and filter before retrieval results are used.

### Question 94 — A

Answer: Use RAG Engine for managed retrieval pipeline components. Capacity and caching while preserving authorization per request. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Capacity and caching while preserving authorization per request.
- **B:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: Capacity and caching while preserving authorization per request.
- **C:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: Capacity and caching while preserving authorization per request.
- **D:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Capacity and caching while preserving authorization per request.

### Question 95 — B

Answer: Store embeddings in a managed vector index. A managed vector or retrieval service. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: A managed vector or retrieval service.
- **B:** Correct. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: A managed vector or retrieval service.
- **C:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: A managed vector or retrieval service.
- **D:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A managed vector or retrieval service.

### Question 96 — A

Answer: Check index freshness and reindexing behavior. Deletion propagation and verification in the indexing pipeline. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Deletion propagation and verification in the indexing pipeline.
- **B:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Deletion propagation and verification in the indexing pipeline.
- **C:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Deletion propagation and verification in the indexing pipeline.
- **D:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Deletion propagation and verification in the indexing pipeline.

### Question 97 — B

Answer: Deduplicate near-identical retrieved chunks. Deduplicate by content identity before ranking. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Deduplicate by content identity before ranking.
- **B:** Correct. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Deduplicate by content identity before ranking.
- **C:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Deduplicate by content identity before ranking.
- **D:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Deduplicate by content identity before ranking.

### Question 98 — C

Answer: Connect approved enterprise content through Agent Search. Agent Search capabilities for the corpus and access model. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Agent Search capabilities for the corpus and access model.
- **B:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: Agent Search capabilities for the corpus and access model.
- **C:** Correct. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Agent Search capabilities for the corpus and access model.
- **D:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Agent Search capabilities for the corpus and access model.

### Question 99 — D

Answer: Filter retrieval using trusted metadata. Access decisions must rely on trusted authorization, not user-controlled labels. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Access decisions must rely on trusted authorization, not user-controlled labels.
- **B:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Access decisions must rely on trusted authorization, not user-controlled labels.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Access decisions must rely on trusted authorization, not user-controlled labels.
- **D:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Access decisions must rely on trusted authorization, not user-controlled labels.

### Question 100 — D

Answer: Store embeddings in a managed vector index. Persistent embeddings with versioning and controlled regeneration. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: Persistent embeddings with versioning and controlled regeneration.
- **B:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: Persistent embeddings with versioning and controlled regeneration.
- **C:** Incorrect for this question. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: Persistent embeddings with versioning and controlled regeneration.
- **D:** Correct. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Persistent embeddings with versioning and controlled regeneration.
