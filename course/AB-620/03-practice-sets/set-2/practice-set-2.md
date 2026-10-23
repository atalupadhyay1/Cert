# Microsoft AB-620 — Full-Length Mock Exam 2

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. An insurer's agent must check a caller against a policy administration system that runs in a data centre with no inbound access. What should the plan specify?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Mediate the on-premises call through an on-premises data gateway
- C. Batch the requests and post them to the source system on a schedule
- D. Mirror the source into Microsoft Fabric and query it with a Fabric data agent

### 2. A proposal would copy customer records into a cloud table every night so the agent never touches the source. Which consequence belongs in the design record?

Domain: Plan and configure agent solutions

- A. Copy the records nightly into Dataverse and answer from the copy
- B. Expose the system through a virtual table or connector view that the agent can read
- C. Batch the requests and post them to the source system on a schedule
- D. Call the internal endpoint straight from the topic over HTTP

### 3. A public-facing agent serves suppliers who have no account in the organisation's tenant. What should the identity plan use?

Domain: Plan and configure agent solutions

- A. Store one API key in a topic variable and reuse it for every user
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Give every conversation a single shared service account credential for the API
- D. Authenticate partners through external identities rather than internal tenant accounts

### 4. An internal agent must show, for any answer, which employee asked. Which identity decision delivers that?

Domain: Plan and configure agent solutions

- A. Store one API key in a topic variable and reuse it for every user
- B. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Give every conversation a single shared service account credential for the API

### 5. A utilities company wants its engineers to reach the agent from the Teams app they already use on site. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Publish to a public website with authenticated sign-in
- C. Publish to email and answer asynchronously
- D. Embed the agent in a custom application through the Direct Line channel

### 6. An insurer will surface the agent inside its own customer portal with the portal's own sign-in and layout. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Publish to a public website with authenticated sign-in
- C. Embed the agent in a custom application through the Direct Line channel
- D. Add the channel for omni-channel engagement so external support queues can route to it

### 7. A contact centre wants chats that the agent cannot resolve to queue for a human agent with the transcript. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents
- B. Publish to email and answer asynchronously
- C. Publish to a public website with authenticated sign-in
- D. Add the channel for omni-channel engagement so external support queues can route to it

### 8. A regulator asks what the agent answered to a specific customer six weeks ago and who changed its instructions. What should the design enable?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Turn on audit logging and retain agent conversation records
- C. Separate development and production environments with environment security groups
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 9. A team builds directly against production data because there is only one environment. Which control should be introduced first?

Domain: Plan and configure agent solutions

- A. Separate development and production environments with environment security groups
- B. Restrict who can author and publish with Copilot Studio security roles
- C. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- D. Turn on audit logging and retain agent conversation records

### 10. An organisation is opening agent building to 200 makers. Which two governance controls belong in the plan? Select two.

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- D. Restrict who can author and publish with Copilot Studio security roles
- E. Separate development and production environments with environment security groups

### 11. A shared escalation topic is used by four agents and must arrive in three environments. How should it be distributed?

Domain: Plan and configure agent solutions

- A. Package the shared topics, flows, and connection references in a solution
- B. Copy the topics into each agent so every team can edit its own copy
- C. Rebuild the same topic in each agent to avoid a shared dependency
- D. Parameterize environment-specific values with environment variables

### 12. A platform team is promoting a reusable agent solution from development to production. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- B. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- C. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- D. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables

### 13. An agent must create a case in a system with a connector action and return the case number. What should be built?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Use an automated cloud flow triggered by an event and have the agent wait for it
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Create the flow with the connector action the agent needs and return the result

### 14. A background process must run whenever a file lands in storage, and the agent is told afterwards. Which trigger fits?

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Use an automated cloud flow triggered by an event and have the agent wait for it
- C. Create the flow with the connector action the agent needs and return the result
- D. Add the capability as a connector action so the agent can call it without a flow

### 15. A flow fails at its third step, and the topic sends an empty answer to the user. What should be added?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Define typed input and output parameters on the flow and bind them from the topic
- D. Use an automated cloud flow triggered by an event and have the agent wait for it

### 16. A flow will be reused by three topics in two agents. Which two changes make it safe to call? Select two.

Domain: Plan and configure agent solutions

- A. Define typed input and output parameters on the flow and bind them from the topic
- B. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- C. Create an agent flow with a manual trigger that the topic calls with inputs
- D. Use an automated cloud flow triggered by an event and have the agent wait for it
- E. Add the capability as a connector action so the agent can call it without a flow

### 17. A bank requires that a person submits every payment instruction in the core system, and the agent may only prepare it. Which pattern fits?

Domain: Plan and configure agent solutions

- A. Have the agent draft the action and require a person to submit it in the source system
- B. Send an approval request and pause the flow until a person responds
- C. Let the agent complete the action and notify a person afterwards
- D. Post an adaptive card to Teams and wait for the human decision before continuing

### 18. A customer asks the agent to waive a fee that policy allows only a supervisor to waive. What should the agent do?

Domain: Plan and configure agent solutions

- A. Hand the conversation off to a live agent with the context attached
- B. Let the agent complete the action and notify a person afterwards
- C. Post an adaptive card to Teams and wait for the human decision before continuing
- D. Send an approval request and pause the flow until a person responds

### 19. A flow returned the wrong identifier to the conversation, and the builder needs the exact run. Where should they look?

Domain: Plan and configure agent solutions

- A. Configure an alert on failed runs and route it to the owning team
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Add a comment step to the flow describing the expected failure
- D. Review the flow run history and its action-level inputs and outputs

### 20. A failure happens twice a week and never while anyone is watching. Which monitoring choice finds the pattern?

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Send flow telemetry to Application Insights and query the traces
- C. Use the Copilot Studio analytics view for session and topic outcomes
- D. Review the flow run history and its action-level inputs and outputs

### 21. A flow that creates work orders runs continuously. Which two controls keep failures from becoming silent outages? Select two.

Domain: Plan and configure agent solutions

- A. Add a comment step to the flow describing the expected failure
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Configure an alert on failed runs and route it to the owning team
- D. Review the flow run history and its action-level inputs and outputs
- E. Configure a retry policy and terminate with a failure code the topic can read

### 22. After a customer says their account number once, later topics must filter answers by it. Which variable choice fits?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- C. Store the value in a global variable so later topics can read it
- D. Configure the message node to send a formatted message with the fields the user needs

### 23. A large agent needs the refund dialogue separated so another team can own it. What should the builder configure?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Configure the message node to send a formatted message with the fields the user needs
- C. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- D. Return an adaptive card so the data renders in labelled fields

### 24. An approval summary contains six values and two buttons. Which two formatting choices are available in a topic? Select two.

Domain: Plan and configure agent solutions

- A. Configure the message node to send a formatted message with the fields the user needs
- B. Return the raw flow output as plain text
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- E. Return an adaptive card so the data renders in labelled fields

### 25. An agent answers correctly but in a rambling style that users dislike. What should be changed?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Add a fallback topic for low-confidence answers that hands off to a person
- C. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- D. Require the answer to cite retrieved passages and refuse when none are found

### 26. A generative answers node mixes content from three unrelated libraries. What should change first?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Require the answer to cite retrieved passages and refuse when none are found
- D. Return an image with the card so the response looks richer

### 27. An organisation wants intranet content searchable with its permissions respected and no bespoke index. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Upload the documents as file knowledge on the agent
- C. Connect the source through a Copilot connector so its content is indexed for answers
- D. Connect through a Power Platform connector and query it from a tool or flow

### 28. A warehouse team is introducing a computer use agent for a licensed desktop application. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record
- B. Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes
- C. Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record
- D. Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes

### 29. A team is connecting several document estates and one operational system to a single agent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Test answers with users of different access → inventory the sources and their permissions → choose the connector or index for each → review unsupported questions → connect and scope the knowledge
- B. Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions
- C. Review unsupported questions → test answers with users of different access → connect and scope the knowledge → inventory the sources and their permissions → choose the connector or index for each
- D. Connect and scope the knowledge → choose the connector or index for each → inventory the sources and their permissions → test answers with users of different access → review unsupported questions

### 30. An agent needs both document knowledge and an operational call into a legacy system. Which two routes cover those needs? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Connect through a Power Platform connector and query it from a tool or flow
- B. Connect the source through a Copilot connector so its content is indexed for answers
- C. Index the content in Azure AI Search and use it as the knowledge source
- D. Register the database as a knowledge source so the agent can query it directly
- E. Upload the documents as file knowledge on the agent

### 31. A new index must support region filters, a citation field, and semantic ranking. What should be designed before ingestion?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Enable semantic ranking and let the agent use the reranked results
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Connect to the search service over a private endpoint with managed identity

### 32. Answers cite the right document but the supporting passage is often the least relevant one. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Recreate the index on every publish so it never goes stale
- C. Use hybrid retrieval with vector and keyword queries
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 33. A single AI Search index serves four tenants. Which two design decisions are required? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Enable semantic ranking and let the agent use the reranked results
- C. Apply a security filter on the query before the agent composes an answer
- D. Connect to the search service over a private endpoint with managed identity
- E. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 34. A legacy application now exposes an API and the agent still drives its user interface. What should the team do?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool unattended on a dedicated machine with a vaulted credential
- B. Provision a machine or machine group and run the tool there with a dedicated account
- C. Configure a computer use tool against the legacy desktop application
- D. Replace the screen automation with an API once the application exposes one

### 35. A hosted agent must call an MCP server that runs in the platform team's cluster. Which transport applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Use a streamable HTTP MCP server so the agent can reach it over the network
- B. Embed the MCP server as a local process inside the agent
- C. Configure the MCP server connection with the authentication the server requires
- D. Add an MCP server as a tool and let the agent discover the tools it exposes

### 36. An MCP tool that worked in a personal environment fails in the shared agent with a 401. What should be checked first?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure the MCP server connection with the authentication the server requires
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Use a streamable HTTP MCP server so the agent can reach it over the network
- D. Expose only the MCP tools the task needs and review their descriptions

### 37. A builder adds all 60 tools from an MCP server so nothing is missing later. What should the review recommend?

Domain: Integrate and extend agents in Copilot Studio

- A. Add an MCP server as a tool and let the agent discover the tools it exposes
- B. Wrap the internal API as MCP tools and register the server endpoint with the agent
- C. Expose only the MCP tools the task needs and review their descriptions
- D. Configure the MCP server connection with the authentication the server requires

### 38. An existing custom connector authenticates with one key shared by the whole company. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Create a custom connector from the OpenAPI definition and add it as a tool
- C. Configure connector authentication so each call uses the caller’s identity
- D. Call the API from an agent flow and return the parsed response to the topic

### 39. An agent pastes raw JSON into its answers because the response fields are undefined. What should be added?

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Call the API from an agent flow and return the parsed response to the topic
- C. Define the response schema so the agent can reason over the returned fields
- D. Call the REST API from a topic with a Send HTTP request action

### 40. A public API must become a reusable tool for four agents. Which two choices apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Hard-code the endpoint URL and key inside the topic
- B. Call the REST API from a topic with a Send HTTP request action
- C. Define the response schema so the agent can reason over the returned fields
- D. Create a custom connector from the OpenAPI definition and add it as a tool
- E. Configure connector authentication so each call uses the caller’s identity

### 41. A parent agent routes a leave question to the payroll child agent. What should be corrected?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Write the parent’s instructions to describe when each child should be used
- D. Give every child the same knowledge source so answers stay consistent

### 42. Two children return the customer identifier in different formats, and the parent fails to match them. What should be standardised?

Domain: Integrate and extend agents in Copilot Studio

- A. Give each child a clear input and output contract and keep shared state in the parent
- B. Build one large agent with every topic so there is a single place to change
- C. Route by intent in the parent and pass only the context the child needs
- D. Give every child the same knowledge source so answers stay consistent

### 43. An architect is splitting a monolithic agent into a parent with specialist children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- B. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions
- C. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions
- D. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent

### 44. A single agent must serve five departments with different owners. Which two design moves fit? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Split the work into a parent agent that delegates to specialist child agents
- C. Give each child a clear input and output contract and keep shared state in the parent
- D. Write the parent’s instructions to describe when each child should be used
- E. Route by intent in the parent and pass only the context the child needs

### 45. A team wants custom orchestration around a Foundry agent instead of declaring it as a connected agent. What should they use?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- B. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- C. Deploy the model in Foundry and point the custom prompt at that deployment
- D. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity

### 46. A custom prompt must use a specific model that is deployed in Microsoft Foundry. What should the builder do?

Domain: Integrate and extend agents in Copilot Studio

- A. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Deploy the model in Foundry and point the custom prompt at that deployment
- D. Keep the default model because it is already configured

### 47. A team has a working Foundry agent and wants it inside a Copilot Studio conversation. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- B. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- C. Evaluate the Foundry agent against the same test set before it is connected
- D. Deploy the model in Foundry and point the custom prompt at that deployment
- E. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent

### 48. A parent depends on a child agent that is republished weekly by another team. What should the parent pin?

Domain: Integrate and extend agents in Copilot Studio

- A. Confirm the caller’s identity and permissions flow through to the connected agent
- B. Add the existing agent as a connected agent and let the parent delegate to it
- C. Write a precise name and description for the connected agent so routing works
- D. Pin the connected agent’s published version that the parent was tested against

### 49. A partner will not expose its agent as a connected agent, but publishes a documented REST endpoint. What should be used instead?

Domain: Integrate and extend agents in Copilot Studio

- A. Copy its topics into the new agent so both can be edited separately
- B. Call the partner’s published API through a custom connector when delegation is unavailable
- C. Confirm the caller’s identity and permissions flow through to the connected agent
- D. Add the existing agent as a connected agent and let the parent delegate to it

### 50. A Fabric data agent answers revenue questions with three different totals in one week. What should be fixed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Define the measures in the semantic model so the data agent answers consistently
- B. Query the lakehouse directly from the agent with a SQL tool
- C. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- D. Export the data nightly into files the agent can search

### 51. A data agent can read every table in the workspace although it only needs one model. What should be tightened?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Grant the data agent’s identity read access to the semantic model only
- C. Export the data nightly into files the agent can search
- D. Define the measures in the semantic model so the data agent answers consistently

### 52. A remote agent's capability must be discoverable and invocable by another organisation's agent. What should the capability be modelled as?

Domain: Integrate and extend agents in Copilot Studio

- A. Track the remote task state and surface long-running results back into the conversation
- B. Model the remote capability as an A2A skill the agent can discover and invoke
- C. Configure authentication between the agents so calls are authorized
- D. Publish an agent card that describes the remote agent’s skills and endpoint

### 53. Two agent platforms must agree on what a remote agent can do before any call is made. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Rebuild the remote agent’s functionality locally instead of using the protocol
- B. Model the remote capability as an A2A skill the agent can discover and invoke
- C. Define which remote agents are trusted and restrict the skills exposed to them
- D. Publish an agent card that describes the remote agent’s skills and endpoint

### 54. A partner agent should reach three of the internal agent's nine skills. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Track the remote task state and surface long-running results back into the conversation
- B. Publish an agent card that describes the remote agent’s skills and endpoint
- C. Configure authentication between the agents so calls are authorized
- D. Define which remote agents are trusted and restrict the skills exposed to them

### 55. A regulator requires that customer text is processed inside one country. What should be settled first?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision enough quota and throughput for peak conversation volume
- B. Choose a model from the catalog that meets quality, latency, and residency needs
- C. Deploy the model in a region that satisfies the data residency requirement
- D. Deploy the chosen model and reference the deployment from the custom prompt

### 56. A pilot supports 20 concurrent users and production expects 2,000. What must be planned?

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the chosen model and reference the deployment from the custom prompt
- B. Deploy the model in a region that satisfies the data residency requirement
- C. Choose a model from the catalog that meets quality, latency, and residency needs
- D. Provision enough quota and throughput for peak conversation volume

### 57. An agent is live and a user reports an answer no one can reproduce. What should be in place to investigate it?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Query conversation and tool spans in Application Insights with KQL
- D. Alert on failed tool calls and answer-quality regressions

### 58. Conversation volume triples and the telemetry bill follows. What should change without losing failures?

Domain: Integrate and extend agents in Copilot Studio

- A. Correlate a failed answer with the tool call and knowledge retrieval behind it
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Log full conversation transcripts indefinitely without retention limits

### 59. Tool calls started failing an hour ago and nobody noticed until a user complained. What should be added?

Domain: Integrate and extend agents in Copilot Studio

- A. Query conversation and tool spans in Application Insights with KQL
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Alert on failed tool calls and answer-quality regressions
- D. Log full conversation transcripts indefinitely without retention limits

### 60. A bad answer must be explained to the business. Which two capabilities matter? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Correlate a failed answer with the tool call and knowledge retrieval behind it
- B. Query conversation and tool spans in Application Insights with KQL
- C. Log full conversation transcripts indefinitely without retention limits
- D. Connect the agent to Application Insights and emit conversation and tool telemetry
- E. Sample telemetry so volume stays affordable while errors are always kept

### 61. A team tunes prompts against the whole test set and reports perfect scores on it. What should they change?

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Build the test set from real anonymized conversations plus the cases that must never fail
- D. Test with a handful of happy-path questions before release

### 62. A quality engineer is establishing an evaluation loop for a new agent. Which sequence is correct?

Domain: Test and manage agents

- A. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- B. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent
- C. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change
- D. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change

### 63. A test set is about to become the release gate. Which two practices protect it? Select two.

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Build the test set from real anonymized conversations plus the cases that must never fail
- C. Version the test set and rerun it for every change
- D. Test with a handful of happy-path questions before release
- E. Generate synthetic cases from the topics and intents the agent supports

### 64. A regulator wants to know how refusal quality was judged before launch. Which method is most defensible?

Domain: Test and manage agents

- A. Rely on the builder trying a few questions in the test pane
- B. Score answers with keyword matching against expected phrases
- C. Use model-based grading against a rubric and review a human sample
- D. Have subject-matter experts score a sample against the rubric

### 65. A team is calibrating an automated grader against human judgement. Which sequence is correct?

Domain: Test and manage agents

- A. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores
- B. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- C. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand
- D. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores

### 66. A backlog of 60 failures has no names attached. What should be introduced?

Domain: Test and manage agents

- A. Group failures by topic and root cause instead of fixing items one at a time
- B. Assign each failure cluster to the owner of the topic, prompt, or connector
- C. Publish when the overall average looks acceptable
- D. Keep failed cases in the test set so they cannot regress

### 67. A managed solution cannot be edited in the test environment, and a fix is needed. Where should the change be made?

Domain: Test and manage agents

- A. Export the managed solution and import it into the target environment
- B. Keep the agent in an unmanaged solution in development and ship a managed solution
- C. Send the agents topic files to the administrator by email
- D. Create a solution and add the agent and its dependencies to it

### 68. A solution is being prepared for its first production release. Which sequence is correct?

Domain: Test and manage agents

- A. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- B. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- C. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- D. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables

### 69. A connector key appears in the solution export and in the topic designer. Where should it live?

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Record the required values in the deployment notes for each environment
- C. Use the current value in production and a default value for development
- D. Store the secret in a vault and reference it from the environment variable

### 70. A solution needs three environments with different endpoints. Which two practices apply? Select two.

Domain: Test and manage agents

- A. Use the current value in production and a default value for development
- B. Hard-code the production endpoint in the topic and change it after import
- C. Record the required values in the deployment notes for each environment
- D. Set the environment variable values as part of the pipeline deployment step
- E. Define an environment variable for the endpoint and set a value per environment

### 71. A release is imported by hand and nobody can say what version is live. What should replace the process?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Add a pre-deployment step that runs the agent test set and blocks on failure
- C. Import the solution by hand into production for each release
- D. Create a pipeline with development, test, and production stages

### 72. Answer quality dropped after a release that passed no automated check. What should the pipeline have done?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Use the pipeline analytics to see which stage failed and why
- C. Import the solution by hand into production for each release
- D. Add a pre-deployment step that runs the agent test set and blocks on failure

### 73. A team is introducing a three-stage pipeline with an approval gate. Which sequence is correct?

Domain: Test and manage agents

- A. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval
- B. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage
- C. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step
- D. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval

### 74. A bank requires evidence before each production release. Which two pipeline features provide it? Select two.

Domain: Test and manage agents

- A. Import the solution by hand into production for each release
- B. Require approval before the production stage runs
- C. Add a pre-deployment step that runs the agent test set and blocks on failure
- D. Use the pipeline analytics to see which stage failed and why
- E. Deploy on a fixed schedule regardless of readiness

### 75. The organisation's security scan must block deployments that fail. What should be added?

Domain: Test and manage agents

- A. Keep the previous managed solution version so you can roll back
- B. Notify the owning team with the deployment result and the failed step
- C. Add a custom pipeline step that calls the validation job
- D. Pass environment-specific values through pipeline configuration rather than editing the solution

### 76. A release must be reversible within ten minutes. What should the pipeline keep?

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Deploy on a fixed schedule regardless of readiness
- C. Pass environment-specific values through pipeline configuration rather than editing the solution
- D. Keep the previous managed solution version so you can roll back

### 77. Account managers keep saying an answer is unhelpful, but nothing records it. What should be added?

Domain: Test and manage agents

- A. Sample production conversations and score them against the rubric on a schedule
- B. Test once before launch and assume behaviour stays stable
- C. Capture user feedback in the conversation and route negative cases to review
- D. Track containment, resolution, and escalation metrics on a dashboard

### 78. Fallback and handoff rates double over a weekend and nobody notices. What should be added?

Domain: Test and manage agents

- A. Capture user feedback in the conversation and route negative cases to review
- B. Track containment, resolution, and escalation metrics on a dashboard
- C. Test once before launch and assume behaviour stays stable
- D. Alert on rising fallback and handoff rates

### 79. Drivers type short, misspelled sentences from a phone. Which change most improves the test set?

Domain: Test and manage agents

- A. Include adversarial and edge cases such as out-of-scope and injection attempts
- B. Build the test set from real anonymized conversations plus the cases that must never fail
- C. Generate synthetic cases from the topics and intents the agent supports
- D. Test with a handful of happy-path questions before release

### 80. A scheduled computer use run must use a credential no employee holds. Which configuration applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure a computer use tool against the legacy desktop application
- B. Run the tool unattended on a dedicated machine with a vaulted credential
- C. Replace the screen automation with an API once the application exposes one
- D. Provision a machine or machine group and run the tool there with a dedicated account

### 81. An internal API must be reusable as MCP tools by three agents. What should the platform team build?

Domain: Integrate and extend agents in Copilot Studio

- A. Use a streamable HTTP MCP server so the agent can reach it over the network
- B. Wrap the internal API as MCP tools and register the server endpoint with the agent
- C. Embed the MCP server as a local process inside the agent
- D. Add an MCP server as a tool and let the agent discover the tools it exposes

### 82. A regression returned four months after it was fixed. What was missing?

Domain: Test and manage agents

- A. Assign each failure cluster to the owner of the topic, prompt, or connector
- B. Group failures by topic and root cause instead of fixing items one at a time
- C. Keep failed cases in the test set so they cannot regress
- D. Publish when the overall average looks acceptable

### 83. A security review requires search traffic to stay off the public internet. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Recreate the index on every publish so it never goes stale
- C. Connect to the search service over a private endpoint with managed identity
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 84. A maker attached a consumer file-sharing connector to an agent that reads contracts. Which control stops this at the environment level?

Domain: Plan and configure agent solutions

- A. Turn on audit logging and retain agent conversation records
- B. Separate development and production environments with environment security groups
- C. Restrict who can author and publish with Copilot Studio security roles
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 85. A two-environment solution needs a working default without any pipeline. Which setting fits?

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Define an environment variable for the endpoint and set a value per environment
- C. Use the current value in production and a default value for development
- D. Set the environment variable values as part of the pipeline deployment step

### 86. One agent will serve employees inside the tenant and suppliers outside it. Which two identity decisions are required? Select two.

Domain: Plan and configure agent solutions

- A. Allow anonymous access to the agent and authenticate only at the API
- B. Give every conversation a single shared service account credential for the API
- C. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- D. Authenticate partners through external identities rather than internal tenant accounts
- E. Store one API key in a topic variable and reuse it for every user

### 87. A branch team keeps a small reference table in a database and wants the agent to look values up directly. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the source through a Copilot connector so its content is indexed for answers
- B. Connect through a Power Platform connector and query it from a tool or flow
- C. Upload the documents as file knowledge on the agent
- D. Register the database as a knowledge source so the agent can query it directly

### 88. A parent sends the whole conversation to every child it may need, and token cost is climbing. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Build one large agent with every topic so there is a single place to change
- C. Give each child a clear input and output contract and keep shared state in the parent
- D. Split the work into a parent agent that delegates to specialist child agents

---

## Case study — Alpine Retail Group

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Region managers want sales figures that match the finance semantic model exactly. Which approach answers that?

Domain: Integrate and extend agents in Copilot Studio

- A. Define the measures in the semantic model so the data agent answers consistently
- B. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- C. Export the data nightly into files the agent can search
- D. Query the lakehouse directly from the agent with a SQL tool

### 90. One agent per country must share the same refund behaviour so a fix is made once. What should be built?

Domain: Plan and configure agent solutions

- A. Copy the topics into each agent so every team can edit its own copy
- B. Extract the shared logic into a reusable component or child agent and reference it
- C. Rebuild the same topic in each agent to avoid a shared dependency
- D. Expose the shared integration as a custom connector any agent can add as a tool

### 91. Country agents move through stages before release. Which two controls supply release evidence? Select two.

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Deploy on a fixed schedule regardless of readiness
- C. Add a pre-deployment step that runs the agent test set and blocks on failure
- D. Use the pipeline analytics to see which stage failed and why
- E. Import the solution by hand into production for each release

---

## Case study — Harborview Clinics

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Practice managers need to see why the assistant refused a question and what it said at the time. Which capability provides that evidence?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Turn on audit logging and retain agent conversation records
- C. Separate development and production environments with environment security groups
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 93. Before release, Harborview must show that refusals were judged appropriate rather than merely counted. Which method gives defensible evidence?

Domain: Test and manage agents

- A. Use model-based grading against a rubric and review a human sample
- B. Rely on the builder trying a few questions in the test pane
- C. Score answers with keyword matching against expected phrases
- D. Have subject-matter experts score a sample against the rubric

### 94. A patient asks for dosing advice and the scheduling content holds nothing relevant. Which behaviour must the answer configuration enforce?

Domain: Plan and configure agent solutions

- A. Add a fallback topic for low-confidence answers that hands off to a person
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Require the answer to cite retrieved passages and refuse when none are found
- D. Point the generative answers node at the specific knowledge source for the question

---

## Case study — Tailwind Logistics

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Consignments come from Dataverse, and carrier status comes from connector operations that are throttled. Which route supplies the carrier status?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect through a Power Platform connector and query it from a tool or flow
- B. Connect the source through a Copilot connector so its content is indexed for answers
- C. Upload the documents as file knowledge on the agent
- D. Index the content in Azure AI Search and use it as the knowledge source

### 96. Under a burst the carrier connector starts throttling. Which two flow behaviours keep the conversation honest? Select two.

Domain: Plan and configure agent solutions

- A. Use an automated cloud flow triggered by an event and have the agent wait for it
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Configure a retry policy and terminate with a failure code the topic can read
- E. Create an agent flow with a manual trigger that the topic calls with inputs

### 97. Drivers type short, misspelled sentences from a phone. Which test material matters most before release?

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Test with a handful of happy-path questions before release
- D. Build the test set from real anonymized conversations plus the cases that must never fail

---

## Case study — Woodgrove Insurance

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Callers must be checked against a policy administration system that stays inside the data centre. Which integration should be planned?

Domain: Plan and configure agent solutions

- A. Batch the requests and post them to the source system on a schedule
- B. Call the internal endpoint straight from the topic over HTTP
- C. Mediate the on-premises call through an on-premises data gateway
- D. Mirror the source into Microsoft Fabric and query it with a Fabric data agent

### 99. Every quoted sentence must be traceable to an exact document version. What must the index carry?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Create the index with the fields, vector profile, and semantic configuration the agent needs
- C. Connect to the search service over a private endpoint with managed identity
- D. Enable semantic ranking and let the agent use the reranked results

### 100. The business case rests on average handling time after launch. What should be tracked?

Domain: Test and manage agents

- A. Track containment, resolution, and escalation metrics on a dashboard
- B. Capture user feedback in the conversation and route negative cases to review
- C. Test once before launch and assume behaviour stays stable
- D. Sample production conversations and score them against the rubric on a schedule

---

## Answer key and explanations

### Question 1 — B

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway reaches the system from the cloud without weakening the network boundary. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway reaches the system from the cloud without weakening the network boundary.
- **B:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway reaches the system from the cloud without weakening the network boundary.
- **C:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway reaches the system from the cloud without weakening the network boundary.
- **D:** Incorrect for this question. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Why the correct answer wins: An on-premises data gateway reaches the system from the cloud without weakening the network boundary.

### Question 2 — A

Answer: Copy the records nightly into Dataverse and answer from the copy. A nightly copy answers yesterday's questions and needs its own reconciliation, which is a business decision the plan must state. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. In this case: A nightly copy answers yesterday's questions and needs its own reconciliation, which is a business decision the plan must state.
- **B:** Incorrect for this question. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which is a business decision the plan must state.
- **C:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which is a business decision the plan must state.
- **D:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which is a business decision the plan must state.

### Question 3 — D

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities give suppliers their own credentials without creating internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: External identities give suppliers their own credentials without creating internal accounts.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities give suppliers their own credentials without creating internal accounts.
- **C:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities give suppliers their own credentials without creating internal accounts.
- **D:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities give suppliers their own credentials without creating internal accounts.

### Question 4 — B

Answer: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream. Entra ID sign-in records the calling employee and their token carries that identity downstream. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Entra ID sign-in records the calling employee and their token carries that identity downstream.
- **B:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Entra ID sign-in records the calling employee and their token carries that identity downstream.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Entra ID sign-in records the calling employee and their token carries that identity downstream.
- **D:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Entra ID sign-in records the calling employee and their token carries that identity downstream.

### Question 5 — A

Answer: Publish to Microsoft Teams and keep the agent inside the tenant. Publishing to Teams keeps the agent where the engineers work and inherits their tenant sign-in. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. In this case: Publishing to Teams keeps the agent where the engineers work and inherits their tenant sign-in.
- **B:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Publishing to Teams keeps the agent where the engineers work and inherits their tenant sign-in.
- **C:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Publishing to Teams keeps the agent where the engineers work and inherits their tenant sign-in.
- **D:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: Publishing to Teams keeps the agent where the engineers work and inherits their tenant sign-in.

### Question 6 — C

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line gives the host application control of the experience and the authentication flow. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Direct Line gives the host application control of the experience and the authentication flow.
- **B:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Direct Line gives the host application control of the experience and the authentication flow.
- **C:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line gives the host application control of the experience and the authentication flow.
- **D:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Direct Line gives the host application control of the experience and the authentication flow.

### Question 7 — D

Answer: Add the channel for omni-channel engagement so external support queues can route to it. Omni-channel engagement carries the conversation into the support queue with its context intact. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Why the correct answer wins: Omni-channel engagement carries the conversation into the support queue with its context intact.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Omni-channel engagement carries the conversation into the support queue with its context intact.
- **C:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Omni-channel engagement carries the conversation into the support queue with its context intact.
- **D:** Correct. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. In this case: Omni-channel engagement carries the conversation into the support queue with its context intact.

### Question 8 — B

Answer: Turn on audit logging and retain agent conversation records. Audit logging with a defined retention period is what makes both questions answerable. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit logging with a defined retention period is what makes both questions answerable.
- **B:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit logging with a defined retention period is what makes both questions answerable.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit logging with a defined retention period is what makes both questions answerable.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit logging with a defined retention period is what makes both questions answerable.

### Question 9 — A

Answer: Separate development and production environments with environment security groups. A separate development environment with security groups stops untested changes from touching live data. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. In this case: A separate development environment with security groups stops untested changes from touching live data.
- **B:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: A separate development environment with security groups stops untested changes from touching live data.
- **C:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: A separate development environment with security groups stops untested changes from touching live data.
- **D:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A separate development environment with security groups stops untested changes from touching live data.

### Question 10 — D, E

Answers: Separate development and production environments with environment security groups; Restrict who can author and publish with Copilot Studio security roles. Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group.
- **B:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group.
- **C:** Incorrect for this question. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Why the correct answer wins: Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group.
- **D:** Correct. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. In this case: Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group.
- **E:** Correct. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. In this case: Environment security groups limit where makers can work, and publishing rights should sit with a narrow named group.

### Question 11 — A

Answer: Package the shared topics, flows, and connection references in a solution. A solution carries the shared topic and its dependencies as one versioned unit. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. In this case: A solution carries the shared topic and its dependencies as one versioned unit.
- **B:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A solution carries the shared topic and its dependencies as one versioned unit.
- **C:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A solution carries the shared topic and its dependencies as one versioned unit.
- **D:** Incorrect for this question. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Why the correct answer wins: A solution carries the shared topic and its dependencies as one versioned unit.

### Question 12 — B

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution and its configuration exist before export, and the pipeline performs the final promotion. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution and its configuration exist before export, and the pipeline performs the final promotion.
- **B:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution and its configuration exist before export, and the pipeline performs the final promotion.
- **C:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution and its configuration exist before export, and the pipeline performs the final promotion.
- **D:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution and its configuration exist before export, and the pipeline performs the final promotion.

### Question 13 — D

Answer: Create the flow with the connector action the agent needs and return the result. A flow wrapping the connector action performs the work and returns the identifier to the conversation. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: A flow wrapping the connector action performs the work and returns the identifier to the conversation.
- **B:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A flow wrapping the connector action performs the work and returns the identifier to the conversation.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A flow wrapping the connector action performs the work and returns the identifier to the conversation.
- **D:** Correct. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. In this case: A flow wrapping the connector action performs the work and returns the identifier to the conversation.

### Question 14 — B

Answer: Use an automated cloud flow triggered by an event and have the agent wait for it. An automated flow responds to the storage event; the agent does not wait on it. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An automated flow responds to the storage event; the agent does not wait on it.
- **B:** Correct. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. In this case: An automated flow responds to the storage event; the agent does not wait on it.
- **C:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: An automated flow responds to the storage event; the agent does not wait on it.
- **D:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An automated flow responds to the storage event; the agent does not wait on it.

### Question 15 — A

Answer: Wrap the calls in a scope with a parallel error branch that returns a structured failure. An error branch that returns a failure value lets the topic say something true instead of nothing. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: An error branch that returns a failure value lets the topic say something true instead of nothing.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An error branch that returns a failure value lets the topic say something true instead of nothing.
- **C:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: An error branch that returns a failure value lets the topic say something true instead of nothing.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: An error branch that returns a failure value lets the topic say something true instead of nothing.

### Question 16 — A, B

Answers: Define typed input and output parameters on the flow and bind them from the topic; Wrap the calls in a scope with a parallel error branch that returns a structured failure. Typed parameters define the contract, and structured error returns stop silent failures from reaching users. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed parameters define the contract, and structured error returns stop silent failures from reaching users.
- **B:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: Typed parameters define the contract, and structured error returns stop silent failures from reaching users.
- **C:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: Typed parameters define the contract, and structured error returns stop silent failures from reaching users.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed parameters define the contract, and structured error returns stop silent failures from reaching users.
- **E:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed parameters define the contract, and structured error returns stop silent failures from reaching users.

### Question 17 — A

Answer: Have the agent draft the action and require a person to submit it in the source system. Drafting leaves the irreversible step in the system that owns it, with the human performing it. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. In this case: Drafting leaves the irreversible step in the system that owns it, with the human performing it.
- **B:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: Drafting leaves the irreversible step in the system that owns it, with the human performing it.
- **C:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: Drafting leaves the irreversible step in the system that owns it, with the human performing it.
- **D:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: Drafting leaves the irreversible step in the system that owns it, with the human performing it.

### Question 18 — A

Answer: Hand the conversation off to a live agent with the context attached. A discretionary decision belongs with a person, so the conversation is handed over with its context. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. In this case: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **B:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **C:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **D:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.

### Question 19 — D

Answer: Review the flow run history and its action-level inputs and outputs. Run history keeps each action's inputs and outputs for that instance. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Why the correct answer wins: Run history keeps each action's inputs and outputs for that instance.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Run history keeps each action's inputs and outputs for that instance.
- **C:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Run history keeps each action's inputs and outputs for that instance.
- **D:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Run history keeps each action's inputs and outputs for that instance.

### Question 20 — B

Answer: Send flow telemetry to Application Insights and query the traces. Traces in Application Insights keep the intermittent failure and its dependencies for later analysis. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Traces in Application Insights keep the intermittent failure and its dependencies for later analysis.
- **B:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Traces in Application Insights keep the intermittent failure and its dependencies for later analysis.
- **C:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Traces in Application Insights keep the intermittent failure and its dependencies for later analysis.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Traces in Application Insights keep the intermittent failure and its dependencies for later analysis.

### Question 21 — C, E

Answers: Configure an alert on failed runs and route it to the owning team; Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs transient faults, and alerting on remaining failures brings a person in. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs transient faults, and alerting on remaining failures brings a person in.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs transient faults, and alerting on remaining failures brings a person in.
- **C:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: A retry policy absorbs transient faults, and alerting on remaining failures brings a person in.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs transient faults, and alerting on remaining failures brings a person in.
- **E:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs transient faults, and alerting on remaining failures brings a person in.

### Question 22 — C

Answer: Store the value in a global variable so later topics can read it. A global variable keeps the account available across topics for the rest of the conversation. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: A global variable keeps the account available across topics for the rest of the conversation.
- **B:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A global variable keeps the account available across topics for the rest of the conversation.
- **C:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: A global variable keeps the account available across topics for the rest of the conversation.
- **D:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A global variable keeps the account available across topics for the rest of the conversation.

### Question 23 — A

Answer: Configure the topic as a redirect target with its own trigger phrases. A redirect topic with its own triggers keeps ownership separate while staying in one agent. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. In this case: A redirect topic with its own triggers keeps ownership separate while staying in one agent.
- **B:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate while staying in one agent.
- **C:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate while staying in one agent.
- **D:** Incorrect for this question. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate while staying in one agent.

### Question 24 — A, E

Answers: Return an adaptive card so the data renders in labelled fields; Configure the message node to send a formatted message with the fields the user needs. A formatted message carries the values, and an adaptive card adds interactive buttons. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. A message node can send structured text without a card. It is the lightest way to make a list readable. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. A message node can send structured text without a card. It is the lightest way to make a list readable. In this case: A formatted message carries the values, and an adaptive card adds interactive buttons.
- **B:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: A formatted message carries the values, and an adaptive card adds interactive buttons.
- **C:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: A formatted message carries the values, and an adaptive card adds interactive buttons.
- **D:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A formatted message carries the values, and an adaptive card adds interactive buttons.
- **E:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: A formatted message carries the values, and an adaptive card adds interactive buttons.

### Question 25 — C

Answer: Configure a custom prompt that fixes the tone, structure, and citation behaviour. A custom prompt fixes tone and structure without changing what the agent knows. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A custom prompt fixes tone and structure without changing what the agent knows.
- **B:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: A custom prompt fixes tone and structure without changing what the agent knows.
- **C:** Correct. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. In this case: A custom prompt fixes tone and structure without changing what the agent knows.
- **D:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: A custom prompt fixes tone and structure without changing what the agent knows.

### Question 26 — A

Answer: Point the generative answers node at the specific knowledge source for the question. Scoping the node to the right knowledge source keeps the answer on topic. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. In this case: Scoping the node to the right knowledge source keeps the answer on topic.
- **B:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Scoping the node to the right knowledge source keeps the answer on topic.
- **C:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: Scoping the node to the right knowledge source keeps the answer on topic.
- **D:** Incorrect for this question. Images can help recognition but add nothing when the question is about a value or a status. Why the correct answer wins: Scoping the node to the right knowledge source keeps the answer on topic.

### Question 27 — C

Answer: Connect the source through a Copilot connector so its content is indexed for answers. A Copilot connector indexes the content with its permissions for grounded answers. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Copilot connector indexes the content with its permissions for grounded answers.
- **B:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector indexes the content with its permissions for grounded answers.
- **C:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector indexes the content with its permissions for grounded answers.
- **D:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: A Copilot connector indexes the content with its permissions for grounded answers.

### Question 28 — D

Answer: Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes. Confirming there is no API, preparing a host, recording steps, running and inspecting the log, then monitoring for interface changes. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Monitoring a tool that has never run and has no host is not possible. Why the correct answer wins: Confirming there is no API, preparing a host, recording steps, running and inspecting the log, then monitoring for interface changes.
- **B:** Incorrect for this question. Recording happens on the prepared machine, after the API check. Why the correct answer wins: Confirming there is no API, preparing a host, recording steps, running and inspecting the log, then monitoring for interface changes.
- **C:** Incorrect for this question. A run cannot precede the host and the recorded steps. Why the correct answer wins: Confirming there is no API, preparing a host, recording steps, running and inspecting the log, then monitoring for interface changes.
- **D:** Correct. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. In this case: Confirming there is no API, preparing a host, recording steps, running and inspecting the log, then monitoring for interface changes.

### Question 29 — B

Answer: Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions. The inventory and permissions come first, the connector or index choice follows, then connection, access testing, and review. Inventory precedes choice, choice precedes connection, and access testing follows connection. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Access testing requires connected sources. Why the correct answer wins: The inventory and permissions come first, the connector or index choice follows, then connection, access testing, and review.
- **B:** Correct. Inventory precedes choice, choice precedes connection, and access testing follows connection. In this case: The inventory and permissions come first, the connector or index choice follows, then connection, access testing, and review.
- **C:** Incorrect for this question. There is nothing to review before the knowledge is connected and tested. Why the correct answer wins: The inventory and permissions come first, the connector or index choice follows, then connection, access testing, and review.
- **D:** Incorrect for this question. The connector cannot be chosen before the inventory describes the sources. Why the correct answer wins: The inventory and permissions come first, the connector or index choice follows, then connection, access testing, and review.

### Question 30 — A, B

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Connect through a Power Platform connector and query it from a tool or flow. A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations.
- **B:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations.
- **C:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations.
- **E:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector indexes documents with permissions, and a Power Platform connector performs operations.

### Question 31 — C

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema, including filterable and retrievable fields plus the semantic configuration, has to exist first. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema, including filterable and retrievable fields plus the semantic configuration, has to exist first.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema, including filterable and retrievable fields plus the semantic configuration, has to exist first.
- **C:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema, including filterable and retrievable fields plus the semantic configuration, has to exist first.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema, including filterable and retrievable fields plus the semantic configuration, has to exist first.

### Question 32 — A

Answer: Enable semantic ranking and let the agent use the reranked results. Semantic ranking reorders the top results so the passage the model reads is the most relevant one. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: Semantic ranking reorders the top results so the passage the model reads is the most relevant one.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Semantic ranking reorders the top results so the passage the model reads is the most relevant one.
- **C:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: Semantic ranking reorders the top results so the passage the model reads is the most relevant one.
- **D:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: Semantic ranking reorders the top results so the passage the model reads is the most relevant one.

### Question 33 — C, E

Answers: Apply a security filter on the query before the agent composes an answer; Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema must carry the tenant field so queries can filter on it, and every query must apply that filter. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema must carry the tenant field so queries can filter on it, and every query must apply that filter.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema must carry the tenant field so queries can filter on it, and every query must apply that filter.
- **C:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The schema must carry the tenant field so queries can filter on it, and every query must apply that filter.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema must carry the tenant field so queries can filter on it, and every query must apply that filter.
- **E:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema must carry the tenant field so queries can filter on it, and every query must apply that filter.

### Question 34 — D

Answer: Replace the screen automation with an API once the application exposes one. Replacing screen automation with the API removes a fragile dependency. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **B:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **C:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **D:** Correct. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. In this case: Replacing screen automation with the API removes a fragile dependency.

### Question 35 — A

Answer: Use a streamable HTTP MCP server so the agent can reach it over the network. Streamable HTTP reaches a remote server over the network, which is what a hosted agent needs. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: Streamable HTTP reaches a remote server over the network, which is what a hosted agent needs.
- **B:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: Streamable HTTP reaches a remote server over the network, which is what a hosted agent needs.
- **C:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Streamable HTTP reaches a remote server over the network, which is what a hosted agent needs.
- **D:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Streamable HTTP reaches a remote server over the network, which is what a hosted agent needs.

### Question 36 — A

Answer: Configure the MCP server connection with the authentication the server requires. The server connection must be authenticated in the environment where the agent runs. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: The server connection must be authenticated in the environment where the agent runs.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: The server connection must be authenticated in the environment where the agent runs.
- **C:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: The server connection must be authenticated in the environment where the agent runs.
- **D:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: The server connection must be authenticated in the environment where the agent runs.

### Question 37 — C

Answer: Expose only the MCP tools the task needs and review their descriptions. Exposing only the needed tools narrows what a bad instruction can reach and improves selection accuracy. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Exposing only the needed tools narrows what a bad instruction can reach and improves selection accuracy.
- **B:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: Exposing only the needed tools narrows what a bad instruction can reach and improves selection accuracy.
- **C:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: Exposing only the needed tools narrows what a bad instruction can reach and improves selection accuracy.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Exposing only the needed tools narrows what a bad instruction can reach and improves selection accuracy.

### Question 38 — C

Answer: Configure connector authentication so each call uses the caller’s identity. Per-user authentication makes the API evaluate each caller's rights rather than one shared identity. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights rather than one shared identity.
- **B:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights rather than one shared identity.
- **C:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication makes the API evaluate each caller's rights rather than one shared identity.
- **D:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights rather than one shared identity.

### Question 39 — C

Answer: Define the response schema so the agent can reason over the returned fields. A declared response schema lets the model use individual fields in a clear answer. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A declared response schema lets the model use individual fields in a clear answer.
- **B:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A declared response schema lets the model use individual fields in a clear answer.
- **C:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: A declared response schema lets the model use individual fields in a clear answer.
- **D:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A declared response schema lets the model use individual fields in a clear answer.

### Question 40 — D, E

Answers: Create a custom connector from the OpenAPI definition and add it as a tool; Configure connector authentication so each call uses the caller’s identity. A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest.
- **C:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest.
- **D:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest.
- **E:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: A custom connector built from OpenAPI gives typed, reusable operations, and per-user authentication keeps permissions honest.

### Question 41 — C

Answer: Write the parent’s instructions to describe when each child should be used. The parent's instructions describe when each child applies, so an ambiguous delegation rule is the cause. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: The parent's instructions describe when each child applies, so an ambiguous delegation rule is the cause.
- **B:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: The parent's instructions describe when each child applies, so an ambiguous delegation rule is the cause.
- **C:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: The parent's instructions describe when each child applies, so an ambiguous delegation rule is the cause.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: The parent's instructions describe when each child applies, so an ambiguous delegation rule is the cause.

### Question 42 — A

Answer: Give each child a clear input and output contract and keep shared state in the parent. An input and output contract that fixes the identifier format keeps the parent able to combine results. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: An input and output contract that fixes the identifier format keeps the parent able to combine results.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: An input and output contract that fixes the identifier format keeps the parent able to combine results.
- **C:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: An input and output contract that fixes the identifier format keeps the parent able to combine results.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: An input and output contract that fixes the identifier format keeps the parent able to combine results.

### Question 43 — A

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Routing instructions, then children, then routing tests, then tuning based on the evidence. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Routing instructions, then children, then routing tests, then tuning based on the evidence.
- **B:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Routing instructions, then children, then routing tests, then tuning based on the evidence.
- **C:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Routing instructions, then children, then routing tests, then tuning based on the evidence.
- **D:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Routing instructions, then children, then routing tests, then tuning based on the evidence.

### Question 44 — B, D

Answers: Split the work into a parent agent that delegates to specialist child agents; Write the parent’s instructions to describe when each child should be used. Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate.
- **B:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate.
- **C:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate.
- **D:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate.
- **E:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Delegating to specialist children gives each department an owner, and clear routing instructions tell the parent when to delegate.

### Question 45 — D

Answer: Expose the Foundry agent through its endpoint and authenticate with the agent’s identity. Calling the Foundry agent's endpoint keeps orchestration on the Copilot Studio side. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Why the correct answer wins: Calling the Foundry agent's endpoint keeps orchestration on the Copilot Studio side.
- **B:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Calling the Foundry agent's endpoint keeps orchestration on the Copilot Studio side.
- **C:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Calling the Foundry agent's endpoint keeps orchestration on the Copilot Studio side.
- **D:** Correct. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. In this case: Calling the Foundry agent's endpoint keeps orchestration on the Copilot Studio side.

### Question 46 — C

Answer: Deploy the model in Foundry and point the custom prompt at that deployment. Referencing the Foundry deployment lets the prompt use that model without delegating the turn. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Referencing the Foundry deployment lets the prompt use that model without delegating the turn.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Referencing the Foundry deployment lets the prompt use that model without delegating the turn.
- **C:** Correct. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. In this case: Referencing the Foundry deployment lets the prompt use that model without delegating the turn.
- **D:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: Referencing the Foundry deployment lets the prompt use that model without delegating the turn.

### Question 47 — C, E

Answers: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent; Evaluate the Foundry agent against the same test set before it is connected. The agent is connected as a connected agent, and it is evaluated on the shared test set first. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: The agent is connected as a connected agent, and it is evaluated on the shared test set first.
- **B:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: The agent is connected as a connected agent, and it is evaluated on the shared test set first.
- **C:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: The agent is connected as a connected agent, and it is evaluated on the shared test set first.
- **D:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: The agent is connected as a connected agent, and it is evaluated on the shared test set first.
- **E:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: The agent is connected as a connected agent, and it is evaluated on the shared test set first.

### Question 48 — D

Answer: Pin the connected agent’s published version that the parent was tested against. Pinning the published version keeps the tested behaviour in place until the parent is retested. An unpinned dependency can change behaviour between your test run and your release. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Pinning the published version keeps the tested behaviour in place until the parent is retested.
- **B:** Incorrect for this question. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Why the correct answer wins: Pinning the published version keeps the tested behaviour in place until the parent is retested.
- **C:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Pinning the published version keeps the tested behaviour in place until the parent is retested.
- **D:** Correct. An unpinned dependency can change behaviour between your test run and your release. In this case: Pinning the published version keeps the tested behaviour in place until the parent is retested.

### Question 49 — B

Answer: Call the partner’s published API through a custom connector when delegation is unavailable. A custom connector over the endpoint gives the parent a callable tool even when delegation is unavailable. A connector gives the parent a callable tool even when the other organisation will not expose a connected agent. The parent then owns retries and error handling. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A copy forks the behaviour and doubles the maintenance from the first day. Why the correct answer wins: A custom connector over the endpoint gives the parent a callable tool even when delegation is unavailable.
- **B:** Correct. A connector gives the parent a callable tool even when the other organisation will not expose a connected agent. The parent then owns retries and error handling. In this case: A custom connector over the endpoint gives the parent a callable tool even when delegation is unavailable.
- **C:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: A custom connector over the endpoint gives the parent a callable tool even when delegation is unavailable.
- **D:** Incorrect for this question. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Why the correct answer wins: A custom connector over the endpoint gives the parent a callable tool even when delegation is unavailable.

### Question 50 — A

Answer: Define the measures in the semantic model so the data agent answers consistently. Measures defined once in the semantic model remove the per-question interpretation of revenue. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. In this case: Measures defined once in the semantic model remove the per-question interpretation of revenue.
- **B:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Measures defined once in the semantic model remove the per-question interpretation of revenue.
- **C:** Incorrect for this question. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Why the correct answer wins: Measures defined once in the semantic model remove the per-question interpretation of revenue.
- **D:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Measures defined once in the semantic model remove the per-question interpretation of revenue.

### Question 51 — B

Answer: Grant the data agent’s identity read access to the semantic model only. Read access scoped to the required model limits what a bad question can reach. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Read access scoped to the required model limits what a bad question can reach.
- **B:** Correct. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. In this case: Read access scoped to the required model limits what a bad question can reach.
- **C:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Read access scoped to the required model limits what a bad question can reach.
- **D:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: Read access scoped to the required model limits what a bad question can reach.

### Question 52 — B

Answer: Model the remote capability as an A2A skill the agent can discover and invoke. An A2A skill is the callable, discoverable unit the calling agent can select. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: An A2A skill is the callable, discoverable unit the calling agent can select.
- **B:** Correct. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. In this case: An A2A skill is the callable, discoverable unit the calling agent can select.
- **C:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: An A2A skill is the callable, discoverable unit the calling agent can select.
- **D:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: An A2A skill is the callable, discoverable unit the calling agent can select.

### Question 53 — D

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. The agent card documents skills and the endpoint, which is what the caller reads first. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: The agent card documents skills and the endpoint, which is what the caller reads first.
- **B:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: The agent card documents skills and the endpoint, which is what the caller reads first.
- **C:** Incorrect for this question. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Why the correct answer wins: The agent card documents skills and the endpoint, which is what the caller reads first.
- **D:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: The agent card documents skills and the endpoint, which is what the caller reads first.

### Question 54 — D

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary that restricts exposed skills stops a partner from reaching the rest. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: A trust boundary that restricts exposed skills stops a partner from reaching the rest.
- **B:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary that restricts exposed skills stops a partner from reaching the rest.
- **C:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A trust boundary that restricts exposed skills stops a partner from reaching the rest.
- **D:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary that restricts exposed skills stops a partner from reaching the rest.

### Question 55 — C

Answer: Deploy the model in a region that satisfies the data residency requirement. Data residency constrains which deployments are acceptable before cost or quality is compared. Residency is a legal constraint, so region choice precedes price comparison. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Data residency constrains which deployments are acceptable before cost or quality is compared.
- **B:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Data residency constrains which deployments are acceptable before cost or quality is compared.
- **C:** Correct. Residency is a legal constraint, so region choice precedes price comparison. In this case: Data residency constrains which deployments are acceptable before cost or quality is compared.
- **D:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Data residency constrains which deployments are acceptable before cost or quality is compared.

### Question 56 — D

Answer: Provision enough quota and throughput for peak conversation volume. Provisioned throughput must cover peak concurrency, or the agent throttles exactly when it matters. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Provisioned throughput must cover peak concurrency, or the agent throttles exactly when it matters.
- **B:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: Provisioned throughput must cover peak concurrency, or the agent throttles exactly when it matters.
- **C:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Provisioned throughput must cover peak concurrency, or the agent throttles exactly when it matters.
- **D:** Correct. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. In this case: Provisioned throughput must cover peak concurrency, or the agent throttles exactly when it matters.

### Question 57 — A

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Conversation and tool telemetry in Application Insights is the evidence that makes the report investigable. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Conversation and tool telemetry in Application Insights is the evidence that makes the report investigable.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Conversation and tool telemetry in Application Insights is the evidence that makes the report investigable.
- **C:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Conversation and tool telemetry in Application Insights is the evidence that makes the report investigable.
- **D:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Conversation and tool telemetry in Application Insights is the evidence that makes the report investigable.

### Question 58 — B

Answer: Sample telemetry so volume stays affordable while errors are always kept. Sampling with errors always retained controls cost while keeping rare failures visible. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Why the correct answer wins: Sampling with errors always retained controls cost while keeping rare failures visible.
- **B:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sampling with errors always retained controls cost while keeping rare failures visible.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sampling with errors always retained controls cost while keeping rare failures visible.
- **D:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sampling with errors always retained controls cost while keeping rare failures visible.

### Question 59 — C

Answer: Alert on failed tool calls and answer-quality regressions. An alert on failed tool calls turns the trend into a notification with an owner. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: An alert on failed tool calls turns the trend into a notification with an owner.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: An alert on failed tool calls turns the trend into a notification with an owner.
- **C:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: An alert on failed tool calls turns the trend into a notification with an owner.
- **D:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: An alert on failed tool calls turns the trend into a notification with an owner.

### Question 60 — A, B

Answers: Query conversation and tool spans in Application Insights with KQL; Correlate a failed answer with the tool call and knowledge retrieval behind it. Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. In this case: Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path.
- **B:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path.
- **C:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path.
- **D:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path.
- **E:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Correlating spans identifies the dependency, and a KQL query reconstructs that conversation's path.

### Question 61 — A

Answer: Hold part of the set out of prompt tuning so results stay honest. Tuning on every case overfits the prompt, so a held-out slice is needed to measure honestly. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: Tuning on every case overfits the prompt, so a held-out slice is needed to measure honestly.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Tuning on every case overfits the prompt, so a held-out slice is needed to measure honestly.
- **C:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: Tuning on every case overfits the prompt, so a held-out slice is needed to measure honestly.
- **D:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Tuning on every case overfits the prompt, so a held-out slice is needed to measure honestly.

### Question 62 — C

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Real questions, classification, rubric scoring, the failure log, and rerunning on change. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Real questions, classification, rubric scoring, the failure log, and rerunning on change.
- **B:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Real questions, classification, rubric scoring, the failure log, and rerunning on change.
- **C:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Real questions, classification, rubric scoring, the failure log, and rerunning on change.
- **D:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Real questions, classification, rubric scoring, the failure log, and rerunning on change.

### Question 63 — A, C

Answers: Version the test set and rerun it for every change; Hold part of the set out of prompt tuning so results stay honest. Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement.
- **B:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement.
- **C:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement.
- **D:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement.
- **E:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Versioning keeps runs comparable, and a holdout stops the set from being tuned into agreement.

### Question 64 — D

Answer: Have subject-matter experts score a sample against the rubric. Expert scoring against a rubric is the reference standard a regulator can accept as evidence. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Expert scoring against a rubric is the reference standard a regulator can accept as evidence.
- **B:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Expert scoring against a rubric is the reference standard a regulator can accept as evidence.
- **C:** Incorrect for this question. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Why the correct answer wins: Expert scoring against a rubric is the reference standard a regulator can accept as evidence.
- **D:** Correct. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. In this case: Expert scoring against a rubric is the reference standard a regulator can accept as evidence.

### Question 65 — B

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. The rubric, the human sample, the comparison, the adjustment, then full runs. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: The rubric, the human sample, the comparison, the adjustment, then full runs.
- **B:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: The rubric, the human sample, the comparison, the adjustment, then full runs.
- **C:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: The rubric, the human sample, the comparison, the adjustment, then full runs.
- **D:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: The rubric, the human sample, the comparison, the adjustment, then full runs.

### Question 66 — B

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assigning clusters to the owners of the topic, prompt, or connector makes fixes part of planned work. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: Assigning clusters to the owners of the topic, prompt, or connector makes fixes part of planned work.
- **B:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assigning clusters to the owners of the topic, prompt, or connector makes fixes part of planned work.
- **C:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assigning clusters to the owners of the topic, prompt, or connector makes fixes part of planned work.
- **D:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assigning clusters to the owners of the topic, prompt, or connector makes fixes part of planned work.

### Question 67 — B

Answer: Keep the agent in an unmanaged solution in development and ship a managed solution. Authoring happens in the source environment's unmanaged solution, then a new managed build is promoted. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: Authoring happens in the source environment's unmanaged solution, then a new managed build is promoted.
- **B:** Correct. Unmanaged is for authoring, managed is for distribution. Shipping unmanaged to production invites local edits that the next import overwrites. In this case: Authoring happens in the source environment's unmanaged solution, then a new managed build is promoted.
- **C:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: Authoring happens in the source environment's unmanaged solution, then a new managed build is promoted.
- **D:** Incorrect for this question. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Why the correct answer wins: Authoring happens in the source environment's unmanaged solution, then a new managed build is promoted.

### Question 68 — A

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. Components, configuration, export, then pipeline deployment. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: Components, configuration, export, then pipeline deployment.
- **B:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: Components, configuration, export, then pipeline deployment.
- **C:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: Components, configuration, export, then pipeline deployment.
- **D:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: Components, configuration, export, then pipeline deployment.

### Question 69 — D

Answer: Store the secret in a vault and reference it from the environment variable. Vault-backed environment variables keep the secret out of the artefact and the design surface. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: Vault-backed environment variables keep the secret out of the artefact and the design surface.
- **B:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: Vault-backed environment variables keep the secret out of the artefact and the design surface.
- **C:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: Vault-backed environment variables keep the secret out of the artefact and the design surface.
- **D:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: Vault-backed environment variables keep the secret out of the artefact and the design surface.

### Question 70 — D, E

Answers: Define an environment variable for the endpoint and set a value per environment; Set the environment variable values as part of the pipeline deployment step. An environment variable holds the endpoint, and the pipeline sets its value per stage. Environment variables are how one solution behaves differently per environment without code changes. Setting values during deployment removes the manual edit that people forget before a release. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: An environment variable holds the endpoint, and the pipeline sets its value per stage.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable holds the endpoint, and the pipeline sets its value per stage.
- **C:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: An environment variable holds the endpoint, and the pipeline sets its value per stage.
- **D:** Correct. Setting values during deployment removes the manual edit that people forget before a release. In this case: An environment variable holds the endpoint, and the pipeline sets its value per stage.
- **E:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable holds the endpoint, and the pipeline sets its value per stage.

### Question 71 — C

Answer: Import the solution by hand into production for each release. Pipeline stages record the version and the approvals of each promotion. Manual imports skip validation and leave no reliable record of what was deployed when. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: Pipeline stages record the version and the approvals of each promotion.
- **B:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: Pipeline stages record the version and the approvals of each promotion.
- **C:** Correct. Manual imports skip validation and leave no reliable record of what was deployed when. In this case: Pipeline stages record the version and the approvals of each promotion.
- **D:** Incorrect for this question. A staged pipeline makes promotion a recorded operation instead of a manual import. Why the correct answer wins: Pipeline stages record the version and the approvals of each promotion.

### Question 72 — D

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment test step blocks a release that fails the set. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment test step blocks a release that fails the set.
- **B:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment test step blocks a release that fails the set.
- **C:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment test step blocks a release that fails the set.
- **D:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment test step blocks a release that fails the set.

### Question 73 — D

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. Solution, configuration, stages, test step, then the approved deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.
- **B:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.
- **C:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: Solution, configuration, stages, test step, then the approved deployment.
- **D:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: Solution, configuration, stages, test step, then the approved deployment.

### Question 74 — B, C

Answers: Require approval before the production stage runs; Add a pre-deployment step that runs the agent test set and blocks on failure. The test gate supplies quality evidence, and the approval records who accepted the release. An approval records who accepted the risk of the release. It must be a person who can read the test results. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: The test gate supplies quality evidence, and the approval records who accepted the release.
- **B:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: The test gate supplies quality evidence, and the approval records who accepted the release.
- **C:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: The test gate supplies quality evidence, and the approval records who accepted the release.
- **D:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: The test gate supplies quality evidence, and the approval records who accepted the release.
- **E:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: The test gate supplies quality evidence, and the approval records who accepted the release.

### Question 75 — C

Answer: Add a custom pipeline step that calls the validation job. A custom pipeline step can run the scan and return a failure status the pipeline honours. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Why the correct answer wins: A custom pipeline step can run the scan and return a failure status the pipeline honours.
- **B:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: A custom pipeline step can run the scan and return a failure status the pipeline honours.
- **C:** Correct. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. In this case: A custom pipeline step can run the scan and return a failure status the pipeline honours.
- **D:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: A custom pipeline step can run the scan and return a failure status the pipeline honours.

### Question 76 — D

Answer: Keep the previous managed solution version so you can roll back. The previous managed version must be available so it can be redeployed quickly. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: The previous managed version must be available so it can be redeployed quickly.
- **B:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: The previous managed version must be available so it can be redeployed quickly.
- **C:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: The previous managed version must be available so it can be redeployed quickly.
- **D:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: The previous managed version must be available so it can be redeployed quickly.

### Question 77 — C

Answer: Capture user feedback in the conversation and route negative cases to review. In-conversation feedback captures the signal with the transcript attached. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: In-conversation feedback captures the signal with the transcript attached.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: In-conversation feedback captures the signal with the transcript attached.
- **C:** Correct. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. In this case: In-conversation feedback captures the signal with the transcript attached.
- **D:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: In-conversation feedback captures the signal with the transcript attached.

### Question 78 — D

Answer: Alert on rising fallback and handoff rates. A trend alert on fallback and handoff rates raises the problem before users file tickets. Fallback and handoff rates move before anyone files a ticket. A trend alert buys time. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: A trend alert on fallback and handoff rates raises the problem before users file tickets.
- **B:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: A trend alert on fallback and handoff rates raises the problem before users file tickets.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: A trend alert on fallback and handoff rates raises the problem before users file tickets.
- **D:** Correct. Fallback and handoff rates move before anyone files a ticket. A trend alert buys time. In this case: A trend alert on fallback and handoff rates raises the problem before users file tickets.

### Question 79 — B

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real phrasing and missing context are what the agent will actually face, and synthetic cases smooth them away. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Why the correct answer wins: Real phrasing and missing context are what the agent will actually face, and synthetic cases smooth them away.
- **B:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real phrasing and missing context are what the agent will actually face, and synthetic cases smooth them away.
- **C:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real phrasing and missing context are what the agent will actually face, and synthetic cases smooth them away.
- **D:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real phrasing and missing context are what the agent will actually face, and synthetic cases smooth them away.

### Question 80 — B

Answer: Run the tool unattended on a dedicated machine with a vaulted credential. An unattended run on a dedicated machine with a vaulted credential is the supported shape. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape.
- **B:** Correct. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. In this case: An unattended run on a dedicated machine with a vaulted credential is the supported shape.
- **C:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape.
- **D:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: An unattended run on a dedicated machine with a vaulted credential is the supported shape.

### Question 81 — B

Answer: Wrap the internal API as MCP tools and register the server endpoint with the agent. A wrapper that exposes the API as MCP tools gives every agent the same typed interface. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: A wrapper that exposes the API as MCP tools gives every agent the same typed interface.
- **B:** Correct. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. In this case: A wrapper that exposes the API as MCP tools gives every agent the same typed interface.
- **C:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: A wrapper that exposes the API as MCP tools gives every agent the same typed interface.
- **D:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: A wrapper that exposes the API as MCP tools gives every agent the same typed interface.

### Question 82 — C

Answer: Keep failed cases in the test set so they cannot regress. The failed case should have stayed in the set so the defect became a permanent test. A fixed failure becomes a permanent test. Removing it invites the same defect back. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Ownership converts findings into changes. An unowned backlog does not improve the agent. Why the correct answer wins: The failed case should have stayed in the set so the defect became a permanent test.
- **B:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: The failed case should have stayed in the set so the defect became a permanent test.
- **C:** Correct. A fixed failure becomes a permanent test. Removing it invites the same defect back. In this case: The failed case should have stayed in the set so the defect became a permanent test.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: The failed case should have stayed in the set so the defect became a permanent test.

### Question 83 — C

Answer: Connect to the search service over a private endpoint with managed identity. A private endpoint with managed identity keeps traffic private and removes stored keys. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **C:** Correct. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. In this case: A private endpoint with managed identity keeps traffic private and removes stored keys.
- **D:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: A private endpoint with managed identity keeps traffic private and removes stored keys.

### Question 84 — D

Answer: Apply a data loss prevention policy that blocks unapproved connectors in the environment. A data loss prevention policy blocks unapproved connectors before publication. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A data loss prevention policy blocks unapproved connectors before publication.
- **B:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: A data loss prevention policy blocks unapproved connectors before publication.
- **C:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: A data loss prevention policy blocks unapproved connectors before publication.
- **D:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: A data loss prevention policy blocks unapproved connectors before publication.

### Question 85 — C

Answer: Use the current value in production and a default value for development. A current value with a sensible default covers a simple two-environment split. Current and default values cover the common two-environment split and are set explicitly per stage. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: A current value with a sensible default covers a simple two-environment split.
- **B:** Incorrect for this question. Environment variables are how one solution behaves differently per environment without code changes. Why the correct answer wins: A current value with a sensible default covers a simple two-environment split.
- **C:** Correct. Current and default values cover the common two-environment split and are set explicitly per stage. In this case: A current value with a sensible default covers a simple two-environment split.
- **D:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: A current value with a sensible default covers a simple two-environment split.

### Question 86 — C, D

Answers: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream; Authenticate partners through external identities rather than internal tenant accounts. Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key.
- **C:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key.
- **D:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key.
- **E:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Employees need tenant sign-in with their token passed downstream, and suppliers need external identities rather than internal accounts or a shared key.

### Question 87 — D

Answer: Register the database as a knowledge source so the agent can query it directly. Registering the database as a knowledge source lets the agent query structured reference data. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: Registering the database as a knowledge source lets the agent query structured reference data.
- **B:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: Registering the database as a knowledge source lets the agent query structured reference data.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: Registering the database as a knowledge source lets the agent query structured reference data.
- **D:** Correct. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. In this case: Registering the database as a knowledge source lets the agent query structured reference data.

### Question 88 — A

Answer: Route by intent in the parent and pass only the context the child needs. Route in the parent and pass only the fields the chosen child needs, which cuts cost and exposure. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. In this case: Route in the parent and pass only the fields the chosen child needs, which cuts cost and exposure.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Route in the parent and pass only the fields the chosen child needs, which cuts cost and exposure.
- **C:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Route in the parent and pass only the fields the chosen child needs, which cuts cost and exposure.
- **D:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Route in the parent and pass only the fields the chosen child needs, which cuts cost and exposure.

### Question 89 — B

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the governed model, so the measures stay the finance definitions. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: A Fabric data agent answers from the governed model, so the measures stay the finance definitions.
- **B:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the governed model, so the measures stay the finance definitions.
- **C:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the governed model, so the measures stay the finance definitions.
- **D:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the governed model, so the measures stay the finance definitions.

### Question 90 — B

Answer: Extract the shared logic into a reusable component or child agent and reference it. A shared component gives one place to change the behaviour while each country agent keeps its own configuration. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A shared component gives one place to change the behaviour while each country agent keeps its own configuration.
- **B:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: A shared component gives one place to change the behaviour while each country agent keeps its own configuration.
- **C:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A shared component gives one place to change the behaviour while each country agent keeps its own configuration.
- **D:** Incorrect for this question. A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once. Why the correct answer wins: A shared component gives one place to change the behaviour while each country agent keeps its own configuration.

### Question 91 — A, C

Answers: Add a pre-deployment step that runs the agent test set and blocks on failure; Require approval before the production stage runs. The test gate shows the agent passed the set, and the approval records who accepted the release. Testing before promotion is what turns a pipeline into a gate rather than a courier. An approval records who accepted the risk of the release. It must be a person who can read the test results. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: The test gate shows the agent passed the set, and the approval records who accepted the release.
- **B:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: The test gate shows the agent passed the set, and the approval records who accepted the release.
- **C:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: The test gate shows the agent passed the set, and the approval records who accepted the release.
- **D:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: The test gate shows the agent passed the set, and the approval records who accepted the release.
- **E:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: The test gate shows the agent passed the set, and the approval records who accepted the release.

### Question 92 — B

Answer: Turn on audit logging and retain agent conversation records. Audit records with defined retention answer both what was said and why the answer was withheld. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit records with defined retention answer both what was said and why the answer was withheld.
- **B:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit records with defined retention answer both what was said and why the answer was withheld.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit records with defined retention answer both what was said and why the answer was withheld.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit records with defined retention answer both what was said and why the answer was withheld.

### Question 93 — D

Answer: Have subject-matter experts score a sample against the rubric. Expert scoring against a rubric is the reference standard for whether a refusal was right. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Why the correct answer wins: Expert scoring against a rubric is the reference standard for whether a refusal was right.
- **B:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Expert scoring against a rubric is the reference standard for whether a refusal was right.
- **C:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Expert scoring against a rubric is the reference standard for whether a refusal was right.
- **D:** Correct. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. In this case: Expert scoring against a rubric is the reference standard for whether a refusal was right.

### Question 94 — C

Answer: Require the answer to cite retrieved passages and refuse when none are found. Requiring a retrieved citation and refusing when none exists keeps clinical questions out of the agent's mouth. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Requiring a retrieved citation and refusing when none exists keeps clinical questions out of the agent's mouth.
- **B:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Requiring a retrieved citation and refusing when none exists keeps clinical questions out of the agent's mouth.
- **C:** Correct. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. In this case: Requiring a retrieved citation and refusing when none exists keeps clinical questions out of the agent's mouth.
- **D:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: Requiring a retrieved citation and refusing when none exists keeps clinical questions out of the agent's mouth.

### Question 95 — A

Answer: Connect through a Power Platform connector and query it from a tool or flow. A Power Platform connector exposes those operations, and the agent calls them through a tool or flow. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Power Platform connector exposes those operations, and the agent calls them through a tool or flow.
- **B:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: A Power Platform connector exposes those operations, and the agent calls them through a tool or flow.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Power Platform connector exposes those operations, and the agent calls them through a tool or flow.
- **D:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Power Platform connector exposes those operations, and the agent calls them through a tool or flow.

### Question 96 — B, D

Answers: Define typed input and output parameters on the flow and bind them from the topic; Configure a retry policy and terminate with a failure code the topic can read. Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported.
- **B:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported.
- **D:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported.
- **E:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: Typed parameters return a real status, and a retry policy absorbs transient throttling before a failure is reported.

### Question 97 — D

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real transcripts carry the phrasing and missing context the agent will actually meet. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Real transcripts carry the phrasing and missing context the agent will actually meet.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real transcripts carry the phrasing and missing context the agent will actually meet.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real transcripts carry the phrasing and missing context the agent will actually meet.
- **D:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real transcripts carry the phrasing and missing context the agent will actually meet.

### Question 98 — C

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway reaches the system without an inbound firewall path. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway reaches the system without an inbound firewall path.
- **B:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway reaches the system without an inbound firewall path.
- **C:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway reaches the system without an inbound firewall path.
- **D:** Incorrect for this question. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Why the correct answer wins: An on-premises data gateway reaches the system without an inbound firewall path.

### Question 99 — B

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. A retrievable document version field in the schema is what makes the citation verifiable. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: A retrievable document version field in the schema is what makes the citation verifiable.
- **B:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: A retrievable document version field in the schema is what makes the citation verifiable.
- **C:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: A retrievable document version field in the schema is what makes the citation verifiable.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: A retrievable document version field in the schema is what makes the citation verifiable.

### Question 100 — A

Answer: Track containment, resolution, and escalation metrics on a dashboard. Operational metrics such as handling time and resolution rate are the evidence a sponsor can act on. Operational metrics show whether the agent is helping. They are the business case for the next release. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Operational metrics show whether the agent is helping. They are the business case for the next release. In this case: Operational metrics such as handling time and resolution rate are the evidence a sponsor can act on.
- **B:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Operational metrics such as handling time and resolution rate are the evidence a sponsor can act on.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Operational metrics such as handling time and resolution rate are the evidence a sponsor can act on.
- **D:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: Operational metrics such as handling time and resolution rate are the evidence a sponsor can act on.
