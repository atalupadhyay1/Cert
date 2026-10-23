# Microsoft AB-620 — Full-Length Mock Exam 5

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. An energy trader wants the agent to answer from five years of settlement history held in a lakehouse. Which integration fits?

Domain: Plan and configure agent solutions

- A. Copy the records nightly into Dataverse and answer from the copy
- B. Batch the requests and post them to the source system on a schedule
- C. Call the internal endpoint straight from the topic over HTTP
- D. Mirror the source into Microsoft Fabric and query it with a Fabric data agent

### 2. A clinic wants appointment data visible inside Dataverse so the agent reads it like a native table. Which option fits?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Mediate the on-premises call through an on-premises data gateway
- C. Copy the records nightly into Dataverse and answer from the copy
- D. Expose the system through a virtual table or connector view that the agent can read

### 3. Contractors outside the tenant must reach the agent with their own credentials. What should the identity plan use?

Domain: Plan and configure agent solutions

- A. Allow anonymous access to the agent and authenticate only at the API
- B. Give every conversation a single shared service account credential for the API
- C. Store one API key in a topic variable and reuse it for every user
- D. Authenticate partners through external identities rather than internal tenant accounts

### 4. The agent must call a clinical records API as the signed-in clinician. Which flow carries that identity?

Domain: Plan and configure agent solutions

- A. Use the on-behalf-of flow so the agent calls the API as the signed-in user
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Store one API key in a topic variable and reuse it for every user
- D. Give every conversation a single shared service account credential for the API

### 5. An agent reads a records API and an Azure AI Search index. Which two identity choices apply? Select two.

Domain: Plan and configure agent solutions

- A. Allow anonymous access to the agent and authenticate only at the API
- B. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- C. Store one API key in a topic variable and reuse it for every user
- D. Use the agent managed identity for Azure resources and keep user identity for business data
- E. Give every conversation a single shared service account credential for the API

### 6. Patients must reach the agent from a public site before they have any account. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Embed the agent in a custom application through the Direct Line channel
- C. Publish to email and answer asynchronously
- D. Publish to a public website with authenticated sign-in

### 7. A hospital group will embed the agent in its own patient app with the app's sign-in. Which channel fits?

Domain: Plan and configure agent solutions

- A. Embed the agent in a custom application through the Direct Line channel
- B. Publish to email and answer asynchronously
- C. Publish to Microsoft Teams and keep the agent inside the tenant
- D. Add the channel for omni-channel engagement so external support queues can route to it

### 8. Staff should find the agent beside other agents inside the Microsoft 365 Copilot experience. Which option fits?

Domain: Plan and configure agent solutions

- A. Publish to a public website with authenticated sign-in
- B. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents
- C. Publish to Microsoft Teams and keep the agent inside the tenant
- D. Publish to email and answer asynchronously

### 9. Contractors may read procedures but never incident reports held in the same library. What must be enforced?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Enforce the source system’s permissions in the knowledge layer so answers respect access
- C. Turn on audit logging and retain agent conversation records
- D. Apply a data loss prevention policy that blocks unapproved connectors in the environment

### 10. An audit asks which answers were given to a named clinician last month. What should be enabled?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Turn on audit logging and retain agent conversation records
- C. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- D. Separate development and production environments with environment security groups

### 11. A retrieved procedure document contains an instruction to ignore the agent's rules. Which control reduces the risk?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Separate development and production environments with environment security groups
- C. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- D. Turn on audit logging and retain agent conversation records

### 12. A hospital is opening agent building to clinical and administrative staff. Which two controls belong in the rollout? Select two.

Domain: Plan and configure agent solutions

- A. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- B. Restrict who can author and publish with Copilot Studio security roles
- C. Turn on audit logging and retain agent conversation records
- D. Separate development and production environments with environment security groups
- E. Constrain the tools the agent may call, validate tool output, and limit autonomous actions

### 13. Four clinic agents need the same eligibility dialogue that changes quarterly. What should be built?

Domain: Plan and configure agent solutions

- A. Parameterize environment-specific values with environment variables
- B. Copy the topics into each agent so every team can edit its own copy
- C. Extract the shared logic into a reusable component or child agent and reference it
- D. Rebuild the same topic in each agent to avoid a shared dependency

### 14. A team is releasing a shared clinical dialogue through three environments. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- B. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- C. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- D. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream

### 15. A topic must validate a referral, call two services, and return a case number. What should be created?

Domain: Plan and configure agent solutions

- A. Create the flow with the connector action the agent needs and return the result
- B. Create an agent flow with a manual trigger that the topic calls with inputs
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Use an automated cloud flow triggered by an event and have the agent wait for it

### 16. A flow fails at a connector step and the conversation ends without a message. What should be added?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Create an agent flow with a manual trigger that the topic calls with inputs
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Define typed input and output parameters on the flow and bind them from the topic

### 17. The flow completes but the topic shows an empty confirmation. What is missing?

Domain: Plan and configure agent solutions

- A. Use an automated cloud flow triggered by an event and have the agent wait for it
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Create the flow with the connector action the agent needs and return the result
- D. Define typed input and output parameters on the flow and bind them from the topic

### 18. A referral flow will be called by two topics in two agents. Which two features make it safe to reuse? Select two.

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Create an agent flow with a manual trigger that the topic calls with inputs
- D. Use an automated cloud flow triggered by an event and have the agent wait for it
- E. Add the capability as a connector action so the agent can call it without a flow

### 19. A patient asks for an exception to a booking rule that only a clinician may grant. What should the agent do?

Domain: Plan and configure agent solutions

- A. Have the agent draft the action and require a person to submit it in the source system
- B. Hand the conversation off to a live agent with the context attached
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Let the agent complete the action and notify a person afterwards

### 20. Every referral letter must leave under a clinician's own signature. Which pattern fits?

Domain: Plan and configure agent solutions

- A. Send an approval request and pause the flow until a person responds
- B. Let the agent complete the action and notify a person afterwards
- C. Post an adaptive card to Teams and wait for the human decision before continuing
- D. Have the agent draft the action and require a person to submit it in the source system

### 21. An imaging API returns a timeout a few times an hour and users see failures. What should change?

Domain: Plan and configure agent solutions

- A. Configure a retry policy and terminate with a failure code the topic can read
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Add a comment step to the flow describing the expected failure
- D. Review the flow run history and its action-level inputs and outputs

### 22. A failure recurs but the run history has rotated away. What should be enabled?

Domain: Plan and configure agent solutions

- A. Use the Copilot Studio analytics view for session and topic outcomes
- B. Add a comment step to the flow describing the expected failure
- C. Send flow telemetry to Application Insights and query the traces
- D. Review the flow run history and its action-level inputs and outputs

### 23. An operations team must detect and investigate flow failures. Which two capabilities apply? Select two.

Domain: Plan and configure agent solutions

- A. Send flow telemetry to Application Insights and query the traces
- B. Review the flow run history and its action-level inputs and outputs
- C. Use the Copilot Studio analytics view for session and topic outcomes
- D. Configure an alert on failed runs and route it to the owning team
- E. Add a comment step to the flow describing the expected failure

### 24. A patient identifier collected at the start must filter answers in every later topic. Which choice fits?

Domain: Plan and configure agent solutions

- A. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- B. Configure the message node to send a formatted message with the fields the user needs
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Store the value in a global variable so later topics can read it

### 25. A booking summary needs four labelled values and a confirm action. What should the topic return?

Domain: Plan and configure agent solutions

- A. Configure the topic as a redirect target with its own trigger phrases
- B. Return an adaptive card so the data renders in labelled fields
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Return the raw flow output as plain text

### 26. A topic collects a one-time code and returns a formatted summary. Which two choices apply? Select two.

Domain: Plan and configure agent solutions

- A. Return the raw flow output as plain text
- B. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Configure the message node to send a formatted message with the fields the user needs
- E. Store the value in a global variable so later topics can read it

### 27. Answers are accurate but include medical abbreviations that patients do not understand. What should be configured?

Domain: Plan and configure agent solutions

- A. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- B. Require the answer to cite retrieved passages and refuse when none are found
- C. Add a fallback topic for low-confidence answers that hands off to a person
- D. Point the generative answers node at the specific knowledge source for the question

### 28. A safety review requires the agent to refuse when the library has no relevant passage. Which configuration enforces that?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- C. Require the answer to cite retrieved passages and refuse when none are found
- D. Add a fallback topic for low-confidence answers that hands off to a person

### 29. Procedure documents live in a SharePoint library whose permissions must keep applying. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the source through a Copilot connector so its content is indexed for answers
- B. Add the SharePoint site as a knowledge source and rely on item-level permissions
- C. Upload the documents as file knowledge on the agent
- D. Register the database as a knowledge source so the agent can query it directly

### 30. The agent must post a work order through an operational system rather than search content. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Upload the documents as file knowledge on the agent
- B. Connect through a Power Platform connector and query it from a tool or flow
- C. Index the content in Azure AI Search and use it as the knowledge source
- D. Connect the source through a Copilot connector so its content is indexed for answers

### 31. A team is connecting document knowledge and an operational system to one agent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Review unsupported questions → test answers with users of different access → connect and scope the knowledge → inventory the sources and their permissions → choose the connector or index for each
- B. Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions
- C. Test answers with users of different access → inventory the sources and their permissions → choose the connector or index for each → review unsupported questions → connect and scope the knowledge
- D. Connect and scope the knowledge → choose the connector or index for each → inventory the sources and their permissions → test answers with users of different access → review unsupported questions

### 32. Two corpora need different permission and ranking behaviour. Which two statements are correct? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Upload the documents as file knowledge on the agent
- C. Connect through a Power Platform connector and query it from a tool or flow
- D. Register the database as a knowledge source so the agent can query it directly
- E. Connect the source through a Copilot connector so its content is indexed for answers

### 33. Two clinics hold identical wording, and each must see only its own copy. Where must the restriction apply?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Recreate the index on every publish so it never goes stale
- C. Enable semantic ranking and let the agent use the reranked results
- D. Apply a security filter on the query before the agent composes an answer

### 34. An index must return a document version and filter by clinic. What should be designed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Enable semantic ranking and let the agent use the reranked results
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Connect to the search service over a private endpoint with managed identity

### 35. Users search by referral number and by description, and numbers are missed. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Enable semantic ranking and let the agent use the reranked results
- C. Use hybrid retrieval with vector and keyword queries
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 36. A search owner must explain a rise in query latency. Which two settings add cost? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Use hybrid retrieval with vector and keyword queries
- B. Recreate the index on every publish so it never goes stale
- C. Enable semantic ranking and let the agent use the reranked results
- D. Connect to the search service over a private endpoint with managed identity
- E. Apply a security filter on the query before the agent composes an answer

### 37. A radiology scheduling tool has no API and the agent must book a slot in it. Which capability fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure a computer use tool against the legacy desktop application
- B. Provision a machine or machine group and run the tool there with a dedicated account
- C. Replace the screen automation with an API once the application exposes one
- D. Run the tool unattended on a dedicated machine with a vaulted credential

### 38. A computer use job silently booked the wrong appointment after a vendor update. Which practice exposes that?

Domain: Integrate and extend agents in Copilot Studio

- A. Monitor computer use runs and capture step screenshots for review
- B. Record the click path once and reuse it without validating each run
- C. Configure a computer use tool against the legacy desktop application
- D. Replace the screen automation with an API once the application exposes one

### 39. A hospital is onboarding computer use for a licensed desktop tool. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record
- B. Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes
- C. Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes
- D. Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record

### 40. An MCP tool fails with unauthorized although it appears in the agent's tool list. What should be fixed?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose only the MCP tools the task needs and review their descriptions
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Use a streamable HTTP MCP server so the agent can reach it over the network
- D. Configure the MCP server connection with the authentication the server requires

### 41. A platform team publishes clinical reference tools that several agents reuse. Which integration fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Embed the MCP server as a local process inside the agent
- B. Add an MCP server as a tool and let the agent discover the tools it exposes
- C. Wrap the internal API as MCP tools and register the server endpoint with the agent
- D. Use a streamable HTTP MCP server so the agent can reach it over the network

### 42. A server offers 40 tools and the agent needs three. What should the review require?

Domain: Integrate and extend agents in Copilot Studio

- A. Wrap the internal API as MCP tools and register the server endpoint with the agent
- B. Expose only the MCP tools the task needs and review their descriptions
- C. Add an MCP server as a tool and let the agent discover the tools it exposes
- D. Configure the MCP server connection with the authentication the server requires

### 43. The MCP server runs outside the agent's hosting environment. Which transport applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Use a streamable HTTP MCP server so the agent can reach it over the network
- B. Embed the MCP server as a local process inside the agent
- C. Configure the MCP server connection with the authentication the server requires
- D. Add an MCP server as a tool and let the agent discover the tools it exposes

### 44. A coverage API currently receives one shared key for all callers. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure connector authentication so each call uses the caller’s identity
- B. Create a custom connector from the OpenAPI definition and add it as a tool
- C. Hard-code the endpoint URL and key inside the topic
- D. Call the API from an agent flow and return the parsed response to the topic

### 45. A coverage response must be reshaped and retried before the agent reads it. Where should the call live?

Domain: Integrate and extend agents in Copilot Studio

- A. Define the response schema so the agent can reason over the returned fields
- B. Call the REST API from a topic with a Send HTTP request action
- C. Call the API from an agent flow and return the parsed response to the topic
- D. Hard-code the endpoint URL and key inside the topic

### 46. A coverage API becomes a tool for several clinical agents. Which two controls apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Call the REST API from a topic with a Send HTTP request action
- B. Create a custom connector from the OpenAPI definition and add it as a tool
- C. Hard-code the endpoint URL and key inside the topic
- D. Configure connector authentication so each call uses the caller’s identity
- E. Define the response schema so the agent can reason over the returned fields

### 47. Fourteen departments share one agent, and each wants its own change calendar. What should the architect do?

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Route by intent in the parent and pass only the context the child needs
- C. Give every child the same knowledge source so answers stay consistent
- D. Split the work into a parent agent that delegates to specialist child agents

### 48. A parent rarely delegates to the billing child and answers billing itself. What should be fixed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Give every child the same knowledge source so answers stay consistent
- B. Write the parent’s instructions to describe when each child should be used
- C. Route by intent in the parent and pass only the context the child needs
- D. Give each child a clear input and output contract and keep shared state in the parent

### 49. A child returns a patient reference the parent cannot join to its own record. What should be agreed?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Build one large agent with every topic so there is a single place to change
- C. Give every child the same knowledge source so answers stay consistent
- D. Give each child a clear input and output contract and keep shared state in the parent

### 50. An architect is consolidating 14 agents into a parent with children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions
- B. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- C. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions
- D. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent

### 51. A parent routes one question across three children, and each answers from a different policy copy. Which two changes help? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Split the work into a parent agent that delegates to specialist child agents
- B. Build one large agent with every topic so there is a single place to change
- C. Give each child a clear input and output contract and keep shared state in the parent
- D. Route by intent in the parent and pass only the context the child needs
- E. Give every child the same knowledge source so answers stay consistent

### 52. A Foundry agent with custom tools has passed evaluation and must answer inside Copilot Studio. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- B. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Deploy the model in Foundry and point the custom prompt at that deployment

### 53. A connected Foundry agent is worse inside the parent than standalone. What was missed?

Domain: Integrate and extend agents in Copilot Studio

- A. Evaluate the Foundry agent against the same test set before it is connected
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Deploy the model in Foundry and point the custom prompt at that deployment

### 54. A custom prompt must use a Foundry deployment and agree with the parent's facts. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Deploy the model in Foundry and point the custom prompt at that deployment
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Ground the Foundry agent in the same indexed knowledge so both layers answer consistently
- D. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- E. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent

### 55. Two published department agents must be reused by a parent without forking them. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Confirm the caller’s identity and permissions flow through to the connected agent
- B. Write a precise name and description for the connected agent so routing works
- C. Add the existing agent as a connected agent and let the parent delegate to it
- D. Copy its topics into the new agent so both can be edited separately

### 56. A parent routes questions to the wrong child because both descriptions are generic. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Write a precise name and description for the connected agent so routing works
- B. Retire the duplicate standalone agent once the parent covers its use cases
- C. Pin the connected agent’s published version that the parent was tested against
- D. Confirm the caller’s identity and permissions flow through to the connected agent

### 57. Clinical utilisation questions must match the measures the analysts publish. Which approach fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- B. Export the data nightly into files the agent can search
- C. Query the lakehouse directly from the agent with a SQL tool
- D. Define the measures in the semantic model so the data agent answers consistently

### 58. A data agent has workspace-wide access but answers from one model. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- C. Export the data nightly into files the agent can search
- D. Grant the data agent’s identity read access to the semantic model only

### 59. A partner must discover an internal agent's capabilities before calling it. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish an agent card that describes the remote agent’s skills and endpoint
- B. Track the remote task state and surface long-running results back into the conversation
- C. Model the remote capability as an A2A skill the agent can discover and invoke
- D. Configure authentication between the agents so calls are authorized

### 60. A remote agent takes minutes and the caller reports nothing in the meantime. What is missing?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish an agent card that describes the remote agent’s skills and endpoint
- B. Rebuild the remote agent’s functionality locally instead of using the protocol
- C. Track the remote task state and surface long-running results back into the conversation
- D. Configure authentication between the agents so calls are authorized

### 61. A partner agent should reach two internal skills only. What should be defined?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure authentication between the agents so calls are authorized
- B. Publish an agent card that describes the remote agent’s skills and endpoint
- C. Model the remote capability as an A2A skill the agent can discover and invoke
- D. Define which remote agents are trusted and restrict the skills exposed to them

### 62. A pilot supports 30 users and production expects 3,000, and throttling has started. What should be reviewed?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision enough quota and throughput for peak conversation volume
- B. Deploy the model in a region that satisfies the data residency requirement
- C. Choose a model from the catalog that meets quality, latency, and residency needs
- D. Deploy the chosen model and reference the deployment from the custom prompt

### 63. A new workload must meet a latency target and a fixed budget. What should be decided first?

Domain: Integrate and extend agents in Copilot Studio

- A. Keep the default model because it is already configured
- B. Choose a model from the catalog that meets quality, latency, and residency needs
- C. Deploy the chosen model and reference the deployment from the custom prompt
- D. Provision enough quota and throughput for peak conversation volume

### 64. A clinician reports a wrong answer and no record exists. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Query conversation and tool spans in Application Insights with KQL
- C. Alert on failed tool calls and answer-quality regressions
- D. Sample telemetry so volume stays affordable while errors are always kept

### 65. A specific bad answer must be traced through retrieval and tools. What should be used?

Domain: Integrate and extend agents in Copilot Studio

- A. Query conversation and tool spans in Application Insights with KQL
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Alert on failed tool calls and answer-quality regressions

### 66. Telemetry costs grow faster than conversation volume. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Correlate a failed answer with the tool call and knowledge retrieval behind it
- B. Log full conversation transcripts indefinitely without retention limits
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Sample telemetry so volume stays affordable while errors are always kept

### 67. An on-call team needs detection and root cause. Which two capabilities apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Log full conversation transcripts indefinitely without retention limits
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Correlate a failed answer with the tool call and knowledge retrieval behind it
- E. Alert on failed tool calls and answer-quality regressions

### 68. A test set was written from topic titles alone. What should be added?

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Test with a handful of happy-path questions before release
- C. Build the test set from real anonymized conversations plus the cases that must never fail
- D. Generate synthetic cases from the topics and intents the agent supports

### 69. A red team wants evidence about out-of-scope and injection attempts. Which cases cover that?

Domain: Test and manage agents

- A. Version the test set and rerun it for every change
- B. Hold part of the set out of prompt tuning so results stay honest
- C. Include adversarial and edge cases such as out-of-scope and injection attempts
- D. Test with a handful of happy-path questions before release

### 70. A quality lead is building the evaluation loop. Which sequence is correct?

Domain: Test and manage agents

- A. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- B. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change
- C. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent
- D. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change

### 71. A set will gate releases for a year. Which two practices keep it honest? Select two.

Domain: Test and manage agents

- A. Generate synthetic cases from the topics and intents the agent supports
- B. Test with a handful of happy-path questions before release
- C. Version the test set and rerun it for every change
- D. Build the test set from real anonymized conversations plus the cases that must never fail
- E. Hold part of the set out of prompt tuning so results stay honest

### 72. A clinical board asks how answer appropriateness was judged before launch. Which method is most defensible?

Domain: Test and manage agents

- A. Rely on the builder trying a few questions in the test pane
- B. Score answers with keyword matching against expected phrases
- C. Use model-based grading against a rubric and review a human sample
- D. Have subject-matter experts score a sample against the rubric

### 73. A team is calibrating automated grading. Which sequence is correct?

Domain: Test and manage agents

- A. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand
- B. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores
- C. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- D. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores

### 74. Sixty failures are being triaged individually although four causes repeat. What should the team do?

Domain: Test and manage agents

- A. Group failures by topic and root cause instead of fixing items one at a time
- B. Compare the new run against the previous baseline before publishing
- C. Publish when the overall average looks acceptable
- D. Keep failed cases in the test set so they cannot regress

### 75. Findings never turn into changes because nobody owns them. What should be introduced?

Domain: Test and manage agents

- A. Group failures by topic and root cause instead of fixing items one at a time
- B. Keep failed cases in the test set so they cannot regress
- C. Assign each failure cluster to the owner of the topic, prompt, or connector
- D. Publish when the overall average looks acceptable

### 76. An agent must travel with its flows and connections to another environment. What must exist first?

Domain: Test and manage agents

- A. Send the agents topic files to the administrator by email
- B. Create a solution and add the agent and its dependencies to it
- C. Set the publisher prefix before creating components so names stay consistent
- D. Export the managed solution and import it into the target environment

### 77. A solution is being prepared for promotion. Which sequence is correct?

Domain: Test and manage agents

- A. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- B. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- C. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- D. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables

### 78. A solution hard-codes a pilot endpoint that will be wrong in production. What should replace it?

Domain: Test and manage agents

- A. Define an environment variable for the endpoint and set a value per environment
- B. Hard-code the production endpoint in the topic and change it after import
- C. Set the environment variable values as part of the pipeline deployment step
- D. Store the secret in a vault and reference it from the environment variable

### 79. A connector key appears in a solution export. Where should it live?

Domain: Test and manage agents

- A. Use the current value in production and a default value for development
- B. Hard-code the production endpoint in the topic and change it after import
- C. Record the required values in the deployment notes for each environment
- D. Store the secret in a vault and reference it from the environment variable

### 80. A two-environment solution needs per-stage values without a vault requirement. Which two practices apply? Select two.

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Store the secret in a vault and reference it from the environment variable
- C. Use the current value in production and a default value for development
- D. Set the environment variable values as part of the pipeline deployment step
- E. Record the required values in the deployment notes for each environment

### 81. A test-covered defect reached production. What should the pipeline add?

Domain: Test and manage agents

- A. Import the solution by hand into production for each release
- B. Require approval before the production stage runs
- C. Add a pre-deployment step that runs the agent test set and blocks on failure
- D. Use the pipeline analytics to see which stage failed and why

### 82. A release must record who accepted the risk. What should be configured?

Domain: Test and manage agents

- A. Use the pipeline analytics to see which stage failed and why
- B. Import the solution by hand into production for each release
- C. Require approval before the production stage runs
- D. Add a pre-deployment step that runs the agent test set and blocks on failure

### 83. A team is setting up a gated pipeline. Which sequence is correct?

Domain: Test and manage agents

- A. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage
- B. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval
- C. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval
- D. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step

### 84. A regulated pipeline needs per-stage values and reversibility. Which two controls apply? Select two.

Domain: Test and manage agents

- A. Keep the previous managed solution version so you can roll back
- B. Deploy only the components that changed when the pipeline supports it
- C. Pass environment-specific values through pipeline configuration rather than editing the solution
- D. Notify the owning team with the deployment result and the failed step
- E. Deploy on a fixed schedule regardless of readiness

### 85. A one-topic fix redeploys forty components. What should change?

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Notify the owning team with the deployment result and the failed step
- C. Deploy on a fixed schedule regardless of readiness
- D. Pass environment-specific values through pipeline configuration rather than editing the solution

### 86. Failures are discovered at the next standup. What should be added?

Domain: Test and manage agents

- A. Keep the previous managed solution version so you can roll back
- B. Deploy only the components that changed when the pipeline supports it
- C. Notify the owning team with the deployment result and the failed step
- D. Deploy on a fixed schedule regardless of readiness

### 87. A policy library was revised and answers silently changed. Which control catches this?

Domain: Test and manage agents

- A. Capture user feedback in the conversation and route negative cases to review
- B. Watch for knowledge-source changes and re-run the evaluation after they land
- C. Test once before launch and assume behaviour stays stable
- D. Track containment, resolution, and escalation metrics on a dashboard

### 88. A year after launch nobody can show whether quality held. What should be introduced?

Domain: Test and manage agents

- A. Track containment, resolution, and escalation metrics on a dashboard
- B. Alert on rising fallback and handoff rates
- C. Sample production conversations and score them against the rubric on a schedule
- D. Test once before launch and assume behaviour stays stable

---

## Case study — Brightwater Water

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. The work-order API is unavailable during storms and the conversation ends silently. What should the flow provide?

Domain: Plan and configure agent solutions

- A. Create an agent flow with a manual trigger that the topic calls with inputs
- B. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Define typed input and output parameters on the flow and bind them from the topic

### 90. Storms produce unusual requests and six times the volume. What should the test set include?

Domain: Test and manage agents

- A. Hold part of the set out of prompt tuning so results stay honest
- B. Test with a handful of happy-path questions before release
- C. Version the test set and rerun it for every change
- D. Include adversarial and edge cases such as out-of-scope and injection attempts

### 91. Success is measured by work orders created without a phone call. What should the team track on a dashboard?

Domain: Test and manage agents

- A. Capture user feedback in the conversation and route negative cases to review
- B. Test once before launch and assume behaviour stays stable
- C. Sample production conversations and score them against the rubric on a schedule
- D. Track containment, resolution, and escalation metrics on a dashboard

---

## Case study — Granite Health

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A clinician must approve and send every referral response personally. Which pattern fits?

Domain: Plan and configure agent solutions

- A. Let the agent complete the action and notify a person afterwards
- B. Send an approval request and pause the flow until a person responds
- C. Post an adaptive card to Teams and wait for the human decision before continuing
- D. Have the agent draft the action and require a person to submit it in the source system

### 93. The coverage API must apply each clinician's rights and expose named fields. Which two controls apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Call the API from an agent flow and return the parsed response to the topic
- B. Configure connector authentication so each call uses the caller’s identity
- C. Call the REST API from a topic with a Send HTTP request action
- D. Hard-code the endpoint URL and key inside the topic
- E. Define the response schema so the agent can reason over the returned fields

### 94. Granite must show that draft quality was judged by clinicians before release. Which method gives that evidence?

Domain: Test and manage agents

- A. Score answers with keyword matching against expected phrases
- B. Use model-based grading against a rubric and review a human sample
- C. Have subject-matter experts score a sample against the rubric
- D. Rely on the builder trying a few questions in the test pane

---

## Case study — Northgate Bank

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Fourteen department behaviours share common logic but need different endpoints. Which two practices apply? Select two.

Domain: Plan and configure agent solutions

- A. Rebuild the same topic in each agent to avoid a shared dependency
- B. Package the shared topics, flows, and connection references in a solution
- C. Extract the shared logic into a reusable component or child agent and reference it
- D. Copy the topics into each agent so every team can edit its own copy
- E. Parameterize environment-specific values with environment variables

### 96. Fourteen department agents are being consolidated under one parent. What should each department keep?

Domain: Integrate and extend agents in Copilot Studio

- A. Route by intent in the parent and pass only the context the child needs
- B. Split the work into a parent agent that delegates to specialist child agents
- C. Build one large agent with every topic so there is a single place to change
- D. Give every child the same knowledge source so answers stay consistent

### 97. Routing failures are reported one at a time across departments. What should the parent team do?

Domain: Test and manage agents

- A. Keep failed cases in the test set so they cannot regress
- B. Publish when the overall average looks acceptable
- C. Group failures by topic and root cause instead of fixing items one at a time
- D. Compare the new run against the previous baseline before publishing

---

## Case study — Solstice Energy

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Contractors outside the tenant need their own sign-in to reach the agent. Which identity decision fits?

Domain: Plan and configure agent solutions

- A. Give every conversation a single shared service account credential for the API
- B. Allow anonymous access to the agent and authenticate only at the API
- C. Authenticate partners through external identities rather than internal tenant accounts
- D. Store one API key in a topic variable and reuse it for every user

### 99. Contractors may read maintenance procedures but not incident reports in the same library. What must be enforced?

Domain: Plan and configure agent solutions

- A. Enforce the source system’s permissions in the knowledge layer so answers respect access
- B. Turn on audit logging and retain agent conversation records
- C. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- D. Separate development and production environments with environment security groups

### 100. The procedure index must never return an incident report to a contractor. Where must that be enforced?

Domain: Integrate and extend agents in Copilot Studio

- A. Enable semantic ranking and let the agent use the reranked results
- B. Connect to the search service over a private endpoint with managed identity
- C. Recreate the index on every publish so it never goes stale
- D. Apply a security filter on the query before the agent composes an answer

---

## Answer key and explanations

### Question 1 — D

Answer: Mirror the source into Microsoft Fabric and query it with a Fabric data agent. Mirroring into Fabric and answering through a data agent removes load from the source and keeps measures governed. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: Mirroring into Fabric and answering through a data agent removes load from the source and keeps measures governed.
- **B:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: Mirroring into Fabric and answering through a data agent removes load from the source and keeps measures governed.
- **C:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: Mirroring into Fabric and answering through a data agent removes load from the source and keeps measures governed.
- **D:** Correct. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. In this case: Mirroring into Fabric and answering through a data agent removes load from the source and keeps measures governed.

### Question 2 — D

Answer: Expose the system through a virtual table or connector view that the agent can read. A virtual table projects the external data into Dataverse, provided the source supports the queries. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: A virtual table projects the external data into Dataverse, provided the source supports the queries.
- **B:** Incorrect for this question. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Why the correct answer wins: A virtual table projects the external data into Dataverse, provided the source supports the queries.
- **C:** Incorrect for this question. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Why the correct answer wins: A virtual table projects the external data into Dataverse, provided the source supports the queries.
- **D:** Correct. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. In this case: A virtual table projects the external data into Dataverse, provided the source supports the queries.

### Question 3 — D

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities give contractors their own credentials without internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities give contractors their own credentials without internal accounts.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities give contractors their own credentials without internal accounts.
- **C:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: External identities give contractors their own credentials without internal accounts.
- **D:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities give contractors their own credentials without internal accounts.

### Question 4 — A

Answer: Use the on-behalf-of flow so the agent calls the API as the signed-in user. On-behalf-of passes the clinician's identity so the API applies their own permissions. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. In this case: On-behalf-of passes the clinician's identity so the API applies their own permissions.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: On-behalf-of passes the clinician's identity so the API applies their own permissions.
- **C:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: On-behalf-of passes the clinician's identity so the API applies their own permissions.
- **D:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: On-behalf-of passes the clinician's identity so the API applies their own permissions.

### Question 5 — B, D

Answers: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream; Use the agent managed identity for Azure resources and keep user identity for business data. User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key.
- **B:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key.
- **C:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key.
- **D:** Correct. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. In this case: User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key.
- **E:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: User sign-in provides attribution and per-caller filtering, and the managed identity covers the Azure resource without a key.

### Question 6 — D

Answer: Publish to a public website with authenticated sign-in. The website channel serves external visitors and can require sign-in only where needed. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: The website channel serves external visitors and can require sign-in only where needed.
- **B:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: The website channel serves external visitors and can require sign-in only where needed.
- **C:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: The website channel serves external visitors and can require sign-in only where needed.
- **D:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: The website channel serves external visitors and can require sign-in only where needed.

### Question 7 — A

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line gives the host app control of the interface and authentication. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line gives the host app control of the interface and authentication.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Direct Line gives the host app control of the interface and authentication.
- **C:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Direct Line gives the host app control of the interface and authentication.
- **D:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Direct Line gives the host app control of the interface and authentication.

### Question 8 — B

Answer: Publish the agent into Microsoft 365 Copilot so it appears alongside other agents. Publishing into Copilot surfaces the agent where staff already work. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.
- **B:** Correct. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. In this case: Publishing into Copilot surfaces the agent where staff already work.
- **C:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.
- **D:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Publishing into Copilot surfaces the agent where staff already work.

### Question 9 — B

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer keeps restricted content out of their answers. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Permission trimming in the knowledge layer keeps restricted content out of their answers.
- **B:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer keeps restricted content out of their answers.
- **C:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer keeps restricted content out of their answers.
- **D:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer keeps restricted content out of their answers.

### Question 10 — B

Answer: Turn on audit logging and retain agent conversation records. Audit logging with retention records the answers and their context. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit logging with retention records the answers and their context.
- **B:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit logging with retention records the answers and their context.
- **C:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit logging with retention records the answers and their context.
- **D:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit logging with retention records the answers and their context.

### Question 11 — C

Answer: Constrain the tools the agent may call, validate tool output, and limit autonomous actions. Limiting tools, validating output, and requiring approval for irreversible actions contains the instruction. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Limiting tools, validating output, and requiring approval for irreversible actions contains the instruction.
- **B:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Limiting tools, validating output, and requiring approval for irreversible actions contains the instruction.
- **C:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Limiting tools, validating output, and requiring approval for irreversible actions contains the instruction.
- **D:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Limiting tools, validating output, and requiring approval for irreversible actions contains the instruction.

### Question 12 — A, D

Answers: Apply a data loss prevention policy that blocks unapproved connectors in the environment; Separate development and production environments with environment security groups. A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data.
- **B:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data.
- **C:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data.
- **D:** Correct. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. In this case: A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data.
- **E:** Incorrect for this question. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Why the correct answer wins: A data loss prevention policy governs connectors in the environment, and separate environments with security groups protect production data.

### Question 13 — C

Answer: Extract the shared logic into a reusable component or child agent and reference it. One shared component gives a single place to change the dialogue. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **B:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: One shared component gives a single place to change the dialogue.
- **C:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: One shared component gives a single place to change the dialogue.
- **D:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: One shared component gives a single place to change the dialogue.

### Question 14 — B

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. Package and configure first, then export and promote through the pipeline. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: Package and configure first, then export and promote through the pipeline.
- **B:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: Package and configure first, then export and promote through the pipeline.
- **C:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: Package and configure first, then export and promote through the pipeline.
- **D:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: Package and configure first, then export and promote through the pipeline.

### Question 15 — B

Answer: Create an agent flow with a manual trigger that the topic calls with inputs. A manual-trigger agent flow runs on demand and returns the case number. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the case number.
- **B:** Correct. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. In this case: A manual-trigger agent flow runs on demand and returns the case number.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the case number.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns the case number.

### Question 16 — A

Answer: Wrap the calls in a scope with a parallel error branch that returns a structured failure. An error branch returning a failure code lets the topic respond honestly. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: An error branch returning a failure code lets the topic respond honestly.
- **B:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An error branch returning a failure code lets the topic respond honestly.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An error branch returning a failure code lets the topic respond honestly.
- **D:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: An error branch returning a failure code lets the topic respond honestly.

### Question 17 — D

Answer: Define typed input and output parameters on the flow and bind them from the topic. Typed output parameters and a topic that reads them. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **C:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: Typed output parameters and a topic that reads them.
- **D:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed output parameters and a topic that reads them.

### Question 18 — A, B

Answers: Wrap the calls in a scope with a parallel error branch that returns a structured failure; Define typed input and output parameters on the flow and bind them from the topic. Typed parameters define the contract, and structured errors stop silent failures. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: Typed parameters define the contract, and structured errors stop silent failures.
- **B:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed parameters define the contract, and structured errors stop silent failures.
- **C:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: Typed parameters define the contract, and structured errors stop silent failures.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed parameters define the contract, and structured errors stop silent failures.
- **E:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed parameters define the contract, and structured errors stop silent failures.

### Question 19 — B

Answer: Hand the conversation off to a live agent with the context attached. Hand the conversation to a person with its context, because the decision is discretionary. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.
- **B:** Correct. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. In this case: Hand the conversation to a person with its context, because the decision is discretionary.
- **C:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.
- **D:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: Hand the conversation to a person with its context, because the decision is discretionary.

### Question 20 — D

Answer: Have the agent draft the action and require a person to submit it in the source system. The agent drafts, and the irreversible send stays with the clinician. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: The agent drafts, and the irreversible send stays with the clinician.
- **B:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: The agent drafts, and the irreversible send stays with the clinician.
- **C:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: The agent drafts, and the irreversible send stays with the clinician.
- **D:** Correct. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. In this case: The agent drafts, and the irreversible send stays with the clinician.

### Question 21 — A

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs the transient fault before the topic reports anything. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs the transient fault before the topic reports anything.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **C:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.

### Question 22 — C

Answer: Send flow telemetry to Application Insights and query the traces. Traces in Application Insights retain the evidence beyond the history window. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Traces in Application Insights retain the evidence beyond the history window.
- **B:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Traces in Application Insights retain the evidence beyond the history window.
- **C:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Traces in Application Insights retain the evidence beyond the history window.
- **D:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Traces in Application Insights retain the evidence beyond the history window.

### Question 23 — B, D

Answers: Configure an alert on failed runs and route it to the owning team; Review the flow run history and its action-level inputs and outputs. Alerts detect the failure, and run history shows what the failing action received. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Why the correct answer wins: Alerts detect the failure, and run history shows what the failing action received.
- **B:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Alerts detect the failure, and run history shows what the failing action received.
- **C:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Alerts detect the failure, and run history shows what the failing action received.
- **D:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: Alerts detect the failure, and run history shows what the failing action received.
- **E:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Alerts detect the failure, and run history shows what the failing action received.

### Question 24 — D

Answer: Store the value in a global variable so later topics can read it. A global variable carries the identifier across the conversation. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A global variable carries the identifier across the conversation.
- **B:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A global variable carries the identifier across the conversation.
- **C:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: A global variable carries the identifier across the conversation.
- **D:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: A global variable carries the identifier across the conversation.

### Question 25 — B

Answer: Return an adaptive card so the data renders in labelled fields. An adaptive card renders the fields and the action in one response. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: An adaptive card renders the fields and the action in one response.
- **B:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: An adaptive card renders the fields and the action in one response.
- **C:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: An adaptive card renders the fields and the action in one response.
- **D:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: An adaptive card renders the fields and the action in one response.

### Question 26 — B, D

Answers: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns; Configure the message node to send a formatted message with the fields the user needs. Keep the code in topic scope so it cannot leak, and use a formatted message for the summary. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. A message node can send structured text without a card. It is the lightest way to make a list readable. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: Keep the code in topic scope so it cannot leak, and use a formatted message for the summary.
- **B:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: Keep the code in topic scope so it cannot leak, and use a formatted message for the summary.
- **C:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: Keep the code in topic scope so it cannot leak, and use a formatted message for the summary.
- **D:** Correct. A message node can send structured text without a card. It is the lightest way to make a list readable. In this case: Keep the code in topic scope so it cannot leak, and use a formatted message for the summary.
- **E:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: Keep the code in topic scope so it cannot leak, and use a formatted message for the summary.

### Question 27 — A

Answer: Configure a custom prompt that fixes the tone, structure, and citation behaviour. A custom prompt sets the reading level and vocabulary without changing the knowledge. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. In this case: A custom prompt sets the reading level and vocabulary without changing the knowledge.
- **B:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: A custom prompt sets the reading level and vocabulary without changing the knowledge.
- **C:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: A custom prompt sets the reading level and vocabulary without changing the knowledge.
- **D:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A custom prompt sets the reading level and vocabulary without changing the knowledge.

### Question 28 — C

Answer: Require the answer to cite retrieved passages and refuse when none are found. Requiring a citation and refusing when retrieval is empty keeps unsupported answers out. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty keeps unsupported answers out.
- **B:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty keeps unsupported answers out.
- **C:** Correct. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. In this case: Requiring a citation and refusing when retrieval is empty keeps unsupported answers out.
- **D:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Requiring a citation and refusing when retrieval is empty keeps unsupported answers out.

### Question 29 — B

Answer: Add the SharePoint site as a knowledge source and rely on item-level permissions. SharePoint knowledge respects each user's existing item access. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: SharePoint knowledge respects each user's existing item access.
- **B:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge respects each user's existing item access.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge respects each user's existing item access.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge respects each user's existing item access.

### Question 30 — B

Answer: Connect through a Power Platform connector and query it from a tool or flow. A Power Platform connector exposes operations the agent calls as tools. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Power Platform connector exposes operations the agent calls as tools.
- **B:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Power Platform connector exposes operations the agent calls as tools.
- **C:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Power Platform connector exposes operations the agent calls as tools.
- **D:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: A Power Platform connector exposes operations the agent calls as tools.

### Question 31 — B

Answer: Inventory the sources and their permissions → choose the connector or index for each → connect and scope the knowledge → test answers with users of different access → review unsupported questions. Inventory, choice, connection, access testing, then review of unsupported questions. Inventory precedes choice, choice precedes connection, and access testing follows connection. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. There is nothing to review before the knowledge is connected and tested. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.
- **B:** Correct. Inventory precedes choice, choice precedes connection, and access testing follows connection. In this case: Inventory, choice, connection, access testing, then review of unsupported questions.
- **C:** Incorrect for this question. Access testing requires connected sources. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.
- **D:** Incorrect for this question. The connector cannot be chosen before the inventory describes the sources. Why the correct answer wins: Inventory, choice, connection, access testing, then review of unsupported questions.

### Question 32 — A, E

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Index the content in Azure AI Search and use it as the knowledge source. The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. In this case: The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking.
- **B:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking.
- **C:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking.
- **E:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: The Copilot connector inherits source permissions, and an AI Search index adds explicit filtering and ranking.

### Question 33 — D

Answer: Apply a security filter on the query before the agent composes an answer. The security filter on the query keeps the other clinic's passage out of the result set. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter on the query keeps the other clinic's passage out of the result set.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter on the query keeps the other clinic's passage out of the result set.
- **C:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The security filter on the query keeps the other clinic's passage out of the result set.
- **D:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter on the query keeps the other clinic's passage out of the result set.

### Question 34 — C

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema decides which fields can be filtered and returned. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema decides which fields can be filtered and returned.
- **C:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema decides which fields can be filtered and returned.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema decides which fields can be filtered and returned.

### Question 35 — C

Answer: Use hybrid retrieval with vector and keyword queries. Hybrid retrieval adds keyword matching for exact identifiers. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.
- **B:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.
- **C:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Hybrid retrieval adds keyword matching for exact identifiers.
- **D:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: Hybrid retrieval adds keyword matching for exact identifiers.

### Question 36 — A, C

Answers: Enable semantic ranking and let the agent use the reranked results; Use hybrid retrieval with vector and keyword queries. Semantic ranking and hybrid retrieval both add work per query. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Semantic ranking and hybrid retrieval both add work per query.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Semantic ranking and hybrid retrieval both add work per query.
- **C:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: Semantic ranking and hybrid retrieval both add work per query.
- **D:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Semantic ranking and hybrid retrieval both add work per query.
- **E:** Incorrect for this question. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Why the correct answer wins: Semantic ranking and hybrid retrieval both add work per query.

### Question 37 — A

Answer: Configure a computer use tool against the legacy desktop application. Computer use drives the existing interface while no programmatic route exists. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. In this case: Computer use drives the existing interface while no programmatic route exists.
- **B:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Computer use drives the existing interface while no programmatic route exists.
- **C:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Computer use drives the existing interface while no programmatic route exists.
- **D:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Computer use drives the existing interface while no programmatic route exists.

### Question 38 — A

Answer: Monitor computer use runs and capture step screenshots for review. Step screenshots and validation of the expected screen expose the mismatch immediately. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Screenshots and step logs are how you diagnose a failed run and prove what the agent did. They also contain sensitive data and need retention rules. In this case: Step screenshots and validation of the expected screen expose the mismatch immediately.
- **B:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: Step screenshots and validation of the expected screen expose the mismatch immediately.
- **C:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: Step screenshots and validation of the expected screen expose the mismatch immediately.
- **D:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Step screenshots and validation of the expected screen expose the mismatch immediately.

### Question 39 — B

Answer: Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes. Confirm no API, prepare the host, record steps, run and inspect, then monitor for change. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Monitoring a tool that has never run and has no host is not possible. Why the correct answer wins: Confirm no API, prepare the host, record steps, run and inspect, then monitor for change.
- **B:** Correct. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. In this case: Confirm no API, prepare the host, record steps, run and inspect, then monitor for change.
- **C:** Incorrect for this question. Recording happens on the prepared machine, after the API check. Why the correct answer wins: Confirm no API, prepare the host, record steps, run and inspect, then monitor for change.
- **D:** Incorrect for this question. A run cannot precede the host and the recorded steps. Why the correct answer wins: Confirm no API, prepare the host, record steps, run and inspect, then monitor for change.

### Question 40 — D

Answer: Configure the MCP server connection with the authentication the server requires. The server connection needs valid authentication before any call succeeds. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: The server connection needs valid authentication before any call succeeds.
- **B:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: The server connection needs valid authentication before any call succeeds.
- **C:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: The server connection needs valid authentication before any call succeeds.
- **D:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: The server connection needs valid authentication before any call succeeds.

### Question 41 — B

Answer: Add an MCP server as a tool and let the agent discover the tools it exposes. An MCP server exposes the tool catalogue for discovery. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: An MCP server exposes the tool catalogue for discovery.
- **B:** Correct. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. In this case: An MCP server exposes the tool catalogue for discovery.
- **C:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: An MCP server exposes the tool catalogue for discovery.
- **D:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: An MCP server exposes the tool catalogue for discovery.

### Question 42 — B

Answer: Expose only the MCP tools the task needs and review their descriptions. Expose only the needed tools so a bad instruction cannot reach the rest. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: Expose only the needed tools so a bad instruction cannot reach the rest.
- **B:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: Expose only the needed tools so a bad instruction cannot reach the rest.
- **C:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Expose only the needed tools so a bad instruction cannot reach the rest.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Expose only the needed tools so a bad instruction cannot reach the rest.

### Question 43 — A

Answer: Use a streamable HTTP MCP server so the agent can reach it over the network. Streamable HTTP reaches a remote server over the network. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: Streamable HTTP reaches a remote server over the network.
- **B:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **C:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **D:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.

### Question 44 — A

Answer: Configure connector authentication so each call uses the caller’s identity. Per-user authentication makes the API evaluate each caller's rights. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication makes the API evaluate each caller's rights.
- **B:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **C:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **D:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.

### Question 45 — C

Answer: Call the API from an agent flow and return the parsed response to the topic. An agent flow can retry and transform before returning clean values. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: An agent flow can retry and transform before returning clean values.
- **B:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: An agent flow can retry and transform before returning clean values.
- **C:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: An agent flow can retry and transform before returning clean values.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: An agent flow can retry and transform before returning clean values.

### Question 46 — D, E

Answers: Configure connector authentication so each call uses the caller’s identity; Define the response schema so the agent can reason over the returned fields. Per-user authentication preserves rights, and a declared schema lets the agent use fields. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: Per-user authentication preserves rights, and a declared schema lets the agent use fields.
- **B:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication preserves rights, and a declared schema lets the agent use fields.
- **C:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication preserves rights, and a declared schema lets the agent use fields.
- **D:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication preserves rights, and a declared schema lets the agent use fields.
- **E:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: Per-user authentication preserves rights, and a declared schema lets the agent use fields.

### Question 47 — D

Answer: Split the work into a parent agent that delegates to specialist child agents. Delegate to specialist children so each department keeps its own owner and release. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Delegate to specialist children so each department keeps its own owner and release.
- **B:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Delegate to specialist children so each department keeps its own owner and release.
- **C:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Delegate to specialist children so each department keeps its own owner and release.
- **D:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Delegate to specialist children so each department keeps its own owner and release.

### Question 48 — B

Answer: Write the parent’s instructions to describe when each child should be used. The parent's routing instructions must describe clearly when that child applies. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: The parent's routing instructions must describe clearly when that child applies.
- **B:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: The parent's routing instructions must describe clearly when that child applies.
- **C:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: The parent's routing instructions must describe clearly when that child applies.
- **D:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: The parent's routing instructions must describe clearly when that child applies.

### Question 49 — D

Answer: Give each child a clear input and output contract and keep shared state in the parent. An input and output contract fixes the identifier format. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: An input and output contract fixes the identifier format.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: An input and output contract fixes the identifier format.
- **C:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: An input and output contract fixes the identifier format.
- **D:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: An input and output contract fixes the identifier format.

### Question 50 — B

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Instructions and children first, then routing tests, then tuning from the evidence. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Instructions and children first, then routing tests, then tuning from the evidence.
- **B:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Instructions and children first, then routing tests, then tuning from the evidence.
- **C:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Instructions and children first, then routing tests, then tuning from the evidence.
- **D:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Instructions and children first, then routing tests, then tuning from the evidence.

### Question 51 — D, E

Answers: Route by intent in the parent and pass only the context the child needs; Give every child the same knowledge source so answers stay consistent. Pass only needed context, and ground every child in the same knowledge. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Pass only needed context, and ground every child in the same knowledge.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Pass only needed context, and ground every child in the same knowledge.
- **C:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Pass only needed context, and ground every child in the same knowledge.
- **D:** Correct. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. In this case: Pass only needed context, and ground every child in the same knowledge.
- **E:** Correct. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. In this case: Pass only needed context, and ground every child in the same knowledge.

### Question 52 — B

Answer: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent. Connect it as a connected agent so the evaluated behaviour answers. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.
- **B:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: Connect it as a connected agent so the evaluated behaviour answers.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.
- **D:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers.

### Question 53 — A

Answer: Evaluate the Foundry agent against the same test set before it is connected. Evaluate the Foundry agent on the shared test set before connecting it. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: Evaluate the Foundry agent on the shared test set before connecting it.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Evaluate the Foundry agent on the shared test set before connecting it.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Evaluate the Foundry agent on the shared test set before connecting it.
- **D:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Evaluate the Foundry agent on the shared test set before connecting it.

### Question 54 — A, C

Answers: Deploy the model in Foundry and point the custom prompt at that deployment; Ground the Foundry agent in the same indexed knowledge so both layers answer consistently. Reference the deployment from the prompt, and ground both layers in the same corpus. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. In this case: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **C:** Correct. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. In this case: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **D:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.
- **E:** Incorrect for this question. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Why the correct answer wins: Reference the deployment from the prompt, and ground both layers in the same corpus.

### Question 55 — C

Answer: Add the existing agent as a connected agent and let the parent delegate to it. Add them as connected agents so their owners keep control. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Add them as connected agents so their owners keep control.
- **B:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Add them as connected agents so their owners keep control.
- **C:** Correct. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. In this case: Add them as connected agents so their owners keep control.
- **D:** Incorrect for this question. A copy forks the behaviour and doubles the maintenance from the first day. Why the correct answer wins: Add them as connected agents so their owners keep control.

### Question 56 — A

Answer: Write a precise name and description for the connected agent so routing works. Precise names and descriptions drive correct routing. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. In this case: Precise names and descriptions drive correct routing.
- **B:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Precise names and descriptions drive correct routing.
- **C:** Incorrect for this question. An unpinned dependency can change behaviour between your test run and your release. Why the correct answer wins: Precise names and descriptions drive correct routing.
- **D:** Incorrect for this question. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Why the correct answer wins: Precise names and descriptions drive correct routing.

### Question 57 — A

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the semantic model where the measures live. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the semantic model where the measures live.
- **B:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures live.
- **C:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures live.
- **D:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures live.

### Question 58 — D

Answer: Grant the data agent’s identity read access to the semantic model only. Scope its read access to that model. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: Scope its read access to that model.
- **B:** Incorrect for this question. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Why the correct answer wins: Scope its read access to that model.
- **C:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: Scope its read access to that model.
- **D:** Correct. Least privilege for the data agent limits what a bad question can reach. Broader workspace access is a common over-grant. In this case: Scope its read access to that model.

### Question 59 — A

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. The agent card lists skills and the endpoint. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: The agent card lists skills and the endpoint.
- **B:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: The agent card lists skills and the endpoint.
- **C:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: The agent card lists skills and the endpoint.
- **D:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: The agent card lists skills and the endpoint.

### Question 60 — C

Answer: Track the remote task state and surface long-running results back into the conversation. Task state tracking so long-running results return to the conversation. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: Task state tracking so long-running results return to the conversation.
- **B:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: Task state tracking so long-running results return to the conversation.
- **C:** Correct. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. In this case: Task state tracking so long-running results return to the conversation.
- **D:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: Task state tracking so long-running results return to the conversation.

### Question 61 — D

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary restricts which skills are exposed. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **B:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **C:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: A trust boundary restricts which skills are exposed.
- **D:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary restricts which skills are exposed.

### Question 62 — A

Answer: Provision enough quota and throughput for peak conversation volume. Provisioned throughput must cover peak concurrency. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. In this case: Provisioned throughput must cover peak concurrency.
- **B:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: Provisioned throughput must cover peak concurrency.
- **C:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Provisioned throughput must cover peak concurrency.
- **D:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Provisioned throughput must cover peak concurrency.

### Question 63 — B

Answer: Choose a model from the catalog that meets quality, latency, and residency needs. Model choice balances quality, latency, and cost. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: Model choice balances quality, latency, and cost.
- **B:** Correct. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. In this case: Model choice balances quality, latency, and cost.
- **C:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Model choice balances quality, latency, and cost.
- **D:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Model choice balances quality, latency, and cost.

### Question 64 — A

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Conversation and tool telemetry makes the report investigable. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Conversation and tool telemetry makes the report investigable.
- **B:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **C:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **D:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.

### Question 65 — A

Answer: Query conversation and tool spans in Application Insights with KQL. A KQL query over correlated spans reconstructs the conversation. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: A KQL query over correlated spans reconstructs the conversation.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.
- **D:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: A KQL query over correlated spans reconstructs the conversation.

### Question 66 — D

Answer: Sample telemetry so volume stays affordable while errors are always kept. Sample the volume and always keep errors. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Why the correct answer wins: Sample the volume and always keep errors.
- **B:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sample the volume and always keep errors.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sample the volume and always keep errors.
- **D:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sample the volume and always keep errors.

### Question 67 — D, E

Answers: Alert on failed tool calls and answer-quality regressions; Correlate a failed answer with the tool call and knowledge retrieval behind it. An alert detects the failure, and correlated traces identify the dependency. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: An alert detects the failure, and correlated traces identify the dependency.
- **D:** Correct. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. In this case: An alert detects the failure, and correlated traces identify the dependency.
- **E:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: An alert detects the failure, and correlated traces identify the dependency.

### Question 68 — C

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real anonymized conversations carry the phrasing the agent will meet. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Real anonymized conversations carry the phrasing the agent will meet.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real anonymized conversations carry the phrasing the agent will meet.
- **C:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real anonymized conversations carry the phrasing the agent will meet.
- **D:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real anonymized conversations carry the phrasing the agent will meet.

### Question 69 — C

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and out-of-scope cases belong in the set. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set.
- **B:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set.
- **C:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and out-of-scope cases belong in the set.
- **D:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and out-of-scope cases belong in the set.

### Question 70 — D

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Questions, classification, scoring, failure log, then reruns. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.
- **B:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.
- **C:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.
- **D:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Questions, classification, scoring, failure log, then reruns.

### Question 71 — C, E

Answers: Hold part of the set out of prompt tuning so results stay honest; Version the test set and rerun it for every change. A holdout prevents overfitting, and versioning keeps comparisons valid. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A holdout prevents overfitting, and versioning keeps comparisons valid.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A holdout prevents overfitting, and versioning keeps comparisons valid.
- **C:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: A holdout prevents overfitting, and versioning keeps comparisons valid.
- **D:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: A holdout prevents overfitting, and versioning keeps comparisons valid.
- **E:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: A holdout prevents overfitting, and versioning keeps comparisons valid.

### Question 72 — D

Answer: Have subject-matter experts score a sample against the rubric. Expert scoring against a rubric is the reference standard a board can accept. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Expert scoring against a rubric is the reference standard a board can accept.
- **B:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Expert scoring against a rubric is the reference standard a board can accept.
- **C:** Incorrect for this question. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Why the correct answer wins: Expert scoring against a rubric is the reference standard a board can accept.
- **D:** Correct. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. In this case: Expert scoring against a rubric is the reference standard a board can accept.

### Question 73 — C

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. Rubric, human sample, comparison, adjustment, full runs. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.
- **B:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.
- **C:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: Rubric, human sample, comparison, adjustment, full runs.
- **D:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: Rubric, human sample, comparison, adjustment, full runs.

### Question 74 — A

Answer: Group failures by topic and root cause instead of fixing items one at a time. Group by root cause and fix the causes. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. In this case: Group by root cause and fix the causes.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Group by root cause and fix the causes.
- **C:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Group by root cause and fix the causes.
- **D:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Group by root cause and fix the causes.

### Question 75 — C

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assign each cluster to the owner of the topic, prompt, or connector. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **B:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **C:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assign each cluster to the owner of the topic, prompt, or connector.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.

### Question 76 — B

Answer: Create a solution and add the agent and its dependencies to it. A solution containing the agent and its dependencies. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: A solution containing the agent and its dependencies.
- **B:** Correct. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. In this case: A solution containing the agent and its dependencies.
- **C:** Incorrect for this question. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Why the correct answer wins: A solution containing the agent and its dependencies.
- **D:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: A solution containing the agent and its dependencies.

### Question 77 — A

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution is packaged and configured before export, and the pipeline performs the deployment. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **B:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **C:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.
- **D:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution is packaged and configured before export, and the pipeline performs the deployment.

### Question 78 — A

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable holds the endpoint per environment. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable holds the endpoint per environment.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **C:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: An environment variable holds the endpoint per environment.
- **D:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: An environment variable holds the endpoint per environment.

### Question 79 — D

Answer: Store the secret in a vault and reference it from the environment variable. A vault-backed environment variable keeps it out of the artefact. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.
- **C:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A vault-backed environment variable keeps it out of the artefact.
- **D:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: A vault-backed environment variable keeps it out of the artefact.

### Question 80 — C, D

Answers: Use the current value in production and a default value for development; Set the environment variable values as part of the pipeline deployment step. A current value with a default, plus deployment-time values per stage. Current and default values cover the common two-environment split and are set explicitly per stage. Setting values during deployment removes the manual edit that people forget before a release. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A current value with a default, plus deployment-time values per stage.
- **B:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: A current value with a default, plus deployment-time values per stage.
- **C:** Correct. Current and default values cover the common two-environment split and are set explicitly per stage. In this case: A current value with a default, plus deployment-time values per stage.
- **D:** Correct. Setting values during deployment removes the manual edit that people forget before a release. In this case: A current value with a default, plus deployment-time values per stage.
- **E:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A current value with a default, plus deployment-time values per stage.

### Question 81 — C

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment test step that blocks on failure. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment test step that blocks on failure.
- **B:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment test step that blocks on failure.
- **C:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment test step that blocks on failure.
- **D:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment test step that blocks on failure.

### Question 82 — C

Answer: Require approval before the production stage runs. An approval gate captures that decision. An approval records who accepted the risk of the release. It must be a person who can read the test results. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: An approval gate captures that decision.
- **B:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: An approval gate captures that decision.
- **C:** Correct. An approval records who accepted the risk of the release. It must be a person who can read the test results. In this case: An approval gate captures that decision.
- **D:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: An approval gate captures that decision.

### Question 83 — C

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. Solution, configuration, stages, test step, approved deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.
- **B:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.
- **C:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: Solution, configuration, stages, test step, approved deployment.
- **D:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: Solution, configuration, stages, test step, approved deployment.

### Question 84 — A, C

Answers: Pass environment-specific values through pipeline configuration rather than editing the solution; Keep the previous managed solution version so you can roll back. Per-stage configuration and the previous version available for rollback. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: Per-stage configuration and the previous version available for rollback.
- **B:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Per-stage configuration and the previous version available for rollback.
- **C:** Correct. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. In this case: Per-stage configuration and the previous version available for rollback.
- **D:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Per-stage configuration and the previous version available for rollback.
- **E:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Per-stage configuration and the previous version available for rollback.

### Question 85 — A

Answer: Deploy only the components that changed when the pipeline supports it. Deploying only the changed components shortens the change window and limits the blast radius of a bad release. Scoped deployment shortens the window and reduces the blast radius of a bad release. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Scoped deployment shortens the window and reduces the blast radius of a bad release. In this case: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **B:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.
- **D:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: Deploying only the changed components shortens the change window and limits the blast radius of a bad release.

### Question 86 — C

Answer: Notify the owning team with the deployment result and the failed step. A notification naming the failed stage. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Why the correct answer wins: A notification naming the failed stage.
- **B:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: A notification naming the failed stage.
- **C:** Correct. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. In this case: A notification naming the failed stage.
- **D:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: A notification naming the failed stage.

### Question 87 — B

Answer: Watch for knowledge-source changes and re-run the evaluation after they land. Re-run the evaluation after a knowledge change. Most answer regressions arrive with a document, not with a model change. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Re-run the evaluation after a knowledge change.
- **B:** Correct. Most answer regressions arrive with a document, not with a model change. In this case: Re-run the evaluation after a knowledge change.
- **C:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Re-run the evaluation after a knowledge change.
- **D:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Re-run the evaluation after a knowledge change.

### Question 88 — C

Answer: Sample production conversations and score them against the rubric on a schedule. Scheduled sampling scored against the rubric shows whether answer quality held over the quarter. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Scheduled sampling scored against the rubric shows whether answer quality held over the quarter.
- **B:** Incorrect for this question. Fallback and handoff rates move before anyone files a ticket. A trend alert buys time. Why the correct answer wins: Scheduled sampling scored against the rubric shows whether answer quality held over the quarter.
- **C:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Scheduled sampling scored against the rubric shows whether answer quality held over the quarter.
- **D:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Scheduled sampling scored against the rubric shows whether answer quality held over the quarter.

### Question 89 — B

Answer: Wrap the calls in a scope with a parallel error branch that returns a structured failure. A retry followed by a terminate with a failure code gives the conversation something true to say. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: A retry followed by a terminate with a failure code gives the conversation something true to say.
- **B:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: A retry followed by a terminate with a failure code gives the conversation something true to say.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A retry followed by a terminate with a failure code gives the conversation something true to say.
- **D:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: A retry followed by a terminate with a failure code gives the conversation something true to say.

### Question 90 — D

Answer: Include adversarial and edge cases such as out-of-scope and injection attempts. Adversarial and high-volume edge cases, because that is where the agent fails visibly. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where the agent fails visibly.
- **B:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where the agent fails visibly.
- **C:** Incorrect for this question. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Why the correct answer wins: Adversarial and high-volume edge cases, because that is where the agent fails visibly.
- **D:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: Adversarial and high-volume edge cases, because that is where the agent fails visibly.

### Question 91 — D

Answer: Track containment, resolution, and escalation metrics on a dashboard. Containment, resolution, and escalation trends are the operational evidence for that claim. Operational metrics show whether the agent is helping. They are the business case for the next release. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence for that claim.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence for that claim.
- **C:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: Containment, resolution, and escalation trends are the operational evidence for that claim.
- **D:** Correct. Operational metrics show whether the agent is helping. They are the business case for the next release. In this case: Containment, resolution, and escalation trends are the operational evidence for that claim.

### Question 92 — D

Answer: Have the agent draft the action and require a person to submit it in the source system. The agent drafts and the irreversible send stays with the clinician in the system that owns it. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: The agent drafts and the irreversible send stays with the clinician in the system that owns it.
- **B:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: The agent drafts and the irreversible send stays with the clinician in the system that owns it.
- **C:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: The agent drafts and the irreversible send stays with the clinician in the system that owns it.
- **D:** Correct. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. In this case: The agent drafts and the irreversible send stays with the clinician in the system that owns it.

### Question 93 — B, E

Answers: Configure connector authentication so each call uses the caller’s identity; Define the response schema so the agent can reason over the returned fields. Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields.
- **B:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields.
- **C:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields.
- **E:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: Per-user authentication keeps the API honest, and a declared schema lets the agent read named fields.

### Question 94 — C

Answer: Have subject-matter experts score a sample against the rubric. Expert scoring against a rubric is the reference a clinical audience will accept. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Expert scoring against a rubric is the reference a clinical audience will accept.
- **B:** Incorrect for this question. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Why the correct answer wins: Expert scoring against a rubric is the reference a clinical audience will accept.
- **C:** Correct. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. In this case: Expert scoring against a rubric is the reference a clinical audience will accept.
- **D:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Expert scoring against a rubric is the reference a clinical audience will accept.

### Question 95 — B, E

Answers: Package the shared topics, flows, and connection references in a solution; Parameterize environment-specific values with environment variables. A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints.
- **B:** Correct. A solution carries the reusable parts between environments as one unit. It is the supported ALM path for shared components. In this case: A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints.
- **C:** Incorrect for this question. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Why the correct answer wins: A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints.
- **D:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints.
- **E:** Correct. Environment variables keep the reusable component identical across environments while endpoints differ. Secrets should still live in a vault. In this case: A solution carries the shared logic as one versioned unit, and environment variables hold the endpoints.

### Question 96 — B

Answer: Split the work into a parent agent that delegates to specialist child agents. Its own specialist child agent, with its own owner and release cycle. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Its own specialist child agent, with its own owner and release cycle.
- **B:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Its own specialist child agent, with its own owner and release cycle.
- **C:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Its own specialist child agent, with its own owner and release cycle.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Its own specialist child agent, with its own owner and release cycle.

### Question 97 — C

Answer: Group failures by topic and root cause instead of fixing items one at a time. Group the failures by topic and root cause so the recurring causes are fixed once. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Group the failures by topic and root cause so the recurring causes are fixed once.
- **B:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Group the failures by topic and root cause so the recurring causes are fixed once.
- **C:** Correct. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. In this case: Group the failures by topic and root cause so the recurring causes are fixed once.
- **D:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Group the failures by topic and root cause so the recurring causes are fixed once.

### Question 98 — C

Answer: Authenticate partners through external identities rather than internal tenant accounts. External identities give contractors credentials without internal accounts. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: External identities give contractors credentials without internal accounts.
- **B:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: External identities give contractors credentials without internal accounts.
- **C:** Correct. External identities give suppliers or citizens their own credentials without creating internal accounts. Federation and guest invitations are the usual mechanisms. In this case: External identities give contractors credentials without internal accounts.
- **D:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: External identities give contractors credentials without internal accounts.

### Question 99 — A

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer keeps incident content out of their answers. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer keeps incident content out of their answers.
- **B:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer keeps incident content out of their answers.
- **C:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer keeps incident content out of their answers.
- **D:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Permission trimming in the knowledge layer keeps incident content out of their answers.

### Question 100 — D

Answer: Apply a security filter on the query before the agent composes an answer. The security filter on the query keeps restricted content out of the result set. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The security filter on the query keeps restricted content out of the result set.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter on the query keeps restricted content out of the result set.
- **C:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter on the query keeps restricted content out of the result set.
- **D:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter on the query keeps restricted content out of the result set.
