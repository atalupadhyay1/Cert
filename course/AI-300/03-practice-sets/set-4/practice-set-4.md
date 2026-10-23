# Microsoft AI-300 — Full-Length Mock Exam 4

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A bank must prove that development jobs cannot alter the production model registry. What separation provides that?

Domain: Design and implement an MLOps infrastructure

- A. Attach a GPU cluster with four always-on nodes
- B. Create a separate Azure Machine Learning workspace per environment
- C. Use one workspace for development, test, and production
- D. Create the workspace in the portal and record the steps in a wiki

### 2. A regulator asks how jobs reach the data without a credential in the code. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Register the data as a versioned data asset
- C. Reference the storage path with the account key inline in the job YAML
- D. Register a datastore that points at the storage account

### 3. An auditor requires that the production environment be reconstructible from a reviewed artifact. What should be delivered?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Define the workspace in a Bicep module deployed per environment
- C. Export an ARM template from the portal after building it by hand
- D. Create the workspace in the portal and record the steps in a wiki

### 4. A resource created by hand outside the template survived three deployments unnoticed. What should be deployed as?

Domain: Design and implement an MLOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Keep public network access enabled so notebooks connect easily
- C. Deploy the module as a deployment stack so removed resources are cleaned up
- D. Create the workspace in the portal and record the steps in a wiki

### 5. Every training run must be reproducible from a recorded command. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Stream the job with az ml job stream to inspect logs
- B. Create the workspace in the portal and record the steps in a wiki
- C. Submit the job with az ml job create --file job.yaml
- D. Run the job from a compute instance notebook

### 6. A security review forbids a stored client secret in the deployment repository. What should replace it?

Domain: Design and implement an MLOps infrastructure

- A. Authenticate the workflow with workload identity federation and no stored secret
- B. Store a service principal client secret as a GitHub repository secret
- C. Grant the pipeline service principal Owner on the subscription
- D. Set the connection string as a plain environment variable in the job

### 7. A named officer must approve any release that touches a customer-facing model. What should be configured?

Domain: Design and implement an MLOps infrastructure

- A. Use GitHub environment protection rules to gate the production deploy job
- B. Fan the tests out across a matrix of dependency versions
- C. Run the pipeline from a GitHub Actions workflow on merge to main
- D. Store a service principal client secret as a GitHub repository secret

### 8. A CI identity leaked from the test subscription must not reach production. What limits the impact?

Domain: Design and implement an MLOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Create a service principal per environment with a least-privilege role assignment
- C. Grant the pipeline service principal Owner on the subscription
- D. Set the connection string as a plain environment variable in the job

### 9. A declined application must be traceable to the exact model that scored it. What pins the artifact?

Domain: Design and implement an MLOps infrastructure

- A. Register the model and always deploy whichever version is latest
- B. Register each candidate with a version and deploy one explicit version
- C. Print the metrics to the job log and read them from the console
- D. Overwrite the existing model version instead of registering a new one

### 10. Two business units must reuse one approved scoring component without copying it. What enables that?

Domain: Design and implement an MLOps infrastructure

- A. Package the preparation step as a reusable component
- B. Publish the component to the workspace registry
- C. Create the workspace in the portal and record the steps in a wiki
- D. Rebuild the environment by hand from the notes in the ticket

### 11. A connection string must rotate quarterly without a code change. Where should it live?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Store connection strings in Key Vault and reference them by name
- C. Reference the storage path with the account key inline in the job YAML
- D. Set the connection string as a plain environment variable in the job

### 12. An audited environment must be reproducible and free of manual change. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Deploy the module as a deployment stack so removed resources are cleaned up
- B. Export an ARM template from the portal after building it by hand
- C. Rebuild the environment by hand from the notes in the ticket
- D. Create the workspace in the portal and record the steps in a wiki
- E. Define the workspace in a Bicep module deployed per environment

### 13. A regulated release must be gated and secret-free. Which two controls apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Use GitHub environment protection rules to gate the production deploy job
- C. Authenticate the workflow with workload identity federation and no stored secret
- D. Fan the tests out across a matrix of dependency versions
- E. Store a service principal client secret as a GitHub repository secret

### 14. A bank is provisioning a new regulated workspace from code. Which sequence is correct?

Domain: Design and implement an MLOps infrastructure

- A. Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace
- B. Authenticate the pipeline → run a smoke job → define the workspace in Bicep → deploy the module
- C. Run a smoke job against the workspace → deploy the module → authenticate the pipeline → define the workspace in Bicep
- D. Deploy the module → define the workspace in Bicep → run a smoke job → authenticate the pipeline

### 15. Audit asks which data asset fed the evaluation that approved a model. What provides that record?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Assign the work to a person instead of investigating the failure
- C. Run the whole workflow as a single script job
- D. Run the job from a compute instance notebook

### 16. Training and scoring must use identical feature logic or the model silently degrades. What enforces it?

Domain: Implement machine learning model lifecycle and operations

- A. Run the whole workflow as a single script job
- B. Assign the work to a person instead of investigating the failure
- C. Package the preparation step as a reusable component
- D. Define the steps as a pipeline job with explicit inputs and outputs

### 17. A tuning exercise must stay within a fixed compute budget across a wide search space. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Use automated ML to establish the tabular baseline
- B. Run a full grid sweep over every combination
- C. Run a sweep job over a searched hyperparameter space
- D. Increase the model size until the answers improve

### 18. Training runs intermittently and the bank is billed for accelerators overnight. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Attach a GPU cluster with four always-on nodes
- B. Attach a GPU cluster with a minimum of zero nodes
- C. Attach a CPU compute cluster for the data preparation step
- D. Run the job from a compute instance notebook

### 19. Two runs produced the same metric with different feature sets and nobody can tell which was which. What should be tracked?

Domain: Implement machine learning model lifecycle and operations

- A. Enable MLflow tracking so runs log to the workspace
- B. Print the metrics to the job log and read them from the console
- C. Disable request logging to reduce storage cost
- D. Assign the work to a person instead of investigating the failure

### 20. Runs are logged locally and never appear in the shared experiment list. What is misconfigured?

Domain: Implement machine learning model lifecycle and operations

- A. Disable request logging to reduce storage cost
- B. Run the job from a compute instance notebook
- C. Print the metrics to the job log and read them from the console
- D. Point the MLflow tracking URI at the workspace endpoint

### 21. A registry entry was replaced in place and the approved decision cannot be rebuilt. What was the error?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Register each candidate with a version and deploy one explicit version
- C. Tag the registered model with the data asset and commit it came from
- D. Overwrite the existing model version instead of registering a new one

### 22. An auditor must rebuild a model approved eighteen months ago. What must registration have captured?

Domain: Implement machine learning model lifecycle and operations

- A. Register the model and always deploy whichever version is latest
- B. Attach a description, metrics, and intended use to the model version
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Tag the registered model with the data asset and commit it came from

### 23. A risk reviewer must judge whether a version is suitable before promotion. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Register the model and always deploy whichever version is latest
- C. Tag the registered model with the data asset and commit it came from
- D. Attach a description, metrics, and intended use to the model version

### 24. A container accepts traffic before the model finishes loading and errors for two minutes. What prevents it?

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Monitor only the accuracy reported at deployment time
- C. Configure liveness and readiness probes on the deployment
- D. Deploy without probes and rely on the platform health check

### 25. Every candidate requires a container rebuild before it can be tested. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Mount the model artifact rather than baking it into the image
- C. Overwrite the existing model version instead of registering a new one
- D. Replace the production deployment in a single step

### 26. A new scorecard model may affect at most five percent of applications initially. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Split endpoint traffic 10/90 so the new deployment receives a canary share
- B. Keep the previous deployment in place so traffic can be moved back
- C. Replace the production deployment in a single step
- D. Deploy straight to production to save a day

### 27. A model must be withdrawable within an hour of a defect being confirmed. What enables that?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Keep the previous deployment in place so traffic can be moved back
- C. Overwrite the existing model version instead of registering a new one
- D. Replace the production deployment in a single step

### 28. A fraud-scoring service peaks at month end and is idle otherwise. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Set autoscale rules on the deployment with a deliberate minimum instance count
- B. Send the overnight file through the online endpoint request by request
- C. Deploy without probes and rely on the platform health check
- D. Pin a fixed instance count for a spiky workload

### 29. A drift report is filed monthly and read only after an incident. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Disable request logging to reduce storage cost
- B. Monitor only the accuracy reported at deployment time
- C. Assign the work to a person instead of investigating the failure
- D. Create an alert rule on the drift and latency metrics

### 30. A regulator asks how the firm knows the model still sees representative data. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Monitor only the accuracy reported at deployment time
- C. Retrain the model on the newer data
- D. Enable data drift monitoring against the training baseline

### 31. A regulated release must be bounded and reversible. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one
- E. Bake the model weights into the container image

### 32. A scored endpoint must survive bursts and not serve before the model loads. Which two configurations apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Set autoscale rules on the deployment with a deliberate minimum instance count
- B. Pin a fixed instance count for a spiky workload
- C. Send the overnight file through the online endpoint request by request
- D. Deploy without probes and rely on the platform health check
- E. Configure liveness and readiness probes on the deployment

### 33. A scorecard candidate must reach production behind a measured gate. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Register the model version → train the candidate → evaluate against the gate → shift all traffic
- B. Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold
- C. Evaluate against the gate → train the candidate → shift all traffic → register the model version
- D. Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate

### 34. Two business units need shared capacity but separate assets and connections. What should be created?

Domain: Design and implement a GenAIOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Use one workspace for development, test, and production
- C. Create a Foundry hub and a project per team
- D. Give every team one project and one shared connection

### 35. A customer assistant runs at steady predictable volume through business hours. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Start on pay-as-you-go while the volume is still unknown
- B. Reserve provisioned throughput for the steady high-volume workload
- C. Pin a fixed instance count for a spiky workload
- D. Use the largest model for every request

### 36. A flow must be tested node by node before each release. What should it be authored as?

Domain: Design and implement a GenAIOps infrastructure

- A. Run the job from a compute instance notebook
- B. Run the flow as a batch job over the evaluation dataset
- C. Author the flow as a directed acyclic graph with typed inputs and outputs
- D. Run the whole workflow as a single script job

### 37. A flow must reference the model endpoint without a credential in the flow file. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Set the connection string as a plain environment variable in the job
- C. Reference the storage path with the account key inline in the job YAML
- D. Store the model credential as a project connection

### 38. A flow running in Azure must reach storage without any stored credential. What should it use?

Domain: Design and implement a GenAIOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Reference the storage path with the account key inline in the job YAML
- C. Assign a managed identity to compute and grant it the storage role
- D. Set the connection string as a plain environment variable in the job

### 39. A key was typed into a node and merged with the flow. What is the defect?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Store the model credential as a project connection
- C. Store connection strings in Key Vault and reference them by name
- D. Set the connection string as a plain environment variable in the job

### 40. A shared index serves four business units and each user may see only their own documents. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Set the connection string as a plain environment variable in the job
- B. Index every document the organization holds
- C. Keep public network access enabled so notebooks connect easily
- D. Set document-level access in the index so retrieval respects entitlements

### 41. Policy wording changes monthly and answers must cite the current version. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Index the documents in Azure AI Search and query the index from the flow
- B. Index every document the organization holds
- C. Increase the model size until the answers improve
- D. Fine-tune the model on the document set instead of retrieving

### 42. An answer cites the right policy but the wrong clause. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Raise retrieval depth to the maximum for safety
- B. Index every document the organization holds
- C. Index each document as one large chunk
- D. Chunk documents by section with a small overlap

### 43. A policy update was published last week and the assistant still quotes the old text. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk documents by section with a small overlap
- B. Rebuild the index on a schedule after the source content changes
- C. Index every document the organization holds
- D. Retrain the model on the newer data

### 44. Retrieval returns an entire policy document and the model quotes an unrelated paragraph. What caused it?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk documents by section with a small overlap
- B. Index every document the organization holds
- C. Index each document as one large chunk
- D. Retrain the model on the newer data

### 45. No prompt change may reach customers until quality is measured. What should be in place?

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Assign the work to a person instead of investigating the failure
- C. Deploy straight to production to save a day
- D. Run the evaluation in continuous integration before the flow is promoted

### 46. A regulated process requires a change record for every prompt edit. Where should prompts live?

Domain: Design and implement a GenAIOps infrastructure

- A. Create a variant to compare two prompt strategies side by side
- B. Paste the API key into a Python node inside the flow
- C. Keep the prompt in its own file under version control
- D. Rewrite the prompt and deploy it immediately

### 47. A service agent can reach a payments tool that must stay out of scope. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Expose every available tool so the agent can choose freely
- C. Register a scoped tool list for the agent
- D. Increase the model size until the answers improve

### 48. A conversation carried one customer's details into the next. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Pass typed state between agent steps
- B. Index every document the organization holds
- C. Bound the agent memory to the current session
- D. Expose every available tool so the agent can choose freely

### 49. A platform team must isolate unit assets and keep flows stable across model swaps. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Paste the API key into a Python node inside the flow
- C. Create a Foundry hub and a project per team
- D. Reference the deployment name from the flow rather than the model family name
- E. Give every team one project and one shared connection

### 50. An assistant must ground on current policy and respect entitlements. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Fine-tune the model on the document set instead of retrieving
- C. Index every document the organization holds
- D. Index the documents in Azure AI Search and query the index from the flow
- E. Set document-level access in the index so retrieval respects entitlements

### 51. A change record and a quality gate are both required for prompt edits. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Run the evaluation in continuous integration before the flow is promoted
- B. Deploy straight to production to save a day
- C. Keep the prompt in its own file under version control
- D. Rewrite the prompt and deploy it immediately
- E. Assign the work to a person instead of investigating the failure

### 52. A claims assistant must ground on current policy documents. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them
- B. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness
- C. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- D. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents

### 53. Four thousand cases must be graded inside a two-week release window. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Generate the evaluation set from the prompt itself
- C. Use an LLM judge with a rubric, calibrated against human grades
- D. Rely on the LLM judge without checking it against human grades

### 54. An answer contradicts a figure it stated two paragraphs earlier. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score fluency for readability and language quality
- C. Score coherence for logical structure
- D. Score relevance of the answer to the question asked

### 55. A retrieved customer document contains text instructing the assistant to ignore its rules. What is the exposure?

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Disable request logging to reduce storage cost
- C. Test indirect injection through retrieved documents
- D. Evaluate toxicity against the threshold the audience requires

### 56. A customer disputes an answer and the team must find which stage failed. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Log prompts and completions against the trace, within data policy
- C. Enable distributed tracing and log the retrieval and model spans
- D. Rely on the LLM judge without checking it against human grades

### 57. A team disabled request logging to cut storage cost and now cannot investigate complaints. What is the objection?

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Log prompts and completions against the trace, within data policy
- C. Enable distributed tracing and log the retrieval and model spans
- D. Assign the work to a person instead of investigating the failure

### 58. A fixed dataset passes every release while production satisfaction falls. What should be added?

Domain: Implement generative AI quality assurance and observability

- A. Run continuous evaluation on sampled production traffic
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Build the evaluation dataset from real queries with graded answers
- D. Accept the behaviour because the aggregate score still looks healthy

### 59. A regulated answer must be supported and on point. Which two metrics apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Score similarity against a reference answer
- B. Score fluency for readability and language quality
- C. Score coherence for logical structure
- D. Score relevance of the answer to the question asked
- E. Score groundedness against the retrieved passages

### 60. An assistant reads external documents and must resist override from users and documents. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Evaluate toxicity against the threshold the audience requires
- C. Test indirect injection through retrieved documents
- D. Disable request logging to reduce storage cost
- E. Score fluency for readability and language quality

### 61. A disputed answer must be diagnosable and reproducible. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Log prompts and completions against the trace, within data policy
- C. Assign the work to a person instead of investigating the failure
- D. Rely on the LLM judge without checking it against human grades
- E. Enable distributed tracing and log the retrieval and model spans

### 62. A regulator asks how a wrong answer is investigated months later. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- B. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set
- C. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set
- D. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set

### 63. A cached answer still quotes a fee schedule replaced last month. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Set a time-to-live on the cache
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Disable request logging to reduce storage cost

### 64. A single endpoint must answer both quick lookups and long case summaries. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Route simple requests to a smaller model
- C. Add a router that classifies the request and selects a model
- D. Cache identical requests and reuse the completion

### 65. A team standardized on the largest model for consistency and the bill tripled. What is the objection to that choice?

Domain: Optimize generative AI systems and model performance

- A. Route simple requests to a smaller model
- B. Add a router that classifies the request and selects a model
- C. Use the largest model for every request
- D. Cache identical requests and reuse the completion

### 66. A stalled dependency causes retries to multiply load during an incident. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Set a request timeout with a bounded retry and backoff
- C. Use the largest model for every request
- D. Stream the response so the first token arrives sooner

### 67. A 5,200-token system prompt ships on every call and much of it repeats. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Raise retrieval depth to the maximum for safety
- B. Increase the model size until the answers improve
- C. Cache identical requests and reuse the completion
- D. Compress the system prompt and remove redundant instructions

### 68. A stable classification task carries a long instruction on every call. What can absorb it?

Domain: Optimize generative AI systems and model performance

- A. Fine-tune on approved examples to shorten the standing prompt
- B. Fine-tune the model on the document set instead of retrieving
- C. Compress the system prompt and remove redundant instructions
- D. Increase the model size until the answers improve

### 69. Twelve months of steady volume justify a lower unit cost. What should be adopted?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Move steady traffic to provisioned throughput
- C. Start on pay-as-you-go while the volume is still unknown
- D. Cache identical requests and reuse the completion

### 70. A unit needs attributable spend and current answers. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Measure tokens per request and set a budget per endpoint
- B. Cache identical requests and reuse the completion
- C. Use the largest model for every request
- D. Accept the behaviour because the aggregate score still looks healthy
- E. Set a time-to-live on the cache

### 71. A mixed workload must cost less while hard cases keep their quality. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Route simple requests to a smaller model
- B. Use the largest model for every request
- C. Cache identical requests and reuse the completion
- D. Add a router that classifies the request and selects a model
- E. Retrain the model on the newer data

### 72. A finance function must cut model spend without losing quality. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver
- B. Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver
- C. Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization
- D. Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held

### 73. A regulator asks which dataset trained a model approved last year. What should have been registered?

Domain: Design and implement an MLOps infrastructure

- A. Disable request logging to reduce storage cost
- B. Reference the storage path with the account key inline in the job YAML
- C. Register a datastore that points at the storage account
- D. Register the data as a versioned data asset

### 74. One module must deploy to four regions with different SKUs and names. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Define the workspace in a Bicep module deployed per environment
- C. Pass environment values through a Bicep parameter file per stage
- D. Export an ARM template from the portal after building it by hand
- E. Create the workspace in the portal and record the steps in a wiki

### 75. A first credit-risk model is needed within a week as a defensible baseline. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Use automated ML to establish the tabular baseline
- C. Run the job from a compute instance notebook
- D. Run the whole workflow as a single script job

### 76. Nine hundred runs share one list and three feature variants cannot be compared. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Disable request logging to reduce storage cost
- C. Enable MLflow tracking so runs log to the workspace
- D. Group the trials under a named experiment

### 77. A deployment resolving the newest registration shipped an untested candidate. What should it reference?

Domain: Implement machine learning model lifecycle and operations

- A. Register the model and always deploy whichever version is latest
- B. Tag the registered model with the data asset and commit it came from
- C. Assign the work to a person instead of investigating the failure
- D. Register each candidate with a version and deploy one explicit version

### 78. Customer behaviour changed after a rate rise and only the deployment-day accuracy is known. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Retrain the model on the newer data
- C. Enable data drift monitoring against the training baseline
- D. Accept the behaviour because the aggregate score still looks healthy

### 79. An application needs a synchronous decision on a single application. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Deploy to a managed online endpoint with an explicit model version
- C. Send the overnight file through the online endpoint request by request
- D. Deploy a batch endpoint for the overnight scoring job

### 80. A monthly portfolio rescoring must avoid always-on capacity and stay reversible. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Deploy a batch endpoint for the overnight scoring job
- B. Keep the previous deployment in place so traffic can be moved back
- C. Bake the model weights into the container image
- D. Replace the production deployment in a single step
- E. Send the overnight file through the online endpoint request by request

### 81. A risk committee needs a pinned artifact and a documented intended use. Which two artifacts apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Tag the registered model with the data asset and commit it came from
- C. Overwrite the existing model version instead of registering a new one
- D. Register each candidate with a version and deploy one explicit version
- E. Attach a description, metrics, and intended use to the model version

### 82. A scorecard release must stay reversible throughout the rollout. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress
- B. Compare error rate and latency → deploy the new version → send a small traffic share → replace the incumbent
- C. Send all traffic to the new deployment → deploy the new version → compare metrics → move traffic back
- D. Replace the incumbent deployment → compare error rate and latency → deploy the new version to a second deployment → send traffic to it

### 83. A finance function must size an assistant before quarter end. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Forecast the peak load → reserve provisioned throughput → measure the current rate → load test
- B. Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration
- C. Reserve provisioned throughput → measure the request rate → forecast the load → load test the configuration
- D. Load test the configuration → reserve provisioned throughput → forecast the load → measure the request rate

### 84. A nightly report must leave the interactive path. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Submit the batch endpoint job → prepare the input dataset → validate the output → confirm the workload is not interactive
- B. Prepare the input dataset → confirm the workload is not interactive → validate the output → submit the job
- C. Validate the output file → submit the job → prepare the input → confirm the workload
- D. Confirm the workload is not interactive → prepare a batch input dataset → submit the batch endpoint job → validate the output file against the schema

### 85. A flow must be scored across four hundred evaluation cases before release. What should be run?

Domain: Design and implement a GenAIOps infrastructure

- A. Deploy the flow to a managed online endpoint
- B. Stream the job with az ml job stream to inspect logs
- C. Run the job from a compute instance notebook
- D. Run the flow as a batch job over the evaluation dataset

### 86. Two retrieval-aware prompt strategies must be compared on the same cases. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Rewrite the prompt and deploy it immediately
- C. Create a variant to compare two prompt strategies side by side
- D. Author the flow as a directed acyclic graph with typed inputs and outputs

### 87. An answer reads beautifully and is factually invented. Which metric would still score it well?

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Score relevance of the answer to the question asked
- C. Score coherence for logical structure
- D. Score groundedness against the retrieved passages

### 88. An answer states a fee cap that no retrieved passage contains. Which metric targets this?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score fluency for readability and language quality
- C. Score relevance of the answer to the question asked
- D. Score coherence for logical structure

---

## Case study — Cedar Ridge Health

Cedar Ridge Health is deploying a generative assistant for care-coordination staff and has been asked by its safety committee to prove the system is ready. The committee wants evidence about harmful output, resistance to instruction-override attempts, and whether the system can be traced when a clinician disputes an answer. The team has a 300-case evaluation set built from last year's queries and no agreed rubric for grading answers. A vendor has offered a jailbreak test suite, and the team is unsure whether running it once before launch is sufficient.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. A patient-portal assistant is a pilot with unknown volume and may be withdrawn. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Pin a fixed instance count for a spiky workload
- B. Reserve provisioned throughput for the steady high-volume workload
- C. Use the largest model for every request
- D. Start on pay-as-you-go while the volume is still unknown

### 90. A 25-case clinical set moved from 0.74 to 0.79 and the team wants to release. What is the objection?

Domain: Implement generative AI quality assurance and observability

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Use a few hundred representative cases rather than a dozen
- C. Assign the work to a person instead of investigating the failure
- D. Generate the evaluation set from the prompt itself

### 91. The same patient-education questions repeat across the portal all day. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Add a router that classifies the request and selects a model
- C. Compress the system prompt and remove redundant instructions
- D. Set a time-to-live on the cache

---

## Case study — Fairhaven Mutual

Fairhaven Mutual runs a client-service assistant and a claims-summary model and is preparing for a regulatory review. The regulator has asked three questions: how the firm detects degradation, how it proves a change did not reduce quality, and how it would withdraw a model within an hour. The firm has telemetry in Application Insights but no alerting, an evaluation set that was written by the same team that wrote the prompt, and a deployment process that rebuilds the container image for every model version. The platform team wants a plan it can execute before the review.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The regulator asks how a model is withdrawn within an hour. What makes withdrawal a single change?

Domain: Design and implement an MLOps infrastructure

- A. Promote versions through aliases such as candidate and production
- B. Overwrite the existing model version instead of registering a new one
- C. Register the model and always deploy whichever version is latest
- D. Register each candidate with a version and deploy one explicit version

### 93. A deployment must be reversible within the hour. What must exist?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Keep the previous deployment in place so traffic can be moved back
- C. Overwrite the existing model version instead of registering a new one
- D. Replace the production deployment in a single step

### 94. The regulator asks how degradation is detected and explained. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Rely on the LLM judge without checking it against human grades
- B. Log prompts and completions against the trace, within data policy
- C. Enable distributed tracing and log the retrieval and model spans
- D. Disable request logging to reduce storage cost
- E. Assign the work to a person instead of investigating the failure

---

## Case study — Granite University

Granite University runs a research assistant over licensed journal content and its own thesis repository. The licences restrict where the content may be stored, so the assistant must query the publisher system in place rather than copy it into the university's own index. Researchers want citations, and the library wants to know which passages an answer relied on when a claim is challenged. The university also runs its own evaluation and has asked for a way to compare retrieval configurations before the academic year starts.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A vendor proposes fine-tuning on licensed journals instead of querying the publisher. What is the objection?

Domain: Optimize generative AI systems and model performance

- A. Fine-tune the model on the document set instead of retrieving
- B. Index the documents in Azure AI Search and query the index from the flow
- C. Set document-level access in the index so retrieval respects entitlements
- D. Rebuild the index on a schedule after the source content changes

### 96. Licences restrict where the content may be stored, but researchers need grounded answers. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Connect to the source through a federated connector and query it in place
- B. Build a knowledge-source connector that indexes the whole corpus into the project
- C. Export the corpus to storage and index it as files
- D. Index every document the organization holds

### 97. A challenged claim must be traced to the passage it relied on. Which metric records that support?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score coherence for logical structure
- C. Score relevance of the answer to the question asked
- D. Score fluency for readability and language quality

---

## Case study — Northgate Bank

Northgate Bank runs a document question-answering assistant over loan files, and internal audit has asked for a control that proves answers are supported by the retrieved evidence. The bank has two evaluation approaches: a similarity score against a reference answer and a groundedness score against retrieved passages, and the team disagrees about which one governs release. Audit also wants to know how a wrong answer is investigated six months after the fact. The bank has a strict retention policy: prompts may be stored for 90 days, and customer identifiers must be redacted before storage.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. A stress-test model must be rebuilt with the exact libraries used at validation. What should be pinned?

Domain: Design and implement an MLOps infrastructure

- A. Reference the floating latest tag for the environment image
- B. Print the metrics to the job log and read them from the console
- C. Disable request logging to reduce storage cost
- D. Build a versioned curated environment for the job

### 99. One script covers prepare, train, and validate, and a failure is impossible to place. What should replace it?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Define the steps as a pipeline job with explicit inputs and outputs
- C. Run the job from a compute instance notebook
- D. Run the whole workflow as a single script job

### 100. A scoring tier must serve more requests per unit of capacity without changing the model family. What should be used?

Domain: Optimize generative AI systems and model performance

- A. Retrain the model on the newer data
- B. Use the largest model for every request
- C. Index every document the organization holds
- D. Use a quantized deployment for the high-throughput tier

---

## Answer key and explanations

### Question 1 — B

Answer: Create a separate Azure Machine Learning workspace per environment. A workspace per environment keeps registered assets apart from development activity. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A workspace per environment keeps registered assets apart from development activity.
- **B:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A workspace per environment keeps registered assets apart from development activity.
- **C:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A workspace per environment keeps registered assets apart from development activity.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A workspace per environment keeps registered assets apart from development activity.

### Question 2 — D

Answer: Register a datastore that points at the storage account. A registered datastore holds the connection outside the job definition. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A registered datastore holds the connection outside the job definition.
- **B:** Incorrect for this question. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Why the correct answer wins: A registered datastore holds the connection outside the job definition.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A registered datastore holds the connection outside the job definition.
- **D:** Correct. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. In this case: A registered datastore holds the connection outside the job definition.

### Question 3 — B

Answer: Define the workspace in a Bicep module deployed per environment. A Bicep module is a reviewable, reproducible definition. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.
- **B:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A Bicep module is a reviewable, reproducible definition.
- **C:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.

### Question 4 — C

Answer: Deploy the module as a deployment stack so removed resources are cleaned up. A deployment stack removes or denies resources it does not own. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **C:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: A deployment stack removes or denies resources it does not own.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A deployment stack removes or denies resources it does not own.

### Question 5 — C

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI is reproducible and auditable. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.
- **C:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI is reproducible and auditable.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.

### Question 6 — A

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation removes the stored secret. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation removes the stored secret.
- **B:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation removes the stored secret.
- **C:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation removes the stored secret.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation removes the stored secret.

### Question 7 — A

Answer: Use GitHub environment protection rules to gate the production deploy job. A protected environment requires approval before the job runs. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: A protected environment requires approval before the job runs.
- **B:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: A protected environment requires approval before the job runs.
- **C:** Incorrect for this question. A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit. Why the correct answer wins: A protected environment requires approval before the job runs.
- **D:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: A protected environment requires approval before the job runs.

### Question 8 — B

Answer: Create a service principal per environment with a least-privilege role assignment. A service principal per environment with a least-privilege role confines the blast radius. Scoping identity per environment limits what a compromised development pipeline can reach. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A service principal per environment with a least-privilege role confines the blast radius.
- **B:** Correct. Scoping identity per environment limits what a compromised development pipeline can reach. In this case: A service principal per environment with a least-privilege role confines the blast radius.
- **C:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: A service principal per environment with a least-privilege role confines the blast radius.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A service principal per environment with a least-privilege role confines the blast radius.

### Question 9 — B

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version identifies what was served. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version identifies what was served.
- **B:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version identifies what was served.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: An explicit model version identifies what was served.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version identifies what was served.

### Question 10 — B

Answer: Publish the component to the workspace registry. A registry shares approved assets across workspaces. A registry shares assets across workspaces, which is how a pattern proven in development is reused in production. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Why the correct answer wins: A registry shares approved assets across workspaces.
- **B:** Correct. A registry shares assets across workspaces, which is how a pattern proven in development is reused in production. In this case: A registry shares approved assets across workspaces.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A registry shares approved assets across workspaces.
- **D:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A registry shares approved assets across workspaces.

### Question 11 — B

Answer: Store connection strings in Key Vault and reference them by name. Key Vault holds the secret and rotation happens outside the code. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.
- **B:** Correct. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. In this case: Key Vault holds the secret and rotation happens outside the code.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the code.

### Question 12 — A, E

Answers: Define the workspace in a Bicep module deployed per environment; Deploy the module as a deployment stack so removed resources are cleaned up. Bicep defines the shape, and a deployment stack removes drift. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: Bicep defines the shape, and a deployment stack removes drift.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **E:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: Bicep defines the shape, and a deployment stack removes drift.

### Question 13 — B, C

Answers: Authenticate the workflow with workload identity federation and no stored secret; Use GitHub environment protection rules to gate the production deploy job. Federated identity removes the secret, and a protected environment adds approval. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **B:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **C:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **D:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **E:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.

### Question 14 — A

Answer: Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace. Definition, pipeline identity, deployment, and a smoke job follow in that order. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. In this case: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **B:** Incorrect for this question. Identity is established early, but the smoke job still precedes both the definition and the deployment. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **C:** Incorrect for this question. A job cannot run against infrastructure that has neither been defined nor deployed, and the pipeline has no identity yet. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.
- **D:** Incorrect for this question. The module is deployed before it is written, and authentication last means the pipeline could never have deployed anything. Why the correct answer wins: Definition, pipeline identity, deployment, and a smoke job follow in that order.

### Question 15 — A

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline records each step input and output. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline records each step input and output.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A pipeline records each step input and output.
- **C:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline records each step input and output.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A pipeline records each step input and output.

### Question 16 — C

Answer: Package the preparation step as a reusable component. A shared component gives both paths the same implementation. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A shared component gives both paths the same implementation.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A shared component gives both paths the same implementation.
- **C:** Correct. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. In this case: A shared component gives both paths the same implementation.
- **D:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: A shared component gives both paths the same implementation.

### Question 17 — C

Answer: Run a sweep job over a searched hyperparameter space. A sampled sweep covers a wide space within a budget. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Why the correct answer wins: A sampled sweep covers a wide space within a budget.
- **B:** Incorrect for this question. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Why the correct answer wins: A sampled sweep covers a wide space within a budget.
- **C:** Correct. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. In this case: A sampled sweep covers a wide space within a budget.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep covers a wide space within a budget.

### Question 18 — B

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum stops billing between runs. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **B:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum stops billing between runs.
- **C:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.

### Question 19 — A

Answer: Enable MLflow tracking so runs log to the workspace. MLflow records parameters and artifacts per run. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: MLflow records parameters and artifacts per run.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: MLflow records parameters and artifacts per run.

### Question 20 — D

Answer: Point the MLflow tracking URI at the workspace endpoint. The tracking URI must point at the workspace. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: The tracking URI must point at the workspace.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The tracking URI must point at the workspace.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: The tracking URI must point at the workspace.
- **D:** Correct. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. In this case: The tracking URI must point at the workspace.

### Question 21 — D

Answer: Overwrite the existing model version instead of registering a new one. Overwriting destroys the artifact and its audit trail. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Overwriting destroys the artifact and its audit trail.
- **B:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: Overwriting destroys the artifact and its audit trail.
- **C:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: Overwriting destroys the artifact and its audit trail.
- **D:** Correct. Overwriting destroys the previous artifact and the audit trail that rollback depends on. In this case: Overwriting destroys the artifact and its audit trail.

### Question 22 — D

Answer: Tag the registered model with the data asset and commit it came from. Tags carrying data asset and commit allow the rebuild. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: Tags carrying data asset and commit allow the rebuild.
- **B:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carrying data asset and commit allow the rebuild.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Tags carrying data asset and commit allow the rebuild.
- **D:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carrying data asset and commit allow the rebuild.

### Question 23 — D

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports the judgement. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **C:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **D:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports the judgement.

### Question 24 — C

Answer: Configure liveness and readiness probes on the deployment. A readiness probe withholds traffic until the model can serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **B:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe withholds traffic until the model can serve.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.

### Question 25 — B

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact decouples the model version from the image. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **B:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact decouples the model version from the image.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact decouples the model version from the image.

### Question 26 — A

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split bounds exposure to a canary share. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split bounds exposure to a canary share.
- **B:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split bounds exposure to a canary share.

### Question 27 — B

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes withdrawal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes withdrawal a traffic change.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.

### Question 28 — A

Answer: Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale follows load with a deliberate minimum. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale follows load with a deliberate minimum.
- **B:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **C:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale follows load with a deliberate minimum.

### Question 29 — D

Answer: Create an alert rule on the drift and latency metrics. An alert turns the metric into an action. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert turns the metric into an action.
- **B:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert turns the metric into an action.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into an action.
- **D:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into an action.

### Question 30 — D

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.

### Question 31 — A, B

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. The traffic split bounds exposure, and the retained deployment enables reversal. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: The traffic split bounds exposure, and the retained deployment enables reversal.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: The traffic split bounds exposure, and the retained deployment enables reversal.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.

### Question 32 — A, E

Answers: Set autoscale rules on the deployment with a deliberate minimum instance count; Configure liveness and readiness probes on the deployment. Autoscale matches capacity, and probes gate traffic until ready. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity, and probes gate traffic until ready.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **E:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: Autoscale matches capacity, and probes gate traffic until ready.

### Question 33 — B

Answer: Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold. Each step consumes the artifact produced before it, ending with a measured canary. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **B:** Correct. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. In this case: Each step consumes the artifact produced before it, ending with a measured canary.
- **C:** Incorrect for this question. There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **D:** Incorrect for this question. A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.

### Question 34 — C

Answer: Create a Foundry hub and a project per team. A hub shares capacity while a project isolates assets. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **B:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **C:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity while a project isolates assets.
- **D:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity while a project isolates assets.

### Question 35 — B

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput gives predictable cost and latency at sustained volume. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.
- **B:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput gives predictable cost and latency at sustained volume.
- **C:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.

### Question 36 — C

Answer: Author the flow as a directed acyclic graph with typed inputs and outputs. A typed directed acyclic graph makes each node testable. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A typed directed acyclic graph makes each node testable.
- **B:** Incorrect for this question. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Why the correct answer wins: A typed directed acyclic graph makes each node testable.
- **C:** Correct. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. In this case: A typed directed acyclic graph makes each node testable.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A typed directed acyclic graph makes each node testable.

### Question 37 — D

Answer: Store the model credential as a project connection. A project connection holds the endpoint and credential externally. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **D:** Correct. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. In this case: A project connection holds the endpoint and credential externally.

### Question 38 — C

Answer: Assign a managed identity to compute and grant it the storage role. A managed identity removes the credential. A managed identity removes credentials from code entirely and is granted only the role the step needs. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: A managed identity removes the credential.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A managed identity removes the credential.
- **C:** Correct. A managed identity removes credentials from code entirely and is granted only the role the step needs. In this case: A managed identity removes the credential.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A managed identity removes the credential.

### Question 39 — A

Answer: Paste the API key into a Python node inside the flow. A key in a flow file is a secret in source control. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. In this case: A key in a flow file is a secret in source control.
- **B:** Incorrect for this question. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Why the correct answer wins: A key in a flow file is a secret in source control.
- **C:** Incorrect for this question. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Why the correct answer wins: A key in a flow file is a secret in source control.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A key in a flow file is a secret in source control.

### Question 40 — D

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.

### Question 41 — A

Answer: Index the documents in Azure AI Search and query the index from the flow. An index supports retrieval against current content. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: An index supports retrieval against current content.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: An index supports retrieval against current content.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: An index supports retrieval against current content.
- **D:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: An index supports retrieval against current content.

### Question 42 — D

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap make the citation specific. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.
- **C:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.
- **D:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap make the citation specific.

### Question 43 — B

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh aligns retrieval with the source. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **B:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh aligns retrieval with the source.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.

### Question 44 — C

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **C:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate relevant text.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.

### Question 45 — D

Answer: Run the evaluation in continuous integration before the flow is promoted. An offline evaluation gate blocks a regression before promotion. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **C:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **D:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An offline evaluation gate blocks a regression before promotion.

### Question 46 — C

Answer: Keep the prompt in its own file under version control. A versioned prompt file is the change record. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A versioned prompt file is the change record.
- **B:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A versioned prompt file is the change record.
- **C:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the change record.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the change record.

### Question 47 — C

Answer: Register a scoped tool list for the agent. A scoped tool list bounds what the agent may call. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **B:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **C:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds what the agent may call.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A scoped tool list bounds what the agent may call.

### Question 48 — C

Answer: Bound the agent memory to the current session. Session-scoped memory prevents facts crossing conversations. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Typed state makes each handoff explicit and testable instead of relying on free text. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **C:** Correct. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. In this case: Session-scoped memory prevents facts crossing conversations.
- **D:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.

### Question 49 — C, D

Answers: Create a Foundry hub and a project per team; Reference the deployment name from the flow rather than the model family name. A hub with a project per unit isolates assets, and the deployment name keeps flows stable. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A hub with a project per unit isolates assets, and the deployment name keeps flows stable.
- **B:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A hub with a project per unit isolates assets, and the deployment name keeps flows stable.
- **C:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub with a project per unit isolates assets, and the deployment name keeps flows stable.
- **D:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A hub with a project per unit isolates assets, and the deployment name keeps flows stable.
- **E:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub with a project per unit isolates assets, and the deployment name keeps flows stable.

### Question 50 — D, E

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing enables grounding, and document-level access enforces entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **D:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **E:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing enables grounding, and document-level access enforces entitlement.

### Question 51 — A, C

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file is the record, and the offline gate is the control. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **B:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **C:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.

### Question 52 — B

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation build on each other. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **B:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation build on each other.
- **C:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **D:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.

### Question 53 — C

Answer: Use an LLM judge with a rubric, calibrated against human grades. An LLM judge calibrated against human grades scales the grading. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **B:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **C:** Correct. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. In this case: An LLM judge calibrated against human grades scales the grading.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.

### Question 54 — C

Answer: Score coherence for logical structure. Coherence measures whether the answer holds together logically. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **C:** Correct. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. In this case: Coherence measures whether the answer holds together logically.
- **D:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Coherence measures whether the answer holds together logically.

### Question 55 — C

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **C:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.
- **D:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.

### Question 56 — C

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing attributes the failure to a specific retrieval or generation stage. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing attributes the failure to a specific retrieval or generation stage.
- **B:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing attributes the failure to a specific retrieval or generation stage.
- **C:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing attributes the failure to a specific retrieval or generation stage.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing attributes the failure to a specific retrieval or generation stage.

### Question 57 — A

Answer: Disable request logging to reduce storage cost. Disabling logging removes the evidence an investigation needs and usually breaches policy. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. In this case: Disabling logging removes the evidence an investigation needs and usually breaches policy.
- **B:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Disabling logging removes the evidence an investigation needs and usually breaches policy.
- **C:** Incorrect for this question. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Why the correct answer wins: Disabling logging removes the evidence an investigation needs and usually breaches policy.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Disabling logging removes the evidence an investigation needs and usually breaches policy.

### Question 58 — A

Answer: Run continuous evaluation on sampled production traffic. Continuous evaluation on sampled traffic catches what a fixed dataset cannot. Online evaluation catches the drift that a fixed offline dataset cannot represent. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Online evaluation catches the drift that a fixed offline dataset cannot represent. In this case: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **B:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **C:** Incorrect for this question. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Continuous evaluation on sampled traffic catches what a fixed dataset cannot.

### Question 59 — D, E

Answers: Score groundedness against the retrieved passages; Score relevance of the answer to the question asked. Groundedness measures support, and relevance measures whether the question was answered. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **C:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **D:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **E:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support, and relevance measures whether the question was answered.

### Question 60 — A, C

Answers: Test indirect injection through retrieved documents; Run adversarial jailbreak and prompt-injection cases before release. Indirect cases test retrieved content, and jailbreak cases test user input. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **B:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **C:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **E:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.

### Question 61 — B, E

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing identifies the stage, and prompt logging permits replay. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **B:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing identifies the stage, and prompt logging permits replay.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **E:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing identifies the stage, and prompt logging permits replay.

### Question 62 — C

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **B:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **C:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **D:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.

### Question 63 — B

Answer: Set a time-to-live on the cache. A TTL stops a cached answer outliving its source. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **B:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A TTL stops a cached answer outliving its source.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A TTL stops a cached answer outliving its source.

### Question 64 — C

Answer: Add a router that classifies the request and selects a model. A router selects a model appropriate to the request. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects a model appropriate to the request.
- **B:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router selects a model appropriate to the request.
- **C:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects a model appropriate to the request.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects a model appropriate to the request.

### Question 65 — C

Answer: Use the largest model for every request. The largest model adds cost where its capability is not needed. The largest model adds cost and latency to requests that do not need its capability. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: The largest model adds cost where its capability is not needed.
- **B:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: The largest model adds cost where its capability is not needed.
- **C:** Correct. The largest model adds cost and latency to requests that do not need its capability. In this case: The largest model adds cost where its capability is not needed.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: The largest model adds cost where its capability is not needed.

### Question 66 — B

Answer: Set a request timeout with a bounded retry and backoff. A bounded timeout with backoff stops a failing dependency amplifying load. A bounded retry with backoff stops a failing dependency from multiplying load. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **B:** Correct. A bounded retry with backoff stops a failing dependency from multiplying load. In this case: A bounded timeout with backoff stops a failing dependency amplifying load.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **D:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.

### Question 67 — D

Answer: Compress the system prompt and remove redundant instructions. Compressing the prompt cuts input tokens on every call. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **D:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Compressing the prompt cuts input tokens on every call.

### Question 68 — A

Answer: Fine-tune on approved examples to shorten the standing prompt. Fine-tuning can move stable instructions into the weights. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. In this case: Fine-tuning can move stable instructions into the weights.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **C:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.

### Question 69 — B

Answer: Move steady traffic to provisioned throughput. Provisioned throughput lowers cost per token at sustained volume. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **B:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Provisioned throughput lowers cost per token at sustained volume.
- **C:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.

### Question 70 — A, E

Answers: Measure tokens per request and set a budget per endpoint; Set a time-to-live on the cache. A token budget attributes cost, and a TTL keeps answers current. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: A token budget attributes cost, and a TTL keeps answers current.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **E:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A token budget attributes cost, and a TTL keeps answers current.

### Question 71 — A, D

Answers: Add a router that classifies the request and selects a model; Route simple requests to a smaller model. A router selects per request, and a smaller model covers the simple majority. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A router selects per request, and a smaller model covers the simple majority.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects per request, and a smaller model covers the simple majority.
- **E:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.

### Question 72 — D

Answer: Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held. Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Evaluation precedes both the change it would validate and the measurement that motivates it. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **B:** Incorrect for this question. An optimization is applied before anything has been measured or attributed. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **C:** Incorrect for this question. A driver is named before measurement, and the evaluation runs before the change exists. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **D:** Correct. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. In this case: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.

### Question 73 — D

Answer: Register the data as a versioned data asset. A versioned data asset records the exact input used. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned data asset records the exact input used.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A versioned data asset records the exact input used.
- **C:** Incorrect for this question. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Why the correct answer wins: A versioned data asset records the exact input used.
- **D:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A versioned data asset records the exact input used.

### Question 74 — B, C

Answers: Pass environment values through a Bicep parameter file per stage; Define the workspace in a Bicep module deployed per environment. The module defines the shape, and a parameter file per region holds the values. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: The module defines the shape, and a parameter file per region holds the values.
- **B:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: The module defines the shape, and a parameter file per region holds the values.
- **C:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: The module defines the shape, and a parameter file per region holds the values.
- **D:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: The module defines the shape, and a parameter file per region holds the values.
- **E:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: The module defines the shape, and a parameter file per region holds the values.

### Question 75 — B

Answer: Use automated ML to establish the tabular baseline. Automated ML produces a baseline quickly across preprocessing and algorithm combinations. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML produces a baseline quickly across preprocessing and algorithm combinations.
- **B:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML produces a baseline quickly across preprocessing and algorithm combinations.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML produces a baseline quickly across preprocessing and algorithm combinations.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML produces a baseline quickly across preprocessing and algorithm combinations.

### Question 76 — D

Answer: Group the trials under a named experiment. A named experiment groups runs so variants compare against each other. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **C:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **D:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups runs so variants compare against each other.

### Question 77 — A

Answer: Register the model and always deploy whichever version is latest. An explicit model version pins what is served. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Deploying whatever is latest lets an untested registration reach production with no promotion gate. In this case: An explicit model version pins what is served.
- **B:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: An explicit model version pins what is served.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An explicit model version pins what is served.
- **D:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: An explicit model version pins what is served.

### Question 78 — C

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 79 — B

Answer: Deploy to a managed online endpoint with an explicit model version. A managed online endpoint serves synchronous requests. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **B:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: A managed online endpoint serves synchronous requests.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **D:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: A managed online endpoint serves synchronous requests.

### Question 80 — A, B

Answers: Deploy a batch endpoint for the overnight scoring job; Keep the previous deployment in place so traffic can be moved back. A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal. A batch endpoint scores a large file on a schedule and needs no always-on capacity. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **C:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **E:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.

### Question 81 — D, E

Answers: Register each candidate with a version and deploy one explicit version; Attach a description, metrics, and intended use to the model version. An explicit version pins the artifact, and the model card documents its intended use. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit version pins the artifact, and the model card documents its intended use.
- **B:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: An explicit version pins the artifact, and the model card documents its intended use.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit version pins the artifact, and the model card documents its intended use.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit version pins the artifact, and the model card documents its intended use.
- **E:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: An explicit version pins the artifact, and the model card documents its intended use.

### Question 82 — A

Answer: Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress. A second deployment preserves the incumbent for measurement and for the rollback itself. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. In this case: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **B:** Incorrect for this question. There is nothing to compare before the candidate exists and is receiving traffic. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **C:** Incorrect for this question. All traffic is shifted before the candidate is deployed, and the comparison comes after the exposure it was meant to prevent. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **D:** Incorrect for this question. Replacing the incumbent destroys the comparison baseline and the thing you would roll back to. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.

### Question 83 — B

Answer: Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration. Measurement and forecasting precede the commercial comparison, and the load test validates it. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The forecast is made without a measurement baseline, and the commitment precedes the measurement entirely. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **B:** Correct. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. In this case: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **C:** Incorrect for this question. Capacity is committed before the demand that justifies it has been measured. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **D:** Incorrect for this question. A load test needs a configuration chosen from the measurement and forecast, both of which come later. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.

### Question 84 — D

Answer: Confirm the workload is not interactive → prepare a batch input dataset → submit the batch endpoint job → validate the output file against the schema. The interaction requirement decides the pattern, input precedes submission, and output is validated after. The interaction requirement decides the pattern, the input must exist before submission, and the output is validated afterwards. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A batch job is submitted before its input exists and before anyone confirmed batch is the right pattern. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and output is validated after.
- **B:** Incorrect for this question. Validation happens before submission, so there is no output to check. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and output is validated after.
- **C:** Incorrect for this question. The output is validated before the job that produces it has run. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and output is validated after.
- **D:** Correct. The interaction requirement decides the pattern, the input must exist before submission, and the output is validated afterwards. In this case: The interaction requirement decides the pattern, input precedes submission, and output is validated after.

### Question 85 — D

Answer: Run the flow as a batch job over the evaluation dataset. A batch run applies the flow to every row of the dataset. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Deploying the flow exposes it as a service the application can call. Why the correct answer wins: A batch run applies the flow to every row of the dataset.
- **B:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A batch run applies the flow to every row of the dataset.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch run applies the flow to every row of the dataset.
- **D:** Correct. A batch run applies the flow to every row, which is how an evaluation dataset is scored. In this case: A batch run applies the flow to every row of the dataset.

### Question 86 — C

Answer: Create a variant to compare two prompt strategies side by side. Variants hold the alternatives together for a reproducible comparison. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.
- **B:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.
- **C:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: Variants hold the alternatives together for a reproducible comparison.
- **D:** Incorrect for this question. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.

### Question 87 — A

Answer: Score fluency for readability and language quality. Fluency measures readability, not factual support. Fluency measures readability and language quality, not factual support. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Fluency measures readability and language quality, not factual support. In this case: Fluency measures readability, not factual support.
- **B:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Fluency measures readability, not factual support.
- **C:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Fluency measures readability, not factual support.
- **D:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Fluency measures readability, not factual support.

### Question 88 — A

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.

### Question 89 — D

Answer: Start on pay-as-you-go while the volume is still unknown. Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **B:** Incorrect for this question. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **D:** Correct. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. In this case: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.

### Question 90 — B

Answer: Use a few hundred representative cases rather than a dozen. A set that small cannot separate a real gain from noise. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **B:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: A set that small cannot separate a real gain from noise.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A set that small cannot separate a real gain from noise.

### Question 91 — A

Answer: Cache identical requests and reuse the completion. Caching removes repeated inference for identical input. Caching removes repeated inference for identical input, which is the cheapest saving available. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Caching removes repeated inference for identical input, which is the cheapest saving available. In this case: Caching removes repeated inference for identical input.
- **B:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Caching removes repeated inference for identical input.
- **C:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Caching removes repeated inference for identical input.
- **D:** Incorrect for this question. A TTL keeps a cached answer from outliving the content it came from. Why the correct answer wins: Caching removes repeated inference for identical input.

### Question 92 — A

Answer: Promote versions through aliases such as candidate and production. An alias pointer lets promotion and withdrawal move without editing deployments. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. In this case: An alias pointer lets promotion and withdrawal move without editing deployments.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An alias pointer lets promotion and withdrawal move without editing deployments.
- **C:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An alias pointer lets promotion and withdrawal move without editing deployments.
- **D:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: An alias pointer lets promotion and withdrawal move without editing deployments.

### Question 93 — B

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes reversal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes reversal a traffic change.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes reversal a traffic change.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes reversal a traffic change.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes reversal a traffic change.

### Question 94 — B, C

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing attributes failures to a stage, and prompt logging supports reproduction. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing attributes failures to a stage, and prompt logging supports reproduction.
- **B:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing attributes failures to a stage, and prompt logging supports reproduction.
- **C:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing attributes failures to a stage, and prompt logging supports reproduction.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing attributes failures to a stage, and prompt logging supports reproduction.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing attributes failures to a stage, and prompt logging supports reproduction.

### Question 95 — A

Answer: Fine-tune the model on the document set instead of retrieving. Fine-tuning copies a snapshot into the model and breaches the licence's storage terms. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. In this case: Fine-tuning copies a snapshot into the model and breaches the licence's storage terms.
- **B:** Incorrect for this question. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Why the correct answer wins: Fine-tuning copies a snapshot into the model and breaches the licence's storage terms.
- **C:** Incorrect for this question. Document-level access keeps retrieval within what the requesting user is allowed to see. Why the correct answer wins: Fine-tuning copies a snapshot into the model and breaches the licence's storage terms.
- **D:** Incorrect for this question. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Why the correct answer wins: Fine-tuning copies a snapshot into the model and breaches the licence's storage terms.

### Question 96 — A

Answer: Connect to the source through a federated connector and query it in place. A federated connector queries the source in place without copying it. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. In this case: A federated connector queries the source in place without copying it.
- **B:** Incorrect for this question. Copying a licensed corpus into an index you host is a storage and licence decision, not just a connector setting. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **C:** Incorrect for this question. Exporting licensed content into your own storage is the step the licence usually forbids, so the copy itself is the risk. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A federated connector queries the source in place without copying it.

### Question 97 — A

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.

### Question 98 — D

Answer: Build a versioned curated environment for the job. A versioned curated environment fixes the package set for that rebuild. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment fixes the package set for that rebuild.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment fixes the package set for that rebuild.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned curated environment fixes the package set for that rebuild.
- **D:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment fixes the package set for that rebuild.

### Question 99 — D

Answer: Run the whole workflow as a single script job. Separate pipeline steps make the failing stage visible and rerunnable. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Separate pipeline steps make the failing stage visible and rerunnable.
- **B:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: Separate pipeline steps make the failing stage visible and rerunnable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Separate pipeline steps make the failing stage visible and rerunnable.
- **D:** Correct. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. In this case: Separate pipeline steps make the failing stage visible and rerunnable.

### Question 100 — D

Answer: Use a quantized deployment for the high-throughput tier. Quantization reduces memory and can raise throughput per unit of capacity. Quantization reduces memory and can raise throughput per unit of capacity at some quality cost. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Quantization reduces memory and can raise throughput per unit of capacity.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Quantization reduces memory and can raise throughput per unit of capacity.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Quantization reduces memory and can raise throughput per unit of capacity.
- **D:** Correct. Quantization reduces memory and can raise throughput per unit of capacity at some quality cost. In this case: Quantization reduces memory and can raise throughput per unit of capacity.
