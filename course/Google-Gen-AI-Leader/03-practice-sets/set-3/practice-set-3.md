# Google Cloud Generative AI Leader — Practice Set 3

Prompt Engineering, Grounding & Output Improvement

100 questions · Suggested practice duration: 160 minutes · Practice target: 80%

Topical learning test, not an exam-weighted mock. Related concepts recur across topics.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual or recalled Google exam items.

## Questions

### 1. A prompt says only 'make this better,' and the result varies widely in audience and tone. What is the best first improvement?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Specify audience, task, constraints, and output expectations
- C. Set an appropriate maximum output length
- D. Few-shot prompting

### 2. A team changes the wording and examples in its request without updating model parameters. What technique is it using?

Domain: Techniques to improve gen AI model output

- A. Pretraining
- B. Supervised fine-tuning
- C. Quantization
- D. Prompt engineering

### 3. An instruction asks the model to respond as a cautious financial educator. Which prompt technique is most directly illustrated?

Domain: Techniques to improve gen AI model output

- A. Few-shot prompting
- B. One-shot prompting
- C. Zero-shot prompting
- D. Role prompting

### 4. A model receives a task instruction with no example input–output pairs. What prompting setup is this?

Domain: Techniques to improve gen AI model output

- A. One-shot prompting
- B. Few-shot prompting
- C. Supervised fine-tuning
- D. Zero-shot prompting

### 5. A request contains exactly one worked input–output example before the new task. Which prompting setup is this?

Domain: Techniques to improve gen AI model output

- A. One-shot prompting
- B. Zero-shot prompting
- C. Few-shot prompting
- D. Supervised fine-tuning

### 6. A team includes several representative example transformations before asking for another transformation. What technique is this?

Domain: Techniques to improve gen AI model output

- A. Few-shot prompting
- B. Zero-shot prompting
- C. Pretraining
- D. One-shot prompting

### 7. A prompt mixes source text and task instructions so the model confuses which text to summarize. What design change is most directly helpful?

Domain: Techniques to improve gen AI model output

- A. Adjust temperature to control sampling variability
- B. Quantization
- C. Clearly separate instructions from untrusted source content
- D. Model weights

### 8. An answer is too technical for first-time users despite being factually reasonable. What should the prompt specify first?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Set an appropriate maximum output length
- C. Specify audience, task, constraints, and output expectations
- D. Few-shot prompting

### 9. A model follows the requested content but uses the wrong labeling convention. Which prompt change may clarify the desired pattern?

Domain: Techniques to improve gen AI model output

- A. Top-k sampling
- B. Few-shot prompting
- C. Quantization
- D. Adjust temperature to control sampling variability

### 10. Several teams edit a shared instruction, and nobody can identify which change caused a regression. What practice is missing?

Domain: Techniques to improve gen AI model output

- A. Version prompts and regression-test revisions
- B. Protected audit trails and traceability
- C. Independent representative evaluation
- D. Continuously evaluate, version, and monitor the solution

### 11. A workflow first extracts requirements, then passes checked requirements to a drafting step. Which prompting pattern is this?

Domain: Techniques to improve gen AI model output

- A. Prompt chaining
- B. Zero-shot prompting
- C. Quantization
- D. Role prompting

### 12. A final recommendation requires a validated calculation from an earlier step. How should those steps be scheduled?

Domain: Google Cloud’s gen AI offerings

- A. Parallelize independent work with a controlled join
- B. Order dependent workflow stages
- C. Adjust temperature to control sampling variability
- D. Top-k sampling

### 13. Three independent documents can be summarized separately before their results are combined. What execution approach may reduce completion time?

Domain: Google Cloud’s gen AI offerings

- A. Greedy next-token selection
- B. Order dependent workflow stages
- C. Parallelize independent work with a controlled join
- D. Set an appropriate maximum output length

### 14. A teaching exercise asks a model to organize an arithmetic solution into intermediate steps. Which broad prompt pattern does this resemble?

Domain: Techniques to improve gen AI model output

- A. One-shot prompting
- B. Zero-shot prompting
- C. Role prompting
- D. Chain-of-thought-style prompting

### 15. An assistant alternates between choosing a tool action, observing its result, and deciding what to do next. Which pattern does this resemble?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. One-shot prompting
- C. ReAct-style reasoning and action
- D. Prompt chaining

### 16. A later prompt relies on a tool response containing an impossible negative stock count. What should happen before proceeding?

Domain: Google Cloud’s gen AI offerings

- A. Validate tool results before downstream use
- B. Bound waits and use safe failure handling
- C. Supported structured output plus schema validation
- D. Authorize and validate tool calls before execution

### 17. An iterative agent revises an answer endlessly. What control addresses this failure most directly?

Domain: Google Cloud’s gen AI offerings

- A. Set an appropriate maximum output length
- B. Bound waits and use safe failure handling
- C. Governed response caching
- D. Enforce task, tool-call, and spending budgets

### 18. A revised prompt works on the two examples its author used while editing it. How should the team assess the revision?

Domain: Techniques to improve gen AI model output

- A. Collect reviewed user feedback and verified outcomes
- B. Version prompts and regression-test revisions
- C. Independent representative evaluation
- D. Continuously evaluate, version, and monitor the solution

### 19. A request must omit unsupported claims and present uncertainties explicitly. Where should these behavioral expectations be made clear?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Specify audience, task, constraints, and output expectations
- C. Few-shot prompting
- D. Model weights

### 20. A prompt tells an agent it is 'authorized for all refunds.' What should actually determine its refund permissions?

Domain: Google Cloud’s gen AI offerings

- A. One-shot prompting
- B. Role prompting
- C. Human approval before a consequential action
- D. Authorize and validate tool calls before execution

### 21. A creative brainstorming task needs control over sampling variability while keeping task instructions unchanged. Which setting is most direct?

Domain: Techniques to improve gen AI model output

- A. Set an appropriate maximum output length
- B. Adjust top-p nucleus sampling
- C. Adjust temperature to control sampling variability
- D. Context window

### 22. A developer wants nucleus sampling rather than a fixed candidate count. Which parameter family is relevant?

Domain: Techniques to improve gen AI model output

- A. Model weights
- B. Top-k sampling
- C. Adjust top-p nucleus sampling
- D. Training epoch

### 23. A decoder should consider only a fixed number of highest-ranked next-token candidates. Which supported setting fits?

Domain: Techniques to improve gen AI model output

- A. Context window
- B. Adjust top-p nucleus sampling
- C. Set an appropriate maximum output length
- D. Top-k sampling

### 24. Responses are repeatedly cut off at the configured generated-token ceiling. Which setting should be reviewed alongside total model limits?

Domain: Techniques to improve gen AI model output

- A. Training epoch
- B. Tokenizer vocabulary
- C. Set an appropriate maximum output length
- D. Training batch

### 25. A downstream system requires a nested object with mandatory fields and approved enum values. Which approach is most direct?

Domain: Techniques to improve gen AI model output

- A. Adjust temperature to control sampling variability
- B. Top-k sampling
- C. Configured stop sequence
- D. Supported structured output plus schema validation

### 26. Why can setting a closing brace as a stop delimiter break an otherwise reasonable nested-JSON response? Which mechanism causes the risk?

Domain: Techniques to improve gen AI model output

- A. Supported structured output plus schema validation
- B. Configured stop sequence
- C. Greedy next-token selection
- D. Quantization

### 27. A deterministic-looking response contains an unsupported claim. Which evaluation is relevant to improving evidence use?

Domain: Techniques to improve gen AI model output

- A. Evaluate answer groundedness
- B. Greedy next-token selection
- C. Adjust temperature to control sampling variability
- D. Top-k sampling

### 28. A record passes JSON validation but names a supplier not present in the source invoice. What additional control is needed?

Domain: Google Cloud’s gen AI offerings

- A. Document AI
- B. Extract, validate, and reconcile structured fields
- C. Adjust temperature to control sampling variability
- D. Supported structured output plus schema validation

### 29. A user needs a concise two-column comparison, but the response is a long narrative. What is the best first prompt change?

Domain: Techniques to improve gen AI model output

- A. Specify audience, task, constraints, and output expectations
- B. Set an appropriate maximum output length
- C. Role prompting
- D. Few-shot prompting

### 30. A team needs reproducible evidence about a decoding change across model updates. What should it maintain?

Domain: Techniques to improve gen AI model output

- A. Collect reviewed user feedback and verified outcomes
- B. Version prompts and regression-test revisions
- C. Continuously evaluate, version, and monitor the solution
- D. Independent representative evaluation

### 31. Which source type should ground answers about a company's unpublished internal travel policy?

Domain: Techniques to improve gen AI model output

- A. Model weights
- B. Ground with authorized first-party enterprise data
- C. Ground with relevant public world information
- D. Ground with a licensed or approved third-party source

### 32. A specialist assistant uses a licensed medical reference database approved for its task. What grounding category applies?

Domain: Techniques to improve gen AI model output

- A. Ground with a licensed or approved third-party source
- B. Ground with relevant public world information
- C. Ground with authorized first-party enterprise data
- D. Pretraining

### 33. An assistant needs current publicly available event information rather than confidential enterprise material. Which grounding category fits?

Domain: Techniques to improve gen AI model output

- A. Supervised fine-tuning
- B. Ground with relevant public world information
- C. Model weights
- D. Ground with authorized first-party enterprise data

### 34. A customer asks for their exact current account balance. Which evidence mechanism is more appropriate than a generic document similarity search?

Domain: Google Cloud’s gen AI offerings

- A. Model weights
- B. Use an authorized database lookup tool
- C. Pretraining knowledge cutoff
- D. Retrieval-augmented generation (RAG)

### 35. A knowledge assistant must cite approved manuals that change every week. Which pattern should be considered first?

Domain: Techniques to improve gen AI model output

- A. Quantization
- B. Retrieval-augmented generation (RAG)
- C. Pretraining
- D. Supervised fine-tuning

### 36. An external reference is technically accessible but prohibits the intended commercial reuse. What issue must be resolved?

Domain: Business strategies for a successful gen AI solution

- A. Ground with relevant public world information
- B. Identity and Access Management (IAM)
- C. Minimize and protect personal data for the approved purpose
- D. Review rights, licenses, and permitted content use

### 37. A retrieval system contains both public HR guidance and restricted disciplinary files. What must govern which passages enter a user's context?

Domain: Business strategies for a successful gen AI solution

- A. Identity and Access Management (IAM)
- B. Ground with authorized first-party enterprise data
- C. Greedy next-token selection
- D. Adjust temperature to control sampling variability

### 38. A generated answer contains a credible source title, but the cited passage does not support its conclusion. Which check exposes this?

Domain: Techniques to improve gen AI model output

- A. Set an appropriate maximum output length
- B. Verify claims against cited source passages
- C. Evaluate answer groundedness
- D. Supported structured output plus schema validation

### 39. An approved evidence set does not answer a high-impact eligibility question. Which response policy is most appropriate?

Domain: Techniques to improve gen AI model output

- A. Adjust temperature to control sampling variability
- B. Top-k sampling
- C. Abstain or escalate when evidence is insufficient
- D. Choose only the largest available model

### 40. A retrieved policy version was replaced yesterday. What knowledge-management step most directly addresses future retrieval?

Domain: Techniques to improve gen AI model output

- A. Refresh and govern the retrieval index
- B. Coherent document chunking
- C. Low-rank adaptation (LoRA)
- D. Pretraining

### 41. A 200-page manual is always retrieved as one unwieldy block. Which preprocessing decision should be reconsidered?

Domain: Techniques to improve gen AI model output

- A. Top-k sampling
- B. Quantization
- C. Tokenizer
- D. Coherent document chunking

### 42. Which representation commonly enables semantic retrieval of paraphrased questions and documents?

Domain: Fundamentals of gen AI

- A. Logits
- B. Tokenizer
- C. Embedding representation
- D. Model weights

### 43. Users search with both exact equipment codes and ordinary descriptive phrases. Which retrieval design is worth evaluating?

Domain: Techniques to improve gen AI model output

- A. Set an appropriate maximum output length
- B. Hybrid lexical and vector retrieval
- C. Adjust temperature to control sampling variability
- D. Embedding representation

### 44. The correct document is among twenty candidates but poorly ordered. Which step may improve the final relevance ranking?

Domain: Techniques to improve gen AI model output

- A. Refresh and govern the retrieval index
- B. Low-rank adaptation (LoRA)
- C. Quantization
- D. Rerank retrieved candidates

### 45. A benchmark asks what proportion of all known relevant passages the system successfully finds. Which metric is this?

Domain: Techniques to improve gen AI model output

- A. Evaluate answer groundedness
- B. Retrieval precision
- C. Time to first token
- D. Retrieval recall

### 46. Only two of ten returned passages are relevant under the evaluation labels. Which metric reflects this result most directly?

Domain: Techniques to improve gen AI model output

- A. Output token generation rate
- B. Time to first token
- C. Retrieval precision
- D. Retrieval recall

### 47. Relevant passages were retrieved, but the answer adds an unsupported exception. Which quality dimension failed?

Domain: Techniques to improve gen AI model output

- A. Time to first token
- B. Retrieval precision
- C. Evaluate answer groundedness
- D. Retrieval recall

### 48. Retrieval returns many mostly irrelevant chunks and exceeds the model's request budget. What design action is most appropriate?

Domain: Techniques to improve gen AI model output

- A. Set an appropriate maximum output length
- B. Validated history compaction
- C. Budget and select relevant context
- D. Coherent document chunking

### 49. A developer proposes reranking to recover a document absent from every candidate set. Which component's limitation should be recognized?

Domain: Techniques to improve gen AI model output

- A. Rerank retrieved candidates
- B. Supervised fine-tuning
- C. Quantization
- D. Refresh and govern the retrieval index

### 50. Deleted confidential documents continue to appear through stale search entries. What retrieval-governance action is needed?

Domain: Techniques to improve gen AI model output

- A. Rerank retrieved candidates
- B. Model weights
- C. Refresh and govern the retrieval index
- D. Coherent document chunking

### 51. A new retrieval prompt is judged only on cases its author used to write it. What should the evaluation add?

Domain: Techniques to improve gen AI model output

- A. Independent representative evaluation
- B. Collect reviewed user feedback and verified outcomes
- C. Version prompts and regression-test revisions
- D. Continuously evaluate, version, and monitor the solution

### 52. A model-based grader rewards polished prose despite incorrect citations. What should the team do?

Domain: Techniques to improve gen AI model output

- A. Calibrate automated judging with expert review
- B. Evaluate answer groundedness
- C. Version prompts and regression-test revisions
- D. Supported structured output plus schema validation

### 53. A generated clinical summary could affect treatment. Which improvement approach adds accountable expert judgment?

Domain: Techniques to improve gen AI model output

- A. Calibrate automated judging with expert review
- B. Set an appropriate maximum output length
- C. Supported structured output plus schema validation
- D. Human-in-the-loop review

### 54. Prompt and retrieval quality were acceptable at launch. What should continue as data and usage change?

Domain: Techniques to improve gen AI model output

- A. Pretraining
- B. Independent representative evaluation
- C. Protected audit trails and traceability
- D. Continuously evaluate, version, and monitor the solution

### 55. A team cannot reproduce yesterday's output because prompt content, model version, and retrieval settings were not recorded. What practice helps?

Domain: Techniques to improve gen AI model output

- A. Protected audit trails and traceability
- B. Independent representative evaluation
- C. Version prompts and regression-test revisions
- D. Continuously evaluate, version, and monitor the solution

### 56. A supported model consistently fails a stable response convention despite careful instructions, and reviewed examples are available. Which parameter-changing method may be evaluated?

Domain: Techniques to improve gen AI model output

- A. Supervised fine-tuning
- B. Budget and select relevant context
- C. Top-k sampling
- D. Retrieval-augmented generation (RAG)

### 57. A supported training method learns prompt embeddings while leaving base model weights fixed. Which technique is this?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Prompt tuning
- C. One-shot prompting
- D. Zero-shot prompting

### 58. An adaptation dataset contains contradictory expected answers. What should happen before running more training?

Domain: Fundamentals of gen AI

- A. Choose only the largest available model
- B. Improve data accuracy, completeness, consistency, and relevance
- C. Adjust temperature to control sampling variability
- D. Add more data without checking its quality

### 59. A prompt change improves accuracy but doubles latency beyond the workflow limit. How should it be assessed?

Domain: Business strategies for a successful gen AI solution

- A. Measure sustained appropriate use and task success
- B. Evaluate objectives and constraints together
- C. Output token generation rate
- D. Compare cost per verified acceptable outcome

### 60. Overall answer accuracy improves, but performance drops sharply for one relevant user group. What additional evaluation is needed?

Domain: Business strategies for a successful gen AI solution

- A. Minimize and protect personal data for the approved purpose
- B. Test subgroup outcomes and investigate disparities
- C. Provide meaningful decision factors and reviewable evidence
- D. Supported structured output plus schema validation

### 61. A request includes instructions, long history, documents, and a desired answer. What needs an explicit capacity plan?

Domain: Techniques to improve gen AI model output

- A. Set an appropriate maximum output length
- B. Coherent document chunking
- C. Budget and select relevant context
- D. Validated history compaction

### 62. A team wants to shorten long conversational history while preserving verified commitments. Which approach should it test?

Domain: Techniques to improve gen AI model output

- A. Model training
- B. Quantization
- C. Validated history compaction
- D. Low-rank adaptation (LoRA)

### 63. A stateless model API forgets a customer's earlier preference when the next request omits it. What application capability is needed?

Domain: Google Cloud’s gen AI offerings

- A. Pretraining
- B. Governed application-managed conversation state
- C. Supervised fine-tuning
- D. Model weights

### 64. Before retaining conversation summaries, which assessment remains necessary even if the model is stateless?

Domain: Business strategies for a successful gen AI solution

- A. Governed application-managed conversation state
- B. Review service-specific retention and data-use terms
- C. Context window
- D. Model weights

### 65. An engineer claims every context overflow silently drops the oldest sentence. What should the design actually follow?

Domain: Techniques to improve gen AI model output

- A. Validated history compaction
- B. Training batch
- C. Coherent document chunking
- D. Budget and select relevant context

### 66. A retrieved page contains text that looks like a new system instruction. How should its role in the prompt be represented?

Domain: Techniques to improve gen AI model output

- A. Adjust temperature to control sampling variability
- B. Choose only the largest available model
- C. Clearly separate instructions from untrusted source content
- D. Top-k sampling

### 67. A complex request demands five incompatible formats at once. Which revision should come first?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Few-shot prompting
- C. Specify audience, task, constraints, and output expectations
- D. Set an appropriate maximum output length

### 68. A single prompt repeatedly mixes extraction errors with drafting errors. Which decomposition can help isolate the causes?

Domain: Techniques to improve gen AI model output

- A. Zero-shot prompting
- B. Prompt chaining
- C. Role prompting
- D. One-shot prompting

### 69. A customer assistant is intended only for product support, but users ask for unrelated legal advice. What should the design define?

Domain: Techniques to improve gen AI model output

- A. Define permitted tasks and non-goals
- B. Enforce task, tool-call, and spending budgets
- C. Role prompting
- D. Configure and test appropriate safety controls

### 70. A source-only summary prompt cannot find evidence for a requested date. What behavior is preferable to choosing a plausible date?

Domain: Techniques to improve gen AI model output

- A. Adjust temperature to control sampling variability
- B. Choose only the largest available model
- C. Greedy next-token selection
- D. Abstain or escalate when evidence is insufficient

### 71. Answers consistently cite last year's procedure even though the prompt is clear. What should be investigated first?

Domain: Techniques to improve gen AI model output

- A. Rerank retrieved candidates
- B. Coherent document chunking
- C. Refresh and govern the retrieval index
- D. Improve data accuracy, completeness, consistency, and relevance

### 72. The correct evidence exists in the corpus but never enters the candidate set. Which retrieval metric should guide diagnosis?

Domain: Techniques to improve gen AI model output

- A. Time to first token
- B. Evaluate answer groundedness
- C. Output token generation rate
- D. Retrieval recall

### 73. Results contain almost every relevant source but are overwhelmed by unrelated material. Which retrieval metric highlights that clutter?

Domain: Techniques to improve gen AI model output

- A. Retrieval recall
- B. Evaluate answer groundedness
- C. Training epoch
- D. Retrieval precision

### 74. A retrieved passage says delivery takes five days; the answer says two days. Which check is directly relevant?

Domain: Techniques to improve gen AI model output

- A. Evaluate answer groundedness
- B. Retrieval precision
- C. Output token generation rate
- D. Retrieval recall

### 75. An integration crashes because fields appear under unpredictable names. What output improvement is most targeted?

Domain: Techniques to improve gen AI model output

- A. Role prompting
- B. Adjust temperature to control sampling variability
- C. Supported structured output plus schema validation
- D. Top-k sampling

### 76. A customer answer uses unexplained internal acronyms. What is the most direct prompt improvement?

Domain: Techniques to improve gen AI model output

- A. Specify audience, task, constraints, and output expectations
- B. Role prompting
- C. Set an appropriate maximum output length
- D. Few-shot prompting

### 77. A proposed prompt is excellent on English examples but poor on required multilingual requests. What evaluation design change is needed?

Domain: Techniques to improve gen AI model output

- A. Continuously evaluate, version, and monitor the solution
- B. Version prompts and regression-test revisions
- C. Collect reviewed user feedback and verified outcomes
- D. Independent representative evaluation

### 78. An AI-generated SQL query is syntactically valid but reads unauthorized tables. What review approach is needed?

Domain: Google Cloud’s gen AI offerings

- A. Supported structured output plus schema validation
- B. Set an appropriate maximum output length
- C. Configure and test appropriate safety controls
- D. Review, test, and scan generated code before use

### 79. Prompt A costs less per call but needs three retries for acceptable output. How should it be compared with Prompt B?

Domain: Business strategies for a successful gen AI solution

- A. Track variable usage and fixed operating cost separately
- B. Time to first token
- C. Measure sustained appropriate use and task success
- D. Compare cost per verified acceptable outcome

### 80. A new prompt appears better offline. How should a consequential production rollout proceed?

Domain: Business strategies for a successful gen AI solution

- A. Version prompts and regression-test revisions
- B. Independent representative evaluation
- C. Stage deployment with quality gates and rollback
- D. Adversarial and misuse-oriented testing

### 81. A product assistant needs current specification citations, while its general language style is already satisfactory. What improvement should be prioritized?

Domain: Techniques to improve gen AI model output

- A. Pretraining
- B. Supervised fine-tuning
- C. Retrieval-augmented generation (RAG)
- D. Low-rank adaptation (LoRA)

### 82. A model knows the relevant facts but repeatedly violates a stable specialized response pattern. Curated examples and a supported tuning path exist. What may help?

Domain: Techniques to improve gen AI model output

- A. Supervised fine-tuning
- B. Retrieval-augmented generation (RAG)
- C. Refresh and govern the retrieval index
- D. Budget and select relevant context

### 83. Semantic search misses exact legal clause numbers that keyword search finds. Which combined retrieval approach deserves evaluation?

Domain: Techniques to improve gen AI model output

- A. Quantization
- B. Hybrid lexical and vector retrieval
- C. Adjust temperature to control sampling variability
- D. Greedy next-token selection

### 84. Search returns tiny fragments that omit the sentence defining an exception. What preprocessing decision may be causing the problem?

Domain: Techniques to improve gen AI model output

- A. Choose only the largest available model
- B. Add more data without checking its quality
- C. Adjust temperature to control sampling variability
- D. Coherent document chunking

### 85. A regulator-facing report must be accountable and source-checked before release. What should complement model generation?

Domain: Techniques to improve gen AI model output

- A. Supported structured output plus schema validation
- B. Human-in-the-loop review
- C. Calibrate automated judging with expert review
- D. Configure and test appropriate safety controls

### 86. A malicious document asks the assistant to email payroll data elsewhere. What control actually prevents the unauthorized send?

Domain: Google Cloud’s gen AI offerings

- A. Role prompting
- B. Authorize and validate tool calls before execution
- C. Clearly separate instructions from untrusted source content
- D. Human approval before a consequential action

### 87. Users flag answers with outdated terminology. How should those reports be incorporated?

Domain: Business strategies for a successful gen AI solution

- A. Collect reviewed user feedback and verified outcomes
- B. Continuously evaluate, version, and monitor the solution
- C. Calibrate automated judging with expert review
- D. Measure sustained appropriate use and task success

### 88. An assistant invents a source URL while correctly following the requested tone. What should quality review focus on?

Domain: Techniques to improve gen AI model output

- A. Verify claims against cited source passages
- B. Supported structured output plus schema validation
- C. Calibrate automated judging with expert review
- D. Evaluate answer groundedness

### 89. A required JSON field is present but its currency unit is wrong. What verification is still needed?

Domain: Google Cloud’s gen AI offerings

- A. Supported structured output plus schema validation
- B. Document AI
- C. Set an appropriate maximum output length
- D. Extract, validate, and reconcile structured fields

### 90. A grounded assistant becomes less accurate after a repository reorganization. What operating practice should identify and investigate this?

Domain: Techniques to improve gen AI model output

- A. Protected audit trails and traceability
- B. Independent representative evaluation
- C. Continuously evaluate, version, and monitor the solution
- D. Pretraining

### 91. A prompt includes a huge source packet, and users wait a long time before seeing any streamed output. Which metric should first isolate the startup problem?

Domain: Techniques to improve gen AI model output

- A. Time to first token
- B. ROUGE
- C. Output token generation rate
- D. Retrieval precision

### 92. Streaming begins promptly but a long answer arrives slowly. Which measurement distinguishes output production speed from initial delay?

Domain: Techniques to improve gen AI model output

- A. Time to first token
- B. Output token generation rate
- C. BLEU
- D. Retrieval recall

### 93. Thousands of requests share the same eligible long instruction prefix but need fresh personalized answers. Which supported optimization could reuse prefix processing?

Domain: Google Cloud’s gen AI offerings

- A. Governed response caching
- B. Retrieval-augmented generation (RAG)
- C. Governed application-managed conversation state
- D. Supported prompt-prefix caching

### 94. An approved public FAQ has identical answers and a controlled freshness period. Which optimization may avoid repeated generation entirely?

Domain: Google Cloud’s gen AI offerings

- A. Supervised fine-tuning
- B. Supported prompt-prefix caching
- C. Governed response caching
- D. Pretraining

### 95. An engineer proposes one shared response cache for all personalized account questions. What consideration should block that naive design?

Domain: Business strategies for a successful gen AI solution

- A. Pseudonymization
- B. Minimize and protect personal data for the approved purpose
- C. Governed response caching
- D. Output token generation rate

### 96. A summary has low wording overlap with a reference despite preserving its facts. Which metric's limitation could explain the low score?

Domain: Fundamentals of gen AI

- A. ROUGE
- B. Time to first token
- C. Perplexity on a comparable evaluation setup
- D. Output token generation rate

### 97. A translated sentence uses a correct alternative expression that differs from a single reference. Which common metric should not be treated as a complete quality verdict?

Domain: Fundamentals of gen AI

- A. BLEU
- B. Retrieval precision
- C. ROUGE
- D. Time to first token

### 98. Two language models use different tokenizers. Which metric requires particular care before comparing headline values across them?

Domain: Fundamentals of gen AI

- A. Retrieval recall
- B. Perplexity on a comparable evaluation setup
- C. Time to first token
- D. Evaluate answer groundedness

### 99. A task can be routed to a smaller model if it meets the same required quality and controls. What should justify that routing?

Domain: Fundamentals of gen AI

- A. Evaluate model fit against business and operational requirements
- B. Model Garden on Agent Platform
- C. Compare cost per verified acceptable outcome
- D. Independent representative evaluation

### 100. A team wants to know whether a revised assistant actually improves task completion for its users. What evaluation approach is most useful?

Domain: Business strategies for a successful gen AI solution

- A. Compare a pilot with an appropriate control or baseline
- B. Collect reviewed user feedback and verified outcomes
- C. Calibrate automated judging with expert review
- D. Establish pre-change business performance

---

## Answer key and explanations

### Question 1 — B

Answer: Specify audience, task, constraints, and output expectations. Define what better means through the audience, task, constraints, and expected output. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Define what better means through the audience, task, constraints, and expected output.
- **B:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: Define what better means through the audience, task, constraints, and expected output.
- **C:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Define what better means through the audience, task, constraints, and expected output.
- **D:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Define what better means through the audience, task, constraints, and expected output.

### Question 2 — D

Answer: Prompt engineering. Instruction and context design are prompt engineering, not model training. Refines instructions, examples, and context at inference time without changing learned model weights. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Instruction and context design are prompt engineering, not model training.
- **B:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Instruction and context design are prompt engineering, not model training.
- **C:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Instruction and context design are prompt engineering, not model training.
- **D:** Correct. Refines instructions, examples, and context at inference time without changing learned model weights. In this case: Instruction and context design are prompt engineering, not model training.

### Question 3 — D

Answer: Role prompting. The prompt assigns a perspective or role; that does not grant professional authority or factual expertise. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: The prompt assigns a perspective or role; that does not grant professional authority or factual expertise.
- **B:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: The prompt assigns a perspective or role; that does not grant professional authority or factual expertise.
- **C:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: The prompt assigns a perspective or role; that does not grant professional authority or factual expertise.
- **D:** Correct. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: The prompt assigns a perspective or role; that does not grant professional authority or factual expertise.

### Question 4 — D

Answer: Zero-shot prompting. No demonstrations are supplied, which defines zero-shot prompting. Gives task instructions without a worked example in the prompt. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: No demonstrations are supplied, which defines zero-shot prompting.
- **B:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: No demonstrations are supplied, which defines zero-shot prompting.
- **C:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: No demonstrations are supplied, which defines zero-shot prompting.
- **D:** Correct. Gives task instructions without a worked example in the prompt. In this case: No demonstrations are supplied, which defines zero-shot prompting.

### Question 5 — A

Answer: One-shot prompting. One demonstration distinguishes one-shot from zero-shot and few-shot formats. Provides one worked demonstration of the desired task behavior in the prompt. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Provides one worked demonstration of the desired task behavior in the prompt. In this case: One demonstration distinguishes one-shot from zero-shot and few-shot formats.
- **B:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: One demonstration distinguishes one-shot from zero-shot and few-shot formats.
- **C:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: One demonstration distinguishes one-shot from zero-shot and few-shot formats.
- **D:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: One demonstration distinguishes one-shot from zero-shot and few-shot formats.

### Question 6 — A

Answer: Few-shot prompting. Multiple demonstrations guide behavior in context without necessarily updating parameters. Provides several worked demonstrations of the desired input-output behavior in the prompt. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Multiple demonstrations guide behavior in context without necessarily updating parameters.
- **B:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: Multiple demonstrations guide behavior in context without necessarily updating parameters.
- **C:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Multiple demonstrations guide behavior in context without necessarily updating parameters.
- **D:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: Multiple demonstrations guide behavior in context without necessarily updating parameters.

### Question 7 — C

Answer: Clearly separate instructions from untrusted source content. Clearly mark the source as data and keep trusted instructions separate, while recognizing delimiters are not a security boundary. Reduces ambiguity and marks external material as data. Delimiters alone are not a security boundary. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Clearly mark the source as data and keep trusted instructions separate, while recognizing delimiters are not a security boundary.
- **B:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Clearly mark the source as data and keep trusted instructions separate, while recognizing delimiters are not a security boundary.
- **C:** Correct. Reduces ambiguity and marks external material as data. Delimiters alone are not a security boundary. In this case: Clearly mark the source as data and keep trusted instructions separate, while recognizing delimiters are not a security boundary.
- **D:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Clearly mark the source as data and keep trusted instructions separate, while recognizing delimiters are not a security boundary.

### Question 8 — C

Answer: Specify audience, task, constraints, and output expectations. An explicit audience and level of detail address the observed mismatch more directly than a model-size change. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: An explicit audience and level of detail address the observed mismatch more directly than a model-size change.
- **B:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: An explicit audience and level of detail address the observed mismatch more directly than a model-size change.
- **C:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: An explicit audience and level of detail address the observed mismatch more directly than a model-size change.
- **D:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: An explicit audience and level of detail address the observed mismatch more directly than a model-size change.

### Question 9 — B

Answer: Few-shot prompting. Representative labeled examples show the exact convention without claiming guaranteed compliance. Provides several worked demonstrations of the desired input-output behavior in the prompt. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Representative labeled examples show the exact convention without claiming guaranteed compliance.
- **B:** Correct. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Representative labeled examples show the exact convention without claiming guaranteed compliance.
- **C:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Representative labeled examples show the exact convention without claiming guaranteed compliance.
- **D:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Representative labeled examples show the exact convention without claiming guaranteed compliance.

### Question 10 — A

Answer: Version prompts and regression-test revisions. Track actual prompt content and changes so comparisons and rollbacks are possible. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Track actual prompt content and changes so comparisons and rollbacks are possible.
- **B:** Incorrect for this question. Records necessary actions, versions, and approvals for investigation while controlling sensitive telemetry access and retention. In this case: Track actual prompt content and changes so comparisons and rollbacks are possible.
- **C:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Track actual prompt content and changes so comparisons and rollbacks are possible.
- **D:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Track actual prompt content and changes so comparisons and rollbacks are possible.

### Question 11 — A

Answer: Prompt chaining. Separate linked stages form a prompt chain rather than a single unconstrained request. Uses linked prompt steps or exchanges so one stage informs later stages of a larger task. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Uses linked prompt steps or exchanges so one stage informs later stages of a larger task. In this case: Separate linked stages form a prompt chain rather than a single unconstrained request.
- **B:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: Separate linked stages form a prompt chain rather than a single unconstrained request.
- **C:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Separate linked stages form a prompt chain rather than a single unconstrained request.
- **D:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Separate linked stages form a prompt chain rather than a single unconstrained request.

### Question 12 — B

Answer: Order dependent workflow stages. A dependent step must wait for its prerequisite instead of using unavailable or unchecked information. Ensures later steps receive validated earlier outputs. Parallelizing a dependency can produce incomplete or incorrect work. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Can reduce duration when branches are independent and resource limits permit. Dependent work still follows its prerequisites. In this case: A dependent step must wait for its prerequisite instead of using unavailable or unchecked information.
- **B:** Correct. Ensures later steps receive validated earlier outputs. Parallelizing a dependency can produce incomplete or incorrect work. In this case: A dependent step must wait for its prerequisite instead of using unavailable or unchecked information.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: A dependent step must wait for its prerequisite instead of using unavailable or unchecked information.
- **D:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: A dependent step must wait for its prerequisite instead of using unavailable or unchecked information.

### Question 13 — C

Answer: Parallelize independent work with a controlled join. Independent branches can run concurrently when limits permit, followed by a controlled join. Can reduce duration when branches are independent and resource limits permit. Dependent work still follows its prerequisites. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: Independent branches can run concurrently when limits permit, followed by a controlled join.
- **B:** Incorrect for this question. Ensures later steps receive validated earlier outputs. Parallelizing a dependency can produce incomplete or incorrect work. In this case: Independent branches can run concurrently when limits permit, followed by a controlled join.
- **C:** Correct. Can reduce duration when branches are independent and resource limits permit. Dependent work still follows its prerequisites. In this case: Independent branches can run concurrently when limits permit, followed by a controlled join.
- **D:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Independent branches can run concurrently when limits permit, followed by a controlled join.

### Question 14 — D

Answer: Chain-of-thought-style prompting. Step-oriented prompting resembles chain-of-thought-style instruction, but visible reasoning is not proof of correctness. Uses intermediate-step demonstrations or structured problem-solving guidance; it is not a guarantee of correctness or access to private internal reasoning. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: Step-oriented prompting resembles chain-of-thought-style instruction, but visible reasoning is not proof of correctness.
- **B:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: Step-oriented prompting resembles chain-of-thought-style instruction, but visible reasoning is not proof of correctness.
- **C:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Step-oriented prompting resembles chain-of-thought-style instruction, but visible reasoning is not proof of correctness.
- **D:** Correct. Uses intermediate-step demonstrations or structured problem-solving guidance; it is not a guarantee of correctness or access to private internal reasoning. In this case: Step-oriented prompting resembles chain-of-thought-style instruction, but visible reasoning is not proof of correctness.

### Question 15 — C

Answer: ReAct-style reasoning and action. ReAct-style work interleaves reasoning and actions, unlike a purely fixed text transformation. Combines deciding a next step with permitted external actions and observations in a controlled loop. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: ReAct-style work interleaves reasoning and actions, unlike a purely fixed text transformation.
- **B:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: ReAct-style work interleaves reasoning and actions, unlike a purely fixed text transformation.
- **C:** Correct. Combines deciding a next step with permitted external actions and observations in a controlled loop. In this case: ReAct-style work interleaves reasoning and actions, unlike a purely fixed text transformation.
- **D:** Incorrect for this question. Uses linked prompt steps or exchanges so one stage informs later stages of a larger task. In this case: ReAct-style work interleaves reasoning and actions, unlike a purely fixed text transformation.

### Question 16 — A

Answer: Validate tool results before downstream use. Validate the observation rather than propagate a suspect tool result through the chain. Checks schema, plausibility, status, and policy. A successful HTTP status does not guarantee a correct business result. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Checks schema, plausibility, status, and policy. A successful HTTP status does not guarantee a correct business result. In this case: Validate the observation rather than propagate a suspect tool result through the chain.
- **B:** Incorrect for this question. Limits stalled work and communicates failure or escalation. Local timeout or cancellation does not prove that a remote operation was rolled back. In this case: Validate the observation rather than propagate a suspect tool result through the chain.
- **C:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Validate the observation rather than propagate a suspect tool result through the chain.
- **D:** Incorrect for this question. Checks the caller, action, arguments, and business policy in trusted code. The model proposes a call; it does not itself grant permission. In this case: Validate the observation rather than propagate a suspect tool result through the chain.

### Question 17 — D

Answer: Enforce task, tool-call, and spending budgets. A workflow needs explicit iteration or task budgets in addition to per-response token limits. Bounds autonomous work and delegation. A stopping condition is separate from content moderation or prompt length. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: A workflow needs explicit iteration or task budgets in addition to per-response token limits.
- **B:** Incorrect for this question. Limits stalled work and communicates failure or escalation. Local timeout or cancellation does not prove that a remote operation was rolled back. In this case: A workflow needs explicit iteration or task budgets in addition to per-response token limits.
- **C:** Incorrect for this question. Reuses eligible results only within appropriate identity, freshness, and semantic boundaries. Similar wording alone does not make a cached answer safe. In this case: A workflow needs explicit iteration or task budgets in addition to per-response token limits.
- **D:** Correct. Bounds autonomous work and delegation. A stopping condition is separate from content moderation or prompt length. In this case: A workflow needs explicit iteration or task budgets in addition to per-response token limits.

### Question 18 — C

Answer: Independent representative evaluation. Evaluate independent representative cases to detect overfitting to the development examples. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Evaluate independent representative cases to detect overfitting to the development examples.
- **B:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Evaluate independent representative cases to detect overfitting to the development examples.
- **C:** Correct. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Evaluate independent representative cases to detect overfitting to the development examples.
- **D:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Evaluate independent representative cases to detect overfitting to the development examples.

### Question 19 — B

Answer: Specify audience, task, constraints, and output expectations. State output and evidence constraints directly, while retaining external evaluation and review. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: State output and evidence constraints directly, while retaining external evaluation and review.
- **B:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: State output and evidence constraints directly, while retaining external evaluation and review.
- **C:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: State output and evidence constraints directly, while retaining external evaluation and review.
- **D:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: State output and evidence constraints directly, while retaining external evaluation and review.

### Question 20 — D

Answer: Authorize and validate tool calls before execution. Trusted code and business policy must authorize actions; prompt wording cannot grant real privileges. Checks the caller, action, arguments, and business policy in trusted code. The model proposes a call; it does not itself grant permission. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: Trusted code and business policy must authorize actions; prompt wording cannot grant real privileges.
- **B:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Trusted code and business policy must authorize actions; prompt wording cannot grant real privileges.
- **C:** Incorrect for this question. Places a qualified decision before the external effect with proper correlation and authorization. Reviewing afterward cannot undo every side effect. In this case: Trusted code and business policy must authorize actions; prompt wording cannot grant real privileges.
- **D:** Correct. Checks the caller, action, arguments, and business policy in trusted code. The model proposes a call; it does not itself grant permission. In this case: Trusted code and business policy must authorize actions; prompt wording cannot grant real privileges.

### Question 21 — C

Answer: Adjust temperature to control sampling variability. Temperature affects distribution sharpness where supported, not truth verification or business authorization. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Temperature affects distribution sharpness where supported, not truth verification or business authorization.
- **B:** Incorrect for this question. Restricts the candidate token set using cumulative probability mass rather than a fixed response length. In this case: Temperature affects distribution sharpness where supported, not truth verification or business authorization.
- **C:** Correct. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Temperature affects distribution sharpness where supported, not truth verification or business authorization.
- **D:** Incorrect for this question. Bounds the information a model can consider within a request according to model-specific limits. In this case: Temperature affects distribution sharpness where supported, not truth verification or business authorization.

### Question 22 — C

Answer: Adjust top-p nucleus sampling. Top-p selects a candidate set using cumulative probability mass. Restricts the candidate token set using cumulative probability mass rather than a fixed response length. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Top-p selects a candidate set using cumulative probability mass.
- **B:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Top-p selects a candidate set using cumulative probability mass.
- **C:** Correct. Restricts the candidate token set using cumulative probability mass rather than a fixed response length. In this case: Top-p selects a candidate set using cumulative probability mass.
- **D:** Incorrect for this question. Is one pass over the designated training dataset under the training setup. It is not the number of examples processed in an individual update. In this case: Top-p selects a candidate set using cumulative probability mass.

### Question 23 — D

Answer: Top-k sampling. Top-k uses a fixed candidate count; it is different from a probability threshold. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Bounds the information a model can consider within a request according to model-specific limits. In this case: Top-k uses a fixed candidate count; it is different from a probability threshold.
- **B:** Incorrect for this question. Restricts the candidate token set using cumulative probability mass rather than a fixed response length. In this case: Top-k uses a fixed candidate count; it is different from a probability threshold.
- **C:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Top-k uses a fixed candidate count; it is different from a probability threshold.
- **D:** Correct. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Top-k uses a fixed candidate count; it is different from a probability threshold.

### Question 24 — C

Answer: Set an appropriate maximum output length. Maximum output capacity directly limits response length, subject to the model's overall limits. Caps generated output tokens within supported limits; too low a cap can truncate an answer. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Is one pass over the designated training dataset under the training setup. It is not the number of examples processed in an individual update. In this case: Maximum output capacity directly limits response length, subject to the model's overall limits.
- **B:** Incorrect for this question. Defines token IDs available to the tokenizer. Its size is different from the number of tokens allowed in one request. In this case: Maximum output capacity directly limits response length, subject to the model's overall limits.
- **C:** Correct. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Maximum output capacity directly limits response length, subject to the model's overall limits.
- **D:** Incorrect for this question. Is a group of examples processed together in a training step or accumulation scheme. Batch size is not a context-window limit. In this case: Maximum output capacity directly limits response length, subject to the model's overall limits.

### Question 25 — D

Answer: Supported structured output plus schema validation. Supported structured output and schema validation target the exact format requirement. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Supported structured output and schema validation target the exact format requirement.
- **B:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Supported structured output and schema validation target the exact format requirement.
- **C:** Incorrect for this question. A supported generated delimiter can terminate a response. A naive delimiter such as a closing brace can truncate nested JSON or omit required syntax. In this case: Supported structured output and schema validation target the exact format requirement.
- **D:** Correct. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Supported structured output and schema validation target the exact format requirement.

### Question 26 — B

Answer: Configured stop sequence. A stop sequence can terminate at an inner object before the complete outer structure is generated. A supported generated delimiter can terminate a response. A naive delimiter such as a closing brace can truncate nested JSON or omit required syntax. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: A stop sequence can terminate at an inner object before the complete outer structure is generated.
- **B:** Correct. A supported generated delimiter can terminate a response. A naive delimiter such as a closing brace can truncate nested JSON or omit required syntax. In this case: A stop sequence can terminate at an inner object before the complete outer structure is generated.
- **C:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: A stop sequence can terminate at an inner object before the complete outer structure is generated.
- **D:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: A stop sequence can terminate at an inner object before the complete outer structure is generated.

### Question 27 — A

Answer: Evaluate answer groundedness. Check whether claims follow the supplied evidence instead of equating low variability with groundedness. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Check whether claims follow the supplied evidence instead of equating low variability with groundedness.
- **B:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: Check whether claims follow the supplied evidence instead of equating low variability with groundedness.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Check whether claims follow the supplied evidence instead of equating low variability with groundedness.
- **D:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Check whether claims follow the supplied evidence instead of equating low variability with groundedness.

### Question 28 — B

Answer: Extract, validate, and reconcile structured fields. Semantic extraction checks must reconcile content with evidence; structure alone is insufficient. Combines supported extraction with checks against source evidence and business rules. Valid JSON alone does not establish field accuracy. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Extracts and processes information from supported documents, including structured fields for suitable processors. In this case: Semantic extraction checks must reconcile content with evidence; structure alone is insufficient.
- **B:** Correct. Combines supported extraction with checks against source evidence and business rules. Valid JSON alone does not establish field accuracy. In this case: Semantic extraction checks must reconcile content with evidence; structure alone is insufficient.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Semantic extraction checks must reconcile content with evidence; structure alone is insufficient.
- **D:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Semantic extraction checks must reconcile content with evidence; structure alone is insufficient.

### Question 29 — A

Answer: Specify audience, task, constraints, and output expectations. Specify the desired table format and scope before treating the issue as a model architecture problem. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: Specify the desired table format and scope before treating the issue as a model architecture problem.
- **B:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Specify the desired table format and scope before treating the issue as a model architecture problem.
- **C:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Specify the desired table format and scope before treating the issue as a model architecture problem.
- **D:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Specify the desired table format and scope before treating the issue as a model architecture problem.

### Question 30 — D

Answer: Independent representative evaluation. Versioned independent tests provide comparison evidence; low sampling settings alone cannot guarantee cross-version reproducibility. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Versioned independent tests provide comparison evidence; low sampling settings alone cannot guarantee cross-version reproducibility.
- **B:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Versioned independent tests provide comparison evidence; low sampling settings alone cannot guarantee cross-version reproducibility.
- **C:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Versioned independent tests provide comparison evidence; low sampling settings alone cannot guarantee cross-version reproducibility.
- **D:** Correct. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Versioned independent tests provide comparison evidence; low sampling settings alone cannot guarantee cross-version reproducibility.

### Question 31 — B

Answer: Ground with authorized first-party enterprise data. Approved company policy is first-party evidence, not a fact to infer from public web material. Uses approved organizational evidence for private business facts, with appropriate access controls. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Approved company policy is first-party evidence, not a fact to infer from public web material.
- **B:** Correct. Uses approved organizational evidence for private business facts, with appropriate access controls. In this case: Approved company policy is first-party evidence, not a fact to infer from public web material.
- **C:** Incorrect for this question. Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available. In this case: Approved company policy is first-party evidence, not a fact to infer from public web material.
- **D:** Incorrect for this question. Uses permitted information from an external provider when that source is authoritative for the requirement. In this case: Approved company policy is first-party evidence, not a fact to infer from public web material.

### Question 32 — A

Answer: Ground with a licensed or approved third-party source. A licensed external reference is third-party evidence, with permissions and usage obligations. Uses permitted information from an external provider when that source is authoritative for the requirement. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Uses permitted information from an external provider when that source is authoritative for the requirement. In this case: A licensed external reference is third-party evidence, with permissions and usage obligations.
- **B:** Incorrect for this question. Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available. In this case: A licensed external reference is third-party evidence, with permissions and usage obligations.
- **C:** Incorrect for this question. Uses approved organizational evidence for private business facts, with appropriate access controls. In this case: A licensed external reference is third-party evidence, with permissions and usage obligations.
- **D:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: A licensed external reference is third-party evidence, with permissions and usage obligations.

### Question 33 — B

Answer: Ground with relevant public world information. Relevant public information can supply current world evidence where supported. Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Relevant public information can supply current world evidence where supported.
- **B:** Correct. Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available. In this case: Relevant public information can supply current world evidence where supported.
- **C:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Relevant public information can supply current world evidence where supported.
- **D:** Incorrect for this question. Uses approved organizational evidence for private business facts, with appropriate access controls. In this case: Relevant public information can supply current world evidence where supported.

### Question 34 — B

Answer: Use an authorized database lookup tool. An authorized transactional lookup provides the current customer-specific value. Retrieves authoritative structured business records through enforced access rather than inventing live facts from model weights. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: An authorized transactional lookup provides the current customer-specific value.
- **B:** Correct. Retrieves authoritative structured business records through enforced access rather than inventing live facts from model weights. In this case: An authorized transactional lookup provides the current customer-specific value.
- **C:** Incorrect for this question. Limits what facts could be learned during training; the model does not inherently know later events without additional evidence or tools. In this case: An authorized transactional lookup provides the current customer-specific value.
- **D:** Incorrect for this question. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: An authorized transactional lookup provides the current customer-specific value.

### Question 35 — B

Answer: Retrieval-augmented generation (RAG). RAG can add current passages at request time rather than repeatedly adapting parameters for document updates. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: RAG can add current passages at request time rather than repeatedly adapting parameters for document updates.
- **B:** Correct. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: RAG can add current passages at request time rather than repeatedly adapting parameters for document updates.
- **C:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: RAG can add current passages at request time rather than repeatedly adapting parameters for document updates.
- **D:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: RAG can add current passages at request time rather than repeatedly adapting parameters for document updates.

### Question 36 — D

Answer: Review rights, licenses, and permitted content use. Permission to access content is not equivalent to permission for every downstream use. Checks source and output obligations rather than assuming AI generation removes intellectual-property restrictions. Closest official exam-guide objective 4.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Uses appropriate public evidence, such as supported Search grounding, rather than assuming private records are publicly available. In this case: Permission to access content is not equivalent to permission for every downstream use.
- **B:** Incorrect for this question. Controls which principals may perform supported actions on resources through roles and policies. In this case: Permission to access content is not equivalent to permission for every downstream use.
- **C:** Incorrect for this question. Limits unnecessary collection, use, retention, and disclosure according to applicable obligations. In this case: Permission to access content is not equivalent to permission for every downstream use.
- **D:** Correct. Checks source and output obligations rather than assuming AI generation removes intellectual-property restrictions. In this case: Permission to access content is not equivalent to permission for every downstream use.

### Question 37 — A

Answer: Identity and Access Management (IAM). Retrieval must enforce the requester's access rather than trust the model not to reveal restricted text. Controls which principals may perform supported actions on resources through roles and policies. Closest official exam-guide objective 4.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Controls which principals may perform supported actions on resources through roles and policies. In this case: Retrieval must enforce the requester's access rather than trust the model not to reveal restricted text.
- **B:** Incorrect for this question. Uses approved organizational evidence for private business facts, with appropriate access controls. In this case: Retrieval must enforce the requester's access rather than trust the model not to reveal restricted text.
- **C:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: Retrieval must enforce the requester's access rather than trust the model not to reveal restricted text.
- **D:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Retrieval must enforce the requester's access rather than trust the model not to reveal restricted text.

### Question 38 — B

Answer: Verify claims against cited source passages. Citation support must be verified at the claim level, not inferred from the presence of a source label. Checks whether a citation actually supports the output. A plausible URL or citation marker is not proof of grounding. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Citation support must be verified at the claim level, not inferred from the presence of a source label.
- **B:** Correct. Checks whether a citation actually supports the output. A plausible URL or citation marker is not proof of grounding. In this case: Citation support must be verified at the claim level, not inferred from the presence of a source label.
- **C:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Citation support must be verified at the claim level, not inferred from the presence of a source label.
- **D:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Citation support must be verified at the claim level, not inferred from the presence of a source label.

### Question 39 — C

Answer: Abstain or escalate when evidence is insufficient. The system should acknowledge uncertainty or escalate rather than fabricate eligibility requirements. Avoids inventing a consequential answer when approved context lacks support. Defined user messaging and review routes improve usefulness. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: The system should acknowledge uncertainty or escalate rather than fabricate eligibility requirements.
- **B:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: The system should acknowledge uncertainty or escalate rather than fabricate eligibility requirements.
- **C:** Correct. Avoids inventing a consequential answer when approved context lacks support. Defined user messaging and review routes improve usefulness. In this case: The system should acknowledge uncertainty or escalate rather than fabricate eligibility requirements.
- **D:** Incorrect for this question. Can increase cost or latency without establishing task suitability or meeting governance requirements. In this case: The system should acknowledge uncertainty or escalate rather than fabricate eligibility requirements.

### Question 40 — A

Answer: Refresh and govern the retrieval index. Refresh and govern source versions so obsolete evidence is removed or clearly marked. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Refresh and govern source versions so obsolete evidence is removed or clearly marked.
- **B:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Refresh and govern source versions so obsolete evidence is removed or clearly marked.
- **C:** Incorrect for this question. Trains low-rank adaptation parameters in a supported fine-tuning setup while typically freezing base weights. It reduces trainable parameter count but does not guarantee unchanged behavior. In this case: Refresh and govern source versions so obsolete evidence is removed or clearly marked.
- **D:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Refresh and govern source versions so obsolete evidence is removed or clearly marked.

### Question 41 — D

Answer: Coherent document chunking. Coherent chunks can improve relevance and context efficiency while preserving metadata and meaning. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Coherent chunks can improve relevance and context efficiency while preserving metadata and meaning.
- **B:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Coherent chunks can improve relevance and context efficiency while preserving metadata and meaning.
- **C:** Incorrect for this question. Maps supported text units into token IDs and back. Tokens can be words, subwords, characters, or byte-derived units depending on the tokenizer. In this case: Coherent chunks can improve relevance and context efficiency while preserving metadata and meaning.
- **D:** Correct. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Coherent chunks can improve relevance and context efficiency while preserving metadata and meaning.

### Question 42 — C

Answer: Embedding representation. Embeddings allow similarity comparison, unlike token IDs alone or one-step output logits. Maps supported content to numeric vectors useful for similarity or other downstream tasks. Similarity is model-dependent and is not proof of factual equivalence. Closest official exam-guide objective 1.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Are unnormalized token scores that can be transformed and normalized for next-token selection. They are not usage logs or security permissions. In this case: Embeddings allow similarity comparison, unlike token IDs alone or one-step output logits.
- **B:** Incorrect for this question. Maps supported text units into token IDs and back. Tokens can be words, subwords, characters, or byte-derived units depending on the tokenizer. In this case: Embeddings allow similarity comparison, unlike token IDs alone or one-step output logits.
- **C:** Correct. Maps supported content to numeric vectors useful for similarity or other downstream tasks. Similarity is model-dependent and is not proof of factual equivalence. In this case: Embeddings allow similarity comparison, unlike token IDs alone or one-step output logits.
- **D:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Embeddings allow similarity comparison, unlike token IDs alone or one-step output logits.

### Question 43 — B

Answer: Hybrid lexical and vector retrieval. Combining lexical and vector retrieval can cover exact identifiers and paraphrase similarity. Combines exact-term matching with semantic similarity. It is useful for identifiers and paraphrases, subject to relevance and access evaluation. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Combining lexical and vector retrieval can cover exact identifiers and paraphrase similarity.
- **B:** Correct. Combines exact-term matching with semantic similarity. It is useful for identifiers and paraphrases, subject to relevance and access evaluation. In this case: Combining lexical and vector retrieval can cover exact identifiers and paraphrase similarity.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Combining lexical and vector retrieval can cover exact identifiers and paraphrase similarity.
- **D:** Incorrect for this question. Maps supported content to numeric vectors useful for similarity or other downstream tasks. Similarity is model-dependent and is not proof of factual equivalence. In this case: Combining lexical and vector retrieval can cover exact identifiers and paraphrase similarity.

### Question 44 — D

Answer: Rerank retrieved candidates. Reranking rescales candidate relevance after initial retrieval without recovering absent candidates. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Reranking rescales candidate relevance after initial retrieval without recovering absent candidates.
- **B:** Incorrect for this question. Trains low-rank adaptation parameters in a supported fine-tuning setup while typically freezing base weights. It reduces trainable parameter count but does not guarantee unchanged behavior. In this case: Reranking rescales candidate relevance after initial retrieval without recovering absent candidates.
- **C:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Reranking rescales candidate relevance after initial retrieval without recovering absent candidates.
- **D:** Correct. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. In this case: Reranking rescales candidate relevance after initial retrieval without recovering absent candidates.

### Question 45 — D

Answer: Retrieval recall. Recall measures coverage of relevant evidence, not cleanliness of the returned set. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Recall measures coverage of relevant evidence, not cleanliness of the returned set.
- **B:** Incorrect for this question. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Recall measures coverage of relevant evidence, not cleanliness of the returned set.
- **C:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Recall measures coverage of relevant evidence, not cleanliness of the returned set.
- **D:** Correct. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Recall measures coverage of relevant evidence, not cleanliness of the returned set.

### Question 46 — C

Answer: Retrieval precision. Precision is the relevant share of the retrieved result set. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Precision is the relevant share of the retrieved result set.
- **B:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Precision is the relevant share of the retrieved result set.
- **C:** Correct. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Precision is the relevant share of the retrieved result set.
- **D:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Precision is the relevant share of the retrieved result set.

### Question 47 — C

Answer: Evaluate answer groundedness. Generation must remain faithful to evidence even when retrieval is relevant. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Generation must remain faithful to evidence even when retrieval is relevant.
- **B:** Incorrect for this question. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Generation must remain faithful to evidence even when retrieval is relevant.
- **C:** Correct. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Generation must remain faithful to evidence even when retrieval is relevant.
- **D:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Generation must remain faithful to evidence even when retrieval is relevant.

### Question 48 — C

Answer: Budget and select relevant context. Select sufficient relevant evidence within capacity instead of indiscriminately stuffing every result into context. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Select sufficient relevant evidence within capacity instead of indiscriminately stuffing every result into context.
- **B:** Incorrect for this question. Replaces verbose history with checked summaries and important factual state. Summaries can lose or distort details and need verification. In this case: Select sufficient relevant evidence within capacity instead of indiscriminately stuffing every result into context.
- **C:** Correct. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. In this case: Select sufficient relevant evidence within capacity instead of indiscriminately stuffing every result into context.
- **D:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Select sufficient relevant evidence within capacity instead of indiscriminately stuffing every result into context.

### Question 49 — A

Answer: Rerank retrieved candidates. Reranking only reorders candidates it receives; initial retrieval must first capture missing evidence. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. In this case: Reranking only reorders candidates it receives; initial retrieval must first capture missing evidence.
- **B:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Reranking only reorders candidates it receives; initial retrieval must first capture missing evidence.
- **C:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Reranking only reorders candidates it receives; initial retrieval must first capture missing evidence.
- **D:** Incorrect for this question. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Reranking only reorders candidates it receives; initial retrieval must first capture missing evidence.

### Question 50 — C

Answer: Refresh and govern the retrieval index. Source changes and deletion obligations must propagate to indexes and other governed copies. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. In this case: Source changes and deletion obligations must propagate to indexes and other governed copies.
- **B:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Source changes and deletion obligations must propagate to indexes and other governed copies.
- **C:** Correct. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Source changes and deletion obligations must propagate to indexes and other governed copies.
- **D:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Source changes and deletion obligations must propagate to indexes and other governed copies.

### Question 51 — A

Answer: Independent representative evaluation. Independent representative cases reduce selection bias and reveal unanticipated failures. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Independent representative cases reduce selection bias and reveal unanticipated failures.
- **B:** Incorrect for this question. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Independent representative cases reduce selection bias and reveal unanticipated failures.
- **C:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Independent representative cases reduce selection bias and reveal unanticipated failures.
- **D:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Independent representative cases reduce selection bias and reveal unanticipated failures.

### Question 52 — A

Answer: Calibrate automated judging with expert review. Calibrate the grader against expert review and relevant failure cases before trusting its scores. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Calibrate the grader against expert review and relevant failure cases before trusting its scores.
- **B:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Calibrate the grader against expert review and relevant failure cases before trusting its scores.
- **C:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Calibrate the grader against expert review and relevant failure cases before trusting its scores.
- **D:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Calibrate the grader against expert review and relevant failure cases before trusting its scores.

### Question 53 — D

Answer: Human-in-the-loop review. Qualified human review addresses consequential errors that formatting and sampling controls do not resolve. Uses qualified people to verify, approve, correct, or escalate outputs, especially where consequences are significant. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Qualified human review addresses consequential errors that formatting and sampling controls do not resolve.
- **B:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Qualified human review addresses consequential errors that formatting and sampling controls do not resolve.
- **C:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Qualified human review addresses consequential errors that formatting and sampling controls do not resolve.
- **D:** Correct. Uses qualified people to verify, approve, correct, or escalate outputs, especially where consequences are significant. In this case: Qualified human review addresses consequential errors that formatting and sampling controls do not resolve.

### Question 54 — D

Answer: Continuously evaluate, version, and monitor the solution. Ongoing evaluation and monitoring can detect drift, emerging cases, and regressions. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Ongoing evaluation and monitoring can detect drift, emerging cases, and regressions.
- **B:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Ongoing evaluation and monitoring can detect drift, emerging cases, and regressions.
- **C:** Incorrect for this question. Records necessary actions, versions, and approvals for investigation while controlling sensitive telemetry access and retention. In this case: Ongoing evaluation and monitoring can detect drift, emerging cases, and regressions.
- **D:** Correct. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Ongoing evaluation and monitoring can detect drift, emerging cases, and regressions.

### Question 55 — C

Answer: Version prompts and regression-test revisions. Version the actual configuration and dependencies, while protecting sensitive request data. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Records necessary actions, versions, and approvals for investigation while controlling sensitive telemetry access and retention. In this case: Version the actual configuration and dependencies, while protecting sensitive request data.
- **B:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Version the actual configuration and dependencies, while protecting sensitive request data.
- **C:** Correct. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Version the actual configuration and dependencies, while protecting sensitive request data.
- **D:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Version the actual configuration and dependencies, while protecting sensitive request data.

### Question 56 — A

Answer: Supervised fine-tuning. Supervised fine-tuning may teach recurring behavior but still needs independent regression tests. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Supervised fine-tuning may teach recurring behavior but still needs independent regression tests.
- **B:** Incorrect for this question. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. In this case: Supervised fine-tuning may teach recurring behavior but still needs independent regression tests.
- **C:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: Supervised fine-tuning may teach recurring behavior but still needs independent regression tests.
- **D:** Incorrect for this question. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: Supervised fine-tuning may teach recurring behavior but still needs independent regression tests.

### Question 57 — B

Answer: Prompt tuning. Prompt tuning learns a parameterized prompt, unlike manually writing role instructions or examples. Learns task-specific prompt representations while keeping base model weights frozen in supported approaches; it differs from manually rewriting prompt text. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Prompt tuning learns a parameterized prompt, unlike manually writing role instructions or examples.
- **B:** Correct. Learns task-specific prompt representations while keeping base model weights frozen in supported approaches; it differs from manually rewriting prompt text. In this case: Prompt tuning learns a parameterized prompt, unlike manually writing role instructions or examples.
- **C:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: Prompt tuning learns a parameterized prompt, unlike manually writing role instructions or examples.
- **D:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: Prompt tuning learns a parameterized prompt, unlike manually writing role instructions or examples.

### Question 58 — B

Answer: Improve data accuracy, completeness, consistency, and relevance. Improving example accuracy and consistency addresses the underlying signal rather than magnifying contradictory data. Addresses defects in the source evidence; greater model capacity does not automatically repair incorrect data. Closest official exam-guide objective 1.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Can increase cost or latency without establishing task suitability or meeting governance requirements. In this case: Improving example accuracy and consistency addresses the underlying signal rather than magnifying contradictory data.
- **B:** Correct. Addresses defects in the source evidence; greater model capacity does not automatically repair incorrect data. In this case: Improving example accuracy and consistency addresses the underlying signal rather than magnifying contradictory data.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Improving example accuracy and consistency addresses the underlying signal rather than magnifying contradictory data.
- **D:** Incorrect for this question. Can amplify errors or irrelevant content and is not a substitute for data validation. In this case: Improving example accuracy and consistency addresses the underlying signal rather than magnifying contradictory data.

### Question 59 — B

Answer: Evaluate objectives and constraints together. Improvement must satisfy required quality and operational constraints together. Balances usefulness, speed, cost, privacy, and safety instead of maximizing one metric without boundaries. Closest official exam-guide objective 4.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Distinguishes installed seats or trial logins from useful adoption. Usage must be interpreted with quality and risk. In this case: Improvement must satisfy required quality and operational constraints together.
- **B:** Correct. Balances usefulness, speed, cost, privacy, and safety instead of maximizing one metric without boundaries. In this case: Improvement must satisfy required quality and operational constraints together.
- **C:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Improvement must satisfy required quality and operational constraints together.
- **D:** Incorrect for this question. Accounts for success rates, rework, review, and full workflow costs rather than only unit model pricing. In this case: Improvement must satisfy required quality and operational constraints together.

### Question 60 — B

Answer: Test subgroup outcomes and investigate disparities. Aggregate averages can hide subgroup failures and inappropriate disparities. Uses relevant, appropriate comparisons and review rather than inferring fairness from one aggregate score. Closest official exam-guide objective 4.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Limits unnecessary collection, use, retention, and disclosure according to applicable obligations. In this case: Aggregate averages can hide subgroup failures and inappropriate disparities.
- **B:** Correct. Uses relevant, appropriate comparisons and review rather than inferring fairness from one aggregate score. In this case: Aggregate averages can hide subgroup failures and inappropriate disparities.
- **C:** Incorrect for this question. Helps stakeholders understand a recommendation without claiming that a fluent generated rationale is the model real internal causal explanation. In this case: Aggregate averages can hide subgroup failures and inappropriate disparities.
- **D:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Aggregate averages can hide subgroup failures and inappropriate disparities.

### Question 61 — C

Answer: Budget and select relevant context. All relevant request components and model-specific generation accounting must fit supported limits. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: All relevant request components and model-specific generation accounting must fit supported limits.
- **B:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: All relevant request components and model-specific generation accounting must fit supported limits.
- **C:** Correct. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. In this case: All relevant request components and model-specific generation accounting must fit supported limits.
- **D:** Incorrect for this question. Replaces verbose history with checked summaries and important factual state. Summaries can lose or distort details and need verification. In this case: All relevant request components and model-specific generation accounting must fit supported limits.

### Question 62 — C

Answer: Validated history compaction. Checked compaction can preserve essential state more efficiently, but it is not lossless. Replaces verbose history with checked summaries and important factual state. Summaries can lose or distort details and need verification. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Learns model parameters from data; it is different from serving a trained model to users. In this case: Checked compaction can preserve essential state more efficiently, but it is not lossless.
- **B:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Checked compaction can preserve essential state more efficiently, but it is not lossless.
- **C:** Correct. Replaces verbose history with checked summaries and important factual state. Summaries can lose or distort details and need verification. In this case: Checked compaction can preserve essential state more efficiently, but it is not lossless.
- **D:** Incorrect for this question. Trains low-rank adaptation parameters in a supported fine-tuning setup while typically freezing base weights. It reduces trainable parameter count but does not guarantee unchanged behavior. In this case: Checked compaction can preserve essential state more efficiently, but it is not lossless.

### Question 63 — B

Answer: Governed application-managed conversation state. Persist and resupply permitted relevant state rather than assume every service automatically remembers prior calls. Stores and supplies relevant history where needed without implying model-weight updates. Stateful platform features and their retention policies must be reviewed separately. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Persist and resupply permitted relevant state rather than assume every service automatically remembers prior calls.
- **B:** Correct. Stores and supplies relevant history where needed without implying model-weight updates. Stateful platform features and their retention policies must be reviewed separately. In this case: Persist and resupply permitted relevant state rather than assume every service automatically remembers prior calls.
- **C:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Persist and resupply permitted relevant state rather than assume every service automatically remembers prior calls.
- **D:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Persist and resupply permitted relevant state rather than assume every service automatically remembers prior calls.

### Question 64 — B

Answer: Review service-specific retention and data-use terms. Application state has its own data-use and retention obligations independent of model weights. Checks logs, abuse monitoring, training use, deletion, account settings, and contracts. Frozen model weights alone do not establish zero retention. Closest official exam-guide objective 4.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Stores and supplies relevant history where needed without implying model-weight updates. Stateful platform features and their retention policies must be reviewed separately. In this case: Application state has its own data-use and retention obligations independent of model weights.
- **B:** Correct. Checks logs, abuse monitoring, training use, deletion, account settings, and contracts. Frozen model weights alone do not establish zero retention. In this case: Application state has its own data-use and retention obligations independent of model weights.
- **C:** Incorrect for this question. Bounds the information a model can consider within a request according to model-specific limits. In this case: Application state has its own data-use and retention obligations independent of model weights.
- **D:** Incorrect for this question. Are learned numerical parameters adjusted during training. Supplying a normal inference request does not inherently update them. In this case: Application state has its own data-use and retention obligations independent of model weights.

### Question 65 — D

Answer: Budget and select relevant context. Overflow behavior is implementation-specific, so capacity and truncation handling must follow documented service rules. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Replaces verbose history with checked summaries and important factual state. Summaries can lose or distort details and need verification. In this case: Overflow behavior is implementation-specific, so capacity and truncation handling must follow documented service rules.
- **B:** Incorrect for this question. Is a group of examples processed together in a training step or accumulation scheme. Batch size is not a context-window limit. In this case: Overflow behavior is implementation-specific, so capacity and truncation handling must follow documented service rules.
- **C:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Overflow behavior is implementation-specific, so capacity and truncation handling must follow documented service rules.
- **D:** Correct. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. In this case: Overflow behavior is implementation-specific, so capacity and truncation handling must follow documented service rules.

### Question 66 — C

Answer: Clearly separate instructions from untrusted source content. External content should be marked as untrusted data; separate execution controls remain necessary. Reduces ambiguity and marks external material as data. Delimiters alone are not a security boundary. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: External content should be marked as untrusted data; separate execution controls remain necessary.
- **B:** Incorrect for this question. Can increase cost or latency without establishing task suitability or meeting governance requirements. In this case: External content should be marked as untrusted data; separate execution controls remain necessary.
- **C:** Correct. Reduces ambiguity and marks external material as data. Delimiters alone are not a security boundary. In this case: External content should be marked as untrusted data; separate execution controls remain necessary.
- **D:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: External content should be marked as untrusted data; separate execution controls remain necessary.

### Question 67 — C

Answer: Specify audience, task, constraints, and output expectations. Resolve contradictory requirements and specify one coherent output contract. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Resolve contradictory requirements and specify one coherent output contract.
- **B:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Resolve contradictory requirements and specify one coherent output contract.
- **C:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: Resolve contradictory requirements and specify one coherent output contract.
- **D:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Resolve contradictory requirements and specify one coherent output contract.

### Question 68 — B

Answer: Prompt chaining. Separate extraction, validation, and drafting into checked stages rather than hide all failures in one output. Uses linked prompt steps or exchanges so one stage informs later stages of a larger task. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Gives task instructions without a worked example in the prompt. In this case: Separate extraction, validation, and drafting into checked stages rather than hide all failures in one output.
- **B:** Correct. Uses linked prompt steps or exchanges so one stage informs later stages of a larger task. In this case: Separate extraction, validation, and drafting into checked stages rather than hide all failures in one output.
- **C:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Separate extraction, validation, and drafting into checked stages rather than hide all failures in one output.
- **D:** Incorrect for this question. Provides one worked demonstration of the desired task behavior in the prompt. In this case: Separate extraction, validation, and drafting into checked stages rather than hide all failures in one output.

### Question 69 — A

Answer: Define permitted tasks and non-goals. Explicit permitted tasks and non-goals support appropriate refusal or handoff, with technical enforcement where needed. Sets business and agent boundaries before granting tools or autonomy. Behavioral descriptions still need technical enforcement. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Sets business and agent boundaries before granting tools or autonomy. Behavioral descriptions still need technical enforcement. In this case: Explicit permitted tasks and non-goals support appropriate refusal or handoff, with technical enforcement where needed.
- **B:** Incorrect for this question. Bounds autonomous work and delegation. A stopping condition is separate from content moderation or prompt length. In this case: Explicit permitted tasks and non-goals support appropriate refusal or handoff, with technical enforcement where needed.
- **C:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Explicit permitted tasks and non-goals support appropriate refusal or handoff, with technical enforcement where needed.
- **D:** Incorrect for this question. Can reduce supported harmful content but does not guarantee factual accuracy, authorization, or complete risk elimination. In this case: Explicit permitted tasks and non-goals support appropriate refusal or handoff, with technical enforcement where needed.

### Question 70 — D

Answer: Abstain or escalate when evidence is insufficient. Acknowledge missing evidence; fluency and low variability do not supply absent facts. Avoids inventing a consequential answer when approved context lacks support. Defined user messaging and review routes improve usefulness. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Acknowledge missing evidence; fluency and low variability do not supply absent facts.
- **B:** Incorrect for this question. Can increase cost or latency without establishing task suitability or meeting governance requirements. In this case: Acknowledge missing evidence; fluency and low variability do not supply absent facts.
- **C:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: Acknowledge missing evidence; fluency and low variability do not supply absent facts.
- **D:** Correct. Avoids inventing a consequential answer when approved context lacks support. Defined user messaging and review routes improve usefulness. In this case: Acknowledge missing evidence; fluency and low variability do not supply absent facts.

### Question 71 — C

Answer: Refresh and govern the retrieval index. Source freshness and index versioning directly address the observed stale evidence. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Rescores an initial result set for relevance. It cannot promote a document that never entered the candidate set. In this case: Source freshness and index versioning directly address the observed stale evidence.
- **B:** Incorrect for this question. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Source freshness and index versioning directly address the observed stale evidence.
- **C:** Correct. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Source freshness and index versioning directly address the observed stale evidence.
- **D:** Incorrect for this question. Addresses defects in the source evidence; greater model capacity does not automatically repair incorrect data. In this case: Source freshness and index versioning directly address the observed stale evidence.

### Question 72 — D

Answer: Retrieval recall. Recall-focused testing measures whether relevant evidence is found at all. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Recall-focused testing measures whether relevant evidence is found at all.
- **B:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Recall-focused testing measures whether relevant evidence is found at all.
- **C:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Recall-focused testing measures whether relevant evidence is found at all.
- **D:** Correct. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Recall-focused testing measures whether relevant evidence is found at all.

### Question 73 — D

Answer: Retrieval precision. Low precision indicates that much of the returned set is irrelevant. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Low precision indicates that much of the returned set is irrelevant.
- **B:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Low precision indicates that much of the returned set is irrelevant.
- **C:** Incorrect for this question. Is one pass over the designated training dataset under the training setup. It is not the number of examples processed in an individual update. In this case: Low precision indicates that much of the returned set is irrelevant.
- **D:** Correct. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Low precision indicates that much of the returned set is irrelevant.

### Question 74 — A

Answer: Evaluate answer groundedness. Compare the generated claim with its evidence rather than only examining retrieval rankings. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Compare the generated claim with its evidence rather than only examining retrieval rankings.
- **B:** Incorrect for this question. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Compare the generated claim with its evidence rather than only examining retrieval rankings.
- **C:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Compare the generated claim with its evidence rather than only examining retrieval rankings.
- **D:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Compare the generated claim with its evidence rather than only examining retrieval rankings.

### Question 75 — C

Answer: Supported structured output plus schema validation. An enforced supported schema and validation target names and required structure. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: An enforced supported schema and validation target names and required structure.
- **B:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: An enforced supported schema and validation target names and required structure.
- **C:** Correct. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: An enforced supported schema and validation target names and required structure.
- **D:** Incorrect for this question. Restricts next-token candidates to a configured number of top-ranked tokens where supported. It does not impose a plain-language vocabulary policy. In this case: An enforced supported schema and validation target names and required structure.

### Question 76 — A

Answer: Specify audience, task, constraints, and output expectations. Specify the audience and terminology expectations rather than change unrelated sampling or compression settings. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. Closest official exam-guide objective 3.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Makes a request actionable without relying on vague demands for better output. It does not replace validation or permissions. In this case: Specify the audience and terminology expectations rather than change unrelated sampling or compression settings.
- **B:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Specify the audience and terminology expectations rather than change unrelated sampling or compression settings.
- **C:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Specify the audience and terminology expectations rather than change unrelated sampling or compression settings.
- **D:** Incorrect for this question. Provides several worked demonstrations of the desired input-output behavior in the prompt. In this case: Specify the audience and terminology expectations rather than change unrelated sampling or compression settings.

### Question 77 — D

Answer: Independent representative evaluation. Representative independent tests must include the actual language requirements of the workflow. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Representative independent tests must include the actual language requirements of the workflow.
- **B:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Representative independent tests must include the actual language requirements of the workflow.
- **C:** Incorrect for this question. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Representative independent tests must include the actual language requirements of the workflow.
- **D:** Correct. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Representative independent tests must include the actual language requirements of the workflow.

### Question 78 — D

Answer: Review, test, and scan generated code before use. Generated code requires security and authorization checks, not merely syntax validation. Treats generated software as an untrusted candidate rather than guaranteed functional or secure output. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Generated code requires security and authorization checks, not merely syntax validation.
- **B:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Generated code requires security and authorization checks, not merely syntax validation.
- **C:** Incorrect for this question. Can reduce supported harmful content but does not guarantee factual accuracy, authorization, or complete risk elimination. In this case: Generated code requires security and authorization checks, not merely syntax validation.
- **D:** Correct. Treats generated software as an untrusted candidate rather than guaranteed functional or secure output. In this case: Generated code requires security and authorization checks, not merely syntax validation.

### Question 79 — D

Answer: Compare cost per verified acceptable outcome. Include retries, review, and acceptance rates in cost per verified outcome. Accounts for success rates, rework, review, and full workflow costs rather than only unit model pricing. Closest official exam-guide objective 4.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Supports capacity and budget planning under changing demand. A token-price reduction need not reduce the total bill if usage grows. In this case: Include retries, review, and acceptance rates in cost per verified outcome.
- **B:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Include retries, review, and acceptance rates in cost per verified outcome.
- **C:** Incorrect for this question. Distinguishes installed seats or trial logins from useful adoption. Usage must be interpreted with quality and risk. In this case: Include retries, review, and acceptance rates in cost per verified outcome.
- **D:** Correct. Accounts for success rates, rework, review, and full workflow costs rather than only unit model pricing. In this case: Include retries, review, and acceptance rates in cost per verified outcome.

### Question 80 — C

Answer: Stage deployment with quality gates and rollback. Use controlled stages, acceptance criteria, monitoring, and a rollback path rather than immediate full exposure. Limits initial exposure and promotes only when defined outcomes remain acceptable. Availability alone does not establish answer quality. Closest official exam-guide objective 4.2: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Makes instruction changes identifiable, comparable, and reversible. A version label is useful only when actual content and dependencies are tracked. In this case: Use controlled stages, acceptance criteria, monitoring, and a rollback path rather than immediate full exposure.
- **B:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Use controlled stages, acceptance criteria, monitoring, and a rollback path rather than immediate full exposure.
- **C:** Correct. Limits initial exposure and promotes only when defined outcomes remain acceptable. Availability alone does not establish answer quality. In this case: Use controlled stages, acceptance criteria, monitoring, and a rollback path rather than immediate full exposure.
- **D:** Incorrect for this question. Probes likely bypasses and harmful interactions before and after release. Passing a finite test suite is not proof that all attacks are prevented. In this case: Use controlled stages, acceptance criteria, monitoring, and a rollback path rather than immediate full exposure.

### Question 81 — C

Answer: Retrieval-augmented generation (RAG). Fresh evidence is the gap, so retrieval is a better first response than behavioral adaptation. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Fresh evidence is the gap, so retrieval is a better first response than behavioral adaptation.
- **B:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Fresh evidence is the gap, so retrieval is a better first response than behavioral adaptation.
- **C:** Correct. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: Fresh evidence is the gap, so retrieval is a better first response than behavioral adaptation.
- **D:** Incorrect for this question. Trains low-rank adaptation parameters in a supported fine-tuning setup while typically freezing base weights. It reduces trainable parameter count but does not guarantee unchanged behavior. In this case: Fresh evidence is the gap, so retrieval is a better first response than behavioral adaptation.

### Question 82 — A

Answer: Supervised fine-tuning. Behavioral adaptation may address recurring style or task-pattern failures after simpler prompt approaches are evaluated. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Behavioral adaptation may address recurring style or task-pattern failures after simpler prompt approaches are evaluated.
- **B:** Incorrect for this question. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: Behavioral adaptation may address recurring style or task-pattern failures after simpler prompt approaches are evaluated.
- **C:** Incorrect for this question. Updates approved evidence, removes or marks obsolete versions, and preserves source authorization. New documents alone do not prove retrieval and generation quality. In this case: Behavioral adaptation may address recurring style or task-pattern failures after simpler prompt approaches are evaluated.
- **D:** Incorrect for this question. Reserves capacity for instructions, evidence, history, and generation according to model-specific limits. Exceeding a limit may cause rejection or configured truncation, not a universal oldest-message deletion rule. In this case: Behavioral adaptation may address recurring style or task-pattern failures after simpler prompt approaches are evaluated.

### Question 83 — B

Answer: Hybrid lexical and vector retrieval. Hybrid retrieval can preserve exact-term matching while retaining semantic matching. Combines exact-term matching with semantic similarity. It is useful for identifiers and paraphrases, subject to relevance and access evaluation. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Uses lower-precision representations to reduce model memory or compute requirements. Quality and runtime compatibility must be measured; savings do not prove hardware fit. In this case: Hybrid retrieval can preserve exact-term matching while retaining semantic matching.
- **B:** Correct. Combines exact-term matching with semantic similarity. It is useful for identifiers and paraphrases, subject to relevance and access evaluation. In this case: Hybrid retrieval can preserve exact-term matching while retaining semantic matching.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Hybrid retrieval can preserve exact-term matching while retaining semantic matching.
- **D:** Incorrect for this question. Chooses a highest-scoring permitted next token at each decoding step. It can still produce false, malformed, or inappropriate output. In this case: Hybrid retrieval can preserve exact-term matching while retaining semantic matching.

### Question 84 — D

Answer: Coherent document chunking. Chunk boundaries need enough coherent context to preserve the meaning of retrieved evidence. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Can increase cost or latency without establishing task suitability or meeting governance requirements. In this case: Chunk boundaries need enough coherent context to preserve the meaning of retrieved evidence.
- **B:** Incorrect for this question. Can amplify errors or irrelevant content and is not a substitute for data validation. In this case: Chunk boundaries need enough coherent context to preserve the meaning of retrieved evidence.
- **C:** Incorrect for this question. Lower values generally make sampling more focused and higher values more varied; neither guarantees factual correctness. In this case: Chunk boundaries need enough coherent context to preserve the meaning of retrieved evidence.
- **D:** Correct. Splits sources into useful retrieval units while preserving sufficient meaning and metadata. Chunk boundaries influence retrieval relevance and answer context. In this case: Chunk boundaries need enough coherent context to preserve the meaning of retrieved evidence.

### Question 85 — B

Answer: Human-in-the-loop review. Qualified review and ownership remain important for consequential externally released content. Uses qualified people to verify, approve, correct, or escalate outputs, especially where consequences are significant. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Qualified review and ownership remain important for consequential externally released content.
- **B:** Correct. Uses qualified people to verify, approve, correct, or escalate outputs, especially where consequences are significant. In this case: Qualified review and ownership remain important for consequential externally released content.
- **C:** Incorrect for this question. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Qualified review and ownership remain important for consequential externally released content.
- **D:** Incorrect for this question. Can reduce supported harmful content but does not guarantee factual accuracy, authorization, or complete risk elimination. In this case: Qualified review and ownership remain important for consequential externally released content.

### Question 86 — B

Answer: Authorize and validate tool calls before execution. Trusted tool authorization and policy enforcement are stronger than relying only on model obedience or delimiters. Checks the caller, action, arguments, and business policy in trusted code. The model proposes a call; it does not itself grant permission. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Specifies a perspective or function to guide response tone and focus; it does not grant expertise or authority. In this case: Trusted tool authorization and policy enforcement are stronger than relying only on model obedience or delimiters.
- **B:** Correct. Checks the caller, action, arguments, and business policy in trusted code. The model proposes a call; it does not itself grant permission. In this case: Trusted tool authorization and policy enforcement are stronger than relying only on model obedience or delimiters.
- **C:** Incorrect for this question. Reduces ambiguity and marks external material as data. Delimiters alone are not a security boundary. In this case: Trusted tool authorization and policy enforcement are stronger than relying only on model obedience or delimiters.
- **D:** Incorrect for this question. Places a qualified decision before the external effect with proper correlation and authorization. Reviewing afterward cannot undo every side effect. In this case: Trusted tool authorization and policy enforcement are stronger than relying only on model obedience or delimiters.

### Question 87 — A

Answer: Collect reviewed user feedback and verified outcomes. Review feedback against evidence and use confirmed issues to improve the system, rather than treating every vote as truth. Turns field issues into improvements without treating popularity as proof of correctness. Closest official exam-guide objective 4.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Review feedback against evidence and use confirmed issues to improve the system, rather than treating every vote as truth.
- **B:** Incorrect for this question. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Review feedback against evidence and use confirmed issues to improve the system, rather than treating every vote as truth.
- **C:** Incorrect for this question. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Review feedback against evidence and use confirmed issues to improve the system, rather than treating every vote as truth.
- **D:** Incorrect for this question. Distinguishes installed seats or trial logins from useful adoption. Usage must be interpreted with quality and risk. In this case: Review feedback against evidence and use confirmed issues to improve the system, rather than treating every vote as truth.

### Question 88 — A

Answer: Verify claims against cited source passages. Source validity and claim support must be checked independently of style compliance. Checks whether a citation actually supports the output. A plausible URL or citation marker is not proof of grounding. Closest official exam-guide objective 3.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Checks whether a citation actually supports the output. A plausible URL or citation marker is not proof of grounding. In this case: Source validity and claim support must be checked independently of style compliance.
- **B:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Source validity and claim support must be checked independently of style compliance.
- **C:** Incorrect for this question. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Source validity and claim support must be checked independently of style compliance.
- **D:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Source validity and claim support must be checked independently of style compliance.

### Question 89 — D

Answer: Extract, validate, and reconcile structured fields. Validate field meaning and source consistency, since a schema alone may allow a wrong value. Combines supported extraction with checks against source evidence and business rules. Valid JSON alone does not establish field accuracy. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Constrains output structure where supported and checks the returned object before use. Correct structure does not imply correct facts or authorized actions. In this case: Validate field meaning and source consistency, since a schema alone may allow a wrong value.
- **B:** Incorrect for this question. Extracts and processes information from supported documents, including structured fields for suitable processors. In this case: Validate field meaning and source consistency, since a schema alone may allow a wrong value.
- **C:** Incorrect for this question. Caps generated output tokens within supported limits; too low a cap can truncate an answer. In this case: Validate field meaning and source consistency, since a schema alone may allow a wrong value.
- **D:** Correct. Combines supported extraction with checks against source evidence and business rules. Valid JSON alone does not establish field accuracy. In this case: Validate field meaning and source consistency, since a schema alone may allow a wrong value.

### Question 90 — C

Answer: Continuously evaluate, version, and monitor the solution. Ongoing monitoring and traceable evaluation can reveal changed retrieval behavior after source-system changes. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Records necessary actions, versions, and approvals for investigation while controlling sensitive telemetry access and retention. In this case: Ongoing monitoring and traceable evaluation can reveal changed retrieval behavior after source-system changes.
- **B:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Ongoing monitoring and traceable evaluation can reveal changed retrieval behavior after source-system changes.
- **C:** Correct. Tracks quality, usage, regressions, security updates, and changing conditions instead of assuming launch completes maintenance. In this case: Ongoing monitoring and traceable evaluation can reveal changed retrieval behavior after source-system changes.
- **D:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Ongoing monitoring and traceable evaluation can reveal changed retrieval behavior after source-system changes.

### Question 91 — A

Answer: Time to first token. Time to first token separates initial processing delay from later token production speed. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Time to first token separates initial processing delay from later token production speed.
- **B:** Incorrect for this question. Uses reference overlap, commonly for summarization assessment. It should be complemented with factual, safety, and human-quality checks. In this case: Time to first token separates initial processing delay from later token production speed.
- **C:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Time to first token separates initial processing delay from later token production speed.
- **D:** Incorrect for this question. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: Time to first token separates initial processing delay from later token production speed.

### Question 92 — B

Answer: Output token generation rate. Output tokens per second measures the streaming phase rather than startup latency. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. Closest official exam-guide objective 3.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Output tokens per second measures the streaming phase rather than startup latency.
- **B:** Correct. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Output tokens per second measures the streaming phase rather than startup latency.
- **C:** Incorrect for this question. Uses reference n-gram overlap, commonly for translation evaluation. Low overlap can reflect wording differences and does not independently establish factual error. In this case: Output tokens per second measures the streaming phase rather than startup latency.
- **D:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Output tokens per second measures the streaming phase rather than startup latency.

### Question 93 — D

Answer: Supported prompt-prefix caching. Prompt-prefix caching targets repeated input processing without serving another user's final answer. Can reuse eligible repeated prefix processing under provider-specific rules. It is not the same as serving a previously generated final answer. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Reuses eligible results only within appropriate identity, freshness, and semantic boundaries. Similar wording alone does not make a cached answer safe. In this case: Prompt-prefix caching targets repeated input processing without serving another user's final answer.
- **B:** Incorrect for this question. Retrieves external evidence, adds it to the request context, and generates an answer without inherently updating model weights. In this case: Prompt-prefix caching targets repeated input processing without serving another user's final answer.
- **C:** Incorrect for this question. Stores and supplies relevant history where needed without implying model-weight updates. Stateful platform features and their retention policies must be reviewed separately. In this case: Prompt-prefix caching targets repeated input processing without serving another user's final answer.
- **D:** Correct. Can reuse eligible repeated prefix processing under provider-specific rules. It is not the same as serving a previously generated final answer. In this case: Prompt-prefix caching targets repeated input processing without serving another user's final answer.

### Question 94 — C

Answer: Governed response caching. Eligible response caching can reuse final results within controlled freshness and identity boundaries. Reuses eligible results only within appropriate identity, freshness, and semantic boundaries. Similar wording alone does not make a cached answer safe. Closest official exam-guide objective 2.5: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Adapts supported models using curated examples of inputs and desired outputs. Independent evaluation is needed to check generalization and regressions. In this case: Eligible response caching can reuse final results within controlled freshness and identity boundaries.
- **B:** Incorrect for this question. Can reuse eligible repeated prefix processing under provider-specific rules. It is not the same as serving a previously generated final answer. In this case: Eligible response caching can reuse final results within controlled freshness and identity boundaries.
- **C:** Correct. Reuses eligible results only within appropriate identity, freshness, and semantic boundaries. Similar wording alone does not make a cached answer safe. In this case: Eligible response caching can reuse final results within controlled freshness and identity boundaries.
- **D:** Incorrect for this question. Learns broad statistical representations from a large corpus before downstream adaptation. The precise objective depends on architecture and modality. In this case: Eligible response caching can reuse final results within controlled freshness and identity boundaries.

### Question 95 — B

Answer: Minimize and protect personal data for the approved purpose. Cross-user reuse could expose private data even when questions have similar wording. Limits unnecessary collection, use, retention, and disclosure according to applicable obligations. Closest official exam-guide objective 4.3: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Replaces direct identifiers with aliases while a linkage or re-identification route may remain; it is not the same as irreversible anonymity. In this case: Cross-user reuse could expose private data even when questions have similar wording.
- **B:** Correct. Limits unnecessary collection, use, retention, and disclosure according to applicable obligations. In this case: Cross-user reuse could expose private data even when questions have similar wording.
- **C:** Incorrect for this question. Reuses eligible results only within appropriate identity, freshness, and semantic boundaries. Similar wording alone does not make a cached answer safe. In this case: Cross-user reuse could expose private data even when questions have similar wording.
- **D:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: Cross-user reuse could expose private data even when questions have similar wording.

### Question 96 — A

Answer: ROUGE. ROUGE measures overlap; valid alternative phrasing can require complementary factual and human-quality checks. Uses reference overlap, commonly for summarization assessment. It should be complemented with factual, safety, and human-quality checks. Closest official exam-guide objective 1.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Uses reference overlap, commonly for summarization assessment. It should be complemented with factual, safety, and human-quality checks. In this case: ROUGE measures overlap; valid alternative phrasing can require complementary factual and human-quality checks.
- **B:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: ROUGE measures overlap; valid alternative phrasing can require complementary factual and human-quality checks.
- **C:** Incorrect for this question. Measures token predictive fit for a language model on a specified dataset. It is not a general guarantee of helpfulness, factuality, or comparability across tokenizers. In this case: ROUGE measures overlap; valid alternative phrasing can require complementary factual and human-quality checks.
- **D:** Incorrect for this question. Measures output production speed under the stated conditions. It is distinct from first-token delay and content correctness. In this case: ROUGE measures overlap; valid alternative phrasing can require complementary factual and human-quality checks.

### Question 97 — A

Answer: BLEU. BLEU's reference-overlap focus can miss acceptable paraphrases, so expert evaluation remains useful. Uses reference n-gram overlap, commonly for translation evaluation. Low overlap can reflect wording differences and does not independently establish factual error. Closest official exam-guide objective 1.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Uses reference n-gram overlap, commonly for translation evaluation. Low overlap can reflect wording differences and does not independently establish factual error. In this case: BLEU's reference-overlap focus can miss acceptable paraphrases, so expert evaluation remains useful.
- **B:** Incorrect for this question. Measures how much of a returned set is relevant. It differs from recall and from whether an answer is faithful to its evidence. In this case: BLEU's reference-overlap focus can miss acceptable paraphrases, so expert evaluation remains useful.
- **C:** Incorrect for this question. Uses reference overlap, commonly for summarization assessment. It should be complemented with factual, safety, and human-quality checks. In this case: BLEU's reference-overlap focus can miss acceptable paraphrases, so expert evaluation remains useful.
- **D:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: BLEU's reference-overlap focus can miss acceptable paraphrases, so expert evaluation remains useful.

### Question 98 — B

Answer: Perplexity on a comparable evaluation setup. Perplexity depends on tokenization and evaluation setup, so unqualified cross-tokenizer comparison can mislead. Measures token predictive fit for a language model on a specified dataset. It is not a general guarantee of helpfulness, factuality, or comparability across tokenizers. Closest official exam-guide objective 1.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Incorrect for this question. Measures how much of the relevant evidence is found under a defined benchmark. It requires a suitable relevance reference set. In this case: Perplexity depends on tokenization and evaluation setup, so unqualified cross-tokenizer comparison can mislead.
- **B:** Correct. Measures token predictive fit for a language model on a specified dataset. It is not a general guarantee of helpfulness, factuality, or comparability across tokenizers. In this case: Perplexity depends on tokenization and evaluation setup, so unqualified cross-tokenizer comparison can mislead.
- **C:** Incorrect for this question. Measures initial response delay before the first token becomes available under the measurement definition. It differs from complete-response latency. In this case: Perplexity depends on tokenization and evaluation setup, so unqualified cross-tokenizer comparison can mislead.
- **D:** Incorrect for this question. Checks whether generated claims are supported by supplied evidence. Relevant retrieval alone does not establish this property. In this case: Perplexity depends on tokenization and evaluation setup, so unqualified cross-tokenizer comparison can mislead.

### Question 99 — A

Answer: Evaluate model fit against business and operational requirements. Measure fit on representative cases rather than assume either smaller or larger is always preferable. Considers modality, quality, context, security, availability, customization, latency, and total cost. Closest official exam-guide objective 1.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Considers modality, quality, context, security, availability, customization, latency, and total cost. In this case: Measure fit on representative cases rather than assume either smaller or larger is always preferable.
- **B:** Incorrect for this question. Helps teams discover and evaluate supported Google, third-party, and open models, subject to model-specific terms and availability. In this case: Measure fit on representative cases rather than assume either smaller or larger is always preferable.
- **C:** Incorrect for this question. Accounts for success rates, rework, review, and full workflow costs rather than only unit model pricing. In this case: Measure fit on representative cases rather than assume either smaller or larger is always preferable.
- **D:** Incorrect for this question. Uses cases not used to design or train the change, including important user groups and failure cases. It supports regression detection rather than merely memorization. In this case: Measure fit on representative cases rather than assume either smaller or larger is always preferable.

### Question 100 — A

Answer: Compare a pilot with an appropriate control or baseline. Compare with an appropriate baseline or control using a suitable and ethical pilot design. Helps separate the effect of the intervention from seasonality and unrelated changes. Experiment design must be ethical and appropriate. Closest official exam-guide objective 4.1: https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf Official study guide: https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf

- **A:** Correct. Helps separate the effect of the intervention from seasonality and unrelated changes. Experiment design must be ethical and appropriate. In this case: Compare with an appropriate baseline or control using a suitable and ethical pilot design.
- **B:** Incorrect for this question. Turns field issues into improvements without treating popularity as proof of correctness. In this case: Compare with an appropriate baseline or control using a suitable and ethical pilot design.
- **C:** Incorrect for this question. Checks a model-based evaluator for agreement, bias, and failure cases instead of treating the judge as ground truth. In this case: Compare with an appropriate baseline or control using a suitable and ethical pilot design.
- **D:** Incorrect for this question. Makes improvement measurable against comparable conditions rather than attributing every later change to AI. In this case: Compare with an appropriate baseline or control using a suitable and ethical pilot design.
