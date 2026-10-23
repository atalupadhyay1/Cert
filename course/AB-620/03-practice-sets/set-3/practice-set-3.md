# Microsoft AB-620 — Full-Length Mock Exam 3

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A treasury team wants live cash positions inside Dataverse so the agent can read them like a native table. Which integration option fits?

Domain: Plan and configure agent solutions

- A. Expose the system through a virtual table or connector view that the agent can read
- B. Call the internal endpoint straight from the topic over HTTP
- C. Copy the records nightly into Dataverse and answer from the copy
- D. Batch the requests and post them to the source system on a schedule

### 2. A developer proposes calling an internal HR endpoint directly from a topic because a gateway seems slow. Which risk belongs in the review?

Domain: Plan and configure agent solutions

- A. Copy the records nightly into Dataverse and answer from the copy
- B. Expose the system through a virtual table or connector view that the agent can read
- C. Call the internal endpoint straight from the topic over HTTP
- D. Mediate the on-premises call through an on-premises data gateway

### 3. An agent must call a payments API that evaluates the signed-in operator's own limits. Which pattern carries the identity?

Domain: Plan and configure agent solutions

- A. Use the on-behalf-of flow so the agent calls the API as the signed-in user
- B. Store one API key in a topic variable and reuse it for every user
- C. Give every conversation a single shared service account credential for the API
- D. Allow anonymous access to the agent and authenticate only at the API

### 4. A vendor proposes one shared API account for every conversation to simplify setup. Which identity control should the design use instead?

Domain: Plan and configure agent solutions

- A. Store one API key in a topic variable and reuse it for every user
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Give every conversation a single shared service account credential for the API
- D. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream

### 5. An agent will read both an internal records API and an Azure AI Search index. Which two identity choices apply? Select two.

Domain: Plan and configure agent solutions

- A. Use the agent managed identity for Azure resources and keep user identity for business data
- B. Give every conversation a single shared service account credential for the API
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- E. Store one API key in a topic variable and reuse it for every user

### 6. A group wants its agent discoverable in the Microsoft 365 Copilot experience used across departments. Which publishing option fits?

Domain: Plan and configure agent solutions

- A. Publish to a public website with authenticated sign-in
- B. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents
- C. Publish to email and answer asynchronously
- D. Publish to Microsoft Teams and keep the agent inside the tenant

### 7. A membership organisation will publish the agent on its public site with member sign-in required. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Embed the agent in a custom application through the Direct Line channel
- C. Add the channel for omni-channel engagement so external support queues can route to it
- D. Publish to a public website with authenticated sign-in

### 8. A logistics firm will embed the agent in a custom dispatch console with its own authentication. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to email and answer asynchronously
- B. Publish to a public website with authenticated sign-in
- C. Embed the agent in a custom application through the Direct Line channel
- D. Publish to Microsoft Teams and keep the agent inside the tenant

### 9. A retrieved supplier document contains a line telling the assistant to forward records to an outside address. Which control addresses this?

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Restrict who can author and publish with Copilot Studio security roles
- C. Separate development and production environments with environment security groups
- D. Constrain the tools the agent may call, validate tool output, and limit autonomous actions

### 10. A dispute requires the exact answer the agent gave three months ago. What makes that possible?

Domain: Plan and configure agent solutions

- A. Separate development and production environments with environment security groups
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Restrict who can author and publish with Copilot Studio security roles
- D. Turn on audit logging and retain agent conversation records

### 11. Three hundred makers can publish to the customer-facing agent today. Which control should be tightened first?

Domain: Plan and configure agent solutions

- A. Separate development and production environments with environment security groups
- B. Turn on audit logging and retain agent conversation records
- C. Restrict who can author and publish with Copilot Studio security roles
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 12. An agent will read internal contracts and answer external partners. Which two controls belong in the design? Select two.

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Enforce the source system’s permissions in the knowledge layer so answers respect access
- D. Separate development and production environments with environment security groups
- E. Constrain the tools the agent may call, validate tool output, and limit autonomous actions

### 13. The same shared topic runs in three regions with different endpoints and no other difference. What should differentiate them?

Domain: Plan and configure agent solutions

- A. Parameterize environment-specific values with environment variables
- B. Copy the topics into each agent so every team can edit its own copy
- C. Extract the shared logic into a reusable component or child agent and reference it
- D. Rebuild the same topic in each agent to avoid a shared dependency

### 14. A shared agent capability must be released to three environments. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- B. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- C. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- D. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream

### 15. A builder needs three connector calls in order, with a value returned to the conversation. What should be created?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Use an automated cloud flow triggered by an event and have the agent wait for it
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Create the flow with the connector action the agent needs and return the result

### 16. A topic calls a flow but receives nothing back even when the flow succeeds. What is missing?

Domain: Plan and configure agent solutions

- A. Add the capability as a connector action so the agent can call it without a flow
- B. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- C. Define typed input and output parameters on the flow and bind them from the topic
- D. Create the flow with the connector action the agent needs and return the result

### 17. A document arrival must trigger enrichment, and the agent should be informed later. Which trigger fits?

Domain: Plan and configure agent solutions

- A. Add the capability as a connector action so the agent can call it without a flow
- B. Create the flow with the connector action the agent needs and return the result
- C. Use an automated cloud flow triggered by an event and have the agent wait for it
- D. Create an agent flow with a manual trigger that the topic calls with inputs

### 18. A flow will be called by a topic that must always reply to the user. Which two features are required? Select two.

Domain: Plan and configure agent solutions

- A. Add the capability as a connector action so the agent can call it without a flow
- B. Create an agent flow with a manual trigger that the topic calls with inputs
- C. Define typed input and output parameters on the flow and bind them from the topic
- D. Use an automated cloud flow triggered by an event and have the agent wait for it
- E. Wrap the calls in a scope with a parallel error branch that returns a structured failure

### 19. A regional manager approves exceptions from a phone in Teams. Which pattern fits best?

Domain: Plan and configure agent solutions

- A. Hand the conversation off to a live agent with the context attached
- B. Send an approval request and pause the flow until a person responds
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Post an adaptive card to Teams and wait for the human decision before continuing

### 20. An approval request sometimes sits unanswered for days and blocks the queue. What should be added?

Domain: Plan and configure agent solutions

- A. Hand the conversation off to a live agent with the context attached
- B. Let the agent complete the action and notify a person afterwards
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Have the agent draft the action and require a person to submit it in the source system

### 21. A flow fails only under load, and the run that failed is no longer visible. What should be enabled?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Send flow telemetry to Application Insights and query the traces
- C. Use the Copilot Studio analytics view for session and topic outcomes
- D. Review the flow run history and its action-level inputs and outputs

### 22. A builder needs the exact input a connector action received on a failed run this morning. Where is that recorded?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Configure an alert on failed runs and route it to the owning team
- C. Use the Copilot Studio analytics view for session and topic outcomes
- D. Review the flow run history and its action-level inputs and outputs

### 23. A connector that creates invoices fails intermittently during month end. Which two controls limit the impact? Select two.

Domain: Plan and configure agent solutions

- A. Configure an alert on failed runs and route it to the owning team
- B. Add a comment step to the flow describing the expected failure
- C. Configure a retry policy and terminate with a failure code the topic can read
- D. Use the Copilot Studio analytics view for session and topic outcomes
- E. Review the flow run history and its action-level inputs and outputs

### 24. A reference number from a completed topic keeps appearing in a new conversation on the same session. What should change?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Store the value in a global variable so later topics can read it

### 25. A summary needs four labelled values and a confirm action. What should the topic return?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Configure the message node to send a formatted message with the fields the user needs
- C. Return the raw flow output as plain text
- D. Return an adaptive card so the data renders in labelled fields

### 26. A long conversation spans six topics that need the same customer context. Which two variable choices fit? Select two.

Domain: Plan and configure agent solutions

- A. Configure the message node to send a formatted message with the fields the user needs
- B. Configure the topic as a redirect target with its own trigger phrases
- C. Store the value in a global variable so later topics can read it
- D. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- E. Return the raw flow output as plain text

### 27. An agent is accurate but answers in bullet lists when adjusters need a short paragraph. What should be configured?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Add a fallback topic for low-confidence answers that hands off to a person
- D. Require the answer to cite retrieved passages and refuse when none are found

### 28. A compliance lead wants proof that every answer came from approved material. Which configuration satisfies that?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Require the answer to cite retrieved passages and refuse when none are found
- D. Add a fallback topic for low-confidence answers that hands off to a person

### 29. A standards library sits in SharePoint with per-site permissions that must keep applying. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Add the SharePoint site as a knowledge source and rely on item-level permissions
- C. Upload the documents as file knowledge on the agent
- D. Register the database as a knowledge source so the agent can query it directly

### 30. A parts catalogue lives in a database and the agent must look up a single part on request. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the source through a Copilot connector so its content is indexed for answers
- B. Connect through a Power Platform connector and query it from a tool or flow
- C. Register the database as a knowledge source so the agent can query it directly
- D. Upload the documents as file knowledge on the agent

### 31. A team is connecting a document estate and an operational system to one agent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect and scope the knowledge → choose the connector or index for each → inventory the sources and their permissions → test answers with users of different access → review unsupported questions
- B. Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions
- C. Test answers with users of different access → inventory the sources and their permissions → choose the connector or index for each → review unsupported questions → connect and scope the knowledge
- D. Review unsupported questions → test answers with users of different access → connect and scope the knowledge → inventory the sources and their permissions → choose the connector or index for each

### 32. A compliance team compares two knowledge options for 200,000 documents. Which two statements are correct? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Connect the source through a Copilot connector so its content is indexed for answers
- C. Connect through a Power Platform connector and query it from a tool or flow
- D. Upload the documents as file knowledge on the agent
- E. Index the content in Azure AI Search and use it as the knowledge source

### 33. Users search by serial number and by failure description, and vector search misses the numbers. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Connect to the search service over a private endpoint with managed identity
- C. Use hybrid retrieval with vector and keyword queries
- D. Enable semantic ranking and let the agent use the reranked results

### 34. The right document is retrieved but a weak passage is quoted in the answer. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Enable semantic ranking and let the agent use the reranked results
- C. Use hybrid retrieval with vector and keyword queries
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 35. A security standard forbids public network access to the search service. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Use hybrid retrieval with vector and keyword queries
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Recreate the index on every publish so it never goes stale

### 36. One index serves five business units with different entitlements. Which two decisions are required? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Connect to the search service over a private endpoint with managed identity
- C. Apply a security filter on the query before the agent composes an answer
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs
- E. Recreate the index on every publish so it never goes stale

### 37. A plant scheduling tool has no API and the agent must set a shift note in it. Which capability fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool unattended on a dedicated machine with a vaulted credential
- B. Replace the screen automation with an API once the application exposes one
- C. Configure a computer use tool against the legacy desktop application
- D. Provision a machine or machine group and run the tool there with a dedicated account

### 38. A computer use agent reports success but the record was never saved after an interface change. What should have been in place?

Domain: Integrate and extend agents in Copilot Studio

- A. Replace the screen automation with an API once the application exposes one
- B. Record the click path once and reuse it without validating each run
- C. Monitor computer use runs and capture step screenshots for review
- D. Configure a computer use tool against the legacy desktop application

### 39. A manufacturer is onboarding computer use for a licensed desktop tool. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record
- B. Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes
- C. Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes
- D. Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record

### 40. A platform team curates tools that several agents should share, and the catalogue grows monthly. Which integration fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Add an MCP server as a tool and let the agent discover the tools it exposes
- B. Embed the MCP server as a local process inside the agent
- C. Wrap the internal API as MCP tools and register the server endpoint with the agent
- D. Configure the MCP server connection with the authentication the server requires

### 41. Tools from an MCP server appear in the agent, but calls fail with an authentication error. What should be fixed?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure the MCP server connection with the authentication the server requires
- B. Expose only the MCP tools the task needs and review their descriptions
- C. Add an MCP server as a tool and let the agent discover the tools it exposes
- D. Use a streamable HTTP MCP server so the agent can reach it over the network

### 42. A builder exposes every tool from a partner server to be safe. What should the review require?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose only the MCP tools the task needs and review their descriptions
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Wrap the internal API as MCP tools and register the server endpoint with the agent
- D. Configure the MCP server connection with the authentication the server requires

### 43. The MCP server runs in a separate cluster from the hosted agent. Which transport is required?

Domain: Integrate and extend agents in Copilot Studio

- A. Embed the MCP server as a local process inside the agent
- B. Configure the MCP server connection with the authentication the server requires
- C. Add an MCP server as a tool and let the agent discover the tools it exposes
- D. Use a streamable HTTP MCP server so the agent can reach it over the network

### 44. A REST service publishes an OpenAPI definition and needs delegated authentication. What should be built?

Domain: Integrate and extend agents in Copilot Studio

- A. Call the API from an agent flow and return the parsed response to the topic
- B. Hard-code the endpoint URL and key inside the topic
- C. Call the REST API from a topic with a Send HTTP request action
- D. Create a custom connector from the OpenAPI definition and add it as a tool

### 45. A REST response must be filtered and retried before the agent sees it. Where should the call sit?

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Call the REST API from a topic with a Send HTTP request action
- C. Call the API from an agent flow and return the parsed response to the topic
- D. Define the response schema so the agent can reason over the returned fields

### 46. A REST tool will be used by four agents across two business units. Which two controls apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Create a custom connector from the OpenAPI definition and add it as a tool
- C. Call the REST API from a topic with a Send HTTP request action
- D. Define the response schema so the agent can reason over the returned fields
- E. Configure connector authentication so each call uses the caller’s identity

### 47. Releasing a change to one business area currently requires retesting an 80-topic agent. What should the architect do?

Domain: Integrate and extend agents in Copilot Studio

- A. Split the work into a parent agent that delegates to specialist child agents
- B. Give every child the same knowledge source so answers stay consistent
- C. Build one large agent with every topic so there is a single place to change
- D. Route by intent in the parent and pass only the context the child needs

### 48. A parent routes supplier questions to the payroll child agent. What should be corrected first?

Domain: Integrate and extend agents in Copilot Studio

- A. Write the parent’s instructions to describe when each child should be used
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Give every child the same knowledge source so answers stay consistent
- D. Route by intent in the parent and pass only the context the child needs

### 49. A child returns a status code the parent cannot interpret, so the summary omits the outcome. What should be agreed?

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Route by intent in the parent and pass only the context the child needs
- D. Give every child the same knowledge source so answers stay consistent

### 50. A team is decomposing a monolithic agent into a parent and three children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions
- B. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- C. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent
- D. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions

### 51. A parent will call four children in one conversation. Which two practices reduce cost and inconsistency? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Give every child the same knowledge source so answers stay consistent
- C. Split the work into a parent agent that delegates to specialist child agents
- D. Give each child a clear input and output contract and keep shared state in the parent
- E. Build one large agent with every topic so there is a single place to change

### 52. A team has a tested Foundry agent with custom tools and wants it to answer inside Copilot Studio. What should they do?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- B. Deploy the model in Foundry and point the custom prompt at that deployment
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity

### 53. A connected Foundry agent performs worse inside the parent than standalone. What was skipped?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the model in Foundry and point the custom prompt at that deployment
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Evaluate the Foundry agent against the same test set before it is connected

### 54. A custom prompt must use a Foundry deployment and stay consistent with the parent's answers. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Ground the Foundry agent in the same indexed knowledge so both layers answer consistently
- B. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- C. Deploy the model in Foundry and point the custom prompt at that deployment
- D. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- E. Evaluate the Foundry agent against the same test set before it is connected

### 55. Two published department agents already cover billing and claims, and a new parent must use them unchanged. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Add the existing agent as a connected agent and let the parent delegate to it
- B. Write a precise name and description for the connected agent so routing works
- C. Copy its topics into the new agent so both can be edited separately
- D. Confirm the caller’s identity and permissions flow through to the connected agent

### 56. A parent rarely delegates because both children have vague descriptions. What should be improved?

Domain: Integrate and extend agents in Copilot Studio

- A. Pin the connected agent’s published version that the parent was tested against
- B. Confirm the caller’s identity and permissions flow through to the connected agent
- C. Write a precise name and description for the connected agent so routing works
- D. Retire the duplicate standalone agent once the parent covers its use cases

### 57. A finance team wants margin questions answered from the governed semantic model. Which approach fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Export the data nightly into files the agent can search
- C. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- D. Define the measures in the semantic model so the data agent answers consistently

### 58. A data agent has workspace-wide read access but needs one model. What should be changed?

Domain: Integrate and extend agents in Copilot Studio

- A. Grant the data agent’s identity read access to the semantic model only
- B. Query the lakehouse directly from the agent with a SQL tool
- C. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- D. Export the data nightly into files the agent can search

### 59. A partner must learn what an internal agent can do before calling it. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish an agent card that describes the remote agent’s skills and endpoint
- B. Configure authentication between the agents so calls are authorized
- C. Track the remote task state and surface long-running results back into the conversation
- D. Model the remote capability as an A2A skill the agent can discover and invoke

### 60. A remote agent offers several capabilities, and the caller must choose one precisely. What should each capability become?

Domain: Integrate and extend agents in Copilot Studio

- A. Rebuild the remote agent’s functionality locally instead of using the protocol
- B. Publish an agent card that describes the remote agent’s skills and endpoint
- C. Configure authentication between the agents so calls are authorized
- D. Model the remote capability as an A2A skill the agent can discover and invoke

### 61. An internal agent should expose two of its eight skills to a partner. What should be defined?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure authentication between the agents so calls are authorized
- B. Define which remote agents are trusted and restrict the skills exposed to them
- C. Publish an agent card that describes the remote agent’s skills and endpoint
- D. Track the remote task state and surface long-running results back into the conversation

### 62. A cheaper model is proposed for a compliance-sensitive agent. What should the team produce first?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the chosen model and reference the deployment from the custom prompt
- B. Compare candidate models on a sample of real cases before switching
- C. Provision enough quota and throughput for peak conversation volume
- D. Keep the default model because it is already configured

### 63. Peak load is thirty times the pilot, and responses start throttling. What should be reviewed?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision enough quota and throughput for peak conversation volume
- B. Deploy the model in a region that satisfies the data residency requirement
- C. Deploy the chosen model and reference the deployment from the custom prompt
- D. Choose a model from the catalog that meets quality, latency, and residency needs

### 64. No one can reconstruct what the agent said to a customer last Tuesday. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Alert on failed tool calls and answer-quality regressions
- B. Query conversation and tool spans in Application Insights with KQL
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Connect the agent to Application Insights and emit conversation and tool telemetry

### 65. A single wrong answer needs its retrieval and tool spans assembled. What should be used?

Domain: Integrate and extend agents in Copilot Studio

- A. Alert on failed tool calls and answer-quality regressions
- B. Query conversation and tool spans in Application Insights with KQL
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Connect the agent to Application Insights and emit conversation and tool telemetry

### 66. Telemetry volume triples after a launch. What keeps the cost predictable without hiding failures?

Domain: Integrate and extend agents in Copilot Studio

- A. Sample telemetry so volume stays affordable while errors are always kept
- B. Connect the agent to Application Insights and emit conversation and tool telemetry
- C. Correlate a failed answer with the tool call and knowledge retrieval behind it
- D. Log full conversation transcripts indefinitely without retention limits

### 67. An operations team owns an agent with four tools. Which two monitoring capabilities matter most? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Log full conversation transcripts indefinitely without retention limits
- B. Correlate a failed answer with the tool call and knowledge retrieval behind it
- C. Alert on failed tool calls and answer-quality regressions
- D. Connect the agent to Application Insights and emit conversation and tool telemetry
- E. Sample telemetry so volume stays affordable while errors are always kept

### 68. A test set was generated entirely from topic titles. Which change most improves it?

Domain: Test and manage agents

- A. Build the test set from real anonymized conversations plus the cases that must never fail
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Test with a handful of happy-path questions before release
- D. Hold part of the set out of prompt tuning so results stay honest

### 69. A red-team asks how the agent reacts to a request to reveal its system instructions. Which cases cover that?

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Include adversarial and edge cases such as out-of-scope and injection attempts
- C. Test with a handful of happy-path questions before release
- D. Version the test set and rerun it for every change

### 70. A team is standing up an evaluation loop before a release. Which sequence is correct?

Domain: Test and manage agents

- A. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change
- B. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change
- C. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- D. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent

### 71. A test set will be reused for a year of releases. Which two practices keep it honest? Select two.

Domain: Test and manage agents

- A. Build the test set from real anonymized conversations plus the cases that must never fail
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Test with a handful of happy-path questions before release
- D. Version the test set and rerun it for every change
- E. Hold part of the set out of prompt tuning so results stay honest

### 72. A team must score 700 answers weekly with one reviewer. Which method is practical?

Domain: Test and manage agents

- A. Have subject-matter experts score a sample against the rubric
- B. Score answers with keyword matching against expected phrases
- C. Use model-based grading against a rubric and review a human sample
- D. Rely on the builder trying a few questions in the test pane

### 73. A quality lead is calibrating automated grading against people. Which sequence is correct?

Domain: Test and manage agents

- A. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores
- B. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores
- C. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- D. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand

### 74. The overall score is 93 percent, but every safety-related answer fails. What should the gate do?

Domain: Test and manage agents

- A. Compare the new run against the previous baseline before publishing
- B. Set a pass threshold per category and block release below it
- C. Publish when the overall average looks acceptable
- D. Keep failed cases in the test set so they cannot regress

### 75. Failures accumulate in a shared backlog that nobody owns. What should change?

Domain: Test and manage agents

- A. Assign each failure cluster to the owner of the topic, prompt, or connector
- B. Publish when the overall average looks acceptable
- C. Group failures by topic and root cause instead of fixing items one at a time
- D. Keep failed cases in the test set so they cannot regress

### 76. The only copy of an agent in the build environment is a managed solution. Where should the change be made?

Domain: Test and manage agents

- A. Create a solution and add the agent and its dependencies to it
- B. Send the agents topic files to the administrator by email
- C. Export the managed solution and import it into the target environment
- D. Keep the agent in an unmanaged solution in development and ship a managed solution

### 77. A solution is being prepared for its first promotion. Which sequence is correct?

Domain: Test and manage agents

- A. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- B. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- C. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- D. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables

### 78. A solution hard-codes a test URL that will be wrong in production. What should replace it?

Domain: Test and manage agents

- A. Set the environment variable values as part of the pipeline deployment step
- B. Hard-code the production endpoint in the topic and change it after import
- C. Store the secret in a vault and reference it from the environment variable
- D. Define an environment variable for the endpoint and set a value per environment

### 79. A connector key is visible in the topic designer and in every export. Where should it live?

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Use the current value in production and a default value for development
- C. Hard-code the production endpoint in the topic and change it after import
- D. Record the required values in the deployment notes for each environment

### 80. A solution serves two environments with different endpoints and no vault requirement. Which two choices fit? Select two.

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Use the current value in production and a default value for development
- C. Hard-code the production endpoint in the topic and change it after import
- D. Set the environment variable values as part of the pipeline deployment step
- E. Record the required values in the deployment notes for each environment

### 81. A regression reached production after passing no automated check. What should the pipeline add?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Add a pre-deployment step that runs the agent test set and blocks on failure
- C. Import the solution by hand into production for each release
- D. Use the pipeline analytics to see which stage failed and why

### 82. A release must record who accepted the risk before production. What should be configured?

Domain: Test and manage agents

- A. Use the pipeline analytics to see which stage failed and why
- B. Add a pre-deployment step that runs the agent test set and blocks on failure
- C. Import the solution by hand into production for each release
- D. Require approval before the production stage runs

### 83. A team is creating a staged pipeline with a gate. Which sequence is correct?

Domain: Test and manage agents

- A. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval
- B. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval
- C. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage
- D. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step

### 84. A regulated pipeline needs per-stage settings and a reversal plan. Which two controls apply? Select two.

Domain: Test and manage agents

- A. Pass environment-specific values through pipeline configuration rather than editing the solution
- B. Notify the owning team with the deployment result and the failed step
- C. Keep the previous managed solution version so you can roll back
- D. Deploy only the components that changed when the pipeline supports it
- E. Deploy on a fixed schedule regardless of readiness

### 85. A single-topic fix redeploys forty components across three stages. What should change?

Domain: Test and manage agents

- A. Notify the owning team with the deployment result and the failed step
- B. Pass environment-specific values through pipeline configuration rather than editing the solution
- C. Deploy on a fixed schedule regardless of readiness
- D. Deploy only the components that changed when the pipeline supports it

### 86. A failed deployment is discovered at the next standup. What should be added?

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Notify the owning team with the deployment result and the failed step
- C. Keep the previous managed solution version so you can roll back
- D. Deploy on a fixed schedule regardless of readiness

### 87. Users say answers are unhelpful but nothing records which ones. What should be added?

Domain: Test and manage agents

- A. Test once before launch and assume behaviour stays stable
- B. Sample production conversations and score them against the rubric on a schedule
- C. Track containment, resolution, and escalation metrics on a dashboard
- D. Capture user feedback in the conversation and route negative cases to review

### 88. A year after launch, no one knows whether quality held. What should be introduced?

Domain: Test and manage agents

- A. Capture user feedback in the conversation and route negative cases to review
- B. Track containment, resolution, and escalation metrics on a dashboard
- C. Test once before launch and assume behaviour stays stable
- D. Sample production conversations and score them against the rubric on a schedule

---

## Case study — Beacon Financial

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Compliance requires that every refusal is logged with the question that triggered it. What should be enabled?

Domain: Plan and configure agent solutions

- A. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- B. Restrict who can author and publish with Copilot Studio security roles
- C. Turn on audit logging and retain agent conversation records
- D. Separate development and production environments with environment security groups

### 90. Some advisors hold a licence for only one product line. Where must that restriction be applied to retrieved material?

Domain: Integrate and extend agents in Copilot Studio

- A. Apply a security filter on the query before the agent composes an answer
- B. Recreate the index on every publish so it never goes stale
- C. Connect to the search service over a private endpoint with managed identity
- D. Enable semantic ranking and let the agent use the reranked results

### 91. The regulator asks how the team knows answers are supported by the source material. Which measure answers that?

Domain: Test and manage agents

- A. Score answers with keyword matching against expected phrases
- B. Measure groundedness by checking each claim against the retrieved passage
- C. Rely on the builder trying a few questions in the test pane
- D. Measure topic-trigger accuracy separately from answer quality

---

## Case study — Litware Manufacturing

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Four plants share one defect-handling behaviour but need different endpoints. Which two practices apply? Select two.

Domain: Plan and configure agent solutions

- A. Parameterize environment-specific values with environment variables
- B. Rebuild the same topic in each agent to avoid a shared dependency
- C. Copy the topics into each agent so every team can edit its own copy
- D. Package the shared topics, flows, and connection references in a solution
- E. Extract the shared logic into a reusable component or child agent and reference it

### 93. Quality standards live in a SharePoint library whose site permissions must keep applying. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Add the SharePoint site as a knowledge source and rely on item-level permissions
- B. Register the database as a knowledge source so the agent can query it directly
- C. Index the content in Azure AI Search and use it as the knowledge source
- D. Upload the documents as file knowledge on the agent

### 94. Standards are revised quarterly by quality managers. Which two controls protect answer quality? Select two.

Domain: Test and manage agents

- A. Track containment, resolution, and escalation metrics on a dashboard
- B. Sample production conversations and score them against the rubric on a schedule
- C. Capture user feedback in the conversation and route negative cases to review
- D. Watch for knowledge-source changes and re-run the evaluation after they land
- E. Test once before launch and assume behaviour stays stable

---

## Case study — Portside Utilities

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. During storms the network API starts failing and the team learns days later. What should be added?

Domain: Plan and configure agent solutions

- A. Use the Copilot Studio analytics view for session and topic outcomes
- B. Add a comment step to the flow describing the expected failure
- C. Configure an alert on failed runs and route it to the owning team
- D. Review the flow run history and its action-level inputs and outputs

### 96. The work-order API response must be reshaped and retried before the agent uses it. Where should the call live?

Domain: Integrate and extend agents in Copilot Studio

- A. Define the response schema so the agent can reason over the returned fields
- B. Call the REST API from a topic with a Send HTTP request action
- C. Call the API from an agent flow and return the parsed response to the topic
- D. Hard-code the endpoint URL and key inside the topic

### 97. Storm days produce six times the normal volume and unusual requests. What should the test set include?

Domain: Test and manage agents

- A. Test with a handful of happy-path questions before release
- B. Include adversarial and edge cases such as out-of-scope and injection attempts
- C. Version the test set and rerun it for every change
- D. Hold part of the set out of prompt tuning so results stay honest

---

## Case study — Salish Education

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Some answers contain personal data, and the agent must only ever show a student their own record. Which identity decision fits?

Domain: Plan and configure agent solutions

- A. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- B. Store one API key in a topic variable and reuse it for every user
- C. Give every conversation a single shared service account credential for the API
- D. Allow anonymous access to the agent and authenticate only at the API

### 99. The same agent must serve students from a public website and from Microsoft Teams. Which channel pair does the case describe?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Publish to email and answer asynchronously
- C. Embed the agent in a custom application through the Direct Line channel
- D. Publish to a public website with authenticated sign-in

### 100. Two surfaces must behave identically, and every change is compared against the last release. What should the test set be?

Domain: Test and manage agents

- A. Generate synthetic cases from the topics and intents the agent supports
- B. Test with a handful of happy-path questions before release
- C. Hold part of the set out of prompt tuning so results stay honest
- D. Version the test set and rerun it for every change

---

## Answer key and explanations

### Question 1 — A

Answer: Expose the system through a virtual table or connector view that the agent can read. A virtual table projects the external source into Dataverse, provided the source can answer the queries the agent issues. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. In this case: A virtual table projects the external source into Dataverse, provided the source can answer the queries the agent issues.
- **B:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: A virtual table projects the external source into Dataverse, provided the source can answer the queries the agent issues.
- **C:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: A virtual table projects the external source into Dataverse, provided the source can answer the queries the agent issues.
- **D:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: A virtual table projects the external source into Dataverse, provided the source can answer the queries the agent issues.

### Question 2 — C

Answer: Call the internal endpoint straight from the topic over HTTP. A direct call usually fails inside a locked-down network and bypasses the connector governance the platform provides. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: A direct call usually fails inside a locked-down network and bypasses the connector governance the platform provides.
- **B:** Incorrect for this question. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Why the correct answer wins: A direct call usually fails inside a locked-down network and bypasses the connector governance the platform provides.
- **C:** Correct. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. In this case: A direct call usually fails inside a locked-down network and bypasses the connector governance the platform provides.
- **D:** Incorrect for this question. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Why the correct answer wins: A direct call usually fails inside a locked-down network and bypasses the connector governance the platform provides.

### Question 3 — A

Answer: Use the on-behalf-of flow so the agent calls the API as the signed-in user. The on-behalf-of flow passes the operator identity to the API so its own rules decide what is allowed. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. In this case: The on-behalf-of flow passes the operator identity to the API so its own rules decide what is allowed.
- **B:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: The on-behalf-of flow passes the operator identity to the API so its own rules decide what is allowed.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: The on-behalf-of flow passes the operator identity to the API so its own rules decide what is allowed.
- **D:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: The on-behalf-of flow passes the operator identity to the API so its own rules decide what is allowed.

### Question 4 — D

Answer: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream. One shared account erases per-user attribution and gives every conversation the same rights. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: One shared account erases per-user attribution and gives every conversation the same rights.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: One shared account erases per-user attribution and gives every conversation the same rights.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: One shared account erases per-user attribution and gives every conversation the same rights.
- **D:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: One shared account erases per-user attribution and gives every conversation the same rights.

### Question 5 — A, D

Answers: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream; Use the agent managed identity for Azure resources and keep user identity for business data. User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. In this case: User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets.
- **D:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets.
- **E:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, while the managed identity reaches Azure resources without stored secrets.

### Question 6 — B

Answer: Publish the agent into Microsoft 365 Copilot so it appears alongside other agents. Publishing into the Copilot experience places the agent where staff already work under tenant controls. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Publishing into the Copilot experience places the agent where staff already work under tenant controls.
- **B:** Correct. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. In this case: Publishing into the Copilot experience places the agent where staff already work under tenant controls.
- **C:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Publishing into the Copilot experience places the agent where staff already work under tenant controls.
- **D:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Publishing into the Copilot experience places the agent where staff already work under tenant controls.

### Question 7 — D

Answer: Publish to a public website with authenticated sign-in. The website channel serves external audiences and can require authentication before member content. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: The website channel serves external audiences and can require authentication before member content.
- **B:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: The website channel serves external audiences and can require authentication before member content.
- **C:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: The website channel serves external audiences and can require authentication before member content.
- **D:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: The website channel serves external audiences and can require authentication before member content.

### Question 8 — C

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line lets the host application own both the interface and the sign-in. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Direct Line lets the host application own both the interface and the sign-in.
- **B:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Direct Line lets the host application own both the interface and the sign-in.
- **C:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line lets the host application own both the interface and the sign-in.
- **D:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Direct Line lets the host application own both the interface and the sign-in.

### Question 9 — D

Answer: Constrain the tools the agent may call, validate tool output, and limit autonomous actions. Limiting tools, validating outputs, and requiring approval before irreversible actions contains an injected instruction. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Limiting tools, validating outputs, and requiring approval before irreversible actions contains an injected instruction.
- **B:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Limiting tools, validating outputs, and requiring approval before irreversible actions contains an injected instruction.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Limiting tools, validating outputs, and requiring approval before irreversible actions contains an injected instruction.
- **D:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Limiting tools, validating outputs, and requiring approval before irreversible actions contains an injected instruction.

### Question 10 — D

Answer: Turn on audit logging and retain agent conversation records. Audit records with a retention period matched to policy keep the answer available for the dispute. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit records with a retention period matched to policy keep the answer available for the dispute.
- **B:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit records with a retention period matched to policy keep the answer available for the dispute.
- **C:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit records with a retention period matched to policy keep the answer available for the dispute.
- **D:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit records with a retention period matched to policy keep the answer available for the dispute.

### Question 11 — C

Answer: Restrict who can author and publish with Copilot Studio security roles. Publishing rights belong with a small named group defined through Copilot Studio security roles. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Publishing rights belong with a small named group defined through Copilot Studio security roles.
- **B:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Publishing rights belong with a small named group defined through Copilot Studio security roles.
- **C:** Correct. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. In this case: Publishing rights belong with a small named group defined through Copilot Studio security roles.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Publishing rights belong with a small named group defined through Copilot Studio security roles.

### Question 12 — B, C

Answers: Apply a data loss prevention policy that blocks unapproved connectors in the environment; Enforce the source system’s permissions in the knowledge layer so answers respect access. Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights.
- **B:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights.
- **C:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights.
- **D:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights.
- **E:** Incorrect for this question. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Why the correct answer wins: Data loss prevention restricts which connectors may carry that content, and permission trimming keeps answers inside the caller's rights.

### Question 13 — A

Answer: Parameterize environment-specific values with environment variables. An environment variable supplies the region endpoint while the component itself stays identical. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. In this case: An environment variable supplies the region endpoint while the component itself stays identical.
- **B:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: An environment variable supplies the region endpoint while the component itself stays identical.
- **C:** Incorrect for this question. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Why the correct answer wins: An environment variable supplies the region endpoint while the component itself stays identical.
- **D:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: An environment variable supplies the region endpoint while the component itself stays identical.

### Question 14 — C

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution is created and configured before it is exported and promoted through the pipeline. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution is created and configured before it is exported and promoted through the pipeline.
- **B:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution is created and configured before it is exported and promoted through the pipeline.
- **C:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution is created and configured before it is exported and promoted through the pipeline.
- **D:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution is created and configured before it is exported and promoted through the pipeline.

### Question 15 — D

Answer: Create the flow with the connector action the agent needs and return the result. A flow wraps the connector calls, sequences them, and returns the value to the topic. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: A flow wraps the connector calls, sequences them, and returns the value to the topic.
- **B:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A flow wraps the connector calls, sequences them, and returns the value to the topic.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A flow wraps the connector calls, sequences them, and returns the value to the topic.
- **D:** Correct. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. In this case: A flow wraps the connector calls, sequences them, and returns the value to the topic.

### Question 16 — C

Answer: Define typed input and output parameters on the flow and bind them from the topic. The flow needs typed output parameters and the topic needs to read them. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: The flow needs typed output parameters and the topic needs to read them.
- **B:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: The flow needs typed output parameters and the topic needs to read them.
- **C:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: The flow needs typed output parameters and the topic needs to read them.
- **D:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: The flow needs typed output parameters and the topic needs to read them.

### Question 17 — C

Answer: Use an automated cloud flow triggered by an event and have the agent wait for it. An automated flow reacts to the event, and the agent does not need to wait for it. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An automated flow reacts to the event, and the agent does not need to wait for it.
- **B:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: An automated flow reacts to the event, and the agent does not need to wait for it.
- **C:** Correct. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. In this case: An automated flow reacts to the event, and the agent does not need to wait for it.
- **D:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An automated flow reacts to the event, and the agent does not need to wait for it.

### Question 18 — C, E

Answers: Wrap the calls in a scope with a parallel error branch that returns a structured failure; Define typed input and output parameters on the flow and bind them from the topic. An error branch prevents a silent stall, and typed parameters let the topic report the real outcome. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An error branch prevents a silent stall, and typed parameters let the topic report the real outcome.
- **B:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An error branch prevents a silent stall, and typed parameters let the topic report the real outcome.
- **C:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: An error branch prevents a silent stall, and typed parameters let the topic report the real outcome.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: An error branch prevents a silent stall, and typed parameters let the topic report the real outcome.
- **E:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: An error branch prevents a silent stall, and typed parameters let the topic report the real outcome.

### Question 19 — D

Answer: Post an adaptive card to Teams and wait for the human decision before continuing. An adaptive card in Teams delivers the decision where the manager already works and records the response. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Why the correct answer wins: An adaptive card in Teams delivers the decision where the manager already works and records the response.
- **B:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: An adaptive card in Teams delivers the decision where the manager already works and records the response.
- **C:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: An adaptive card in Teams delivers the decision where the manager already works and records the response.
- **D:** Correct. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. In this case: An adaptive card in Teams delivers the decision where the manager already works and records the response.

### Question 20 — C

Answer: Set a response timeout and route to a fallback owner when nobody answers. A response timeout routes to a fallback owner so the request cannot stall indefinitely. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Why the correct answer wins: A response timeout routes to a fallback owner so the request cannot stall indefinitely.
- **B:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: A response timeout routes to a fallback owner so the request cannot stall indefinitely.
- **C:** Correct. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. In this case: A response timeout routes to a fallback owner so the request cannot stall indefinitely.
- **D:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: A response timeout routes to a fallback owner so the request cannot stall indefinitely.

### Question 21 — B

Answer: Send flow telemetry to Application Insights and query the traces. Telemetry in Application Insights keeps the trace, including the dependency call that failed. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Telemetry in Application Insights keeps the trace, including the dependency call that failed.
- **B:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Telemetry in Application Insights keeps the trace, including the dependency call that failed.
- **C:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Telemetry in Application Insights keeps the trace, including the dependency call that failed.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Telemetry in Application Insights keeps the trace, including the dependency call that failed.

### Question 22 — D

Answer: Review the flow run history and its action-level inputs and outputs. Run history keeps each action's inputs and outputs for that specific run. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Run history keeps each action's inputs and outputs for that specific run.
- **B:** Incorrect for this question. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Why the correct answer wins: Run history keeps each action's inputs and outputs for that specific run.
- **C:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Run history keeps each action's inputs and outputs for that specific run.
- **D:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Run history keeps each action's inputs and outputs for that specific run.

### Question 23 — A, C

Answers: Configure an alert on failed runs and route it to the owning team; Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted.
- **B:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted.
- **C:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted.
- **D:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted.
- **E:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs transient faults, and an alert brings a person in when retries are exhausted.

### Question 24 — B

Answer: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns. Reset the value at the start of the topic and keep it in topic scope so it cannot leak forward. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: Reset the value at the start of the topic and keep it in topic scope so it cannot leak forward.
- **B:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: Reset the value at the start of the topic and keep it in topic scope so it cannot leak forward.
- **C:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: Reset the value at the start of the topic and keep it in topic scope so it cannot leak forward.
- **D:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: Reset the value at the start of the topic and keep it in topic scope so it cannot leak forward.

### Question 25 — D

Answer: Return an adaptive card so the data renders in labelled fields. An adaptive card renders labelled values and the action in one response. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: An adaptive card renders labelled values and the action in one response.
- **B:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: An adaptive card renders labelled values and the action in one response.
- **C:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: An adaptive card renders labelled values and the action in one response.
- **D:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: An adaptive card renders labelled values and the action in one response.

### Question 26 — B, C

Answers: Store the value in a global variable so later topics can read it; Configure the topic as a redirect target with its own trigger phrases. A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership.
- **B:** Correct. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. In this case: A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership.
- **C:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership.
- **D:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership.
- **E:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: A global variable keeps shared context available, and a redirect topic keeps the dialogue separated for ownership.

### Question 27 — B

Answer: Configure a custom prompt that fixes the tone, structure, and citation behaviour. A custom prompt sets the required structure and tone without changing the knowledge. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A custom prompt sets the required structure and tone without changing the knowledge.
- **B:** Correct. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. In this case: A custom prompt sets the required structure and tone without changing the knowledge.
- **C:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: A custom prompt sets the required structure and tone without changing the knowledge.
- **D:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: A custom prompt sets the required structure and tone without changing the knowledge.

### Question 28 — C

Answer: Require the answer to cite retrieved passages and refuse when none are found. Requiring a citation from retrieved passages, and refusing when none exists, is what makes the answer verifiable. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: Requiring a citation from retrieved passages, and refusing when none exists, is what makes the answer verifiable.
- **B:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Requiring a citation from retrieved passages, and refusing when none exists, is what makes the answer verifiable.
- **C:** Correct. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. In this case: Requiring a citation from retrieved passages, and refusing when none exists, is what makes the answer verifiable.
- **D:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Requiring a citation from retrieved passages, and refusing when none exists, is what makes the answer verifiable.

### Question 29 — B

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge respects each user's existing access without creating a copy. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint knowledge respects each user's existing access without creating a copy.
- **B:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge respects each user's existing access without creating a copy.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge respects each user's existing access without creating a copy.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge respects each user's existing access without creating a copy.

### Question 30 — C

Answer: Register the database as a knowledge source so the agent can query it directly. Registering the database as knowledge lets the agent query structured reference data directly. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: Registering the database as knowledge lets the agent query structured reference data directly.
- **B:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: Registering the database as knowledge lets the agent query structured reference data directly.
- **C:** Correct. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. In this case: Registering the database as knowledge lets the agent query structured reference data directly.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: Registering the database as knowledge lets the agent query structured reference data directly.

### Question 31 — B

Answer: Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions. Inventory precedes choice, connection precedes access testing, and the unsupported-question review comes last. Inventory precedes choice, choice precedes connection, and access testing follows connection. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The connector cannot be chosen before the inventory describes the sources. Why the correct answer wins: Inventory precedes choice, connection precedes access testing, and the unsupported-question review comes last.
- **B:** Correct. Inventory precedes choice, choice precedes connection, and access testing follows connection. In this case: Inventory precedes choice, connection precedes access testing, and the unsupported-question review comes last.
- **C:** Incorrect for this question. Access testing requires connected sources. Why the correct answer wins: Inventory precedes choice, connection precedes access testing, and the unsupported-question review comes last.
- **D:** Incorrect for this question. There is nothing to review before the knowledge is connected and tested. Why the correct answer wins: Inventory precedes choice, connection precedes access testing, and the unsupported-question review comes last.

### Question 32 — B, E

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Index the content in Azure AI Search and use it as the knowledge source. A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters.
- **B:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters.
- **C:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters.
- **E:** Correct. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. In this case: A Copilot connector inherits the source permissions, and an AI Search index gives control over chunking, ranking, and filters.

### Question 33 — C

Answer: Use hybrid retrieval with vector and keyword queries. Hybrid retrieval pairs keyword matching with vectors so exact identifiers are found. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Hybrid retrieval pairs keyword matching with vectors so exact identifiers are found.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Hybrid retrieval pairs keyword matching with vectors so exact identifiers are found.
- **C:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Hybrid retrieval pairs keyword matching with vectors so exact identifiers are found.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: Hybrid retrieval pairs keyword matching with vectors so exact identifiers are found.

### Question 34 — B

Answer: Enable semantic ranking and let the agent use the reranked results. Semantic ranking reorders the candidates so the strongest passage reaches the model. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Semantic ranking reorders the candidates so the strongest passage reaches the model.
- **B:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: Semantic ranking reorders the candidates so the strongest passage reaches the model.
- **C:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: Semantic ranking reorders the candidates so the strongest passage reaches the model.
- **D:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: Semantic ranking reorders the candidates so the strongest passage reaches the model.

### Question 35 — A

Answer: Connect to the search service over a private endpoint with managed identity. A private endpoint with managed identity keeps traffic private and removes stored keys. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. In this case: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **B:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **C:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **D:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.

### Question 36 — C, D

Answers: Apply a security filter on the query before the agent composes an answer; Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema must store the entitlement field, and every query must filter on it before the model reads anything. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema must store the entitlement field, and every query must filter on it before the model reads anything.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema must store the entitlement field, and every query must filter on it before the model reads anything.
- **C:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The schema must store the entitlement field, and every query must filter on it before the model reads anything.
- **D:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema must store the entitlement field, and every query must filter on it before the model reads anything.
- **E:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema must store the entitlement field, and every query must filter on it before the model reads anything.

### Question 37 — C

Answer: Configure a computer use tool against the legacy desktop application. Computer use drives the existing interface when no programmatic route exists. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Computer use drives the existing interface when no programmatic route exists.
- **B:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Computer use drives the existing interface when no programmatic route exists.
- **C:** Correct. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. In this case: Computer use drives the existing interface when no programmatic route exists.
- **D:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Computer use drives the existing interface when no programmatic route exists.

### Question 38 — C

Answer: Monitor computer use runs and capture step screenshots for review. Step screenshots and validation of the expected screen make that failure visible immediately. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Step screenshots and validation of the expected screen make that failure visible immediately.
- **B:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: Step screenshots and validation of the expected screen make that failure visible immediately.
- **C:** Correct. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. In this case: Step screenshots and validation of the expected screen make that failure visible immediately.
- **D:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: Step screenshots and validation of the expected screen make that failure visible immediately.

### Question 39 — B

Answer: Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes. Confirm no API, prepare a host, record the steps, run and inspect, then monitor for interface change. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Monitoring a tool that has never run and has no host is not possible. Why the correct answer wins: Confirm no API, prepare a host, record the steps, run and inspect, then monitor for interface change.
- **B:** Correct. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. In this case: Confirm no API, prepare a host, record the steps, run and inspect, then monitor for interface change.
- **C:** Incorrect for this question. Recording happens on the prepared machine, after the API check. Why the correct answer wins: Confirm no API, prepare a host, record the steps, run and inspect, then monitor for interface change.
- **D:** Incorrect for this question. A run cannot precede the host and the recorded steps. Why the correct answer wins: Confirm no API, prepare a host, record the steps, run and inspect, then monitor for interface change.

### Question 40 — A

Answer: Add an MCP server as a tool and let the agent discover the tools it exposes. An MCP server exposes the catalogue so agents discover tools without redeployment. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. In this case: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **B:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **C:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.

### Question 41 — A

Answer: Configure the MCP server connection with the authentication the server requires. The MCP server connection needs valid authentication before any tool call succeeds. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: The MCP server connection needs valid authentication before any tool call succeeds.
- **B:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: The MCP server connection needs valid authentication before any tool call succeeds.
- **C:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: The MCP server connection needs valid authentication before any tool call succeeds.
- **D:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: The MCP server connection needs valid authentication before any tool call succeeds.

### Question 42 — A

Answer: Expose only the MCP tools the task needs and review their descriptions. Expose only the tools the task needs, so a bad instruction cannot reach the rest. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: Expose only the tools the task needs, so a bad instruction cannot reach the rest.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Expose only the tools the task needs, so a bad instruction cannot reach the rest.
- **C:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: Expose only the tools the task needs, so a bad instruction cannot reach the rest.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Expose only the tools the task needs, so a bad instruction cannot reach the rest.

### Question 43 — D

Answer: Use a streamable HTTP MCP server so the agent can reach it over the network. Streamable HTTP reaches a remote server over the network. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **B:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **C:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **D:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: Streamable HTTP reaches a remote server over the network.

### Question 44 — D

Answer: Create a custom connector from the OpenAPI definition and add it as a tool. A custom connector from the definition gives typed operations and delegated authentication. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A custom connector from the definition gives typed operations and delegated authentication.
- **B:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector from the definition gives typed operations and delegated authentication.
- **C:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector from the definition gives typed operations and delegated authentication.
- **D:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector from the definition gives typed operations and delegated authentication.

### Question 45 — C

Answer: Call the API from an agent flow and return the parsed response to the topic. An agent flow can transform and retry before returning clean values to the topic. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: An agent flow can transform and retry before returning clean values to the topic.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: An agent flow can transform and retry before returning clean values to the topic.
- **C:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: An agent flow can transform and retry before returning clean values to the topic.
- **D:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: An agent flow can transform and retry before returning clean values to the topic.

### Question 46 — D, E

Answers: Configure connector authentication so each call uses the caller’s identity; Define the response schema so the agent can reason over the returned fields. Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields.
- **B:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields.
- **C:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields.
- **D:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields.
- **E:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication preserves each caller's rights, and a declared schema lets the agent use individual fields.

### Question 47 — A

Answer: Split the work into a parent agent that delegates to specialist child agents. Delegate to specialist children so each area has an owner, a test set, and its own release. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Delegate to specialist children so each area has an owner, a test set, and its own release.
- **B:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Delegate to specialist children so each area has an owner, a test set, and its own release.
- **C:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Delegate to specialist children so each area has an owner, a test set, and its own release.
- **D:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Delegate to specialist children so each area has an owner, a test set, and its own release.

### Question 48 — A

Answer: Write the parent’s instructions to describe when each child should be used. The parent's routing instructions describe when each child applies, so unclear descriptions cause the misroute. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: The parent's routing instructions describe when each child applies, so unclear descriptions cause the misroute.
- **B:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: The parent's routing instructions describe when each child applies, so unclear descriptions cause the misroute.
- **C:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: The parent's routing instructions describe when each child applies, so unclear descriptions cause the misroute.
- **D:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: The parent's routing instructions describe when each child applies, so unclear descriptions cause the misroute.

### Question 49 — B

Answer: Give each child a clear input and output contract and keep shared state in the parent. An input and output contract fixes the format so the parent can combine results safely. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: An input and output contract fixes the format so the parent can combine results safely.
- **B:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: An input and output contract fixes the format so the parent can combine results safely.
- **C:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: An input and output contract fixes the format so the parent can combine results safely.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: An input and output contract fixes the format so the parent can combine results safely.

### Question 50 — B

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Routing instructions and children come first, testing follows, and tuning follows the test evidence. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Routing instructions and children come first, testing follows, and tuning follows the test evidence.
- **B:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Routing instructions and children come first, testing follows, and tuning follows the test evidence.
- **C:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Routing instructions and children come first, testing follows, and tuning follows the test evidence.
- **D:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Routing instructions and children come first, testing follows, and tuning follows the test evidence.

### Question 51 — A, B

Answers: Route by intent in the parent and pass only the context the child needs; Give every child the same knowledge source so answers stay consistent. Pass only the context each child needs, and ground every child in the same knowledge source. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. In this case: Pass only the context each child needs, and ground every child in the same knowledge source.
- **B:** Correct. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. In this case: Pass only the context each child needs, and ground every child in the same knowledge source.
- **C:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge source.
- **D:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge source.
- **E:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge source.

### Question 52 — A

Answer: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent. Connect the Foundry agent so the turn is delegated to the behaviour that was already evaluated. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: Connect the Foundry agent so the turn is delegated to the behaviour that was already evaluated.
- **B:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Connect the Foundry agent so the turn is delegated to the behaviour that was already evaluated.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Connect the Foundry agent so the turn is delegated to the behaviour that was already evaluated.
- **D:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Connect the Foundry agent so the turn is delegated to the behaviour that was already evaluated.

### Question 53 — D

Answer: Evaluate the Foundry agent against the same test set before it is connected. The Foundry agent should have been evaluated on the shared test set before being connected. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: The Foundry agent should have been evaluated on the shared test set before being connected.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: The Foundry agent should have been evaluated on the shared test set before being connected.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: The Foundry agent should have been evaluated on the shared test set before being connected.
- **D:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: The Foundry agent should have been evaluated on the shared test set before being connected.

### Question 54 — A, C

Answers: Deploy the model in Foundry and point the custom prompt at that deployment; Ground the Foundry agent in the same indexed knowledge so both layers answer consistently. Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. In this case: Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses.
- **B:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses.
- **C:** Correct. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. In this case: Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses.
- **D:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses.
- **E:** Incorrect for this question. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Why the correct answer wins: Deploy the model and reference that deployment from the prompt, and ground it in the same corpus the parent uses.

### Question 55 — A

Answer: Add the existing agent as a connected agent and let the parent delegate to it. Add them as connected agents so their owners keep control of behaviour and releases. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. In this case: Add them as connected agents so their owners keep control of behaviour and releases.
- **B:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Add them as connected agents so their owners keep control of behaviour and releases.
- **C:** Incorrect for this question. A copy forks the behaviour and doubles the maintenance from the first day. Why the correct answer wins: Add them as connected agents so their owners keep control of behaviour and releases.
- **D:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Add them as connected agents so their owners keep control of behaviour and releases.

### Question 56 — C

Answer: Write a precise name and description for the connected agent so routing works. Names and descriptions drive routing, so they must state precisely what each child handles. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An unpinned dependency can change behaviour between your test run and your release. Why the correct answer wins: Names and descriptions drive routing, so they must state precisely what each child handles.
- **B:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Names and descriptions drive routing, so they must state precisely what each child handles.
- **C:** Correct. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. In this case: Names and descriptions drive routing, so they must state precisely what each child handles.
- **D:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Names and descriptions drive routing, so they must state precisely what each child handles.

### Question 57 — C

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the model, so the agreed measures are used. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the model, so the agreed measures are used.
- **B:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the model, so the agreed measures are used.
- **C:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the model, so the agreed measures are used.
- **D:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: A Fabric data agent answers from the model, so the agreed measures are used.

### Question 58 — A

Answer: Grant the data agent’s identity read access to the semantic model only. Scope its read access to the model it answers from. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. In this case: Scope its read access to the model it answers from.
- **B:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Scope its read access to the model it answers from.
- **C:** Incorrect for this question. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Why the correct answer wins: Scope its read access to the model it answers from.
- **D:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Scope its read access to the model it answers from.

### Question 59 — A

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. The agent card advertises skills and the endpoint so the caller can discover them. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: The agent card advertises skills and the endpoint so the caller can discover them.
- **B:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: The agent card advertises skills and the endpoint so the caller can discover them.
- **C:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: The agent card advertises skills and the endpoint so the caller can discover them.
- **D:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: The agent card advertises skills and the endpoint so the caller can discover them.

### Question 60 — D

Answer: Model the remote capability as an A2A skill the agent can discover and invoke. Each capability is modelled as an A2A skill with a description precise enough to select. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: Each capability is modelled as an A2A skill with a description precise enough to select.
- **B:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: Each capability is modelled as an A2A skill with a description precise enough to select.
- **C:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: Each capability is modelled as an A2A skill with a description precise enough to select.
- **D:** Correct. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. In this case: Each capability is modelled as an A2A skill with a description precise enough to select.

### Question 61 — B

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary restricts which skills a remote agent may invoke. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.
- **B:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary restricts which skills a remote agent may invoke.
- **C:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.
- **D:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.

### Question 62 — B

Answer: Compare candidate models on a sample of real cases before switching. A side-by-side run on real cases is the evidence that quality survives the change. A side-by-side run on real questions is the only evidence that a cheaper model is still good enough. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: A side-by-side run on real cases is the evidence that quality survives the change.
- **B:** Correct. A side-by-side run on real questions is the only evidence that a cheaper model is still good enough. In this case: A side-by-side run on real cases is the evidence that quality survives the change.
- **C:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: A side-by-side run on real cases is the evidence that quality survives the change.
- **D:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: A side-by-side run on real cases is the evidence that quality survives the change.

### Question 63 — A

Answer: Provision enough quota and throughput for peak conversation volume. Provisioned throughput must cover peak concurrency, not the pilot's average. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. In this case: Provisioned throughput must cover peak concurrency, not the pilot's average.
- **B:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: Provisioned throughput must cover peak concurrency, not the pilot's average.
- **C:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Provisioned throughput must cover peak concurrency, not the pilot's average.
- **D:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Provisioned throughput must cover peak concurrency, not the pilot's average.

### Question 64 — D

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Conversation and tool telemetry in Application Insights makes the transcript reconstructable. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Conversation and tool telemetry in Application Insights makes the transcript reconstructable.
- **B:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Conversation and tool telemetry in Application Insights makes the transcript reconstructable.
- **C:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Conversation and tool telemetry in Application Insights makes the transcript reconstructable.
- **D:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Conversation and tool telemetry in Application Insights makes the transcript reconstructable.

### Question 65 — B

Answer: Query conversation and tool spans in Application Insights with KQL. A KQL query over correlated spans reconstructs that conversation's dependencies. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: A KQL query over correlated spans reconstructs that conversation's dependencies.
- **B:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: A KQL query over correlated spans reconstructs that conversation's dependencies.
- **C:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: A KQL query over correlated spans reconstructs that conversation's dependencies.
- **D:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: A KQL query over correlated spans reconstructs that conversation's dependencies.

### Question 66 — A

Answer: Sample telemetry so volume stays affordable while errors are always kept. Sampling with errors always retained controls cost and keeps rare failures visible. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sampling with errors always retained controls cost and keeps rare failures visible.
- **B:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sampling with errors always retained controls cost and keeps rare failures visible.
- **C:** Incorrect for this question. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Why the correct answer wins: Sampling with errors always retained controls cost and keeps rare failures visible.
- **D:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sampling with errors always retained controls cost and keeps rare failures visible.

### Question 67 — B, C

Answers: Alert on failed tool calls and answer-quality regressions; Correlate a failed answer with the tool call and knowledge retrieval behind it. Alerting on failed tool calls detects outages, and correlated traces explain the individual failure. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Alerting on failed tool calls detects outages, and correlated traces explain the individual failure.
- **B:** Correct. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. In this case: Alerting on failed tool calls detects outages, and correlated traces explain the individual failure.
- **C:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: Alerting on failed tool calls detects outages, and correlated traces explain the individual failure.
- **D:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Alerting on failed tool calls detects outages, and correlated traces explain the individual failure.
- **E:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Alerting on failed tool calls detects outages, and correlated traces explain the individual failure.

### Question 68 — A

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Synthetic cases read cleaner than real users, so they miss the phrasing and missing context that cause failures. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Synthetic cases read cleaner than real users, so they miss the phrasing and missing context that cause failures.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Synthetic cases read cleaner than real users, so they miss the phrasing and missing context that cause failures.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Synthetic cases read cleaner than real users, so they miss the phrasing and missing context that cause failures.
- **D:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Synthetic cases read cleaner than real users, so they miss the phrasing and missing context that cause failures.

### Question 69 — B

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and out-of-scope cases belong in the set, because that is where the agent fails visibly. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where the agent fails visibly.
- **B:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and out-of-scope cases belong in the set, because that is where the agent fails visibly.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where the agent fails visibly.
- **D:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where the agent fails visibly.

### Question 70 — B

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Questions, classification, rubric scoring, the failure log, then rerunning on change. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Questions, classification, rubric scoring, the failure log, then rerunning on change.
- **B:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Questions, classification, rubric scoring, the failure log, then rerunning on change.
- **C:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Questions, classification, rubric scoring, the failure log, then rerunning on change.
- **D:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Questions, classification, rubric scoring, the failure log, then rerunning on change.

### Question 71 — D, E

Answers: Version the test set and rerun it for every change; Hold part of the set out of prompt tuning so results stay honest. Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement.
- **D:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement.
- **E:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: Versioning makes comparisons meaningful, and a holdout prevents tuning the prompt into agreement.

### Question 72 — C

Answer: Use model-based grading against a rubric and review a human sample. Rubric-based automated grading scales, with a human sample to keep it calibrated. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Why the correct answer wins: Rubric-based automated grading scales, with a human sample to keep it calibrated.
- **B:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Rubric-based automated grading scales, with a human sample to keep it calibrated.
- **C:** Correct. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. In this case: Rubric-based automated grading scales, with a human sample to keep it calibrated.
- **D:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Rubric-based automated grading scales, with a human sample to keep it calibrated.

### Question 73 — C

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. Define the rubric, score a human sample, compare, adjust, then run the full set. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: Define the rubric, score a human sample, compare, adjust, then run the full set.
- **B:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: Define the rubric, score a human sample, compare, adjust, then run the full set.
- **C:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: Define the rubric, score a human sample, compare, adjust, then run the full set.
- **D:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: Define the rubric, score a human sample, compare, adjust, then run the full set.

### Question 74 — B

Answer: Set a pass threshold per category and block release below it. Per-category thresholds block a release that fails a high-risk path despite a strong average. Category thresholds stop a strong average from hiding a weak high-risk path. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path despite a strong average.
- **B:** Correct. Category thresholds stop a strong average from hiding a weak high-risk path. In this case: Per-category thresholds block a release that fails a high-risk path despite a strong average.
- **C:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path despite a strong average.
- **D:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path despite a strong average.

### Question 75 — A

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assign each cluster to the owner of the topic, prompt, or connector. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assign each cluster to the owner of the topic, prompt, or connector.
- **B:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **C:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **D:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.

### Question 76 — D

Answer: Keep the agent in an unmanaged solution in development and ship a managed solution. Author in an unmanaged solution and build managed versions for downstream environments. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Why the correct answer wins: Author in an unmanaged solution and build managed versions for downstream environments.
- **B:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: Author in an unmanaged solution and build managed versions for downstream environments.
- **C:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: Author in an unmanaged solution and build managed versions for downstream environments.
- **D:** Correct. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. In this case: Author in an unmanaged solution and build managed versions for downstream environments.

### Question 77 — C

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. Package, configure, export, then deploy through the pipeline. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: Package, configure, export, then deploy through the pipeline.
- **B:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: Package, configure, export, then deploy through the pipeline.
- **C:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: Package, configure, export, then deploy through the pipeline.
- **D:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: Package, configure, export, then deploy through the pipeline.

### Question 78 — D

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable holds the endpoint per environment. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **C:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **D:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable holds the endpoint per environment.

### Question 79 — A

Answer: Store the secret in a vault and reference it from the environment variable. A vault-backed environment variable keeps the secret out of the artefact and the design surface. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: A vault-backed environment variable keeps the secret out of the artefact and the design surface.
- **B:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and the design surface.
- **C:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and the design surface.
- **D:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and the design surface.

### Question 80 — B, D

Answers: Use the current value in production and a default value for development; Set the environment variable values as part of the pipeline deployment step. A current value with a default covers a simple split, and setting values during deployment removes manual edits. Current and default values cover the common two-environment split and are set explicitly per stage. Setting values during deployment removes the manual edit that people forget before a release. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: A current value with a default covers a simple split, and setting values during deployment removes manual edits.
- **B:** Correct. Current and default values cover the common two-environment split and are set explicitly per stage. In this case: A current value with a default covers a simple split, and setting values during deployment removes manual edits.
- **C:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A current value with a default covers a simple split, and setting values during deployment removes manual edits.
- **D:** Correct. Setting values during deployment removes the manual edit that people forget before a release. In this case: A current value with a default covers a simple split, and setting values during deployment removes manual edits.
- **E:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A current value with a default covers a simple split, and setting values during deployment removes manual edits.

### Question 81 — B

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment step that runs the test set and blocks on failure. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure.
- **B:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment step that runs the test set and blocks on failure.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure.
- **D:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure.

### Question 82 — D

Answer: Require approval before the production stage runs. An approval gate captures that decision with the release. An approval records who accepted the risk of the release. It must be a person who can read the test results. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: An approval gate captures that decision with the release.
- **B:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: An approval gate captures that decision with the release.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: An approval gate captures that decision with the release.
- **D:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: An approval gate captures that decision with the release.

### Question 83 — B

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. Solution, configuration, stages, test step, then the approved deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.
- **B:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: Solution, configuration, stages, test step, then the approved deployment.
- **C:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.
- **D:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.

### Question 84 — A, C

Answers: Pass environment-specific values through pipeline configuration rather than editing the solution; Keep the previous managed solution version so you can roll back. Configuration belongs with the stage, and keeping the previous version makes a rollback possible. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. In this case: Configuration belongs with the stage, and keeping the previous version makes a rollback possible.
- **B:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version makes a rollback possible.
- **C:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: Configuration belongs with the stage, and keeping the previous version makes a rollback possible.
- **D:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version makes a rollback possible.
- **E:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version makes a rollback possible.

### Question 85 — D

Answer: Deploy only the components that changed when the pipeline supports it. Deploy only the changed components to shorten the window and limit blast radius. Scoped deployment shortens the window and reduces the blast radius of a bad release. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Deploy only the changed components to shorten the window and limit blast radius.
- **B:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: Deploy only the changed components to shorten the window and limit blast radius.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Deploy only the changed components to shorten the window and limit blast radius.
- **D:** Correct. Scoped deployment shortens the window and reduces the blast radius of a bad release. In this case: Deploy only the changed components to shorten the window and limit blast radius.

### Question 86 — B

Answer: Notify the owning team with the deployment result and the failed step. A notification naming the failed stage reaches the owner immediately. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: A notification naming the failed stage reaches the owner immediately.
- **B:** Correct. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. In this case: A notification naming the failed stage reaches the owner immediately.
- **C:** Incorrect for this question. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Why the correct answer wins: A notification naming the failed stage reaches the owner immediately.
- **D:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: A notification naming the failed stage reaches the owner immediately.

### Question 87 — D

Answer: Capture user feedback in the conversation and route negative cases to review. In-conversation feedback captures the signal together with the transcript. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: In-conversation feedback captures the signal together with the transcript.
- **B:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: In-conversation feedback captures the signal together with the transcript.
- **C:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: In-conversation feedback captures the signal together with the transcript.
- **D:** Correct. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. In this case: In-conversation feedback captures the signal together with the transcript.

### Question 88 — D

Answer: Sample production conversations and score them against the rubric on a schedule. Scheduled sampling with rubric scoring measures quality over time. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Scheduled sampling with rubric scoring measures quality over time.
- **B:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Scheduled sampling with rubric scoring measures quality over time.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Scheduled sampling with rubric scoring measures quality over time.
- **D:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Scheduled sampling with rubric scoring measures quality over time.

### Question 89 — C

Answer: Turn on audit logging and retain agent conversation records. Audit logging with a defined retention period records the question and the refusal for later review. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit logging with a defined retention period records the question and the refusal for later review.
- **B:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit logging with a defined retention period records the question and the refusal for later review.
- **C:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit logging with a defined retention period records the question and the refusal for later review.
- **D:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit logging with a defined retention period records the question and the refusal for later review.

### Question 90 — A

Answer: Apply a security filter on the query before the agent composes an answer. The security filter on the query keeps unlicensed passages out of the result set entirely. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter on the query keeps unlicensed passages out of the result set entirely.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter on the query keeps unlicensed passages out of the result set entirely.
- **C:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter on the query keeps unlicensed passages out of the result set entirely.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The security filter on the query keeps unlicensed passages out of the result set entirely.

### Question 91 — B

Answer: Measure groundedness by checking each claim against the retrieved passage. Groundedness checks each claim against the retrieved passage, which is the evidence being asked for. Groundedness catches the failure that matters most in an enterprise agent: a fluent answer the source does not support. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is the evidence being asked for.
- **B:** Correct. Groundedness catches the failure that matters most in an enterprise agent: a fluent answer the source does not support. In this case: Groundedness checks each claim against the retrieved passage, which is the evidence being asked for.
- **C:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is the evidence being asked for.
- **D:** Incorrect for this question. A right answer to the wrong intent still fails the user. Separating the measures tells you which layer to fix. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is the evidence being asked for.

### Question 92 — A, D

Answers: Package the shared topics, flows, and connection references in a solution; Parameterize environment-specific values with environment variables. A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. In this case: A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact.
- **B:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact.
- **C:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact.
- **D:** Correct. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. In this case: A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact.
- **E:** Incorrect for this question. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Why the correct answer wins: A solution carries the shared behaviour, and environment variables keep plant endpoints out of the artefact.

### Question 93 — A

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge applies each engineer's existing access without creating a copy. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge applies each engineer's existing access without creating a copy.
- **B:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge applies each engineer's existing access without creating a copy.
- **C:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint knowledge applies each engineer's existing access without creating a copy.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge applies each engineer's existing access without creating a copy.

### Question 94 — B, D

Answers: Watch for knowledge-source changes and re-run the evaluation after they land; Sample production conversations and score them against the rubric on a schedule. Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest. Most answer regressions arrive with a document, not with a model change. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest.
- **B:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest.
- **C:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest.
- **D:** Correct. Most answer regressions arrive with a document, not with a model change. In this case: Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest.
- **E:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Re-running the evaluation after a revision catches source-driven regressions, and scheduled sampling catches the rest.

### Question 95 — C

Answer: Configure an alert on failed runs and route it to the owning team. An alert on failed dependency calls notifies an owner while there is still time to act. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: An alert on failed dependency calls notifies an owner while there is still time to act.
- **B:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: An alert on failed dependency calls notifies an owner while there is still time to act.
- **C:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: An alert on failed dependency calls notifies an owner while there is still time to act.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: An alert on failed dependency calls notifies an owner while there is still time to act.

### Question 96 — C

Answer: Call the API from an agent flow and return the parsed response to the topic. An agent flow can retry and transform the response before the topic reads clean values. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: An agent flow can retry and transform the response before the topic reads clean values.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: An agent flow can retry and transform the response before the topic reads clean values.
- **C:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: An agent flow can retry and transform the response before the topic reads clean values.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: An agent flow can retry and transform the response before the topic reads clean values.

### Question 97 — B

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and high-volume edge cases are where the agent fails most visibly. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and high-volume edge cases are where the agent fails most visibly.
- **B:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and high-volume edge cases are where the agent fails most visibly.
- **C:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and high-volume edge cases are where the agent fails most visibly.
- **D:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and high-volume edge cases are where the agent fails most visibly.

### Question 98 — A

Answer: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream. Entra ID sign-in lets the agent pass the student's identity so records are filtered to that person. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Entra ID sign-in lets the agent pass the student's identity so records are filtered to that person.
- **B:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Entra ID sign-in lets the agent pass the student's identity so records are filtered to that person.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Entra ID sign-in lets the agent pass the student's identity so records are filtered to that person.
- **D:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Entra ID sign-in lets the agent pass the student's identity so records are filtered to that person.

### Question 99 — D

Answer: Publish to a public website with authenticated sign-in. The website channel serves external visitors and Teams serves staff and students inside the tenant. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: The website channel serves external visitors and Teams serves staff and students inside the tenant.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: The website channel serves external visitors and Teams serves staff and students inside the tenant.
- **C:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: The website channel serves external visitors and Teams serves staff and students inside the tenant.
- **D:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: The website channel serves external visitors and Teams serves staff and students inside the tenant.

### Question 100 — D

Answer: Version the test set and rerun it for every change. A versioned set makes the two surfaces comparable and the releases comparable. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A versioned set makes the two surfaces comparable and the releases comparable.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A versioned set makes the two surfaces comparable and the releases comparable.
- **C:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: A versioned set makes the two surfaces comparable and the releases comparable.
- **D:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: A versioned set makes the two surfaces comparable and the releases comparable.
