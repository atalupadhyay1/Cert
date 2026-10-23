# Microsoft AB-620 — Full-Length Mock Exam 4

AI Agent Builder Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A bank's agent must read account status from a mainframe gateway that permits outbound calls only. What should the plan specify?

Domain: Plan and configure agent solutions

- A. Batch the requests and post them to the source system on a schedule
- B. Mediate the on-premises call through an on-premises data gateway
- C. Mirror the source into Microsoft Fabric and query it with a Fabric data agent
- D. Call the internal endpoint straight from the topic over HTTP

### 2. A department has no live interface and proposes a nightly extract for the agent. Which integration option fits?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Batch the requests and post them to the source system on a schedule
- C. Expose the system through a virtual table or connector view that the agent can read
- D. Copy the records nightly into Dataverse and answer from the copy

### 3. The agent reads an Azure AI Search index and writes nothing else. Which identity fits the call?

Domain: Plan and configure agent solutions

- A. Use the agent managed identity for Azure resources and keep user identity for business data
- B. Give every conversation a single shared service account credential for the API
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Store one API key in a topic variable and reuse it for every user

### 4. A support agent answers account questions and then updates the ticket system as the signed-in user. Which two identity elements are needed? Select two.

Domain: Plan and configure agent solutions

- A. Require Microsoft Entra ID sign-in for the agent and pass the user token downstream
- B. Use the on-behalf-of flow so the agent calls the API as the signed-in user
- C. Allow anonymous access to the agent and authenticate only at the API
- D. Give every conversation a single shared service account credential for the API
- E. Store one API key in a topic variable and reuse it for every user

### 5. A media company wants the agent inside its subscriber app with the app's own sign-in flow. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to email and answer asynchronously
- B. Embed the agent in a custom application through the Direct Line channel
- C. Publish to Microsoft Teams and keep the agent inside the tenant
- D. Publish to a public website with authenticated sign-in

### 6. A public-sector team wants the agent available beside other agents in the Copilot experience. Which option fits?

Domain: Plan and configure agent solutions

- A. Publish to Microsoft Teams and keep the agent inside the tenant
- B. Add the channel for omni-channel engagement so external support queues can route to it
- C. Publish to a public website with authenticated sign-in
- D. Publish the agent into Microsoft 365 Copilot so it appears alongside other agents

### 7. A utility wants unresolved chats to move into its human support queue with full context. Which channel fits?

Domain: Plan and configure agent solutions

- A. Publish to email and answer asynchronously
- B. Publish to a public website with authenticated sign-in
- C. Add the channel for omni-channel engagement so external support queues can route to it
- D. Embed the agent in a custom application through the Direct Line channel

### 8. An agent serves two customer segments, and each must only see its own contractual terms. What must be enforced?

Domain: Plan and configure agent solutions

- A. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- B. Enforce the source system’s permissions in the knowledge layer so answers respect access
- C. Separate development and production environments with environment security groups
- D. Turn on audit logging and retain agent conversation records

### 9. A retrieved support article contains a sentence instructing the assistant to reveal its configuration. Which control applies?

Domain: Plan and configure agent solutions

- A. Restrict who can author and publish with Copilot Studio security roles
- B. Turn on audit logging and retain agent conversation records
- C. Constrain the tools the agent may call, validate tool output, and limit autonomous actions
- D. Separate development and production environments with environment security groups

### 10. A maker attached a personal cloud storage connector to an agent that reads customer records. Which control blocks this?

Domain: Plan and configure agent solutions

- A. Separate development and production environments with environment security groups
- B. Turn on audit logging and retain agent conversation records
- C. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- D. Restrict who can author and publish with Copilot Studio security roles

### 11. Four agents must call the same ticketing API with the same authentication and schema. What should be built once?

Domain: Plan and configure agent solutions

- A. Copy the topics into each agent so every team can edit its own copy
- B. Expose the shared integration as a custom connector any agent can add as a tool
- C. Rebuild the same topic in each agent to avoid a shared dependency
- D. Extract the shared logic into a reusable component or child agent and reference it

### 12. A team is releasing a shared agent capability through three environments. Which sequence is correct?

Domain: Plan and configure agent solutions

- A. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- B. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- C. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies
- D. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables

### 13. A topic must collect four values, call two services, and return a reference number in the same turn. What should be built?

Domain: Plan and configure agent solutions

- A. Create the flow with the connector action the agent needs and return the result
- B. Add the capability as a connector action so the agent can call it without a flow
- C. Create an agent flow with a manual trigger that the topic calls with inputs
- D. Use an automated cloud flow triggered by an event and have the agent wait for it

### 14. The agent needs one connector operation with no branching or transformation. What is the lightest option?

Domain: Plan and configure agent solutions

- A. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Create the flow with the connector action the agent needs and return the result
- D. Add the capability as a connector action so the agent can call it without a flow

### 15. A ticket closure must trigger a survey, and the agent only reports it later. Which trigger fits?

Domain: Plan and configure agent solutions

- A. Use an automated cloud flow triggered by an event and have the agent wait for it
- B. Wrap the calls in a scope with a parallel error branch that returns a structured failure
- C. Add the capability as a connector action so the agent can call it without a flow
- D. Create an agent flow with a manual trigger that the topic calls with inputs

### 16. A flow is called from a topic that must always respond. Which two features are required? Select two.

Domain: Plan and configure agent solutions

- A. Add the capability as a connector action so the agent can call it without a flow
- B. Define typed input and output parameters on the flow and bind them from the topic
- C. Use an automated cloud flow triggered by an event and have the agent wait for it
- D. Create an agent flow with a manual trigger that the topic calls with inputs
- E. Wrap the calls in a scope with a parallel error branch that returns a structured failure

### 17. A customer asks for a goodwill credit that policy allows only a team lead to grant. What should the agent do?

Domain: Plan and configure agent solutions

- A. Set a response timeout and route to a fallback owner when nobody answers
- B. Let the agent complete the action and notify a person afterwards
- C. Hand the conversation off to a live agent with the context attached
- D. Have the agent draft the action and require a person to submit it in the source system

### 18. Outbound regulatory letters must come from a named officer's mailbox, never the agent's own. Which pattern fits?

Domain: Plan and configure agent solutions

- A. Post an adaptive card to Teams and wait for the human decision before continuing
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Send an approval request and pause the flow until a person responds
- D. Let the agent complete the action and notify a person afterwards

### 19. A downstream service returns a timeout twice an hour and the agent reports failure each time. What should change?

Domain: Plan and configure agent solutions

- A. Use the Copilot Studio analytics view for session and topic outcomes
- B. Configure a retry policy and terminate with a failure code the topic can read
- C. Add a comment step to the flow describing the expected failure
- D. Configure an alert on failed runs and route it to the owning team

### 20. A flow fails intermittently, and the failing runs have already expired from the history view. What should be enabled?

Domain: Plan and configure agent solutions

- A. Review the flow run history and its action-level inputs and outputs
- B. Use the Copilot Studio analytics view for session and topic outcomes
- C. Send flow telemetry to Application Insights and query the traces
- D. Add a comment step to the flow describing the expected failure

### 21. A builder is debugging a single failed run and also owns the alert queue. Which two capabilities fit those tasks? Select two.

Domain: Plan and configure agent solutions

- A. Use the Copilot Studio analytics view for session and topic outcomes
- B. Send flow telemetry to Application Insights and query the traces
- C. Review the flow run history and its action-level inputs and outputs
- D. Add a comment step to the flow describing the expected failure
- E. Configure an alert on failed runs and route it to the owning team

### 22. A one-time verification code keeps reappearing in later turns of the same conversation. What should be fixed?

Domain: Plan and configure agent solutions

- A. Store the value in a global variable so later topics can read it
- B. Configure the topic as a redirect target with its own trigger phrases
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns

### 23. A resolution summary needs three labelled values and a link action. What should the topic return?

Domain: Plan and configure agent solutions

- A. Configure the message node to send a formatted message with the fields the user needs
- B. Return an adaptive card so the data renders in labelled fields
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Return the raw flow output as plain text

### 24. A long support conversation needs shared context and readable lists. Which two choices apply? Select two.

Domain: Plan and configure agent solutions

- A. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- B. Store the value in a global variable so later topics can read it
- C. Configure the message node to send a formatted message with the fields the user needs
- D. Configure the topic as a redirect target with its own trigger phrases
- E. Return the raw flow output as plain text

### 25. Answers are correct but too long for a mobile chat window. What should be configured?

Domain: Plan and configure agent solutions

- A. Point the generative answers node at the specific knowledge source for the question
- B. Add a fallback topic for low-confidence answers that hands off to a person
- C. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- D. Require the answer to cite retrieved passages and refuse when none are found

### 26. The agent invents answers to questions outside its support scope. What should be added?

Domain: Plan and configure agent solutions

- A. Return an image with the card so the response looks richer
- B. Point the generative answers node at the specific knowledge source for the question
- C. Add a fallback topic for low-confidence answers that hands off to a person
- D. Configure a custom prompt that fixes the tone, structure, and citation behaviour

### 27. A service desk must create and update tickets through connector operations rather than search. Which route fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Connect through a Power Platform connector and query it from a tool or flow
- C. Connect the source through a Copilot connector so its content is indexed for answers
- D. Upload the documents as file knowledge on the agent

### 28. A records team must choose knowledge routes for two libraries with different permission models. Which two statements are correct? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Index the content in Azure AI Search and use it as the knowledge source
- B. Upload the documents as file knowledge on the agent
- C. Add the SharePoint site as a knowledge source and rely on item-level permissions
- D. Register the database as a knowledge source so the agent can query it directly
- E. Connect through a Power Platform connector and query it from a tool or flow

### 29. An index must return a citation field and filter by product version. What should be designed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Connect to the search service over a private endpoint with managed identity
- C. Enable semantic ranking and let the agent use the reranked results
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 30. Search by case number returns nothing although the case exists in the index. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Recreate the index on every publish so it never goes stale
- B. Use hybrid retrieval with vector and keyword queries
- C. Connect to the search service over a private endpoint with managed identity
- D. Enable semantic ranking and let the agent use the reranked results

### 31. A public-sector security standard requires private connectivity to the search service. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Use hybrid retrieval with vector and keyword queries
- B. Connect to the search service over a private endpoint with managed identity
- C. Create the index with the fields, vector profile, and semantic configuration the agent needs
- D. Recreate the index on every publish so it never goes stale

### 32. An index serves staff and contractors with different entitlements. Which two settings matter most? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Create the index with the fields, vector profile, and semantic configuration the agent needs
- B. Recreate the index on every publish so it never goes stale
- C. Enable semantic ranking and let the agent use the reranked results
- D. Apply a security filter on the query before the agent composes an answer
- E. Connect to the search service over a private endpoint with managed identity

### 33. A vendor now offers an API for the application the agent drives through the screen. What should the team do?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure a computer use tool against the legacy desktop application
- B. Run the tool unattended on a dedicated machine with a vaulted credential
- C. Provision a machine or machine group and run the tool there with a dedicated account
- D. Replace the screen automation with an API once the application exposes one

### 34. A nightly computer use job must run with a credential no employee holds. Which configuration applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision a machine or machine group and run the tool there with a dedicated account
- B. Record the click path once and reuse it without validating each run
- C. Run the tool unattended on a dedicated machine with a vaulted credential
- D. Replace the screen automation with an API once the application exposes one

### 35. A team is onboarding computer use for a legacy desktop application. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → monitor for interface changes → record the steps on a test record
- B. Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes
- C. Record the steps on a test record → provision a machine with the application installed → confirm no API exists for the task → run the tool and inspect the step log → monitor for interface changes
- D. Monitor for interface changes → run the tool and inspect the step log → confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record

### 36. A security team publishes approved tools through one catalogue that other teams extend. Which integration fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure the MCP server connection with the authentication the server requires
- B. Wrap the internal API as MCP tools and register the server endpoint with the agent
- C. Add an MCP server as a tool and let the agent discover the tools it exposes
- D. Embed the MCP server as a local process inside the agent

### 37. A partner MCP server exposes 30 tools and the agent uses two. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure the MCP server connection with the authentication the server requires
- B. Use a streamable HTTP MCP server so the agent can reach it over the network
- C. Expose only the MCP tools the task needs and review their descriptions
- D. Add an MCP server as a tool and let the agent discover the tools it exposes

### 38. The MCP server is remote and the agent is hosted by the platform. Which transport applies?

Domain: Integrate and extend agents in Copilot Studio

- A. Wrap the internal API as MCP tools and register the server endpoint with the agent
- B. Use a streamable HTTP MCP server so the agent can reach it over the network
- C. Embed the MCP server as a local process inside the agent
- D. Configure the MCP server connection with the authentication the server requires

### 39. An MCP server lists its tools in the agent, but every call returns unauthorized. What should be fixed?

Domain: Integrate and extend agents in Copilot Studio

- A. Expose only the MCP tools the task needs and review their descriptions
- B. Use a streamable HTTP MCP server so the agent can reach it over the network
- C. Configure the MCP server connection with the authentication the server requires
- D. Add an MCP server as a tool and let the agent discover the tools it exposes

### 40. An agent quotes raw JSON because the response fields are not declared. What should be added?

Domain: Integrate and extend agents in Copilot Studio

- A. Call the REST API from a topic with a Send HTTP request action
- B. Call the API from an agent flow and return the parsed response to the topic
- C. Define the response schema so the agent can reason over the returned fields
- D. Hard-code the endpoint URL and key inside the topic

### 41. A connector uses one shared key for every caller, and access reviews fail. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure connector authentication so each call uses the caller’s identity
- B. Call the API from an agent flow and return the parsed response to the topic
- C. Hard-code the endpoint URL and key inside the topic
- D. Create a custom connector from the OpenAPI definition and add it as a tool

### 42. A REST service must become a reliable reusable tool for three agents. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Call the REST API from a topic with a Send HTTP request action
- B. Hard-code the endpoint URL and key inside the topic
- C. Define the response schema so the agent can reason over the returned fields
- D. Call the API from an agent flow and return the parsed response to the topic
- E. Create a custom connector from the OpenAPI definition and add it as a tool

### 43. Two teams need a different release cadence for their parts of one large agent. What should the architect do?

Domain: Integrate and extend agents in Copilot Studio

- A. Split the work into a parent agent that delegates to specialist child agents
- B. Build one large agent with every topic so there is a single place to change
- C. Give each child a clear input and output contract and keep shared state in the parent
- D. Route by intent in the parent and pass only the context the child needs

### 44. A parent answers insurance questions itself rather than delegating to the claims child. What should be fixed?

Domain: Integrate and extend agents in Copilot Studio

- A. Write the parent’s instructions to describe when each child should be used
- B. Give each child a clear input and output contract and keep shared state in the parent
- C. Give every child the same knowledge source so answers stay consistent
- D. Route by intent in the parent and pass only the context the child needs

### 45. The parent cannot tell whether a child succeeded because the response carries no status field. What should be agreed?

Domain: Integrate and extend agents in Copilot Studio

- A. Give each child a clear input and output contract and keep shared state in the parent
- B. Build one large agent with every topic so there is a single place to change
- C. Route by intent in the parent and pass only the context the child needs
- D. Give every child the same knowledge source so answers stay consistent

### 46. An architect is building a parent with three specialist children. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions
- B. Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear
- C. Test routing with representative questions → add each specialist as a connected agent → tune the descriptions where misroutes appear → write the parent agents routing instructions
- D. Tune the descriptions where misroutes appear → write the parent agents routing instructions → test routing with representative questions → add each specialist as a connected agent

### 47. A parent passes the full transcript and the same broad knowledge to every child it calls. Which two changes reduce cost and contradiction? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Build one large agent with every topic so there is a single place to change
- B. Route by intent in the parent and pass only the context the child needs
- C. Split the work into a parent agent that delegates to specialist child agents
- D. Give every child the same knowledge source so answers stay consistent
- E. Give each child a clear input and output contract and keep shared state in the parent

### 48. A tested Foundry agent with custom tools must answer inside the Copilot Studio conversation. What should be done?

Domain: Integrate and extend agents in Copilot Studio

- A. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Deploy the model in Foundry and point the custom prompt at that deployment

### 49. A Foundry agent quotes an older policy than the Copilot Studio parent. What should be aligned?

Domain: Integrate and extend agents in Copilot Studio

- A. Ground the Foundry agent in the same indexed knowledge so both layers answer consistently
- B. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity
- C. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- D. Evaluate the Foundry agent against the same test set before it is connected

### 50. A Foundry agent and a specific model deployment are both part of the plan. Which two steps apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Re-implement the Foundry agent’s logic as topics in Copilot Studio
- B. Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent
- C. Evaluate the Foundry agent against the same test set before it is connected
- D. Deploy the model in Foundry and point the custom prompt at that deployment
- E. Expose the Foundry agent through its endpoint and authenticate with the agent’s identity

### 51. A connected agent answers with more rights than the caller has. What should be verified?

Domain: Integrate and extend agents in Copilot Studio

- A. Write a precise name and description for the connected agent so routing works
- B. Retire the duplicate standalone agent once the parent covers its use cases
- C. Pin the connected agent’s published version that the parent was tested against
- D. Confirm the caller’s identity and permissions flow through to the connected agent

### 52. A child agent is republished weekly by another team and the parent is tested monthly. What should the parent pin?

Domain: Integrate and extend agents in Copilot Studio

- A. Write a precise name and description for the connected agent so routing works
- B. Pin the connected agent’s published version that the parent was tested against
- C. Add the existing agent as a connected agent and let the parent delegate to it
- D. Retire the duplicate standalone agent once the parent covers its use cases

### 53. A finance question must be answered from governed measures rather than raw tables. Which approach fits?

Domain: Integrate and extend agents in Copilot Studio

- A. Query the lakehouse directly from the agent with a SQL tool
- B. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- C. Define the measures in the semantic model so the data agent answers consistently
- D. Export the data nightly into files the agent can search

### 54. A data agent reports two different totals for the same question in one session. What should be fixed first?

Domain: Integrate and extend agents in Copilot Studio

- A. Define the measures in the semantic model so the data agent answers consistently
- B. Export the data nightly into files the agent can search
- C. Create a Fabric data agent over the semantic model and connect it to Copilot Studio
- D. Query the lakehouse directly from the agent with a SQL tool

### 55. An external partner needs to discover what an internal agent can do. What should be published?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure authentication between the agents so calls are authorized
- B. Model the remote capability as an A2A skill the agent can discover and invoke
- C. Publish an agent card that describes the remote agent’s skills and endpoint
- D. Track the remote task state and surface long-running results back into the conversation

### 56. A remote agent takes minutes and the conversation ends with no result. What is missing?

Domain: Integrate and extend agents in Copilot Studio

- A. Configure authentication between the agents so calls are authorized
- B. Publish an agent card that describes the remote agent’s skills and endpoint
- C. Rebuild the remote agent’s functionality locally instead of using the protocol
- D. Track the remote task state and surface long-running results back into the conversation

### 57. A partner agent may call two of eight internal skills. What should be defined?

Domain: Integrate and extend agents in Copilot Studio

- A. Define which remote agents are trusted and restrict the skills exposed to them
- B. Configure authentication between the agents so calls are authorized
- C. Publish an agent card that describes the remote agent’s skills and endpoint
- D. Model the remote capability as an A2A skill the agent can discover and invoke

### 58. A workload needs short answers, low latency, and a fixed cost ceiling. What should be decided first?

Domain: Integrate and extend agents in Copilot Studio

- A. Choose a model from the catalog that meets quality, latency, and residency needs
- B. Deploy the chosen model and reference the deployment from the custom prompt
- C. Keep the default model because it is already configured
- D. Provision enough quota and throughput for peak conversation volume

### 59. Customer text must stay in one jurisdiction. Which decision comes before cost comparison?

Domain: Integrate and extend agents in Copilot Studio

- A. Provision enough quota and throughput for peak conversation volume
- B. Choose a model from the catalog that meets quality, latency, and residency needs
- C. Deploy the model in a region that satisfies the data residency requirement
- D. Deploy the chosen model and reference the deployment from the custom prompt

### 60. A user reports a wrong answer and there is no record of the conversation. What should be enabled?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect the agent to Application Insights and emit conversation and tool telemetry
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Alert on failed tool calls and answer-quality regressions
- D. Query conversation and tool spans in Application Insights with KQL

### 61. A failure must be tied to the exact dependency call behind it. Which capability is needed?

Domain: Integrate and extend agents in Copilot Studio

- A. Correlate a failed answer with the tool call and knowledge retrieval behind it
- B. Query conversation and tool spans in Application Insights with KQL
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Sample telemetry so volume stays affordable while errors are always kept

### 62. Transcript retention costs are rising while errors must stay visible. What should change?

Domain: Integrate and extend agents in Copilot Studio

- A. Sample telemetry so volume stays affordable while errors are always kept
- B. Log full conversation transcripts indefinitely without retention limits
- C. Connect the agent to Application Insights and emit conversation and tool telemetry
- D. Query conversation and tool spans in Application Insights with KQL

### 63. An on-call engineer needs both detection and diagnosis. Which two capabilities apply? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Log full conversation transcripts indefinitely without retention limits
- B. Sample telemetry so volume stays affordable while errors are always kept
- C. Alert on failed tool calls and answer-quality regressions
- D. Connect the agent to Application Insights and emit conversation and tool telemetry
- E. Query conversation and tool spans in Application Insights with KQL

### 64. A team has 400 synthetic cases and no real transcripts. What should they add first?

Domain: Test and manage agents

- A. Test with a handful of happy-path questions before release
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Hold part of the set out of prompt tuning so results stay honest
- D. Build the test set from real anonymized conversations plus the cases that must never fail

### 65. A test set is edited silently between releases and scores jump. What should be introduced?

Domain: Test and manage agents

- A. Version the test set and rerun it for every change
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Test with a handful of happy-path questions before release
- D. Hold part of the set out of prompt tuning so results stay honest

### 66. A quality engineer is building the release test loop. Which sequence is correct?

Domain: Test and manage agents

- A. Classify them by intent → rerun on every change → collect real questions → score answers against the rubric → add the failures to the set
- B. Score answers against the rubric → collect real questions → add the failures to the set → classify them by intent → rerun on every change
- C. Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change
- D. Add the failures to the set → score answers against the rubric → collect real questions → rerun on every change → classify them by intent

### 67. A team keeps tuning prompts until the scores look good. Which two practices restore credibility? Select two.

Domain: Test and manage agents

- A. Test with a handful of happy-path questions before release
- B. Hold part of the set out of prompt tuning so results stay honest
- C. Build the test set from real anonymized conversations plus the cases that must never fail
- D. Include adversarial and edge cases such as out-of-scope and injection attempts
- E. Generate synthetic cases from the topics and intents the agent supports

### 68. A team must score 1,200 answers every release with one reviewer. Which method is practical?

Domain: Test and manage agents

- A. Use model-based grading against a rubric and review a human sample
- B. Have subject-matter experts score a sample against the rubric
- C. Score answers with keyword matching against expected phrases
- D. Rely on the builder trying a few questions in the test pane

### 69. A team is calibrating an automated grader. Which sequence is correct?

Domain: Test and manage agents

- A. Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release
- B. Score a sample by hand → run the full set on every release → define the rubric → adjust the grader → compare the grader with the human scores
- C. Adjust the grader → compare the grader with the human scores → define the rubric → run the full set on every release → score a sample by hand
- D. Run the full set on every release → define the rubric → score a sample by hand → adjust the grader → compare the grader with the human scores

### 70. A hundred failures reduce to four recurring causes when examined. What should the team do?

Domain: Test and manage agents

- A. Publish when the overall average looks acceptable
- B. Compare the new run against the previous baseline before publishing
- C. Keep failed cases in the test set so they cannot regress
- D. Group failures by topic and root cause instead of fixing items one at a time

### 71. A new prompt fixes one case and breaks three others. What should the process include?

Domain: Test and manage agents

- A. Keep failed cases in the test set so they cannot regress
- B. Compare the new run against the previous baseline before publishing
- C. Assign each failure cluster to the owner of the topic, prompt, or connector
- D. Publish when the overall average looks acceptable

### 72. A finished agent must travel with its flows and connection references. What must exist first?

Domain: Test and manage agents

- A. Send the agents topic files to the administrator by email
- B. Create a solution and add the agent and its dependencies to it
- C. Set the publisher prefix before creating components so names stay consistent
- D. Export the managed solution and import it into the target environment

### 73. A solution is being prepared for promotion to test. Which sequence is correct?

Domain: Test and manage agents

- A. Export managed and import downstream → create the solution → deploy through the pipeline → add the agent and its dependencies → replace hard-coded values with environment variables
- B. Add the agent and its dependencies → deploy through the pipeline → create the solution → replace hard-coded values with environment variables → export managed and import downstream
- C. Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline
- D. Replace hard-coded values with environment variables → deploy through the pipeline → create the solution → export managed and import downstream → add the agent and its dependencies

### 74. A connector key appears in the export file. Where should it live?

Domain: Test and manage agents

- A. Hard-code the production endpoint in the topic and change it after import
- B. Record the required values in the deployment notes for each environment
- C. Use the current value in production and a default value for development
- D. Store the secret in a vault and reference it from the environment variable

### 75. A solution points at a staging endpoint that must differ per environment. What should replace it?

Domain: Test and manage agents

- A. Store the secret in a vault and reference it from the environment variable
- B. Define an environment variable for the endpoint and set a value per environment
- C. Hard-code the production endpoint in the topic and change it after import
- D. Set the environment variable values as part of the pipeline deployment step

### 76. A two-environment solution needs per-stage values without a vault. Which two practices apply? Select two.

Domain: Test and manage agents

- A. Use the current value in production and a default value for development
- B. Hard-code the production endpoint in the topic and change it after import
- C. Store the secret in a vault and reference it from the environment variable
- D. Set the environment variable values as part of the pipeline deployment step
- E. Record the required values in the deployment notes for each environment

### 77. A release that had never been tested reached production. What should the pipeline add?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Import the solution by hand into production for each release
- C. Use the pipeline analytics to see which stage failed and why
- D. Add a pre-deployment step that runs the agent test set and blocks on failure

### 78. Releases are imported by hand, and nobody can name the live version. What should replace this?

Domain: Test and manage agents

- A. Require approval before the production stage runs
- B. Create a pipeline with development, test, and production stages
- C. Import the solution by hand into production for each release
- D. Add a pre-deployment step that runs the agent test set and blocks on failure

### 79. A team is setting up a gated deployment pipeline. Which sequence is correct?

Domain: Test and manage agents

- A. Configure the pipeline stages → add the pre-deployment test step → create the solution in development → run the deployment with approval → set environment variables for each stage
- B. Add the pre-deployment test step → set environment variables for each stage → create the solution in development → configure the pipeline stages → run the deployment with approval
- C. Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval
- D. Run the deployment with approval → create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step

### 80. A release must be reversible and the team must learn of failures immediately. Which two controls apply? Select two.

Domain: Test and manage agents

- A. Notify the owning team with the deployment result and the failed step
- B. Deploy only the components that changed when the pipeline supports it
- C. Pass environment-specific values through pipeline configuration rather than editing the solution
- D. Deploy on a fixed schedule regardless of readiness
- E. Keep the previous managed solution version so you can roll back

### 81. The security team's scan must block a deployment that fails. What should be added?

Domain: Test and manage agents

- A. Deploy only the components that changed when the pipeline supports it
- B. Notify the owning team with the deployment result and the failed step
- C. Pass environment-specific values through pipeline configuration rather than editing the solution
- D. Add a custom pipeline step that calls the validation job

### 82. Each stage needs a different tenant identifier, and the solution is rebuilt per stage. What should change?

Domain: Test and manage agents

- A. Notify the owning team with the deployment result and the failed step
- B. Deploy only the components that changed when the pipeline supports it
- C. Deploy on a fixed schedule regardless of readiness
- D. Pass environment-specific values through pipeline configuration rather than editing the solution

### 83. Users complain that answers are unhelpful, but no signal is captured. What should be added?

Domain: Test and manage agents

- A. Test once before launch and assume behaviour stays stable
- B. Track containment, resolution, and escalation metrics on a dashboard
- C. Sample production conversations and score them against the rubric on a schedule
- D. Capture user feedback in the conversation and route negative cases to review

### 84. Nobody can say whether answer quality held over the last quarter. What should be introduced?

Domain: Test and manage agents

- A. Track containment, resolution, and escalation metrics on a dashboard
- B. Test once before launch and assume behaviour stays stable
- C. Sample production conversations and score them against the rubric on a schedule
- D. Alert on rising fallback and handoff rates

### 85. One solution must serve internal staff and external customers. Which two channel decisions apply? Select two.

Domain: Plan and configure agent solutions

- A. Add the channel for omni-channel engagement so external support queues can route to it
- B. Publish to email and answer asynchronously
- C. Publish to a public website with authenticated sign-in
- D. Embed the agent in a custom application through the Direct Line channel
- E. Publish to Microsoft Teams and keep the agent inside the tenant

### 86. A 60-topic agent needs the claims dialogue separated so another team can own it. What should be configured?

Domain: Plan and configure agent solutions

- A. Store the value in a global variable so later topics can read it
- B. Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns
- C. Configure the topic as a redirect target with its own trigger phrases
- D. Configure the message node to send a formatted message with the fields the user needs

### 87. A team is connecting a Fabric data agent to a Copilot Studio parent. Which sequence is correct?

Domain: Integrate and extend agents in Copilot Studio

- A. Model the measures in the semantic model → create the Fabric data agent over it → grant the data agent read access → connect it to Copilot Studio → test the questions it must refuse
- B. Connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it → test the questions it must refuse → grant the data agent read access
- C. Grant the data agent read access → create the Fabric data agent over it → model the measures in the semantic model → connect it to Copilot Studio → test the questions it must refuse
- D. Test the questions it must refuse → grant the data agent read access → connect it to Copilot Studio → model the measures in the semantic model → create the Fabric data agent over it

### 88. A model is approved but the prompt still calls the platform default. What is missing?

Domain: Integrate and extend agents in Copilot Studio

- A. Keep the default model because it is already configured
- B. Deploy the chosen model and reference the deployment from the custom prompt
- C. Deploy the model in a region that satisfies the data residency requirement
- D. Provision enough quota and throughput for peak conversation volume

---

## Case study — Cobalt Bank

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. The agent may prepare a payment instruction but never submit one without a decision. Which pattern fits?

Domain: Plan and configure agent solutions

- A. Let the agent complete the action and notify a person afterwards
- B. Have the agent draft the action and require a person to submit it in the source system
- C. Set a response timeout and route to a fallback owner when nobody answers
- D. Send an approval request and pause the flow until a person responds

### 90. The settlement system sits in a locked network and exposes only an internal SOAP endpoint. Which integration fits?

Domain: Plan and configure agent solutions

- A. Call the internal endpoint straight from the topic over HTTP
- B. Batch the requests and post them to the source system on a schedule
- C. Expose the system through a virtual table or connector view that the agent can read
- D. Mediate the on-premises call through an on-premises data gateway

### 91. Releases need per-stage settings and a quick reversal. Which two controls apply? Select two.

Domain: Test and manage agents

- A. Notify the owning team with the deployment result and the failed step
- B. Keep the previous managed solution version so you can roll back
- C. Deploy only the components that changed when the pipeline supports it
- D. Deploy on a fixed schedule regardless of readiness
- E. Pass environment-specific values through pipeline configuration rather than editing the solution

---

## Case study — Kestrel Support

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A password question returns an article from the billing library because the node searches everything. What should change?

Domain: Plan and configure agent solutions

- A. Require the answer to cite retrieved passages and refuse when none are found
- B. Add a fallback topic for low-confidence answers that hands off to a person
- C. Configure a custom prompt that fixes the tone, structure, and citation behaviour
- D. Point the generative answers node at the specific knowledge source for the question

### 93. The billing API sometimes returns fields the agent has never seen, and the answer becomes raw JSON. What should be added?

Domain: Integrate and extend agents in Copilot Studio

- A. Call the REST API from a topic with a Send HTTP request action
- B. Define the response schema so the agent can reason over the returned fields
- C. Call the API from an agent flow and return the parsed response to the topic
- D. Hard-code the endpoint URL and key inside the topic

### 94. Escalation rates must be compared across model changes. What should the test set be?

Domain: Test and manage agents

- A. Test with a handful of happy-path questions before release
- B. Generate synthetic cases from the topics and intents the agent supports
- C. Hold part of the set out of prompt tuning so results stay honest
- D. Version the test set and rerun it for every change

---

## Case study — Redwood Public Works

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. The department must show which record was read for any answer. What should be enabled?

Domain: Plan and configure agent solutions

- A. Separate development and production environments with environment security groups
- B. Apply a data loss prevention policy that blocks unapproved connectors in the environment
- C. Restrict who can author and publish with Copilot Studio security roles
- D. Turn on audit logging and retain agent conversation records

### 96. Permit data must never be queried over the public internet. What should be configured?

Domain: Integrate and extend agents in Copilot Studio

- A. Connect to the search service over a private endpoint with managed identity
- B. Recreate the index on every publish so it never goes stale
- C. Use hybrid retrieval with vector and keyword queries
- D. Create the index with the fields, vector profile, and semantic configuration the agent needs

### 97. Answer-quality findings have no owner and never become changes. What should be introduced?

Domain: Test and manage agents

- A. Group failures by topic and root cause instead of fixing items one at a time
- B. Assign each failure cluster to the owner of the topic, prompt, or connector
- C. Keep failed cases in the test set so they cannot regress
- D. Publish when the overall average looks acceptable

---

## Case study — Trellis Media

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Briefs, brand rules, and performance data sit in three systems with different access models. Which two routes fit? Select two.

Domain: Integrate and extend agents in Copilot Studio

- A. Register the database as a knowledge source so the agent can query it directly
- B. Index the content in Azure AI Search and use it as the knowledge source
- C. Upload the documents as file knowledge on the agent
- D. Connect the source through a Copilot connector so its content is indexed for answers
- E. Connect through a Power Platform connector and query it from a tool or flow

### 99. One brand-rule dialogue must serve three campaign agents and change once. What should be built?

Domain: Plan and configure agent solutions

- A. Extract the shared logic into a reusable component or child agent and reference it
- B. Expose the shared integration as a custom connector any agent can add as a tool
- C. Copy the topics into each agent so every team can edit its own copy
- D. Rebuild the same topic in each agent to avoid a shared dependency

### 100. Account managers rate answers badly, and the team wants the transcript with the rating. What should be added?

Domain: Test and manage agents

- A. Sample production conversations and score them against the rubric on a schedule
- B. Test once before launch and assume behaviour stays stable
- C. Track containment, resolution, and escalation metrics on a dashboard
- D. Capture user feedback in the conversation and route negative cases to review

---

## Answer key and explanations

### Question 1 — B

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway brokers the call without opening an inbound path into the network. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path into the network.
- **B:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway brokers the call without opening an inbound path into the network.
- **C:** Incorrect for this question. Mirroring gives the agent fast analytical access without touching the source system per question. It adds replication latency and a second copy of the data. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path into the network.
- **D:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path into the network.

### Question 2 — D

Answer: Copy the records nightly into Dataverse and answer from the copy. A nightly copy answers yesterday's questions and needs its own reconciliation, which the plan must state. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which the plan must state.
- **B:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which the plan must state.
- **C:** Incorrect for this question. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Why the correct answer wins: A nightly copy answers yesterday's questions and needs its own reconciliation, which the plan must state.
- **D:** Correct. A nightly copy removes the live dependency but answers yesterday’s questions and needs its own reconciliation. In this case: A nightly copy answers yesterday's questions and needs its own reconciliation, which the plan must state.

### Question 3 — A

Answer: Use the agent managed identity for Azure resources and keep user identity for business data. The managed identity reaches the Azure resource without a stored key. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Mixing both is normal: platform resources are called by the agent identity, business records by the user. Each call still needs an explicit permission grant. In this case: The managed identity reaches the Azure resource without a stored key.
- **B:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: The managed identity reaches the Azure resource without a stored key.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: The managed identity reaches the Azure resource without a stored key.
- **D:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: The managed identity reaches the Azure resource without a stored key.

### Question 4 — A, B

Answers: Require Microsoft Entra ID sign-in for the agent and pass the user token downstream; Use the on-behalf-of flow so the agent calls the API as the signed-in user. Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. Local study-map skill 1.2 (Identity Strategy and Authentication), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. User sign-in keeps the agent inside the tenant identity model and lets downstream systems see who asked. Token passing has to be configured per connection. In this case: Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API.
- **B:** Correct. On-behalf-of preserves the caller’s identity across service boundaries, so the API applies that user’s own permissions. It needs consent and a registered client. In this case: Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API.
- **C:** Incorrect for this question. Anonymous access to an internal agent removes the audit trail and usually fails the security review before it reaches the API. Why the correct answer wins: Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API.
- **D:** Incorrect for this question. One shared account is easy to set up and destroys per-user accountability and least privilege. Why the correct answer wins: Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API.
- **E:** Incorrect for this question. A shared key in a variable is visible in the design surface and identical for all users, so nothing can be attributed or revoked per person. Why the correct answer wins: Tenant sign-in identifies the user, and the on-behalf-of flow carries that identity into the ticket API.

### Question 5 — B

Answer: Embed the agent in a custom application through the Direct Line channel. Direct Line gives the app control of the interface and authentication. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Direct Line gives the app control of the interface and authentication.
- **B:** Correct. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. In this case: Direct Line gives the app control of the interface and authentication.
- **C:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Direct Line gives the app control of the interface and authentication.
- **D:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Direct Line gives the app control of the interface and authentication.

### Question 6 — D

Answer: Publish the agent into Microsoft 365 Copilot so it appears alongside other agents. Publishing into the Copilot experience surfaces the agent where staff already work. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. Why the correct answer wins: Publishing into the Copilot experience surfaces the agent where staff already work.
- **B:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Publishing into the Copilot experience surfaces the agent where staff already work.
- **C:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Publishing into the Copilot experience surfaces the agent where staff already work.
- **D:** Correct. Surfacing the agent in Copilot puts it where employees already work. It inherits Copilot licensing and admin controls. In this case: Publishing into the Copilot experience surfaces the agent where staff already work.

### Question 7 — C

Answer: Add the channel for omni-channel engagement so external support queues can route to it. Omni-channel engagement carries the conversation, and its transcript, into the queue. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Omni-channel engagement carries the conversation, and its transcript, into the queue.
- **B:** Incorrect for this question. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Why the correct answer wins: Omni-channel engagement carries the conversation, and its transcript, into the queue.
- **C:** Correct. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. In this case: Omni-channel engagement carries the conversation, and its transcript, into the queue.
- **D:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: Omni-channel engagement carries the conversation, and its transcript, into the queue.

### Question 8 — B

Answer: Enforce the source system’s permissions in the knowledge layer so answers respect access. Permission trimming in the knowledge layer keeps each segment's content out of the other's answers. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Permission trimming in the knowledge layer keeps each segment's content out of the other's answers.
- **B:** Correct. An agent must never answer from content the caller could not open directly. Permission trimming belongs in the retrieval layer, not in the prompt. In this case: Permission trimming in the knowledge layer keeps each segment's content out of the other's answers.
- **C:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Permission trimming in the knowledge layer keeps each segment's content out of the other's answers.
- **D:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Permission trimming in the knowledge layer keeps each segment's content out of the other's answers.

### Question 9 — C

Answer: Constrain the tools the agent may call, validate tool output, and limit autonomous actions. Constraining tools and validating output limits what an injected instruction can achieve. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Constraining tools and validating output limits what an injected instruction can achieve.
- **B:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: Constraining tools and validating output limits what an injected instruction can achieve.
- **C:** Correct. Prompt injection defence is mostly about blast radius: fewer tools, checked outputs, and a human before irreversible actions. In this case: Constraining tools and validating output limits what an injected instruction can achieve.
- **D:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Constraining tools and validating output limits what an injected instruction can achieve.

### Question 10 — C

Answer: Apply a data loss prevention policy that blocks unapproved connectors in the environment. A data loss prevention policy refuses the unapproved connector at the environment level. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: A data loss prevention policy refuses the unapproved connector at the environment level.
- **B:** Incorrect for this question. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Why the correct answer wins: A data loss prevention policy refuses the unapproved connector at the environment level.
- **C:** Correct. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. In this case: A data loss prevention policy refuses the unapproved connector at the environment level.
- **D:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: A data loss prevention policy refuses the unapproved connector at the environment level.

### Question 11 — B

Answer: Expose the shared integration as a custom connector any agent can add as a tool. A custom connector gives every agent one typed, authenticated interface to the API. A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A custom connector gives every agent one typed, authenticated interface to the API.
- **B:** Correct. A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once. In this case: A custom connector gives every agent one typed, authenticated interface to the API.
- **C:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A custom connector gives every agent one typed, authenticated interface to the API.
- **D:** Incorrect for this question. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Why the correct answer wins: A custom connector gives every agent one typed, authenticated interface to the API.

### Question 12 — A

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution exists and is configured before export, and the pipeline performs the promotion. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution exists and is configured before export, and the pipeline performs the promotion.
- **B:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution exists and is configured before export, and the pipeline performs the promotion.
- **C:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution exists and is configured before export, and the pipeline performs the promotion.
- **D:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution exists and is configured before export, and the pipeline performs the promotion.

### Question 13 — C

Answer: Create an agent flow with a manual trigger that the topic calls with inputs. A manual-trigger agent flow runs on demand and returns values to the conversation. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns values to the conversation.
- **B:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns values to the conversation.
- **C:** Correct. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. In this case: A manual-trigger agent flow runs on demand and returns values to the conversation.
- **D:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: A manual-trigger agent flow runs on demand and returns values to the conversation.

### Question 14 — D

Answer: Add the capability as a connector action so the agent can call it without a flow. A connector action adds the operation as a typed tool without a flow. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.
- **B:** Incorrect for this question. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.
- **C:** Incorrect for this question. The connector action does the actual work, and the flow wraps it with inputs, outputs, and error handling. Why the correct answer wins: A connector action adds the operation as a typed tool without a flow.
- **D:** Correct. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. In this case: A connector action adds the operation as a typed tool without a flow.

### Question 15 — A

Answer: Use an automated cloud flow triggered by an event and have the agent wait for it. An automated flow reacts to the closure event without blocking the conversation. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. In this case: An automated flow reacts to the closure event without blocking the conversation.
- **B:** Incorrect for this question. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Why the correct answer wins: An automated flow reacts to the closure event without blocking the conversation.
- **C:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: An automated flow reacts to the closure event without blocking the conversation.
- **D:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: An automated flow reacts to the closure event without blocking the conversation.

### Question 16 — B, E

Answers: Wrap the calls in a scope with a parallel error branch that returns a structured failure; Define typed input and output parameters on the flow and bind them from the topic. Typed parameters return the outcome, and an error branch prevents a silent stall. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. Local study-map skill 1.6 (Agent Flows, Actions, and Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A connector action is the lightest route when no multi-step logic is needed. It also gives the agent a typed tool description. Why the correct answer wins: Typed parameters return the outcome, and an error branch prevents a silent stall.
- **B:** Correct. Typed parameters are what let the topic pass values in and read values back. Without them the flow cannot report success or failure. In this case: Typed parameters return the outcome, and an error branch prevents a silent stall.
- **C:** Incorrect for this question. Event flows are right for background work, but a conversation cannot block on an event that may never arrive. Why the correct answer wins: Typed parameters return the outcome, and an error branch prevents a silent stall.
- **D:** Incorrect for this question. A manual-trigger agent flow runs when the topic invokes it and returns values to the conversation. It is the standard way to add multi-step logic. Why the correct answer wins: Typed parameters return the outcome, and an error branch prevents a silent stall.
- **E:** Correct. Error handling has to hand the conversation a value it can act on. A silent failure leaves the user waiting for an answer that never comes. In this case: Typed parameters return the outcome, and an error branch prevents a silent stall.

### Question 17 — C

Answer: Hand the conversation off to a live agent with the context attached. A discretionary decision belongs with a person, so the conversation is handed over with its context. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **B:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **C:** Correct. A handoff transfers the conversation and its history to a person. It suits judgement calls, not a single recorded approval. In this case: A discretionary decision belongs with a person, so the conversation is handed over with its context.
- **D:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: A discretionary decision belongs with a person, so the conversation is handed over with its context.

### Question 18 — B

Answer: Have the agent draft the action and require a person to submit it in the source system. Drafting leaves the irreversible send with the human in the system that owns it. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A card in Teams puts the decision where the approver already works. The flow must handle no response and a rejection. Why the correct answer wins: Drafting leaves the irreversible send with the human in the system that owns it.
- **B:** Correct. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. In this case: Drafting leaves the irreversible send with the human in the system that owns it.
- **C:** Incorrect for this question. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Why the correct answer wins: Drafting leaves the irreversible send with the human in the system that owns it.
- **D:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: Drafting leaves the irreversible send with the human in the system that owns it.

### Question 19 — B

Answer: Configure a retry policy and terminate with a failure code the topic can read. A retry policy absorbs the transient fault before the topic reports anything. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **B:** Correct. Transient faults deserve a retry, and a permanent one deserves a clear failure value. Returning nothing is what breaks the conversation. In this case: A retry policy absorbs the transient fault before the topic reports anything.
- **C:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.
- **D:** Incorrect for this question. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Why the correct answer wins: A retry policy absorbs the transient fault before the topic reports anything.

### Question 20 — C

Answer: Send flow telemetry to Application Insights and query the traces. Traces in Application Insights keep the evidence beyond the run history window. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. Why the correct answer wins: Traces in Application Insights keep the evidence beyond the run history window.
- **B:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Traces in Application Insights keep the evidence beyond the run history window.
- **C:** Correct. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. In this case: Traces in Application Insights keep the evidence beyond the run history window.
- **D:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Traces in Application Insights keep the evidence beyond the run history window.

### Question 21 — C, E

Answers: Review the flow run history and its action-level inputs and outputs; Configure an alert on failed runs and route it to the owning team. Run history shows what each action received, and alerts route the failures that need attention. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. Local study-map skill 1.8 (Flow Parameters, Error Handling, and Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Built-in analytics show engagement, resolution, and escalation by topic. It is aggregate evidence, not a per-request trace. Why the correct answer wins: Run history shows what each action received, and alerts route the failures that need attention.
- **B:** Incorrect for this question. Traces correlate a conversation with the flow and API calls behind it. They are what you need when the failure is intermittent. Why the correct answer wins: Run history shows what each action received, and alerts route the failures that need attention.
- **C:** Correct. Run history shows which action failed and what it received. It is the fastest first stop for a failing flow. In this case: Run history shows what each action received, and alerts route the failures that need attention.
- **D:** Incorrect for this question. A comment documents intent for the next author but changes nothing about how the run behaves. Why the correct answer wins: Run history shows what each action received, and alerts route the failures that need attention.
- **E:** Correct. An alert turns a silent failure into a work item. It needs an owner and a threshold that does not fire constantly. In this case: Run history shows what each action received, and alerts route the failures that need attention.

### Question 22 — D

Answer: Set the variable inside a scope and reset it at the start of the topic so it does not leak between turns. Keep the code in topic scope and clear it so it cannot survive into later turns. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: Keep the code in topic scope and clear it so it cannot survive into later turns.
- **B:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: Keep the code in topic scope and clear it so it cannot survive into later turns.
- **C:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: Keep the code in topic scope and clear it so it cannot survive into later turns.
- **D:** Correct. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. In this case: Keep the code in topic scope and clear it so it cannot survive into later turns.

### Question 23 — B

Answer: Return an adaptive card so the data renders in labelled fields. An adaptive card renders labelled values and an action in one response. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: An adaptive card renders labelled values and an action in one response.
- **B:** Correct. Cards render structured data and can carry actions. They need a schema and a fallback for clients that do not render them. In this case: An adaptive card renders labelled values and an action in one response.
- **C:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: An adaptive card renders labelled values and an action in one response.
- **D:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: An adaptive card renders labelled values and an action in one response.

### Question 24 — B, C

Answers: Store the value in a global variable so later topics can read it; Configure the message node to send a formatted message with the fields the user needs. A global variable carries the customer context, and a formatted message presents the list clearly. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. A message node can send structured text without a card. It is the lightest way to make a list readable. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A global variable carries the customer context, and a formatted message presents the list clearly.
- **B:** Correct. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. In this case: A global variable carries the customer context, and a formatted message presents the list clearly.
- **C:** Correct. A message node can send structured text without a card. It is the lightest way to make a list readable. In this case: A global variable carries the customer context, and a formatted message presents the list clearly.
- **D:** Incorrect for this question. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Why the correct answer wins: A global variable carries the customer context, and a formatted message presents the list clearly.
- **E:** Incorrect for this question. Raw output is quick to build and hard to read, especially when a field is empty or very long. Why the correct answer wins: A global variable carries the customer context, and a formatted message presents the list clearly.

### Question 25 — C

Answer: Configure a custom prompt that fixes the tone, structure, and citation behaviour. A custom prompt constrains length and structure without altering the source knowledge. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A custom prompt constrains length and structure without altering the source knowledge.
- **B:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: A custom prompt constrains length and structure without altering the source knowledge.
- **C:** Correct. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. In this case: A custom prompt constrains length and structure without altering the source knowledge.
- **D:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: A custom prompt constrains length and structure without altering the source knowledge.

### Question 26 — C

Answer: Add a fallback topic for low-confidence answers that hands off to a person. A fallback path for low-confidence answers hands the question to a person instead of guessing. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Images can help recognition but add nothing when the question is about a value or a status. Why the correct answer wins: A fallback path for low-confidence answers hands the question to a person instead of guessing.
- **B:** Incorrect for this question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Why the correct answer wins: A fallback path for low-confidence answers hands the question to a person instead of guessing.
- **C:** Correct. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. In this case: A fallback path for low-confidence answers hands the question to a person instead of guessing.
- **D:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: A fallback path for low-confidence answers hands the question to a person instead of guessing.

### Question 27 — B

Answer: Connect through a Power Platform connector and query it from a tool or flow. A Power Platform connector exposes those operations as callable tools. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Power Platform connector exposes those operations as callable tools.
- **B:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Power Platform connector exposes those operations as callable tools.
- **C:** Incorrect for this question. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. Why the correct answer wins: A Power Platform connector exposes those operations as callable tools.
- **D:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Power Platform connector exposes those operations as callable tools.

### Question 28 — A, C

Answers: Add the SharePoint site as a knowledge source and rely on item-level permissions; Index the content in Azure AI Search and use it as the knowledge source. SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. In this case: SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control.
- **B:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control.
- **C:** Correct. SharePoint knowledge respects the user’s existing item access and needs no copy. Large libraries still need curated scope. In this case: SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control.
- **D:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control.
- **E:** Incorrect for this question. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Why the correct answer wins: SharePoint knowledge honours item access, and an AI Search index adds explicit filtering and ranking control.

### Question 29 — D

Answer: Create the index with the fields, vector profile, and semantic configuration the agent needs. The schema, including filterable and retrievable fields, decides what queries can do. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The schema, including filterable and retrievable fields, decides what queries can do.
- **B:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The schema, including filterable and retrievable fields, decides what queries can do.
- **C:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: The schema, including filterable and retrievable fields, decides what queries can do.
- **D:** Correct. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. In this case: The schema, including filterable and retrievable fields, decides what queries can do.

### Question 30 — B

Answer: Use hybrid retrieval with vector and keyword queries. Hybrid retrieval adds keyword matching so exact identifiers are found alongside paraphrases. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: Hybrid retrieval adds keyword matching so exact identifiers are found alongside paraphrases.
- **B:** Correct. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. In this case: Hybrid retrieval adds keyword matching so exact identifiers are found alongside paraphrases.
- **C:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: Hybrid retrieval adds keyword matching so exact identifiers are found alongside paraphrases.
- **D:** Incorrect for this question. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Why the correct answer wins: Hybrid retrieval adds keyword matching so exact identifiers are found alongside paraphrases.

### Question 31 — B

Answer: Connect to the search service over a private endpoint with managed identity. A private endpoint with managed identity keeps the traffic off the public internet. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: A private endpoint with managed identity keeps the traffic off the public internet.
- **B:** Correct. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. In this case: A private endpoint with managed identity keeps the traffic off the public internet.
- **C:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: A private endpoint with managed identity keeps the traffic off the public internet.
- **D:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: A private endpoint with managed identity keeps the traffic off the public internet.

### Question 32 — C, D

Answers: Apply a security filter on the query before the agent composes an answer; Enable semantic ranking and let the agent use the reranked results. The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads.
- **C:** Correct. Semantic ranking improves the order of the top results and therefore the passages the model sees. It costs extra latency and quota. In this case: The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads.
- **D:** Correct. Filtering at query time is the only reliable way to stop one user’s content reaching another. Post-filtering leaks through result counts and answers. In this case: The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads.
- **E:** Incorrect for this question. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Why the correct answer wins: The security filter keeps unauthorized content out, and semantic ranking improves which passage the model reads.

### Question 33 — D

Answer: Replace the screen automation with an API once the application exposes one. Replacing screen automation with the API removes a fragile dependency. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Computer use drives the user interface when no API exists. It is fragile to layout changes and must be monitored. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **B:** Incorrect for this question. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **C:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Replacing screen automation with the API removes a fragile dependency.
- **D:** Correct. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. In this case: Replacing screen automation with the API removes a fragile dependency.

### Question 34 — C

Answer: Run the tool unattended on a dedicated machine with a vaulted credential. Run unattended on a dedicated machine with a vaulted credential. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The tool needs a host with the application installed and a dedicated identity. Sharing a builders desktop is neither reliable nor auditable. Why the correct answer wins: Run unattended on a dedicated machine with a vaulted credential.
- **B:** Incorrect for this question. An unvalidated click path will eventually click the wrong control after an application update. Why the correct answer wins: Run unattended on a dedicated machine with a vaulted credential.
- **C:** Correct. Unattended runs need a credential that no person holds and a host that stays available. Interactive desktop sessions cannot be depended on. In this case: Run unattended on a dedicated machine with a vaulted credential.
- **D:** Incorrect for this question. An API is more stable and cheaper to run than clicking through a screen. Retiring the automation removes a whole class of failure. Why the correct answer wins: Run unattended on a dedicated machine with a vaulted credential.

### Question 35 — B

Answer: Confirm no API exists for the task → provision a machine with the application installed → record the steps on a test record → run the tool and inspect the step log → monitor for interface changes. Confirm no API, prepare a host, record steps, run and inspect, then monitor for change. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. Local study-map skill 2.3 (Computer Use Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A run cannot precede the host and the recorded steps. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **B:** Correct. The API check justifies the approach, the host comes before recording, and monitoring follows the first run. In this case: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **C:** Incorrect for this question. Recording happens on the prepared machine, after the API check. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.
- **D:** Incorrect for this question. Monitoring a tool that has never run and has no host is not possible. Why the correct answer wins: Confirm no API, prepare a host, record steps, run and inspect, then monitor for change.

### Question 36 — C

Answer: Add an MCP server as a tool and let the agent discover the tools it exposes. An MCP server exposes the catalogue so agents discover tools without redeployment. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **B:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **C:** Correct. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. In this case: An MCP server exposes the catalogue so agents discover tools without redeployment.
- **D:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: An MCP server exposes the catalogue so agents discover tools without redeployment.

### Question 37 — C

Answer: Expose only the MCP tools the task needs and review their descriptions. Expose only the needed tools to limit what a bad instruction can reach. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.
- **B:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.
- **C:** Correct. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. In this case: Expose only the needed tools to limit what a bad instruction can reach.
- **D:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Expose only the needed tools to limit what a bad instruction can reach.

### Question 38 — B

Answer: Use a streamable HTTP MCP server so the agent can reach it over the network. Streamable HTTP reaches a remote server over the network. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Wrapping the API once gives every agent the same typed tools. The wrapper owns authentication and error translation. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **B:** Correct. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. In this case: Streamable HTTP reaches a remote server over the network.
- **C:** Incorrect for this question. A local process transport does not exist in a hosted agent, so the server must be reachable over the network. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.
- **D:** Incorrect for this question. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Why the correct answer wins: Streamable HTTP reaches a remote server over the network.

### Question 39 — C

Answer: Configure the MCP server connection with the authentication the server requires. Configure the server connection's authentication before expecting successful calls. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. Local study-map skill 2.4 (MCP Tools), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Every exposed tool widens what a bad instruction can do. Descriptions are what the model uses to choose, so they must be accurate. Why the correct answer wins: Configure the server connection's authentication before expecting successful calls.
- **B:** Incorrect for this question. Streamable HTTP is the transport for a remote server. A local process transport only works when the server runs beside the client. Why the correct answer wins: Configure the server connection's authentication before expecting successful calls.
- **C:** Correct. Server connections need credentials the agent can use on the user’s behalf. Without them the tools list but every call fails. In this case: Configure the server connection's authentication before expecting successful calls.
- **D:** Incorrect for this question. MCP gives the agent a standard interface to external tools and resources. Discovery means the server can grow without a redeploy of the agent. Why the correct answer wins: Configure the server connection's authentication before expecting successful calls.

### Question 40 — C

Answer: Define the response schema so the agent can reason over the returned fields. A declared response schema lets the model use named fields in a readable answer. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A declared response schema lets the model use named fields in a readable answer.
- **B:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A declared response schema lets the model use named fields in a readable answer.
- **C:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: A declared response schema lets the model use named fields in a readable answer.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A declared response schema lets the model use named fields in a readable answer.

### Question 41 — A

Answer: Configure connector authentication so each call uses the caller’s identity. Per-user authentication makes the API evaluate each caller's rights. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Per-user authentication keeps the API permissions honest. A shared key makes every user as powerful as the key. In this case: Per-user authentication makes the API evaluate each caller's rights.
- **B:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **C:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.
- **D:** Incorrect for this question. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. Why the correct answer wins: Per-user authentication makes the API evaluate each caller's rights.

### Question 42 — D, E

Answers: Create a custom connector from the OpenAPI definition and add it as a tool; Call the API from an agent flow and return the parsed response to the topic. A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed.
- **B:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed.
- **C:** Incorrect for this question. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Why the correct answer wins: A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed.
- **D:** Correct. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. In this case: A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed.
- **E:** Correct. An OpenAPI-backed connector gives the agent typed operations and a real authentication model. It is reusable across agents. In this case: A custom connector from the published definition gives typed reuse, and a flow adds retry and shaping where needed.

### Question 43 — A

Answer: Split the work into a parent agent that delegates to specialist child agents. Delegating to specialist children gives each area an owner and an independent release. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. In this case: Delegating to specialist children gives each area an owner and an independent release.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Delegating to specialist children gives each area an owner and an independent release.
- **C:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Delegating to specialist children gives each area an owner and an independent release.
- **D:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Delegating to specialist children gives each area an owner and an independent release.

### Question 44 — A

Answer: Write the parent’s instructions to describe when each child should be used. Routing depends on the parent's instructions, so unclear delegation guidance is the cause. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Routing quality is mostly instruction quality. Vague descriptions cause the parent to answer itself instead of delegating. In this case: Routing depends on the parent's instructions, so unclear delegation guidance is the cause.
- **B:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Routing depends on the parent's instructions, so unclear delegation guidance is the cause.
- **C:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: Routing depends on the parent's instructions, so unclear delegation guidance is the cause.
- **D:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: Routing depends on the parent's instructions, so unclear delegation guidance is the cause.

### Question 45 — A

Answer: Give each child a clear input and output contract and keep shared state in the parent. A contract that fixes field formats keeps the parent able to combine child outputs. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. In this case: A contract that fixes field formats keeps the parent able to combine child outputs.
- **B:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: A contract that fixes field formats keeps the parent able to combine child outputs.
- **C:** Incorrect for this question. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. Why the correct answer wins: A contract that fixes field formats keeps the parent able to combine child outputs.
- **D:** Incorrect for this question. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Why the correct answer wins: A contract that fixes field formats keeps the parent able to combine child outputs.

### Question 46 — B

Answer: Write the parent agents routing instructions → add each specialist as a connected agent → test routing with representative questions → tune the descriptions where misroutes appear. Instructions, children, routing tests, then tuning from the evidence. Instructions and children precede testing, and tuning follows evidence from the test. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Tuning before testing guesses at failures the test would reveal. Why the correct answer wins: Instructions, children, routing tests, then tuning from the evidence.
- **B:** Correct. Instructions and children precede testing, and tuning follows evidence from the test. In this case: Instructions, children, routing tests, then tuning from the evidence.
- **C:** Incorrect for this question. Testing requires the children and the instructions already in place. Why the correct answer wins: Instructions, children, routing tests, then tuning from the evidence.
- **D:** Incorrect for this question. There is no misroute to tune before the children exist and routing has been tested. Why the correct answer wins: Instructions, children, routing tests, then tuning from the evidence.

### Question 47 — B, D

Answers: Route by intent in the parent and pass only the context the child needs; Give every child the same knowledge source so answers stay consistent. Pass only the context each child needs, and ground every child in the same knowledge. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. Local study-map skill 2.6 (Multi-Agent Design in Copilot Studio), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. One large agent is easy to start and hard to test, own, or deploy without disturbing unrelated behaviour. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge.
- **B:** Correct. Minimal context reduces cost and accidental data exposure. Over-sharing across children is a common review finding. In this case: Pass only the context each child needs, and ground every child in the same knowledge.
- **C:** Incorrect for this question. Delegation keeps each agent small enough to test and own. The parent still has to describe when each child applies. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge.
- **D:** Correct. A shared source keeps definitions aligned across children. It also means one bad document affects every specialist equally. In this case: Pass only the context each child needs, and ground every child in the same knowledge.
- **E:** Incorrect for this question. Contracts stop the children from guessing at context. Keeping state in the parent avoids two children holding different versions of the truth. Why the correct answer wins: Pass only the context each child needs, and ground every child in the same knowledge.

### Question 48 — A

Answer: Publish the agent in Microsoft Foundry and connect it to Copilot Studio as a connected agent. Connect it as a connected agent so the evaluated behaviour answers the turn. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. In this case: Connect it as a connected agent so the evaluated behaviour answers the turn.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers the turn.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers the turn.
- **D:** Incorrect for this question. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Why the correct answer wins: Connect it as a connected agent so the evaluated behaviour answers the turn.

### Question 49 — A

Answer: Ground the Foundry agent in the same indexed knowledge so both layers answer consistently. Both layers must answer from the same indexed corpus. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Two layers answering from different corpora produce contradictions the user cannot explain. Shared grounding removes that class of defect. In this case: Both layers must answer from the same indexed corpus.
- **B:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Both layers must answer from the same indexed corpus.
- **C:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Both layers must answer from the same indexed corpus.
- **D:** Incorrect for this question. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Why the correct answer wins: Both layers must answer from the same indexed corpus.

### Question 50 — C, D

Answers: Evaluate the Foundry agent against the same test set before it is connected; Deploy the model in Foundry and point the custom prompt at that deployment. Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. Local study-map skill 2.7 (Foundry Agent Integration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Rebuilding duplicates work that already exists and drifts as soon as either side changes. Why the correct answer wins: Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt.
- **B:** Incorrect for this question. A Foundry agent brings models, tools, and evaluation from the Foundry side into the Copilot Studio conversation. The connection needs its own identity and testing. Why the correct answer wins: Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt.
- **C:** Correct. A connected agent inherits its own quality problems into your conversation. Testing it separately is what separates the two causes of a bad answer. In this case: Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt.
- **D:** Correct. Referencing a deployment gives control over model choice and version. It keeps the conversation in Copilot Studio rather than delegating the whole turn. In this case: Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt.
- **E:** Incorrect for this question. Direct endpoint calls suit custom orchestration. They put error handling and identity on your side of the boundary. Why the correct answer wins: Evaluate the agent on the shared test set, and deploy the model and reference it from the prompt.

### Question 51 — D

Answer: Confirm the caller’s identity and permissions flow through to the connected agent. Identity and permissions must flow through the delegation, or the child acts as a service. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Identity and permissions must flow through the delegation, or the child acts as a service.
- **B:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Identity and permissions must flow through the delegation, or the child acts as a service.
- **C:** Incorrect for this question. An unpinned dependency can change behaviour between your test run and your release. Why the correct answer wins: Identity and permissions must flow through the delegation, or the child acts as a service.
- **D:** Correct. Delegation must not quietly elevate the user. If identity does not flow, the connected agent answers from a service context. In this case: Identity and permissions must flow through the delegation, or the child acts as a service.

### Question 52 — B

Answer: Pin the connected agent’s published version that the parent was tested against. Pinning the tested version keeps behaviour stable between retests. An unpinned dependency can change behaviour between your test run and your release. Local study-map skill 2.8 (Connected and Existing Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. The parent chooses between children from their names and descriptions. A vague description causes misroutes that look like model failures. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.
- **B:** Correct. An unpinned dependency can change behaviour between your test run and your release. In this case: Pinning the tested version keeps behaviour stable between retests.
- **C:** Incorrect for this question. Reusing a published agent keeps its owners and its release cycle. The parent only needs to know when to call it. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.
- **D:** Incorrect for this question. Leaving two entry points invites divergence and doubles the testing burden. Why the correct answer wins: Pinning the tested version keeps behaviour stable between retests.

### Question 53 — B

Answer: Create a Fabric data agent over the semantic model and connect it to Copilot Studio. A Fabric data agent answers from the semantic model where the measures are defined. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures are defined.
- **B:** Correct. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. In this case: A Fabric data agent answers from the semantic model where the measures are defined.
- **C:** Incorrect for this question. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures are defined.
- **D:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: A Fabric data agent answers from the semantic model where the measures are defined.

### Question 54 — A

Answer: Define the measures in the semantic model so the data agent answers consistently. One defined measure removes the per-question interpretation of the number. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Measures encode the agreed definition. Without them every question invites a new interpretation of revenue. In this case: One defined measure removes the per-question interpretation of the number.
- **B:** Incorrect for this question. A nightly export adds staleness and a second definition of the numbers the warehouse already owns. Why the correct answer wins: One defined measure removes the per-question interpretation of the number.
- **C:** Incorrect for this question. A Fabric data agent answers analytical questions from governed data without exposing SQL to the model. It needs a semantic model with good measures. Why the correct answer wins: One defined measure removes the per-question interpretation of the number.
- **D:** Incorrect for this question. Raw SQL access is powerful and easy to get wrong, and it bypasses the measure definitions the business agreed. Why the correct answer wins: One defined measure removes the per-question interpretation of the number.

### Question 55 — C

Answer: Publish an agent card that describes the remote agent’s skills and endpoint. The agent card lists skills and the endpoint for discovery. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: The agent card lists skills and the endpoint for discovery.
- **B:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: The agent card lists skills and the endpoint for discovery.
- **C:** Correct. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. In this case: The agent card lists skills and the endpoint for discovery.
- **D:** Incorrect for this question. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Why the correct answer wins: The agent card lists skills and the endpoint for discovery.

### Question 56 — D

Answer: Track the remote task state and surface long-running results back into the conversation. A2A task state must be tracked so long-running results reach the conversation. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A2A task state must be tracked so long-running results reach the conversation.
- **B:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A2A task state must be tracked so long-running results reach the conversation.
- **C:** Incorrect for this question. Rebuilding defeats the point of a standard protocol and creates two implementations to keep aligned. Why the correct answer wins: A2A task state must be tracked so long-running results reach the conversation.
- **D:** Correct. A2A tasks can outlive a single call. Without state tracking the user is told nothing while the work is still running. In this case: A2A task state must be tracked so long-running results reach the conversation.

### Question 57 — A

Answer: Define which remote agents are trusted and restrict the skills exposed to them. A trust boundary restricts which skills a remote agent may invoke. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. Local study-map skill 2.10 (A2A Protocol Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Trust boundaries decide what a remote agent may invoke on your side. Unlimited exposure turns a partner into an insider. In this case: A trust boundary restricts which skills a remote agent may invoke.
- **B:** Incorrect for this question. Agent-to-agent calls still need an identity and a permission decision. An open endpoint is an open door. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.
- **C:** Incorrect for this question. The agent card is how another agent discovers what a remote agent can do. Without it the integration is hard-coded. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.
- **D:** Incorrect for this question. Skills are the callable unit in A2A. Each one needs a description precise enough for the caller to choose it. Why the correct answer wins: A trust boundary restricts which skills a remote agent may invoke.

### Question 58 — A

Answer: Choose a model from the catalog that meets quality, latency, and residency needs. Model choice balances quality, latency, and cost before deployment details matter. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. In this case: Model choice balances quality, latency, and cost before deployment details matter.
- **B:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Model choice balances quality, latency, and cost before deployment details matter.
- **C:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: Model choice balances quality, latency, and cost before deployment details matter.
- **D:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Model choice balances quality, latency, and cost before deployment details matter.

### Question 59 — C

Answer: Deploy the model in a region that satisfies the data residency requirement. Residency constrains acceptable deployments, so it is settled first. Residency is a legal constraint, so region choice precedes price comparison. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: Residency constrains acceptable deployments, so it is settled first.
- **B:** Incorrect for this question. Model choice is a trade between answer quality, response time, cost, and where the data may be processed. Why the correct answer wins: Residency constrains acceptable deployments, so it is settled first.
- **C:** Correct. Residency is a legal constraint, so region choice precedes price comparison. In this case: Residency constrains acceptable deployments, so it is settled first.
- **D:** Incorrect for this question. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Why the correct answer wins: Residency constrains acceptable deployments, so it is settled first.

### Question 60 — A

Answer: Connect the agent to Application Insights and emit conversation and tool telemetry. Conversation and tool telemetry makes the report investigable. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. In this case: Conversation and tool telemetry makes the report investigable.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **C:** Incorrect for this question. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.
- **D:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Conversation and tool telemetry makes the report investigable.

### Question 61 — A

Answer: Correlate a failed answer with the tool call and knowledge retrieval behind it. Correlated spans connect the conversation to the downstream call. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Correlation is the whole point: the symptom is in the conversation, the cause is usually in a dependency. In this case: Correlated spans connect the conversation to the downstream call.
- **B:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Correlated spans connect the conversation to the downstream call.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Correlated spans connect the conversation to the downstream call.
- **D:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Correlated spans connect the conversation to the downstream call.

### Question 62 — A

Answer: Sample telemetry so volume stays affordable while errors are always kept. Sample the volume and always keep errors, which controls cost without hiding failures. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. In this case: Sample the volume and always keep errors, which controls cost without hiding failures.
- **B:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Sample the volume and always keep errors, which controls cost without hiding failures.
- **C:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Sample the volume and always keep errors, which controls cost without hiding failures.
- **D:** Incorrect for this question. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Why the correct answer wins: Sample the volume and always keep errors, which controls cost without hiding failures.

### Question 63 — C, E

Answers: Alert on failed tool calls and answer-quality regressions; Query conversation and tool spans in Application Insights with KQL. Alerting detects the failure, and a KQL query diagnoses the individual conversation. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. Local study-map skill 2.12 (Application Insights Monitoring), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Unlimited transcript retention is a privacy and cost problem, not a monitoring strategy. Why the correct answer wins: Alerting detects the failure, and a KQL query diagnoses the individual conversation.
- **B:** Incorrect for this question. Sampling keeps cost predictable, and keeping errors makes the rare failure still visible. Why the correct answer wins: Alerting detects the failure, and a KQL query diagnoses the individual conversation.
- **C:** Correct. An alert converts a trend into an action. It needs an owner and a threshold tuned to real noise. In this case: Alerting detects the failure, and a KQL query diagnoses the individual conversation.
- **D:** Incorrect for this question. Telemetry is what makes a production failure diagnosable. Without it every report starts with a reproduction attempt. Why the correct answer wins: Alerting detects the failure, and a KQL query diagnoses the individual conversation.
- **E:** Correct. KQL joins a bad answer to the retrieval and tool calls behind it. It is the tool for a question no dashboard answers. In this case: Alerting detects the failure, and a KQL query diagnoses the individual conversation.

### Question 64 — D

Answer: Build the test set from real anonymized conversations plus the cases that must never fail. Real anonymized conversations carry phrasing and missing context that synthetic cases smooth away. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Real anonymized conversations carry phrasing and missing context that synthetic cases smooth away.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Real anonymized conversations carry phrasing and missing context that synthetic cases smooth away.
- **C:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Real anonymized conversations carry phrasing and missing context that synthetic cases smooth away.
- **D:** Correct. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. In this case: Real anonymized conversations carry phrasing and missing context that synthetic cases smooth away.

### Question 65 — A

Answer: Version the test set and rerun it for every change. Versioning the set makes comparisons meaningful and exposes edits. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: Versioning the set makes comparisons meaningful and exposes edits.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: Versioning the set makes comparisons meaningful and exposes edits.
- **C:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: Versioning the set makes comparisons meaningful and exposes edits.
- **D:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: Versioning the set makes comparisons meaningful and exposes edits.

### Question 66 — C

Answer: Collect real questions → classify them by intent → score answers against the rubric → add the failures to the set → rerun on every change. Questions, classification, scoring, failure log, then reruns. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Classification needs the questions, and the rerun is the last step, not the first. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.
- **B:** Incorrect for this question. Scoring cannot happen before there are questions to score. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.
- **C:** Correct. Questions precede classification, scoring precedes the failure log, and the loop closes by rerunning. In this case: Questions, classification, scoring, failure log, then reruns.
- **D:** Incorrect for this question. The failure log depends on scoring, and classification defines the categories the log uses. Why the correct answer wins: Questions, classification, scoring, failure log, then reruns.

### Question 67 — B, D

Answers: Hold part of the set out of prompt tuning so results stay honest; Include adversarial and edge cases such as out-of-scope and injection attempts. A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores.
- **B:** Correct. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. In this case: A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores.
- **C:** Incorrect for this question. Real questions carry the phrasing and missing context that synthetic ones smooth away. The must-never-fail cases protect the highest-consequence journeys. Why the correct answer wins: A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores.
- **D:** Correct. Edge cases are where agents fail most visibly. An out-of-scope question should produce a refusal, not a confident guess. In this case: A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores.
- **E:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A holdout slice measures honestly, and adversarial cases expose behaviour that tuning ignores.

### Question 68 — A

Answer: Use model-based grading against a rubric and review a human sample. Automated rubric grading scales, with a human sample for calibration. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Model-based grading scales to hundreds of cases, and the human sample keeps the grader calibrated. In this case: Automated rubric grading scales, with a human sample for calibration.
- **B:** Incorrect for this question. Expert scoring is the reference standard and does not scale to every release. It is best used to validate the automated grader. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.
- **C:** Incorrect for this question. Keyword matching is cheap and blind to a correct answer phrased differently. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.
- **D:** Incorrect for this question. The test pane is for development feedback, not for evidence about release quality. Why the correct answer wins: Automated rubric grading scales, with a human sample for calibration.

### Question 69 — A

Answer: Define the rubric → score a sample by hand → compare the grader with the human scores → adjust the grader → run the full set on every release. Rubric, human sample, comparison, adjustment, then full runs. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. Local study-map skill 3.2 (Evaluation Methods), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The rubric comes first, the human sample calibrates the grader, and the full run follows calibration. In this case: Rubric, human sample, comparison, adjustment, then full runs.
- **B:** Incorrect for this question. Hand scoring without a rubric produces judgements that cannot be compared with the grader. Why the correct answer wins: Rubric, human sample, comparison, adjustment, then full runs.
- **C:** Incorrect for this question. The grader cannot be adjusted before it is compared with human scores produced under a rubric. Why the correct answer wins: Rubric, human sample, comparison, adjustment, then full runs.
- **D:** Incorrect for this question. A full run without a rubric or a calibrated grader measures nothing consistently. Why the correct answer wins: Rubric, human sample, comparison, adjustment, then full runs.

### Question 70 — D

Answer: Group failures by topic and root cause instead of fixing items one at a time. Group by root cause and fix the causes rather than individual items. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Group by root cause and fix the causes rather than individual items.
- **B:** Incorrect for this question. A regression check catches the fix that repairs one case and breaks three. Why the correct answer wins: Group by root cause and fix the causes rather than individual items.
- **C:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Group by root cause and fix the causes rather than individual items.
- **D:** Correct. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. In this case: Group by root cause and fix the causes rather than individual items.

### Question 71 — B

Answer: Compare the new run against the previous baseline before publishing. A regression comparison against the previous run surfaces the three breakages. A regression check catches the fix that repairs one case and breaks three. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: A regression comparison against the previous run surfaces the three breakages.
- **B:** Correct. A regression check catches the fix that repairs one case and breaks three. In this case: A regression comparison against the previous run surfaces the three breakages.
- **C:** Incorrect for this question. Ownership converts findings into changes. An unowned backlog does not improve the agent. Why the correct answer wins: A regression comparison against the previous run surfaces the three breakages.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: A regression comparison against the previous run surfaces the three breakages.

### Question 72 — B

Answer: Create a solution and add the agent and its dependencies to it. Only solution-aware components move as a unit, so the agent and dependencies belong in a solution. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Topic files are not a supported deployment unit and carry no dependencies or version record. Why the correct answer wins: Only solution-aware components move as a unit, so the agent and dependencies belong in a solution.
- **B:** Correct. Only solution-aware components can be moved and versioned as a unit. The agent alone is not a deployable package. In this case: Only solution-aware components move as a unit, so the agent and dependencies belong in a solution.
- **C:** Incorrect for this question. The prefix is fixed early and awkward to change later. A consistent prefix also prevents name collisions in the target environment. Why the correct answer wins: Only solution-aware components move as a unit, so the agent and dependencies belong in a solution.
- **D:** Incorrect for this question. Export and import is the supported transport for a solution. Connections and variables still need configuration on arrival. Why the correct answer wins: Only solution-aware components move as a unit, so the agent and dependencies belong in a solution.

### Question 73 — C

Answer: Create the solution → add the agent and its dependencies → replace hard-coded values with environment variables → export managed and import downstream → deploy through the pipeline. The solution is packaged and configured before promotion, and the pipeline performs the deployment. Packaging precedes configuration, and configuration precedes promotion. Local study-map skill 3.4 (Solution Packaging for Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. There is nothing to export before the solution exists and holds the components. Why the correct answer wins: The solution is packaged and configured before promotion, and the pipeline performs the deployment.
- **B:** Incorrect for this question. Adding to a solution requires the solution, and the pipeline runs after the export. Why the correct answer wins: The solution is packaged and configured before promotion, and the pipeline performs the deployment.
- **C:** Correct. Packaging precedes configuration, and configuration precedes promotion. In this case: The solution is packaged and configured before promotion, and the pipeline performs the deployment.
- **D:** Incorrect for this question. Configuration applies to components that must already be in a solution. Why the correct answer wins: The solution is packaged and configured before promotion, and the pipeline performs the deployment.

### Question 74 — D

Answer: Store the secret in a vault and reference it from the environment variable. A vault-backed environment variable keeps the secret out of the export. A vault-backed variable keeps the value out of the solution export and the design surface. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the export.
- **B:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the export.
- **C:** Incorrect for this question. Current and default values cover the common two-environment split and are set explicitly per stage. Why the correct answer wins: A vault-backed environment variable keeps the secret out of the export.
- **D:** Correct. A vault-backed variable keeps the value out of the solution export and the design surface. In this case: A vault-backed environment variable keeps the secret out of the export.

### Question 75 — B

Answer: Define an environment variable for the endpoint and set a value per environment. An environment variable supplies the endpoint for each environment. Environment variables are how one solution behaves differently per environment without code changes. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: An environment variable supplies the endpoint for each environment.
- **B:** Correct. Environment variables are how one solution behaves differently per environment without code changes. In this case: An environment variable supplies the endpoint for each environment.
- **C:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: An environment variable supplies the endpoint for each environment.
- **D:** Incorrect for this question. Setting values during deployment removes the manual edit that people forget before a release. Why the correct answer wins: An environment variable supplies the endpoint for each environment.

### Question 76 — A, D

Answers: Use the current value in production and a default value for development; Set the environment variable values as part of the pipeline deployment step. A current value with a default covers the split, and deployment sets the stage value. Current and default values cover the common two-environment split and are set explicitly per stage. Setting values during deployment removes the manual edit that people forget before a release. Local study-map skill 3.5 (Environment Variables and Configuration), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Current and default values cover the common two-environment split and are set explicitly per stage. In this case: A current value with a default covers the split, and deployment sets the stage value.
- **B:** Incorrect for this question. Hard-coding guarantees a wrong endpoint in at least one environment and hides the value from review. Why the correct answer wins: A current value with a default covers the split, and deployment sets the stage value.
- **C:** Incorrect for this question. A vault-backed variable keeps the value out of the solution export and the design surface. Why the correct answer wins: A current value with a default covers the split, and deployment sets the stage value.
- **D:** Correct. Setting values during deployment removes the manual edit that people forget before a release. In this case: A current value with a default covers the split, and deployment sets the stage value.
- **E:** Incorrect for this question. Documentation helps a human but does not stop a deployment with a missing value. Why the correct answer wins: A current value with a default covers the split, and deployment sets the stage value.

### Question 77 — D

Answer: Add a pre-deployment step that runs the agent test set and blocks on failure. A pre-deployment test step blocks release when the set fails. Testing before promotion is what turns a pipeline into a gate rather than a courier. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: A pre-deployment test step blocks release when the set fails.
- **B:** Incorrect for this question. Manual imports skip validation and leave no reliable record of what was deployed when. Why the correct answer wins: A pre-deployment test step blocks release when the set fails.
- **C:** Incorrect for this question. Stage-level results shorten the loop between a failed run and the person who can fix it. Why the correct answer wins: A pre-deployment test step blocks release when the set fails.
- **D:** Correct. Testing before promotion is what turns a pipeline into a gate rather than a courier. In this case: A pre-deployment test step blocks release when the set fails.

### Question 78 — C

Answer: Import the solution by hand into production for each release. Staged pipelines record the version and approvals of each promotion. Manual imports skip validation and leave no reliable record of what was deployed when. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. An approval records who accepted the risk of the release. It must be a person who can read the test results. Why the correct answer wins: Staged pipelines record the version and approvals of each promotion.
- **B:** Incorrect for this question. A staged pipeline makes promotion a recorded operation instead of a manual import. Why the correct answer wins: Staged pipelines record the version and approvals of each promotion.
- **C:** Correct. Manual imports skip validation and leave no reliable record of what was deployed when. In this case: Staged pipelines record the version and approvals of each promotion.
- **D:** Incorrect for this question. Testing before promotion is what turns a pipeline into a gate rather than a courier. Why the correct answer wins: Staged pipelines record the version and approvals of each promotion.

### Question 79 — C

Answer: Create the solution in development → set environment variables for each stage → configure the pipeline stages → add the pre-deployment test step → run the deployment with approval. Solution, configuration, stages, test step, then approved deployment. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A pipeline with no solution and unset variables deploys nothing useful. Why the correct answer wins: Solution, configuration, stages, test step, then approved deployment.
- **B:** Incorrect for this question. The test step runs against a solution that must exist and be configured first. Why the correct answer wins: Solution, configuration, stages, test step, then approved deployment.
- **C:** Correct. Packaging and configuration come before the pipeline, and the gate runs inside the deployment. In this case: Solution, configuration, stages, test step, then approved deployment.
- **D:** Incorrect for this question. A deployment cannot run before there is a pipeline and something to deploy. Why the correct answer wins: Solution, configuration, stages, test step, then approved deployment.

### Question 80 — A, E

Answers: Keep the previous managed solution version so you can roll back; Notify the owning team with the deployment result and the failed step. Keeping the previous version enables rollback, and a notification names the failed stage. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Local study-map skill 3.6 (Power Platform Pipelines), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. In this case: Keeping the previous version enables rollback, and a notification names the failed stage.
- **B:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Keeping the previous version enables rollback, and a notification names the failed stage.
- **C:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: Keeping the previous version enables rollback, and a notification names the failed stage.
- **D:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Keeping the previous version enables rollback, and a notification names the failed stage.
- **E:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: Keeping the previous version enables rollback, and a notification names the failed stage.

### Question 81 — D

Answer: Add a custom pipeline step that calls the validation job. A custom pipeline step can run the scan and return a failing status. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: A custom pipeline step can run the scan and return a failing status.
- **B:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: A custom pipeline step can run the scan and return a failing status.
- **C:** Incorrect for this question. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Why the correct answer wins: A custom pipeline step can run the scan and return a failing status.
- **D:** Correct. Extensions let a pipeline run your own gate. The step must return a failure status the pipeline understands. In this case: A custom pipeline step can run the scan and return a failing status.

### Question 82 — D

Answer: Pass environment-specific values through pipeline configuration rather than editing the solution. Per-stage configuration removes the need for separate builds. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Per-stage configuration removes the need for separate builds.
- **B:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Per-stage configuration removes the need for separate builds.
- **C:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Per-stage configuration removes the need for separate builds.
- **D:** Correct. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. In this case: Per-stage configuration removes the need for separate builds.

### Question 83 — D

Answer: Capture user feedback in the conversation and route negative cases to review. In-conversation feedback records the complaint with the transcript. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: In-conversation feedback records the complaint with the transcript.
- **B:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: In-conversation feedback records the complaint with the transcript.
- **C:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: In-conversation feedback records the complaint with the transcript.
- **D:** Correct. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. In this case: In-conversation feedback records the complaint with the transcript.

### Question 84 — C

Answer: Sample production conversations and score them against the rubric on a schedule. Scheduled sampling and rubric scoring measure quality over time. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: Scheduled sampling and rubric scoring measure quality over time.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: Scheduled sampling and rubric scoring measure quality over time.
- **C:** Correct. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. In this case: Scheduled sampling and rubric scoring measure quality over time.
- **D:** Incorrect for this question. Fallback and handoff rates move before anyone files a ticket. A trend alert buys time. Why the correct answer wins: Scheduled sampling and rubric scoring measure quality over time.

### Question 85 — C, E

Answers: Publish to Microsoft Teams and keep the agent inside the tenant; Publish to a public website with authenticated sign-in. Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. Local study-map skill 1.3 (Channels, Deployment, and Audience Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Omni-channel routing suits a contact centre with human handoff. It is heavier than a website embed for a simple internal agent. Why the correct answer wins: Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in.
- **B:** Incorrect for this question. Email suits low-urgency requests and long answers. It cannot support a multi-step authenticated transaction well. Why the correct answer wins: Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in.
- **C:** Correct. The website channel suits external audiences when identity is still required. Anonymous public use needs a different risk decision. In this case: Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in.
- **D:** Incorrect for this question. Direct Line gives full control of the host application and its authentication. The team must build the client and its sign-in. Why the correct answer wins: Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in.
- **E:** Correct. Teams is the default internal channel and inherits tenant sign-in. It is a poor fit when the audience has no Teams account. In this case: Teams covers staff inside the tenant, and the website covers external visitors with their own sign-in.

### Question 86 — C

Answer: Configure the topic as a redirect target with its own trigger phrases. A redirect topic with its own triggers keeps ownership separate inside one agent. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. Local study-map skill 1.9 (Topics, Response Formatting, and Variables), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Global variables persist across topics and are right for things like the selected account. They are wrong for a value that should die with the topic. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate inside one agent.
- **B:** Incorrect for this question. Topic-scoped values reset when the topic ends, and explicit resets stop a stale value from an earlier turn. Leaking variables are a common source of wrong confirmations. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate inside one agent.
- **C:** Correct. Redirect topics keep the conversation in one agent while separating the flows. Trigger phrases decide when the redirect is offered. In this case: A redirect topic with its own triggers keeps ownership separate inside one agent.
- **D:** Incorrect for this question. A message node can send structured text without a card. It is the lightest way to make a list readable. Why the correct answer wins: A redirect topic with its own triggers keeps ownership separate inside one agent.

### Question 87 — A

Answer: Model the measures in the semantic model → create the Fabric data agent over it → grant the data agent read access → connect it to Copilot Studio → test the questions it must refuse. Measures, agent creation, permissions, connection, then boundary testing. Measures precede the agent, permissions precede connection, and boundary testing comes last. Local study-map skill 2.9 (Fabric Data Agents), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Measures precede the agent, permissions precede connection, and boundary testing comes last. In this case: Measures, agent creation, permissions, connection, then boundary testing.
- **B:** Incorrect for this question. Connection without permissions produces an agent that cannot read its own model. Why the correct answer wins: Measures, agent creation, permissions, connection, then boundary testing.
- **C:** Incorrect for this question. Access is granted to an agent that must already exist over a modelled source. Why the correct answer wins: Measures, agent creation, permissions, connection, then boundary testing.
- **D:** Incorrect for this question. Nothing can be tested before the agent exists and is connected. Why the correct answer wins: Measures, agent creation, permissions, connection, then boundary testing.

### Question 88 — B

Answer: Deploy the chosen model and reference the deployment from the custom prompt. The chosen model must be deployed and referenced by name from the prompt. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. Local study-map skill 2.11 (Foundry Model Catalog and Custom Prompts), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. A default is a starting point, not a decision about quality or cost. Why the correct answer wins: The chosen model must be deployed and referenced by name from the prompt.
- **B:** Correct. A deployment is the addressable unit the agent calls. Referencing it by name makes the choice visible and changeable. In this case: The chosen model must be deployed and referenced by name from the prompt.
- **C:** Incorrect for this question. Residency is a legal constraint, so region choice precedes price comparison. Why the correct answer wins: The chosen model must be deployed and referenced by name from the prompt.
- **D:** Incorrect for this question. Quota exhaustion shows up as throttling at the worst moment. Capacity has to be planned against the peak, not the average. Why the correct answer wins: The chosen model must be deployed and referenced by name from the prompt.

### Question 89 — D

Answer: Send an approval request and pause the flow until a person responds. An approval pauses the flow until a person decides, then resumes with that outcome. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. Local study-map skill 1.7 (Human-in-the-Loop Agent Flows), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Notifying after the fact is notification, not human-in-the-loop, and it cannot prevent a wrong action. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes with that outcome.
- **B:** Incorrect for this question. Drafting keeps the irreversible step with the human in the system that owns it. It is slower but leaves an auditable trail. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes with that outcome.
- **C:** Incorrect for this question. A timeout keeps a request from stalling indefinitely. The fallback owner must be defined before the flow goes live. Why the correct answer wins: An approval pauses the flow until a person decides, then resumes with that outcome.
- **D:** Correct. Approvals stop the automation at the decision point and record who approved. The flow resumes with that outcome. In this case: An approval pauses the flow until a person decides, then resumes with that outcome.

### Question 90 — D

Answer: Mediate the on-premises call through an on-premises data gateway. An on-premises data gateway brokers the call without opening an inbound path. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. Local study-map skill 1.1 (Enterprise Integration and Solution Planning), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Direct HTTP calls are simple but usually fail in a locked-down network and bypass the connector governance the platform already provides. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **B:** Incorrect for this question. Batching suits bulk work, not a conversation that expects an answer in seconds. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **C:** Incorrect for this question. A virtual table projects an external system as Dataverse-shaped data. It keeps one access path but depends on the source supporting the queries. Why the correct answer wins: An on-premises data gateway brokers the call without opening an inbound path.
- **D:** Correct. A gateway lets a cloud agent reach an on-premises system without opening an inbound firewall path. It adds a component to install, patch, and monitor. In this case: An on-premises data gateway brokers the call without opening an inbound path.

### Question 91 — B, E

Answers: Pass environment-specific values through pipeline configuration rather than editing the solution; Keep the previous managed solution version so you can roll back. Configuration belongs with the stage, and keeping the previous version enables rollback. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. Local study-map skill 3.7 (Extending Pipelines and Deployment Controls), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A notification with the failing step is what lets the team respond in minutes rather than at the next standup. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version enables rollback.
- **B:** Correct. A rollback plan is what makes a release reversible. Keeping the previous version is the cheapest version of that plan. In this case: Configuration belongs with the stage, and keeping the previous version enables rollback.
- **C:** Incorrect for this question. Scoped deployment shortens the window and reduces the blast radius of a bad release. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version enables rollback.
- **D:** Incorrect for this question. A schedule deploys whatever is in the source stage, including unfinished work. Why the correct answer wins: Configuration belongs with the stage, and keeping the previous version enables rollback.
- **E:** Correct. Configuration belongs with the stage, not in the artefact, or every environment needs its own build. In this case: Configuration belongs with the stage, and keeping the previous version enables rollback.

### Question 92 — D

Answer: Point the generative answers node at the specific knowledge source for the question. Scope the generative answers node to the knowledge source that matches the question. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. Local study-map skill 1.10 (Custom Prompts, Adaptive Cards, and Generative Answers), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Refusal on empty retrieval is what keeps a grounded agent from improvising. Citations make the remaining answers reviewable. Why the correct answer wins: Scope the generative answers node to the knowledge source that matches the question.
- **B:** Incorrect for this question. A fallback path protects the user from a confident wrong answer. It should be measured, not treated as failure. Why the correct answer wins: Scope the generative answers node to the knowledge source that matches the question.
- **C:** Incorrect for this question. Instructions in a custom prompt shape format and citation habits. They complement grounding but cannot substitute for it. Why the correct answer wins: Scope the generative answers node to the knowledge source that matches the question.
- **D:** Correct. Scoping the node to one source keeps answers on topic and makes the citation checkable. Broad scope invites answers from unrelated content. In this case: Scope the generative answers node to the knowledge source that matches the question.

### Question 93 — B

Answer: Define the response schema so the agent can reason over the returned fields. A declared response schema lets the agent use named fields and degrade gracefully on unexpected ones. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. Local study-map skill 2.5 (Custom Connectors and REST APIs), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Send HTTP request is quick for one endpoint inside one topic. It hides the integration from other agents and carries its own auth handling. Why the correct answer wins: A declared response schema lets the agent use named fields and degrade gracefully on unexpected ones.
- **B:** Correct. A declared schema is what lets the model use individual fields instead of pasting raw JSON into the answer. In this case: A declared response schema lets the agent use named fields and degrade gracefully on unexpected ones.
- **C:** Incorrect for this question. A flow adds retry, transformation, and error branches around the API call. It is the right shape when the response needs shaping. Why the correct answer wins: A declared response schema lets the agent use named fields and degrade gracefully on unexpected ones.
- **D:** Incorrect for this question. Credentials in a topic are visible to every maker in the environment and cannot be rotated safely. Why the correct answer wins: A declared response schema lets the agent use named fields and degrade gracefully on unexpected ones.

### Question 94 — D

Answer: Version the test set and rerun it for every change. A versioned set makes each model comparison comparable. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. Local study-map skill 3.1 (Test Set Design), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Happy-path-only testing passes almost any agent and predicts almost nothing about production. Why the correct answer wins: A versioned set makes each model comparison comparable.
- **B:** Incorrect for this question. Synthetic cases cover breadth quickly and can be generated in volume. They tend to be cleaner than real user language. Why the correct answer wins: A versioned set makes each model comparison comparable.
- **C:** Incorrect for this question. Tuning against every case overfits the prompt to the test. A held-out slice is the only honest measure left. Why the correct answer wins: A versioned set makes each model comparison comparable.
- **D:** Correct. A versioned set makes comparisons meaningful across releases. It also stops silent edits from hiding a regression. In this case: A versioned set makes each model comparison comparable.

### Question 95 — D

Answer: Turn on audit logging and retain agent conversation records. Audit logging with retention records the access and the answer for later review. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. Local study-map skill 1.4 (Responsible AI, Security, and Governance), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Incorrect for this question. Environment separation and security groups limit who can build against production data. They are the base control for any governed rollout. Why the correct answer wins: Audit logging with retention records the access and the answer for later review.
- **B:** Incorrect for this question. Data loss prevention decides which connectors a maker may use and where data may flow. It is the control that stops an agent leaking content to a personal service. Why the correct answer wins: Audit logging with retention records the access and the answer for later review.
- **C:** Incorrect for this question. Security roles decide who may create agents and who may publish them. Publishing rights deserve the narrower group. Why the correct answer wins: Audit logging with retention records the access and the answer for later review.
- **D:** Correct. Audit records show who changed what and what the agent answered. Retention has to match the organisations data policy, not default forever. In this case: Audit logging with retention records the access and the answer for later review.

### Question 96 — A

Answer: Connect to the search service over a private endpoint with managed identity. A private endpoint with managed identity keeps search traffic private. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. Local study-map skill 2.2 (Azure AI Search Grounding), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Correct. Private networking and managed identity keep the traffic off the public internet and remove stored keys. Both must be planned before go-live. In this case: A private endpoint with managed identity keeps search traffic private.
- **B:** Incorrect for this question. Rebuilding on publish is slow, expensive, and briefly serves an empty index to real users. Why the correct answer wins: A private endpoint with managed identity keeps search traffic private.
- **C:** Incorrect for this question. Hybrid retrieval catches exact identifiers that embeddings miss and paraphrases that keywords miss. It is usually worth the extra query cost. Why the correct answer wins: A private endpoint with managed identity keeps search traffic private.
- **D:** Incorrect for this question. The index schema decides what can be filtered, ranked, and returned. Getting it wrong is expensive to change later. Why the correct answer wins: A private endpoint with managed identity keeps search traffic private.

### Question 97 — B

Answer: Assign each failure cluster to the owner of the topic, prompt, or connector. Assign each cluster to the owner of the topic, prompt, or connector. Ownership converts findings into changes. An unowned backlog does not improve the agent. Local study-map skill 3.3 (Reviewing and Acting on Results), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Clustering turns a list of symptoms into a short list of causes, which is what makes a fix affordable. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **B:** Correct. Ownership converts findings into changes. An unowned backlog does not improve the agent. In this case: Assign each cluster to the owner of the topic, prompt, or connector.
- **C:** Incorrect for this question. A fixed failure becomes a permanent test. Removing it invites the same defect back. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.
- **D:** Incorrect for this question. An average hides the cases that matter most, and it moves when the mix of cases changes. Why the correct answer wins: Assign each cluster to the owner of the topic, prompt, or connector.

### Question 98 — D, E

Answers: Connect the source through a Copilot connector so its content is indexed for answers; Connect through a Power Platform connector and query it from a tool or flow. A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. Local study-map skill 2.1 (Copilot Connectors and Power Platform Connectors), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Copilot Studio tools, MCP, and multi-agent documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced/

- **A:** Incorrect for this question. Direct database knowledge answers structured questions but exposes schema choices and needs careful scoping. Why the correct answer wins: A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call.
- **B:** Incorrect for this question. AI Search gives control over chunking, vector profiles, filtering, and ranking. It is the heaviest option and the most controllable. Why the correct answer wins: A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call.
- **C:** Incorrect for this question. File knowledge is quick for a small, static set. It has size limits and no permission model beyond the agent itself. Why the correct answer wins: A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call.
- **D:** Correct. A Copilot connector brings external content into the Microsoft Graph index and honours its permissions. It is the right route for document-shaped knowledge. In this case: A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call.
- **E:** Correct. A Power Platform connector exposes operations rather than indexed content, so the agent asks a question of the system instead of searching text. In this case: A Copilot connector indexes document content with permissions, and a Power Platform connector supplies the operational data call.

### Question 99 — A

Answer: Extract the shared logic into a reusable component or child agent and reference it. A shared component gives one place to change the dialogue across all three agents. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. Local study-map skill 1.5 (Reusable Agent Components and Solutions), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Microsoft Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/

- **A:** Correct. One shared component means one place to fix a bug or tighten a prompt. The trade-off is a dependency that must be versioned and deployed. In this case: A shared component gives one place to change the dialogue across all three agents.
- **B:** Incorrect for this question. A custom connector gives every agent the same typed interface to one system. Authentication and throttling are configured once. Why the correct answer wins: A shared component gives one place to change the dialogue across all three agents.
- **C:** Incorrect for this question. Copies diverge quickly, and a fix has to be repeated in every agent that holds one. Why the correct answer wins: A shared component gives one place to change the dialogue across all three agents.
- **D:** Incorrect for this question. Avoiding the dependency duplicates the maintenance and the risk of inconsistent answers. Why the correct answer wins: A shared component gives one place to change the dialogue across all three agents.

### Question 100 — D

Answer: Capture user feedback in the conversation and route negative cases to review. In-conversation feedback captures the rating alongside the conversation. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. Local study-map skill 3.8 (Production Quality Monitoring and Continuous Evaluation), mapped to the official guide: Microsoft AB-620 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform ALM and pipeline documentation: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Scheduled scoring catches the drift that a launch test cannot see. It depends on privacy-safe sampling. Why the correct answer wins: In-conversation feedback captures the rating alongside the conversation.
- **B:** Incorrect for this question. Behaviour drifts with knowledge, models, and user questions, so a single launch test dates quickly. Why the correct answer wins: In-conversation feedback captures the rating alongside the conversation.
- **C:** Incorrect for this question. Operational metrics show whether the agent is helping. They are the business case for the next release. Why the correct answer wins: In-conversation feedback captures the rating alongside the conversation.
- **D:** Correct. Thumbs-down is a cheap signal that something is wrong, and the transcript says what. In this case: In-conversation feedback captures the rating alongside the conversation.
