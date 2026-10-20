# AIF-C01 — Practice Set 1

100 questions · Suggested time: 140 minutes · Practice target: 80%

Select one answer unless the question says Select TWO. Answers and explanations follow all questions.

These are original learning questions, not actual AWS exam questions.

## Questions

### 1. A default predictor uses a field recorded only after the borrower defaults. What evaluation risk is present?

Domain: Fundamentals of AI and ML

- A. Data distribution drift
- B. Overfitting
- C. Underfitting
- D. Data leakage

### 2. Two models meet the same task-quality requirements, but one uses substantially fewer computational resources. Which responsible selection practice should guide comparison?

Domain: Guidelines for Responsible AI

- A. More training epochs alone
- B. Evaluate environmental efficiency alongside task quality
- C. Always fill the entire context window
- D. A larger model alone

### 3. An application needs to cap the length of generated responses. Which setting is most directly relevant?

Domain: Fundamentals of GenAI

- A. Maximum output tokens
- B. Temperature
- C. Top-p sampling
- D. Embedding

### 4. An ML team wants AWS tooling for potential bias analysis and model explanations. Which capability fits?

Domain: Guidelines for Responsible AI

- A. Amazon SageMaker Clarify
- B. AWS CloudTrail
- C. Amazon Textract
- D. Amazon SageMaker Model Cards

### 5. A team needs an independent estimate of how an adapted assistant performs on real user tasks. What should it use?

Domain: Applications of Foundation Models

- A. Always fill the entire context window
- B. Representative held-out evaluation prompts
- C. More training epochs alone
- D. A larger model alone

### 6. A sampler considers only the 20 most likely next tokens. Which decoding control is this?

Domain: Fundamentals of GenAI

- A. Top-k sampling
- B. Top-p sampling
- C. Temperature
- D. Maximum output tokens

### 7. A model endpoint needs alarms for elevated latency and error metrics. Which AWS service fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. AWS Key Management Service (AWS KMS)
- B. AWS CloudTrail
- C. Amazon CloudWatch
- D. AWS Artifact

### 8. A company plans to use third-party images for model adaptation. Which review is needed before assuming reuse is permitted?

Domain: Guidelines for Responsible AI

- A. Check content rights and licensing
- B. Token
- C. Maximum output tokens
- D. Temperature

### 9. An LLM cannot accept an entire manual plus a desired response in one request. Which limit is being reached?

Domain: Fundamentals of GenAI

- A. Top-k sampling
- B. Context window
- C. Temperature
- D. Maximum output tokens

### 10. An organization assumes a managed AI service removes all customer security duties. Which concept corrects this assumption?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Grant broad administrator access to every caller
- B. Make all internal documents publicly accessible
- C. Deploy without evaluation
- D. Shared responsibility model

### 11. A RAG assistant retrieves the right document but adds unsupported claims. Which evaluation dimension targets this failure?

Domain: Applications of Foundation Models

- A. Token and request cost measurement
- B. Inference latency
- C. Retrieval relevance evaluation
- D. Groundedness evaluation

### 12. A query uses different wording from a relevant document but should still retrieve it by meaning. Which retrieval technique fits?

Domain: Applications of Foundation Models

- A. Vector similarity search
- B. Classification
- C. Exact keyword search
- D. Regression

### 13. A company prepares a public-facing GenAI release. Which TWO practices strengthen responsible deployment? (Select TWO.)

Domain: Guidelines for Responsible AI

- A. Treat a safety filter as a complete guarantee
- B. Adversarial testing and red teaming
- C. Stop monitoring after launch
- D. Deploy without evaluation
- E. Document intended uses and known limitations

### 14. A retailer scores five million historical records overnight with no immediate response requirement. Which inference mode fits?

Domain: Fundamentals of AI and ML

- A. Real-time inference
- B. Training
- C. Batch inference
- D. Validation

### 15. An application creates original product descriptions from attributes. Which modeling capability is this?

Domain: Fundamentals of GenAI

- A. Classification
- B. Regression
- C. Clustering
- D. Generative modeling

### 16. A team has many approved examples and needs persistent task-specific behavior through weight updates. Which method fits?

Domain: Applications of Foundation Models

- A. Fine-tuning
- B. Pretraining
- C. Retrieval-Augmented Generation (RAG)
- D. Prompt engineering

### 17. A prompt begins act as a concise technical editor. Which technique is this?

Domain: Applications of Foundation Models

- A. Fine-tuning
- B. Model distillation
- C. Role-based prompting
- D. Retrieval-Augmented Generation (RAG)

### 18. Employees need an enterprise assistant that answers questions over supported connected company content. Which service fits?

Domain: Fundamentals of GenAI

- A. Amazon SageMaker Ground Truth
- B. Amazon Q Business
- C. Amazon Q Developer
- D. Amazon Polly

### 19. A simulated warehouse robot receives rewards for safe, efficient deliveries. Which learning approach fits?

Domain: Fundamentals of AI and ML

- A. Deterministic rule-based processing
- B. Unsupervised learning
- C. Reinforcement learning
- D. Supervised learning

### 20. An application must access a supported AWS service through a VPC endpoint without public internet routing for that traffic. Which technology fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Amazon CloudWatch
- B. Encryption in transit using TLS
- C. AWS Key Management Service (AWS KMS)
- D. AWS PrivateLink

### 21. A price predictor must be evaluated by average absolute error in dollars. Which metric fits?

Domain: Fundamentals of AI and ML

- A. Recall
- B. Mean absolute error
- C. Precision
- D. Accuracy

### 22. A company needs to discover personal information in Amazon S3 datasets before AI use. Which service fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. AWS Artifact
- B. Amazon Macie
- C. AWS Key Management Service (AWS KMS)
- D. Amazon CloudWatch

### 23. A team compares two foundation models for a production assistant. Which TWO evaluation activities are essential? (Select TWO.)

Domain: Fundamentals of GenAI

- A. A larger model alone
- B. Token and request cost measurement
- C. Task-specific quality evaluation
- D. More training epochs alone
- E. Deploy without evaluation

### 24. A retailer needs sentiment detection in customer reviews. Which AWS service fits?

Domain: Fundamentals of AI and ML

- A. Amazon Translate
- B. Amazon Transcribe
- C. Amazon Rekognition
- D. Amazon Comprehend

### 25. A team needs to know which prompt revision caused a drop in quality and restore the prior revision. Which practice fits?

Domain: Applications of Foundation Models

- A. Versioned prompt management
- B. Model quantization
- C. Embedding
- D. Temperature

### 26. An assistant's output feeds software that requires valid JSON with specific fields. Which approach is best?

Domain: Applications of Foundation Models

- A. Top-k sampling
- B. Temperature
- C. Explicit output schema and validation
- D. Context window

### 27. A team compares generated summaries with reference summaries using recall-oriented text overlap. Which metric fits?

Domain: Applications of Foundation Models

- A. BLEU
- B. Precision
- C. ROUGE
- D. Mean absolute error

### 28. An internal RAG assistant may encounter malicious instructions in documents. Which TWO controls should be applied? (Select TWO.)

Domain: Security, Compliance, and Governance for AI Solutions

- A. Enforce authorization before retrieval and actions
- B. Grant broad administrator access to every caller
- C. Deploy without evaluation
- D. Treat retrieved content as untrusted data
- E. Make all internal documents publicly accessible

### 29. A contact center needs text transcripts of recorded calls. Which service fits?

Domain: Fundamentals of AI and ML

- A. Amazon Translate
- B. Amazon Textract
- C. Amazon Polly
- D. Amazon Transcribe

### 30. A complex document request is split into extract facts, compare records, and draft a summary. Which technique is this?

Domain: Applications of Foundation Models

- A. Model distillation
- B. Pretraining
- C. Temperature
- D. Task decomposition

### 31. A prototype has unpredictable, low inference traffic and wants no reserved capacity commitment. Which Bedrock access option fits?

Domain: Fundamentals of GenAI

- A. Pretraining
- B. On-demand inference
- C. Provisioned Throughput
- D. Fine-tuning

### 32. A document assistant should retrieve only documents marked finance. Which retrieval control fits?

Domain: Applications of Foundation Models

- A. Top-k sampling
- B. Maximum output tokens
- C. Temperature
- D. Metadata filtering

### 33. A chatbot must actually check live inventory through an API rather than guess. Which capability is needed?

Domain: Applications of Foundation Models

- A. Embedding
- B. Tool or action invocation
- C. Fine-tuning
- D. Generative modeling

### 34. A vision model should remain reliable when lighting conditions change within its intended setting. Which dimension is this?

Domain: Guidelines for Responsible AI

- A. Inference latency
- B. Robustness
- C. Accuracy
- D. Token and request cost measurement

### 35. A GenAI application stores prompts that may contain personal information. Which TWO governance practices are appropriate? (Select TWO.)

Domain: Security, Compliance, and Governance for AI Solutions

- A. Defined retention and deletion policies
- B. Grant broad administrator access to every caller
- C. Make all internal documents publicly accessible
- D. Stop monitoring after launch
- E. Data minimization

### 36. A company must ensure its AI data processing meets geographic restrictions. Which review is needed?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Data residency and processing-location review
- B. Maximum output tokens
- C. Temperature
- D. Top-k sampling

### 37. A governance team wants a structured record of a model's intended use, evaluation results, and risk rating. Which feature fits?

Domain: Guidelines for Responsible AI

- A. Amazon CloudWatch
- B. Amazon Bedrock Guardrails
- C. Amazon SageMaker Clarify
- D. Amazon SageMaker Model Cards

### 38. A screening team wants to measure the fraction of all true disease cases detected. Which metric fits?

Domain: Fundamentals of AI and ML

- A. Mean absolute error
- B. Recall
- C. Accuracy
- D. Precision

### 39. A search system represents sentences as vectors so that similar meanings are close. What representation is this?

Domain: Fundamentals of GenAI

- A. Embedding
- B. Hyperparameters
- C. Token
- D. Target labels

### 40. A very simple predictor performs poorly on both training and validation examples. Which issue is most likely?

Domain: Fundamentals of AI and ML

- A. Underfitting
- B. Data distribution drift
- C. Overfitting
- D. Data leakage

### 41. Long source files must be divided into retrievable passages before indexing. Which preparation step is this?

Domain: Applications of Foundation Models

- A. Document chunking
- B. Temperature
- C. Pretraining
- D. Fine-tuning

### 42. An image generator starts with noise and repeatedly denoises it into an image. Which model family fits?

Domain: Fundamentals of GenAI

- A. Regression
- B. Clustering
- C. Deterministic rule-based processing
- D. Diffusion model

### 43. Investigators want to know what fraction of fraud alerts are genuinely fraudulent. Which metric answers this?

Domain: Fundamentals of AI and ML

- A. Recall
- B. Mean absolute error
- C. Accuracy
- D. Precision

### 44. A team wants a managed Bedrock feature to connect approved documents to retrieval-based answers. Which feature fits?

Domain: Applications of Foundation Models

- A. Amazon Polly
- B. Amazon SageMaker Ground Truth
- C. Amazon Bedrock Knowledge Bases
- D. Amazon Q Developer

### 45. A governance team wants a history of supported resource configurations and checks against configured rules. Which AWS service fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. AWS Key Management Service (AWS KMS)
- B. AWS CloudTrail
- C. AWS Artifact
- D. AWS Config

### 46. A sampler keeps the smallest token set whose cumulative probability reaches 0.9. Which method is this?

Domain: Fundamentals of GenAI

- A. Context window
- B. Top-k sampling
- C. Maximum output tokens
- D. Top-p sampling

### 47. A deployed endpoint scores a newly received payment for fraud risk. Which activity is this?

Domain: Fundamentals of AI and ML

- A. Final test evaluation
- B. Inference
- C. Validation
- D. Training

### 48. Before launching a customer-service ML pilot, which TWO foundations should a team prioritize? (Select TWO.)

Domain: Fundamentals of AI and ML

- A. Business outcome metrics
- B. A larger model alone
- C. Deploy without evaluation
- D. More training epochs alone
- E. Clean and representative training data

### 49. A team needs a model primarily designed to generate and summarize natural language. Which category fits?

Domain: Fundamentals of GenAI

- A. Regression
- B. Deterministic rule-based processing
- C. Amazon Rekognition
- D. Large language model

### 50. A classifier performs almost perfectly on training data but poorly on untouched examples. What is the likely issue?

Domain: Fundamentals of AI and ML

- A. Underfitting
- B. Data leakage
- C. Overfitting
- D. Data distribution drift

### 51. An AI recommendation could materially affect a person's access to a service. Which control supports appropriate oversight?

Domain: Guidelines for Responsible AI

- A. More training epochs alone
- B. Human review and escalation
- C. Treat a safety filter as a complete guarantee
- D. Stop monitoring after launch

### 52. A team needs a managed search service with vector capabilities to store document embeddings and retrieve nearby vectors. Which listed option fits?

Domain: Applications of Foundation Models

- A. Amazon Polly
- B. Amazon Transcribe
- C. AWS Key Management Service (AWS KMS)
- D. Amazon OpenSearch Service with vector capabilities

### 53. A team uses fixed instructions with placeholders for customer text and retrieved evidence. Which artifact is this?

Domain: Applications of Foundation Models

- A. Pretraining
- B. Model quantization
- C. Reusable prompt template
- D. Embedding

### 54. A model has similar overall accuracy to its predecessor but performs much worse for one relevant demographic group. Which principle needs assessment?

Domain: Guidelines for Responsible AI

- A. Inference latency
- B. Token and request cost measurement
- C. Fairness assessment
- D. Explainability

### 55. A team has stable high demand and wants to evaluate reserved model capacity for a supported Bedrock model. Which option should it assess?

Domain: Fundamentals of GenAI

- A. Prompt engineering
- B. On-demand inference
- C. Retrieval-Augmented Generation (RAG)
- D. Provisioned Throughput

### 56. A prompt includes three sample reviews and correct sentiment labels before a new review. Which approach is this?

Domain: Applications of Foundation Models

- A. Zero-shot prompting
- B. Few-shot prompting
- C. Pretraining
- D. Fine-tuning

### 57. A RAG system returns passages unrelated to the question. Which evaluation dimension should be inspected first?

Domain: Applications of Foundation Models

- A. Retrieval relevance evaluation
- B. Maximum output tokens
- C. Inference latency
- D. Groundedness evaluation

### 58. A team must control which workloads can invoke a model and read a specific dataset. Which AWS service provides permission controls?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Amazon Macie
- B. AWS Identity and Access Management (IAM)
- C. AWS Key Management Service (AWS KMS)
- D. AWS CloudTrail

### 59. A model must interpret an uploaded photo alongside a written question. Which capability is needed?

Domain: Fundamentals of GenAI

- A. Large language model
- B. Multimodal model
- C. Regression
- D. Deterministic rule-based processing

### 60. A reviewer needs to understand which input factors most influenced a model decision. Which capability fits?

Domain: Guidelines for Responsible AI

- A. Inference latency
- B. Privacy protection
- C. Transparency
- D. Explainability

### 61. A retriever returns 30 candidate passages, then another relevance step selects the best five. Which step is this?

Domain: Applications of Foundation Models

- A. Document chunking
- B. Temperature
- C. Reranking
- D. Fine-tuning

### 62. A team prepares to fine-tune a model. Which TWO data practices support a trustworthy assessment? (Select TWO.)

Domain: Applications of Foundation Models

- A. A larger model alone
- B. Deploy without evaluation
- C. Curate high-quality task examples
- D. Keep evaluation data separate from adaptation data
- E. Always fill the entire context window

### 63. An assistant must retrieve a policy, check an external system, and initiate an approved workflow. Which Bedrock capability fits orchestration?

Domain: Applications of Foundation Models

- A. Amazon SageMaker Ground Truth
- B. Amazon Bedrock Agents
- C. Amazon Textract
- D. Amazon Bedrock Knowledge Bases

### 64. An auditor needs records of supported AWS API calls affecting an AI environment. Which service fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. AWS Artifact
- B. AWS CloudTrail
- C. Amazon Macie
- D. Amazon CloudWatch

### 65. An engineer runs optimization over labeled examples to update neural network weights. Which lifecycle stage is this?

Domain: Fundamentals of AI and ML

- A. Final test evaluation
- B. Inference
- C. Training
- D. Validation

### 66. A retailer wants to discover shopper segments from purchase behavior without labeled segments. Which approach fits?

Domain: Fundamentals of AI and ML

- A. Unsupervised learning
- B. Deterministic rule-based processing
- C. Supervised learning
- D. Reinforcement learning

### 67. A team improves an assistant by rewriting its instructions without training. Which technique is this?

Domain: Fundamentals of GenAI

- A. Fine-tuning
- B. Pretraining
- C. Prompt engineering
- D. Model distillation

### 68. A team must prevent unnecessary exposure of customer personal details in model inputs and outputs. Which principle fits?

Domain: Guidelines for Responsible AI

- A. Inference latency
- B. Privacy protection
- C. Generative modeling
- D. Explainability

### 69. A model pretrained on broad data is reused for summarization, question answering, and adaptation. What is it?

Domain: Fundamentals of GenAI

- A. Foundation model
- B. Deterministic rule-based processing
- C. Clustering
- D. Regression

### 70. An attacker adds mislabeled examples to a training dataset to create harmful learned behavior. Which threat is this?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Data poisoning
- B. Prompt injection
- C. Hallucination
- D. Data distribution drift

### 71. A diagram places AI as the broadest field, ML inside AI, and multi-layer neural network methods inside ML. What label belongs on the innermost group?

Domain: Fundamentals of AI and ML

- A. Clustering
- B. Deterministic rule-based processing
- C. Regression
- D. Deep learning

### 72. A team reduces model weight precision to lower memory requirements. Which optimization is this?

Domain: Applications of Foundation Models

- A. Retrieval-Augmented Generation (RAG)
- B. Model distillation
- C. Model quantization
- D. Prompt engineering

### 73. A RAG assistant answers from a changing policy repository. Which TWO practices improve traceability and freshness? (Select TWO.)

Domain: Applications of Foundation Models

- A. More training epochs alone
- B. Deploy without evaluation
- C. Refresh the retrieval index when sources change
- D. A larger model alone
- E. Require source citations and inspect support

### 74. A model bills for input and output units that can be word fragments. What are these units called?

Domain: Fundamentals of GenAI

- A. Target labels
- B. Model parameters
- C. Token
- D. Embedding

### 75. An agent platform wants a standardized protocol for connecting compatible AI applications to external tools and data. Which concept fits?

Domain: Fundamentals of GenAI

- A. Model Context Protocol (MCP)
- B. Model quantization
- C. Fine-tuning
- D. Temperature

### 76. A model application only needs read access to one approved bucket. Which access principle should its policy follow?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Least-privilege access
- B. Deploy without evaluation
- C. Make all internal documents publicly accessible
- D. Grant broad administrator access to every caller

### 77. A bank must mark a transaction as suspicious or normal. What type of prediction is this?

Domain: Fundamentals of AI and ML

- A. Clustering
- B. Classification
- C. Regression
- D. Generative modeling

### 78. Users should be told that a service uses AI and what its limitations are. Which principle fits?

Domain: Guidelines for Responsible AI

- A. Robustness
- B. Transparency
- C. Explainability
- D. Privacy protection

### 79. A chatbot must answer from frequently updated internal manuals without retraining model weights. Which architecture fits?

Domain: Applications of Foundation Models

- A. Fine-tuning
- B. Retrieval-Augmented Generation (RAG)
- C. Model distillation
- D. Pretraining

### 80. A developer wants AI help explaining code and suggesting improvements in a development workflow. Which service fits?

Domain: Fundamentals of GenAI

- A. Amazon Q Developer
- B. Amazon Textract
- C. Amazon Transcribe
- D. Amazon Q Business

### 81. A real estate model predicts a house sale price. Which ML task fits?

Domain: Fundamentals of AI and ML

- A. Clustering
- B. Generative modeling
- C. Classification
- D. Regression

### 82. A company appoints an owner for AI incidents and defines escalation responsibilities. Which principle is this?

Domain: Guidelines for Responsible AI

- A. Inference latency
- B. Accountability
- C. Embedding
- D. Precision

### 83. A smaller student model is trained using outputs from a larger teacher. What technique is this?

Domain: Fundamentals of GenAI

- A. Prompt engineering
- B. Model quantization
- C. Model distillation
- D. Retrieval-Augmented Generation (RAG)

### 84. A prompt says classify this review as positive or negative and supplies no examples. Which prompting style is this?

Domain: Applications of Foundation Models

- A. Zero-shot prompting
- B. Fine-tuning
- C. Pretraining
- D. Few-shot prompting

### 85. A translation team needs a common n-gram precision-oriented comparison with reference translations. Which metric fits?

Domain: Applications of Foundation Models

- A. BLEU
- B. Recall
- C. ROUGE
- D. Mean absolute error

### 86. A company updates a pretrained model's weights using approved domain examples. Which approach is this?

Domain: Fundamentals of GenAI

- A. Prompt engineering
- B. Retrieval-Augmented Generation (RAG)
- C. Fine-tuning
- D. Inference

### 87. A company needs managed cryptographic keys for encryption in supported data services. Which AWS service fits?

Domain: Security, Compliance, and Governance for AI Solutions

- A. AWS Key Management Service (AWS KMS)
- B. AWS CloudTrail
- C. Amazon CloudWatch
- D. AWS Artifact

### 88. A GenAI assistant is too costly and slow. Which TWO changes are sensible candidates to evaluate while preserving quality? (Select TWO.)

Domain: Applications of Foundation Models

- A. Evaluate a smaller adequate model
- B. Deploy without evaluation
- C. Remove irrelevant prompt content
- D. Always fill the entire context window
- E. More training epochs alone

### 89. A Bedrock application needs configured filters for inappropriate content and sensitive information. Which capability fits?

Domain: Guidelines for Responsible AI

- A. Amazon Bedrock Guardrails
- B. Amazon S3
- C. Amazon SageMaker Model Cards
- D. Amazon SageMaker Ground Truth

### 90. A lender has applications labeled repaid or defaulted. Which learning approach fits prediction of future defaults?

Domain: Fundamentals of AI and ML

- A. Reinforcement learning
- B. Deterministic rule-based processing
- C. Supervised learning
- D. Unsupervised learning

### 91. A writer wants more varied outputs from a sampling-based model. Which inference setting is most directly relevant?

Domain: Fundamentals of GenAI

- A. Maximum output tokens
- B. Context window
- C. Target labels
- D. Temperature

### 92. A chatbot invents a nonexistent product policy and states it confidently. What failure is this?

Domain: Fundamentals of GenAI

- A. Data leakage
- B. Underfitting
- C. Hallucination
- D. Data distribution drift

### 93. An otherwise accurate assistant takes too long to answer users. Which operational metric directly captures this issue?

Domain: Applications of Foundation Models

- A. Inference latency
- B. Precision
- C. Recall
- D. Accuracy

### 94. A vision team needs human workers to label bounding boxes for training images. Which service supports this workflow?

Domain: Fundamentals of AI and ML

- A. Amazon Bedrock
- B. Amazon S3
- C. Amazon SageMaker Ground Truth
- D. Amazon Polly

### 95. A finance team needs key-value fields and tables from scanned invoices. Which AWS service best fits?

Domain: Fundamentals of AI and ML

- A. Amazon Transcribe
- B. Amazon Rekognition
- C. Amazon Textract
- D. Amazon Comprehend

### 96. A vendor first trains a model on a vast general corpus before task adaptation. Which stage is this?

Domain: Fundamentals of GenAI

- A. Retrieval-Augmented Generation (RAG)
- B. Inference
- C. Prompt engineering
- D. Pretraining

### 97. A model underperforms for an underrepresented user group. Which TWO actions are appropriate? (Select TWO.)

Domain: Guidelines for Responsible AI

- A. A larger model alone
- B. Deploy without evaluation
- C. Improve representative coverage in data
- D. Evaluate performance across relevant subgroups
- E. Use only aggregate accuracy

### 98. A retrieved page tells an assistant to ignore its instructions and reveal confidential information. Which threat is this?

Domain: Security, Compliance, and Governance for AI Solutions

- A. Overfitting
- B. Prompt injection
- C. Data distribution drift
- D. Data poisoning

### 99. An assistant answers questions about frequently changing company policies. Which TWO actions reduce unsupported factual answers? (Select TWO.)

Domain: Fundamentals of GenAI

- A. More training epochs alone
- B. Temperature
- C. Retrieve current approved sources
- D. A larger model alone
- E. Verify factual claims against trusted sources

### 100. A brand assistant must be evaluated for subtle tone and practical usefulness. Which evaluation approach is most direct?

Domain: Applications of Foundation Models

- A. Inference latency
- B. BLEU
- C. Human evaluation
- D. ROUGE

---

## Answer key and explanations

### Question 1 — D

Answer: Data leakage. Using future outcomes or overlapping evaluation records gives an unrealistically favorable estimate. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.
- **B:** Incorrect for this question. Overfitting: Fits training-specific noise and patterns, producing weak generalization.
- **C:** Incorrect for this question. Underfitting: Fails to capture important patterns, often performing poorly on both training and unseen data.
- **D:** Correct. Data leakage: Allows information unavailable at prediction time to influence training or evaluation.

### Question 2 — B

Answer: Evaluate environmental efficiency alongside task quality. Environmental efficiency should be considered with quality and safety, rather than using a bigger model or more computation by default. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **B:** Correct. Evaluate environmental efficiency alongside task quality: Considers resource use and whether a smaller adequate model can meet the need without unnecessary computation.
- **C:** Incorrect for this question. Always fill the entire context window: Consumes tokens and can introduce irrelevant information; more context is not inherently better.
- **D:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.

### Question 3 — A

Answer: Maximum output tokens. An output-length cap can constrain response size and cost but may truncate a response. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Correct. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **B:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **C:** Incorrect for this question. Top-p sampling: Restricts sampling to a set of tokens whose cumulative probability reaches a chosen threshold.
- **D:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.

### Question 4 — A

Answer: Amazon SageMaker Clarify. Bias detection and prediction explanations are SageMaker Clarify capabilities; documentation or API logs alone do not perform this analysis. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html Further reading: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html

- **A:** Correct. Amazon SageMaker Clarify: Provides capabilities for detecting potential bias and explaining model predictions in supported ML workflows.
- **B:** Incorrect for this question. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.
- **C:** Incorrect for this question. Amazon Textract: Extracts text, form fields, and tables from document images.
- **D:** Incorrect for this question. Amazon SageMaker Model Cards: Documents model purpose, evaluation results, intended uses, and risk considerations for governance.

### Question 5 — B

Answer: Representative held-out evaluation prompts. Independent realistic prompts expose generalization failures that adaptation examples or capacity alone cannot establish. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Always fill the entire context window: Consumes tokens and can introduce irrelevant information; more context is not inherently better.
- **B:** Correct. Representative held-out evaluation prompts: Provide an independent test of quality across realistic users and tasks without reusing adaptation examples.
- **C:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **D:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.

### Question 6 — A

Answer: Top-k sampling. Top-k is a fixed candidate-count restriction, not a cumulative probability threshold. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Correct. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.
- **B:** Incorrect for this question. Top-p sampling: Restricts sampling to a set of tokens whose cumulative probability reaches a chosen threshold.
- **C:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **D:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.

### Question 7 — C

Answer: Amazon CloudWatch. Metrics, operational logs, and alarms fit CloudWatch; API audit trails have a separate role. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

- **A:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **B:** Incorrect for this question. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.
- **C:** Correct. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.
- **D:** Incorrect for this question. AWS Artifact: Provides on-demand access to AWS compliance reports and agreements.

### Question 8 — A

Answer: Check content rights and licensing. Generative AI does not erase rights and licensing obligations; permitted uses must be reviewed. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Correct. Check content rights and licensing: Verifies permitted use of training data and generated material instead of assuming AI removes intellectual property obligations.
- **B:** Incorrect for this question. Token: Is a model-dependent unit of text or other input representation used in processing and billing.
- **C:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **D:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.

### Question 9 — B

Answer: Context window. The total information considered per request is bounded; a larger context does not inherently eliminate errors. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.
- **B:** Correct. Context window: Limits the amount of input and generated content a model can consider within a request, according to model-specific rules.
- **C:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **D:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.

### Question 10 — D

Answer: Shared responsibility model. AWS secures the underlying infrastructure, while customers retain duties such as data governance and application permissions, depending on the service. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://aws.amazon.com/compliance/shared-responsibility-model/

- **A:** Incorrect for this question. Grant broad administrator access to every caller: Violates least privilege and increases the impact of mistakes or compromise.
- **B:** Incorrect for this question. Make all internal documents publicly accessible: Removes confidentiality protections and is not a safe solution to retrieval or access problems.
- **C:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **D:** Correct. Shared responsibility model: Divides security responsibilities between AWS and the customer, depending on the services used.

### Question 11 — D

Answer: Groundedness evaluation. Groundedness asks whether the response is supported by context, not just whether retrieval returned relevant passages. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Token and request cost measurement: Tracks input/output usage and actual prices to compare the economics of candidate models.
- **B:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **C:** Incorrect for this question. Retrieval relevance evaluation: Checks whether retrieved passages contain information useful for answering the query.
- **D:** Correct. Groundedness evaluation: Checks whether generated claims are supported by the supplied source context.

### Question 12 — A

Answer: Vector similarity search. Semantic retrieval compares embeddings; exact lexical matching is not required for paraphrases. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Vector similarity search: Retrieves nearby embedding vectors to find semantically related content.
- **B:** Incorrect for this question. Classification: Predicts a discrete category, such as fraud or legitimate.
- **C:** Incorrect for this question. Exact keyword search: Matches lexical terms and can be useful when exact identifiers or wording matter.
- **D:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.

### Question 13 — B, E

Answer: Adversarial testing and red teaming; Document intended uses and known limitations. Challenging tests and documented scope support risk management; a safety filter alone cannot establish safe deployment. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Treat a safety filter as a complete guarantee: Overstates control effectiveness; filters can miss harmful content and need layered safeguards.
- **B:** Correct. Adversarial testing and red teaming: Probes likely misuse and failure modes with challenging inputs before and after release.
- **C:** Incorrect for this question. Stop monitoring after launch: Misses changes in risks and performance; responsible AI requires ongoing oversight.
- **D:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **E:** Correct. Document intended uses and known limitations: Creates reviewable records of scope, performance, assumptions, and risk controls.

### Question 14 — C

Answer: Batch inference. The workload has no interactive response requirement and can process a collection asynchronously. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Real-time inference: Serves individual prediction requests with interactive response requirements.
- **B:** Incorrect for this question. Training: Adjusts model parameters using training examples and an optimization objective.
- **C:** Correct. Batch inference: Processes a collection of inputs asynchronously when immediate individual responses are unnecessary.
- **D:** Incorrect for this question. Validation: Uses a held-out development dataset to select models or hyperparameters.

### Question 15 — D

Answer: Generative modeling. Producing novel content is generative; choosing a label or predicting a numeric quantity is not the same task. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Classification: Predicts a discrete category, such as fraud or legitimate.
- **B:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **C:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **D:** Correct. Generative modeling: Creates new content based on patterns learned from training data.

### Question 16 — A

Answer: Fine-tuning. Persistent learned output behavior can be adapted through fine-tuning when suitable data, support, and evaluation justify it. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **B:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **C:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **D:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.

### Question 17 — C

Answer: Role-based prompting. A requested role is a prompt instruction, not proof of expertise or a change to the model weights. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **B:** Incorrect for this question. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.
- **C:** Correct. Role-based prompting: Sets a perspective or function, such as a concise technical editor, in the instructions.
- **D:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.

### Question 18 — B

Answer: Amazon Q Business. Enterprise question answering over connected organizational information fits Amazon Q Business. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html Further reading: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html

- **A:** Incorrect for this question. Amazon SageMaker Ground Truth: Supports workflows for labeling training data with human workers and automation.
- **B:** Correct. Amazon Q Business: Is a generative AI assistant for enterprise information with supported data connectors and access-aware retrieval.
- **C:** Incorrect for this question. Amazon Q Developer: Provides generative AI assistance for software development and AWS-related technical tasks.
- **D:** Incorrect for this question. Amazon Polly: Converts text into synthesized speech.

### Question 19 — C

Answer: Reinforcement learning. Sequential actions with feedback rewards indicate reinforcement learning, rather than fixed labeled examples. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **B:** Incorrect for this question. Unsupervised learning: Discovers structure in data without supplied target labels.
- **C:** Correct. Reinforcement learning: Learns actions through interaction and reward signals.
- **D:** Incorrect for this question. Supervised learning: Learns a mapping from input examples to known target labels.

### Question 20 — D

Answer: AWS PrivateLink. Private service connectivity controls network paths; encryption and monitoring address separate concerns. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html

- **A:** Incorrect for this question. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.
- **B:** Incorrect for this question. Encryption in transit using TLS: Protects data while it travels over a network; it is distinct from encrypting stored data.
- **C:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **D:** Correct. AWS PrivateLink: Provides private connectivity to supported services through VPC endpoints without requiring public internet routing for that service traffic.

### Question 21 — B

Answer: Mean absolute error. Absolute numeric prediction errors are meaningful for a continuous target; classification metrics are not the direct fit. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Recall: Measures the fraction of actual positives that the model identifies.
- **B:** Correct. Mean absolute error: Measures average absolute numeric prediction error in the target variable units.
- **C:** Incorrect for this question. Precision: Measures the fraction of predicted positives that are actually positive.
- **D:** Incorrect for this question. Accuracy: Measures the fraction of all predictions that are correct; imbalance can make it misleading.

### Question 22 — B

Answer: Amazon Macie. Sensitive-data discovery in S3 is Macie; encryption alone does not identify the sensitive fields. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html

- **A:** Incorrect for this question. AWS Artifact: Provides on-demand access to AWS compliance reports and agreements.
- **B:** Correct. Amazon Macie: Discovers and reports sensitive data such as personal information in Amazon S3 using managed analysis.
- **C:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **D:** Incorrect for this question. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.

### Question 23 — B, C

Answer: Task-specific quality evaluation; Token and request cost measurement. Model selection should jointly measure task quality and workload economics, not assume bigger is always better. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **B:** Correct. Token and request cost measurement: Tracks input/output usage and actual prices to compare the economics of candidate models.
- **C:** Correct. Task-specific quality evaluation: Tests representative prompts against defined acceptance criteria rather than assuming all models perform equally.
- **D:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **E:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.

### Question 24 — D

Answer: Amazon Comprehend. The requested task analyzes the meaning or entities of existing text, not language conversion or audio recognition. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html Further reading: https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html

- **A:** Incorrect for this question. Amazon Translate: Translates text between supported languages.
- **B:** Incorrect for this question. Amazon Transcribe: Converts speech audio into text.
- **C:** Incorrect for this question. Amazon Rekognition: Analyzes images and video for objects, scenes, and other supported visual features.
- **D:** Correct. Amazon Comprehend: Uses natural language processing for tasks such as entity extraction and sentiment analysis.

### Question 25 — A

Answer: Versioned prompt management. Tracking prompt versions enables controlled comparisons and rollback after a regression. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Versioned prompt management: Tracks prompt revisions so changes can be evaluated, reproduced, and rolled back.
- **B:** Incorrect for this question. Model quantization: Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.
- **C:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.
- **D:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.

### Question 26 — C

Answer: Explicit output schema and validation. A requested format should be validated; prompting alone does not ensure every generated object is valid. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.
- **B:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **C:** Correct. Explicit output schema and validation: Requests a structured format and checks generated output against that format before downstream use.
- **D:** Incorrect for this question. Context window: Limits the amount of input and generated content a model can consider within a request, according to model-specific rules.

### Question 27 — C

Answer: ROUGE. ROUGE is commonly used for summary overlap, but complementary factual and human evaluation is still needed. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. BLEU: Measures n-gram overlap with reference text and is commonly associated with machine translation evaluation.
- **B:** Incorrect for this question. Precision: Measures the fraction of predicted positives that are actually positive.
- **C:** Correct. ROUGE: Measures text overlap, commonly recall-oriented, between generated and reference summaries; it does not prove factual accuracy.
- **D:** Incorrect for this question. Mean absolute error: Measures average absolute numeric prediction error in the target variable units.

### Question 28 — A, D

Answer: Enforce authorization before retrieval and actions; Treat retrieved content as untrusted data. Trusted authorization and treating retrieved instructions as untrusted reduce exposure; prompts alone are not security boundaries. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Correct. Enforce authorization before retrieval and actions: Uses trusted application and identity controls to ensure users access only permitted records and operations.
- **B:** Incorrect for this question. Grant broad administrator access to every caller: Violates least privilege and increases the impact of mistakes or compromise.
- **C:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **D:** Correct. Treat retrieved content as untrusted data: Separates source material from trusted instructions and avoids granting documents authority over tools or security policies.
- **E:** Incorrect for this question. Make all internal documents publicly accessible: Removes confidentiality protections and is not a safe solution to retrieval or access problems.

### Question 29 — D

Answer: Amazon Transcribe. The input is speech audio and the required output is text. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html Further reading: https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html

- **A:** Incorrect for this question. Amazon Translate: Translates text between supported languages.
- **B:** Incorrect for this question. Amazon Textract: Extracts text, form fields, and tables from document images.
- **C:** Incorrect for this question. Amazon Polly: Converts text into synthesized speech.
- **D:** Correct. Amazon Transcribe: Converts speech audio into text.

### Question 30 — D

Answer: Task decomposition. Explicit smaller subtasks improve control; this does not require exposing private internal reasoning. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.
- **B:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **C:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **D:** Correct. Task decomposition: Breaks a complex request into smaller explicit subtasks to improve control and reviewability.

### Question 31 — B

Answer: On-demand inference. Variable, exploratory traffic can use consumption-based access without a reserved throughput commitment. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **B:** Correct. On-demand inference: Supports usage-based access without reserving dedicated model throughput in advance.
- **C:** Incorrect for this question. Provisioned Throughput: Reserves model capacity for supported models under the applicable pricing and commitment terms.
- **D:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.

### Question 32 — D

Answer: Metadata filtering. Retrieval attributes can constrain results to the requested subset; sampling controls do not enforce source categories. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.
- **B:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **C:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **D:** Correct. Metadata filtering: Restricts retrieval candidates using attributes such as department, date, or document type.

### Question 33 — B

Answer: Tool or action invocation. External actions require a controlled integration; generating a statement that an action happened is not performing it. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.
- **B:** Correct. Tool or action invocation: Calls an external function or API to perform an operation or obtain information unavailable in model weights.
- **C:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **D:** Incorrect for this question. Generative modeling: Creates new content based on patterns learned from training data.

### Question 34 — B

Answer: Robustness. The focus is dependable behavior under variation and challenging inputs, rather than a single average accuracy number. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Correct. Robustness: Concerns maintaining acceptable behavior under expected variations, disturbances, or challenging inputs.
- **C:** Incorrect for this question. Accuracy: Measures the fraction of all predictions that are correct; imbalance can make it misleading.
- **D:** Incorrect for this question. Token and request cost measurement: Tracks input/output usage and actual prices to compare the economics of candidate models.

### Question 35 — A, E

Answer: Data minimization; Defined retention and deletion policies. Limit data to its approved purpose and set explicit lifecycle rules; collecting everything indefinitely increases exposure. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Correct. Defined retention and deletion policies: Specify how long prompts, logs, datasets, and outputs may be kept and when they must be removed.
- **B:** Incorrect for this question. Grant broad administrator access to every caller: Violates least privilege and increases the impact of mistakes or compromise.
- **C:** Incorrect for this question. Make all internal documents publicly accessible: Removes confidentiality protections and is not a safe solution to retrieval or access problems.
- **D:** Incorrect for this question. Stop monitoring after launch: Misses changes in risks and performance; responsible AI requires ongoing oversight.
- **E:** Correct. Data minimization: Collects and retains only data necessary for the approved purpose.

### Question 36 — A

Answer: Data residency and processing-location review. Processing location and routing must be reviewed explicitly; sampling settings do not address geographic requirements. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Correct. Data residency and processing-location review: Checks where data is stored and processed, including applicable model and routing configurations.
- **B:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **C:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **D:** Incorrect for this question. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.

### Question 37 — D

Answer: Amazon SageMaker Model Cards. A structured record of model purpose, evaluation, and risk is a model card, not an enforcement filter. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html Further reading: https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html

- **A:** Incorrect for this question. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.
- **B:** Incorrect for this question. Amazon Bedrock Guardrails: Applies configured controls such as content filters and sensitive-information handling to supported generative AI interactions.
- **C:** Incorrect for this question. Amazon SageMaker Clarify: Provides capabilities for detecting potential bias and explaining model predictions in supported ML workflows.
- **D:** Correct. Amazon SageMaker Model Cards: Documents model purpose, evaluation results, intended uses, and risk considerations for governance.

### Question 38 — B

Answer: Recall. Recall measures coverage of actual positives and is useful when missing positives is costly. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Mean absolute error: Measures average absolute numeric prediction error in the target variable units.
- **B:** Correct. Recall: Measures the fraction of actual positives that the model identifies.
- **C:** Incorrect for this question. Accuracy: Measures the fraction of all predictions that are correct; imbalance can make it misleading.
- **D:** Incorrect for this question. Precision: Measures the fraction of predicted positives that are actually positive.

### Question 39 — A

Answer: Embedding. Semantic vector representations enable similarity comparison without exact keyword overlap. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Correct. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.
- **B:** Incorrect for this question. Hyperparameters: Are configuration choices such as learning rate, selected outside the parameter-learning process.
- **C:** Incorrect for this question. Token: Is a model-dependent unit of text or other input representation used in processing and billing.
- **D:** Incorrect for this question. Target labels: Are known outcomes provided to a supervised learning algorithm.

### Question 40 — A

Answer: Underfitting. Poor performance even on the training set can indicate insufficient model capacity or inadequate learning. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Correct. Underfitting: Fails to capture important patterns, often performing poorly on both training and unseen data.
- **B:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.
- **C:** Incorrect for this question. Overfitting: Fits training-specific noise and patterns, producing weak generalization.
- **D:** Incorrect for this question. Data leakage: Allows information unavailable at prediction time to influence training or evaluation.

### Question 41 — A

Answer: Document chunking. Splitting documents into coherent passages controls retrieval granularity and the amount of evidence supplied per match. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Document chunking: Splits source content into retrievable passages; size and boundaries affect retrieval quality and context use.
- **B:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **C:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **D:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.

### Question 42 — D

Answer: Diffusion model. Iterative denoising is a characteristic mechanism of diffusion-based generation. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **B:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **C:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **D:** Correct. Diffusion model: Learns to reverse a noise-adding process and is commonly used for image generation.

### Question 43 — D

Answer: Precision. When false positive alerts are costly, precision directly describes how trustworthy positive predictions are. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Recall: Measures the fraction of actual positives that the model identifies.
- **B:** Incorrect for this question. Mean absolute error: Measures average absolute numeric prediction error in the target variable units.
- **C:** Incorrect for this question. Accuracy: Measures the fraction of all predictions that are correct; imbalance can make it misleading.
- **D:** Correct. Precision: Measures the fraction of predicted positives that are actually positive.

### Question 44 — C

Answer: Amazon Bedrock Knowledge Bases. A managed Bedrock retrieval workflow fits Knowledge Bases; it is different from human labeling or development assistance. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html Further reading: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

- **A:** Incorrect for this question. Amazon Polly: Converts text into synthesized speech.
- **B:** Incorrect for this question. Amazon SageMaker Ground Truth: Supports workflows for labeling training data with human workers and automation.
- **C:** Correct. Amazon Bedrock Knowledge Bases: Manages supported retrieval and generation workflows over connected data sources for grounding model responses.
- **D:** Incorrect for this question. Amazon Q Developer: Provides generative AI assistance for software development and AWS-related technical tasks.

### Question 45 — D

Answer: AWS Config. AWS Config tracks supported resource configurations and evaluates configured rules; compliance reports and activity trails serve different purposes. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **B:** Incorrect for this question. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.
- **C:** Incorrect for this question. AWS Artifact: Provides on-demand access to AWS compliance reports and agreements.
- **D:** Correct. AWS Config: Records supported resource configurations and evaluates them against configured rules.

### Question 46 — D

Answer: Top-p sampling. Nucleus sampling uses cumulative probability mass; its candidate count can vary by step. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Context window: Limits the amount of input and generated content a model can consider within a request, according to model-specific rules.
- **B:** Incorrect for this question. Top-k sampling: Restricts sampling candidates to the k highest-probability tokens at each step.
- **C:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **D:** Correct. Top-p sampling: Restricts sampling to a set of tokens whose cumulative probability reaches a chosen threshold.

### Question 47 — B

Answer: Inference. Using a model to predict a new operational example is inference; weights need not be updated. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Final test evaluation: Estimates generalization using held-out data not used for training or model selection.
- **B:** Correct. Inference: Uses a trained model to produce outputs for new inputs.
- **C:** Incorrect for this question. Validation: Uses a held-out development dataset to select models or hyperparameters.
- **D:** Incorrect for this question. Training: Adjusts model parameters using training examples and an optimization objective.

### Question 48 — A, E

Answer: Clean and representative training data; Business outcome metrics. Data quality and measurable business value are prerequisites; extra capacity or training alone does not establish suitability. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Correct. Business outcome metrics: Measure operational value, such as handling time, revenue, or resolved customer issues.
- **B:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **C:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **D:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **E:** Correct. Clean and representative training data: Reduces avoidable data errors and improves coverage of the intended operating population.

### Question 49 — D

Answer: Large language model. Language modeling generates and transforms text; it is not a guarantee that the generated text is factual. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **B:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **C:** Incorrect for this question. Amazon Rekognition: Analyzes images and video for objects, scenes, and other supported visual features.
- **D:** Correct. Large language model: Models language token sequences and can perform tasks such as text generation and summarization.

### Question 50 — C

Answer: Overfitting. A large training-versus-held-out performance gap is characteristic of overfitting. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Underfitting: Fails to capture important patterns, often performing poorly on both training and unseen data.
- **B:** Incorrect for this question. Data leakage: Allows information unavailable at prediction time to influence training or evaluation.
- **C:** Correct. Overfitting: Fits training-specific noise and patterns, producing weak generalization.
- **D:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.

### Question 51 — B

Answer: Human review and escalation. Consequential or uncertain outputs need appropriate human oversight and escalation, not blind reliance on automation. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **B:** Correct. Human review and escalation: Routes uncertain or consequential cases to qualified people instead of allowing unchecked automation.
- **C:** Incorrect for this question. Treat a safety filter as a complete guarantee: Overstates control effectiveness; filters can miss harmful content and need layered safeguards.
- **D:** Incorrect for this question. Stop monitoring after launch: Misses changes in risks and performance; responsible AI requires ongoing oversight.

### Question 52 — D

Answer: Amazon OpenSearch Service with vector capabilities. A supported vector index stores and searches embeddings; speech services and encryption-key management do not provide semantic retrieval. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Amazon Polly: Converts text into synthesized speech.
- **B:** Incorrect for this question. Amazon Transcribe: Converts speech audio into text.
- **C:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **D:** Correct. Amazon OpenSearch Service with vector capabilities: Can index embeddings and perform supported vector similarity queries for semantic retrieval.

### Question 53 — C

Answer: Reusable prompt template. Templates keep instructions consistent while substituting user input and retrieved context. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **B:** Incorrect for this question. Model quantization: Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.
- **C:** Correct. Reusable prompt template: Defines a consistent instruction structure with placeholders for task-specific inputs.
- **D:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.

### Question 54 — C

Answer: Fairness assessment. The concern is unequal outcomes across relevant populations; overall quality alone does not reveal this. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Incorrect for this question. Token and request cost measurement: Tracks input/output usage and actual prices to compare the economics of candidate models.
- **C:** Correct. Fairness assessment: Examines whether system performance and outcomes create inappropriate disparities across relevant groups.
- **D:** Incorrect for this question. Explainability: Helps people understand which factors influenced a model output or decision.

### Question 55 — D

Answer: Provisioned Throughput. Reserved throughput may suit predictable sustained demand, but support, commitments, and economics must be checked. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.
- **B:** Incorrect for this question. On-demand inference: Supports usage-based access without reserving dedicated model throughput in advance.
- **C:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **D:** Correct. Provisioned Throughput: Reserves model capacity for supported models under the applicable pricing and commitment terms.

### Question 56 — B

Answer: Few-shot prompting. A small set of examples supplied in context demonstrates expected behavior without training weights. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Zero-shot prompting: Provides task instructions without worked task examples in the prompt.
- **B:** Correct. Few-shot prompting: Includes a small number of demonstrations of the desired input-output behavior in the prompt.
- **C:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **D:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.

### Question 57 — A

Answer: Retrieval relevance evaluation. Retrieval quality must be checked separately from generation; a generator cannot reliably answer from irrelevant evidence. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Retrieval relevance evaluation: Checks whether retrieved passages contain information useful for answering the query.
- **B:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **C:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **D:** Incorrect for this question. Groundedness evaluation: Checks whether generated claims are supported by the supplied source context.

### Question 58 — B

Answer: AWS Identity and Access Management (IAM). Permission policies and roles determine access to AWS actions and resources; encryption and logs do not grant appropriate permissions. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html

- **A:** Incorrect for this question. Amazon Macie: Discovers and reports sensitive data such as personal information in Amazon S3 using managed analysis.
- **B:** Correct. AWS Identity and Access Management (IAM): Controls which principals can perform which actions on AWS resources through policies and roles.
- **C:** Incorrect for this question. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **D:** Incorrect for this question. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.

### Question 59 — B

Answer: Multimodal model. The defining requirement is handling distinct input or output modalities, rather than text alone. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Large language model: Models language token sequences and can perform tasks such as text generation and summarization.
- **B:** Correct. Multimodal model: Processes or generates more than one modality, such as text and images.
- **C:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **D:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.

### Question 60 — D

Answer: Explainability. Understanding factors behind a specific model output is explainability; general disclosure alone is not enough. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Incorrect for this question. Privacy protection: Limits collection, exposure, and use of personal information according to applicable requirements.
- **C:** Incorrect for this question. Transparency: Communicates system purpose, limitations, data practices, and the role of AI to relevant stakeholders.
- **D:** Correct. Explainability: Helps people understand which factors influenced a model output or decision.

### Question 61 — C

Answer: Reranking. A second relevance scoring stage reorders retrieved candidates; it does not change the source model weights. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Document chunking: Splits source content into retrievable passages; size and boundaries affect retrieval quality and context use.
- **B:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **C:** Correct. Reranking: Reorders an initially retrieved candidate set by relevance before selecting context.
- **D:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.

### Question 62 — C, D

Answer: Curate high-quality task examples; Keep evaluation data separate from adaptation data. Consistent adaptation examples and independent evaluation data enable meaningful fine-tuning assessment. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **B:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **C:** Correct. Curate high-quality task examples: Provides consistent, representative examples for adaptation and reduces conflicting supervision.
- **D:** Correct. Keep evaluation data separate from adaptation data: Preserves an independent estimate of generalization and reduces evaluation leakage.
- **E:** Incorrect for this question. Always fill the entire context window: Consumes tokens and can introduce irrelevant information; more context is not inherently better.

### Question 63 — B

Answer: Amazon Bedrock Agents. Multi-step task completion involving actions calls for orchestration, not retrieval alone. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html Further reading: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html

- **A:** Incorrect for this question. Amazon SageMaker Ground Truth: Supports workflows for labeling training data with human workers and automation.
- **B:** Correct. Amazon Bedrock Agents: Orchestrates foundation-model reasoning with supported knowledge retrieval and actions to complete tasks.
- **C:** Incorrect for this question. Amazon Textract: Extracts text, form fields, and tables from document images.
- **D:** Incorrect for this question. Amazon Bedrock Knowledge Bases: Manages supported retrieval and generation workflows over connected data sources for grounding model responses.

### Question 64 — B

Answer: AWS CloudTrail. An audit of supported API activity uses CloudTrail; operational latency monitoring is a different purpose. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html

- **A:** Incorrect for this question. AWS Artifact: Provides on-demand access to AWS compliance reports and agreements.
- **B:** Correct. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.
- **C:** Incorrect for this question. Amazon Macie: Discovers and reports sensitive data such as personal information in Amazon S3 using managed analysis.
- **D:** Incorrect for this question. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.

### Question 65 — C

Answer: Training. Learning weights from examples is training; serving an already learned model is inference. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Final test evaluation: Estimates generalization using held-out data not used for training or model selection.
- **B:** Incorrect for this question. Inference: Uses a trained model to produce outputs for new inputs.
- **C:** Correct. Training: Adjusts model parameters using training examples and an optimization objective.
- **D:** Incorrect for this question. Validation: Uses a held-out development dataset to select models or hyperparameters.

### Question 66 — A

Answer: Unsupervised learning. No target labels are available; discovering inherent groups is an unsupervised task. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Correct. Unsupervised learning: Discovers structure in data without supplied target labels.
- **B:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **C:** Incorrect for this question. Supervised learning: Learns a mapping from input examples to known target labels.
- **D:** Incorrect for this question. Reinforcement learning: Learns actions through interaction and reward signals.

### Question 67 — C

Answer: Prompt engineering. Instructions and examples provided at request time change the input, not the learned weights. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **B:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **C:** Correct. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.
- **D:** Incorrect for this question. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.

### Question 68 — B

Answer: Privacy protection. Protecting personal information concerns privacy; useful model outputs do not justify unnecessary exposure. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Correct. Privacy protection: Limits collection, exposure, and use of personal information according to applicable requirements.
- **C:** Incorrect for this question. Generative modeling: Creates new content based on patterns learned from training data.
- **D:** Incorrect for this question. Explainability: Helps people understand which factors influenced a model output or decision.

### Question 69 — A

Answer: Foundation model. Broad pretraining and reuse across downstream tasks distinguish a foundation model from a narrow task-specific predictor. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Correct. Foundation model: Is pretrained on broad data and can be adapted to a range of downstream tasks.
- **B:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **C:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **D:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.

### Question 70 — A

Answer: Data poisoning. Manipulating training examples to alter learned behavior is data poisoning rather than an inference-time instruction attack. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Correct. Data poisoning: Contaminates training or adaptation data to influence the learned model behavior.
- **B:** Incorrect for this question. Prompt injection: Places malicious instructions in user input or retrieved content to redirect a model away from the application intent.
- **C:** Incorrect for this question. Hallucination: Is plausible-looking generated content that is factually incorrect or unsupported.
- **D:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.

### Question 71 — D

Answer: Deep learning. Layered neural networks characterize deep learning, which is contained within machine learning and the broader field of AI. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **B:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **C:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **D:** Correct. Deep learning: Is a subset of ML using neural networks with multiple layers to learn representations.

### Question 72 — C

Answer: Model quantization. Lower numeric precision changes model representation and resource needs; it must be checked for quality impacts. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **B:** Incorrect for this question. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.
- **C:** Correct. Model quantization: Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.
- **D:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.

### Question 73 — C, E

Answer: Require source citations and inspect support; Refresh the retrieval index when sources change. Traceable evidence and refreshed sources improve a document-grounded workflow; neither removes the need for checking answers. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **B:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **C:** Correct. Refresh the retrieval index when sources change: Keeps indexed evidence aligned with approved source content according to the required freshness schedule.
- **D:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **E:** Correct. Require source citations and inspect support: Improves traceability to retrieved evidence but still requires checking that the citations support the claims.

### Question 74 — C

Answer: Token. Tokenization units are model-dependent and are not always entire words. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Target labels: Are known outcomes provided to a supervised learning algorithm.
- **B:** Incorrect for this question. Model parameters: Are internal values learned during training, such as weights.
- **C:** Correct. Token: Is a model-dependent unit of text or other input representation used in processing and billing.
- **D:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.

### Question 75 — A

Answer: Model Context Protocol (MCP). MCP is an integration protocol for tools and data. Authentication and authorization remain separate requirements. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Correct. Model Context Protocol (MCP): Standardizes how AI applications connect to external tools and data sources; it does not itself grant authorization.
- **B:** Incorrect for this question. Model quantization: Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.
- **C:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **D:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.

### Question 76 — A

Answer: Least-privilege access. Limit privileges to necessary actions and resources; more permission increases potential blast radius. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

- **A:** Correct. Least-privilege access: Grants only the actions and resources necessary for a role or workload.
- **B:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **C:** Incorrect for this question. Make all internal documents publicly accessible: Removes confidentiality protections and is not a safe solution to retrieval or access problems.
- **D:** Incorrect for this question. Grant broad administrator access to every caller: Violates least privilege and increases the impact of mistakes or compromise.

### Question 77 — B

Answer: Classification. The required output is a discrete class rather than a continuous value or unlabeled group. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **B:** Correct. Classification: Predicts a discrete category, such as fraud or legitimate.
- **C:** Incorrect for this question. Regression: Predicts a continuous numeric quantity, such as a sale price.
- **D:** Incorrect for this question. Generative modeling: Creates new content based on patterns learned from training data.

### Question 78 — B

Answer: Transparency. Informing stakeholders about system use and limitations is transparency, distinct from attributing a particular prediction. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Robustness: Concerns maintaining acceptable behavior under expected variations, disturbances, or challenging inputs.
- **B:** Correct. Transparency: Communicates system purpose, limitations, data practices, and the role of AI to relevant stakeholders.
- **C:** Incorrect for this question. Explainability: Helps people understand which factors influenced a model output or decision.
- **D:** Incorrect for this question. Privacy protection: Limits collection, exposure, and use of personal information according to applicable requirements.

### Question 79 — B

Answer: Retrieval-Augmented Generation (RAG). Changing facts in external documents are best supplied through retrieval rather than embedded by repeatedly updating weights. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html Further reading: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

- **A:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **B:** Correct. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **C:** Incorrect for this question. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.
- **D:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.

### Question 80 — A

Answer: Amazon Q Developer. Developer-oriented coding and AWS technical assistance fits Amazon Q Developer. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html Further reading: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html

- **A:** Correct. Amazon Q Developer: Provides generative AI assistance for software development and AWS-related technical tasks.
- **B:** Incorrect for this question. Amazon Textract: Extracts text, form fields, and tables from document images.
- **C:** Incorrect for this question. Amazon Transcribe: Converts speech audio into text.
- **D:** Incorrect for this question. Amazon Q Business: Is a generative AI assistant for enterprise information with supported data connectors and access-aware retrieval.

### Question 81 — D

Answer: Regression. The target is a continuous numeric measurement; regression predicts its magnitude. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Clustering: Groups similar examples without requiring predefined category labels.
- **B:** Incorrect for this question. Generative modeling: Creates new content based on patterns learned from training data.
- **C:** Incorrect for this question. Classification: Predicts a discrete category, such as fraud or legitimate.
- **D:** Correct. Regression: Predicts a continuous numeric quantity, such as a sale price.

### Question 82 — B

Answer: Accountability. Named ownership and escalation paths create accountability; an AI system does not remove organizational responsibility. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Correct. Accountability: Assigns ownership, review responsibilities, and escalation paths for AI decisions and impacts.
- **C:** Incorrect for this question. Embedding: Is a numeric vector representation used to capture relationships such as semantic similarity.
- **D:** Incorrect for this question. Precision: Measures the fraction of predicted positives that are actually positive.

### Question 83 — C

Answer: Model distillation. A smaller model learning from a larger teacher is distillation, not merely lowering numerical precision. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.
- **B:** Incorrect for this question. Model quantization: Uses lower-precision numeric representations to reduce model memory and potentially improve inference efficiency.
- **C:** Correct. Model distillation: Trains a smaller student model to reproduce useful behavior of a larger teacher model.
- **D:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.

### Question 84 — A

Answer: Zero-shot prompting. Instructions without demonstrations are zero-shot prompting; no parameter updates are involved. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Zero-shot prompting: Provides task instructions without worked task examples in the prompt.
- **B:** Incorrect for this question. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **C:** Incorrect for this question. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.
- **D:** Incorrect for this question. Few-shot prompting: Includes a small number of demonstrations of the desired input-output behavior in the prompt.

### Question 85 — A

Answer: BLEU. BLEU is associated with reference-based translation overlap; it is not a complete semantic quality measure. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. BLEU: Measures n-gram overlap with reference text and is commonly associated with machine translation evaluation.
- **B:** Incorrect for this question. Recall: Measures the fraction of actual positives that the model identifies.
- **C:** Incorrect for this question. ROUGE: Measures text overlap, commonly recall-oriented, between generated and reference summaries; it does not prove factual accuracy.
- **D:** Incorrect for this question. Mean absolute error: Measures average absolute numeric prediction error in the target variable units.

### Question 86 — C

Answer: Fine-tuning. Changing an existing model's weights with task examples is fine-tuning, unlike prompt-only or retrieval-only adaptation. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.
- **B:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **C:** Correct. Fine-tuning: Updates an existing model using task-specific examples to adapt its behavior.
- **D:** Incorrect for this question. Inference: Uses a trained model to produce outputs for new inputs.

### Question 87 — A

Answer: AWS Key Management Service (AWS KMS). Cryptographic key management is separate from auditing, operational monitoring, and compliance reports. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html Further reading: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

- **A:** Correct. AWS Key Management Service (AWS KMS): Manages cryptographic keys and supports encryption controls for integrated services.
- **B:** Incorrect for this question. AWS CloudTrail: Records supported AWS account activity and API events for auditing and investigation.
- **C:** Incorrect for this question. Amazon CloudWatch: Collects operational metrics and logs and supports alarms and monitoring.
- **D:** Incorrect for this question. AWS Artifact: Provides on-demand access to AWS compliance reports and agreements.

### Question 88 — A, C

Answer: Remove irrelevant prompt content; Evaluate a smaller adequate model. Remove unnecessary tokens and test an adequate smaller model; verify quality rather than assuming savings imply suitability. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Evaluate a smaller adequate model: Can reduce cost and latency when measured quality still meets the use case requirements.
- **B:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **C:** Correct. Remove irrelevant prompt content: Can reduce input token use and improve focus while preserving necessary instructions and evidence.
- **D:** Incorrect for this question. Always fill the entire context window: Consumes tokens and can introduce irrelevant information; more context is not inherently better.
- **E:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.

### Question 89 — A

Answer: Amazon Bedrock Guardrails. Configured response controls can filter supported harmful content categories, but do not guarantee the elimination of all harm. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html Further reading: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html

- **A:** Correct. Amazon Bedrock Guardrails: Applies configured controls such as content filters and sensitive-information handling to supported generative AI interactions.
- **B:** Incorrect for this question. Amazon S3: Provides object storage for datasets, artifacts, and other objects.
- **C:** Incorrect for this question. Amazon SageMaker Model Cards: Documents model purpose, evaluation results, intended uses, and risk considerations for governance.
- **D:** Incorrect for this question. Amazon SageMaker Ground Truth: Supports workflows for labeling training data with human workers and automation.

### Question 90 — C

Answer: Supervised learning. Known historical outcomes make learning an input-to-target mapping possible. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html

- **A:** Incorrect for this question. Reinforcement learning: Learns actions through interaction and reward signals.
- **B:** Incorrect for this question. Deterministic rule-based processing: Executes explicit rules; it does not learn patterns from training examples.
- **C:** Correct. Supervised learning: Learns a mapping from input examples to known target labels.
- **D:** Incorrect for this question. Unsupervised learning: Discovers structure in data without supplied target labels.

### Question 91 — D

Answer: Temperature. Temperature changes sampling behavior; it neither expands the context window nor guarantees factual correctness. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Maximum output tokens: Caps generated response length, subject to model-specific limits.
- **B:** Incorrect for this question. Context window: Limits the amount of input and generated content a model can consider within a request, according to model-specific rules.
- **C:** Incorrect for this question. Target labels: Are known outcomes provided to a supervised learning algorithm.
- **D:** Correct. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.

### Question 92 — C

Answer: Hallucination. Fluent output can contain fabricated facts; confidence in wording is not evidence of factual grounding. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Data leakage: Allows information unavailable at prediction time to influence training or evaluation.
- **B:** Incorrect for this question. Underfitting: Fails to capture important patterns, often performing poorly on both training and unseen data.
- **C:** Correct. Hallucination: Is plausible-looking generated content that is factually incorrect or unsupported.
- **D:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.

### Question 93 — A

Answer: Inference latency. Interactive wait time is a latency concern; correctness metrics measure different dimensions. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Correct. Inference latency: Measures the time required to return a prediction or response.
- **B:** Incorrect for this question. Precision: Measures the fraction of predicted positives that are actually positive.
- **C:** Incorrect for this question. Recall: Measures the fraction of actual positives that the model identifies.
- **D:** Incorrect for this question. Accuracy: Measures the fraction of all predictions that are correct; imbalance can make it misleading.

### Question 94 — C

Answer: Amazon SageMaker Ground Truth. Human annotation of training examples is a data-labeling workflow. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html Further reading: https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html

- **A:** Incorrect for this question. Amazon Bedrock: Provides managed access to foundation models and features for building generative AI applications.
- **B:** Incorrect for this question. Amazon S3: Provides object storage for datasets, artifacts, and other objects.
- **C:** Correct. Amazon SageMaker Ground Truth: Supports workflows for labeling training data with human workers and automation.
- **D:** Incorrect for this question. Amazon Polly: Converts text into synthesized speech.

### Question 95 — C

Answer: Amazon Textract. Document structure, forms, and tables call for document extraction rather than speech or general image analysis. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html Further reading: https://docs.aws.amazon.com/textract/latest/dg/what-is.html

- **A:** Incorrect for this question. Amazon Transcribe: Converts speech audio into text.
- **B:** Incorrect for this question. Amazon Rekognition: Analyzes images and video for objects, scenes, and other supported visual features.
- **C:** Correct. Amazon Textract: Extracts text, form fields, and tables from document images.
- **D:** Incorrect for this question. Amazon Comprehend: Uses natural language processing for tasks such as entity extraction and sentiment analysis.

### Question 96 — D

Answer: Pretraining. Broad initial learning from a corpus is pretraining, not retrieving context or sending instructions during inference. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. Retrieval-Augmented Generation (RAG): Retrieves relevant external information and supplies it to a generator as context without inherently updating model weights.
- **B:** Incorrect for this question. Inference: Uses a trained model to produce outputs for new inputs.
- **C:** Incorrect for this question. Prompt engineering: Shapes instructions, context, and examples supplied at inference time without changing model weights.
- **D:** Correct. Pretraining: Learns broad patterns from a large corpus before adaptation to a narrower task.

### Question 97 — C, D

Answer: Evaluate performance across relevant subgroups; Improve representative coverage in data. Measure disparities and address missing coverage; improving data representation alone is not proof that fairness is achieved. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html

- **A:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **B:** Incorrect for this question. Deploy without evaluation: Omits evidence of quality and risk and is not an appropriate substitute for validating an AI system.
- **C:** Correct. Improve representative coverage in data: Addresses missing or underrepresented operating populations, while still requiring evaluation of actual outcomes.
- **D:** Correct. Evaluate performance across relevant subgroups: Can reveal disparities hidden by aggregate metrics; grouping choices should be appropriate and lawful.
- **E:** Incorrect for this question. Use only aggregate accuracy: Can conceal uneven performance across populations and does not establish fairness or safety.

### Question 98 — B

Answer: Prompt injection. Malicious instructions delivered during inference are prompt injection; contamination of a training dataset is a separate threat. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

- **A:** Incorrect for this question. Overfitting: Fits training-specific noise and patterns, producing weak generalization.
- **B:** Correct. Prompt injection: Places malicious instructions in user input or retrieved content to redirect a model away from the application intent.
- **C:** Incorrect for this question. Data distribution drift: Occurs when production input distributions change relative to the reference data.
- **D:** Incorrect for this question. Data poisoning: Contaminates training or adaptation data to influence the learned model behavior.

### Question 99 — C, E

Answer: Retrieve current approved sources; Verify factual claims against trusted sources. Current retrieved evidence and independent claim checking address stale or unsupported facts; neither guarantees perfect output. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html

- **A:** Incorrect for this question. More training epochs alone: Repeats passes over training data but does not inherently fix label errors, bias, or leakage.
- **B:** Incorrect for this question. Temperature: Controls sampling randomness; lower values generally make outputs more focused, but do not guarantee correctness.
- **C:** Correct. Retrieve current approved sources: Provides up-to-date evidence at inference time; model pretraining alone does not supply newly changed facts.
- **D:** Incorrect for this question. A larger model alone: Adds capacity but does not automatically improve data quality or suitability for a business problem.
- **E:** Correct. Verify factual claims against trusted sources: Checks generated claims instead of treating confident language as proof of accuracy.

### Question 100 — C

Answer: Human evaluation. Qualified reviewers can assess nuanced usefulness and tone that simple overlap metrics do not capture. Reference: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html

- **A:** Incorrect for this question. Inference latency: Measures the time required to return a prediction or response.
- **B:** Incorrect for this question. BLEU: Measures n-gram overlap with reference text and is commonly associated with machine translation evaluation.
- **C:** Correct. Human evaluation: Uses qualified reviewers to assess dimensions such as correctness, usefulness, tone, and safety.
- **D:** Incorrect for this question. ROUGE: Measures text overlap, commonly recall-oriented, between generated and reference summaries; it does not prove factual accuracy.
