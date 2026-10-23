# Microsoft AB-620 — Full-Length Mock Exam 1

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A manufacturer wants its Copilot Studio agent to read job status from an on-premises ERP that cannot accept inbound connections. What should the integration plan include?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Batch the requests and post them to the source system on a schedule
- C. Copy the records nightly into Dataverse and answer from the copy
- D. Mediate the on-premises call through an on-premises data gateway

### 2. A city agency will publish an internal agent in Teams, and auditors want every answer attributable to a named employee. Which identity approach fits?

Domain: Plan and configure agent solutions

- A. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Store one API key in a topic variable and reuse it for every user
- D. Give every conversation a single shared service account credential for the API

### 3. An agent calls a finance API that must apply the signed-in analyst's own permissions, and the API accepts OAuth tokens. Which pattern applies?

Domain: Plan and configure agent solutions

- A. Give every conversation a single shared service account credential for the API
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Use the on-behalf-of flow so the agent calls the API as the signed-in user
- D. Store one API key in a topic variable and reuse it for every user

### 4. An agent calls Azure AI Search for platform content and a business API for account records. Which identity design fits both dependencies?

Domain: Plan and configure agent solutions

- A. Store one API key in a topic variable and reuse it for every user
- B. Use the agent managed identity for Azure resources and keep user identity for business data
- C. Give every conversation a single shared service account credential for the API
- D. Allow anonymous access to the agent and authenticate only at the API

### 5. A hospital built an agent for its own clinicians only, and the identity team refuses a second sign-in. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to email and answer asynchronously
- B. Embed the agent in a custom application through the Direct Line channel
- C. Publish to Microsoft Teams and keep the agent inside the tenant
- D. Publish to a public website with authenticated sign-in

### 6. A retailer wants the agent on its public website for customers, and account answers must come only after sign-in. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to email and answer asynchronously
- B. Embed the agent in a custom application through the Direct Line channel
- C. Publish to a public website with authenticated sign-in
- D. Publish to Microsoft Teams and keep the agent inside the tenant

### 7. A software vendor wants the agent embedded in its own mobile app, keeping the app's identity and layout. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents
- B. Publish to email and answer asynchronously
- C. Publish to Microsoft Teams and keep the agent inside the tenant
- D. Embed the agent in a custom application through the Direct Line channel

### 8. An administrator finds that a maker added a personal social connector to an agent that reads HR policy. Which control addresses this at environment level?

Domain: Plan and configure agent solutions

- A. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- B. Separate development and production environments with environment security groups
- C. Turn on audit logging and retain agent conversation records
- D. Restrict who can author and publish with Copilot Studio security roles

### 9. A security reviewer asks how an agent with three tools should resist instructions embedded in a retrieved document. Which design responds?

Domain: Plan and configure agent solutions

- A. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- B. Restrict who can author and publish with Copilot Studio security roles
- C. Separate development and production environments with environment security groups
- D. Turn on audit logging and retain agent conversation records

### 10. A poisoned document may reach an agent that can also call a records system. Which two controls limit the damage? Select two.

Domain: Plan and configure agent solutions

- A. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- B. Enforce the source system’s permissions in the knowledge layer so answers respect access
- C. Turn on audit logging and retain agent conversation records
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- E. Separate development and production environments with environment security groups

### 11. Three country agents share one refund-eligibility dialogue, and a policy change must reach all three once. What should be built?

Domain: Plan and configure agent solutions

- A. Expose the shared integration as a custom connector any agent can add as a tool
- B. Extract the shared logic into a reusable component or child agent and reference it
- C. Copy the topics into each agent so every team can edit its own copy
- D. Rebuild the same topic in each agent to avoid a shared dependency

### 12. A team is packaging a shared agent component so it can move through three environments with its flows. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- B. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- C. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- D. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream

### 13. A shared dialogue is used by three agents in four environments. Which two practices stop it from drifting? Select two.

Domain: Plan and configure agent solutions

- A. Extract the shared logic into a reusable component or child agent and reference it
- B. Rebuild the same topic in each agent to avoid a shared dependency
- C. Copy the topics into each agent so every team can edit its own copy
- D. Package the shared topics, flows, and connection references in a solution
- E. Parameterize environment-specific values with environment variables

### 14. A builder must validate three fields, call two systems, and return a reference number within one conversational turn. What should be created?

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Use an automated cloud flow triggered by an event and have the agent wait for it
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Create the flow with the connector action the agent needs and return the result

### 15. An agent flow finishes successfully, but the topic cannot confirm the outcome to the user. What is missing?

Domain: Plan and configure agent solutions

- A. Add the capability as a connector action so the agent can call it without a flow
- B. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- C. Create the flow with the connector action the agent needs and return the result
- D. Define typed input and output parameters on the flow and bind them from the topic

### 16. A connector call throws an unhandled error and the user waits for an answer that never arrives. Which change keeps the conversation in control?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Use an automated cloud flow triggered by an event and have the agent wait for it
- D. Create the flow with the connector action the agent needs and return the result

### 17. A nightly reconciliation flow will be called by the agent. Which two flow features are essential before the topic depends on it? Select two.

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Use an automated cloud flow triggered by an event and have the agent wait for it
- D. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- E. Add the capability as a connector action so the agent can call it without a flow

### 18. Approvers work in Microsoft Teams and will not open another portal to release a blocked request. Which pattern delivers the decision to them?

Domain: Plan and configure agent solutions

- A. Post an adaptive card to Teams and wait for the human decision before continuing
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Let the agent complete the action and notify a person afterwards
- D. Set a response timeout and route to a fallback owner when nobody answers

### 19. An agent handling bereavement claims receives a request for a discretionary payment. Which behaviour is appropriate?

Domain: Plan and configure agent solutions

- A. Let the agent complete the action and notify a person afterwards
- B. Send an approval request and pause the flow until a person responds
- C. Have the agent draft the action and require a person to submit it in the source system
- D. Hand the conversation off to a live agent with the context attached

### 20. A service desk wants a request validated and approved by a manager before the agent confirms it. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. An approval card goes to the owning manager → the agent gathers the request → the flow validates the required fields → the agent confirms the outcome to the user → the flow resumes with the decision
- B. The agent gathers the request → the flow validates the required fields → an approval card goes to the owning manager → the flow resumes with the decision → the agent confirms the outcome to the user
- C. The agent confirms the outcome to the user → the flow resumes with the decision → the agent gathers the request → an approval card goes to the owning manager → the flow validates the required fields
- D. The flow resumes with the decision → the agent gathers the request → an approval card goes to the owning manager → the agent confirms the outcome to the user → the flow validates the required fields

### 21. A flow returned a wrong value to the conversation, and the builder wants the action that produced it. Where should they look first?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Configure an alert on failed runs and route it to the owning team
- C. Review the flow run history and its action-level inputs and outputs
- D. Use the Copilot Studio analytics view for session and topic outcomes

### 22. A dependent API returns a transient 503 once or twice a day, and users are simply told the request failed. Which change addresses it?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Configure a retry policy and terminate with a failure code the topic can read
- C. Use the Copilot Studio analytics view for session and topic outcomes
- D. Review the flow run history and its action-level inputs and outputs

### 23. An agent flow runs 4,000 times a day across three regions. Which two monitoring choices fit that volume? Select two.

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Review the flow run history and its action-level inputs and outputs
- C. Configure an alert on failed runs and route it to the owning team
- D. Send flow telemetry to Application Insights and query the traces
- E. Use the Copilot Studio analytics view for session and topic outcomes

### 24. A topic that asks for a case number offers the previous conversation's case number in the next one. What should be fixed?

Domain: Plan and configure agent solutions

- A. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- B. Store the value in a global variable so later topics can read it
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Configure the message node to send a formatted message with the fields the user needs

### 25. An answer contains six labelled values and two actions, and it must render clearly on a phone. What should the topic return?

Domain: Plan and configure agent solutions

- A. Configure the message node to send a formatted message with the fields the user needs
- B. Return an adaptive card so the data renders in labelled fields
- C. Return the raw flow output as plain text
- D. Configure the topic as a redirect target with its own trigger phrases

### 26. A conversation spans several topics that each need values from earlier steps. Which two variable practices keep the data correct? Select two.

Domain: Plan and configure agent solutions

- A. Store the value in a global variable so later topics can read it
- B. Configure the topic as a redirect target with its own trigger phrases
- C. Return the raw flow output as plain text
- D. Configure the message node to send a formatted message with the fields the user needs
- E. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns

### 27. A generative answers node returns HR policy text for a payroll question because its scope is too broad. What should change?

Domain: Plan and configure agent solutions

- A. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- B. Point the generative answers node at the specific knowledge source for the question
- C. Add a fallback topic for low-confidence answers that hands off to a person
- D. Require the answer to cite retrieved passages and refuse when none are found

### 28. Compliance requires the agent to refuse when its approved knowledge holds no answer. Which behaviour must the configuration enforce?

Domain: Plan and configure agent solutions

- A. Require the answer to cite retrieved passages and refuse when none are found
- B. Add a fallback topic for low-confidence answers that hands off to a person
- C. Point the generative answers node at the specific knowledge source for the question
- D. Configure a custom prompt that fixes the tone, structure, and citation behaviour

### 29. A legal team's policies sit in SharePoint with item-level permissions, and the agent must not become a way around them. Which knowledge route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Index the content in Azure AI Search and use it as the knowledge source
- C. Add the SharePoint site as a knowledge source and rely on item-level permissions
- D. Upload the documents as file knowledge on the agent

### 30. An organisation wants 200,000 pages of an external collaboration platform searchable by an agent with its permissions preserved, and no custom index pipeline. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect through a Power Platform connector and query it from a tool or flow
- B. Upload the documents as file knowledge on the agent
- C. Index the content in Azure AI Search and use it as the knowledge source
- D. Connect the source through a Copilot connector so its content is indexed for answers

### 31. A team must choose between a Copilot connector and an Azure AI Search index for two different corpora. Which two statements are correct? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Connect the source through a Copilot connector so its content is indexed for answers
- C. Upload the documents as file knowledge on the agent
- D. Index the content in Azure AI Search and use it as the knowledge source
- E. Connect through a Power Platform connector and query it from a tool or flow

### 32. An index serves four business units, and each must see only its own contracts. Where must the restriction be enforced?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Enable semantic ranking and let the agent use the reranked results
- C. Apply a security filter on the query before the agent composes an answer
- D. Connect to the search service over a private endpoint with managed identity

### 33. Users search by exact contract number and by description, and vector-only retrieval misses the numbers. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Create the index with the fields, vector profile, and semantic configuration the agent needs
- B. Enable semantic ranking and let the agent use the reranked results
- C. Use hybrid retrieval with vector and keyword queries
- D. Recreate the index on every publish so it never goes stale

### 34. A search team must explain a latency increase after a configuration change. Which two choices add query cost? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Connect to the search service over a private endpoint with managed identity
- C. Use hybrid retrieval with vector and keyword queries
- D. Recreate the index on every publish so it never goes stale
- E. Apply a security filter on the query before the agent composes an answer

### 35. A vendor application has no API and will not get one this year, but the agent must read asset history from it. Which capability applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool unattended on a dedicated machine with a vaulted credential
- B. Replace the screen automation with an API once the application exposes one
- C. Configure a computer use tool against the legacy desktop application
- D. Provision a machine or machine group and run the tool there with a dedicated account

### 36. A computer use tool must run every hour with nobody logged in at the console. What must be provisioned?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool unattended on a dedicated machine with a vaulted credential
- B. Configure a computer use tool against the legacy desktop application
- C. Provision a machine or machine group and run the tool there with a dedicated account
- D. Record the click path once and reuse it without validating each run

### 37. A computer use run clicked the wrong control after a vendor update, and nobody noticed for two days. Which practice would have caught it?

Domain: Integrate and extend agents in Copilot Studio

- A. Replace the screen automation with an API once the application exposes one
- B. Record the click path once and reuse it without validating each run
- C. Provision a machine or machine group and run the tool there with a dedicated account
- D. Monitor computer use runs and capture step screenshots for review

### 38. A team wants the agent to use a shared internal tool catalogue that other teams extend every week. Which integration fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Embed the MCP server as a local process inside the agent
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Configure the MCP server connection with the authentication the server requires
- D. Wrap the internal API as MCP tools and register the server endpoint with the agent

### 39. An MCP server's tools appear in the agent, but every call fails with an authorization error. What is missing?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose only the MCP tools the task needs and review their descriptions
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Use a streamable HTTP MCP server so the agent can reach it over the network
- D. Configure the MCP server connection with the authentication the server requires

### 40. A platform team is adding an MCP server to a production agent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the MCP server and configure its authentication → verify each tool call → identify the tools the agent needs → register the server with the agent → restrict the exposed tools
- B. Identify the tools the agent needs → deploy the MCP server and configure its authentication → register the server with the agent → restrict the exposed tools → verify each tool call
- C. Register the server with the agent → identify the tools the agent needs → verify each tool call → deploy the MCP server and configure its authentication → restrict the exposed tools
- D. Verify each tool call → restrict the exposed tools → identify the tools the agent needs → deploy the MCP server and configure its authentication → register the server with the agent

### 41. A review of a hosted agent's MCP integration produces three findings. Which two are correct requirements? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Use a streamable HTTP MCP server so the agent can reach it over the network
- B. Embed the MCP server as a local process inside the agent
- C. Wrap the internal API as MCP tools and register the server endpoint with the agent
- D. Configure the MCP server connection with the authentication the server requires
- E. Expose only the MCP tools the task needs and review their descriptions

### 42. An internal API publishes an OpenAPI definition and needs per-user OAuth. Which tool route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Call the API from an agent flow and return the parsed response to the topic
- B. Create a custom connector from the OpenAPI definition and add it as a tool
- C. Call the REST API from a topic with a Send HTTP request action
- D. Hard-code the endpoint URL and key inside the topic

### 43. A REST response must be reshaped and retried before the agent reads it. Where should the call live?

Domain: Integrate and extend agents in Copilot Studio

- A. Call the REST API from a topic with a Send HTTP request action
- B. Hard-code the endpoint URL and key inside the topic
- C. Define the response schema so the agent can reason over the returned fields
- D. Call the API from an agent flow and return the parsed response to the topic

### 44. A REST integration is about to be published to four business units. Which two controls must be in place? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Define the response schema so the agent can reason over the returned fields
- B. Call the REST API from a topic with a Send HTTP request action
- C. Configure connector authentication so each call uses the caller’s identity
- D. Hard-code the endpoint URL and key inside the topic
- E. Create a custom connector from the OpenAPI definition and add it as a tool

### 45. One agent now serves five departments with 60 topics and cannot be regression-tested as a whole. What should the architect do?

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Give every child the same knowledge source so answers stay consistent
- C. Split the work into a parent agent that delegates to specialist child agents
- D. Route by intent in the parent and pass only the context the child needs

### 46. A parent agent keeps answering questions that belong to a specialist child instead of delegating. What should be adjusted first?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Build one large agent with every topic so there is a single place to change
- C. Write the parent’s instructions to describe when each child should be used
- D. Give each child a clear input and output contract and keep shared state in the parent

### 47. A team is converting one large agent into a parent with three specialist children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions
- B. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- C. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent
- D. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions

### 48. A parent delegates to three children owned by different teams. Which two practices keep their answers consistent? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Give each child a clear input and output contract and keep shared state in the parent
- B. Route by intent in the parent and pass only the context the child needs
- C. Give every child the same knowledge source so answers stay consistent
- D. Build one large agent with every topic so there is a single place to change
- E. Split the work into a parent agent that delegates to specialist child agents

### 49. A team already built and evaluated an agent in Microsoft Foundry with its own tools and wants it inside the Copilot Studio conversation. What should they do?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- B. Deploy the model in Foundry and point the custom prompt at that deployment
- C. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- D. Re-implement the Foundry agent’s logic as topics in Copilot Studio

### 50. A connected Foundry agent answers worse inside the parent than it does in its own portal. What should have been done before connecting?

Domain: Integrate and extend agents in Copilot Studio

- A. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Deploy the model in Foundry and point the custom prompt at that deployment
- D. Evaluate the Foundry agent against the same test set before it is connected

### 51. Three department agents are already published and owned by their teams, and a new parent must delegate to them without forking them. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Write a precise name and description for the connected agent so routing works
- B. Add the existing agent as a connected agent and let the parent delegate to it
- C. Confirm the caller’s identity and permissions flow through to the connected agent
- D. Copy its topics into the new agent so both can be edited separately

### 52. A parent routes every billing question to the HR child agent. Which change is most likely to fix it?

Domain: Integrate and extend agents in Copilot Studio

- A. Retire the duplicate standalone agent once the parent covers its use cases
- B. Pin the connected agent’s published version that the parent was tested against
- C. Write a precise name and description for the connected agent so routing works
- D. Confirm the caller’s identity and permissions flow through to the connected agent

### 53. An auditor finds a connected agent answering from a service identity rather than the user's. What must be verified?

Domain: Integrate and extend agents in Copilot Studio

- A. Pin the connected agent’s published version that the parent was tested against
- B. Write a precise name and description for the connected agent so routing works
- C. Confirm the caller’s identity and permissions flow through to the connected agent
- D. Retire the duplicate standalone agent once the parent covers its use cases

### 54. Managers ask for revenue by region, and the figures must match the finance semantic model exactly. Which approach answers the question?

Domain: Integrate and extend agents in Copilot Studio

- A. Export the data nightly into files the agent can search
- B. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- C. Query the lakehouse directly from the agent with a SQL tool
- D. Grant the data agent’s identity read access to the semantic model only

### 55. A team is connecting a Fabric data agent to Copilot Studio. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Grant the data agent read access → create the Fabric data agent over it → model the measures in the semantic model → connect it to Copilot Studio → test the questions it must refuse
- B. Test the questions it must refuse → grant the data agent read access → connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it
- C. Connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it → test the questions it must refuse → grant the data agent read access
- D. Model the measures in the semantic model → create the Fabric data agent over it → grant the data agent read access → connect it to Copilot Studio → test the questions it must refuse

### 56. A Fabric data agent must read one semantic model and nothing else in the workspace. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Grant the data agent’s identity read access to the semantic model only
- C. Export the data nightly into files the agent can search
- D. Define the measures in the semantic model so the data agent answers consistently

### 57. Two organisations want their agents to discover each other's capabilities without a bespoke integration contract. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Model the remote capability as an A2A skill the agent can discover and invoke
- B. Rebuild the remote agent’s functionality locally instead of using the protocol
- C. Publish an agent card that describes the remote agent’s skills and endpoint
- D. Configure authentication between the agents so calls are authorized

### 58. A remote agent takes four minutes to finish, and the user is told nothing until it ends. Which part of the integration is missing?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish an agent card that describes the remote agent’s skills and endpoint
- B. Track the remote task state and surface long-running results back into the conversation
- C. Define which remote agents are trusted and restrict the skills exposed to them
- D. Configure authentication between the agents so calls are authorized

### 59. An A2A integration would let a partner agent invoke every skill on an internal agent. What should be decided before go-live?

Domain: Integrate and extend agents in Copilot Studio

- A. Rebuild the remote agent’s functionality locally instead of using the protocol
- B. Define which remote agents are trusted and restrict the skills exposed to them
- C. Model the remote capability as an A2A skill the agent can discover and invoke
- D. Publish an agent card that describes the remote agent’s skills and endpoint

### 60. A workload must run in the EU, answer within two seconds, and stay inside a fixed cost. What should the team do first?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the model in a region that satisfies the data residency requirement
- B. Keep the default model because it is already configured
- C. Provision enough quota and throughput for peak conversation volume
- D. Choose a model from the catalog that meets quality, latency, and residency needs

### 61. An agent that behaved in testing starts throttling at 300 concurrent conversations. What should be reviewed?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the chosen model and reference the deployment from the custom prompt
- B. Choose a model from the catalog that meets quality, latency, and residency needs
- C. Provision enough quota and throughput for peak conversation volume
- D. Deploy the model in a region that satisfies the data residency requirement

### 62. Users report wrong answers and the team has no record of the conversations that produced them. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Query conversation and tool spans in Application Insights with KQL
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Alert on failed tool calls and answer-quality regressions

### 63. One answer was wrong for one user at 14:32, and the team needs the retrieval and tool calls behind it. What should they use?

Domain: Integrate and extend agents in Copilot Studio

- A. Query conversation and tool spans in Application Insights with KQL
- B. Connect the agent to Application Insights and emit conversation and tool telemetry
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Alert on failed tool calls and answer-quality regressions

### 64. A monitoring budget is fixed for the year. Which two practices keep telemetry affordable and still useful? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Log full conversation transcripts indefinitely without retention limits
- B. Alert on failed tool calls and answer-quality regressions
- C. Sample telemetry so volume stays affordable while errors are always kept
- D. Connect the agent to Application Insights and emit conversation and tool telemetry
- E. Correlate a failed answer with the tool call and knowledge retrieval behind it

### 65. A team has 300 synthetic cases and no real transcripts. What is the most valuable addition to the test set?

Domain: Test and manage agents

- A. Generate synthetic cases from the topics and intents the agent supports
- B. Build the test set from real anonymized conversations plus the cases that must never fail
- C. Test with a handful of happy-path questions before release
- D. Include adversarial and edge cases such as out-of-scope and injection attempts

### 66. Reviewers ask how the agent behaves when a document instructs it to ignore its rules. Which cases cover this?

Domain: Test and manage agents

- A. Include adversarial and edge cases such as out-of-scope and injection attempts
- B. Hold part of the set out of prompt tuning so results stay honest
- C. Version the test set and rerun it for every change
- D. Test with a handful of happy-path questions before release

### 67. A team is building a reusable test set for a support agent. Which sequence is correct?

Domain: Test and manage agents

- A. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change
- B. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change
- C. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- D. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent

### 68. A test set will gate every release for a year. Which two practices keep it trustworthy? Select two.

Domain: Test and manage agents

- A. Version the test set and rerun it for every change
- B. Hold part of the set out of prompt tuning so results stay honest
- C. Test with a handful of happy-path questions before release
- D. Generate synthetic cases from the topics and intents the agent supports
- E. Build the test set from real anonymized conversations plus the cases that must never fail

### 69. A team must score 900 answers after every prompt change with two reviewers available. Which method fits?

Domain: Test and manage agents

- A. Use model-based grading against a rubric and review a human sample
- B. Rely on the builder trying a few questions in the test pane
- C. Score answers with keyword matching against expected phrases
- D. Have subject-matter experts score a sample against the rubric

### 70. A grounded agent gives fluent answers that the retrieved passage does not support. Which measure detects this?

Domain: Test and manage agents

- A. Measure topic-trigger accuracy separately from answer quality
- B. Rely on the builder trying a few questions in the test pane
- C. Measure groundedness by checking each claim against the retrieved passage
- D. Score answers with keyword matching against expected phrases

### 71. A quality lead is introducing automated grading for agent answers. Which sequence is correct?

Domain: Test and manage agents

- A. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- B. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores
- C. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand
- D. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores

### 72. A run produces 47 failures that look unrelated, and the backlog is growing. What should the team do first?

Domain: Test and manage agents

- A. Publish when the overall average looks acceptable
- B. Compare the new run against the previous baseline before publishing
- C. Group failures by topic and root cause instead of fixing items one at a time
- D. Assign each failure cluster to the owner of the topic, prompt, or connector

### 73. The average score is 91 percent, but every complaint-handling case fails. What should change in the release gate?

Domain: Test and manage agents

- A. Publish when the overall average looks acceptable
- B. Compare the new run against the previous baseline before publishing
- C. Keep failed cases in the test set so they cannot regress
- D. Set a pass threshold per category and block release below it

### 74. Failures are fixed only when someone remembers them between releases. What should be introduced?

Domain: Test and manage agents

- A. Keep failed cases in the test set so they cannot regress
- B. Compare the new run against the previous baseline before publishing
- C. Assign each failure cluster to the owner of the topic, prompt, or connector
- D. Publish when the overall average looks acceptable

### 75. A finished agent must move to another environment together with its flows and connector references. What must exist first?

Domain: Test and manage agents

- A. Export the managed solution and import it into the target environment
- B. Set the publisher prefix before creating components so names stay consistent
- C. Create a solution and add the agent and its dependencies to it
- D. Send the agents topic files to the administrator by email

### 76. A managed solution was imported into a development environment and the team cannot edit the agent. What should they author in?

Domain: Test and manage agents

- A. Send the agents topic files to the administrator by email
- B. Set the publisher prefix before creating components so names stay consistent
- C. Export the managed solution and import it into the target environment
- D. Keep the agent in an unmanaged solution in development and ship a managed solution

### 77. A connector key currently sits in a topic variable and appears in solution exports. Where should the value live?

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Use the current value in production and a default value for development
- C. Hard-code the production endpoint in the topic and change it after import
- D. Record the required values in the deployment notes for each environment

### 78. A solution will be imported into three environments with different endpoints and one shared secret. Which two practices apply? Select two.

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Hard-code the production endpoint in the topic and change it after import
- C. Record the required values in the deployment notes for each environment
- D. Define an environment variable for the endpoint and set a value per environment
- E. Use the current value in production and a default value for development

### 79. A defect that the test set already covers reached production. Which pipeline change prevents a repeat?

Domain: Test and manage agents

- A. Add a pre-deployment step that runs the agent test set and blocks on failure
- B. Use the pipeline analytics to see which stage failed and why
- C. Import the solution by hand into production for each release
- D. Require approval before the production stage runs

### 80. A release must record that a named person accepted the risk before it reaches production. What should be configured?

Domain: Test and manage agents

- A. Add a pre-deployment step that runs the agent test set and blocks on failure
- B. Use the pipeline analytics to see which stage failed and why
- C. Import the solution by hand into production for each release
- D. Require approval before the production stage runs

### 81. A team is setting up a three-stage deployment for an agent solution. Which sequence is correct?

Domain: Test and manage agents

- A. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval
- B. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval
- C. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step
- D. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage

### 82. The organisation wants its own validation job to gate every deployment. What should be added to the pipeline?

Domain: Test and manage agents

- A. Notify the owning team with the deployment result and the failed step
- B. Use the pipeline analytics to see which stage failed and why
- C. Deploy on a fixed schedule regardless of readiness
- D. Add a custom pipeline step that calls the validation job

### 83. A release degrades answer quality and the team needs the previous behaviour back within minutes. What should have been planned?

Domain: Test and manage agents

- A. Keep the previous managed solution version so you can roll back
- B. Deploy only the components that changed when the pipeline supports it
- C. Deploy on a fixed schedule regardless of readiness
- D. Notify the owning team with the deployment result and the failed step

### 84. Six weeks after launch, nobody can say whether answers are still good. What should be introduced?

Domain: Test and manage agents

- A. Track containment, resolution, and escalation metrics on a dashboard
- B. Test once before launch and assume behaviour stays stable
- C. Capture user feedback in the conversation and route negative cases to review
- D. Sample production conversations and score them against the rubric on a schedule

### 85. A knowledge library is revised twice a year by its owners. Which two controls keep answer quality stable across those revisions? Select two.

Domain: Test and manage agents

- A. Watch for knowledge-source changes and re-run the evaluation after they land
- B. Test once before launch and assume behaviour stays stable
- C. Sample production conversations and score them against the rubric on a schedule
- D. Capture user feedback in the conversation and route negative cases to review
- E. Track containment, resolution, and escalation metrics on a dashboard

### 86. A supplier-facing agent must authenticate partners who have no account in the organisation's tenant. What should the identity plan include?

Domain: Plan and configure agent solutions

- A. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- B. Give every conversation a single shared service account credential for the API
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Authenticate partners through external identities rather than internal tenant accounts

### 87. A sponsor asks whether the agent reduced escalations over the quarter. What should be presented?

Domain: Test and manage agents

- A. Alert on rising fallback and handoff rates
- B. Track containment, resolution, and escalation metrics on a dashboard
- C. Test once before launch and assume behaviour stays stable
- D. Sample production conversations and score them against the rubric on a schedule

### 88. A computer use tool must run at night with a credential no person holds. Which configuration applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Record the click path once and reuse it without validating each run
- B. Run the tool unattended on a dedicated machine with a vaulted credential
- C. Provision a machine or machine group and run the tool there with a dedicated account
- D. Replace the screen automation with an API once the application exposes one

---

## Case study — Contoso Field Service

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. The scheduling system refuses all inbound connections from the cloud. Which integration should the plan use for it?

Domain: Plan and configure agent solutions

- A. Mediate the on-premises call through an on-premises data gateway
- B. Copy the records nightly into Dataverse and answer from the copy
- C. Batch the requests and post them to the source system on a schedule
- D. Call the internal endpoint straight from the topic over HTTP

### 90. The parts service publishes an OpenAPI definition and must authorise each engineer individually. Which two steps connect it correctly? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Create a custom connector from the OpenAPI definition and add it as a tool
- B. Call the API from an agent flow and return the parsed response to the topic
- C. Configure connector authentication so each call uses the caller’s identity
- D. Hard-code the endpoint URL and key inside the topic
- E. Call the REST API from a topic with a Send HTTP request action

### 91. Development, test, and production each point at a different parts endpoint. What should carry the endpoint in the solution?

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Use the current value in production and a default value for development
- C. Record the required values in the deployment notes for each environment
- D. Define an environment variable for the endpoint and set a value per environment

---

## Case study — Fabrikam Maintenance

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Fabrikam Maintenance technicians use a Windows desktop application that will have no API this year, and the agent must read asset history from it. Which capability fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure a computer use tool against the legacy desktop application
- B. Run the tool unattended on a dedicated machine with a vaulted credential
- C. Replace the screen automation with an API once the application exposes one
- D. Provision a machine or machine group and run the tool there with a dedicated account

### 93. Approval is required before any parts order above the threshold is raised. What should the flow do?

Domain: Plan and configure agent solutions

- A. Send an approval request and pause the flow until a person responds
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Let the agent complete the action and notify a person afterwards

### 94. The desktop application sometimes takes too long to open, and the run currently ends with no message to the technician. Which change gives a usable outcome?

Domain: Plan and configure agent solutions

- A. Use the Copilot Studio analytics view for session and topic outcomes
- B. Review the flow run history and its action-level inputs and outputs
- C. Add a comment step to the flow describing the expected failure
- D. Configure a retry policy and terminate with a failure code the topic can read

---

## Case study — Meridian Claims

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Meridian Claims keeps 60,000 policy documents in SharePoint, governed by claim team membership. Which knowledge route preserves that access control?

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Index the content in Azure AI Search and use it as the knowledge source
- C. Add the SharePoint site as a knowledge source and rely on item-level permissions
- D. Upload the documents as file knowledge on the agent

### 96. Meridian needs retrieval limited to the adjuster's claim team even when two teams hold identical wording. Where must that restriction be applied?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Enable semantic ranking and let the agent use the reranked results
- C. Recreate the index on every publish so it never goes stale
- D. Apply a security filter on the query before the agent composes an answer

### 97. Meridian must score 900 answers after each prompt change and show the result before production. Which method fits?

Domain: Test and manage agents

- A. Rely on the builder trying a few questions in the test pane
- B. Use model-based grading against a rubric and review a human sample
- C. Have subject-matter experts score a sample against the rubric
- D. Score answers with keyword matching against expected phrases

---

## Case study — Northwind Commerce

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Northwind publishes the same agent to public visitors and to staff, and staff answers must respect internal permissions. What must the design enforce?

Domain: Plan and configure agent solutions

- A. Enforce the source system’s permissions in the knowledge layer so answers respect access
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Separate development and production environments with environment security groups
- D. Turn on audit logging and retain agent conversation records

### 99. The content is split across two indexed libraries and one system reachable only through connector operations. Which two routes fit? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Add the SharePoint site as a knowledge source and rely on item-level permissions
- C. Register the database as a knowledge source so the agent can query it directly
- D. Connect through a Power Platform connector and query it from a tool or flow
- E. Upload the documents as file knowledge on the agent

### 100. Northwind ships weekly, and acceptance evidence must be comparable between releases. What should be done with the test set?

Domain: Test and manage agents

- A. Generate synthetic cases from the topics and intents the agent supports
- B. Hold part of the set out of prompt tuning so results stay honest
- C. Test with a handful of happy-path questions before release
- D. Version the test set and rerun it for every change

---

## Answer key and explanations

### Question 1 — D

Answer: Mediate the on-premises call through an on-premises data gateway. A gateway brokers the call from the cloud without opening an inbound path, and the plan must budget for installing and monitoring it. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: A gateway brokers the call from the cloud without opening an inbound path, and the plan must budget for installing and monitoring it.
- **B:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: A gateway brokers the call from the cloud without opening an inbound path, and the plan must budget for installing and monitoring it.
- **C:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: A gateway brokers the call from the cloud without opening an inbound path, and the plan must budget for installing and monitoring it.
- **D:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: A gateway brokers the call from the cloud without opening an inbound path, and the plan must budget for installing and monitoring it.

### Question 2 — A

Answer: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream. Entra ID sign-in records who asked, and passing the user token lets downstream systems apply that person's permissions. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Entra ID sign-in records who asked, and passing the user token lets downstream systems apply that person's permissions.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Entra ID sign-in records who asked, and passing the user token lets downstream systems apply that person's permissions.
- **C:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Entra ID sign-in records who asked, and passing the user token lets downstream systems apply that person's permissions.
- **D:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Entra ID sign-in records who asked, and passing the user token lets downstream systems apply that person's permissions.

### Question 3 — C

Answer: Use the on-behalf-of flow so the agent calls the API as the signed-in user. The on-behalf-of flow carries the analyst identity across the service boundary so the API evaluates their rights. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: The on-behalf-of flow carries the analyst identity across the service boundary so the API evaluates their rights.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: The on-behalf-of flow carries the analyst identity across the service boundary so the API evaluates their rights.
- **C:** Correct. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. In this case: The on-behalf-of flow carries the analyst identity across the service boundary so the API evaluates their rights.
- **D:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: The on-behalf-of flow carries the analyst identity across the service boundary so the API evaluates their rights.

### Question 4 — B

Answer: Use the agent managed identity for Azure resources and keep user identity for business data. Platform resources are reached with the agent managed identity while business records are filtered by the signed-in user. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Platform resources are reached with the agent managed identity while business records are filtered by the signed-in user.
- **B:** Correct. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. In this case: Platform resources are reached with the agent managed identity while business records are filtered by the signed-in user.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Platform resources are reached with the agent managed identity while business records are filtered by the signed-in user.
- **D:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Platform resources are reached with the agent managed identity while business records are filtered by the signed-in user.

### Question 5 — C

Answer: Publish to Microsoft Teams and keep the agent inside the tenant. Teams is inside the tenant, so the agent inherits the clinicians' existing sign-in and needs no separate account. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Teams is inside the tenant, so the agent inherits the clinicians' existing sign-in and needs no separate account.
- **B:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: Teams is inside the tenant, so the agent inherits the clinicians' existing sign-in and needs no separate account.
- **C:** Correct. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. In this case: Teams is inside the tenant, so the agent inherits the clinicians' existing sign-in and needs no separate account.
- **D:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Teams is inside the tenant, so the agent inherits the clinicians' existing sign-in and needs no separate account.

### Question 6 — C

Answer: Publish to a public website with authenticated sign-in. The website channel supports an external audience while still requiring authentication before account-specific content. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: The website channel supports an external audience while still requiring authentication before account-specific content.
- **B:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: The website channel supports an external audience while still requiring authentication before account-specific content.
- **C:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: The website channel supports an external audience while still requiring authentication before account-specific content.
- **D:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: The website channel supports an external audience while still requiring authentication before account-specific content.

### Question 7 — D

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line hands the client experience and authentication to the host application, which is what an owned mobile app needs. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Why the correct answer wins: Direct Line hands the client experience and authentication to the host application, which is what an owned mobile app needs.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Direct Line hands the client experience and authentication to the host application, which is what an owned mobile app needs.
- **C:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Direct Line hands the client experience and authentication to the host application, which is what an owned mobile app needs.
- **D:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line hands the client experience and authentication to the host application, which is what an owned mobile app needs.

### Question 8 — A

Answer: Apply a data loss prevention policy that blocks unapproved connectors in the environment. A data loss prevention policy decides which connectors may be used in the environment, so the connector is blocked before publication. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: A data loss prevention policy decides which connectors may be used in the environment, so the connector is blocked before publication.
- **B:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: A data loss prevention policy decides which connectors may be used in the environment, so the connector is blocked before publication.
- **C:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A data loss prevention policy decides which connectors may be used in the environment, so the connector is blocked before publication.
- **D:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: A data loss prevention policy decides which connectors may be used in the environment, so the connector is blocked before publication.

### Question 9 — A

Answer: Constrain the tools the agent may call, validate tool output, and limit autonomous actions. Limiting tools, validating their output, and requiring approval for irreversible actions contains the blast radius of an injected instruction. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Limiting tools, validating their output, and requiring approval for irreversible actions contains the blast radius of an injected instruction.
- **B:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Limiting tools, validating their output, and requiring approval for irreversible actions contains the blast radius of an injected instruction.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Limiting tools, validating their output, and requiring approval for irreversible actions contains the blast radius of an injected instruction.
- **D:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Limiting tools, validating their output, and requiring approval for irreversible actions contains the blast radius of an injected instruction.

### Question 10 — A, B

Answers: Constrain the tools the agent may call, validate tool output, and limit autonomous actions; Enforce the source system’s permissions in the knowledge layer so answers respect access. Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting.
- **B:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting.
- **C:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting.
- **E:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Trimming content by the caller's permissions stops the leak, and constraining tools and outputs stops the injected instruction from acting.

### Question 11 — B

Answer: Extract the shared logic into a reusable component or child agent and reference it. A single shared component gives one place to change the dialogue, with a versioned dependency each country agent references. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once. Why the correct answer wins: A single shared component gives one place to change the dialogue, with a versioned dependency each country agent references.
- **B:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: A single shared component gives one place to change the dialogue, with a versioned dependency each country agent references.
- **C:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A single shared component gives one place to change the dialogue, with a versioned dependency each country agent references.
- **D:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A single shared component gives one place to change the dialogue, with a versioned dependency each country agent references.

### Question 12 — B

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. Packaging precedes configuration, configuration precedes promotion, and the pipeline runs the deployment last. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: Packaging precedes configuration, configuration precedes promotion, and the pipeline runs the deployment last.
- **B:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: Packaging precedes configuration, configuration precedes promotion, and the pipeline runs the deployment last.
- **C:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: Packaging precedes configuration, configuration precedes promotion, and the pipeline runs the deployment last.
- **D:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: Packaging precedes configuration, configuration precedes promotion, and the pipeline runs the deployment last.

### Question 13 — D, E

Answers: Package the shared topics, flows, and connection references in a solution; Parameterize environment-specific values with environment variables. A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Why the correct answer wins: A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact.
- **B:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact.
- **C:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact.
- **D:** Correct. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. In this case: A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact.
- **E:** Correct. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. In this case: A solution carries the component as one versioned unit, and environment variables keep endpoints out of the artefact.

### Question 14 — A

Answer: Create an agent flow with a manual trigger that the topic calls with inputs. A manual-trigger agent flow runs on demand from the topic and can return the reference number to the conversation. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. In this case: A manual-trigger agent flow runs on demand from the topic and can return the reference number to the conversation.
- **B:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A manual-trigger agent flow runs on demand from the topic and can return the reference number to the conversation.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A manual-trigger agent flow runs on demand from the topic and can return the reference number to the conversation.
- **D:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A manual-trigger agent flow runs on demand from the topic and can return the reference number to the conversation.

### Question 15 — D

Answer: Define typed input and output parameters on the flow and bind them from the topic. The flow needs typed output parameters the topic can read; without them there is no value to confirm. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: The flow needs typed output parameters the topic can read; without them there is no value to confirm.
- **B:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: The flow needs typed output parameters the topic can read; without them there is no value to confirm.
- **C:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: The flow needs typed output parameters the topic can read; without them there is no value to confirm.
- **D:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: The flow needs typed output parameters the topic can read; without them there is no value to confirm.

### Question 16 — A

Answer: Wrap the calls in a scope with a parallel error branch that returns a structured failure. A scope with an error branch can return a structured failure the topic turns into an honest message. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: A scope with an error branch can return a structured failure the topic turns into an honest message.
- **B:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: A scope with an error branch can return a structured failure the topic turns into an honest message.
- **C:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A scope with an error branch can return a structured failure the topic turns into an honest message.
- **D:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A scope with an error branch can return a structured failure the topic turns into an honest message.

### Question 17 — B, D

Answers: Define typed input and output parameters on the flow and bind them from the topic; Wrap the calls in a scope with a parallel error branch that returns a structured failure. Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome.
- **B:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome.
- **C:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome.
- **D:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome.
- **E:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed parameters carry values both ways, and an error branch guarantees the conversation gets a usable outcome.

### Question 18 — A

Answer: Post an adaptive card to Teams and wait for the human decision before continuing. An adaptive card in Teams puts the approval where the approver already works, and the flow waits for that decision. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. In this case: An adaptive card in Teams puts the approval where the approver already works, and the flow waits for that decision.
- **B:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: An adaptive card in Teams puts the approval where the approver already works, and the flow waits for that decision.
- **C:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: An adaptive card in Teams puts the approval where the approver already works, and the flow waits for that decision.
- **D:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: An adaptive card in Teams puts the approval where the approver already works, and the flow waits for that decision.

### Question 19 — D

Answer: Hand the conversation off to a live agent with the context attached. A discretionary judgement belongs with a person, so the conversation is handed over with its context rather than automated. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: A discretionary judgement belongs with a person, so the conversation is handed over with its context rather than automated.
- **B:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: A discretionary judgement belongs with a person, so the conversation is handed over with its context rather than automated.
- **C:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: A discretionary judgement belongs with a person, so the conversation is handed over with its context rather than automated.
- **D:** Correct. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. In this case: A discretionary judgement belongs with a person, so the conversation is handed over with its context rather than automated.

### Question 20 — B

Answer: The agent gathers the request → the flow validates the required fields → an approval card goes to the owning manager → the flow resumes with the decision → the agent confirms the outcome to the user. Gathering and validating precede the approval, and confirmation comes only after the decision returns. Gather, validate, decide, resume, confirm is the only order that keeps the human decision before the action. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Approval without a validated request asks the manager to approve nothing. Why the correct answer wins: Gathering and validating precede the approval, and confirmation comes only after the decision returns.
- **B:** Correct. Gather, validate, decide, resume, confirm is the only order that keeps the human decision before the action. In this case: Gathering and validating precede the approval, and confirmation comes only after the decision returns.
- **C:** Incorrect for this question. Confirming the outcome before the decision is made is exactly the failure mode HITL avoids. Why the correct answer wins: Gathering and validating precede the approval, and confirmation comes only after the decision returns.
- **D:** Incorrect for this question. The flow cannot resume before the request exists and has been approved. Why the correct answer wins: Gathering and validating precede the approval, and confirmation comes only after the decision returns.

### Question 21 — C

Answer: Review the flow run history and its action-level inputs and outputs. Run history records each action's inputs and outputs for that specific run, which is exactly the failing instance. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Run history records each action's inputs and outputs for that specific run, which is exactly the failing instance.
- **B:** Incorrect for this question. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Why the correct answer wins: Run history records each action's inputs and outputs for that specific run, which is exactly the failing instance.
- **C:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Run history records each action's inputs and outputs for that specific run, which is exactly the failing instance.
- **D:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Run history records each action's inputs and outputs for that specific run, which is exactly the failing instance.

### Question 22 — B

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs the transient fault, and a terminate action returns a failure code the topic can explain. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs the transient fault, and a terminate action returns a failure code the topic can explain.
- **B:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs the transient fault, and a terminate action returns a failure code the topic can explain.
- **C:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs the transient fault, and a terminate action returns a failure code the topic can explain.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs the transient fault, and a terminate action returns a failure code the topic can explain.

### Question 23 — C, D

Answers: Send flow telemetry to Application Insights and query the traces; Configure an alert on failed runs and route it to the owning team. Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking.
- **B:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking.
- **C:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking.
- **D:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking.
- **E:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Traces in Application Insights scale to that volume, and an alert on failures routes the problem to an owner without manual checking.

### Question 24 — A

Answer: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns. The value must be set and cleared inside the topic scope so a stale case number cannot survive into a later turn. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: The value must be set and cleared inside the topic scope so a stale case number cannot survive into a later turn.
- **B:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: The value must be set and cleared inside the topic scope so a stale case number cannot survive into a later turn.
- **C:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: The value must be set and cleared inside the topic scope so a stale case number cannot survive into a later turn.
- **D:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: The value must be set and cleared inside the topic scope so a stale case number cannot survive into a later turn.

### Question 25 — B

Answer: Return an adaptive card so the data renders in labelled fields. An adaptive card renders labelled fields and actions in a layout the client controls, which plain text cannot do. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: An adaptive card renders labelled fields and actions in a layout the client controls, which plain text cannot do.
- **B:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: An adaptive card renders labelled fields and actions in a layout the client controls, which plain text cannot do.
- **C:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: An adaptive card renders labelled fields and actions in a layout the client controls, which plain text cannot do.
- **D:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: An adaptive card renders labelled fields and actions in a layout the client controls, which plain text cannot do.

### Question 26 — A, E

Answers: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns; Store the value in a global variable so later topics can read it. Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns.
- **B:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns.
- **C:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns.
- **D:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns.
- **E:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: Global variables carry the account across topics, while topic-scoped values are cleared so nothing leaks between turns.

### Question 27 — B

Answer: Point the generative answers node at the specific knowledge source for the question. Pointing the node at the specific knowledge source limits the content the answer can draw from. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Pointing the node at the specific knowledge source limits the content the answer can draw from.
- **B:** Correct. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. In this case: Pointing the node at the specific knowledge source limits the content the answer can draw from.
- **C:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Pointing the node at the specific knowledge source limits the content the answer can draw from.
- **D:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: Pointing the node at the specific knowledge source limits the content the answer can draw from.

### Question 28 — A

Answer: Require the answer to cite retrieved passages and refuse when none are found. Requiring a citation from retrieved passages and refusing otherwise is what prevents a fluent unsupported answer. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. In this case: Requiring a citation from retrieved passages and refusing otherwise is what prevents a fluent unsupported answer.
- **B:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Requiring a citation from retrieved passages and refusing otherwise is what prevents a fluent unsupported answer.
- **C:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: Requiring a citation from retrieved passages and refusing otherwise is what prevents a fluent unsupported answer.
- **D:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Requiring a citation from retrieved passages and refusing otherwise is what prevents a fluent unsupported answer.

### Question 29 — C

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge honours each user's existing item access, so no copy and no second permission model is created. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge honours each user's existing item access, so no copy and no second permission model is created.
- **B:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint knowledge honours each user's existing item access, so no copy and no second permission model is created.
- **C:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge honours each user's existing item access, so no copy and no second permission model is created.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge honours each user's existing item access, so no copy and no second permission model is created.

### Question 30 — D

Answer: Connect the source through a Copilot connector so its content is indexed for answers. A Copilot connector brings the content into the Microsoft Graph index and inherits the source permission model. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: A Copilot connector brings the content into the Microsoft Graph index and inherits the source permission model.
- **B:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector brings the content into the Microsoft Graph index and inherits the source permission model.
- **C:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Copilot connector brings the content into the Microsoft Graph index and inherits the source permission model.
- **D:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector brings the content into the Microsoft Graph index and inherits the source permission model.

### Question 31 — B, D

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Index the content in Azure AI Search and use it as the knowledge source. A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking.
- **B:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking.
- **D:** Correct. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. In this case: A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking.
- **E:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: A Copilot connector indexes content with its permissions, while an AI Search index gives control over chunking, filtering, and ranking.

### Question 32 — C

Answer: Apply a security filter on the query before the agent composes an answer. The query must carry the security filter so restricted passages never enter the result set the model reads. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The query must carry the security filter so restricted passages never enter the result set the model reads.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The query must carry the security filter so restricted passages never enter the result set the model reads.
- **C:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The query must carry the security filter so restricted passages never enter the result set the model reads.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The query must carry the security filter so restricted passages never enter the result set the model reads.

### Question 33 — C

Answer: Use hybrid retrieval with vector and keyword queries. Hybrid retrieval adds keyword matching to the vector query, so exact identifiers are found alongside paraphrases. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: Hybrid retrieval adds keyword matching to the vector query, so exact identifiers are found alongside paraphrases.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: Hybrid retrieval adds keyword matching to the vector query, so exact identifiers are found alongside paraphrases.
- **C:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Hybrid retrieval adds keyword matching to the vector query, so exact identifiers are found alongside paraphrases.
- **D:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Hybrid retrieval adds keyword matching to the vector query, so exact identifiers are found alongside paraphrases.

### Question 34 — A, C

Answers: Enable semantic ranking and let the agent use the reranked results; Use hybrid retrieval with vector and keyword queries. Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase.
- **C:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase.
- **D:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase.
- **E:** Incorrect for this question. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Why the correct answer wins: Semantic ranking and hybrid retrieval both do more work per query, so either can explain the increase.

### Question 35 — C

Answer: Configure a computer use tool against the legacy desktop application. Computer use drives the existing user interface when no programmatic interface exists. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Computer use drives the existing user interface when no programmatic interface exists.
- **B:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Computer use drives the existing user interface when no programmatic interface exists.
- **C:** Correct. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. In this case: Computer use drives the existing user interface when no programmatic interface exists.
- **D:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Computer use drives the existing user interface when no programmatic interface exists.

### Question 36 — C

Answer: Provision a machine or machine group and run the tool there with a dedicated account. An unattended host with a dedicated identity is required, because an interactive desktop session cannot be relied on hourly. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: An unattended host with a dedicated identity is required, because an interactive desktop session cannot be relied on hourly.
- **B:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: An unattended host with a dedicated identity is required, because an interactive desktop session cannot be relied on hourly.
- **C:** Correct. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. In this case: An unattended host with a dedicated identity is required, because an interactive desktop session cannot be relied on hourly.
- **D:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: An unattended host with a dedicated identity is required, because an interactive desktop session cannot be relied on hourly.

### Question 37 — D

Answer: Monitor computer use runs and capture step screenshots for review. Step logs and screenshots per run expose a changed interface immediately, instead of when a user complains. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Step logs and screenshots per run expose a changed interface immediately, instead of when a user complains.
- **B:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: Step logs and screenshots per run expose a changed interface immediately, instead of when a user complains.
- **C:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Step logs and screenshots per run expose a changed interface immediately, instead of when a user complains.
- **D:** Correct. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. In this case: Step logs and screenshots per run expose a changed interface immediately, instead of when a user complains.

### Question 38 — B

Answer: Add an MCP server as a tool and let the agent discover the tools it exposes. An MCP server exposes tools that the agent discovers, so the catalogue can grow without redeploying the agent. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: An MCP server exposes tools that the agent discovers, so the catalogue can grow without redeploying the agent.
- **B:** Correct. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. In this case: An MCP server exposes tools that the agent discovers, so the catalogue can grow without redeploying the agent.
- **C:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: An MCP server exposes tools that the agent discovers, so the catalogue can grow without redeploying the agent.
- **D:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: An MCP server exposes tools that the agent discovers, so the catalogue can grow without redeploying the agent.

### Question 39 — D

Answer: Configure the MCP server connection with the authentication the server requires. The server connection needs configured authentication before any tool call can succeed. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: The server connection needs configured authentication before any tool call can succeed.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: The server connection needs configured authentication before any tool call can succeed.
- **C:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: The server connection needs configured authentication before any tool call can succeed.
- **D:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: The server connection needs configured authentication before any tool call can succeed.

### Question 40 — B

Answer: Identify the tools the agent needs → deploy the MCP server and configure its authentication → register the server with the agent → restrict the exposed tools → verify each tool call. The need defines the tools, the secured server is deployed and registered, and exposure is narrowed before verification. Need comes first, the server must exist and be secured before registration, and exposure is narrowed before verification. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Tool selection is a design decision that precedes deployment and verification. Why the correct answer wins: The need defines the tools, the secured server is deployed and registered, and exposure is narrowed before verification.
- **B:** Correct. Need comes first, the server must exist and be secured before registration, and exposure is narrowed before verification. In this case: The need defines the tools, the secured server is deployed and registered, and exposure is narrowed before verification.
- **C:** Incorrect for this question. A server cannot be registered before it is deployed and authenticated. Why the correct answer wins: The need defines the tools, the secured server is deployed and registered, and exposure is narrowed before verification.
- **D:** Incorrect for this question. Verification requires a registered server with tools already exposed. Why the correct answer wins: The need defines the tools, the secured server is deployed and registered, and exposure is narrowed before verification.

### Question 41 — A, E

Answers: Use a streamable HTTP MCP server so the agent can reach it over the network; Expose only the MCP tools the task needs and review their descriptions. A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed.
- **B:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed.
- **C:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed.
- **E:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: A remote server must be reachable over streamable HTTP, and only the tools the task needs should be exposed.

### Question 42 — B

Answer: Create a custom connector from the OpenAPI definition and add it as a tool. A custom connector built from the definition carries typed operations and a real per-user authentication model. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A custom connector built from the definition carries typed operations and a real per-user authentication model.
- **B:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector built from the definition carries typed operations and a real per-user authentication model.
- **C:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector built from the definition carries typed operations and a real per-user authentication model.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector built from the definition carries typed operations and a real per-user authentication model.

### Question 43 — D

Answer: Call the API from an agent flow and return the parsed response to the topic. An agent flow can retry, transform, and branch on errors before returning clean values to the topic. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: An agent flow can retry, transform, and branch on errors before returning clean values to the topic.
- **B:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: An agent flow can retry, transform, and branch on errors before returning clean values to the topic.
- **C:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: An agent flow can retry, transform, and branch on errors before returning clean values to the topic.
- **D:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: An agent flow can retry, transform, and branch on errors before returning clean values to the topic.

### Question 44 — A, C

Answers: Configure connector authentication so each call uses the caller’s identity; Define the response schema so the agent can reason over the returned fields. Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON.
- **C:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON.
- **E:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication keeps permissions honest, and a declared response schema lets the agent read fields instead of raw JSON.

### Question 45 — C

Answer: Split the work into a parent agent that delegates to specialist child agents. Splitting into a parent and specialist children gives each part an owner, a test set, and its own release. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Splitting into a parent and specialist children gives each part an owner, a test set, and its own release.
- **B:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Splitting into a parent and specialist children gives each part an owner, a test set, and its own release.
- **C:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Splitting into a parent and specialist children gives each part an owner, a test set, and its own release.
- **D:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Splitting into a parent and specialist children gives each part an owner, a test set, and its own release.

### Question 46 — C

Answer: Write the parent’s instructions to describe when each child should be used. Routing follows the parent's instructions, so vague descriptions of when to delegate are the first thing to fix. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Routing follows the parent's instructions, so vague descriptions of when to delegate are the first thing to fix.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Routing follows the parent's instructions, so vague descriptions of when to delegate are the first thing to fix.
- **C:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: Routing follows the parent's instructions, so vague descriptions of when to delegate are the first thing to fix.
- **D:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Routing follows the parent's instructions, so vague descriptions of when to delegate are the first thing to fix.

### Question 47 — B

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Instructions and children exist before routing is tested, and description tuning follows the evidence from that test. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Instructions and children exist before routing is tested, and description tuning follows the evidence from that test.
- **B:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Instructions and children exist before routing is tested, and description tuning follows the evidence from that test.
- **C:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Instructions and children exist before routing is tested, and description tuning follows the evidence from that test.
- **D:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Instructions and children exist before routing is tested, and description tuning follows the evidence from that test.

### Question 48 — A, C

Answers: Give each child a clear input and output contract and keep shared state in the parent; Give every child the same knowledge source so answers stay consistent. Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned.
- **B:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned.
- **C:** Correct. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. In this case: Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned.
- **D:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned.
- **E:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Explicit input and output contracts stop guessing, and one shared knowledge source keeps definitions aligned.

### Question 49 — C

Answer: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent. Connecting the published Foundry agent delegates the turn while preserving its tools, evaluation, and ownership. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Connecting the published Foundry agent delegates the turn while preserving its tools, evaluation, and ownership.
- **B:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Connecting the published Foundry agent delegates the turn while preserving its tools, evaluation, and ownership.
- **C:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: Connecting the published Foundry agent delegates the turn while preserving its tools, evaluation, and ownership.
- **D:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Connecting the published Foundry agent delegates the turn while preserving its tools, evaluation, and ownership.

### Question 50 — D

Answer: Evaluate the Foundry agent against the same test set before it is connected. The Foundry agent should have been evaluated on the same test set, so its quality and the parent's routing are separated. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: The Foundry agent should have been evaluated on the same test set, so its quality and the parent's routing are separated.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: The Foundry agent should have been evaluated on the same test set, so its quality and the parent's routing are separated.
- **C:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: The Foundry agent should have been evaluated on the same test set, so its quality and the parent's routing are separated.
- **D:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: The Foundry agent should have been evaluated on the same test set, so its quality and the parent's routing are separated.

### Question 51 — B

Answer: Add the existing agent as a connected agent and let the parent delegate to it. Adding them as connected agents reuses the published behaviour and leaves each team in control of its release. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Adding them as connected agents reuses the published behaviour and leaves each team in control of its release.
- **B:** Correct. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. In this case: Adding them as connected agents reuses the published behaviour and leaves each team in control of its release.
- **C:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Adding them as connected agents reuses the published behaviour and leaves each team in control of its release.
- **D:** Incorrect for this question. A copy forks the behaviour and doubles the maintenance from the first day. Why the correct answer wins: Adding them as connected agents reuses the published behaviour and leaves each team in control of its release.

### Question 52 — C

Answer: Write a precise name and description for the connected agent so routing works. Routing depends on the child's name and description, so a precise description of the billing agent's scope is the first fix. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Routing depends on the child's name and description, so a precise description of the billing agent's scope is the first fix.
- **B:** Incorrect for this question. An unpinned dependency can change behaviour between your test run and your release. Why the correct answer wins: Routing depends on the child's name and description, so a precise description of the billing agent's scope is the first fix.
- **C:** Correct. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. In this case: Routing depends on the child's name and description, so a precise description of the billing agent's scope is the first fix.
- **D:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Routing depends on the child's name and description, so a precise description of the billing agent's scope is the first fix.

### Question 53 — C

Answer: Confirm the caller’s identity and permissions flow through to the connected agent. Identity has to flow through the delegation, or the child answers with permissions the user never had. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An unpinned dependency can change behaviour between your test run and your release. Why the correct answer wins: Identity has to flow through the delegation, or the child answers with permissions the user never had.
- **B:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Identity has to flow through the delegation, or the child answers with permissions the user never had.
- **C:** Correct. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. In this case: Identity has to flow through the delegation, or the child answers with permissions the user never had.
- **D:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Identity has to flow through the delegation, or the child answers with permissions the user never had.

### Question 54 — B

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the governed semantic model, so the measures stay the ones finance defined. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the governed semantic model, so the measures stay the ones finance defined.
- **B:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the governed semantic model, so the measures stay the ones finance defined.
- **C:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the governed semantic model, so the measures stay the ones finance defined.
- **D:** Incorrect for this question. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Why the correct answer wins: A Fabric data agent answers from the governed semantic model, so the measures stay the ones finance defined.

### Question 55 — D

Answer: Model the measures in the semantic model → create the Fabric data agent over it → grant the data agent read access → connect it to Copilot Studio → test the questions it must refuse. Measures precede the agent, permissions precede connection, and boundary testing comes last. Measures precede the agent, permissions precede connection, and boundary testing comes last. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Access is granted to an agent that must already exist over a modelled source. Why the correct answer wins: Measures precede the agent, permissions precede connection, and boundary testing comes last.
- **B:** Incorrect for this question. Nothing can be tested before the agent exists and is connected. Why the correct answer wins: Measures precede the agent, permissions precede connection, and boundary testing comes last.
- **C:** Incorrect for this question. Connection without permissions produces an agent that cannot read its own model. Why the correct answer wins: Measures precede the agent, permissions precede connection, and boundary testing comes last.
- **D:** Correct. Measures precede the agent, permissions precede connection, and boundary testing comes last. In this case: Measures precede the agent, permissions precede connection, and boundary testing comes last.

### Question 56 — B

Answer: Grant the data agent’s identity read access to the semantic model only. Read access scoped to that model gives the agent what it needs without exposing unrelated workspace content. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Read access scoped to that model gives the agent what it needs without exposing unrelated workspace content.
- **B:** Correct. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. In this case: Read access scoped to that model gives the agent what it needs without exposing unrelated workspace content.
- **C:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Read access scoped to that model gives the agent what it needs without exposing unrelated workspace content.
- **D:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: Read access scoped to that model gives the agent what it needs without exposing unrelated workspace content.

### Question 57 — C

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. An agent card advertises the remote agent's skills and endpoint so the caller can discover them at runtime. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: An agent card advertises the remote agent's skills and endpoint so the caller can discover them at runtime.
- **B:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: An agent card advertises the remote agent's skills and endpoint so the caller can discover them at runtime.
- **C:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: An agent card advertises the remote agent's skills and endpoint so the caller can discover them at runtime.
- **D:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: An agent card advertises the remote agent's skills and endpoint so the caller can discover them at runtime.

### Question 58 — B

Answer: Track the remote task state and surface long-running results back into the conversation. A2A tasks outlive a single call, so state tracking is needed to surface progress and the final result. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A2A tasks outlive a single call, so state tracking is needed to surface progress and the final result.
- **B:** Correct. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. In this case: A2A tasks outlive a single call, so state tracking is needed to surface progress and the final result.
- **C:** Incorrect for this question. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Why the correct answer wins: A2A tasks outlive a single call, so state tracking is needed to surface progress and the final result.
- **D:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A2A tasks outlive a single call, so state tracking is needed to surface progress and the final result.

### Question 59 — B

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary decides which remote agents may call which skills, so a partner cannot act as an insider. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: A trust boundary decides which remote agents may call which skills, so a partner cannot act as an insider.
- **B:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary decides which remote agents may call which skills, so a partner cannot act as an insider.
- **C:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: A trust boundary decides which remote agents may call which skills, so a partner cannot act as an insider.
- **D:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary decides which remote agents may call which skills, so a partner cannot act as an insider.

### Question 60 — D

Answer: Choose a model from the catalog that meets quality, latency, and residency needs. Model choice is the first decision, because quality, latency, cost, and residency all narrow the catalogue. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: Model choice is the first decision, because quality, latency, cost, and residency all narrow the catalogue.
- **B:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: Model choice is the first decision, because quality, latency, cost, and residency all narrow the catalogue.
- **C:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Model choice is the first decision, because quality, latency, cost, and residency all narrow the catalogue.
- **D:** Correct. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. In this case: Model choice is the first decision, because quality, latency, cost, and residency all narrow the catalogue.

### Question 61 — C

Answer: Provision enough quota and throughput for peak conversation volume. Provisioned quota and throughput must be sized for peak concurrency, not for the test load. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Provisioned quota and throughput must be sized for peak concurrency, not for the test load.
- **B:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Provisioned quota and throughput must be sized for peak concurrency, not for the test load.
- **C:** Correct. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. In this case: Provisioned quota and throughput must be sized for peak concurrency, not for the test load.
- **D:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: Provisioned quota and throughput must be sized for peak concurrency, not for the test load.

### Question 62 — A

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Connecting Application Insights gives conversation and tool telemetry, which is the evidence everything else depends on. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Connecting Application Insights gives conversation and tool telemetry, which is the evidence everything else depends on.
- **B:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Connecting Application Insights gives conversation and tool telemetry, which is the evidence everything else depends on.
- **C:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Connecting Application Insights gives conversation and tool telemetry, which is the evidence everything else depends on.
- **D:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Connecting Application Insights gives conversation and tool telemetry, which is the evidence everything else depends on.

### Question 63 — A

Answer: Query conversation and tool spans in Application Insights with KQL. A KQL query over the correlated spans reconstructs that single conversation and its dependencies. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: A KQL query over the correlated spans reconstructs that single conversation and its dependencies.
- **B:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: A KQL query over the correlated spans reconstructs that single conversation and its dependencies.
- **C:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: A KQL query over the correlated spans reconstructs that single conversation and its dependencies.
- **D:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: A KQL query over the correlated spans reconstructs that single conversation and its dependencies.

### Question 64 — B, C

Answers: Sample telemetry so volume stays affordable while errors are always kept; Alert on failed tool calls and answer-quality regressions. Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action.
- **B:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action.
- **C:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action.
- **D:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action.
- **E:** Incorrect for this question. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Why the correct answer wins: Sampling with errors always kept controls cost, and an alert on failed calls turns the data into action.

### Question 65 — B

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real anonymized conversations carry the phrasing and missing context that synthetic cases smooth away. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real anonymized conversations carry the phrasing and missing context that synthetic cases smooth away.
- **B:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real anonymized conversations carry the phrasing and missing context that synthetic cases smooth away.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real anonymized conversations carry the phrasing and missing context that synthetic cases smooth away.
- **D:** Incorrect for this question. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Why the correct answer wins: Real anonymized conversations carry the phrasing and missing context that synthetic cases smooth away.

### Question 66 — A

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and out-of-scope cases belong in the set, because that is where failures are most visible. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and out-of-scope cases belong in the set, because that is where failures are most visible.
- **B:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where failures are most visible.
- **C:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where failures are most visible.
- **D:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set, because that is where failures are most visible.

### Question 67 — A

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning on change. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning on change.
- **B:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning on change.
- **C:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning on change.
- **D:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning on change.

### Question 68 — A, B

Answers: Hold part of the set out of prompt tuning so results stay honest; Version the test set and rerun it for every change. A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases.
- **B:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases.
- **D:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases.
- **E:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: A held-out slice stops overfitting during tuning, and versioning keeps comparisons meaningful across releases.

### Question 69 — A

Answer: Use model-based grading against a rubric and review a human sample. Model-based grading against a rubric scales to 900 cases, with a human sample to keep the grader calibrated. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. In this case: Model-based grading against a rubric scales to 900 cases, with a human sample to keep the grader calibrated.
- **B:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Model-based grading against a rubric scales to 900 cases, with a human sample to keep the grader calibrated.
- **C:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Model-based grading against a rubric scales to 900 cases, with a human sample to keep the grader calibrated.
- **D:** Incorrect for this question. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Why the correct answer wins: Model-based grading against a rubric scales to 900 cases, with a human sample to keep the grader calibrated.

### Question 70 — C

Answer: Measure groundedness by checking each claim against the retrieved passage. Groundedness checks each claim against the retrieved passage, which is exactly the failure being described. Groundedness catches the failure that matters most in an enterprise agent: a fluent answer the source does not support. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A right answer to the wrong intent still fails the user. Separating the measures tells you which layer to fix. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is exactly the failure being described.
- **B:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is exactly the failure being described.
- **C:** Correct. Groundedness catches the failure that matters most in an enterprise agent: a fluent answer the source does not support. In this case: Groundedness checks each claim against the retrieved passage, which is exactly the failure being described.
- **D:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Groundedness checks each claim against the retrieved passage, which is exactly the failure being described.

### Question 71 — A

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. The rubric comes first, the human sample calibrates the grader, and full runs follow calibration. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: The rubric comes first, the human sample calibrates the grader, and full runs follow calibration.
- **B:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: The rubric comes first, the human sample calibrates the grader, and full runs follow calibration.
- **C:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: The rubric comes first, the human sample calibrates the grader, and full runs follow calibration.
- **D:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: The rubric comes first, the human sample calibrates the grader, and full runs follow calibration.

### Question 72 — C

Answer: Group failures by topic and root cause instead of fixing items one at a time. Grouping by topic and root cause turns symptoms into a short list of causes that can be fixed and owned. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Grouping by topic and root cause turns symptoms into a short list of causes that can be fixed and owned.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Grouping by topic and root cause turns symptoms into a short list of causes that can be fixed and owned.
- **C:** Correct. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. In this case: Grouping by topic and root cause turns symptoms into a short list of causes that can be fixed and owned.
- **D:** Incorrect for this question. Ownership converts findings into changes. An unowned backlog does not improve the agent. Why the correct answer wins: Grouping by topic and root cause turns symptoms into a short list of causes that can be fixed and owned.

### Question 73 — D

Answer: Set a pass threshold per category and block release below it. Per-category thresholds stop a strong average from hiding a weak high-risk path. Category thresholds stop a strong average from hiding a weak high-risk path. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Per-category thresholds stop a strong average from hiding a weak high-risk path.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Per-category thresholds stop a strong average from hiding a weak high-risk path.
- **C:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Per-category thresholds stop a strong average from hiding a weak high-risk path.
- **D:** Correct. Category thresholds stop a strong average from hiding a weak high-risk path. In this case: Per-category thresholds stop a strong average from hiding a weak high-risk path.

### Question 74 — C

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assigning each failure cluster to the owner of the topic, prompt, or connector makes the fixes part of normal work. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assigning each failure cluster to the owner of the topic, prompt, or connector makes the fixes part of normal work.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Assigning each failure cluster to the owner of the topic, prompt, or connector makes the fixes part of normal work.
- **C:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assigning each failure cluster to the owner of the topic, prompt, or connector makes the fixes part of normal work.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assigning each failure cluster to the owner of the topic, prompt, or connector makes the fixes part of normal work.

### Question 75 — C

Answer: Create a solution and add the agent and its dependencies to it. Only solution-aware components can be exported and imported as a unit, so the agent and its dependencies go into a solution. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: Only solution-aware components can be exported and imported as a unit, so the agent and its dependencies go into a solution.
- **B:** Incorrect for this question. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Why the correct answer wins: Only solution-aware components can be exported and imported as a unit, so the agent and its dependencies go into a solution.
- **C:** Correct. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. In this case: Only solution-aware components can be exported and imported as a unit, so the agent and its dependencies go into a solution.
- **D:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: Only solution-aware components can be exported and imported as a unit, so the agent and its dependencies go into a solution.

### Question 76 — D

Answer: Keep the agent in an unmanaged solution in development and ship a managed solution. Authoring happens in an unmanaged solution, and the managed build is produced for downstream environments. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: Authoring happens in an unmanaged solution, and the managed build is produced for downstream environments.
- **B:** Incorrect for this question. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Why the correct answer wins: Authoring happens in an unmanaged solution, and the managed build is produced for downstream environments.
- **C:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: Authoring happens in an unmanaged solution, and the managed build is produced for downstream environments.
- **D:** Correct. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. In this case: Authoring happens in an unmanaged solution, and the managed build is produced for downstream environments.

### Question 77 — A

Answer: Store the secret in a vault and reference it from the environment variable. A vault-backed environment variable keeps the secret out of the artefact and out of every design surface. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: A vault-backed environment variable keeps the secret out of the artefact and out of every design surface.
- **B:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and out of every design surface.
- **C:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and out of every design surface.
- **D:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the artefact and out of every design surface.

### Question 78 — A, D

Answers: Store the secret in a vault and reference it from the environment variable; Define an environment variable for the endpoint and set a value per environment. The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable. A vault-backed variable keeps the value out of the solution export and the design surface. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable.
- **C:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable.
- **D:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable.
- **E:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: The endpoint belongs in an environment variable, and the secret belongs in a vault referenced by that variable.

### Question 79 — A

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment step that runs the test set and blocks on failure turns the pipeline into a gate. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment step that runs the test set and blocks on failure turns the pipeline into a gate.
- **B:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure turns the pipeline into a gate.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure turns the pipeline into a gate.
- **D:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment step that runs the test set and blocks on failure turns the pipeline into a gate.

### Question 80 — D

Answer: Require approval before the production stage runs. An approval gate records who accepted the release, and it should be someone who has read the test results. An approval records who accepted the risk of the release. It must be a person who can read the test results. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: An approval gate records who accepted the release, and it should be someone who has read the test results.
- **B:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: An approval gate records who accepted the release, and it should be someone who has read the test results.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: An approval gate records who accepted the release, and it should be someone who has read the test results.
- **D:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: An approval gate records who accepted the release, and it should be someone who has read the test results.

### Question 81 — B

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. The solution and its configuration exist before the pipeline, and the test gate runs inside the deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: The solution and its configuration exist before the pipeline, and the test gate runs inside the deployment.
- **B:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: The solution and its configuration exist before the pipeline, and the test gate runs inside the deployment.
- **C:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: The solution and its configuration exist before the pipeline, and the test gate runs inside the deployment.
- **D:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: The solution and its configuration exist before the pipeline, and the test gate runs inside the deployment.

### Question 82 — D

Answer: Add a custom pipeline step that calls the validation job. A custom pipeline step can call the validation job and fail the deployment when it returns a failure. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: A custom pipeline step can call the validation job and fail the deployment when it returns a failure.
- **B:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A custom pipeline step can call the validation job and fail the deployment when it returns a failure.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: A custom pipeline step can call the validation job and fail the deployment when it returns a failure.
- **D:** Correct. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. In this case: A custom pipeline step can call the validation job and fail the deployment when it returns a failure.

### Question 83 — A

Answer: Keep the previous managed solution version so you can roll back. Keeping the previous managed version available is what makes a fast rollback possible. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: Keeping the previous managed version available is what makes a fast rollback possible.
- **B:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Keeping the previous managed version available is what makes a fast rollback possible.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Keeping the previous managed version available is what makes a fast rollback possible.
- **D:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Keeping the previous managed version available is what makes a fast rollback possible.

### Question 84 — D

Answer: Sample production conversations and score them against the rubric on a schedule. Scheduled sampling and rubric scoring catches drift that a launch test cannot see. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Scheduled sampling and rubric scoring catches drift that a launch test cannot see.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Scheduled sampling and rubric scoring catches drift that a launch test cannot see.
- **C:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Scheduled sampling and rubric scoring catches drift that a launch test cannot see.
- **D:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Scheduled sampling and rubric scoring catches drift that a launch test cannot see.

### Question 85 — A, C

Answers: Watch for knowledge-source changes and re-run the evaluation after they land; Sample production conversations and score them against the rubric on a schedule. Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest. Most answer regressions arrive with a document, not with a model change. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Most answer regressions arrive with a document, not with a model change. In this case: Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest.
- **C:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest.
- **D:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest.
- **E:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Re-running the evaluation after a source change catches regressions, and scheduled production sampling catches the rest.

### Question 86 — D

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities, federated or invited, give partners their own credentials without creating internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Why the correct answer wins: External identities, federated or invited, give partners their own credentials without creating internal accounts.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities, federated or invited, give partners their own credentials without creating internal accounts.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities, federated or invited, give partners their own credentials without creating internal accounts.
- **D:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities, federated or invited, give partners their own credentials without creating internal accounts.

### Question 87 — B

Answer: Track containment, resolution, and escalation metrics on a dashboard. Containment, resolution, and escalation trends are the operational evidence a sponsor can act on. Operational metrics show whether the agent is helping. They are the business case for the next release. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Fallback and handoff rates move before anyone files a ticket. A trend alert buys time. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence a sponsor can act on.
- **B:** Correct. Operational metrics show whether the agent is helping. They are the business case for the next release. In this case: Containment, resolution, and escalation trends are the operational evidence a sponsor can act on.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence a sponsor can act on.
- **D:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence a sponsor can act on.

### Question 88 — B

Answer: Run the tool unattended on a dedicated machine with a vaulted credential. An unattended run on a dedicated machine with a vaulted credential is the supported shape for that. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape for that.
- **B:** Correct. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. In this case: An unattended run on a dedicated machine with a vaulted credential is the supported shape for that.
- **C:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape for that.
- **D:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape for that.

### Question 89 — A

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway brokers the call from the cloud without opening an inbound firewall path, and it must be installed and monitored. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway brokers the call from the cloud without opening an inbound firewall path, and it must be installed and monitored.
- **B:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: An on-premises data gateway brokers the call from the cloud without opening an inbound firewall path, and it must be installed and monitored.
- **C:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway brokers the call from the cloud without opening an inbound firewall path, and it must be installed and monitored.
- **D:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway brokers the call from the cloud without opening an inbound firewall path, and it must be installed and monitored.

### Question 90 — A, C

Answers: Create a custom connector from the OpenAPI definition and add it as a tool; Configure connector authentication so each call uses the caller’s identity. A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement.
- **B:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement.
- **C:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement.
- **E:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector built from the definition gives typed operations, and per-user authentication makes the service evaluate that engineer's entitlement.

### Question 91 — D

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable supplies the endpoint per stage, so the same solution artefact works in every environment. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable supplies the endpoint per stage, so the same solution artefact works in every environment.
- **B:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: An environment variable supplies the endpoint per stage, so the same solution artefact works in every environment.
- **C:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: An environment variable supplies the endpoint per stage, so the same solution artefact works in every environment.
- **D:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable supplies the endpoint per stage, so the same solution artefact works in every environment.

### Question 92 — A

Answer: Configure a computer use tool against the legacy desktop application. Computer use drives the existing interface, which is the only option while the vendor exposes no API. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. In this case: Computer use drives the existing interface, which is the only option while the vendor exposes no API.
- **B:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Computer use drives the existing interface, which is the only option while the vendor exposes no API.
- **C:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Computer use drives the existing interface, which is the only option while the vendor exposes no API.
- **D:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Computer use drives the existing interface, which is the only option while the vendor exposes no API.

### Question 93 — A

Answer: Send an approval request and pause the flow until a person responds. An approval pauses the flow until a supervisor decides, so the irreversible action cannot happen before that decision. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. In this case: An approval pauses the flow until a supervisor decides, so the irreversible action cannot happen before that decision.
- **B:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: An approval pauses the flow until a supervisor decides, so the irreversible action cannot happen before that decision.
- **C:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: An approval pauses the flow until a supervisor decides, so the irreversible action cannot happen before that decision.
- **D:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: An approval pauses the flow until a supervisor decides, so the irreversible action cannot happen before that decision.

### Question 94 — D

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry followed by a terminate with a failure code lets the topic explain the problem instead of stalling. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the problem instead of stalling.
- **B:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the problem instead of stalling.
- **C:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry followed by a terminate with a failure code lets the topic explain the problem instead of stalling.
- **D:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry followed by a terminate with a failure code lets the topic explain the problem instead of stalling.

### Question 95 — C

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge applies each adjuster's existing item access, so the agent introduces no second permission model. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge applies each adjuster's existing item access, so the agent introduces no second permission model.
- **B:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint knowledge applies each adjuster's existing item access, so the agent introduces no second permission model.
- **C:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge applies each adjuster's existing item access, so the agent introduces no second permission model.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge applies each adjuster's existing item access, so the agent introduces no second permission model.

### Question 96 — D

Answer: Apply a security filter on the query before the agent composes an answer. The security filter belongs on the query, so another team's copy never enters the passages the model reads. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter belongs on the query, so another team's copy never enters the passages the model reads.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The security filter belongs on the query, so another team's copy never enters the passages the model reads.
- **C:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter belongs on the query, so another team's copy never enters the passages the model reads.
- **D:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter belongs on the query, so another team's copy never enters the passages the model reads.

### Question 97 — B

Answer: Use model-based grading against a rubric and review a human sample. Rubric-based grading scales to 900 cases, and a human sample keeps the grader calibrated against expert judgement. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Rubric-based grading scales to 900 cases, and a human sample keeps the grader calibrated against expert judgement.
- **B:** Correct. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. In this case: Rubric-based grading scales to 900 cases, and a human sample keeps the grader calibrated against expert judgement.
- **C:** Incorrect for this question. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Why the correct answer wins: Rubric-based grading scales to 900 cases, and a human sample keeps the grader calibrated against expert judgement.
- **D:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Rubric-based grading scales to 900 cases, and a human sample keeps the grader calibrated against expert judgement.

### Question 98 — A

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer stops the public experience from ever reaching internal content. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer stops the public experience from ever reaching internal content.
- **B:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer stops the public experience from ever reaching internal content.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Permission trimming in the knowledge layer stops the public experience from ever reaching internal content.
- **D:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer stops the public experience from ever reaching internal content.

### Question 99 — B, D

Answers: Add the SharePoint site as a knowledge source and rely on item-level permissions; Connect through a Power Platform connector and query it from a tool or flow. SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service.
- **B:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service.
- **C:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service.
- **D:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service.
- **E:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint supplies indexed document knowledge with its permissions, and the connector supplies operational access to the legacy service.

### Question 100 — D

Answer: Version the test set and rerun it for every change. A versioned set makes run-to-run comparison meaningful and stops a silent edit from hiding a regression. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A versioned set makes run-to-run comparison meaningful and stops a silent edit from hiding a regression.
- **B:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: A versioned set makes run-to-run comparison meaningful and stops a silent edit from hiding a regression.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A versioned set makes run-to-run comparison meaningful and stops a silent edit from hiding a regression.
- **D:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: A versioned set makes run-to-run comparison meaningful and stops a silent edit from hiding a regression.
