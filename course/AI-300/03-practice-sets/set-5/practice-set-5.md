# Microsoft AI-300 — Full-Length Mock Exam 5

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A model retrained last month resolves different library versions than the original run. What should be pinned?

Domain: Design and implement an MLOps infrastructure

- A. Reference the floating latest tag for the environment image
- B. Print the metrics to the job log and read them from the console
- C. Disable request logging to reduce storage cost
- D. Build a versioned curated environment for the job

### 2. Four brands each maintain a copy of the same captioning preprocessor. What should be created?

Domain: Design and implement an MLOps infrastructure

- A. Package the preparation step as a reusable component
- B. Run the job from a compute instance notebook
- C. Run the whole workflow as a single script job
- D. Create the workspace in the portal and record the steps in a wiki

### 3. A new brand must receive an identical workspace under change control. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Create the workspace in the portal and record the steps in a wiki
- C. Export an ARM template from the portal after building it by hand
- D. Define the workspace in a Bicep module deployed per environment

### 4. A resource added by hand outside the template was never removed and cost grew silently. What should be deployed as?

Domain: Design and implement an MLOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Keep public network access enabled so notebooks connect easily
- C. Deploy the module as a deployment stack so removed resources are cleaned up
- D. Create the workspace in the portal and record the steps in a wiki

### 5. A scheduled retraining job must run identically from a laptop and from a pipeline. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Stream the job with az ml job stream to inspect logs
- B. Run the job from a compute instance notebook
- C. Submit the job with az ml job create --file job.yaml
- D. Create the workspace in the portal and record the steps in a wiki

### 6. The group forbids long-lived credentials in any repository. What should authenticate deployments?

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Authenticate the workflow with workload identity federation and no stored secret
- C. Store a service principal client secret as a GitHub repository secret
- D. Set the connection string as a plain environment variable in the job

### 7. A brand manager must approve any release that changes a customer-facing generator. What should be configured?

Domain: Design and implement an MLOps infrastructure

- A. Use GitHub environment protection rules to gate the production deploy job
- B. Fan the tests out across a matrix of dependency versions
- C. Run the pipeline from a GitHub Actions workflow on merge to main
- D. Store a service principal client secret as a GitHub repository secret

### 8. An advertising claim must be traceable to the exact generator version that produced the copy. What pins it?

Domain: Design and implement an MLOps infrastructure

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Register the model and always deploy whichever version is latest
- C. Register each candidate with a version and deploy one explicit version
- D. Overwrite the existing model version instead of registering a new one

### 9. Unreleased campaign material may not leave the private network. What must the workspace use?

Domain: Design and implement an MLOps infrastructure

- A. Place a private endpoint on the workspace and its storage
- B. Set the connection string as a plain environment variable in the job
- C. Reference the storage path with the account key inline in the job YAML
- D. Keep public network access enabled so notebooks connect easily

### 10. A connection string must rotate without redeploying the job definition. Where should it live?

Domain: Design and implement an MLOps infrastructure

- A. Reference the storage path with the account key inline in the job YAML
- B. Set the connection string as a plain environment variable in the job
- C. Store connection strings in Key Vault and reference them by name
- D. Print the metrics to the job log and read them from the console

### 11. One module must deploy to six brands with different names and capacity. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Export an ARM template from the portal after building it by hand
- C. Define the workspace in a Bicep module deployed per environment
- D. Pass environment values through a Bicep parameter file per stage
- E. Rebuild the environment by hand from the notes in the ticket

### 12. A release must be secret-free and gated. Which two controls apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Use GitHub environment protection rules to gate the production deploy job
- B. Authenticate the workflow with workload identity federation and no stored secret
- C. Store a service principal client secret as a GitHub repository secret
- D. Fan the tests out across a matrix of dependency versions
- E. Grant the pipeline service principal Owner on the subscription

### 13. A group is provisioning a new brand workspace from code. Which sequence is correct?

Domain: Design and implement an MLOps infrastructure

- A. Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace
- B. Run a smoke job against the workspace → deploy the module → authenticate the pipeline → define the workspace in Bicep
- C. Authenticate the pipeline → run a smoke job → define the workspace in Bicep → deploy the module
- D. Deploy the module → define the workspace in Bicep → run a smoke job → authenticate the pipeline

### 14. An editor asks which training data produced the captioning model that wrote a headline. What provides the record?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Define the steps as a pipeline job with explicit inputs and outputs
- C. Run the job from a compute instance notebook
- D. Run the whole workflow as a single script job

### 15. A tabular propensity model needs a credible baseline within a week. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Run the whole workflow as a single script job
- B. Run a sweep job over a searched hyperparameter space
- C. Run the job from a compute instance notebook
- D. Use automated ML to establish the tabular baseline

### 16. Two captioning models scored the same BLEU and the team cannot tell which preprocessing each used. What should be tracked?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Disable request logging to reduce storage cost
- C. Assign the work to a person instead of investigating the failure
- D. Enable MLflow tracking so runs log to the workspace

### 17. Six hundred runs share one list and three variants cannot be compared. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Group the trials under a named experiment
- B. Enable MLflow tracking so runs log to the workspace
- C. Disable request logging to reduce storage cost
- D. Print the metrics to the job log and read them from the console

### 18. An editor must judge whether a generator is suitable before it goes live. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Attach a description, metrics, and intended use to the model version
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Register the model and always deploy whichever version is latest

### 19. Brand counsel must rebuild the generator that produced last year's campaign copy. What must registration record?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Overwrite the existing model version instead of registering a new one
- C. Tag the registered model with the data asset and commit it came from
- D. Attach a description, metrics, and intended use to the model version

### 20. A publishing tool needs a synchronous response for a single request. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Deploy a batch endpoint for the overnight scoring job
- C. Run the job from a compute instance notebook
- D. Deploy to a managed online endpoint with an explicit model version

### 21. A generator container errors for ninety seconds after start while weights load. What should be added?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy without probes and rely on the platform health check
- B. Pin a fixed instance count for a spiky workload
- C. Configure liveness and readiness probes on the deployment
- D. Monitor only the accuracy reported at deployment time

### 22. Each candidate currently needs a new container image before testing can start. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Mount the model artifact rather than baking it into the image
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one

### 23. A new generator may affect at most five percent of published descriptions initially. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Split endpoint traffic 10/90 so the new deployment receives a canary share
- B. Replace the production deployment in a single step
- C. Keep the previous deployment in place so traffic can be moved back
- D. Deploy straight to production to save a day

### 24. A generator must be withdrawable within minutes if it produces off-brand copy. What enables that?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Replace the production deployment in a single step
- C. Overwrite the existing model version instead of registering a new one
- D. Keep the previous deployment in place so traffic can be moved back

### 25. A new product range changed the vocabulary and nobody knows whether the model still fits. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Enable data drift monitoring against the training baseline
- D. Retrain the model on the newer data

### 26. A monthly drift report is filed and read only after an incident. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Create an alert rule on the drift and latency metrics
- C. Disable request logging to reduce storage cost
- D. Monitor only the accuracy reported at deployment time

### 27. An editorial audit needs comparable runs and a pinned artifact. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Register each candidate with a version and deploy one explicit version
- B. Enable MLflow tracking so runs log to the workspace
- C. Print the metrics to the job log and read them from the console
- D. Register the model and always deploy whichever version is latest
- E. Disable request logging to reduce storage cost

### 28. A launch must be bounded and reversible. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Replace the production deployment in a single step
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Keep the previous deployment in place so traffic can be moved back
- D. Overwrite the existing model version instead of registering a new one
- E. Bake the model weights into the container image

### 29. A captioning candidate must reach production behind a gate. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Evaluate against the gate → train the candidate → shift all traffic → register the model version
- B. Register the model version → train the candidate → evaluate against the gate → shift all traffic
- C. Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold
- D. Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate

### 30. Six brands need shared capacity but separate assets. What should be created?

Domain: Design and implement a GenAIOps infrastructure

- A. Give every team one project and one shared connection
- B. Create a Foundry hub and a project per team
- C. Use one workspace for development, test, and production
- D. Create the workspace in the portal and record the steps in a wiki

### 31. A flow broke when the model behind its deployment was replaced. What should the flow reference instead?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Select a model from the catalog and deploy it into the project
- C. Reference the deployment name from the flow rather than the model family name
- D. Hardcode the model family name inside the flow

### 32. A content studio runs a steady assistant workload at predictable volume. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Use the largest model for every request
- B. Reserve provisioned throughput for the steady high-volume workload
- C. Pin a fixed instance count for a spiky workload
- D. Start on pay-as-you-go while the volume is still unknown

### 33. A pilot may end after a quarter with unknown volume. What fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Start on pay-as-you-go while the volume is still unknown
- B. Reserve provisioned throughput for the steady high-volume workload
- C. Use the largest model for every request
- D. Pin a fixed instance count for a spiky workload

### 34. A public-facing generator must enforce harm thresholds on prompts and completions. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Evaluate toxicity against the threshold the audience requires
- D. Apply a content filter policy appropriate to the audience

### 35. Two headline strategies must be compared on the same articles. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Create a variant to compare two prompt strategies side by side
- B. Hardcode the model family name inside the flow
- C. Rewrite the prompt and deploy it immediately
- D. Author the flow as a directed acyclic graph with typed inputs and outputs

### 36. A flow must reference its model endpoint without a credential in the file. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Store the model credential as a project connection
- B. Reference the storage path with the account key inline in the job YAML
- C. Set the connection string as a plain environment variable in the job
- D. Paste the API key into a Python node inside the flow

### 37. A working key was typed into a node and committed with the flow. What is the defect?

Domain: Design and implement a GenAIOps infrastructure

- A. Store the model credential as a project connection
- B. Store connection strings in Key Vault and reference them by name
- C. Paste the API key into a Python node inside the flow
- D. Set the connection string as a plain environment variable in the job

### 38. Retrieval cannot find campaign codes such as BR-2024-Q3. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Use vector search alone with no keyword component
- B. Increase the model size until the answers improve
- C. Use hybrid search with semantic ranking
- D. Fine-tune the model on the document set instead of retrieving

### 39. One index serves six brands and each team may see only its own material. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Set document-level access in the index so retrieval respects entitlements
- C. Index every document the organization holds
- D. Set the connection string as a plain environment variable in the job

### 40. Generated copy follows the right style guide but the wrong section. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Index each document as one large chunk
- B. Chunk documents by section with a small overlap
- C. Raise retrieval depth to the maximum for safety
- D. Index every document the organization holds

### 41. Retrieval returns an entire brand book and the model quotes an unrelated page. What caused it?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Index every document the organization holds
- D. Index each document as one large chunk

### 42. Editors require every tone change to be reviewable and revertible. Where should prompts live?

Domain: Design and implement a GenAIOps infrastructure

- A. Keep the prompt in its own file under version control
- B. Create a variant to compare two prompt strategies side by side
- C. Rewrite the prompt and deploy it immediately
- D. Paste the API key into a Python node inside the flow

### 43. A tone edit reached live copy and lowered quality for three days. What was missing?

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Assign the work to a person instead of investigating the failure
- D. Deploy straight to production to save a day

### 44. A publishing agent can reach a scheduling tool that is out of scope. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Increase the model size until the answers improve
- B. Index every document the organization holds
- C. Register a scoped tool list for the agent
- D. Expose every available tool so the agent can choose freely

### 45. A conversation carried one client's embargoed details into another client's session. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Pass typed state between agent steps
- B. Index every document the organization holds
- C. Bound the agent memory to the current session
- D. Expose every available tool so the agent can choose freely

### 46. A brand assistant must ground on current material and respect team boundaries. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Fine-tune the model on the document set instead of retrieving
- C. Index the documents in Azure AI Search and query the index from the flow
- D. Index every document the organization holds
- E. Set document-level access in the index so retrieval respects entitlements

### 47. A tone change needs a record and a quality gate. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Run the evaluation in continuous integration before the flow is promoted
- B. Assign the work to a person instead of investigating the failure
- C. Rewrite the prompt and deploy it immediately
- D. Deploy straight to production to save a day
- E. Keep the prompt in its own file under version control

### 48. A studio must isolate brand assets and keep flows stable across model swaps. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Reference the deployment name from the flow rather than the model family name
- B. Give every team one project and one shared connection
- C. Paste the API key into a Python node inside the flow
- D. Hardcode the model family name inside the flow
- E. Create a Foundry hub and a project per team

### 49. A brand assistant must ground on current style and product material. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents
- B. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness
- C. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- D. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them

### 50. Two thousand headline variants must be graded each week. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Generate the evaluation set from the prompt itself
- C. Use an LLM judge with a rubric, calibrated against human grades
- D. Rely on the LLM judge without checking it against human grades

### 51. A thirty-case set moved from 0.71 to 0.77 and the team wants to declare a win. What is the objection?

Domain: Implement generative AI quality assurance and observability

- A. Use a few hundred representative cases rather than a dozen
- B. Assign the work to a person instead of investigating the failure
- C. Retrain the model on the newer data
- D. Generate the evaluation set from the prompt itself

### 52. Generated copy asserts a product claim that no retrieved specification supports. Which metric targets this?

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Score coherence for logical structure
- C. Score relevance of the answer to the question asked
- D. Score groundedness against the retrieved passages

### 53. An answer summarizes a specification for a different product. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Score similarity against a reference answer
- C. Score groundedness against the retrieved passages
- D. Score relevance of the answer to the question asked

### 54. Copy quality is poor and the team is about to rewrite the prompt. What should be measured first?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Rely on the LLM judge without checking it against human grades
- C. Increase the model size until the answers improve
- D. Measure retrieval recall before scoring answer quality

### 55. Copy contradicts a claim it made two paragraphs earlier. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score coherence for logical structure
- B. Score relevance of the answer to the question asked
- C. Score fluency for readability and language quality
- D. Score groundedness against the retrieved passages

### 56. A supplier brief contains text instructing the assistant to ignore its brand rules. What is the exposure?

Domain: Implement generative AI quality assurance and observability

- A. Test indirect injection through retrieved documents
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Evaluate toxicity against the threshold the audience requires
- D. Disable request logging to reduce storage cost

### 57. A public generator must not produce abusive copy for any input. What should be evaluated?

Domain: Implement generative AI quality assurance and observability

- A. Score similarity against a reference answer
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Evaluate toxicity against the threshold the audience requires
- D. Score fluency for readability and language quality

### 58. A fixed dataset passes every release while reader satisfaction falls. What should be added?

Domain: Implement generative AI quality assurance and observability

- A. Build the evaluation dataset from real queries with graded answers
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Run continuous evaluation on sampled production traffic

### 59. Published copy must be supported and on point. Which two metrics apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Score similarity against a reference answer
- C. Score relevance of the answer to the question asked
- D. Score groundedness against the retrieved passages
- E. Score coherence for logical structure

### 60. An assistant reads supplier documents and must resist override from users and documents. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Score fluency for readability and language quality
- C. Run adversarial jailbreak and prompt-injection cases before release
- D. Evaluate toxicity against the threshold the audience requires
- E. Test indirect injection through retrieved documents

### 61. A disputed publication must be diagnosable and reproducible. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Log prompts and completions against the trace, within data policy
- B. Disable request logging to reduce storage cost
- C. Enable distributed tracing and log the retrieval and model spans
- D. Assign the work to a person instead of investigating the failure
- E. Rely on the LLM judge without checking it against human grades

### 62. A published claim is challenged and the team must explain it. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set
- B. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- C. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set
- D. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set

### 63. The group CFO cannot attribute model spend to a brand. What must be measured first?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Use the largest model for every request
- C. Measure tokens per request and set a budget per endpoint
- D. Accept the behaviour because the aggregate score still looks healthy

### 64. A product feed repeats the same four hundred descriptions all day. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Compress the system prompt and remove redundant instructions
- B. Cache identical requests and reuse the completion
- C. Set a time-to-live on the cache
- D. Add a router that classifies the request and selects a model

### 65. A cached description still quotes a specification replaced last month. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Disable request logging to reduce storage cost
- D. Set a time-to-live on the cache

### 66. Most requests are short product summaries and every one calls the largest model. What should change?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Increase the model size until the answers improve
- C. Route simple requests to a smaller model
- D. Retrain the model on the newer data

### 67. One endpoint serves both short summaries and long creative briefs. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Route simple requests to a smaller model
- C. Cache identical requests and reuse the completion
- D. Use the largest model for every request

### 68. A stalled dependency causes retries to multiply load during a launch. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Set a request timeout with a bounded retry and backoff
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Stream the response so the first token arrives sooner

### 69. A stable tone-rewrite task carries a long instruction on every call. What can absorb it?

Domain: Optimize generative AI systems and model performance

- A. Fine-tune on approved examples to shorten the standing prompt
- B. Fine-tune the model on the document set instead of retrieving
- C. Increase the model size until the answers improve
- D. Compress the system prompt and remove redundant instructions

### 70. Overnight bulk description generation needs no interactive response. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Stream the response so the first token arrives sooner
- C. Set a request timeout with a bounded retry and backoff
- D. Move non-urgent generation into a batch run

### 71. A brand needs attributable spend and current copy. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Set a time-to-live on the cache
- B. Use the largest model for every request
- C. Measure tokens per request and set a budget per endpoint
- D. Accept the behaviour because the aggregate score still looks healthy
- E. Cache identical requests and reuse the completion

### 72. A mixed workload must cost less without losing quality on long briefs. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Retrain the model on the newer data
- B. Route simple requests to a smaller model
- C. Cache identical requests and reuse the completion
- D. Add a router that classifies the request and selects a model
- E. Use the largest model for every request

### 73. A group must cut model spend without losing editorial quality. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver
- B. Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held
- C. Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver
- D. Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization

### 74. A deployment failed because it was created before its endpoint existed. What is the correct order?

Domain: Design and implement an MLOps infrastructure

- A. Run the job from a compute instance notebook
- B. Replace the production deployment in a single step
- C. Submit the job with az ml job create --file job.yaml
- D. Create the endpoint first, then the deployment, with az ml online-endpoint and online-deployment

### 75. Captioning training runs twice weekly and accelerators bill overnight. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Attach a GPU cluster with a minimum of zero nodes
- B. Run the job from a compute instance notebook
- C. Attach a CPU compute cluster for the data preparation step
- D. Attach a GPU cluster with four always-on nodes

### 76. Runs are logged on the engineer laptop and never appear in the shared experiment list. What is misconfigured?

Domain: Implement machine learning model lifecycle and operations

- A. Point the MLflow tracking URI at the workspace endpoint
- B. Print the metrics to the job log and read them from the console
- C. Disable request logging to reduce storage cost
- D. Run the job from a compute instance notebook

### 77. An editor must judge suitability before a generator goes live. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Attach a description, metrics, and intended use to the model version
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Register the model and always deploy whichever version is latest

### 78. A drift report is filed monthly and consulted only after an incident. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Create an alert rule on the drift and latency metrics
- B. Disable request logging to reduce storage cost
- C. Monitor only the accuracy reported at deployment time
- D. Assign the work to a person instead of investigating the failure

### 79. Brand counsel needs provenance and documented intended use. Which two artifacts apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Register the model and always deploy whichever version is latest
- C. Overwrite the existing model version instead of registering a new one
- D. Tag the registered model with the data asset and commit it came from
- E. Attach a description, metrics, and intended use to the model version

### 80. A captioning endpoint must survive launches and not serve before the model loads. Which two configurations apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Set autoscale rules on the deployment with a deliberate minimum instance count
- C. Configure liveness and readiness probes on the deployment
- D. Pin a fixed instance count for a spiky workload
- E. Deploy without probes and rely on the platform health check

### 81. A generator release must stay reversible throughout rollout. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress
- B. Send all traffic to the new deployment → deploy the new version → compare metrics → move traffic back
- C. Replace the incumbent deployment → compare error rate and latency → deploy the new version to a second deployment → send traffic to it
- D. Compare error rate and latency → deploy the new version → send a small traffic share → replace the incumbent

### 82. Off-brand copy reaches customers and the team must respond. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Fix the identified cause → confirm the impact → contain the incident → add a regression case
- B. Contain the incident → add a regression case → fix the cause → confirm the impact
- C. Confirm the impact and scope from telemetry → contain the incident by shifting traffic or disabling the feature → fix the identified cause → add a regression case and update the gate
- D. Add a regression case → contain the incident → confirm the impact → fix the cause

### 83. A captioning model degraded after a product change. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Retrain on refreshed data → detect the drop → compare distributions → promote through the gate
- B. Identify the upstream source → retrain → detect the drop → compare distributions
- C. Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate
- D. Compare distributions → identify the upstream source → detect the drop → retrain on refreshed data

### 84. Brand counsel must rebuild the generator that produced last year campaign copy. What must registration record?

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Tag the registered model with the data asset and commit it came from
- C. Attach a description, metrics, and intended use to the model version
- D. Print the metrics to the job log and read them from the console

### 85. Generated copy follows the right style guide but cites the wrong section. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Chunk documents by section with a small overlap
- C. Index each document as one large chunk
- D. Raise retrieval depth to the maximum for safety

### 86. Retrieval returns a whole brand book and the model quotes an unrelated page. What caused it?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk documents by section with a small overlap
- B. Index each document as one large chunk
- C. Retrain the model on the newer data
- D. Index every document the organization holds

### 87. A metadata preparation step processes five gigabytes of CSV and needs no accelerator. What should it target?

Domain: Implement machine learning model lifecycle and operations

- A. Create the workspace in the portal and record the steps in a wiki
- B. Run the job from a compute instance notebook
- C. Attach a GPU cluster with a minimum of zero nodes
- D. Attach a CPU compute cluster for the data preparation step

### 88. A deployment was created before its endpoint existed and failed. What is the required order?

Domain: Design and implement an MLOps infrastructure

- A. Submit the job with az ml job create --file job.yaml
- B. Run the job from a compute instance notebook
- C. Create the endpoint first, then the deployment, with az ml online-endpoint and online-deployment
- D. Replace the production deployment in a single step

---

## Case study — Atlas Distribution

Atlas Distribution operates 40 warehouses and runs generative assistants for shift planning and supplier correspondence. Warehouse connectivity is unreliable, so perceived latency matters more than total response time, and supervisors often wait for the first visible token. The operations team wants a single decision framework for choosing between a fine-tuned model, a retrieved grounding approach, and a larger general model for each task. Spend is reviewed monthly by the CFO, who wants to know which workloads justify provisioned capacity and which should stay on pay-as-you-go.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. The CFO wants to know which workloads justify a commitment. Which workloads qualify?

Domain: Optimize generative AI systems and model performance

- A. Move steady traffic to provisioned throughput
- B. Cache identical requests and reuse the completion
- C. Increase the model size until the answers improve
- D. Start on pay-as-you-go while the volume is still unknown

### 90. Spend is reviewed monthly and must fall without quality loss. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Compress the system prompt and remove redundant instructions
- C. Use the largest model for every request
- D. Retrain the model on the newer data
- E. Cache identical requests and reuse the completion

### 91. Dispatchers wait for visible text on unreliable mobile links. What should be enabled?

Domain: Optimize generative AI systems and model performance

- A. Move non-urgent generation into a batch run
- B. Cache identical requests and reuse the completion
- C. Stream the response so the first token arrives sooner
- D. Set a request timeout with a bounded retry and backoff

---

## Case study — Brightwater Water

Brightwater Water operates a network-fault assistant for field crews and wants to reduce the cost of running it. The assistant sends a 6,000-token system prompt on every request, retrieves twelve passages per answer, and routes every question to the largest available model. Monthly spend is now four times the forecast, and the finance team wants a reduction within one quarter without a drop in answer quality. Crews have complained that the first token takes eight seconds on a slow connection, which matters more than total generation time in the field.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. An outage decision must be traceable to the exact model that made it. What pins it?

Domain: Design and implement an MLOps infrastructure

- A. Overwrite the existing model version instead of registering a new one
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Register the model and always deploy whichever version is latest
- D. Register each candidate with a version and deploy one explicit version

### 93. A million nightly meter readings must be scored without always-on capacity. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy to a managed online endpoint with an explicit model version
- B. Run the job from a compute instance notebook
- C. Send the overnight file through the online endpoint request by request
- D. Deploy a batch endpoint for the overnight scoring job

### 94. Customer-facing outage notices must be filtered for abusive language before release. What should be evaluated?

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Score similarity against a reference answer
- C. Score fluency for readability and language quality
- D. Evaluate toxicity against the threshold the audience requires

---

## Case study — Kestrel Group

Kestrel Group is consolidating four business units onto a single AI platform and has inherited four different practices. One unit deploys models from notebooks, one uses infrastructure as code with a manual approval gate, one has no experiment tracking, and one runs generative workloads with the API key in a flow repository. The group CIO wants a single standard for infrastructure, promotion, and evaluation, and has asked for a plan that shows where each unit is out of compliance. Group audit also wants a register of every deployed model and agent with its owner.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. The CIO wants one promotion mechanism across four units. What should deployments resolve?

Domain: Design and implement an MLOps infrastructure

- A. Overwrite the existing model version instead of registering a new one
- B. Promote versions through aliases such as candidate and production
- C. Register the model and always deploy whichever version is latest
- D. Register each candidate with a version and deploy one explicit version

### 96. One unit deploys from notebooks and another uses code. What should the standard be?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Define the workspace in a Bicep module deployed per environment
- C. Rebuild the environment by hand from the notes in the ticket
- D. Export an ARM template from the portal after building it by hand

### 97. One unit has no experiment tracking and cannot compare runs. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Enable MLflow tracking so runs log to the workspace
- B. Assign the work to a person instead of investigating the failure
- C. Group the trials under a named experiment
- D. Disable request logging to reduce storage cost
- E. Print the metrics to the job log and read them from the console

---

## Case study — Skyline Media

Skyline Media publishes a news archive of twenty years and wants a research assistant for its journalists. The archive sits in a third-party system, and the retrieval index is built from summaries rather than full text, so journalists report that quoted passages cannot be found. A standards editor requires that every published claim be traceable to a source document, and a recent incident involved an assistant inventing a plausible quotation. The publisher also wants to compare two retrieval configurations on the same set of historical queries before committing.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Archive footage is licensed and may not be copied into the index. How should the assistant ground on it?

Domain: Design and implement a GenAIOps infrastructure

- A. Export the corpus to storage and index it as files
- B. Build a knowledge-source connector that indexes the whole corpus into the project
- C. Index every document the organization holds
- D. Connect to the source through a federated connector and query it in place

### 99. A published caption is disputed and the team must find which stage failed. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Enable distributed tracing and log the retrieval and model spans
- B. Disable request logging to reduce storage cost
- C. Rely on the LLM judge without checking it against human grades
- D. Log prompts and completions against the trace, within data policy

### 100. A cheaper summarizer is proposed for clip descriptions and must not lower caption quality. What is required?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Re-run the evaluation after the cost optimization
- C. Retrain the model on the newer data
- D. Ship the optimization and watch the support queue

---

## Answer key and explanations

### Question 1 — D

Answer: Build a versioned curated environment for the job. A versioned curated environment fixes the package set. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment fixes the package set.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment fixes the package set.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned curated environment fixes the package set.
- **D:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment fixes the package set.

### Question 2 — A

Answer: Package the preparation step as a reusable component. A component gives the step one versioned implementation. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. In this case: A component gives the step one versioned implementation.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A component gives the step one versioned implementation.
- **C:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A component gives the step one versioned implementation.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A component gives the step one versioned implementation.

### Question 3 — D

Answer: Define the workspace in a Bicep module deployed per environment. A reviewed Bicep module recreates the environment identically. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **C:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **D:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A reviewed Bicep module recreates the environment identically.

### Question 4 — C

Answer: Deploy the module as a deployment stack so removed resources are cleaned up. A deployment stack removes or denies resources it does not own. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **C:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: A deployment stack removes or denies resources it does not own.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A deployment stack removes or denies resources it does not own.

### Question 5 — C

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI is repeatable. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI is repeatable.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI is repeatable.
- **C:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI is repeatable.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI is repeatable.

### Question 6 — B

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation removes the stored secret. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation removes the stored secret.
- **B:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation removes the stored secret.
- **C:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation removes the stored secret.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation removes the stored secret.

### Question 7 — A

Answer: Use GitHub environment protection rules to gate the production deploy job. A protected environment requires approval before the job runs. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: A protected environment requires approval before the job runs.
- **B:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: A protected environment requires approval before the job runs.
- **C:** Incorrect for this question. A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit. Why the correct answer wins: A protected environment requires approval before the job runs.
- **D:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: A protected environment requires approval before the job runs.

### Question 8 — C

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version identifies what was served. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit model version identifies what was served.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version identifies what was served.
- **C:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version identifies what was served.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version identifies what was served.

### Question 9 — A

Answer: Place a private endpoint on the workspace and its storage. A private endpoint keeps traffic on the virtual network. A private endpoint removes public network access, so traffic stays on the virtual network. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A private endpoint removes public network access, so traffic stays on the virtual network. In this case: A private endpoint keeps traffic on the virtual network.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **D:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.

### Question 10 — C

Answer: Store connection strings in Key Vault and reference them by name. Key Vault holds the secret and rotation happens outside the code. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.
- **C:** Correct. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. In this case: Key Vault holds the secret and rotation happens outside the code.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.

### Question 11 — C, D

Answers: Pass environment values through a Bicep parameter file per stage; Define the workspace in a Bicep module deployed per environment. The module defines the shape, and a parameter file per brand supplies values. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: The module defines the shape, and a parameter file per brand supplies values.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: The module defines the shape, and a parameter file per brand supplies values.
- **C:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: The module defines the shape, and a parameter file per brand supplies values.
- **D:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: The module defines the shape, and a parameter file per brand supplies values.
- **E:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: The module defines the shape, and a parameter file per brand supplies values.

### Question 12 — A, B

Answers: Authenticate the workflow with workload identity federation and no stored secret; Use GitHub environment protection rules to gate the production deploy job. Federated identity removes the secret, and a protected environment adds approval. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **B:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **C:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **D:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **E:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.

### Question 13 — A

Answer: Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace. Definition, pipeline identity, deployment, and a smoke job follow in that order. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. In this case: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **B:** Incorrect for this question. A job cannot run against infrastructure that has neither been defined nor deployed, and the pipeline has no identity yet. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **C:** Incorrect for this question. Identity is established early, but the smoke job still precedes both the definition and the deployment. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **D:** Incorrect for this question. The module is deployed before it is written, and authentication last means the pipeline could never have deployed anything. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.

### Question 14 — B

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline records each step input and output. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A pipeline records each step input and output.
- **B:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline records each step input and output.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A pipeline records each step input and output.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline records each step input and output.

### Question 15 — D

Answer: Use automated ML to establish the tabular baseline. Automated ML produces a baseline quickly. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML produces a baseline quickly.
- **B:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML produces a baseline quickly.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML produces a baseline quickly.
- **D:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML produces a baseline quickly.

### Question 16 — D

Answer: Enable MLflow tracking so runs log to the workspace. MLflow records parameters and artifacts per run. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **D:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: MLflow records parameters and artifacts per run.

### Question 17 — A

Answer: Group the trials under a named experiment. A named experiment groups runs so variants compare. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups runs so variants compare.
- **B:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups runs so variants compare.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups runs so variants compare.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A named experiment groups runs so variants compare.

### Question 18 — B

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports the judgement. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **B:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports the judgement.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports the judgement.

### Question 19 — C

Answer: Tag the registered model with the data asset and commit it came from. Tags carrying the data asset and commit make the rebuild possible. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **C:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carrying the data asset and commit make the rebuild possible.
- **D:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.

### Question 20 — D

Answer: Deploy to a managed online endpoint with an explicit model version. A managed online endpoint serves synchronous requests. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **B:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **D:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: A managed online endpoint serves synchronous requests.

### Question 21 — C

Answer: Configure liveness and readiness probes on the deployment. A readiness probe withholds traffic until the model can serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe withholds traffic until the model can serve.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.

### Question 22 — B

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact decouples the model version from the image. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **B:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact decouples the model version from the image.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact decouples the model version from the image.

### Question 23 — A

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split bounds exposure to a canary share. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split bounds exposure to a canary share.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **C:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split bounds exposure to a canary share.

### Question 24 — D

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes withdrawal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **D:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes withdrawal a traffic change.

### Question 25 — C

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 26 — B

Answer: Create an alert rule on the drift and latency metrics. An alert turns the metric into an action. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into an action.
- **B:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into an action.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert turns the metric into an action.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert turns the metric into an action.

### Question 27 — A, B

Answers: Enable MLflow tracking so runs log to the workspace; Register each candidate with a version and deploy one explicit version. MLflow tracks parameters and metrics, and the explicit version pins the artifact. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: MLflow tracks parameters and metrics, and the explicit version pins the artifact.
- **B:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: MLflow tracks parameters and metrics, and the explicit version pins the artifact.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: MLflow tracks parameters and metrics, and the explicit version pins the artifact.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: MLflow tracks parameters and metrics, and the explicit version pins the artifact.
- **E:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: MLflow tracks parameters and metrics, and the explicit version pins the artifact.

### Question 28 — B, C

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. A canary share bounds exposure, and a retained deployment enables reversal. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A canary share bounds exposure, and a retained deployment enables reversal.
- **C:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A canary share bounds exposure, and a retained deployment enables reversal.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.

### Question 29 — C

Answer: Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold. Each step consumes the artifact produced before it, ending with a measured canary. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **B:** Incorrect for this question. Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **C:** Correct. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. In this case: Each step consumes the artifact produced before it, ending with a measured canary.
- **D:** Incorrect for this question. A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.

### Question 30 — B

Answer: Create a Foundry hub and a project per team. A hub shares capacity while a project isolates assets. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **B:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity while a project isolates assets.
- **C:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity while a project isolates assets.

### Question 31 — C

Answer: Reference the deployment name from the flow rather than the model family name. A deployment name is the stable reference. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A deployment name is the stable reference.
- **B:** Incorrect for this question. The catalog lists models with their capabilities; deploying one into the project makes it addressable by a deployment name. Why the correct answer wins: A deployment name is the stable reference.
- **C:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A deployment name is the stable reference.
- **D:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A deployment name is the stable reference.

### Question 32 — B

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput gives predictable cost and latency. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.
- **B:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput gives predictable cost and latency.
- **C:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.
- **D:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.

### Question 33 — A

Answer: Start on pay-as-you-go while the volume is still unknown. Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. In this case: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **B:** Incorrect for this question. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.

### Question 34 — D

Answer: Apply a content filter policy appropriate to the audience. A content filter policy applies those thresholds. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: A content filter policy applies those thresholds.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A content filter policy applies those thresholds.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: A content filter policy applies those thresholds.
- **D:** Correct. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. In this case: A content filter policy applies those thresholds.

### Question 35 — A

Answer: Create a variant to compare two prompt strategies side by side. Variants hold alternatives together for a reproducible comparison. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: Variants hold alternatives together for a reproducible comparison.
- **B:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.
- **D:** Incorrect for this question. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.

### Question 36 — A

Answer: Store the model credential as a project connection. A project connection holds the endpoint and credential externally. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. In this case: A project connection holds the endpoint and credential externally.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project connection holds the endpoint and credential externally.

### Question 37 — C

Answer: Paste the API key into a Python node inside the flow. A key in a flow file is a secret in source control. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Why the correct answer wins: A key in a flow file is a secret in source control.
- **B:** Incorrect for this question. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Why the correct answer wins: A key in a flow file is a secret in source control.
- **C:** Correct. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. In this case: A key in a flow file is a secret in source control.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A key in a flow file is a secret in source control.

### Question 38 — C

Answer: Use hybrid search with semantic ranking. Hybrid search retains keyword matching for exact identifiers. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **C:** Correct. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. In this case: Hybrid search retains keyword matching for exact identifiers.
- **D:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.

### Question 39 — B

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.

### Question 40 — B

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap make the cited passage specific. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **B:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap make the cited passage specific.
- **C:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.

### Question 41 — D

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **D:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate relevant text.

### Question 42 — A

Answer: Keep the prompt in its own file under version control. A versioned prompt file makes the change reviewable. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file makes the change reviewable.
- **B:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A versioned prompt file makes the change reviewable.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file makes the change reviewable.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A versioned prompt file makes the change reviewable.

### Question 43 — B

Answer: Run the evaluation in continuous integration before the flow is promoted. An offline evaluation gate before promotion. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An offline evaluation gate before promotion.
- **B:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An offline evaluation gate before promotion.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An offline evaluation gate before promotion.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An offline evaluation gate before promotion.

### Question 44 — C

Answer: Register a scoped tool list for the agent. A scoped tool list bounds what the agent may call. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **C:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds what the agent may call.
- **D:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds what the agent may call.

### Question 45 — C

Answer: Bound the agent memory to the current session. Session-scoped memory prevents facts crossing conversations. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Typed state makes each handoff explicit and testable instead of relying on free text. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **C:** Correct. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. In this case: Session-scoped memory prevents facts crossing conversations.
- **D:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.

### Question 46 — C, E

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing enables grounding, and document-level access enforces entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **C:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **E:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing enables grounding, and document-level access enforces entitlement.

### Question 47 — A, E

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file is the record, and the offline gate is the control. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **E:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the record, and the offline gate is the control.

### Question 48 — A, E

Answers: Create a Foundry hub and a project per team; Reference the deployment name from the flow rather than the model family name. A project per brand isolates assets, and the deployment name keeps flows stable. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A project per brand isolates assets, and the deployment name keeps flows stable.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A project per brand isolates assets, and the deployment name keeps flows stable.
- **C:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project per brand isolates assets, and the deployment name keeps flows stable.
- **D:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A project per brand isolates assets, and the deployment name keeps flows stable.
- **E:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A project per brand isolates assets, and the deployment name keeps flows stable.

### Question 49 — B

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation build on each other. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **B:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation build on each other.
- **C:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **D:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.

### Question 50 — C

Answer: Use an LLM judge with a rubric, calibrated against human grades. An LLM judge calibrated against human grades scales the grading. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **B:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **C:** Correct. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. In this case: An LLM judge calibrated against human grades scales the grading.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.

### Question 51 — A

Answer: Use a few hundred representative cases rather than a dozen. A set that small cannot separate a real gain from noise. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: A set that small cannot separate a real gain from noise.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A set that small cannot separate a real gain from noise.

### Question 52 — D

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.

### Question 53 — D

Answer: Score relevance of the answer to the question asked. Relevance measures whether the answer addresses the question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **B:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **C:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **D:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Relevance measures whether the answer addresses the question.

### Question 54 — D

Answer: Measure retrieval recall before scoring answer quality. If retrieval never returned the passage, prompt tuning addresses the wrong component. If retrieval never returned the passage, an answer-quality score is measuring the wrong component. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: If retrieval never returned the passage, prompt tuning addresses the wrong component.
- **B:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: If retrieval never returned the passage, prompt tuning addresses the wrong component.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: If retrieval never returned the passage, prompt tuning addresses the wrong component.
- **D:** Correct. If retrieval never returned the passage, an answer-quality score is measuring the wrong component. In this case: If retrieval never returned the passage, prompt tuning addresses the wrong component.

### Question 55 — A

Answer: Score coherence for logical structure. Coherence measures whether the answer holds together logically. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. In this case: Coherence measures whether the answer holds together logically.
- **B:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **D:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Coherence measures whether the answer holds together logically.

### Question 56 — A

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.

### Question 57 — C

Answer: Evaluate toxicity against the threshold the audience requires. Toxicity evaluation measures harmful output against the required threshold. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.
- **C:** Correct. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. In this case: Toxicity evaluation measures harmful output against the required threshold.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.

### Question 58 — D

Answer: Run continuous evaluation on sampled production traffic. Continuous evaluation on sampled traffic catches what a fixed dataset cannot. Online evaluation catches the drift that a fixed offline dataset cannot represent. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **B:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **D:** Correct. Online evaluation catches the drift that a fixed offline dataset cannot represent. In this case: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.

### Question 59 — C, D

Answers: Score groundedness against the retrieved passages; Score relevance of the answer to the question asked. Groundedness measures support, and relevance measures whether the question was answered. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **B:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **C:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **D:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **E:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.

### Question 60 — C, E

Answers: Test indirect injection through retrieved documents; Run adversarial jailbreak and prompt-injection cases before release. Indirect cases test retrieved content, and jailbreak cases test user input. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **C:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **D:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **E:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.

### Question 61 — A, C

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing identifies the stage, and prompt logging permits replay. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing identifies the stage, and prompt logging permits replay.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **C:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing identifies the stage, and prompt logging permits replay.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **E:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.

### Question 62 — D

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **B:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **C:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **D:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.

### Question 63 — C

Answer: Measure tokens per request and set a budget per endpoint. Per-request token measurement is what lets spend be attributed to a brand. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a brand.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a brand.
- **C:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: Per-request token measurement is what lets spend be attributed to a brand.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a brand.

### Question 64 — B

Answer: Cache identical requests and reuse the completion. Caching removes repeated inference for identical input. Caching removes repeated inference for identical input, which is the cheapest saving available. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Caching removes repeated inference for identical input.
- **B:** Correct. Caching removes repeated inference for identical input, which is the cheapest saving available. In this case: Caching removes repeated inference for identical input.
- **C:** Incorrect for this question. A TTL keeps a cached answer from outliving the content it came from. Why the correct answer wins: Caching removes repeated inference for identical input.
- **D:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Caching removes repeated inference for identical input.

### Question 65 — D

Answer: Set a time-to-live on the cache. A TTL stops a cached answer outliving its source. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **D:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A TTL stops a cached answer outliving its source.

### Question 66 — C

Answer: Route simple requests to a smaller model. A smaller model serves simple requests at lower cost. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A smaller model serves simple requests at lower cost.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A smaller model serves simple requests at lower cost.
- **C:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A smaller model serves simple requests at lower cost.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A smaller model serves simple requests at lower cost.

### Question 67 — A

Answer: Add a router that classifies the request and selects a model. A router selects a model appropriate to the request. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects a model appropriate to the request.
- **B:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router selects a model appropriate to the request.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects a model appropriate to the request.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects a model appropriate to the request.

### Question 68 — B

Answer: Set a request timeout with a bounded retry and backoff. A bounded timeout with backoff stops a failing dependency amplifying load. A bounded retry with backoff stops a failing dependency from multiplying load. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **B:** Correct. A bounded retry with backoff stops a failing dependency from multiplying load. In this case: A bounded timeout with backoff stops a failing dependency amplifying load.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **D:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.

### Question 69 — A

Answer: Fine-tune on approved examples to shorten the standing prompt. Fine-tuning can move stable instructions into the weights. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. In this case: Fine-tuning can move stable instructions into the weights.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **D:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.

### Question 70 — D

Answer: Move non-urgent generation into a batch run. Batch work uses cheaper capacity off the interactive path. Batch work uses cheaper capacity and takes the work off the interactive path. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **B:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **C:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **D:** Correct. Batch work uses cheaper capacity and takes the work off the interactive path. In this case: Batch work uses cheaper capacity off the interactive path.

### Question 71 — A, C

Answers: Measure tokens per request and set a budget per endpoint; Set a time-to-live on the cache. A token budget attributes cost, and a TTL keeps copy current. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A token budget attributes cost, and a TTL keeps copy current.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A token budget attributes cost, and a TTL keeps copy current.
- **C:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: A token budget attributes cost, and a TTL keeps copy current.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A token budget attributes cost, and a TTL keeps copy current.
- **E:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A token budget attributes cost, and a TTL keeps copy current.

### Question 72 — B, D

Answers: Add a router that classifies the request and selects a model; Route simple requests to a smaller model. A router selects per request, and a smaller model covers the simple majority. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **B:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A router selects per request, and a smaller model covers the simple majority.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects per request, and a smaller model covers the simple majority.
- **E:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.

### Question 73 — B

Answer: Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held. Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An optimization is applied before anything has been measured or attributed. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **B:** Correct. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. In this case: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **C:** Incorrect for this question. Evaluation precedes both the change it would validate and the measurement that motivates it. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **D:** Incorrect for this question. A driver is named before measurement, and the evaluation runs before the change exists. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.

### Question 74 — D

Answer: Create the endpoint first, then the deployment, with az ml online-endpoint and online-deployment. The endpoint must exist before a deployment is attached to it. A managed online endpoint must exist before a deployment is attached to it, and a deployment begins with zero traffic until one is assigned. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.
- **C:** Incorrect for this question. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.
- **D:** Correct. A managed online endpoint must exist before a deployment is attached to it, and a deployment begins with zero traffic until one is assigned. In this case: The endpoint must exist before a deployment is attached to it.

### Question 75 — A

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum stops billing between runs. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum stops billing between runs.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **C:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **D:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.

### Question 76 — A

Answer: Point the MLflow tracking URI at the workspace endpoint. The tracking URI must point at the workspace endpoint. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. In this case: The tracking URI must point at the workspace endpoint.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The tracking URI must point at the workspace endpoint.

### Question 77 — B

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports the judgement. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **B:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports the judgement.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports the judgement.

### Question 78 — A

Answer: Create an alert rule on the drift and latency metrics. An alert turns the metric into an action. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into an action.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert turns the metric into an action.
- **C:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert turns the metric into an action.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into an action.

### Question 79 — D, E

Answers: Tag the registered model with the data asset and commit it came from; Attach a description, metrics, and intended use to the model version. Tags record the data asset and commit, and the card documents intended use. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.
- **D:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags record the data asset and commit, and the card documents intended use.
- **E:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: Tags record the data asset and commit, and the card documents intended use.

### Question 80 — B, C

Answers: Set autoscale rules on the deployment with a deliberate minimum instance count; Configure liveness and readiness probes on the deployment. Autoscale matches capacity, and probes gate traffic until ready. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **B:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity, and probes gate traffic until ready.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: Autoscale matches capacity, and probes gate traffic until ready.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **E:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.

### Question 81 — A

Answer: Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress. A second deployment preserves the incumbent for measurement and rollback. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. In this case: A second deployment preserves the incumbent for measurement and rollback.
- **B:** Incorrect for this question. All traffic is shifted before the candidate is deployed, and the comparison comes after the exposure it was meant to prevent. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.
- **C:** Incorrect for this question. Replacing the incumbent destroys the comparison baseline and the thing you would roll back to. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.
- **D:** Incorrect for this question. There is nothing to compare before the candidate exists and is receiving traffic. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.

### Question 82 — C

Answer: Confirm the impact and scope from telemetry → contain the incident by shifting traffic or disabling the feature → fix the identified cause → add a regression case and update the gate. Impact is confirmed, the incident contained, the cause fixed, and a regression case added. Containment protects users before the root cause is chased, and the gate change stops the same defect returning. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. The cause is fixed before impact is confirmed, and containment arrives after the fix it was meant to buy time for. Why the correct answer wins: Impact is confirmed, the incident contained, the cause fixed, and a regression case added.
- **B:** Incorrect for this question. The scope of impact is confirmed last, so nobody knows what was affected while the fix was being written. Why the correct answer wins: Impact is confirmed, the incident contained, the cause fixed, and a regression case added.
- **C:** Correct. Containment protects users before the root cause is chased, and the gate change stops the same defect returning. In this case: Impact is confirmed, the incident contained, the cause fixed, and a regression case added.
- **D:** Incorrect for this question. A regression case is added before the defect is understood, and containment precedes impact assessment. Why the correct answer wins: Impact is confirmed, the incident contained, the cause fixed, and a regression case added.

### Question 83 — C

Answer: Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate. Detection precedes attribution, and retraining follows once the changed source is known. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Retraining before the drop is detected and attributed risks training on data that has the same defect. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.
- **B:** Incorrect for this question. The source is named before any evidence exists, and detection comes last. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.
- **C:** Correct. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. In this case: Detection precedes attribution, and retraining follows once the changed source is known.
- **D:** Incorrect for this question. A distribution comparison needs a detected drop to compare against, so the trigger is out of order. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.

### Question 84 — B

Answer: Tag the registered model with the data asset and commit it came from. Tags carrying the data asset and commit make the rebuild possible. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **B:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carrying the data asset and commit make the rebuild possible.
- **C:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.

### Question 85 — B

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap make the cited passage specific. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **B:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap make the cited passage specific.
- **C:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **D:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.

### Question 86 — B

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **B:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate relevant text.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.

### Question 87 — D

Answer: Attach a CPU compute cluster for the data preparation step. CPU compute is sufficient and cheaper per core. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **C:** Incorrect for this question. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **D:** Correct. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. In this case: CPU compute is sufficient and cheaper per core.

### Question 88 — C

Answer: Create the endpoint first, then the deployment, with az ml online-endpoint and online-deployment. The endpoint must exist before a deployment is attached to it. A managed online endpoint must exist before a deployment is attached to it, and a deployment begins with zero traffic until one is assigned. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.
- **C:** Correct. A managed online endpoint must exist before a deployment is attached to it, and a deployment begins with zero traffic until one is assigned. In this case: The endpoint must exist before a deployment is attached to it.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: The endpoint must exist before a deployment is attached to it.

### Question 89 — A

Answer: Move steady traffic to provisioned throughput. Workloads with sustained steady volume justify provisioned throughput. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Workloads with sustained steady volume justify provisioned throughput.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Workloads with sustained steady volume justify provisioned throughput.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Workloads with sustained steady volume justify provisioned throughput.
- **D:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Workloads with sustained steady volume justify provisioned throughput.

### Question 90 — A, B

Answers: Compress the system prompt and remove redundant instructions; Add a router that classifies the request and selects a model. A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases. A shorter system prompt reduces input tokens on every single call. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases.
- **B:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases.
- **E:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A compressed prompt cuts tokens per call, and a router keeps strong models for hard cases.

### Question 91 — C

Answer: Stream the response so the first token arrives sooner. Streaming delivers the first token sooner and improves perceived latency. Streaming improves perceived latency without changing total generation time. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Batch work uses cheaper capacity and takes the work off the interactive path. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.
- **C:** Correct. Streaming improves perceived latency without changing total generation time. In this case: Streaming delivers the first token sooner and improves perceived latency.
- **D:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.

### Question 92 — D

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version identifies what was served. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version identifies what was served.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit model version identifies what was served.
- **C:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version identifies what was served.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version identifies what was served.

### Question 93 — D

Answer: Deploy a batch endpoint for the overnight scoring job. A batch endpoint scores a large dataset without always-on capacity. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.
- **D:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint scores a large dataset without always-on capacity.

### Question 94 — D

Answer: Evaluate toxicity against the threshold the audience requires. Toxicity evaluation measures harmful output against the required threshold. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.
- **B:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Toxicity evaluation measures harmful output against the required threshold.
- **D:** Correct. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. In this case: Toxicity evaluation measures harmful output against the required threshold.

### Question 95 — B

Answer: Promote versions through aliases such as candidate and production. An alias gives a stable pointer that promotion moves without editing deployments. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An alias gives a stable pointer that promotion moves without editing deployments.
- **B:** Correct. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. In this case: An alias gives a stable pointer that promotion moves without editing deployments.
- **C:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An alias gives a stable pointer that promotion moves without editing deployments.
- **D:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: An alias gives a stable pointer that promotion moves without editing deployments.

### Question 96 — B

Answer: Define the workspace in a Bicep module deployed per environment. A reviewed Bicep module gives every unit the same reproducible definition. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A reviewed Bicep module gives every unit the same reproducible definition.
- **B:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A reviewed Bicep module gives every unit the same reproducible definition.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A reviewed Bicep module gives every unit the same reproducible definition.
- **D:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A reviewed Bicep module gives every unit the same reproducible definition.

### Question 97 — A, C

Answers: Enable MLflow tracking so runs log to the workspace; Group the trials under a named experiment. Enabling tracking records each run, and a named experiment makes variants comparable. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: Enabling tracking records each run, and a named experiment makes variants comparable.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Enabling tracking records each run, and a named experiment makes variants comparable.
- **C:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: Enabling tracking records each run, and a named experiment makes variants comparable.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Enabling tracking records each run, and a named experiment makes variants comparable.
- **E:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Enabling tracking records each run, and a named experiment makes variants comparable.

### Question 98 — D

Answer: Connect to the source through a federated connector and query it in place. A federated connector queries the source in place without copying it. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Exporting licensed content into your own storage is the step the licence usually forbids, so the copy itself is the risk. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **B:** Incorrect for this question. Copying a licensed corpus into an index you host is a storage and licence decision, not just a connector setting. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **D:** Correct. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. In this case: A federated connector queries the source in place without copying it.

### Question 99 — A

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing attributes the failure to retrieval or generation. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing attributes the failure to retrieval or generation.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.
- **C:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.
- **D:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.

### Question 100 — B

Answer: Re-run the evaluation after the cost optimization. Quality must be re-measured after any change that trades accuracy for cost. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.
- **B:** Correct. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. In this case: Quality must be re-measured after any change that trades accuracy for cost.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.
- **D:** Incorrect for this question. The support queue is a lagging signal that reports damage after users have already experienced it. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.
