# Sources, coverage, and editorial notes

## Primary sources

The official AIF-C01 guide and its five domain pages were retrieved during authoring on **2026-10-20**. Service-specific reading links in the questions are supplemental references; this package does not claim every supplemental URL was live-checked. AWS services, model support, pricing, and documentation can change.

- Certification: https://aws.amazon.com/certification/certified-ai-practitioner/
- Exam guide: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html
- Domain 1: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html
- Domain 2: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html
- Domain 3: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html
- Domain 4: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html
- Domain 5: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html

## Coverage map

| Official task area | Examples practiced |
|---|---|
| 1.1 AI concepts | Learning paradigms, classification/regression, inference, features, deep learning, time series |
| 1.2 Practical AI use cases | Business value, managed speech/text/document/vision services, suitable prediction tasks |
| 1.3 Lifecycle | Training, data quality, overfitting/underfitting, leakage, labeling, batch inference, evaluation metrics |
| 2.1 GenAI concepts | Foundation models, LLMs, embeddings, tokens, context, multimodal/diffusion, pretraining, MCP, memory, orchestration |
| 2.2 Capabilities and limitations | Generated content, hallucinations, verification, quality/cost tradeoffs, business ROI |
| 2.3 AWS GenAI technologies | Bedrock, Q assistants, JumpStart, on-demand access, Provisioned Throughput |
| 3.1 FM application design | RAG, Knowledge Bases, retrieval, chunking, reranking, vector stores, tools, agents, efficiency |
| 3.2 Prompt engineering | Zero/few-shot, role instructions, decomposition, templates, schema validation, prompt versioning |
| 3.3 Model adaptation | Fine-tuning, continued pretraining, distillation, curated data, held-out evaluation |
| 3.4 FM evaluation | Human review, groundedness, retrieval relevance, ROUGE, BLEU, BERTScore, perplexity, latency |
| 4.1 Responsible systems | Fairness, subgroup analysis, privacy, robustness, inclusion, safety controls, IP rights, sustainability |
| 4.2 Transparency/explainability | Prediction explanations, disclosures, Clarify, Model Cards, feedback and risk-based tradeoffs |
| 5.1 Security | IAM, KMS, PrivateLink, TLS, prompt injection, poisoning, authorization, secret handling, source provenance |
| 5.2 Governance/compliance | CloudTrail, CloudWatch, Macie, Artifact, Config, Inspector, Trusted Advisor, residency, retention |

This is a coverage map, not a claim that every example or current service in the official guide appears in every set. Examples are distributed across the package. In particular, specialized AgentCore features, all vector database choices, and every orchestration pattern are not exhaustively tested. Study the current official objectives as well as these questions.

## Question construction

The source contains 100 shared objective families with six authored prompts each. Thirty set-specific extensions replace selected prompts to broaden coverage without changing per-domain counts or question-type totals. Each delivered set contains 100 questions, with 600 normalized-distinct question texts across the delivered CSVs. Many prompts intentionally test the same distinction in different business contexts; option sets and explanations can repeat.

Single-answer alternatives are shuffled and their correct positions are balanced. Select-two answer positions are deterministically shuffled. Seeds only control ordering, not correctness. The manifest preserves objective IDs and option keys. The answer key is derived from authored correct concepts rather than guessed from shuffled positions.

## Boundaries and publication review

- No actual or recalled AWS exam questions are used.
- No passing, score, employment, or certification guarantee is made.
- The tests use Udemy-supported CSV question types, not native AWS matching/ordering interactions.
- Current availability, pricing, throughput terms, and model support must be reviewed before making implementation decisions. No fixed service price is asserted.
- Filters, RAG, low-temperature sampling, representative data, and private endpoints are not presented as complete guarantees of truth, fairness, compliance, or security.
- Automated checks validate structure and source consistency, not independent factual correctness or instructional quality.
- An instructor should perform a final subject-matter review and preview the actual Udemy import before publication.
