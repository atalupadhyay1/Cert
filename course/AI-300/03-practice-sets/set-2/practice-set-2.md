# Microsoft AI-300 — Full-Length Mock Exam 2

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A delivery team is asked why a test job consumed the production datastore credentials. What separation would have prevented it?

Domain: Design and implement an MLOps infrastructure

- A. Attach a GPU cluster with four always-on nodes
- B. Use one workspace for development, test, and production
- C. Run the job from a compute instance notebook
- D. Create a separate Azure Machine Learning workspace per environment

### 2. A job YAML contains a storage account key and a physical path that changed twice last quarter. What should replace it?

Domain: Design and implement an MLOps infrastructure

- A. Reference the storage path with the account key inline in the job YAML
- B. Print the metrics to the job log and read them from the console
- C. Register a datastore that points at the storage account
- D. Register the data as a versioned data asset

### 3. A dependency upgrade broke a pipeline overnight even though nobody changed the training code. What would have prevented it?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Disable request logging to reduce storage cost
- C. Reference the floating latest tag for the environment image
- D. Build a versioned curated environment for the job

### 4. Three teams maintain three copies of the same feature-engineering code and they now disagree. What should be created?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Package the preparation step as a reusable component
- C. Run the job from a compute instance notebook
- D. Run the whole workflow as a single script job

### 5. A model must be explainable to a client two years after delivery, including the data it saw. What should have been versioned?

Domain: Design and implement an MLOps infrastructure

- A. Register the data as a versioned data asset
- B. Reference the storage path with the account key inline in the job YAML
- C. Register a datastore that points at the storage account
- D. Assign the work to a person instead of investigating the failure

### 6. A client requires that their environment be reproducible from a reviewed definition. What should be delivered?

Domain: Design and implement an MLOps infrastructure

- A. Export an ARM template from the portal after building it by hand
- B. Define the workspace in a Bicep module deployed per environment
- C. Rebuild the environment by hand from the notes in the ticket
- D. Create the workspace in the portal and record the steps in a wiki

### 7. The same module deploys to three tenants with different names and SKUs. Where do the differences belong?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Export an ARM template from the portal after building it by hand
- C. Pass environment values through a Bicep parameter file per stage
- D. Rebuild the environment by hand from the notes in the ticket

### 8. A resource added by hand outside the template is never removed, and cost grows silently. What deployment model fixes that?

Domain: Design and implement an MLOps infrastructure

- A. Keep public network access enabled so notebooks connect easily
- B. Deploy the module as a deployment stack so removed resources are cleaned up
- C. Create the workspace in the portal and record the steps in a wiki
- D. Assign the work to a person instead of investigating the failure

### 9. A client wants every training run submitted by an auditable command rather than a notebook cell. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Stream the job with az ml job stream to inspect logs
- C. Run the job from a compute instance notebook
- D. Submit the job with az ml job create --file job.yaml

### 10. An engineer must watch a running job fail in real time during a client call. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Disable request logging to reduce storage cost
- B. Submit the job with az ml job create --file job.yaml
- C. Print the metrics to the job log and read them from the console
- D. Stream the job with az ml job stream to inspect logs

### 11. A client security review forbids any long-lived credential in the repository. What should authenticate the deployment workflow?

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Store a service principal client secret as a GitHub repository secret
- C. Set the connection string as a plain environment variable in the job
- D. Authenticate the workflow with workload identity federation and no stored secret

### 12. A regulated client requires a named approver before any production deployment. What should be configured?

Domain: Design and implement an MLOps infrastructure

- A. Run the pipeline from a GitHub Actions workflow on merge to main
- B. Use GitHub environment protection rules to gate the production deploy job
- C. Store a service principal client secret as a GitHub repository secret
- D. Fan the tests out across a matrix of dependency versions

### 13. A connection string must be rotatable without redeploying the job definition. Where should it live?

Domain: Design and implement an MLOps infrastructure

- A. Store connection strings in Key Vault and reference them by name
- B. Print the metrics to the job log and read them from the console
- C. Reference the storage path with the account key inline in the job YAML
- D. Set the connection string as a plain environment variable in the job

### 14. A client audit requires a pinned artifact and its provenance. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Overwrite the existing model version instead of registering a new one
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Tag the registered model with the data asset and commit it came from
- D. Register each candidate with a version and deploy one explicit version
- E. Register the model and always deploy whichever version is latest

### 15. An environment must be recreated from code and stay free of manual changes. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Deploy the module as a deployment stack so removed resources are cleaned up
- B. Rebuild the environment by hand from the notes in the ticket
- C. Define the workspace in a Bicep module deployed per environment
- D. Create the workspace in the portal and record the steps in a wiki
- E. Export an ARM template from the portal after building it by hand

### 16. A delivery team must grant a flow access without secrets. Which sequence is correct?

Domain: Design and implement an MLOps infrastructure

- A. Verify a grounded answer → assign the identity → grant the role → inventory the sources
- B. Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content
- C. Assign the identity → verify the answer → inventory the sources → grant the role
- D. Grant the identity Owner on each source → inventory the data sources → verify the answer → assign a managed identity

### 17. A client asks for evidence that the evaluation step consumed the exact output of the training step. What provides that?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Run the whole workflow as a single script job
- C. Assign the work to a person instead of investigating the failure
- D. Send the overnight file through the online endpoint request by request

### 18. A single script hides which of six stages failed and reruns everything to recover. What should replace it?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Run the whole workflow as a single script job
- C. Run the job from a compute instance notebook
- D. Print the metrics to the job log and read them from the console

### 19. A client needs a defensible baseline for a tabular risk model within two days. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Run the whole workflow as a single script job
- C. Run the job from a compute instance notebook
- D. Use automated ML to establish the tabular baseline

### 20. Deep learning experiments run twice a week and the team is billed for idle accelerators overnight. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Attach a GPU cluster with four always-on nodes
- C. Attach a CPU compute cluster for the data preparation step
- D. Attach a GPU cluster with a minimum of zero nodes

### 21. Every combination of four hyperparameters was run and the experiment cost more than the project. What should have been used instead?

Domain: Implement machine learning model lifecycle and operations

- A. Run a full grid sweep over every combination
- B. Run a sweep job over a searched hyperparameter space
- C. Retrain the model on the newer data
- D. Increase the model size until the answers improve

### 22. Runs appear in the engineer's local directory and never in the shared experiment list. What is wrong?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Point the MLflow tracking URI at the workspace endpoint
- C. Disable request logging to reduce storage cost
- D. Print the metrics to the job log and read them from the console

### 23. Three preprocessing strategies were trialled and their runs are scattered across one list of nine hundred. What should have been used?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Disable request logging to reduce storage cost
- C. Enable MLflow tracking so runs log to the workspace
- D. Group the trials under a named experiment

### 24. A deployment resolved whichever version was newest and shipped an untested candidate. What should it reference?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy straight to production to save a day
- B. Register the model and always deploy whichever version is latest
- C. Overwrite the existing model version instead of registering a new one
- D. Register each candidate with a version and deploy one explicit version

### 25. A client reviewer must judge suitability before a promotion meeting. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Register the model and always deploy whichever version is latest
- C. Attach a description, metrics, and intended use to the model version
- D. Accept the behaviour because the aggregate score still looks healthy

### 26. A registry entry was replaced in place last year and the approved decision can no longer be reproduced. What was the error?

Domain: Implement machine learning model lifecycle and operations

- A. Tag the registered model with the data asset and commit it came from
- B. Register each candidate with a version and deploy one explicit version
- C. Assign the work to a person instead of investigating the failure
- D. Overwrite the existing model version instead of registering a new one

### 27. An application calls for a single prediction and needs a response in milliseconds. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Deploy to a managed online endpoint with an explicit model version
- C. Send the overnight file through the online endpoint request by request
- D. Deploy a batch endpoint for the overnight scoring job

### 28. Every candidate currently requires a container build before it can be tested. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Mount the model artifact rather than baking it into the image
- B. Overwrite the existing model version instead of registering a new one
- C. Bake the model weights into the container image
- D. Replace the production deployment in a single step

### 29. A new deployment returns errors for ninety seconds after start because the model is still loading. What should be added?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy without probes and rely on the platform health check
- B. Pin a fixed instance count for a spiky workload
- C. Configure liveness and readiness probes on the deployment
- D. Monitor only the accuracy reported at deployment time

### 30. A client requires that a new version affect no more than five percent of requests initially. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy straight to production to save a day
- B. Keep the previous deployment in place so traffic can be moved back
- C. Replace the production deployment in a single step
- D. Split endpoint traffic 10/90 so the new deployment receives a canary share

### 31. A release must be reversible inside the client's five-minute window. What must exist?

Domain: Implement machine learning model lifecycle and operations

- A. Replace the production deployment in a single step
- B. Bake the model weights into the container image
- C. Overwrite the existing model version instead of registering a new one
- D. Keep the previous deployment in place so traffic can be moved back

### 32. A nightly job loops over the online endpoint one record at a time and now misses its window. What is the error?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Set autoscale rules on the deployment with a deliberate minimum instance count
- C. Deploy a batch endpoint for the overnight scoring job
- D. Split endpoint traffic 10/90 so the new deployment receives a canary share

### 33. A scoring service peaks at month end and is idle otherwise, and the client objects to paying for the peak. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Pin a fixed instance count for a spiky workload
- C. Set autoscale rules on the deployment with a deliberate minimum instance count
- D. Deploy without probes and rely on the platform health check

### 34. A client asks whether the model still sees the data it was trained on. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Enable data drift monitoring against the training baseline
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Retrain the model on the newer data

### 35. Accuracy was recorded once at deployment and never again, and the client asks how degradation is detected. What is the gap?

Domain: Implement machine learning model lifecycle and operations

- A. Assign the work to a person instead of investigating the failure
- B. Monitor only the accuracy reported at deployment time
- C. Enable data drift monitoring against the training baseline
- D. Create an alert rule on the drift and latency metrics

### 36. A client endpoint must survive bursts and must not serve before the model loads. Which two configurations apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Deploy without probes and rely on the platform health check
- B. Send the overnight file through the online endpoint request by request
- C. Configure liveness and readiness probes on the deployment
- D. Set autoscale rules on the deployment with a deliberate minimum instance count
- E. Pin a fixed instance count for a spiky workload

### 37. A release needs a bounded canary and a fast reversal. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Replace the production deployment in a single step
- C. Keep the previous deployment in place so traffic can be moved back
- D. Split endpoint traffic 10/90 so the new deployment receives a canary share
- E. Overwrite the existing model version instead of registering a new one

### 38. A modelling team must put a candidate into production behind a gate. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Evaluate against the gate → train the candidate → shift all traffic → register the model version
- B. Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold
- C. Register the model version → train the candidate → evaluate against the gate → shift all traffic
- D. Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate

### 39. A pipeline must reference published assets and a pinned environment. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Run the pipeline in the test environment → reference both from the pipeline YAML → publish the component → build the environment
- B. Build the environment → run the pipeline → publish the component → reference it in the YAML
- C. Publish the component to the registry → build a versioned environment that pins its dependencies → reference both from the pipeline YAML → run the pipeline in the test environment
- D. Reference both from the pipeline YAML → build the environment → publish the component → run the pipeline

### 40. Three delivery teams need shared model capacity but separate assets. What should be created?

Domain: Design and implement a GenAIOps infrastructure

- A. Create a Foundry hub and a project per team
- B. Use one workspace for development, test, and production
- C. Give every team one project and one shared connection
- D. Create the workspace in the portal and record the steps in a wiki

### 41. A flow references a model family and broke when the client swapped the underlying deployment. What should the flow reference?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Hardcode the model family name inside the flow
- C. Reference the deployment name from the flow rather than the model family name
- D. Select a model from the catalog and deploy it into the project

### 42. A client assistant serves a steady 800 requests a minute all day. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Reserve provisioned throughput for the steady high-volume workload
- B. Start on pay-as-you-go while the volume is still unknown
- C. Pin a fixed instance count for a spiky workload
- D. Use the largest model for every request

### 43. A pilot may end after eight weeks with unpredictable usage. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Reserve provisioned throughput for the steady high-volume workload
- B. Pin a fixed instance count for a spiky workload
- C. Use the largest model for every request
- D. Start on pay-as-you-go while the volume is still unknown

### 44. A flow running on Azure must reach storage without any stored secret. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Set the connection string as a plain environment variable in the job
- C. Assign a managed identity to compute and grant it the storage role
- D. Reference the storage path with the account key inline in the job YAML

### 45. A key appeared in a merged pull request because it was typed into a node. What was the defect?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Set the connection string as a plain environment variable in the job
- C. Store connection strings in Key Vault and reference them by name
- D. Store the model credential as a project connection

### 46. A client knowledge base changes weekly and answers must cite the current revision. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Increase the model size until the answers improve
- B. Fine-tune the model on the document set instead of retrieving
- C. Index the documents in Azure AI Search and query the index from the flow
- D. Index every document the organization holds

### 47. Retrieval cannot find contract numbers such as CT-2024-118. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Fine-tune the model on the document set instead of retrieving
- B. Increase the model size until the answers improve
- C. Use vector search alone with no keyword component
- D. Use hybrid search with semantic ranking

### 48. A shared index holds documents from four clients and each user must see only their own. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Keep public network access enabled so notebooks connect easily
- C. Set the connection string as a plain environment variable in the job
- D. Set document-level access in the index so retrieval respects entitlements

### 49. Answers cite the right contract but the wrong clause. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk documents by section with a small overlap
- B. Index every document the organization holds
- C. Index each document as one large chunk
- D. Raise retrieval depth to the maximum for safety

### 50. A client updates policy pages nightly and answers still reflect last quarter. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Rebuild the index on a schedule after the source content changes
- D. Index every document the organization holds

### 51. A client requires every prompt change to be reviewable and revertible. Where should prompts live?

Domain: Design and implement a GenAIOps infrastructure

- A. Keep the prompt in its own file under version control
- B. Rewrite the prompt and deploy it immediately
- C. Create a variant to compare two prompt strategies side by side
- D. Paste the API key into a Python node inside the flow

### 52. A prompt edit reduced quality for a week before anyone noticed. What was missing?

Domain: Design and implement a GenAIOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Rewrite the prompt and deploy it immediately
- D. Deploy straight to production to save a day

### 53. An agent can call a payment tool that is out of scope for research work. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Register a scoped tool list for the agent
- B. Increase the model size until the answers improve
- C. Expose every available tool so the agent can choose freely
- D. Index every document the organization holds

### 54. A flow must be testable step by step and comparable across two prompt strategies. Which two features apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Author the flow as a directed acyclic graph with typed inputs and outputs
- C. Rewrite the prompt and deploy it immediately
- D. Run the whole workflow as a single script job
- E. Create a variant to compare two prompt strategies side by side

### 55. A client assistant must ground on current documents and respect entitlements. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Index the documents in Azure AI Search and query the index from the flow
- B. Index every document the organization holds
- C. Set document-level access in the index so retrieval respects entitlements
- D. Fine-tune the model on the document set instead of retrieving
- E. Keep public network access enabled so notebooks connect easily

### 56. A regulated client requires a change record and a quality gate for prompts. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Keep the prompt in its own file under version control
- C. Rewrite the prompt and deploy it immediately
- D. Deploy straight to production to save a day
- E. Run the evaluation in continuous integration before the flow is promoted

### 57. An agent must be bounded in what it can do and in what it remembers. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Expose every available tool so the agent can choose freely
- B. Register a scoped tool list for the agent
- C. Bound the agent memory to the current session
- D. Index every document the organization holds
- E. Pass typed state between agent steps

### 58. A consultancy must deliver a grounded assistant to a client. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness
- B. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- C. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents
- D. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them

### 59. A client disputes the evaluation result and asks what it was measured on. What should the set contain?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Build the evaluation dataset from real queries with graded answers
- C. Generate the evaluation set from the prompt itself
- D. Accept the behaviour because the aggregate score still looks healthy

### 60. A forty-case set improved from 0.72 to 0.78 and the client asks whether that is real. What is the answer?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Generate the evaluation set from the prompt itself
- C. Use a few hundred representative cases rather than a dozen
- D. Retrain the model on the newer data

### 61. Grading three thousand cases by hand is not feasible within the engagement. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Use an LLM judge with a rubric, calibrated against human grades
- C. Rely on the LLM judge without checking it against human grades
- D. Generate the evaluation set from the prompt itself

### 62. An answer is well written but asserts a liability cap that no retrieved passage states. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score relevance of the answer to the question asked
- B. Score groundedness against the retrieved passages
- C. Score coherence for logical structure
- D. Score fluency for readability and language quality

### 63. An answer faithfully summarizes a passage that does not address the question. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score relevance of the answer to the question asked
- B. Score groundedness against the retrieved passages
- C. Score similarity against a reference answer
- D. Score fluency for readability and language quality

### 64. A client asks for evidence that the assistant resists instruction override. What must be run?

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Evaluate toxicity against the threshold the audience requires
- C. Run adversarial jailbreak and prompt-injection cases before release
- D. Accept the behaviour because the aggregate score still looks healthy

### 65. A retrieved client document contains text instructing the assistant to ignore its rules. What is being tested?

Domain: Implement generative AI quality assurance and observability

- A. Test indirect injection through retrieved documents
- B. Disable request logging to reduce storage cost
- C. Run adversarial jailbreak and prompt-injection cases before release
- D. Evaluate toxicity against the threshold the audience requires

### 66. A wrong answer must be attributed to retrieval or to generation. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Rely on the LLM judge without checking it against human grades
- B. Enable distributed tracing and log the retrieval and model spans
- C. Disable request logging to reduce storage cost
- D. Log prompts and completions against the trace, within data policy

### 67. Users in one region rate answers poorly and the dataset does not cover their questions. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Run continuous evaluation on sampled production traffic
- B. Rely on the LLM judge without checking it against human grades
- C. Run the evaluation in continuous integration before the flow is promoted
- D. Capture user feedback and review a sample of rated conversations weekly

### 68. A retrieval-based assistant must resist override from both users and documents. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Test indirect injection through retrieved documents
- B. Evaluate toxicity against the threshold the audience requires
- C. Disable request logging to reduce storage cost
- D. Run adversarial jailbreak and prompt-injection cases before release
- E. Score fluency for readability and language quality

### 69. A disputed answer must be diagnosable months later. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Rely on the LLM judge without checking it against human grades
- B. Assign the work to a person instead of investigating the failure
- C. Disable request logging to reduce storage cost
- D. Enable distributed tracing and log the retrieval and model spans
- E. Log prompts and completions against the trace, within data policy

### 70. A client escalates a wrong answer and the team must explain it. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set
- B. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- C. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set
- D. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set

### 71. A client portal repeats the same two hundred questions all day. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Cache identical requests and reuse the completion
- C. Set a time-to-live on the cache
- D. Compress the system prompt and remove redundant instructions

### 72. A cached answer cites a clause that changed last month. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Cache identical requests and reuse the completion
- C. Set a time-to-live on the cache
- D. Disable request logging to reduce storage cost

### 73. A client workload mixes short lookups and long analyses behind one endpoint. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Cache identical requests and reuse the completion
- C. Add a router that classifies the request and selects a model
- D. Route simple requests to a smaller model

### 74. Most requests are three-line summaries and every one calls the most expensive model. What should change?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Retrain the model on the newer data
- C. Route simple requests to a smaller model
- D. Use the largest model for every request

### 75. A team standardized on the largest model for consistency and the bill tripled. What is the objection?

Domain: Optimize generative AI systems and model performance

- A. Route simple requests to a smaller model
- B. Add a router that classifies the request and selects a model
- C. Use the largest model for every request
- D. Cache identical requests and reuse the completion

### 76. A client complains that nothing appears for six seconds although the answer completes in eight. What should change?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Move non-urgent generation into a batch run
- C. Set a request timeout with a bounded retry and backoff
- D. Stream the response so the first token arrives sooner

### 77. Twenty passages are retrieved per answer and only one is used. What should change?

Domain: Optimize generative AI systems and model performance

- A. Retrieve fewer but better-ranked passages
- B. Increase the model size until the answers improve
- C. Raise retrieval depth to the maximum for safety
- D. Index every document the organization holds

### 78. A 5,000-token instruction is sent with every request and a third of it is repeated. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Raise retrieval depth to the maximum for safety
- B. Compress the system prompt and remove redundant instructions
- C. Cache identical requests and reuse the completion
- D. Increase the model size until the answers improve

### 79. A stable classification task ships a long instruction on every call. What can absorb it?

Domain: Optimize generative AI systems and model performance

- A. Fine-tune the model on the document set instead of retrieving
- B. Fine-tune on approved examples to shorten the standing prompt
- C. Increase the model size until the answers improve
- D. Compress the system prompt and remove redundant instructions

### 80. A nightly report generation does not need a response until morning. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Stream the response so the first token arrives sooner
- B. Set a request timeout with a bounded retry and backoff
- C. Move non-urgent generation into a batch run
- D. Add a router that classifies the request and selects a model

### 81. A client requires attributable spend and fresh answers. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Use the largest model for every request
- D. Measure tokens per request and set a budget per endpoint
- E. Set a time-to-live on the cache

### 82. A mixed workload must cost less without losing quality on hard cases. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Retrain the model on the newer data
- C. Cache identical requests and reuse the completion
- D. Add a router that classifies the request and selects a model
- E. Route simple requests to a smaller model

### 83. A client engagement must cut model spend without losing quality. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization
- B. Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver
- C. Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver
- D. Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held

### 84. A regulated engagement changes prompts frequently and needs a reviewable release. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Review the diff and metric change → edit the prompt in a branch → deploy the version → run the evaluation gate
- B. Edit the prompt file in a branch → run the offline evaluation gate → review the diff and metric change in a pull request → deploy the approved version and watch the online metrics
- C. Run the offline evaluation gate → deploy the version → review the diff → edit the prompt
- D. Deploy the approved version → edit the prompt in a branch → run the evaluation gate → review the diff

### 85. A nightly reporting workload must be moved off the interactive path. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Submit the batch endpoint job → prepare the input dataset → validate the output → confirm the workload is not interactive
- B. Confirm the workload is not interactive → prepare a batch input dataset → submit the batch endpoint job → validate the output file against the schema
- C. Validate the output file → submit the job → prepare the input → confirm the workload
- D. Prepare the input dataset → confirm the workload is not interactive → validate the output → submit the job

### 86. A run records only that it finished, with no accuracy and no artifact. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Disable request logging to reduce storage cost
- C. Log metrics and the model artifact explicitly in the training script
- D. Assign the work to a person instead of investigating the failure

### 87. Retrieval hands the model a whole sixty-page manual and it quotes an unrelated section. What caused this?

Domain: Design and implement a GenAIOps infrastructure

- A. Index each document as one large chunk
- B. Retrain the model on the newer data
- C. Index every document the organization holds
- D. Chunk documents by section with a small overlap

### 88. An answer states a figure in the second paragraph and contradicts it in the fourth. Which metric catches this?

Domain: Implement generative AI quality assurance and observability

- A. Score coherence for logical structure
- B. Score groundedness against the retrieved passages
- C. Score fluency for readability and language quality
- D. Score relevance of the answer to the question asked

---

## Case study — Alpine Manufacturing

Alpine Manufacturing operates a predictive-maintenance model on 4,000 sensors across three plants. The model was trained on eighteen months of data and its accuracy has fallen from 0.91 to 0.74 since a production line was retooled, though the aggregate dashboard still looks acceptable because two other lines improved. The data science team monitors only the accuracy reported at deployment and has no baseline for the new sensor distributions. Plant engineers want an alert before a failure, and the platform team wants to know whether the fix is a retrain or something else.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Accuracy fell after a line was retooled and only deployment-time accuracy is recorded. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Retrain the model on the newer data
- B. Monitor only the accuracy reported at deployment time
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Enable data drift monitoring against the training baseline

### 90. The team needs early warning and a defensible record. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Create an alert rule on the drift and latency metrics
- B. Monitor only the accuracy reported at deployment time
- C. Retrain the model on the newer data
- D. Accept the behaviour because the aggregate score still looks healthy
- E. Assign the work to a person instead of investigating the failure

### 91. Twelve irrelevant passages are retrieved per answer. What should change?

Domain: Optimize generative AI systems and model performance

- A. Raise retrieval depth to the maximum for safety
- B. Increase the model size until the answers improve
- C. Retrieve fewer but better-ranked passages
- D. Index every document the organization holds

---

## Case study — Harborview Health

Harborview Health runs a clinical summarization service on Foundry that drafts discharge summaries from 400,000 encounters a year. Clinicians report that the service occasionally states a medication dose that appears nowhere in the record, and the quality team cannot reproduce the failures because prompts and completions are not retained. A recent red-team exercise found that a scanned document containing hidden instructions could make the assistant ignore its safety rules. The compliance office requires evidence that each released change was evaluated, and the evaluation must not be produced by the same prompt it is testing.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Drafts state medication doses that no retrieved note supports. Which metric targets this?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score coherence for logical structure
- C. Score relevance of the answer to the question asked
- D. Score fluency for readability and language quality

### 93. The assistant must ground on current records and respect access. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Set document-level access in the index so retrieval respects entitlements
- C. Index the documents in Azure AI Search and query the index from the flow
- D. Keep public network access enabled so notebooks connect easily
- E. Fine-tune the model on the document set instead of retrieving

### 94. A scanned document can make the assistant ignore its rules. What is the exposure?

Domain: Implement generative AI quality assurance and observability

- A. Test indirect injection through retrieved documents
- B. Evaluate toxicity against the threshold the audience requires
- C. Run adversarial jailbreak and prompt-injection cases before release
- D. Disable request logging to reduce storage cost

---

## Case study — Northwind MLOps

Northwind runs machine learning operations for a manufacturing group and is under pressure to cut model-release effort. Engineers train in notebooks on a compute instance, copy the resulting model file to a share, and ask a platform engineer to deploy it by hand. The group has six production models, no experiment tracking, and no agreement on which environment image a job should use, so two runs of the same script have produced different results. The platform team wants one repeatable path from commit to deployment, with an approval step before production.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. The group must tune models cheaply and stop paying for idle accelerators. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Attach a GPU cluster with four always-on nodes
- C. Attach a GPU cluster with a minimum of zero nodes
- D. Run the job from a compute instance notebook
- E. Run a full grid sweep over every combination

### 96. Platform engineers deploy by hand today and want one repeatable submission path. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Submit the job with az ml job create --file job.yaml
- B. Run the job from a compute instance notebook
- C. Create the workspace in the portal and record the steps in a wiki
- D. Stream the job with az ml job stream to inspect logs

### 97. The path from commit to deployment must not depend on a stored secret. What should authenticate it?

Domain: Design and implement an MLOps infrastructure

- A. Store a service principal client secret as a GitHub repository secret
- B. Grant the pipeline service principal Owner on the subscription
- C. Authenticate the workflow with workload identity federation and no stored secret
- D. Set the connection string as a plain environment variable in the job

---

## Case study — Woodgrove Insurance

Woodgrove Insurance runs a claims triage model and a generative assistant that explains the triage decision to adjusters. The assistant is grounded in a policy index that is rebuilt monthly, and adjusters have started escalating answers that cite an expired endorsement. The insurer must retain evidence of each model version and each evaluation result for seven years, and a regulator has asked how the triage model is monitored after deployment. A pilot team has proposed fine-tuning a model on the policy corpus instead of maintaining the index.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. A pilot proposes fine-tuning on the policy corpus instead of maintaining an index. What is the objection?

Domain: Design and implement a GenAIOps infrastructure

- A. Rebuild the index on a schedule after the source content changes
- B. Index the documents in Azure AI Search and query the index from the flow
- C. Set document-level access in the index so retrieval respects entitlements
- D. Fine-tune the model on the document set instead of retrieving

### 99. The index is rebuilt monthly and adjusters see expired endorsements. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Rebuild the index on a schedule after the source content changes
- D. Index every document the organization holds

### 100. A seven-year audit requires a pinned artifact and provenance. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Register the model and always deploy whichever version is latest
- C. Register each candidate with a version and deploy one explicit version
- D. Accept the behaviour because the aggregate score still looks healthy
- E. Tag the registered model with the data asset and commit it came from

---

## Answer key and explanations

### Question 1 — D

Answer: Create a separate Azure Machine Learning workspace per environment. A workspace per environment keeps assets and credentials apart, so a test job cannot use production connections. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A workspace per environment keeps assets and credentials apart, so a test job cannot use production connections.
- **B:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A workspace per environment keeps assets and credentials apart, so a test job cannot use production connections.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A workspace per environment keeps assets and credentials apart, so a test job cannot use production connections.
- **D:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A workspace per environment keeps assets and credentials apart, so a test job cannot use production connections.

### Question 2 — C

Answer: Register a datastore that points at the storage account. A registered datastore holds the connection and lets jobs reference data by name. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A registered datastore holds the connection and lets jobs reference data by name.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A registered datastore holds the connection and lets jobs reference data by name.
- **C:** Correct. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. In this case: A registered datastore holds the connection and lets jobs reference data by name.
- **D:** Incorrect for this question. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Why the correct answer wins: A registered datastore holds the connection and lets jobs reference data by name.

### Question 3 — D

Answer: Build a versioned curated environment for the job. A versioned curated environment pins the package set that the job resolves. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment pins the package set that the job resolves.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned curated environment pins the package set that the job resolves.
- **C:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment pins the package set that the job resolves.
- **D:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment pins the package set that the job resolves.

### Question 4 — B

Answer: Package the preparation step as a reusable component. A component gives the step one versioned implementation with a typed interface. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A component gives the step one versioned implementation with a typed interface.
- **B:** Correct. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. In this case: A component gives the step one versioned implementation with a typed interface.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A component gives the step one versioned implementation with a typed interface.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A component gives the step one versioned implementation with a typed interface.

### Question 5 — A

Answer: Register the data as a versioned data asset. A versioned data asset records the exact input used by the run. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A versioned data asset records the exact input used by the run.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A versioned data asset records the exact input used by the run.
- **C:** Incorrect for this question. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Why the correct answer wins: A versioned data asset records the exact input used by the run.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned data asset records the exact input used by the run.

### Question 6 — B

Answer: Define the workspace in a Bicep module deployed per environment. A declarative Bicep module is reviewable and recreates the environment identically. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A declarative Bicep module is reviewable and recreates the environment identically.
- **B:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A declarative Bicep module is reviewable and recreates the environment identically.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A declarative Bicep module is reviewable and recreates the environment identically.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative Bicep module is reviewable and recreates the environment identically.

### Question 7 — C

Answer: Pass environment values through a Bicep parameter file per stage. A parameter file per tenant keeps one module and varies only values. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A parameter file per tenant keeps one module and varies only values.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A parameter file per tenant keeps one module and varies only values.
- **C:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: A parameter file per tenant keeps one module and varies only values.
- **D:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A parameter file per tenant keeps one module and varies only values.

### Question 8 — B

Answer: Deploy the module as a deployment stack so removed resources are cleaned up. A deployment stack tracks what it owns and removes or denies out-of-band resources. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A deployment stack tracks what it owns and removes or denies out-of-band resources.
- **B:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: A deployment stack tracks what it owns and removes or denies out-of-band resources.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A deployment stack tracks what it owns and removes or denies out-of-band resources.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment stack tracks what it owns and removes or denies out-of-band resources.

### Question 9 — D

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI is repeatable and auditable. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and auditable.
- **B:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and auditable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and auditable.
- **D:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI is repeatable and auditable.

### Question 10 — D

Answer: Stream the job with az ml job stream to inspect logs. Streaming attaches to the live job log. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Streaming attaches to the live job log.
- **B:** Incorrect for this question. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Why the correct answer wins: Streaming attaches to the live job log.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Streaming attaches to the live job log.
- **D:** Correct. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. In this case: Streaming attaches to the live job log.

### Question 11 — D

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation exchanges the workflow token for a credential with no stored secret. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential with no stored secret.
- **B:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential with no stored secret.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential with no stored secret.
- **D:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation exchanges the workflow token for a credential with no stored secret.

### Question 12 — B

Answer: Use GitHub environment protection rules to gate the production deploy job. A protected environment enforces approval before the job runs. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit. Why the correct answer wins: A protected environment enforces approval before the job runs.
- **B:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: A protected environment enforces approval before the job runs.
- **C:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: A protected environment enforces approval before the job runs.
- **D:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: A protected environment enforces approval before the job runs.

### Question 13 — A

Answer: Store connection strings in Key Vault and reference them by name. Key Vault centralizes the secret so rotation happens once, outside the code. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. In this case: Key Vault centralizes the secret so rotation happens once, outside the code.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Key Vault centralizes the secret so rotation happens once, outside the code.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: Key Vault centralizes the secret so rotation happens once, outside the code.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Key Vault centralizes the secret so rotation happens once, outside the code.

### Question 14 — C, D

Answers: Register each candidate with a version and deploy one explicit version; Tag the registered model with the data asset and commit it came from. An explicit version pins the artifact, and tags record the data asset and commit. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit version pins the artifact, and tags record the data asset and commit.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit version pins the artifact, and tags record the data asset and commit.
- **C:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: An explicit version pins the artifact, and tags record the data asset and commit.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit version pins the artifact, and tags record the data asset and commit.
- **E:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit version pins the artifact, and tags record the data asset and commit.

### Question 15 — A, C

Answers: Define the workspace in a Bicep module deployed per environment; Deploy the module as a deployment stack so removed resources are cleaned up. Bicep defines the shape, and a deployment stack removes or denies drift. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: Bicep defines the shape, and a deployment stack removes or denies drift.
- **B:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes or denies drift.
- **C:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: Bicep defines the shape, and a deployment stack removes or denies drift.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes or denies drift.
- **E:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes or denies drift.

### Question 16 — B

Answer: Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content. Scope is inventoried first, identity replaces the secret, the grant is minimal, and verification proves it. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Verification precedes the configuration it verifies, and the inventory comes last. Why the correct answer wins: Scope is inventoried first, identity replaces the secret, the grant is minimal, and verification proves it.
- **B:** Correct. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. In this case: Scope is inventoried first, identity replaces the secret, the grant is minimal, and verification proves it.
- **C:** Incorrect for this question. The answer is verified before any role has been granted, and the sources are inventoried after the grant. Why the correct answer wins: Scope is inventoried first, identity replaces the secret, the grant is minimal, and verification proves it.
- **D:** Incorrect for this question. A broad grant is made before the sources are known, and the identity is assigned after it has been granted permissions. Why the correct answer wins: Scope is inventoried first, identity replaces the secret, the grant is minimal, and verification proves it.

### Question 17 — A

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline job records each step input and output explicitly. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline job records each step input and output explicitly.
- **B:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline job records each step input and output explicitly.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A pipeline job records each step input and output explicitly.
- **D:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A pipeline job records each step input and output explicitly.

### Question 18 — B

Answer: Run the whole workflow as a single script job. Separate steps make the failing stage visible and rerunnable. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: Separate steps make the failing stage visible and rerunnable.
- **B:** Correct. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. In this case: Separate steps make the failing stage visible and rerunnable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Separate steps make the failing stage visible and rerunnable.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Separate steps make the failing stage visible and rerunnable.

### Question 19 — D

Answer: Use automated ML to establish the tabular baseline. Automated ML tests combinations quickly and produces a baseline. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML tests combinations quickly and produces a baseline.
- **B:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML tests combinations quickly and produces a baseline.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML tests combinations quickly and produces a baseline.
- **D:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML tests combinations quickly and produces a baseline.

### Question 20 — D

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum stops billing between runs. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **B:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **C:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **D:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum stops billing between runs.

### Question 21 — A

Answer: Run a full grid sweep over every combination. A sampled sweep finds the promising region without exhaustive coverage. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. In this case: A sampled sweep finds the promising region without exhaustive coverage.
- **B:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: A sampled sweep finds the promising region without exhaustive coverage.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A sampled sweep finds the promising region without exhaustive coverage.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep finds the promising region without exhaustive coverage.

### Question 22 — B

Answer: Point the MLflow tracking URI at the workspace endpoint. The tracking URI must point at the workspace endpoint. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **B:** Correct. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. In this case: The tracking URI must point at the workspace endpoint.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: The tracking URI must point at the workspace endpoint.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: The tracking URI must point at the workspace endpoint.

### Question 23 — D

Answer: Group the trials under a named experiment. A named experiment groups runs so variants compare against each other. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **C:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups runs so variants compare against each other.
- **D:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups runs so variants compare against each other.

### Question 24 — D

Answer: Register each candidate with a version and deploy one explicit version. An explicit version pins what is served. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An explicit version pins what is served.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit version pins what is served.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit version pins what is served.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit version pins what is served.

### Question 25 — C

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports the decision. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports the decision.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports the decision.
- **C:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports the decision.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A model card with metrics and intended use supports the decision.

### Question 26 — D

Answer: Overwrite the existing model version instead of registering a new one. Overwriting destroys the artifact and the audit trail. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.
- **B:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Overwriting destroys the artifact and the audit trail.
- **D:** Correct. Overwriting destroys the previous artifact and the audit trail that rollback depends on. In this case: Overwriting destroys the artifact and the audit trail.

### Question 27 — B

Answer: Deploy to a managed online endpoint with an explicit model version. A managed online endpoint serves synchronous requests. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **B:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: A managed online endpoint serves synchronous requests.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A managed online endpoint serves synchronous requests.
- **D:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: A managed online endpoint serves synchronous requests.

### Question 28 — A

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact decouples the model version from the image. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact decouples the model version from the image.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **C:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact decouples the model version from the image.

### Question 29 — C

Answer: Configure liveness and readiness probes on the deployment. A readiness probe withholds traffic until the container can serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe withholds traffic until the container can serve.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe withholds traffic until the container can serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe withholds traffic until the container can serve.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe withholds traffic until the container can serve.

### Question 30 — D

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split sends a bounded canary share. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split sends a bounded canary share.
- **B:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split sends a bounded canary share.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split sends a bounded canary share.
- **D:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split sends a bounded canary share.

### Question 31 — D

Answer: Keep the previous deployment in place so traffic can be moved back. A retained previous deployment makes rollback a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained previous deployment makes rollback a traffic change.
- **B:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained previous deployment makes rollback a traffic change.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained previous deployment makes rollback a traffic change.
- **D:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained previous deployment makes rollback a traffic change.

### Question 32 — A

Answer: Send the overnight file through the online endpoint request by request. Bulk scoring through an online endpoint wastes capacity and is slow. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. In this case: Bulk scoring through an online endpoint wastes capacity and is slow.
- **B:** Incorrect for this question. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Why the correct answer wins: Bulk scoring through an online endpoint wastes capacity and is slow.
- **C:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: Bulk scoring through an online endpoint wastes capacity and is slow.
- **D:** Incorrect for this question. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Why the correct answer wins: Bulk scoring through an online endpoint wastes capacity and is slow.

### Question 33 — C

Answer: Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale follows load with a deliberate minimum. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale follows load with a deliberate minimum.
- **C:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale follows load with a deliberate minimum.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale follows load with a deliberate minimum.

### Question 34 — B

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **B:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 35 — B

Answer: Monitor only the accuracy reported at deployment time. A deployment-time snapshot says nothing about subsequent data. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **B:** Correct. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. In this case: A deployment-time snapshot says nothing about subsequent data.
- **C:** Incorrect for this question. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **D:** Incorrect for this question. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.

### Question 36 — C, D

Answers: Configure liveness and readiness probes on the deployment; Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale matches capacity to load, and probes gate traffic until ready. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until ready.
- **B:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until ready.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: Autoscale matches capacity to load, and probes gate traffic until ready.
- **D:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity to load, and probes gate traffic until ready.
- **E:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until ready.

### Question 37 — C, D

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. The traffic split bounds exposure, and the retained deployment makes reversal cheap. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment makes reversal cheap.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment makes reversal cheap.
- **C:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: The traffic split bounds exposure, and the retained deployment makes reversal cheap.
- **D:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: The traffic split bounds exposure, and the retained deployment makes reversal cheap.
- **E:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment makes reversal cheap.

### Question 38 — B

Answer: Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold. Each step consumes the artifact the previous step produced, ending with a measured canary. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target. Why the correct answer wins: Each step consumes the artifact the previous step produced, ending with a measured canary.
- **B:** Correct. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. In this case: Each step consumes the artifact the previous step produced, ending with a measured canary.
- **C:** Incorrect for this question. Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version. Why the correct answer wins: Each step consumes the artifact the previous step produced, ending with a measured canary.
- **D:** Incorrect for this question. A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic. Why the correct answer wins: Each step consumes the artifact the previous step produced, ending with a measured canary.

### Question 39 — C

Answer: Publish the component to the registry → build a versioned environment that pins its dependencies → reference both from the pipeline YAML → run the pipeline in the test environment. Assets are published and pinned before the YAML references them, and the run comes last. The reusable assets must exist and be versioned before a pipeline can reference them, and the run comes last. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. The pipeline runs before its references exist, and the assets are published afterwards. Why the correct answer wins: Assets are published and pinned before the YAML references them, and the run comes last.
- **B:** Incorrect for this question. The run precedes both the component publication and the YAML reference that would make it resolvable. Why the correct answer wins: Assets are published and pinned before the YAML references them, and the run comes last.
- **C:** Correct. The reusable assets must exist and be versioned before a pipeline can reference them, and the run comes last. In this case: Assets are published and pinned before the YAML references them, and the run comes last.
- **D:** Incorrect for this question. The YAML references assets that have not been published or built yet. Why the correct answer wins: Assets are published and pinned before the YAML references them, and the run comes last.

### Question 40 — A

Answer: Create a Foundry hub and a project per team. A hub shares capacity while a project isolates each team's assets. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity while a project isolates each team's assets.
- **B:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.
- **C:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.

### Question 41 — C

Answer: Reference the deployment name from the flow rather than the model family name. A deployment name is the stable reference a flow calls. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A deployment name is the stable reference a flow calls.
- **B:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A deployment name is the stable reference a flow calls.
- **C:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A deployment name is the stable reference a flow calls.
- **D:** Incorrect for this question. The catalog lists models with their capabilities; deploying one into the project makes it addressable by a deployment name. Why the correct answer wins: A deployment name is the stable reference a flow calls.

### Question 42 — A

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput gives predictable cost and latency at sustained volume. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput gives predictable cost and latency at sustained volume.
- **B:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.
- **C:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput gives predictable cost and latency at sustained volume.

### Question 43 — D

Answer: Start on pay-as-you-go while the volume is still unknown. Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **D:** Correct. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. In this case: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.

### Question 44 — C

Answer: Assign a managed identity to compute and grant it the storage role. A managed identity removes the credential from configuration entirely. A managed identity removes credentials from code entirely and is granted only the role the step needs. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: A managed identity removes the credential from configuration entirely.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A managed identity removes the credential from configuration entirely.
- **C:** Correct. A managed identity removes credentials from code entirely and is granted only the role the step needs. In this case: A managed identity removes the credential from configuration entirely.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A managed identity removes the credential from configuration entirely.

### Question 45 — A

Answer: Paste the API key into a Python node inside the flow. A key in a flow file is a secret in source control. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. In this case: A key in a flow file is a secret in source control.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A key in a flow file is a secret in source control.
- **C:** Incorrect for this question. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Why the correct answer wins: A key in a flow file is a secret in source control.
- **D:** Incorrect for this question. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Why the correct answer wins: A key in a flow file is a secret in source control.

### Question 46 — C

Answer: Index the documents in Azure AI Search and query the index from the flow. An index supports retrieval against current content. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: An index supports retrieval against current content.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: An index supports retrieval against current content.
- **C:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: An index supports retrieval against current content.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: An index supports retrieval against current content.

### Question 47 — D

Answer: Use hybrid search with semantic ranking. Hybrid search retains keyword matching for exact identifiers. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **C:** Incorrect for this question. Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **D:** Correct. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. In this case: Hybrid search retains keyword matching for exact identifiers.

### Question 48 — D

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.

### Question 49 — A

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap make the cited passage specific. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap make the cited passage specific.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **C:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.
- **D:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap make the cited passage specific.

### Question 50 — C

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh aligns retrieval with the source. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **C:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh aligns retrieval with the source.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.

### Question 51 — A

Answer: Keep the prompt in its own file under version control. A separate versioned prompt file makes the change reviewable. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A separate versioned prompt file makes the change reviewable.
- **B:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A separate versioned prompt file makes the change reviewable.
- **C:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A separate versioned prompt file makes the change reviewable.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A separate versioned prompt file makes the change reviewable.

### Question 52 — B

Answer: Run the evaluation in continuous integration before the flow is promoted. An offline evaluation gate before promotion. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An offline evaluation gate before promotion.
- **B:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An offline evaluation gate before promotion.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An offline evaluation gate before promotion.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An offline evaluation gate before promotion.

### Question 53 — A

Answer: Register a scoped tool list for the agent. A scoped tool list bounds what the agent may call. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds what the agent may call.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **C:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds what the agent may call.

### Question 54 — B, E

Answers: Author the flow as a directed acyclic graph with typed inputs and outputs; Create a variant to compare two prompt strategies side by side. A typed graph makes steps testable, and variants hold strategies side by side. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A typed graph makes steps testable, and variants hold strategies side by side.
- **B:** Correct. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. In this case: A typed graph makes steps testable, and variants hold strategies side by side.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A typed graph makes steps testable, and variants hold strategies side by side.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A typed graph makes steps testable, and variants hold strategies side by side.
- **E:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: A typed graph makes steps testable, and variants hold strategies side by side.

### Question 55 — A, C

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing enables grounding, and document-level access enforces entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **C:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **D:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **E:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.

### Question 56 — B, E

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file is the change record, and the offline gate is the quality control. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned prompt file is the change record, and the offline gate is the quality control.
- **B:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the change record, and the offline gate is the quality control.
- **C:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the change record, and the offline gate is the quality control.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file is the change record, and the offline gate is the quality control.
- **E:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file is the change record, and the offline gate is the quality control.

### Question 57 — B, C

Answers: Register a scoped tool list for the agent; Bound the agent memory to the current session. A scoped tool list bounds actions, and session-scoped memory bounds retention. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds actions, and session-scoped memory bounds retention.
- **B:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds actions, and session-scoped memory bounds retention.
- **C:** Correct. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. In this case: A scoped tool list bounds actions, and session-scoped memory bounds retention.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds actions, and session-scoped memory bounds retention.
- **E:** Incorrect for this question. Typed state makes each handoff explicit and testable instead of relying on free text. Why the correct answer wins: A scoped tool list bounds actions, and session-scoped memory bounds retention.

### Question 58 — A

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation build on each other in that order. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **B:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **C:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **D:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.

### Question 59 — B

Answer: Build the evaluation dataset from real queries with graded answers. Real queries with graded answers are what make the result defensible. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries with graded answers are what make the result defensible.
- **B:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries with graded answers are what make the result defensible.
- **C:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries with graded answers are what make the result defensible.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries with graded answers are what make the result defensible.

### Question 60 — C

Answer: Use a few hundred representative cases rather than a dozen. A set that small has too wide a confidence interval to separate a gain from noise. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A set that small has too wide a confidence interval to separate a gain from noise.
- **B:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A set that small has too wide a confidence interval to separate a gain from noise.
- **C:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: A set that small has too wide a confidence interval to separate a gain from noise.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A set that small has too wide a confidence interval to separate a gain from noise.

### Question 61 — B

Answer: Use an LLM judge with a rubric, calibrated against human grades. An LLM judge calibrated against human grades scales the work. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An LLM judge calibrated against human grades scales the work.
- **B:** Correct. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. In this case: An LLM judge calibrated against human grades scales the work.
- **C:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: An LLM judge calibrated against human grades scales the work.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: An LLM judge calibrated against human grades scales the work.

### Question 62 — B

Answer: Score groundedness against the retrieved passages. Groundedness measures support by the retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures support by the retrieved context.
- **B:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support by the retrieved context.
- **C:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support by the retrieved context.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support by the retrieved context.

### Question 63 — A

Answer: Score relevance of the answer to the question asked. Relevance measures whether the answer addresses the question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Relevance measures whether the answer addresses the question.
- **B:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **C:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Relevance measures whether the answer addresses the question.

### Question 64 — C

Answer: Run adversarial jailbreak and prompt-injection cases before release. Jailbreak testing measures resistance to override attempts. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Jailbreak testing measures resistance to override attempts.
- **B:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Jailbreak testing measures resistance to override attempts.
- **C:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Jailbreak testing measures resistance to override attempts.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Jailbreak testing measures resistance to override attempts.

### Question 65 — A

Answer: Test indirect injection through retrieved documents. Indirect injection tests instructions hidden in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection tests instructions hidden in retrieved content.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection tests instructions hidden in retrieved content.
- **C:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection tests instructions hidden in retrieved content.
- **D:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection tests instructions hidden in retrieved content.

### Question 66 — B

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing shows the failing stage. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing shows the failing stage.
- **B:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing shows the failing stage.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing shows the failing stage.
- **D:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing shows the failing stage.

### Question 67 — D

Answer: Capture user feedback and review a sample of rated conversations weekly. Capturing and triaging feedback surfaces traffic the dataset lacks. User feedback is the only signal about traffic that the evaluation set does not contain. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Online evaluation catches the drift that a fixed offline dataset cannot represent. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **B:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **C:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **D:** Correct. User feedback is the only signal about traffic that the evaluation set does not contain. In this case: Capturing and triaging feedback surfaces traffic the dataset lacks.

### Question 68 — A, D

Answers: Run adversarial jailbreak and prompt-injection cases before release; Test indirect injection through retrieved documents. Jailbreak cases test user input, and indirect cases test retrieved content. Adversarial cases test whether instructions in the input or the content can override the system prompt. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Jailbreak cases test user input, and indirect cases test retrieved content.
- **B:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Jailbreak cases test user input, and indirect cases test retrieved content.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Jailbreak cases test user input, and indirect cases test retrieved content.
- **D:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Jailbreak cases test user input, and indirect cases test retrieved content.
- **E:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Jailbreak cases test user input, and indirect cases test retrieved content.

### Question 69 — D, E

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing attributes the failure to a stage, and prompt logging allows replay. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing attributes the failure to a stage, and prompt logging allows replay.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing attributes the failure to a stage, and prompt logging allows replay.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing attributes the failure to a stage, and prompt logging allows replay.
- **D:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing attributes the failure to a stage, and prompt logging allows replay.
- **E:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing attributes the failure to a stage, and prompt logging allows replay.

### Question 70 — D

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace identifies the stage, retrieval shows whether the passage existed, and the case joins the regression set. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace identifies the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **B:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace identifies the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **C:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace identifies the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **D:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace identifies the stage, retrieval shows whether the passage existed, and the case joins the regression set.

### Question 71 — B

Answer: Cache identical requests and reuse the completion. Caching removes repeated inference for identical input. Caching removes repeated inference for identical input, which is the cheapest saving available. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Caching removes repeated inference for identical input.
- **B:** Correct. Caching removes repeated inference for identical input, which is the cheapest saving available. In this case: Caching removes repeated inference for identical input.
- **C:** Incorrect for this question. A TTL keeps a cached answer from outliving the content it came from. Why the correct answer wins: Caching removes repeated inference for identical input.
- **D:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Caching removes repeated inference for identical input.

### Question 72 — C

Answer: Set a time-to-live on the cache. A TTL stops a cached answer outliving its source. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **C:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A TTL stops a cached answer outliving its source.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A TTL stops a cached answer outliving its source.

### Question 73 — C

Answer: Add a router that classifies the request and selects a model. A router classifies and selects an appropriate model. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router classifies and selects an appropriate model.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router classifies and selects an appropriate model.
- **C:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router classifies and selects an appropriate model.
- **D:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router classifies and selects an appropriate model.

### Question 74 — C

Answer: Route simple requests to a smaller model. A smaller model handles simple requests at lower cost. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A smaller model handles simple requests at lower cost.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A smaller model handles simple requests at lower cost.
- **C:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A smaller model handles simple requests at lower cost.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A smaller model handles simple requests at lower cost.

### Question 75 — C

Answer: Use the largest model for every request. The largest model adds cost and latency where its capability is not needed. The largest model adds cost and latency to requests that do not need its capability. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: The largest model adds cost and latency where its capability is not needed.
- **B:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: The largest model adds cost and latency where its capability is not needed.
- **C:** Correct. The largest model adds cost and latency to requests that do not need its capability. In this case: The largest model adds cost and latency where its capability is not needed.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: The largest model adds cost and latency where its capability is not needed.

### Question 76 — D

Answer: Stream the response so the first token arrives sooner. Streaming delivers the first token sooner. Streaming improves perceived latency without changing total generation time. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Streaming delivers the first token sooner.
- **B:** Incorrect for this question. Batch work uses cheaper capacity and takes the work off the interactive path. Why the correct answer wins: Streaming delivers the first token sooner.
- **C:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Streaming delivers the first token sooner.
- **D:** Correct. Streaming improves perceived latency without changing total generation time. In this case: Streaming delivers the first token sooner.

### Question 77 — A

Answer: Retrieve fewer but better-ranked passages. Fewer, better-ranked passages cut tokens and improve precision. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer, better-ranked passages cut tokens and improve precision.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **C:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.

### Question 78 — B

Answer: Compress the system prompt and remove redundant instructions. Compressing the prompt cuts input tokens on every call. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **B:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Compressing the prompt cuts input tokens on every call.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.

### Question 79 — B

Answer: Fine-tune on approved examples to shorten the standing prompt. Fine-tuning can move stable instructions into the weights. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **B:** Correct. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. In this case: Fine-tuning can move stable instructions into the weights.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **D:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.

### Question 80 — C

Answer: Move non-urgent generation into a batch run. Batch work uses cheaper capacity off the interactive path. Batch work uses cheaper capacity and takes the work off the interactive path. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Streaming improves perceived latency without changing total generation time. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **B:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.
- **C:** Correct. Batch work uses cheaper capacity and takes the work off the interactive path. In this case: Batch work uses cheaper capacity off the interactive path.
- **D:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Batch work uses cheaper capacity off the interactive path.

### Question 81 — D, E

Answers: Measure tokens per request and set a budget per endpoint; Set a time-to-live on the cache. A token budget attributes cost, and a TTL keeps answers current. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **D:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: A token budget attributes cost, and a TTL keeps answers current.
- **E:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A token budget attributes cost, and a TTL keeps answers current.

### Question 82 — D, E

Answers: Add a router that classifies the request and selects a model; Route simple requests to a smaller model. A router selects per request, and a smaller model covers the simple majority. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects per request, and a smaller model covers the simple majority.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects per request, and a smaller model covers the simple majority.
- **E:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A router selects per request, and a smaller model covers the simple majority.

### Question 83 — D

Answer: Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held. Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A driver is named before measurement, and the evaluation runs before the change exists. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **B:** Incorrect for this question. Evaluation precedes both the change it would validate and the measurement that motivates it. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **C:** Incorrect for this question. An optimization is applied before anything has been measured or attributed. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.
- **D:** Correct. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. In this case: Measurement attributes spend, the breakdown picks the lever, and evaluation makes the saving safe.

### Question 84 — B

Answer: Edit the prompt file in a branch → run the offline evaluation gate → review the diff and metric change in a pull request → deploy the approved version and watch the online metrics. The edit is measured before review, review precedes deployment, and online metrics confirm the offline result. The change is measured before review, review happens before deployment, and online metrics confirm the offline result. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. The diff cannot be reviewed before the edit, and deployment precedes the gate that would block it. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the offline result.
- **B:** Correct. The change is measured before review, review happens before deployment, and online metrics confirm the offline result. In this case: The edit is measured before review, review precedes deployment, and online metrics confirm the offline result.
- **C:** Incorrect for this question. The gate runs before the prompt is edited, so it measures the old wording and clears the way for an unreviewed deploy. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the offline result.
- **D:** Incorrect for this question. A version is deployed before it has been edited, evaluated, or reviewed. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the offline result.

### Question 85 — B

Answer: Confirm the workload is not interactive → prepare a batch input dataset → submit the batch endpoint job → validate the output file against the schema. The interaction requirement decides the pattern, input precedes submission, and the output is validated after. The interaction requirement decides the pattern, the input must exist before submission, and the output is validated afterwards. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A batch job is submitted before its input exists and before anyone confirmed batch is the right pattern. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and the output is validated after.
- **B:** Correct. The interaction requirement decides the pattern, the input must exist before submission, and the output is validated afterwards. In this case: The interaction requirement decides the pattern, input precedes submission, and the output is validated after.
- **C:** Incorrect for this question. The output is validated before the job that produces it has run. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and the output is validated after.
- **D:** Incorrect for this question. Validation happens before submission, so there is no output to check. Why the correct answer wins: The interaction requirement decides the pattern, input precedes submission, and the output is validated after.

### Question 86 — C

Answer: Log metrics and the model artifact explicitly in the training script. Explicit logging of metrics and the model artifact is required for a comparable run. Explicit logging captures the numbers and artifact a comparison needs; without it the run records only that it happened. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Explicit logging of metrics and the model artifact is required for a comparable run.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Explicit logging of metrics and the model artifact is required for a comparable run.
- **C:** Correct. Explicit logging captures the numbers and artifact a comparison needs; without it the run records only that it happened. In this case: Explicit logging of metrics and the model artifact is required for a comparable run.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Explicit logging of metrics and the model artifact is required for a comparable run.

### Question 87 — A

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate the relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate the relevant text.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate the relevant text.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate the relevant text.
- **D:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate the relevant text.

### Question 88 — A

Answer: Score coherence for logical structure. Coherence measures whether the answer holds together logically. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. In this case: Coherence measures whether the answer holds together logically.
- **B:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Coherence measures whether the answer holds together logically.
- **D:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Coherence measures whether the answer holds together logically.

### Question 89 — D

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.

### Question 90 — A, B

Answers: Create an alert rule on the drift and latency metrics; Monitor only the accuracy reported at deployment time. An alert turns the metric into action, and the recorded baseline makes the comparison meaningful. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into action, and the recorded baseline makes the comparison meaningful.
- **B:** Correct. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. In this case: An alert turns the metric into action, and the recorded baseline makes the comparison meaningful.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: An alert turns the metric into action, and the recorded baseline makes the comparison meaningful.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An alert turns the metric into action, and the recorded baseline makes the comparison meaningful.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into action, and the recorded baseline makes the comparison meaningful.

### Question 91 — C

Answer: Retrieve fewer but better-ranked passages. Fewer, better-ranked passages improve precision and cut cost. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer, better-ranked passages improve precision and cut cost.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer, better-ranked passages improve precision and cut cost.
- **C:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer, better-ranked passages improve precision and cut cost.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Fewer, better-ranked passages improve precision and cut cost.

### Question 92 — A

Answer: Score groundedness against the retrieved passages. Groundedness measures support by the retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support by the retrieved context.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support by the retrieved context.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures support by the retrieved context.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support by the retrieved context.

### Question 93 — B, C

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing enables grounding, and document-level access enforces entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **B:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **C:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing enables grounding, and document-level access enforces entitlement.
- **D:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.
- **E:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing enables grounding, and document-level access enforces entitlement.

### Question 94 — A

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.
- **B:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **C:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.

### Question 95 — A, C

Answers: Run a sweep job over a searched hyperparameter space; Attach a GPU cluster with a minimum of zero nodes. A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. In this case: A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing.
- **B:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing.
- **C:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing.
- **E:** Incorrect for this question. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Why the correct answer wins: A sampled sweep bounds trial cost, and a zero-minimum GPU cluster stops idle billing.

### Question 96 — A

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI is repeatable and can run in a pipeline. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI is repeatable and can run in a pipeline.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and can run in a pipeline.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and can run in a pipeline.
- **D:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI is repeatable and can run in a pipeline.

### Question 97 — C

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation removes the stored secret. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation removes the stored secret.
- **B:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation removes the stored secret.
- **C:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation removes the stored secret.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation removes the stored secret.

### Question 98 — D

Answer: Fine-tune the model on the document set instead of retrieving. Fine-tuning bakes a snapshot that goes stale as policies change. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as policies change.
- **B:** Incorrect for this question. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as policies change.
- **C:** Incorrect for this question. Document-level access keeps retrieval within what the requesting user is allowed to see. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as policies change.
- **D:** Correct. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. In this case: Fine-tuning bakes a snapshot that goes stale as policies change.

### Question 99 — C

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh keeps retrieval aligned with current policy. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with current policy.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with current policy.
- **C:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh keeps retrieval aligned with current policy.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with current policy.

### Question 100 — C, E

Answers: Register each candidate with a version and deploy one explicit version; Tag the registered model with the data asset and commit it came from. An explicit version pins the artifact, and tags record where it came from. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit version pins the artifact, and tags record where it came from.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit version pins the artifact, and tags record where it came from.
- **C:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit version pins the artifact, and tags record where it came from.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit version pins the artifact, and tags record where it came from.
- **E:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: An explicit version pins the artifact, and tags record where it came from.
