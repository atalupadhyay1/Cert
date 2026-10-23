# Microsoft AI-300 — Full-Length Mock Exam 6

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A holding company must prove that one unit's experiments cannot alter another unit's production assets. What provides that boundary?

Domain: Design and implement an MLOps infrastructure

- A. Create a separate Azure Machine Learning workspace per environment
- B. Create the workspace in the portal and record the steps in a wiki
- C. Attach a GPU cluster with four always-on nodes
- D. Use one workspace for development, test, and production

### 2. A group audit asks how jobs reach storage without credentials in code. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Register a datastore that points at the storage account
- B. Print the metrics to the job log and read them from the console
- C. Register the data as a versioned data asset
- D. Reference the storage path with the account key inline in the job YAML

### 3. A model approved last quarter cannot be rebuilt because dependencies resolved differently. What should have been pinned?

Domain: Design and implement an MLOps infrastructure

- A. Reference the floating latest tag for the environment image
- B. Disable request logging to reduce storage cost
- C. Print the metrics to the job log and read them from the console
- D. Build a versioned curated environment for the job

### 4. An auditor asks which dataset trained a model approved two years ago. What should have been registered?

Domain: Design and implement an MLOps infrastructure

- A. Reference the storage path with the account key inline in the job YAML
- B. Disable request logging to reduce storage cost
- C. Register the data as a versioned data asset
- D. Register a datastore that points at the storage account

### 5. Every unit must define its environment in a reviewable artifact. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Define the workspace in a Bicep module deployed per environment
- B. Export an ARM template from the portal after building it by hand
- C. Rebuild the environment by hand from the notes in the ticket
- D. Create the workspace in the portal and record the steps in a wiki

### 6. One module must deploy to four units with different names and capacity. What should hold the differences?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Pass environment values through a Bicep parameter file per stage
- C. Rebuild the environment by hand from the notes in the ticket
- D. Export an ARM template from the portal after building it by hand

### 7. Resources added by hand outside the template were never removed. What should be deployed as?

Domain: Design and implement an MLOps infrastructure

- A. Deploy the module as a deployment stack so removed resources are cleaned up
- B. Keep public network access enabled so notebooks connect easily
- C. Assign the work to a person instead of investigating the failure
- D. Create the workspace in the portal and record the steps in a wiki

### 8. A group standard requires every training run to be reproducible from a command. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Submit the job with az ml job create --file job.yaml
- C. Run the job from a compute instance notebook
- D. Stream the job with az ml job stream to inspect logs

### 9. No unit may store a long-lived credential in its repository. What should authenticate deployments?

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Authenticate the workflow with workload identity federation and no stored secret
- C. Store a service principal client secret as a GitHub repository secret
- D. Set the connection string as a plain environment variable in the job

### 10. A group change board must approve any production release. What should be configured?

Domain: Design and implement an MLOps infrastructure

- A. Store a service principal client secret as a GitHub repository secret
- B. Run the pipeline from a GitHub Actions workflow on merge to main
- C. Use GitHub environment protection rules to gate the production deploy job
- D. Fan the tests out across a matrix of dependency versions

### 11. A decision must be traceable to the exact model that produced it. What pins the artifact?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Overwrite the existing model version instead of registering a new one
- C. Register each candidate with a version and deploy one explicit version
- D. Register the model and always deploy whichever version is latest

### 12. Promotion must move a pointer rather than edit each deployment. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Register the model and always deploy whichever version is latest
- B. Overwrite the existing model version instead of registering a new one
- C. Register each candidate with a version and deploy one explicit version
- D. Promote versions through aliases such as candidate and production

### 13. Regulated content may not traverse the public internet. What must the workspace use?

Domain: Design and implement an MLOps infrastructure

- A. Place a private endpoint on the workspace and its storage
- B. Keep public network access enabled so notebooks connect easily
- C. Set the connection string as a plain environment variable in the job
- D. Reference the storage path with the account key inline in the job YAML

### 14. Group policy requires a connection string to rotate without touching code. Where should it live?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Reference the storage path with the account key inline in the job YAML
- C. Set the connection string as a plain environment variable in the job
- D. Store connection strings in Key Vault and reference them by name

### 15. A group standard requires reproducible environments with no manual drift. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Rebuild the environment by hand from the notes in the ticket
- C. Deploy the module as a deployment stack so removed resources are cleaned up
- D. Export an ARM template from the portal after building it by hand
- E. Define the workspace in a Bicep module deployed per environment

### 16. A release must be secret-free and gated by an approver. Which two controls apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Authenticate the workflow with workload identity federation and no stored secret
- C. Fan the tests out across a matrix of dependency versions
- D. Use GitHub environment protection rules to gate the production deploy job
- E. Store a service principal client secret as a GitHub repository secret

### 17. An audit asks which data fed the evaluation that approved a model. What provides that record?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Run the job from a compute instance notebook
- C. Assign the work to a person instead of investigating the failure
- D. Run the whole workflow as a single script job

### 18. One script hides which stage failed and forces a full rerun to recover. What should replace it?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Assign the work to a person instead of investigating the failure
- C. Define the steps as a pipeline job with explicit inputs and outputs
- D. Run the whole workflow as a single script job

### 19. A tuning run must fit a fixed compute budget across a wide space. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Run a full grid sweep over every combination
- C. Increase the model size until the answers improve
- D. Use automated ML to establish the tabular baseline

### 20. Thirty-two combinations ran at full overhead and the tuning bill blew the project budget. What should have been used?

Domain: Implement machine learning model lifecycle and operations

- A. Increase the model size until the answers improve
- B. Run a full grid sweep over every combination
- C. Run a sweep job over a searched hyperparameter space
- D. Retrain the model on the newer data

### 21. A first tabular model is needed within a week as a defensible baseline. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Run the whole workflow as a single script job
- B. Use automated ML to establish the tabular baseline
- C. Run the job from a compute instance notebook
- D. Run a sweep job over a searched hyperparameter space

### 22. Training runs intermittently and accelerators bill overnight. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Attach a CPU compute cluster for the data preparation step
- C. Attach a GPU cluster with a minimum of zero nodes
- D. Attach a GPU cluster with four always-on nodes

### 23. Runs are logged on a laptop and never reach the shared experiment list. What is misconfigured?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Run the job from a compute instance notebook
- C. Disable request logging to reduce storage cost
- D. Point the MLflow tracking URI at the workspace endpoint

### 24. Nine hundred runs share one list and three variants cannot be compared. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Disable request logging to reduce storage cost
- B. Enable MLflow tracking so runs log to the workspace
- C. Print the metrics to the job log and read them from the console
- D. Group the trials under a named experiment

### 25. A registry entry was replaced in place, so the approved decision can no longer be rebuilt. What was the error?

Domain: Implement machine learning model lifecycle and operations

- A. Register each candidate with a version and deploy one explicit version
- B. Overwrite the existing model version instead of registering a new one
- C. Tag the registered model with the data asset and commit it came from
- D. Assign the work to a person instead of investigating the failure

### 26. A reviewer must judge whether a version is suitable before promotion. What should it carry?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Register the model and always deploy whichever version is latest
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Attach a description, metrics, and intended use to the model version

### 27. An auditor must rebuild a model approved eighteen months ago. What must registration record?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Overwrite the existing model version instead of registering a new one
- C. Print the metrics to the job log and read them from the console
- D. Attach a description, metrics, and intended use to the model version

### 28. An application needs a synchronous decision for a single request. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Run the job from a compute instance notebook
- C. Deploy to a managed online endpoint with an explicit model version
- D. Deploy a batch endpoint for the overnight scoring job

### 29. Every candidate needs a container build before anyone can test it. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Bake the model weights into the container image
- C. Mount the model artifact rather than baking it into the image
- D. Replace the production deployment in a single step

### 30. A container errors for two minutes after start while weights load. What should be added?

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Deploy without probes and rely on the platform health check
- C. Configure liveness and readiness probes on the deployment
- D. Monitor only the accuracy reported at deployment time

### 31. Nine hundred thousand records must be scored inside a single overnight window. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy to a managed online endpoint with an explicit model version
- B. Send the overnight file through the online endpoint request by request
- C. Deploy a batch endpoint for the overnight scoring job
- D. Run the job from a compute instance notebook

### 32. A new version may affect at most a small share of requests before measurement. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy straight to production to save a day
- B. Replace the production deployment in a single step
- C. Keep the previous deployment in place so traffic can be moved back
- D. Split endpoint traffic 10/90 so the new deployment receives a canary share

### 33. A release must be reversible within minutes. What must exist?

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Bake the model weights into the container image
- C. Keep the previous deployment in place so traffic can be moved back
- D. Replace the production deployment in a single step

### 34. Load peaks for two hours and idles for sixteen. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Set autoscale rules on the deployment with a deliberate minimum instance count
- B. Deploy without probes and rely on the platform health check
- C. Send the overnight file through the online endpoint request by request
- D. Pin a fixed instance count for a spiky workload

### 35. Input distributions shifted after a process change and nobody noticed. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Enable data drift monitoring against the training baseline
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Monitor only the accuracy reported at deployment time
- D. Retrain the model on the newer data

### 36. A drift report is filed monthly and read only after something breaks. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Disable request logging to reduce storage cost
- C. Create an alert rule on the drift and latency metrics
- D. Monitor only the accuracy reported at deployment time

### 37. An audit needs step-level lineage and a pinned artifact. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Run the whole workflow as a single script job
- C. Define the steps as a pipeline job with explicit inputs and outputs
- D. Register each candidate with a version and deploy one explicit version
- E. Register the model and always deploy whichever version is latest

### 38. A reviewer needs provenance and documented intended use. Which two artifacts apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Attach a description, metrics, and intended use to the model version
- C. Register the model and always deploy whichever version is latest
- D. Overwrite the existing model version instead of registering a new one
- E. Accept the behaviour because the aggregate score still looks healthy

### 39. A release must be bounded and reversible. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one
- E. Bake the model weights into the container image

### 40. An endpoint must survive bursts and not serve before the model loads. Which two configurations apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Deploy without probes and rely on the platform health check
- C. Configure liveness and readiness probes on the deployment
- D. Pin a fixed instance count for a spiky workload
- E. Set autoscale rules on the deployment with a deliberate minimum instance count

### 41. A release must stay reversible throughout rollout. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Replace the incumbent deployment → compare error rate and latency → deploy the new version to a second deployment → send traffic to it
- B. Compare error rate and latency → deploy the new version → send a small traffic share → replace the incumbent
- C. Send all traffic to the new deployment → deploy the new version → compare metrics → move traffic back
- D. Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress

### 42. A model degraded after an upstream change. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Compare distributions → identify the upstream source → detect the drop → retrain on refreshed data
- B. Identify the upstream source → retrain → detect the drop → compare distributions
- C. Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate
- D. Retrain on refreshed data → detect the drop → compare distributions → promote through the gate

### 43. Four units need shared capacity but separate assets and connections. What should be created?

Domain: Design and implement a GenAIOps infrastructure

- A. Use one workspace for development, test, and production
- B. Give every team one project and one shared connection
- C. Create the workspace in the portal and record the steps in a wiki
- D. Create a Foundry hub and a project per team

### 44. A flow broke when the model family behind its deployment was swapped. What should the flow call?

Domain: Design and implement a GenAIOps infrastructure

- A. Select a model from the catalog and deploy it into the project
- B. Reference the deployment name from the flow rather than the model family name
- C. Hardcode the model family name inside the flow
- D. Paste the API key into a Python node inside the flow

### 45. A steady workload runs at predictable volume all day. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Pin a fixed instance count for a spiky workload
- B. Use the largest model for every request
- C. Start on pay-as-you-go while the volume is still unknown
- D. Reserve provisioned throughput for the steady high-volume workload

### 46. A pilot may end after a quarter and its volume is unpredictable. What fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Pin a fixed instance count for a spiky workload
- B. Use the largest model for every request
- C. Start on pay-as-you-go while the volume is still unknown
- D. Reserve provisioned throughput for the steady high-volume workload

### 47. A group standard requires harm thresholds on prompts and completions. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Apply a content filter policy appropriate to the audience
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Evaluate toxicity against the threshold the audience requires
- D. Accept the behaviour because the aggregate score still looks healthy

### 48. A flow must be tested node by node before release. What should it be authored as?

Domain: Design and implement a GenAIOps infrastructure

- A. Run the job from a compute instance notebook
- B. Author the flow as a directed acyclic graph with typed inputs and outputs
- C. Run the whole workflow as a single script job
- D. Run the flow as a batch job over the evaluation dataset

### 49. Two prompt strategies must be compared on the same cases. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Author the flow as a directed acyclic graph with typed inputs and outputs
- B. Create a variant to compare two prompt strategies side by side
- C. Hardcode the model family name inside the flow
- D. Rewrite the prompt and deploy it immediately

### 50. A flow must call its model endpoint with no credential stored in the file. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Store the model credential as a project connection
- C. Set the connection string as a plain environment variable in the job
- D. Reference the storage path with the account key inline in the job YAML

### 51. A key was pasted into a node and merged with the flow. What is the defect?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Store connection strings in Key Vault and reference them by name
- C. Set the connection string as a plain environment variable in the job
- D. Store the model credential as a project connection

### 52. Policy wording changes monthly and every answer must cite the current version. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Index the documents in Azure AI Search and query the index from the flow
- B. Index every document the organization holds
- C. Fine-tune the model on the document set instead of retrieving
- D. Increase the model size until the answers improve

### 53. One index serves four units and each user may see only their own documents. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Keep public network access enabled so notebooks connect easily
- C. Set the connection string as a plain environment variable in the job
- D. Set document-level access in the index so retrieval respects entitlements

### 54. A policy update was published last week and answers still quote the old text. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Index every document the organization holds
- D. Rebuild the index on a schedule after the source content changes

### 55. Retrieval returns an entire manual and the model quotes an unrelated section. What caused it?

Domain: Design and implement a GenAIOps infrastructure

- A. Index each document as one large chunk
- B. Chunk documents by section with a small overlap
- C. Index every document the organization holds
- D. Retrain the model on the newer data

### 56. A group standard requires a change record for every prompt edit. Where should prompts live?

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Paste the API key into a Python node inside the flow
- C. Keep the prompt in its own file under version control
- D. Create a variant to compare two prompt strategies side by side

### 57. No prompt change may reach production until quality is measured. What should be in place?

Domain: Design and implement a GenAIOps infrastructure

- A. Deploy straight to production to save a day
- B. Assign the work to a person instead of investigating the failure
- C. Rewrite the prompt and deploy it immediately
- D. Run the evaluation in continuous integration before the flow is promoted

### 58. A platform team must isolate assets per unit and keep flows stable across model swaps. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Reference the deployment name from the flow rather than the model family name
- C. Paste the API key into a Python node inside the flow
- D. Give every team one project and one shared connection
- E. Create a Foundry hub and a project per team

### 59. An assistant must ground on current documents and respect entitlements. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Set document-level access in the index so retrieval respects entitlements
- C. Keep public network access enabled so notebooks connect easily
- D. Index the documents in Azure AI Search and query the index from the flow
- E. Fine-tune the model on the document set instead of retrieving

### 60. A prompt change needs a record and a quality gate. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Keep the prompt in its own file under version control
- C. Deploy straight to production to save a day
- D. Run the evaluation in continuous integration before the flow is promoted
- E. Rewrite the prompt and deploy it immediately

### 61. A flow needs access to several sources without secrets. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Grant the identity Owner on each source → inventory the data sources → verify the answer → assign a managed identity
- B. Assign the identity → verify the answer → inventory the sources → grant the role
- C. Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content
- D. Verify a grounded answer → assign the identity → grant the role → inventory the sources

### 62. A grounded assistant must be built from source documents. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents
- B. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- C. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness
- D. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them

### 63. A regulator asks what the evaluation was measured on. What should the set contain?

Domain: Implement generative AI quality assurance and observability

- A. Generate the evaluation set from the prompt itself
- B. Build the evaluation dataset from real queries with graded answers
- C. Assign the work to a person instead of investigating the failure
- D. Accept the behaviour because the aggregate score still looks healthy

### 64. A twenty-case set moved from 0.72 to 0.79 and the team wants to declare a win. What is the objection?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Use a few hundred representative cases rather than a dozen
- C. Retrain the model on the newer data
- D. Generate the evaluation set from the prompt itself

### 65. An answer faithfully summarizes a passage about a different product. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score relevance of the answer to the question asked
- C. Score fluency for readability and language quality
- D. Score similarity against a reference answer

### 66. A retrieved document contains text instructing the assistant to ignore its rules. What is the exposure?

Domain: Implement generative AI quality assurance and observability

- A. Evaluate toxicity against the threshold the audience requires
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Disable request logging to reduce storage cost
- D. Test indirect injection through retrieved documents

### 67. A disputed answer must be attributed to retrieval or generation. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Enable distributed tracing and log the retrieval and model spans
- C. Log prompts and completions against the trace, within data policy
- D. Rely on the LLM judge without checking it against human grades

### 68. An answer must be replayable within the retention window. What must have been captured?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Log prompts and completions against the trace, within data policy
- C. Disable request logging to reduce storage cost
- D. Enable distributed tracing and log the retrieval and model spans

### 69. Users downvote a class of answers the dataset does not contain. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Capture user feedback and review a sample of rated conversations weekly
- B. Run continuous evaluation on sampled production traffic
- C. Rely on the LLM judge without checking it against human grades
- D. Run the evaluation in continuous integration before the flow is promoted

### 70. A released answer must be supported and on point. Which two metrics apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Score relevance of the answer to the question asked
- B. Score fluency for readability and language quality
- C. Score similarity against a reference answer
- D. Score coherence for logical structure
- E. Score groundedness against the retrieved passages

### 71. An assistant reads external documents and must resist override attempts from users and documents. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Evaluate toxicity against the threshold the audience requires
- D. Disable request logging to reduce storage cost
- E. Test indirect injection through retrieved documents

### 72. A disputed answer must be diagnosable later and reproducible from the log. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Enable distributed tracing and log the retrieval and model spans
- B. Rely on the LLM judge without checking it against human grades
- C. Disable request logging to reduce storage cost
- D. Assign the work to a person instead of investigating the failure
- E. Log prompts and completions against the trace, within data policy

### 73. A safety lead must prove an assistant resists harmful and injected instructions. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Run the adversarial evaluation → configure the content filter → assemble the cases → monitor the rates
- B. Assemble jailbreak and injection cases → configure the content filter and system prompt → run the adversarial evaluation → monitor the filtered and blocked rates in production
- C. Monitor the blocked rates in production → assemble the cases → configure the filter → run the evaluation
- D. Configure the content filter → run the adversarial evaluation → assemble the cases → monitor the rates

### 74. A wrong answer was escalated and the team must explain it. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- B. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set
- C. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set
- D. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set

### 75. The CFO cannot attribute model spend to a workload. What must be measured first?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Use the largest model for every request
- D. Measure tokens per request and set a budget per endpoint

### 76. One endpoint serves both quick lookups and long analyses. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Route simple requests to a smaller model
- C. Add a router that classifies the request and selects a model
- D. Cache identical requests and reuse the completion

### 77. Users wait eight seconds before any text appears although the answer completes in ten. What should change?

Domain: Optimize generative AI systems and model performance

- A. Move non-urgent generation into a batch run
- B. Cache identical requests and reuse the completion
- C. Set a request timeout with a bounded retry and backoff
- D. Stream the response so the first token arrives sooner

### 78. A stalled dependency causes retries to multiply load. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Use the largest model for every request
- C. Set a request timeout with a bounded retry and backoff
- D. Stream the response so the first token arrives sooner

### 79. Sixteen passages come back per answer and most are irrelevant. What should change?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Raise retrieval depth to the maximum for safety
- C. Retrieve fewer but better-ranked passages
- D. Index every document the organization holds

### 80. A 6,000-token system prompt ships on every call and much of it repeats. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Raise retrieval depth to the maximum for safety
- B. Increase the model size until the answers improve
- C. Cache identical requests and reuse the completion
- D. Compress the system prompt and remove redundant instructions

### 81. A cheaper model variant was proposed and nobody measured whether answers stayed correct. What is required?

Domain: Optimize generative AI systems and model performance

- A. Re-run the evaluation after the cost optimization
- B. Retrain the model on the newer data
- C. Increase the model size until the answers improve
- D. Ship the optimization and watch the support queue

### 82. Steady volume for twelve months justifies a lower unit cost. What should be adopted?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Move steady traffic to provisioned throughput
- C. Start on pay-as-you-go while the volume is still unknown
- D. Cache identical requests and reuse the completion

### 83. Overnight bulk generation needs no interactive response. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Set a request timeout with a bounded retry and backoff
- C. Move non-urgent generation into a batch run
- D. Stream the response so the first token arrives sooner

### 84. A group needs attributable spend and current answers. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Cache identical requests and reuse the completion
- C. Use the largest model for every request
- D. Set a time-to-live on the cache
- E. Measure tokens per request and set a budget per endpoint

### 85. A group workload must cost less while hard cases keep their current quality. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Retrain the model on the newer data
- C. Add a router that classifies the request and selects a model
- D. Route simple requests to a smaller model
- E. Use the largest model for every request

### 86. A group must cut model spend without losing quality. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver
- B. Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held
- C. Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization
- D. Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver

### 87. A platform team must size an assistant before peak season. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Reserve provisioned throughput → measure the request rate → forecast the load → load test the configuration
- B. Load test the configuration → reserve provisioned throughput → forecast the load → measure the request rate
- C. Forecast the peak load → reserve provisioned throughput → measure the current rate → load test
- D. Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration

### 88. A unit must rebuild a model approved last year exactly as approved. Which two practices make that possible? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Build a versioned curated environment for the job
- B. Reference the floating latest tag for the environment image
- C. Disable request logging to reduce storage cost
- D. Register the data as a versioned data asset
- E. Reference the storage path with the account key inline in the job YAML

---

## Case study — Evergreen Pharma

Evergreen Pharma runs a medical-information assistant that summarizes approved product documentation for field staff. The assistant must never answer outside approved content, must cite the document and revision it used, and must be evaluated before every release because promotional material is regulated. The company has a validated quality process that requires a documented change record for each model or prompt change. Field staff have asked for faster answers, and the current release cycle takes three weeks because evaluation is run by hand.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Promotional summaries must be supported by approved documentation. Which metric governs release?

Domain: Implement generative AI quality assurance and observability

- A. Score coherence for logical structure
- B. Score fluency for readability and language quality
- C. Score groundedness against the retrieved passages
- D. Score relevance of the answer to the question asked

### 90. A document revision is published and the assistant quotes the previous one. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Index every document the organization holds
- C. Rebuild the index on a schedule after the source content changes
- D. Chunk documents by section with a small overlap

### 91. A validated process needs a change record and a quality gate. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Deploy straight to production to save a day
- C. Run the evaluation in continuous integration before the flow is promoted
- D. Keep the prompt in its own file under version control
- E. Assign the work to a person instead of investigating the failure

---

## Case study — Lakeshore Council

Lakeshore Council runs a public-facing assistant that answers questions about services, permits, and bin collection. The council's content team updates pages weekly, and residents have reported answers based on guidance that was replaced after a service change. The council must publish an accessibility statement and must not return content that the requesting user could not access in the source system. A local journalist has begun testing the assistant with adversarial prompts and publishing the results.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The council was audited a year ago and must now show whether the model still fits current claims. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Enable data drift monitoring against the training baseline
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Retrain the model on the newer data
- D. Monitor only the accuracy reported at deployment time

### 93. A benefits model must be withdrawn within an hour if a defect is confirmed. What makes withdrawal a single change?

Domain: Implement machine learning model lifecycle and operations

- A. Replace the production deployment in a single step
- B. Keep the previous deployment in place so traffic can be moved back
- C. Bake the model weights into the container image
- D. Overwrite the existing model version instead of registering a new one

### 94. The evaluation set was written by the same team that authored the prompt. What is the risk?

Domain: Implement generative AI quality assurance and observability

- A. Build the evaluation dataset from real queries with graded answers
- B. Generate the evaluation set from the prompt itself
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Assign the work to a person instead of investigating the failure

---

## Case study — Litware Analytics

Litware Analytics builds retrieval-augmented assistants for enterprise clients and is standardizing its GenAIOps practice. Each client engagement currently copies a prompt file into a notebook, edits it in place, and deploys the flow to a shared endpoint whose connection string is stored in the flow repository. Client contracts require that content access follow the client's own entitlement model, and two clients have asked for evidence that a change to the prompt was evaluated before release. The team wants to compare two prompt strategies for the same task without maintaining parallel forks.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A second region must be stood up to the same standard under change control. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Define the workspace in a Bicep module deployed per environment
- C. Export an ARM template from the portal after building it by hand
- D. Create the workspace in the portal and record the steps in a wiki

### 96. One index serves four client accounts and each analyst may see only their own. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Set the connection string as a plain environment variable in the job
- C. Index every document the organization holds
- D. Set document-level access in the index so retrieval respects entitlements

### 97. Analysts send both one-line lookups and long modelling questions to one endpoint. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Route simple requests to a smaller model
- C. Cache identical requests and reuse the completion
- D. Add a router that classifies the request and selects a model

---

## Case study — Portside Utilities

Portside Utilities runs a customer assistant that answers questions about tariffs, outages, and meter readings from a document set that changes daily during storm season. During the last storm the assistant confidently quoted an outdated outage number for six hours, and the operations team only learned about it from social media. The utility has a small platform team, a fixed monthly budget for model spend, and a requirement that no customer account data leave its tenant. The team also wants the assistant to stop answering when the retrieved content does not support an answer.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. The only quality number available is the one recorded on go-live day. What is the gap?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Create an alert rule on the drift and latency metrics
- C. Assign the work to a person instead of investigating the failure
- D. Enable data drift monitoring against the training baseline

### 99. A generated outage summary contradicts a figure it stated earlier. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score coherence for logical structure
- B. Score fluency for readability and language quality
- C. Score relevance of the answer to the question asked
- D. Score groundedness against the retrieved passages

### 100. A cached answer still quotes a tariff replaced last month. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Set a time-to-live on the cache
- B. Cache identical requests and reuse the completion
- C. Disable request logging to reduce storage cost
- D. Accept the behaviour because the aggregate score still looks healthy

---

## Answer key and explanations

### Question 1 — A

Answer: Create a separate Azure Machine Learning workspace per environment. A workspace per environment keeps registered assets and jobs apart. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A workspace per environment keeps registered assets and jobs apart.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A workspace per environment keeps registered assets and jobs apart.
- **C:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A workspace per environment keeps registered assets and jobs apart.
- **D:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A workspace per environment keeps registered assets and jobs apart.

### Question 2 — A

Answer: Register a datastore that points at the storage account. A registered datastore holds the connection outside the job definition. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. In this case: A registered datastore holds the connection outside the job definition.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A registered datastore holds the connection outside the job definition.
- **C:** Incorrect for this question. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Why the correct answer wins: A registered datastore holds the connection outside the job definition.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A registered datastore holds the connection outside the job definition.

### Question 3 — D

Answer: Build a versioned curated environment for the job. A versioned curated environment fixes the interpreter and package set. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set.
- **D:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment fixes the interpreter and package set.

### Question 4 — C

Answer: Register the data as a versioned data asset. A versioned data asset records the exact input used. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A versioned data asset records the exact input used.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned data asset records the exact input used.
- **C:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A versioned data asset records the exact input used.
- **D:** Incorrect for this question. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Why the correct answer wins: A versioned data asset records the exact input used.

### Question 5 — A

Answer: Define the workspace in a Bicep module deployed per environment. A Bicep module is a reviewable, reproducible definition. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A Bicep module is a reviewable, reproducible definition.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A Bicep module is a reviewable, reproducible definition.

### Question 6 — B

Answer: Pass environment values through a Bicep parameter file per stage. A parameter file per unit keeps one module and varies only values. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A parameter file per unit keeps one module and varies only values.
- **B:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: A parameter file per unit keeps one module and varies only values.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A parameter file per unit keeps one module and varies only values.
- **D:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A parameter file per unit keeps one module and varies only values.

### Question 7 — A

Answer: Deploy the module as a deployment stack so removed resources are cleaned up. A deployment stack removes or denies resources it does not own. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: A deployment stack removes or denies resources it does not own.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment stack removes or denies resources it does not own.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A deployment stack removes or denies resources it does not own.

### Question 8 — B

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI is reproducible and auditable. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.
- **B:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI is reproducible and auditable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.
- **D:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI is reproducible and auditable.

### Question 9 — B

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation removes the stored secret. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation removes the stored secret.
- **B:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation removes the stored secret.
- **C:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation removes the stored secret.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation removes the stored secret.

### Question 10 — C

Answer: Use GitHub environment protection rules to gate the production deploy job. A protected environment requires approval before the job runs. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: A protected environment requires approval before the job runs.
- **B:** Incorrect for this question. A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit. Why the correct answer wins: A protected environment requires approval before the job runs.
- **C:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: A protected environment requires approval before the job runs.
- **D:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: A protected environment requires approval before the job runs.

### Question 11 — C

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version identifies what was served. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: An explicit model version identifies what was served.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version identifies what was served.
- **C:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version identifies what was served.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version identifies what was served.

### Question 12 — D

Answer: Promote versions through aliases such as candidate and production. An alias gives a stable pointer that promotion moves. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An alias gives a stable pointer that promotion moves.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An alias gives a stable pointer that promotion moves.
- **C:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: An alias gives a stable pointer that promotion moves.
- **D:** Correct. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. In this case: An alias gives a stable pointer that promotion moves.

### Question 13 — A

Answer: Place a private endpoint on the workspace and its storage. A private endpoint keeps traffic on the virtual network. A private endpoint removes public network access, so traffic stays on the virtual network. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A private endpoint removes public network access, so traffic stays on the virtual network. In this case: A private endpoint keeps traffic on the virtual network.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.

### Question 14 — D

Answer: Store connection strings in Key Vault and reference them by name. Key Vault holds the secret outside the code. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Key Vault holds the secret outside the code.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: Key Vault holds the secret outside the code.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Key Vault holds the secret outside the code.
- **D:** Correct. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. In this case: Key Vault holds the secret outside the code.

### Question 15 — C, E

Answers: Define the workspace in a Bicep module deployed per environment; Deploy the module as a deployment stack so removed resources are cleaned up. Bicep defines the shape, and a deployment stack removes drift. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **B:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **C:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: Bicep defines the shape, and a deployment stack removes drift.
- **D:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes drift.
- **E:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: Bicep defines the shape, and a deployment stack removes drift.

### Question 16 — B, D

Answers: Authenticate the workflow with workload identity federation and no stored secret; Use GitHub environment protection rules to gate the production deploy job. Federated identity removes the secret, and a protected environment adds approval. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **B:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **C:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **D:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **E:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.

### Question 17 — A

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline records each step input and output. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline records each step input and output.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A pipeline records each step input and output.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A pipeline records each step input and output.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline records each step input and output.

### Question 18 — D

Answer: Run the whole workflow as a single script job. Separate pipeline steps make the failure visible and rerunnable. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.
- **C:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.
- **D:** Correct. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. In this case: Separate pipeline steps make the failure visible and rerunnable.

### Question 19 — A

Answer: Run a sweep job over a searched hyperparameter space. A sampled sweep covers a wide space within a budget. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. In this case: A sampled sweep covers a wide space within a budget.
- **B:** Incorrect for this question. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Why the correct answer wins: A sampled sweep covers a wide space within a budget.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep covers a wide space within a budget.
- **D:** Incorrect for this question. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Why the correct answer wins: A sampled sweep covers a wide space within a budget.

### Question 20 — B

Answer: Run a full grid sweep over every combination. A sampled sweep finds the promising region within a budget. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep finds the promising region within a budget.
- **B:** Correct. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. In this case: A sampled sweep finds the promising region within a budget.
- **C:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: A sampled sweep finds the promising region within a budget.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A sampled sweep finds the promising region within a budget.

### Question 21 — B

Answer: Use automated ML to establish the tabular baseline. Automated ML produces a baseline quickly. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML produces a baseline quickly.
- **B:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML produces a baseline quickly.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML produces a baseline quickly.
- **D:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML produces a baseline quickly.

### Question 22 — C

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum stops billing between runs. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **B:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **C:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum stops billing between runs.
- **D:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.

### Question 23 — D

Answer: Point the MLflow tracking URI at the workspace endpoint. The tracking URI must point at the workspace endpoint. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **D:** Correct. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. In this case: The tracking URI must point at the workspace endpoint.

### Question 24 — D

Answer: Group the trials under a named experiment. A named experiment groups runs so variants compare. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups runs so variants compare.
- **B:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups runs so variants compare.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A named experiment groups runs so variants compare.
- **D:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups runs so variants compare.

### Question 25 — B

Answer: Overwrite the existing model version instead of registering a new one. Overwriting destroys the artifact and the audit trail. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.
- **B:** Correct. Overwriting destroys the previous artifact and the audit trail that rollback depends on. In this case: Overwriting destroys the artifact and the audit trail.
- **C:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.

### Question 26 — D

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports the judgement. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A model card with metrics and intended use supports the judgement.
- **D:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports the judgement.

### Question 27 — A

Answer: Tag the registered model with the data asset and commit it came from. Tags carrying the data asset and commit make the rebuild possible. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carrying the data asset and commit make the rebuild possible.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.
- **D:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carrying the data asset and commit make the rebuild possible.

### Question 28 — C

Answer: Deploy to a managed online endpoint with an explicit model version. A managed online endpoint serves synchronous requests. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **C:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: A managed online endpoint serves synchronous requests.
- **D:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: A managed online endpoint serves synchronous requests.

### Question 29 — C

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact decouples the model version from the image. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **B:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **C:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact decouples the model version from the image.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact decouples the model version from the image.

### Question 30 — C

Answer: Configure liveness and readiness probes on the deployment. A readiness probe withholds traffic until the model can serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **B:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe withholds traffic until the model can serve.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.

### Question 31 — C

Answer: Deploy a batch endpoint for the overnight scoring job. A batch endpoint scores a large dataset without always-on capacity. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.
- **B:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.
- **C:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint scores a large dataset without always-on capacity.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch endpoint scores a large dataset without always-on capacity.

### Question 32 — D

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split bounds exposure to a canary share. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **C:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **D:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split bounds exposure to a canary share.

### Question 33 — C

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes reversal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes reversal a traffic change.
- **B:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes reversal a traffic change.
- **C:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes reversal a traffic change.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes reversal a traffic change.

### Question 34 — A

Answer: Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale follows load with a deliberate minimum. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale follows load with a deliberate minimum.
- **B:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale follows load with a deliberate minimum.

### Question 35 — A

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 36 — C

Answer: Create an alert rule on the drift and latency metrics. An alert turns the metric into an action. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into an action.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert turns the metric into an action.
- **C:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into an action.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert turns the metric into an action.

### Question 37 — C, D

Answers: Define the steps as a pipeline job with explicit inputs and outputs; Register each candidate with a version and deploy one explicit version. The pipeline records lineage, and the explicit version pins the artifact. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.
- **B:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.
- **C:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: The pipeline records lineage, and the explicit version pins the artifact.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: The pipeline records lineage, and the explicit version pins the artifact.
- **E:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.

### Question 38 — A, B

Answers: Tag the registered model with the data asset and commit it came from; Attach a description, metrics, and intended use to the model version. Tags record the data asset and commit, and the card documents intended use. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags record the data asset and commit, and the card documents intended use.
- **B:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: Tags record the data asset and commit, and the card documents intended use.
- **C:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.
- **E:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Tags record the data asset and commit, and the card documents intended use.

### Question 39 — A, B

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. A canary share bounds exposure, and a retained deployment enables reversal. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A canary share bounds exposure, and a retained deployment enables reversal.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A canary share bounds exposure, and a retained deployment enables reversal.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables reversal.

### Question 40 — C, E

Answers: Set autoscale rules on the deployment with a deliberate minimum instance count; Configure liveness and readiness probes on the deployment. Autoscale matches capacity, and probes gate traffic until ready. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **B:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: Autoscale matches capacity, and probes gate traffic until ready.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity, and probes gate traffic until ready.
- **E:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity, and probes gate traffic until ready.

### Question 41 — D

Answer: Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress. A second deployment preserves the incumbent for measurement and rollback. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the incumbent destroys the comparison baseline and the thing you would roll back to. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.
- **B:** Incorrect for this question. There is nothing to compare before the candidate exists and is receiving traffic. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.
- **C:** Incorrect for this question. All traffic is shifted before the candidate is deployed, and the comparison comes after the exposure it was meant to prevent. Why the correct answer wins: A second deployment preserves the incumbent for measurement and rollback.
- **D:** Correct. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. In this case: A second deployment preserves the incumbent for measurement and rollback.

### Question 42 — C

Answer: Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate. Detection precedes attribution, and retraining follows once the changed source is known. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A distribution comparison needs a detected drop to compare against, so the trigger is out of order. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.
- **B:** Incorrect for this question. The source is named before any evidence exists, and detection comes last. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.
- **C:** Correct. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. In this case: Detection precedes attribution, and retraining follows once the changed source is known.
- **D:** Incorrect for this question. Retraining before the drop is detected and attributed risks training on data that has the same defect. Why the correct answer wins: Detection precedes attribution, and retraining follows once the changed source is known.

### Question 43 — D

Answer: Create a Foundry hub and a project per team. A hub shares capacity while a project isolates assets. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity while a project isolates assets.
- **D:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity while a project isolates assets.

### Question 44 — B

Answer: Reference the deployment name from the flow rather than the model family name. A deployment name is the stable reference. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The catalog lists models with their capabilities; deploying one into the project makes it addressable by a deployment name. Why the correct answer wins: A deployment name is the stable reference.
- **B:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A deployment name is the stable reference.
- **C:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A deployment name is the stable reference.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A deployment name is the stable reference.

### Question 45 — D

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput gives predictable cost and latency. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.
- **C:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput gives predictable cost and latency.
- **D:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput gives predictable cost and latency.

### Question 46 — C

Answer: Start on pay-as-you-go while the volume is still unknown. Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **C:** Correct. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. In this case: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **D:** Incorrect for this question. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.

### Question 47 — A

Answer: Apply a content filter policy appropriate to the audience. A content filter policy applies those thresholds. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. In this case: A content filter policy applies those thresholds.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: A content filter policy applies those thresholds.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: A content filter policy applies those thresholds.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A content filter policy applies those thresholds.

### Question 48 — B

Answer: Author the flow as a directed acyclic graph with typed inputs and outputs. A typed directed acyclic graph makes each node testable. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A typed directed acyclic graph makes each node testable.
- **B:** Correct. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. In this case: A typed directed acyclic graph makes each node testable.
- **C:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A typed directed acyclic graph makes each node testable.
- **D:** Incorrect for this question. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Why the correct answer wins: A typed directed acyclic graph makes each node testable.

### Question 49 — B

Answer: Create a variant to compare two prompt strategies side by side. Variants hold alternatives together for a reproducible comparison. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.
- **B:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: Variants hold alternatives together for a reproducible comparison.
- **C:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: Variants hold alternatives together for a reproducible comparison.

### Question 50 — B

Answer: Store the model credential as a project connection. A project connection holds the endpoint and credential externally. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **B:** Correct. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. In this case: A project connection holds the endpoint and credential externally.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A project connection holds the endpoint and credential externally.

### Question 51 — A

Answer: Paste the API key into a Python node inside the flow. A key in a flow file is a secret in source control. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. In this case: A key in a flow file is a secret in source control.
- **B:** Incorrect for this question. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Why the correct answer wins: A key in a flow file is a secret in source control.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A key in a flow file is a secret in source control.
- **D:** Incorrect for this question. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Why the correct answer wins: A key in a flow file is a secret in source control.

### Question 52 — A

Answer: Index the documents in Azure AI Search and query the index from the flow. An index supports retrieval against current content. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: An index supports retrieval against current content.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: An index supports retrieval against current content.
- **C:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: An index supports retrieval against current content.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: An index supports retrieval against current content.

### Question 53 — D

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.

### Question 54 — D

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh aligns retrieval with the source. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **D:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh aligns retrieval with the source.

### Question 55 — A

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate relevant text.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.

### Question 56 — C

Answer: Keep the prompt in its own file under version control. A versioned prompt file is the change record. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the change record.
- **B:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A versioned prompt file is the change record.
- **C:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the change record.
- **D:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A versioned prompt file is the change record.

### Question 57 — D

Answer: Run the evaluation in continuous integration before the flow is promoted. An offline evaluation gate blocks a regression before promotion. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **D:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An offline evaluation gate blocks a regression before promotion.

### Question 58 — B, E

Answers: Create a Foundry hub and a project per team; Reference the deployment name from the flow rather than the model family name. A project per unit isolates assets, and the deployment name keeps flows stable. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A project per unit isolates assets, and the deployment name keeps flows stable.
- **B:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A project per unit isolates assets, and the deployment name keeps flows stable.
- **C:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project per unit isolates assets, and the deployment name keeps flows stable.
- **D:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A project per unit isolates assets, and the deployment name keeps flows stable.
- **E:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A project per unit isolates assets, and the deployment name keeps flows stable.

### Question 59 — B, D

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing enables grounding, and document-level access enforces entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **B:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **C:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **D:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **E:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.

### Question 60 — B, D

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file is the record, and the offline gate is the control. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **B:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **C:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **D:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **E:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.

### Question 61 — C

Answer: Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content. The inventory defines scope, identity replaces the secret, the grant is minimal, and verification proves it. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A broad grant is made before the sources are known, and the identity is assigned after it has been granted permissions. Why the correct answer wins: The inventory defines scope, identity replaces the secret, the grant is minimal, and verification proves it.
- **B:** Incorrect for this question. The answer is verified before any role has been granted, and the sources are inventoried after the grant. Why the correct answer wins: The inventory defines scope, identity replaces the secret, the grant is minimal, and verification proves it.
- **C:** Correct. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. In this case: The inventory defines scope, identity replaces the secret, the grant is minimal, and verification proves it.
- **D:** Incorrect for this question. Verification precedes the configuration it verifies, and the inventory comes last. Why the correct answer wins: The inventory defines scope, identity replaces the secret, the grant is minimal, and verification proves it.

### Question 62 — C

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation build on each other. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **B:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.
- **C:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation build on each other.
- **D:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other.

### Question 63 — B

Answer: Build the evaluation dataset from real queries with graded answers. Real queries with graded answers make the result defensible. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries with graded answers make the result defensible.
- **B:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries with graded answers make the result defensible.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries with graded answers make the result defensible.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries with graded answers make the result defensible.

### Question 64 — B

Answer: Use a few hundred representative cases rather than a dozen. A set that small cannot separate a real gain from noise. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **B:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: A set that small cannot separate a real gain from noise.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A set that small cannot separate a real gain from noise.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A set that small cannot separate a real gain from noise.

### Question 65 — B

Answer: Score relevance of the answer to the question asked. Relevance measures whether the answer addresses the question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **B:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Relevance measures whether the answer addresses the question.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **D:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Relevance measures whether the answer addresses the question.

### Question 66 — D

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **D:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.

### Question 67 — B

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing shows the failing stage. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing shows the failing stage.
- **B:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing shows the failing stage.
- **C:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing shows the failing stage.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing shows the failing stage.

### Question 68 — B

Answer: Log prompts and completions against the trace, within data policy. Prompts and completions logged against the trace allow replay. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Prompts and completions logged against the trace allow replay.
- **B:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Prompts and completions logged against the trace allow replay.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Prompts and completions logged against the trace allow replay.
- **D:** Incorrect for this question. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Why the correct answer wins: Prompts and completions logged against the trace allow replay.

### Question 69 — A

Answer: Capture user feedback and review a sample of rated conversations weekly. Capturing and triaging feedback surfaces traffic the dataset lacks. User feedback is the only signal about traffic that the evaluation set does not contain. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. User feedback is the only signal about traffic that the evaluation set does not contain. In this case: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **B:** Incorrect for this question. Online evaluation catches the drift that a fixed offline dataset cannot represent. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **C:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **D:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.

### Question 70 — A, E

Answers: Score groundedness against the retrieved passages; Score relevance of the answer to the question asked. Groundedness measures support, and relevance measures whether the question was answered. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **C:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **D:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **E:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support, and relevance measures whether the question was answered.

### Question 71 — B, E

Answers: Test indirect injection through retrieved documents; Run adversarial jailbreak and prompt-injection cases before release. Indirect cases test retrieved content, and jailbreak cases test user input. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **B:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **E:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.

### Question 72 — A, E

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing identifies the stage, and prompt logging permits replay. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing identifies the stage, and prompt logging permits replay.
- **B:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **E:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing identifies the stage, and prompt logging permits replay.

### Question 73 — B

Answer: Assemble jailbreak and injection cases → configure the content filter and system prompt → run the adversarial evaluation → monitor the filtered and blocked rates in production. Cases define the test, the control is configured, the test proves it, and monitoring keeps it honest. The attack set defines what is being tested, the control is configured, the test proves it, and monitoring keeps it honest afterwards. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The filter is configured after the evaluation that was supposed to validate it. Why the correct answer wins: Cases define the test, the control is configured, the test proves it, and monitoring keeps it honest.
- **B:** Correct. The attack set defines what is being tested, the control is configured, the test proves it, and monitoring keeps it honest afterwards. In this case: Cases define the test, the control is configured, the test proves it, and monitoring keeps it honest.
- **C:** Incorrect for this question. Production monitoring comes before the control it is meant to watch has even been configured. Why the correct answer wins: Cases define the test, the control is configured, the test proves it, and monitoring keeps it honest.
- **D:** Incorrect for this question. The evaluation runs before the adversarial cases exist, so it has nothing to test against. Why the correct answer wins: Cases define the test, the control is configured, the test proves it, and monitoring keeps it honest.

### Question 74 — B

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **B:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **C:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **D:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.

### Question 75 — D

Answer: Measure tokens per request and set a budget per endpoint. Per-request token measurement is what lets spend be attributed to a workload. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a workload.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a workload.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a workload.
- **D:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: Per-request token measurement is what lets spend be attributed to a workload.

### Question 76 — C

Answer: Add a router that classifies the request and selects a model. A router selects a model appropriate to the request. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects a model appropriate to the request.
- **B:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router selects a model appropriate to the request.
- **C:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects a model appropriate to the request.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects a model appropriate to the request.

### Question 77 — D

Answer: Stream the response so the first token arrives sooner. Streaming delivers the first token sooner. Streaming improves perceived latency without changing total generation time. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Batch work uses cheaper capacity and takes the work off the interactive path. Why the correct answer wins: Streaming delivers the first token sooner.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Streaming delivers the first token sooner.
- **C:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Streaming delivers the first token sooner.
- **D:** Correct. Streaming improves perceived latency without changing total generation time. In this case: Streaming delivers the first token sooner.

### Question 78 — C

Answer: Set a request timeout with a bounded retry and backoff. A bounded timeout with backoff stops a failing dependency amplifying load. A bounded retry with backoff stops a failing dependency from multiplying load. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.
- **C:** Correct. A bounded retry with backoff stops a failing dependency from multiplying load. In this case: A bounded timeout with backoff stops a failing dependency amplifying load.
- **D:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: A bounded timeout with backoff stops a failing dependency amplifying load.

### Question 79 — C

Answer: Retrieve fewer but better-ranked passages. Fewer, better-ranked passages cut tokens and improve precision. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **B:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **C:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer, better-ranked passages cut tokens and improve precision.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.

### Question 80 — D

Answer: Compress the system prompt and remove redundant instructions. Compressing the prompt cuts input tokens on every call. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **D:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Compressing the prompt cuts input tokens on every call.

### Question 81 — A

Answer: Re-run the evaluation after the cost optimization. Quality must be re-measured after any change that trades accuracy for cost. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. In this case: Quality must be re-measured after any change that trades accuracy for cost.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.
- **D:** Incorrect for this question. The support queue is a lagging signal that reports damage after users have already experienced it. Why the correct answer wins: Quality must be re-measured after any change that trades accuracy for cost.

### Question 82 — B

Answer: Move steady traffic to provisioned throughput. Provisioned throughput lowers cost per token at sustained volume. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **B:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Provisioned throughput lowers cost per token at sustained volume.
- **C:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.

### Question 83 — C

Answer: Move non-urgent generation into a batch run. Batch work uses cheaper capacity off the interactive path. Batch work uses cheaper capacity and takes the work off the interactive path. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **B:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **C:** Correct. Batch work uses cheaper capacity and takes the work off the interactive path. In this case: Batch work uses cheaper capacity off the interactive path.
- **D:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.

### Question 84 — D, E

Answers: Measure tokens per request and set a budget per endpoint; Set a time-to-live on the cache. A token budget attributes cost, and a TTL keeps answers current. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **D:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A token budget attributes cost, and a TTL keeps answers current.
- **E:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: A token budget attributes cost, and a TTL keeps answers current.

### Question 85 — C, D

Answers: Add a router that classifies the request and selects a model; Route simple requests to a smaller model. A router selects per request, and a smaller model covers the simple majority. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **C:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects per request, and a smaller model covers the simple majority.
- **D:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A router selects per request, and a smaller model covers the simple majority.
- **E:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.

### Question 86 — B

Answer: Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held. Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An optimization is applied before anything has been measured or attributed. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **B:** Correct. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. In this case: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **C:** Incorrect for this question. A driver is named before measurement, and the evaluation runs before the change exists. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **D:** Incorrect for this question. Evaluation precedes both the change it would validate and the measurement that motivates it. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.

### Question 87 — D

Answer: Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration. Measurement and forecasting precede the commercial comparison, and the load test validates it. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Capacity is committed before the demand that justifies it has been measured. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **B:** Incorrect for this question. A load test needs a configuration chosen from the measurement and forecast, both of which come later. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **C:** Incorrect for this question. The forecast is made without a measurement baseline, and the commitment precedes the measurement entirely. Why the correct answer wins: Measurement and forecasting precede the commercial comparison, and the load test validates it.
- **D:** Correct. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. In this case: Measurement and forecasting precede the commercial comparison, and the load test validates it.

### Question 88 — A, D

Answers: Build a versioned curated environment for the job; Register the data as a versioned data asset. A pinned environment fixes dependencies, and a versioned data asset fixes the input. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A pinned environment fixes dependencies, and a versioned data asset fixes the input.
- **B:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A pinned environment fixes dependencies, and a versioned data asset fixes the input.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A pinned environment fixes dependencies, and a versioned data asset fixes the input.
- **D:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A pinned environment fixes dependencies, and a versioned data asset fixes the input.
- **E:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A pinned environment fixes dependencies, and a versioned data asset fixes the input.

### Question 89 — C

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.

### Question 90 — C

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh aligns retrieval with the current revision. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh aligns retrieval with the current revision.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh aligns retrieval with the current revision.
- **C:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh aligns retrieval with the current revision.
- **D:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh aligns retrieval with the current revision.

### Question 91 — C, D

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file is the record, and the offline gate is the control. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **B:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.
- **C:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **D:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the record, and the offline gate is the control.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned prompt file is the record, and the offline gate is the control.

### Question 92 — A

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 93 — B

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes withdrawal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes withdrawal a traffic change.
- **C:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.

### Question 94 — A

Answer: Build the evaluation dataset from real queries with graded answers. A set authored from the prompt repeats its assumptions and passes changes users would reject. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: A set authored from the prompt repeats its assumptions and passes changes users would reject.
- **B:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A set authored from the prompt repeats its assumptions and passes changes users would reject.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A set authored from the prompt repeats its assumptions and passes changes users would reject.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A set authored from the prompt repeats its assumptions and passes changes users would reject.

### Question 95 — B

Answer: Define the workspace in a Bicep module deployed per environment. A reviewed Bicep module recreates the environment identically. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **B:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A reviewed Bicep module recreates the environment identically.
- **C:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.

### Question 96 — D

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.

### Question 97 — D

Answer: Add a router that classifies the request and selects a model. A router classifies the request and selects an appropriate model. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router classifies the request and selects an appropriate model.
- **B:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router classifies the request and selects an appropriate model.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router classifies the request and selects an appropriate model.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router classifies the request and selects an appropriate model.

### Question 98 — A

Answer: Monitor only the accuracy reported at deployment time. A deployment-time snapshot says nothing about subsequent data. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. In this case: A deployment-time snapshot says nothing about subsequent data.
- **B:** Incorrect for this question. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **D:** Incorrect for this question. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.

### Question 99 — A

Answer: Score coherence for logical structure. Coherence measures whether the answer holds together logically. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. In this case: Coherence measures whether the answer holds together logically.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **D:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Coherence measures whether the answer holds together logically.

### Question 100 — A

Answer: Set a time-to-live on the cache. A TTL stops a cached answer outliving its source. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A TTL stops a cached answer outliving its source.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A TTL stops a cached answer outliving its source.
