# Sources, coverage, and editorial notes

## Primary sources retrieved October 21, 2026

1. [Official certification page](https://cloud.google.com/learn/certification/generative-ai-leader): describes a business-level audience with or without hands-on technical experience, lists 50–60 multiple-choice questions and 90 minutes, and notes recent branding updates.
2. [Official exam guide PDF](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf): provides the four section weights, objectives, and current exam product names.
3. [Official study guide PDF](https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf): supplies conceptual definitions and offering comparisons. Selected portions were retrieved during authoring; not every linked product page was independently verified.
4. [Learning path](https://www.cloudskillsboost.google/paths/1951): linked by the certification page; not independently retrieved in full.

No official sample-question set was copied or used as the question bank. Guide links are scope and study references, not a claim that Google wrote or endorsed these questions or that each link proves every recommended design choice line by line.

## Coverage by guide objective

| Objective | Examples practiced |
|---|---|
| 1.1 Core concepts and use cases | AI/ML/gen AI, learning approaches, lifecycle, foundation models, language/multimodal/diffusion models, model fit, suitable business tasks |
| 1.2 Data and business implications | Structured/unstructured and labeled/unlabeled distinctions, quality, usable authorized access |
| 1.3 Landscape layers | Infrastructure, platform, agent, application; model layer represented through foundation-model concepts |
| 1.4 Google model families | Gemini, Gemma, Imagen, Veo |
| 2.1 Google Cloud strengths | TPU/GPU infrastructure, managed capacity, open model choice, enterprise controls, prebuilt/low-code enablement |
| 2.2 AI-powered work | Gemini app/Gems, Gemini for Workspace, Gemini Enterprise, notebook-style source-grounded work |
| 2.3 Customer experience | Agent Search, public search evidence, Conversational Agents, Agent Assist, Conversational Insights, CCaaS |
| 2.4 Development | Model Garden, AutoML, custom agents, RAG APIs |
| 2.5 Tooling | Agent Studio versus Google AI Studio, storage, runtime/functions, AI APIs, authoritative database lookup, external tool execution |
| 3.1 Limitations and mitigation | Hallucinations, cutoff, adaptation, human review, prompt tuning, monitoring and versioning |
| 3.2 Prompting | Zero/one/few-shot, role prompting, chaining, structured intermediate-step guidance, ReAct |
| 3.3 Grounding and settings | RAG, first-party/third-party/world evidence, temperature, top-p, output length |
| 4.1 Business implementation | Prioritization, pilots, total cost/benefit, outcomes, adoption, stakeholder alignment |
| 4.2 Secure AI | SAIF, IAM, Security Command Center, lifecycle security |
| 4.3 Responsible AI | Transparency, privacy, pseudonymization, subgroup fairness, accountability and review |

This is a map of coverage, not a claim that every example, feature, SKU, lifecycle tool, or SDK is exhaustively assessed in each set. Fine-grained offerings such as Feature Store and specific enterprise notebook APIs are not implementation-tested here. Some concepts appear as alternatives and explanatory contrasts rather than as a dedicated correct answer.

## Branding and availability

The retrieved exam guide uses Gemini Enterprise Agent Platform, Agent Search, Agent Platform AutoML, and Agent Studio. The study material also uses differing customer-experience names. This bank primarily follows the exam-guide wording and describes the underlying purpose without asserting universal account or region availability. Cloud Functions and Cloud Run functions naming is noted explicitly.

No fixed service prices, free-tier promises, paid-plan inclusions, or universal data-handling guarantees are made. Financial cases use explicitly illustrative figures, not Google pricing. Assess actual service terms, permissions, models, and account configuration before implementation.

## Construction and repetition

The source contains 100 shared objective families with six authored prompts each. Twenty-four set-specific business cases replace selected prompts, leaving **600 delivered questions**, not 624. The exports contain 600 normalized-distinct question texts, but intentionally repeat concepts, options, and explanations across sets. They are not six statistically independent tests or 600 unrelated topics.

All questions have one best answer out of four options. Correct answer concepts are authored before deterministic shuffling. Each displayed position is correct 25 times per set. The answer manifest preserves the link from displayed choices to authored concepts and guide objectives.

## Exam resemblance boundaries

The questions use business needs, constraints, product selection, and technique comparisons consistent with the guide's level and scope. They are not copied or recalled exam items. Exact real-exam difficulty, wording, answer-option construction, coverage, or performance prediction is not established.

The official test has 50–60 questions in 90 minutes according to the retrieved page; the 100-question sets and 160-minute suggestion are expanded study settings. The 80% practice target is not an official passing score.

## Review still required

Automated checks establish counts, formatting, source/key consistency, arithmetic regressions, and normalized wording uniqueness. They do not independently certify factual accuracy, remove all semantic repetition, calibrate difficulty, or confirm Udemy account imports. An instructor should review all questions, open source links, and preview all six imported sets before publication.
