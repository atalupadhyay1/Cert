# Microsoft AB-620 — Full-Length Mock Exam 6

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A library system runs on a server that cannot accept inbound connections from the cloud. Which integration should the plan use?

Domain: Plan and configure agent solutions

- A. Batch the requests and post them to the source system on a schedule
- B. Mirror the source into Microsoft Fabric and query it with a Fabric data agent
- C. Call the internal endpoint straight from the topic over HTTP
- D. Mediate the on-premises call through an on-premises data gateway

### 2. An admissions office needs the agent to answer from ten years of application history without loading the operational database. Which option fits?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Copy the records nightly into Dataverse and answer from the copy
- C. Mirror the source into Microsoft Fabric and query it with a Fabric data agent
- D. Expose the system through a virtual table or connector view that the agent can read

### 3. Applicants have no account in the university's tenant but must sign in before seeing their status. Which identity approach fits?

Domain: Plan and configure agent solutions

- A. Allow anonymous access to the agent and authenticate only at the API
- B. Store one API key in a topic variable and reuse it for every user
- C. Give every conversation a single shared service account credential for the API
- D. Authenticate partners through external identities rather than internal tenant accounts

### 4. Every answer to a supplier must be attributable to a named internal employee. Which identity decision delivers that?

Domain: Plan and configure agent solutions

- A. Give every conversation a single shared service account credential for the API
- B. Store one API key in a topic variable and reuse it for every user
- C. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- D. Allow anonymous access to the agent and authenticate only at the API

### 5. An agent serves internal staff and calls a portal API that must apply their own rights. Which two identity elements apply? Select two.

Domain: Plan and configure agent solutions

- A. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- B. Use the on-behalf-of flow so the agent calls the API as the signed-in user
- C. Give every conversation a single shared service account credential for the API
- D. Store one API key in a topic variable and reuse it for every user
- E. Allow anonymous access to the agent and authenticate only at the API

### 6. A transit authority wants disruption answers on its public site for all passengers. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Publish to email and answer asynchronously
- C. Publish to a public website with authenticated sign-in
- D. Embed the agent in a custom application through the Direct Line channel

### 7. Staff should reach the agent beside other agents in the Microsoft 365 Copilot experience. Which option fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents
- C. Publish to email and answer asynchronously
- D. Add the channel for omni-channel engagement so external support queues can route to it

### 8. A distributor will embed the agent in its supplier portal with the portal's own sign-in. Which channel fits?

Domain: Plan and configure agent solutions

- A. Add the channel for omni-channel engagement so external support queues can route to it
- B. Embed the agent in a custom application through the Direct Line channel
- C. Publish to email and answer asynchronously
- D. Publish to a public website with authenticated sign-in

### 9. Suppliers must only ever see their own purchase orders. What must the design enforce?

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Separate development and production environments with environment security groups
- D. Enforce the source system’s permissions in the knowledge layer so answers respect access

### 10. Sixty makers can publish to the supplier-facing agent. Which control should be tightened?

Domain: Plan and configure agent solutions

- A. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- B. Turn on audit logging and retain agent conversation records
- C. Separate development and production environments with environment security groups
- D. Restrict who can author and publish with Copilot Studio security roles

### 11. A maker added a consumer file-sharing connector to an agent that reads contracts. What blocks this at environment level?

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- C. Separate development and production environments with environment security groups
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 12. A public-facing agent reads partner documents and can call one API. Which two controls belong in the design? Select two.

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Turn on audit logging and retain agent conversation records
- C. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- E. Separate development and production environments with environment security groups

### 13. Five campus agents need the same enrolment dialogue that changes once a term. What should be built?

Domain: Plan and configure agent solutions

- A. Rebuild the same topic in each agent to avoid a shared dependency
- B. Extract the shared logic into a reusable component or child agent and reference it
- C. Parameterize environment-specific values with environment variables
- D. Copy the topics into each agent so every team can edit its own copy

### 14. A team is releasing a shared enrolment dialogue through three environments. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- B. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- C. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- D. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies

### 15. A topic must validate a request, call two systems, and return a reference number in one turn. What should be created?

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Create the flow with the connector action the agent needs and return the result
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Use an automated cloud flow triggered by an event and have the agent wait for it

### 16. A flow succeeds but the topic cannot display the result. What is missing?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Create the flow with the connector action the agent needs and return the result
- D. Define typed input and output parameters on the flow and bind them from the topic

### 17. Only one connector call is needed, with no branching. What is the lightest implementation?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Create the flow with the connector action the agent needs and return the result

### 18. A flow will be called from two topics and must never fail silently. Which two features are required? Select two.

Domain: Plan and configure agent solutions

- A. Use an automated cloud flow triggered by an event and have the agent wait for it
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- D. Define typed input and output parameters on the flow and bind them from the topic
- E. Create an agent flow with a manual trigger that the topic calls with inputs

### 19. An order above a threshold needs a supervisor's decision before it is created. What should the flow do?

Domain: Plan and configure agent solutions

- A. Send an approval request and pause the flow until a person responds
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Let the agent complete the action and notify a person afterwards

### 20. A supplier asks for a commercial exception that only a category manager may grant. What should the agent do?

Domain: Plan and configure agent solutions

- A. Hand the conversation off to a live agent with the context attached
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Let the agent complete the action and notify a person afterwards
- D. Post an adaptive card to Teams and wait for the human decision before continuing

### 21. A downstream API returns transient timeouts and users see failures. What should change?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Configure a retry policy and terminate with a failure code the topic can read
- C. Review the flow run history and its action-level inputs and outputs
- D. Use the Copilot Studio analytics view for session and topic outcomes

### 22. A builder must inspect the exact payload a failed action received this morning. Where is it recorded?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Review the flow run history and its action-level inputs and outputs
- D. Configure an alert on failed runs and route it to the owning team

### 23. A flow runs thousands of times a day across regions. Which two monitoring choices fit? Select two.

Domain: Plan and configure agent solutions

- A. Send flow telemetry to Application Insights and query the traces
- B. Add a comment step to the flow describing the expected failure
- C. Review the flow run history and its action-level inputs and outputs
- D. Use the Copilot Studio analytics view for session and topic outcomes
- E. Configure an alert on failed runs and route it to the owning team

### 24. A one-time reference code reappears in a later conversation in the same session. What should be fixed?

Domain: Plan and configure agent solutions

- A. Store the value in a global variable so later topics can read it
- B. Configure the topic as a redirect target with its own trigger phrases
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns

### 25. A 50-topic agent needs the fines dialogue separated for another team to own. What should be configured?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Store the value in a global variable so later topics can read it
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Return an adaptive card so the data renders in labelled fields

### 26. A long supplier conversation needs shared context and a structured summary. Which two choices apply? Select two.

Domain: Plan and configure agent solutions

- A. Store the value in a global variable so later topics can read it
- B. Return the raw flow output as plain text
- C. Return an adaptive card so the data renders in labelled fields
- D. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- E. Configure the message node to send a formatted message with the fields the user needs

### 27. Answers cite the right policy but ignore the required house format. What should be configured?

Domain: Plan and configure agent solutions

- A. Add a fallback topic for low-confidence answers that hands off to a person
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Require the answer to cite retrieved passages and refuse when none are found
- D. Point the generative answers node at the specific knowledge source for the question

### 28. A regulator requires the agent to refuse when no approved passage supports an answer. Which configuration enforces that?

Domain: Plan and configure agent solutions

- A. Require the answer to cite retrieved passages and refuse when none are found
- B. Point the generative answers node at the specific knowledge source for the question
- C. Add a fallback topic for low-confidence answers that hands off to a person
- D. Configure a custom prompt that fixes the tone, structure, and citation behaviour

### 29. The agent must read and update purchase orders through an operational system. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Connect through a Power Platform connector and query it from a tool or flow
- C. Upload the documents as file knowledge on the agent
- D. Connect the source through a Copilot connector so its content is indexed for answers

### 30. Supplier onboarding documents sit in SharePoint with item-level permissions that must keep applying. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Upload the documents as file knowledge on the agent
- C. Add the SharePoint site as a knowledge source and rely on item-level permissions
- D. Index the content in Azure AI Search and use it as the knowledge source

### 31. A distributor is connecting supplier onboarding documents and a purchase-order system to one agent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Review unsupported questions → test answers with users of different access → connect and scope the knowledge → inventory the sources and their permissions → choose the connector or index for each
- B. Test answers with users of different access → inventory the sources and their permissions → choose the connector or index for each → review unsupported questions → connect and scope the knowledge
- C. Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions
- D. Connect and scope the knowledge → choose the connector or index for each → inventory the sources and their permissions → test answers with users of different access → review unsupported questions

### 32. One agent answers from a document library and from a search index the team owns. Which two statements are correct? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the source through a Copilot connector so its content is indexed for answers
- B. Index the content in Azure AI Search and use it as the knowledge source
- C. Upload the documents as file knowledge on the agent
- D. Register the database as a knowledge source so the agent can query it directly
- E. Connect through a Power Platform connector and query it from a tool or flow

### 33. An index must filter by market and return a citation field. What should be designed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Connect to the search service over a private endpoint with managed identity
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Enable semantic ranking and let the agent use the reranked results

### 34. Each market must see only its own policy wording, even when copies are identical. Where must the restriction apply?

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Recreate the index on every publish so it never goes stale
- C. Apply a security filter on the query before the agent composes an answer
- D. Connect to the search service over a private endpoint with managed identity

### 35. Search by order number fails although the record is indexed. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Use hybrid retrieval with vector and keyword queries
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Enable semantic ranking and let the agent use the reranked results

### 36. A security review and a quality review raise separate search requirements. Which two settings matter? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Connect to the search service over a private endpoint with managed identity
- C. Enable semantic ranking and let the agent use the reranked results
- D. Apply a security filter on the query before the agent composes an answer
- E. Use hybrid retrieval with vector and keyword queries

### 37. A legacy customs application has no API and the agent must lodge a declaration. Which capability fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool unattended on a dedicated machine with a vaulted credential
- B. Provision a machine or machine group and run the tool there with a dedicated account
- C. Replace the screen automation with an API once the application exposes one
- D. Configure a computer use tool against the legacy desktop application

### 38. A computer use tool must run every hour without anyone logged in. What must be provisioned?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision a machine or machine group and run the tool there with a dedicated account
- B. Configure a computer use tool against the legacy desktop application
- C. Replace the screen automation with an API once the application exposes one
- D. Run the tool unattended on a dedicated machine with a vaulted credential

### 39. A team is introducing computer use for a customs application. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record
- B. Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes
- C. Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record
- D. Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes

### 40. A shared tool catalogue is extended by other teams every week. Which integration fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure the MCP server connection with the authentication the server requires
- B. Embed the MCP server as a local process inside the agent
- C. Add an MCP server as a tool and let the agent discover the tools it exposes
- D. Wrap the internal API as MCP tools and register the server endpoint with the agent

### 41. The MCP server runs in a different cluster from the hosted agent. Which transport applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Use a streamable HTTP MCP server so the agent can reach it over the network
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Embed the MCP server as a local process inside the agent
- D. Configure the MCP server connection with the authentication the server requires

### 42. MCP tools appear but every call is rejected as unauthorized. What should be fixed?

Domain: Integrate and extend agents in Copilot Studio

- A. Add an MCP server as a tool and let the agent discover the tools it exposes
- B. Configure the MCP server connection with the authentication the server requires
- C. Expose only the MCP tools the task needs and review their descriptions
- D. Use a streamable HTTP MCP server so the agent can reach it over the network

### 43. A server exposes 50 tools and the agent needs four. What should the review require?

Domain: Integrate and extend agents in Copilot Studio

- A. Wrap the internal API as MCP tools and register the server endpoint with the agent
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Expose only the MCP tools the task needs and review their descriptions
- D. Configure the MCP server connection with the authentication the server requires

### 44. The supplier portal API authenticates with one key shared by every supplier. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Configure connector authentication so each call uses the caller’s identity
- C. Create a custom connector from the OpenAPI definition and add it as a tool
- D. Call the API from an agent flow and return the parsed response to the topic

### 45. A portal response must be retried and reshaped before the agent reads it. Where should the call live?

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Define the response schema so the agent can reason over the returned fields
- C. Call the REST API from a topic with a Send HTTP request action
- D. Call the API from an agent flow and return the parsed response to the topic

### 46. A REST service must become a reusable tool with named response fields. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Call the REST API from a topic with a Send HTTP request action
- C. Define the response schema so the agent can reason over the returned fields
- D. Create a custom connector from the OpenAPI definition and add it as a tool
- E. Call the API from an agent flow and return the parsed response to the topic

### 47. One agent answers for five business functions, and every change risks unrelated behaviour. What should the architect do?

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Route by intent in the parent and pass only the context the child needs
- C. Give every child the same knowledge source so answers stay consistent
- D. Split the work into a parent agent that delegates to specialist child agents

### 48. A parent answers pricing questions itself instead of delegating to the pricing child. What should be fixed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Write the parent’s instructions to describe when each child should be used
- D. Give every child the same knowledge source so answers stay consistent

### 49. A child reports amounts in minor units while the parent expects currency. What should be agreed?

Domain: Integrate and extend agents in Copilot Studio

- A. Give every child the same knowledge source so answers stay consistent
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Route by intent in the parent and pass only the context the child needs
- D. Build one large agent with every topic so there is a single place to change

### 50. A team is decomposing a monolithic agent into a parent and children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent
- B. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- C. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions
- D. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions

### 51. A parent passes every collected field to each child even when the child needs one value. Which two changes apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Split the work into a parent agent that delegates to specialist child agents
- C. Give each child a clear input and output contract and keep shared state in the parent
- D. Build one large agent with every topic so there is a single place to change
- E. Give every child the same knowledge source so answers stay consistent

### 52. A tested Foundry agent with custom tools must answer inside Copilot Studio. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the model in Foundry and point the custom prompt at that deployment
- B. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- C. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- D. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent

### 53. A connected Foundry agent performs worse inside the parent than standalone. What was missed?

Domain: Integrate and extend agents in Copilot Studio

- A. Evaluate the Foundry agent against the same test set before it is connected
- B. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- C. Deploy the model in Foundry and point the custom prompt at that deployment
- D. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity

### 54. A Foundry agent will answer supply questions beside the Copilot Studio parent. Which two steps keep their facts aligned? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- B. Ground the Foundry agent in the same indexed knowledge so both layers answer consistently
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- E. Deploy the model in Foundry and point the custom prompt at that deployment

### 55. Two published department agents must be reused by a new parent unchanged. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Confirm the caller’s identity and permissions flow through to the connected agent
- B. Add the existing agent as a connected agent and let the parent delegate to it
- C. Write a precise name and description for the connected agent so routing works
- D. Copy its topics into the new agent so both can be edited separately

### 56. A child is republished weekly and the parent is retested monthly. What should the parent pin?

Domain: Integrate and extend agents in Copilot Studio

- A. Pin the connected agent’s published version that the parent was tested against
- B. Retire the duplicate standalone agent once the parent covers its use cases
- C. Write a precise name and description for the connected agent so routing works
- D. Add the existing agent as a connected agent and let the parent delegate to it

### 57. Store performance questions must match the measures the analysts publish. Which approach fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- B. Export the data nightly into files the agent can search
- C. Query the lakehouse directly from the agent with a SQL tool
- D. Define the measures in the semantic model so the data agent answers consistently

### 58. A data agent can read every workspace table but needs one model. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- C. Export the data nightly into files the agent can search
- D. Grant the data agent’s identity read access to the semantic model only

### 59. A partner must discover what an internal agent can do. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Track the remote task state and surface long-running results back into the conversation
- B. Publish an agent card that describes the remote agent’s skills and endpoint
- C. Configure authentication between the agents so calls are authorized
- D. Model the remote capability as an A2A skill the agent can discover and invoke

### 60. An A2A endpoint is reachable by anyone who knows the URL. What must be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure authentication between the agents so calls are authorized
- B. Model the remote capability as an A2A skill the agent can discover and invoke
- C. Track the remote task state and surface long-running results back into the conversation
- D. Publish an agent card that describes the remote agent’s skills and endpoint

### 61. Only three of nine internal skills may be exposed to a partner. What should be defined?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish an agent card that describes the remote agent’s skills and endpoint
- B. Track the remote task state and surface long-running results back into the conversation
- C. Model the remote capability as an A2A skill the agent can discover and invoke
- D. Define which remote agents are trusted and restrict the skills exposed to them

### 62. A workload must meet a quality bar, a latency target, and a budget. What should be decided first?

Domain: Integrate and extend agents in Copilot Studio

- A. Choose a model from the catalog that meets quality, latency, and residency needs
- B. Deploy the chosen model and reference the deployment from the custom prompt
- C. Provision enough quota and throughput for peak conversation volume
- D. Keep the default model because it is already configured

### 63. Data must be processed only within one country. Which decision precedes cost comparison?

Domain: Integrate and extend agents in Copilot Studio

- A. Choose a model from the catalog that meets quality, latency, and residency needs
- B. Provision enough quota and throughput for peak conversation volume
- C. Deploy the chosen model and reference the deployment from the custom prompt
- D. Deploy the model in a region that satisfies the data residency requirement

### 64. A user reports a wrong answer and there is no record of it. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Alert on failed tool calls and answer-quality regressions
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Query conversation and tool spans in Application Insights with KQL

### 65. A bad answer must be traced through retrieval and tool calls. What should be used?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Query conversation and tool spans in Application Insights with KQL
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Alert on failed tool calls and answer-quality regressions

### 66. Telemetry volume grows faster than the budget. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Log full conversation transcripts indefinitely without retention limits
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Correlate a failed answer with the tool call and knowledge retrieval behind it

### 67. An on-call engineer needs detection and root cause. Which two capabilities apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Log full conversation transcripts indefinitely without retention limits
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Correlate a failed answer with the tool call and knowledge retrieval behind it
- D. Alert on failed tool calls and answer-quality regressions
- E. Connect the agent to Application Insights and emit conversation and tool telemetry

### 68. A test set was generated only from documentation. What should be added first?

Domain: Test and manage agents

- A. Generate synthetic cases from the topics and intents the agent supports
- B. Test with a handful of happy-path questions before release
- C. Hold part of the set out of prompt tuning so results stay honest
- D. Build the test set from real anonymized conversations plus the cases that must never fail

### 69. Scores jump between releases because the set changes silently. What should be introduced?

Domain: Test and manage agents

- A. Version the test set and rerun it for every change
- B. Test with a handful of happy-path questions before release
- C. Hold part of the set out of prompt tuning so results stay honest
- D. Generate synthetic cases from the topics and intents the agent supports

### 70. A quality engineer is building the evaluation loop. Which sequence is correct?

Domain: Test and manage agents

- A. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change
- B. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change
- C. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- D. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent

### 71. A team keeps tuning until scores look good. Which two practices restore credibility? Select two.

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Test with a handful of happy-path questions before release
- D. Include adversarial and edge cases such as out-of-scope and injection attempts
- E. Build the test set from real anonymized conversations plus the cases that must never fail

### 72. A team must score 1,000 answers each week with one reviewer. Which method is practical?

Domain: Test and manage agents

- A. Score answers with keyword matching against expected phrases
- B. Use model-based grading against a rubric and review a human sample
- C. Rely on the builder trying a few questions in the test pane
- D. Have subject-matter experts score a sample against the rubric

### 73. A quality lead is calibrating an automated grader against librarian and analyst judgement. Which sequence is correct?

Domain: Test and manage agents

- A. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- B. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores
- C. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand
- D. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores

### 74. The average score is 92 percent but every safety case fails. What should the gate do?

Domain: Test and manage agents

- A. Set a pass threshold per category and block release below it
- B. Compare the new run against the previous baseline before publishing
- C. Keep failed cases in the test set so they cannot regress
- D. Publish when the overall average looks acceptable

### 75. Findings never become changes because nobody owns them. What should be introduced?

Domain: Test and manage agents

- A. Assign each failure cluster to the owner of the topic, prompt, or connector
- B. Publish when the overall average looks acceptable
- C. Keep failed cases in the test set so they cannot regress
- D. Group failures by topic and root cause instead of fixing items one at a time

### 76. Three teams will create solutions in one environment. What should be agreed first?

Domain: Test and manage agents

- A. Set the publisher prefix before creating components so names stay consistent
- B. Send the agents topic files to the administrator by email
- C. Keep the agent in an unmanaged solution in development and ship a managed solution
- D. Create a solution and add the agent and its dependencies to it

### 77. A supplier-facing agent solution is being promoted from development to test. Which sequence is correct?

Domain: Test and manage agents

- A. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- B. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- C. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- D. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies

### 78. A solution hard-codes a development endpoint that will be wrong in production. What should replace it?

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Set the environment variable values as part of the pipeline deployment step
- C. Store the secret in a vault and reference it from the environment variable
- D. Define an environment variable for the endpoint and set a value per environment

### 79. The supplier portal secret is visible inside the exported solution. Where should the value live?

Domain: Test and manage agents

- A. Record the required values in the deployment notes for each environment
- B. Use the current value in production and a default value for development
- C. Store the secret in a vault and reference it from the environment variable
- D. Hard-code the production endpoint in the topic and change it after import

### 80. A distributor runs development and test with different portal endpoints and no vault requirement. Which two practices apply? Select two.

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Use the current value in production and a default value for development
- C. Store the secret in a vault and reference it from the environment variable
- D. Record the required values in the deployment notes for each environment
- E. Set the environment variable values as part of the pipeline deployment step

### 81. A defect the test set already covered reached the supplier portal in production. What should the pipeline add?

Domain: Test and manage agents

- A. Import the solution by hand into production for each release
- B. Require approval before the production stage runs
- C. Add a pre-deployment step that runs the agent test set and blocks on failure
- D. Use the pipeline analytics to see which stage failed and why

### 82. Release policy requires a named person to accept each deployment. What should be configured?

Domain: Test and manage agents

- A. Add a pre-deployment step that runs the agent test set and blocks on failure
- B. Use the pipeline analytics to see which stage failed and why
- C. Import the solution by hand into production for each release
- D. Require approval before the production stage runs

### 83. A distributor is adding stages and a gate to its first pipeline. Which sequence is correct?

Domain: Test and manage agents

- A. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage
- B. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval
- C. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step
- D. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval

### 84. A pipeline serves five environments and the team must learn of failures fast. Which two controls apply? Select two.

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Deploy on a fixed schedule regardless of readiness
- C. Notify the owning team with the deployment result and the failed step
- D. Keep the previous managed solution version so you can roll back
- E. Pass environment-specific values through pipeline configuration rather than editing the solution

### 85. A release degrades quality and must be reversed within minutes. What should be kept?

Domain: Test and manage agents

- A. Keep the previous managed solution version so you can roll back
- B. Deploy on a fixed schedule regardless of readiness
- C. Deploy only the components that changed when the pipeline supports it
- D. Pass environment-specific values through pipeline configuration rather than editing the solution

### 86. A one-topic fix redeploys every component. What should change?

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Notify the owning team with the deployment result and the failed step
- C. Deploy on a fixed schedule regardless of readiness
- D. Pass environment-specific values through pipeline configuration rather than editing the solution

### 87. Suppliers say answers are unhelpful but no signal is recorded. What should be added?

Domain: Test and manage agents

- A. Sample production conversations and score them against the rubric on a schedule
- B. Capture user feedback in the conversation and route negative cases to review
- C. Test once before launch and assume behaviour stays stable
- D. Track containment, resolution, and escalation metrics on a dashboard

### 88. A policy revision changed answers without any deployment. Which control catches this?

Domain: Test and manage agents

- A. Test once before launch and assume behaviour stays stable
- B. Track containment, resolution, and escalation metrics on a dashboard
- C. Capture user feedback in the conversation and route negative cases to review
- D. Watch for knowledge-source changes and re-run the evaluation after they land

---

## Case study — Atlas Distribution

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A supplier must only ever see its own purchase orders and invoices. What must the design enforce?

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Separate development and production environments with environment security groups
- C. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- D. Enforce the source system’s permissions in the knowledge layer so answers respect access

### 90. The supplier portal API must apply each supplier's own access and return named fields. Which two controls apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Configure connector authentication so each call uses the caller’s identity
- C. Define the response schema so the agent can reason over the returned fields
- D. Call the REST API from a topic with a Send HTTP request action
- E. Call the API from an agent flow and return the parsed response to the topic

### 91. The agent must move through five environments. Which two packaging choices apply? Select two.

Domain: Test and manage agents

- A. Export the managed solution and import it into the target environment
- B. Create a solution and add the agent and its dependencies to it
- C. Keep the agent in an unmanaged solution in development and ship a managed solution
- D. Set the publisher prefix before creating components so names stay consistent
- E. Send the agents topic files to the administrator by email

---

## Case study — Evergreen University

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Applicants have no tenant account but must sign in to see their document status. Which identity decision fits?

Domain: Plan and configure agent solutions

- A. Authenticate partners through external identities rather than internal tenant accounts
- B. Give every conversation a single shared service account credential for the API
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Store one API key in a topic variable and reuse it for every user

### 93. Document status comes from a student information system through connector operations. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the source through a Copilot connector so its content is indexed for answers
- B. Index the content in Azure AI Search and use it as the knowledge source
- C. Connect through a Power Platform connector and query it from a tool or flow
- D. Upload the documents as file knowledge on the agent

### 94. Policy is revised twice a year, and each revision must be tested before it reaches applicants. What should the pipeline include?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Add a pre-deployment step that runs the agent test set and blocks on failure
- C. Use the pipeline analytics to see which stage failed and why
- D. Import the solution by hand into production for each release

---

## Case study — Lakeshore Library

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Forty branches share one catalogue dialogue that changes once a quarter. What should be built?

Domain: Plan and configure agent solutions

- A. Rebuild the same topic in each agent to avoid a shared dependency
- B. Extract the shared logic into a reusable component or child agent and reference it
- C. Parameterize environment-specific values with environment variables
- D. Copy the topics into each agent so every team can edit its own copy

### 96. The bibliographic index must filter by branch and return a citation. What should be designed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Enable semantic ranking and let the agent use the reranked results
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Recreate the index on every publish so it never goes stale

### 97. A branch identifier change must take effect without rebuilding the agent. What should hold that value?

Domain: Test and manage agents

- A. Define an environment variable for the endpoint and set a value per environment
- B. Hard-code the production endpoint in the topic and change it after import
- C. Store the secret in a vault and reference it from the environment variable
- D. Set the environment variable values as part of the pipeline deployment step

---

## Case study — Skyline Transit

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. The live operations feed fails several times a day and passengers see an error. What should the flow do?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Review the flow run history and its action-level inputs and outputs
- D. Configure a retry policy and terminate with a failure code the topic can read

### 99. Disruption events produce unusual questions and traffic spikes. What should the test set include?

Domain: Test and manage agents

- A. Test with a handful of happy-path questions before release
- B. Include adversarial and edge cases such as out-of-scope and injection attempts
- C. Version the test set and rerun it for every change
- D. Hold part of the set out of prompt tuning so results stay honest

### 100. When the feed is down the conversation simply stops, and the passenger is left waiting. What should the flow provide?

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- D. Define typed input and output parameters on the flow and bind them from the topic

---

## Answer key and explanations

### Question 1 — D

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway brokers the call without opening an inbound path. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **B:** Incorrect for this question. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **C:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **D:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway brokers the call without opening an inbound path.

### Question 2 — C

Answer: Mirror the source into Microsoft Fabric and query it with a Fabric data agent. Mirroring into Fabric and answering through a data agent separates analytics load from the operational system. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: Mirroring into Fabric and answering through a data agent separates analytics load from the operational system.
- **B:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: Mirroring into Fabric and answering through a data agent separates analytics load from the operational system.
- **C:** Correct. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. In this case: Mirroring into Fabric and answering through a data agent separates analytics load from the operational system.
- **D:** Incorrect for this question. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Why the correct answer wins: Mirroring into Fabric and answering through a data agent separates analytics load from the operational system.

### Question 3 — D

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities give applicants credentials without internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities give applicants credentials without internal accounts.
- **B:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: External identities give applicants credentials without internal accounts.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities give applicants credentials without internal accounts.
- **D:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities give applicants credentials without internal accounts.

### Question 4 — C

Answer: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream. Entra ID sign-in records the employee and passes that identity downstream. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Entra ID sign-in records the employee and passes that identity downstream.
- **B:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Entra ID sign-in records the employee and passes that identity downstream.
- **C:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Entra ID sign-in records the employee and passes that identity downstream.
- **D:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Entra ID sign-in records the employee and passes that identity downstream.

### Question 5 — A, B

Answers: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream; Use the on-behalf-of flow so the agent calls the API as the signed-in user. Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API.
- **B:** Correct. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. In this case: Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API.
- **D:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API.
- **E:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Tenant sign-in identifies the employee, and on-behalf-of carries that identity into the API.

### Question 6 — C

Answer: Publish to a public website with authenticated sign-in. The website channel serves an external audience without requiring tenant accounts. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: The website channel serves an external audience without requiring tenant accounts.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: The website channel serves an external audience without requiring tenant accounts.
- **C:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: The website channel serves an external audience without requiring tenant accounts.
- **D:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: The website channel serves an external audience without requiring tenant accounts.

### Question 7 — B

Answer: Publish the agent into Microsoft 365 Copilot so it appears alongside other agents. Publishing into Copilot surfaces the agent where staff already work. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.
- **B:** Correct. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. In this case: Publishing into Copilot surfaces the agent where staff already work.
- **C:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.
- **D:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.

### Question 8 — B

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line lets the host application own the interface and authentication. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Direct Line lets the host application own the interface and authentication.
- **B:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line lets the host application own the interface and authentication.
- **C:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Direct Line lets the host application own the interface and authentication.
- **D:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Direct Line lets the host application own the interface and authentication.

### Question 9 — D

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer keeps one supplier's records out of another's answers. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **B:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **D:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.

### Question 10 — D

Answer: Restrict who can author and publish with Copilot Studio security roles. Publishing rights belong to a narrow group defined through Copilot Studio security roles. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Publishing rights belong to a narrow group defined through Copilot Studio security roles.
- **B:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Publishing rights belong to a narrow group defined through Copilot Studio security roles.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Publishing rights belong to a narrow group defined through Copilot Studio security roles.
- **D:** Correct. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. In this case: Publishing rights belong to a narrow group defined through Copilot Studio security roles.

### Question 11 — D

Answer: Apply a data loss prevention policy that blocks unapproved connectors in the environment. A data loss prevention policy refuses unapproved connectors before publication. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A data loss prevention policy refuses unapproved connectors before publication.
- **B:** Incorrect for this question. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Why the correct answer wins: A data loss prevention policy refuses unapproved connectors before publication.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: A data loss prevention policy refuses unapproved connectors before publication.
- **D:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: A data loss prevention policy refuses unapproved connectors before publication.

### Question 12 — B, C

Answers: Constrain the tools the agent may call, validate tool output, and limit autonomous actions; Turn on audit logging and retain agent conversation records. Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable.
- **B:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable.
- **C:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable.
- **E:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Constraining tools and validating output limits injected instructions, and audit logging keeps every answer reviewable.

### Question 13 — B

Answer: Extract the shared logic into a reusable component or child agent and reference it. One shared component gives a single place to change the dialogue. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **B:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: One shared component gives a single place to change the dialogue.
- **C:** Incorrect for this question. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **D:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: One shared component gives a single place to change the dialogue.

### Question 14 — C

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. Package and configure, then export and promote through the pipeline. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: Package and configure, then export and promote through the pipeline.
- **B:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: Package and configure, then export and promote through the pipeline.
- **C:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: Package and configure, then export and promote through the pipeline.
- **D:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: Package and configure, then export and promote through the pipeline.

### Question 15 — A

Answer: Create an agent flow with a manual trigger that the topic calls with inputs. A manual-trigger agent flow runs on demand and returns the value. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. In this case: A manual-trigger agent flow runs on demand and returns the value.
- **B:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the value.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the value.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the value.

### Question 16 — D

Answer: Define typed input and output parameters on the flow and bind them from the topic. Typed output parameters and a topic that reads them. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **C:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **D:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed output parameters and a topic that reads them.

### Question 17 — C

Answer: Add the capability as a connector action so the agent can call it without a flow. A connector action adds the operation as a typed tool without a flow. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.
- **B:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.
- **C:** Correct. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. In this case: A connector action adds the operation as a typed tool without a flow.
- **D:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.

### Question 18 — C, D

Answers: Wrap the calls in a scope with a parallel error branch that returns a structured failure; Define typed input and output parameters on the flow and bind them from the topic. An error branch returns a failure the topic can explain, and typed parameters carry the outcome. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: An error branch returns a failure the topic can explain, and typed parameters carry the outcome.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An error branch returns a failure the topic can explain, and typed parameters carry the outcome.
- **C:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: An error branch returns a failure the topic can explain, and typed parameters carry the outcome.
- **D:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: An error branch returns a failure the topic can explain, and typed parameters carry the outcome.
- **E:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An error branch returns a failure the topic can explain, and typed parameters carry the outcome.

### Question 19 — A

Answer: Send an approval request and pause the flow until a person responds. An approval pauses the flow until a person decides, then resumes. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. In this case: An approval pauses the flow until a person decides, then resumes.
- **B:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes.
- **C:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes.
- **D:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes.

### Question 20 — A

Answer: Hand the conversation off to a live agent with the context attached. Hand the conversation to a person with its context, because the decision is discretionary. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. In this case: Hand the conversation to a person with its context, because the decision is discretionary.
- **B:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.
- **C:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.
- **D:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.

### Question 21 — B

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs the transient fault before the topic reports anything. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **B:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs the transient fault before the topic reports anything.
- **C:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **D:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.

### Question 22 — C

Answer: Review the flow run history and its action-level inputs and outputs. Run history keeps each action's inputs and outputs for that run. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Run history keeps each action's inputs and outputs for that run.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Run history keeps each action's inputs and outputs for that run.
- **C:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Run history keeps each action's inputs and outputs for that run.
- **D:** Incorrect for this question. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Why the correct answer wins: Run history keeps each action's inputs and outputs for that run.

### Question 23 — A, E

Answers: Send flow telemetry to Application Insights and query the traces; Configure an alert on failed runs and route it to the owning team. Traces in Application Insights scale, and an alert routes failures to an owner. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Traces in Application Insights scale, and an alert routes failures to an owner.
- **B:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Traces in Application Insights scale, and an alert routes failures to an owner.
- **C:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Traces in Application Insights scale, and an alert routes failures to an owner.
- **D:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Traces in Application Insights scale, and an alert routes failures to an owner.
- **E:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: Traces in Application Insights scale, and an alert routes failures to an owner.

### Question 24 — D

Answer: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns. Keep it in topic scope and clear it so it cannot leak forward. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: Keep it in topic scope and clear it so it cannot leak forward.
- **B:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: Keep it in topic scope and clear it so it cannot leak forward.
- **C:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: Keep it in topic scope and clear it so it cannot leak forward.
- **D:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: Keep it in topic scope and clear it so it cannot leak forward.

### Question 25 — A

Answer: Configure the topic as a redirect target with its own trigger phrases. A redirect topic with its own triggers keeps ownership separate. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. In this case: A redirect topic with its own triggers keeps ownership separate.
- **B:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate.
- **C:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate.
- **D:** Incorrect for this question. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate.

### Question 26 — A, C

Answers: Store the value in a global variable so later topics can read it; Return an adaptive card so the data renders in labelled fields. A global variable carries the supplier context, and an adaptive card renders the summary. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: A global variable carries the supplier context, and an adaptive card renders the summary.
- **B:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: A global variable carries the supplier context, and an adaptive card renders the summary.
- **C:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: A global variable carries the supplier context, and an adaptive card renders the summary.
- **D:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A global variable carries the supplier context, and an adaptive card renders the summary.
- **E:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A global variable carries the supplier context, and an adaptive card renders the summary.

### Question 27 — B

Answer: Configure a custom prompt that fixes the tone, structure, and citation behaviour. A custom prompt fixes structure and tone without changing the source. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: A custom prompt fixes structure and tone without changing the source.
- **B:** Correct. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. In this case: A custom prompt fixes structure and tone without changing the source.
- **C:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: A custom prompt fixes structure and tone without changing the source.
- **D:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A custom prompt fixes structure and tone without changing the source.

### Question 28 — A

Answer: Require the answer to cite retrieved passages and refuse when none are found. Requiring a citation and refusing when retrieval is empty prevents unsupported answers. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. In this case: Requiring a citation and refusing when retrieval is empty prevents unsupported answers.
- **B:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty prevents unsupported answers.
- **C:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty prevents unsupported answers.
- **D:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty prevents unsupported answers.

### Question 29 — B

Answer: Connect through a Power Platform connector and query it from a tool or flow. A Power Platform connector exposes those operations as tools. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Power Platform connector exposes those operations as tools.
- **B:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Power Platform connector exposes those operations as tools.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Power Platform connector exposes those operations as tools.
- **D:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: A Power Platform connector exposes those operations as tools.

### Question 30 — C

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge respects existing item access. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge respects existing item access.
- **B:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge respects existing item access.
- **C:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge respects existing item access.
- **D:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint knowledge respects existing item access.

### Question 31 — C

Answer: Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions. Inventory, choice, connection, access testing, then review of unsupported questions. Inventory precedes choice, choice precedes connection, and access testing follows connection. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. There is nothing to review before the knowledge is connected and tested. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.
- **B:** Incorrect for this question. Access testing requires connected sources. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.
- **C:** Correct. Inventory precedes choice, choice precedes connection, and access testing follows connection. In this case: Inventory, choice, connection, access testing, then review of unsupported questions.
- **D:** Incorrect for this question. The connector cannot be chosen before the inventory describes the sources. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.

### Question 32 — A, B

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Index the content in Azure AI Search and use it as the knowledge source. A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control.
- **B:** Correct. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. In this case: A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control.
- **E:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: A Copilot connector inherits source permissions, and an AI Search index adds filtering and ranking control.

### Question 33 — C

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema decides which fields can be filtered and returned. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **C:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema decides which fields can be filtered and returned.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema decides which fields can be filtered and returned.

### Question 34 — C

Answer: Apply a security filter on the query before the agent composes an answer. The security filter on the query keeps other markets' passages out of the results. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The security filter on the query keeps other markets' passages out of the results.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter on the query keeps other markets' passages out of the results.
- **C:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter on the query keeps other markets' passages out of the results.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter on the query keeps other markets' passages out of the results.

### Question 35 — B

Answer: Use hybrid retrieval with vector and keyword queries. Hybrid retrieval adds keyword matching for exact identifiers. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.
- **B:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Hybrid retrieval adds keyword matching for exact identifiers.
- **C:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.

### Question 36 — B, C

Answers: Enable semantic ranking and let the agent use the reranked results; Connect to the search service over a private endpoint with managed identity. Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet.
- **B:** Correct. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. In this case: Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet.
- **C:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet.
- **D:** Incorrect for this question. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Why the correct answer wins: Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet.
- **E:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: Semantic ranking improves which passage the model reads, and a private endpoint keeps traffic off the public internet.

### Question 37 — D

Answer: Configure a computer use tool against the legacy desktop application. Computer use drives the existing interface while no API exists. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Computer use drives the existing interface while no API exists.
- **B:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Computer use drives the existing interface while no API exists.
- **C:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Computer use drives the existing interface while no API exists.
- **D:** Correct. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. In this case: Computer use drives the existing interface while no API exists.

### Question 38 — A

Answer: Provision a machine or machine group and run the tool there with a dedicated account. An unattended machine with a dedicated identity is required for scheduled runs. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. In this case: An unattended machine with a dedicated identity is required for scheduled runs.
- **B:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: An unattended machine with a dedicated identity is required for scheduled runs.
- **C:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: An unattended machine with a dedicated identity is required for scheduled runs.
- **D:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: An unattended machine with a dedicated identity is required for scheduled runs.

### Question 39 — D

Answer: Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes. Confirm no API, prepare a host, record steps, run and inspect, then monitor for change. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Monitoring a tool that has never run and has no host is not possible. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **B:** Incorrect for this question. Recording happens on the prepared machine, after the API check. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **C:** Incorrect for this question. A run cannot precede the host and the recorded steps. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **D:** Correct. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. In this case: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.

### Question 40 — C

Answer: Add an MCP server as a tool and let the agent discover the tools it exposes. An MCP server exposes the catalogue for discovery without redeploying agents. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: An MCP server exposes the catalogue for discovery without redeploying agents.
- **B:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: An MCP server exposes the catalogue for discovery without redeploying agents.
- **C:** Correct. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. In this case: An MCP server exposes the catalogue for discovery without redeploying agents.
- **D:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: An MCP server exposes the catalogue for discovery without redeploying agents.

### Question 41 — A

Answer: Use a streamable HTTP MCP server so the agent can reach it over the network. Streamable HTTP reaches a remote server over the network. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: Streamable HTTP reaches a remote server over the network.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **C:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.

### Question 42 — B

Answer: Configure the MCP server connection with the authentication the server requires. Configure the connection authentication before expecting successful calls. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Configure the connection authentication before expecting successful calls.
- **B:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: Configure the connection authentication before expecting successful calls.
- **C:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: Configure the connection authentication before expecting successful calls.
- **D:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: Configure the connection authentication before expecting successful calls.

### Question 43 — C

Answer: Expose only the MCP tools the task needs and review their descriptions. Expose only the needed tools to limit what a bad instruction can reach. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.
- **C:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: Expose only the needed tools to limit what a bad instruction can reach.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.

### Question 44 — B

Answer: Configure connector authentication so each call uses the caller’s identity. Per-user authentication makes the API evaluate each caller's rights. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **B:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication makes the API evaluate each caller's rights.
- **C:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **D:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.

### Question 45 — D

Answer: Call the API from an agent flow and return the parsed response to the topic. An agent flow can retry and transform before returning clean values. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: An agent flow can retry and transform before returning clean values.
- **B:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: An agent flow can retry and transform before returning clean values.
- **C:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: An agent flow can retry and transform before returning clean values.
- **D:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: An agent flow can retry and transform before returning clean values.

### Question 46 — C, D

Answers: Create a custom connector from the OpenAPI definition and add it as a tool; Define the response schema so the agent can reason over the returned fields. A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields.
- **C:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields.
- **D:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields.
- **E:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A custom connector from OpenAPI gives typed reuse, and a declared schema lets the agent use named fields.

### Question 47 — D

Answer: Split the work into a parent agent that delegates to specialist child agents. Delegate to specialist children so each function has an owner and a release. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Delegate to specialist children so each function has an owner and a release.
- **B:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Delegate to specialist children so each function has an owner and a release.
- **C:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Delegate to specialist children so each function has an owner and a release.
- **D:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Delegate to specialist children so each function has an owner and a release.

### Question 48 — C

Answer: Write the parent’s instructions to describe when each child should be used. The parent's instructions define when each child applies, so unclear guidance is the cause. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: The parent's instructions define when each child applies, so unclear guidance is the cause.
- **B:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: The parent's instructions define when each child applies, so unclear guidance is the cause.
- **C:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: The parent's instructions define when each child applies, so unclear guidance is the cause.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: The parent's instructions define when each child applies, so unclear guidance is the cause.

### Question 49 — B

Answer: Give each child a clear input and output contract and keep shared state in the parent. An input and output contract fixes the format. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: An input and output contract fixes the format.
- **B:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: An input and output contract fixes the format.
- **C:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: An input and output contract fixes the format.
- **D:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: An input and output contract fixes the format.

### Question 50 — B

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Instructions and children, then routing tests, then tuning from the evidence. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Instructions and children, then routing tests, then tuning from the evidence.
- **B:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Instructions and children, then routing tests, then tuning from the evidence.
- **C:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Instructions and children, then routing tests, then tuning from the evidence.
- **D:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Instructions and children, then routing tests, then tuning from the evidence.

### Question 51 — A, E

Answers: Route by intent in the parent and pass only the context the child needs; Give every child the same knowledge source so answers stay consistent. Pass only the needed context, and ground every child in the same knowledge. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. In this case: Pass only the needed context, and ground every child in the same knowledge.
- **B:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Pass only the needed context, and ground every child in the same knowledge.
- **C:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Pass only the needed context, and ground every child in the same knowledge.
- **D:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Pass only the needed context, and ground every child in the same knowledge.
- **E:** Correct. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. In this case: Pass only the needed context, and ground every child in the same knowledge.

### Question 52 — D

Answer: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent. Connect it as a connected agent so the evaluated behaviour answers. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.
- **B:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.
- **C:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.
- **D:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: Connect it as a connected agent so the evaluated behaviour answers.

### Question 53 — A

Answer: Evaluate the Foundry agent against the same test set before it is connected. Evaluate it on the shared test set before connecting. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: Evaluate it on the shared test set before connecting.
- **B:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Evaluate it on the shared test set before connecting.
- **C:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Evaluate it on the shared test set before connecting.
- **D:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Evaluate it on the shared test set before connecting.

### Question 54 — B, E

Answers: Deploy the model in Foundry and point the custom prompt at that deployment; Ground the Foundry agent in the same indexed knowledge so both layers answer consistently. Reference the deployment from the prompt, and ground both layers in the same corpus. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **B:** Correct. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. In this case: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **D:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **E:** Correct. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. In this case: Reference the deployment from the prompt, and ground both layers in the same corpus.

### Question 55 — B

Answer: Add the existing agent as a connected agent and let the parent delegate to it. Add them as connected agents so their owners keep control. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Add them as connected agents so their owners keep control.
- **B:** Correct. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. In this case: Add them as connected agents so their owners keep control.
- **C:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Add them as connected agents so their owners keep control.
- **D:** Incorrect for this question. A copy forks the behaviour and doubles the maintenance from the first day. Why the correct answer wins: Add them as connected agents so their owners keep control.

### Question 56 — A

Answer: Pin the connected agent’s published version that the parent was tested against. Pinning the tested version keeps behaviour stable between retests. An unpinned dependency can change behaviour between your test run and your release. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. An unpinned dependency can change behaviour between your test run and your release. In this case: Pinning the tested version keeps behaviour stable between retests.
- **B:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.
- **C:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.
- **D:** Incorrect for this question. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.

### Question 57 — A

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the semantic model where measures live. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the semantic model where measures live.
- **B:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the semantic model where measures live.
- **C:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the semantic model where measures live.
- **D:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: A Fabric data agent answers from the semantic model where measures live.

### Question 58 — D

Answer: Grant the data agent’s identity read access to the semantic model only. Scope its read access to that model. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Scope its read access to that model.
- **B:** Incorrect for this question. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Why the correct answer wins: Scope its read access to that model.
- **C:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Scope its read access to that model.
- **D:** Correct. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. In this case: Scope its read access to that model.

### Question 59 — B

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. The agent card lists skills and the endpoint. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: The agent card lists skills and the endpoint.
- **B:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: The agent card lists skills and the endpoint.
- **C:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: The agent card lists skills and the endpoint.
- **D:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: The agent card lists skills and the endpoint.

### Question 60 — A

Answer: Configure authentication between the agents so calls are authorized. Authentication and authorisation between the agents. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. In this case: Authentication and authorisation between the agents.
- **B:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: Authentication and authorisation between the agents.
- **C:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: Authentication and authorisation between the agents.
- **D:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: Authentication and authorisation between the agents.

### Question 61 — D

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary restricts which skills are exposed. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **B:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **C:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **D:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary restricts which skills are exposed.

### Question 62 — A

Answer: Choose a model from the catalog that meets quality, latency, and residency needs. Model choice balances quality, latency, and cost. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. In this case: Model choice balances quality, latency, and cost.
- **B:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Model choice balances quality, latency, and cost.
- **C:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Model choice balances quality, latency, and cost.
- **D:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: Model choice balances quality, latency, and cost.

### Question 63 — D

Answer: Deploy the model in a region that satisfies the data residency requirement. Residency is a legal constraint, so it narrows acceptable deployments before cost or quality is compared. Residency is a legal constraint, so region choice precedes price comparison. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Residency is a legal constraint, so it narrows acceptable deployments before cost or quality is compared.
- **B:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Residency is a legal constraint, so it narrows acceptable deployments before cost or quality is compared.
- **C:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Residency is a legal constraint, so it narrows acceptable deployments before cost or quality is compared.
- **D:** Correct. Residency is a legal constraint, so region choice precedes price comparison. In this case: Residency is a legal constraint, so it narrows acceptable deployments before cost or quality is compared.

### Question 64 — C

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Conversation and tool telemetry makes the report investigable. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **C:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Conversation and tool telemetry makes the report investigable.
- **D:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.

### Question 65 — B

Answer: Query conversation and tool spans in Application Insights with KQL. A KQL query over correlated spans reconstructs the conversation. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.
- **B:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: A KQL query over correlated spans reconstructs the conversation.
- **C:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.
- **D:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.

### Question 66 — C

Answer: Sample telemetry so volume stays affordable while errors are always kept. Sample the volume and always keep errors. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sample the volume and always keep errors.
- **B:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sample the volume and always keep errors.
- **C:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sample the volume and always keep errors.
- **D:** Incorrect for this question. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Why the correct answer wins: Sample the volume and always keep errors.

### Question 67 — C, D

Answers: Alert on failed tool calls and answer-quality regressions; Correlate a failed answer with the tool call and knowledge retrieval behind it. An alert detects the failure, and correlated traces identify the dependency. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.
- **C:** Correct. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. In this case: An alert detects the failure, and correlated traces identify the dependency.
- **D:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: An alert detects the failure, and correlated traces identify the dependency.
- **E:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.

### Question 68 — D

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real anonymized conversations carry the phrasing users actually type. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real anonymized conversations carry the phrasing users actually type.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real anonymized conversations carry the phrasing users actually type.
- **C:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Real anonymized conversations carry the phrasing users actually type.
- **D:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real anonymized conversations carry the phrasing users actually type.

### Question 69 — A

Answer: Version the test set and rerun it for every change. Versioning the set keeps comparisons valid. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: Versioning the set keeps comparisons valid.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Versioning the set keeps comparisons valid.
- **C:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Versioning the set keeps comparisons valid.
- **D:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Versioning the set keeps comparisons valid.

### Question 70 — B

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Questions, classification, scoring, failure log, reruns. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Questions, classification, scoring, failure log, reruns.
- **B:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Questions, classification, scoring, failure log, reruns.
- **C:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Questions, classification, scoring, failure log, reruns.
- **D:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Questions, classification, scoring, failure log, reruns.

### Question 71 — A, D

Answers: Hold part of the set out of prompt tuning so results stay honest; Include adversarial and edge cases such as out-of-scope and injection attempts. A holdout measures honestly, and adversarial cases expose what tuning ignores. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: A holdout measures honestly, and adversarial cases expose what tuning ignores.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A holdout measures honestly, and adversarial cases expose what tuning ignores.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A holdout measures honestly, and adversarial cases expose what tuning ignores.
- **D:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: A holdout measures honestly, and adversarial cases expose what tuning ignores.
- **E:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: A holdout measures honestly, and adversarial cases expose what tuning ignores.

### Question 72 — B

Answer: Use model-based grading against a rubric and review a human sample. Automated rubric grading scales, with a human sample for calibration. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.
- **B:** Correct. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. In this case: Automated rubric grading scales, with a human sample for calibration.
- **C:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.
- **D:** Incorrect for this question. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.

### Question 73 — A

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. Rubric, human sample, comparison, adjustment, full runs. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: Rubric, human sample, comparison, adjustment, full runs.
- **B:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.
- **C:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.
- **D:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.

### Question 74 — A

Answer: Set a pass threshold per category and block release below it. Per-category thresholds block a release that fails a high-risk path. Category thresholds stop a strong average from hiding a weak high-risk path. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Category thresholds stop a strong average from hiding a weak high-risk path. In this case: Per-category thresholds block a release that fails a high-risk path.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path.
- **C:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Per-category thresholds block a release that fails a high-risk path.

### Question 75 — A

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assign each cluster to the owner of the topic, prompt, or connector. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assign each cluster to the owner of the topic, prompt, or connector.
- **B:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **C:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **D:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.

### Question 76 — A

Answer: Set the publisher prefix before creating components so names stay consistent. The publisher prefix is fixed early and prevents collisions. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. In this case: The publisher prefix is fixed early and prevents collisions.
- **B:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: The publisher prefix is fixed early and prevents collisions.
- **C:** Incorrect for this question. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. Why the correct answer wins: The publisher prefix is fixed early and prevents collisions.
- **D:** Incorrect for this question. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Why the correct answer wins: The publisher prefix is fixed early and prevents collisions.

### Question 77 — C

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution is packaged and configured before export, and the pipeline performs the deployment. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **B:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **C:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **D:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.

### Question 78 — D

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable holds the endpoint per environment. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **B:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **C:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **D:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable holds the endpoint per environment.

### Question 79 — C

Answer: Store the secret in a vault and reference it from the environment variable. A vault-backed environment variable keeps it out of the artefact. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.
- **B:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.
- **C:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: A vault-backed environment variable keeps it out of the artefact.
- **D:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.

### Question 80 — B, E

Answers: Use the current value in production and a default value for development; Set the environment variable values as part of the pipeline deployment step. A current value with a default, plus deployment-time values. Current and default values cover the common two-environment split and are set explicitly per stage. Setting values during deployment removes the manual edit that people forget before a release. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A current value with a default, plus deployment-time values.
- **B:** Correct. Current and default values cover the common two-environment split and are set explicitly per stage. In this case: A current value with a default, plus deployment-time values.
- **C:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: A current value with a default, plus deployment-time values.
- **D:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A current value with a default, plus deployment-time values.
- **E:** Correct. Setting values during deployment removes the manual edit that people forget before a release. In this case: A current value with a default, plus deployment-time values.

### Question 81 — C

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment test step that blocks on failure. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment test step that blocks on failure.
- **B:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment test step that blocks on failure.
- **C:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment test step that blocks on failure.
- **D:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment test step that blocks on failure.

### Question 82 — D

Answer: Require approval before the production stage runs. An approval gate captures the decision. An approval records who accepted the risk of the release. It must be a person who can read the test results. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: An approval gate captures the decision.
- **B:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: An approval gate captures the decision.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: An approval gate captures the decision.
- **D:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: An approval gate captures the decision.

### Question 83 — B

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. Solution, configuration, stages, test step, approved deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.
- **B:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: Solution, configuration, stages, test step, approved deployment.
- **C:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.
- **D:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.

### Question 84 — C, E

Answers: Pass environment-specific values through pipeline configuration rather than editing the solution; Notify the owning team with the deployment result and the failed step. Per-stage configuration replaces rebuilds, and a notification names the failed stage. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Per-stage configuration replaces rebuilds, and a notification names the failed stage.
- **B:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Per-stage configuration replaces rebuilds, and a notification names the failed stage.
- **C:** Correct. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. In this case: Per-stage configuration replaces rebuilds, and a notification names the failed stage.
- **D:** Incorrect for this question. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Why the correct answer wins: Per-stage configuration replaces rebuilds, and a notification names the failed stage.
- **E:** Correct. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. In this case: Per-stage configuration replaces rebuilds, and a notification names the failed stage.

### Question 85 — A

Answer: Keep the previous managed solution version so you can roll back. The previous managed version, so it can be redeployed. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: The previous managed version, so it can be redeployed.
- **B:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: The previous managed version, so it can be redeployed.
- **C:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: The previous managed version, so it can be redeployed.
- **D:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: The previous managed version, so it can be redeployed.

### Question 86 — A

Answer: Deploy only the components that changed when the pipeline supports it. Deploying only the changed components shortens the change window and limits the blast radius of a bad release. Scoped deployment shortens the window and reduces the blast radius of a bad release. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Scoped deployment shortens the window and reduces the blast radius of a bad release. In this case: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **B:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **D:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.

### Question 87 — B

Answer: Capture user feedback in the conversation and route negative cases to review. In-conversation feedback records the rating with the transcript. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: In-conversation feedback records the rating with the transcript.
- **B:** Correct. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. In this case: In-conversation feedback records the rating with the transcript.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: In-conversation feedback records the rating with the transcript.
- **D:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: In-conversation feedback records the rating with the transcript.

### Question 88 — D

Answer: Watch for knowledge-source changes and re-run the evaluation after they land. Re-run the evaluation after a knowledge change. Most answer regressions arrive with a document, not with a model change. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Re-run the evaluation after a knowledge change.
- **B:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Re-run the evaluation after a knowledge change.
- **C:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Re-run the evaluation after a knowledge change.
- **D:** Correct. Most answer regressions arrive with a document, not with a model change. In this case: Re-run the evaluation after a knowledge change.

### Question 89 — D

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer keeps one supplier's records out of another's answers. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **B:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **C:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.
- **D:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer keeps one supplier's records out of another's answers.

### Question 90 — B, C

Answers: Configure connector authentication so each call uses the caller’s identity; Define the response schema so the agent can reason over the returned fields. Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields.
- **B:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields.
- **C:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields.
- **D:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields.
- **E:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication keeps the portal honest, and a declared schema lets the agent read named fields.

### Question 91 — B, C

Answers: Create a solution and add the agent and its dependencies to it; Keep the agent in an unmanaged solution in development and ship a managed solution. The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed.
- **B:** Correct. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. In this case: The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed.
- **C:** Correct. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. In this case: The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed.
- **D:** Incorrect for this question. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Why the correct answer wins: The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed.
- **E:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: The agent and its dependencies go into a solution, which is authored unmanaged and shipped managed.

### Question 92 — A

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities give applicants their own credentials without internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities give applicants their own credentials without internal accounts.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities give applicants their own credentials without internal accounts.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities give applicants their own credentials without internal accounts.
- **D:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: External identities give applicants their own credentials without internal accounts.

### Question 93 — C

Answer: Connect through a Power Platform connector and query it from a tool or flow. A Power Platform connector exposes the operations the agent calls as tools. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: A Power Platform connector exposes the operations the agent calls as tools.
- **B:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Power Platform connector exposes the operations the agent calls as tools.
- **C:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Power Platform connector exposes the operations the agent calls as tools.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Power Platform connector exposes the operations the agent calls as tools.

### Question 94 — B

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment test step that blocks release when the set fails. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment test step that blocks release when the set fails.
- **B:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment test step that blocks release when the set fails.
- **C:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment test step that blocks release when the set fails.
- **D:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment test step that blocks release when the set fails.

### Question 95 — B

Answer: Extract the shared logic into a reusable component or child agent and reference it. One shared component gives a single place to change the dialogue. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **B:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: One shared component gives a single place to change the dialogue.
- **C:** Incorrect for this question. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **D:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: One shared component gives a single place to change the dialogue.

### Question 96 — C

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema decides which fields can be filtered and returned. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **C:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema decides which fields can be filtered and returned.
- **D:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema decides which fields can be filtered and returned.

### Question 97 — A

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable supplies the value per environment without touching the artefact. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable supplies the value per environment without touching the artefact.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable supplies the value per environment without touching the artefact.
- **C:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: An environment variable supplies the value per environment without touching the artefact.
- **D:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: An environment variable supplies the value per environment without touching the artefact.

### Question 98 — D

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs the transient failure before the topic reports anything to the passenger. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs the transient failure before the topic reports anything to the passenger.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs the transient failure before the topic reports anything to the passenger.
- **C:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs the transient failure before the topic reports anything to the passenger.
- **D:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs the transient failure before the topic reports anything to the passenger.

### Question 99 — B

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and high-volume edge cases, because that is where failures are visible. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where failures are visible.
- **B:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and high-volume edge cases, because that is where failures are visible.
- **C:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where failures are visible.
- **D:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where failures are visible.

### Question 100 — C

Answer: Wrap the calls in a scope with a parallel error branch that returns a structured failure. A retry followed by a terminate with a failure code lets the topic explain the disruption honestly. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the disruption honestly.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the disruption honestly.
- **C:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: A retry followed by a terminate with a failure code lets the topic explain the disruption honestly.
- **D:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the disruption honestly.
