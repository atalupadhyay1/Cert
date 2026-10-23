# CCAO-F sources, coverage, and design notes

Baseline: official Exam Guide v1.0, effective July 2026; reviewed October 21, 2026. The portal announces an Associate – Foundations exam update on December 7, 2026, with an updated guide due November 17, 2026. This package does not claim coverage of the unpublished update. Recheck and revise before using it for that exam version.

## Authoritative scope

- **Certification portal:** [https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification](https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification)
- **Exam guide:** [Claude Certified Associate – Foundations Exam Guide v1.0 (effective July 2026)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf)
- **Program certification page:** [Anthropic Partner Academy — certifications](https://anthropic-partners.skilljar.com/page/partner-certifications)
- **Certification FAQ:** [Anthropic Partner Academy — certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications)
- **Prep-course outline (audience and topic confirmation only):** [Claude Certified Associate – Foundations path](https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations)

Supporting product-behavior references used for scenario design:

- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) — project knowledge, instructions, RAG scaling on paid plans, sharing permissions; also notes a staged rollout of a newer Projects version.
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) — availability varies by plan, templates, editing and sharing behavior.
- [Claude prompting documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

These references inform concepts only. The exam guide controls the tested blueprint; product pages describe evolving behavior and do not override organizational policy.

## Exam facts used

| Item | Value |
|---|---|
| Exam code | CCAO-F |
| Credential | Claude Certified Associate – Foundations |
| Blueprint version | v1.0, effective July 2026 |
| Items | 60 |
| Format | Multiple-choice and multiple-response; each multiple-response item states how many responses to select |
| Time | 120 minutes |
| Delivery | Proctored, online and/or test center per program policy |
| Passing score | 720 on a 100–1,000 scaled range |
| Fee | $99 USD list price |
| Validity | 12 months |
| Prerequisites | None mandatory; regular hands-on professional Claude use recommended |
| Audience | Business and knowledge-work practitioners, not API or agent developers |

**Scoring meaning.** The cut score is not a raw percentage. A 720 scaled score must not be described as 72% correct, and the 80% practice target in this package is a custom study convention, not an official pass threshold.

## Official domains and weights

| # | Domain | Weight |
|---|---|---:|
| 1 | Prompting and Task Execution | 14% |
| 2 | Output Evaluation and Validation | 21% |
| 3 | Product and Model Selection | 12% |
| 4 | Workflow Integration and Solution Design | 16% |
| 5 | Configuration and Knowledge Management | 12% |
| 6 | Governance, Risk, and Responsible Use | 15% |
| 7 | Troubleshooting and Optimization | 10% |

Total: 100%.

## Package allocation

| Test | Topic | Domain allocation |
|---|---|---|
| 1 | Prompting and Task Execution | Domain 1: 100 |
| 2 | Output Evaluation and Validation | Domain 2: 100 |
| 3 | Product, Model, and Configuration Decisions | Domain 3: 50, Domain 5: 50 |
| 4 | Workflow Integration and Solution Design | Domain 4: 100 |
| 5 | Governance, Risk, and Troubleshooting | Domain 6: 60, Domain 7: 40 |
| 6 | Integrated Associate Scenarios and Final Review | Domain 1: 14, Domain 2: 21, Domain 3: 12, Domain 4: 16, Domain 5: 12, Domain 6: 15, Domain 7: 10 |

Test 6 uses an integer approximation of the official weights: 14/21/12/16/12/15/10. Tests 1–5 are focused learning sets and intentionally do not imitate exam proportions.

## Coverage by domain

| # | Domain | Weight | Tests 1–5 | Test 6 | Package |
|---|---|---:|---:|---:|---:|
| 1 | Prompting and Task Execution | 14% | 100 | 14 | 114 |
| 2 | Output Evaluation and Validation | 21% | 100 | 21 | 121 |
| 3 | Product and Model Selection | 12% | 50 | 12 | 62 |
| 4 | Workflow Integration and Solution Design | 16% | 100 | 16 | 116 |
| 5 | Configuration and Knowledge Management | 12% | 50 | 12 | 62 |
| 6 | Governance, Risk, and Responsible Use | 15% | 60 | 15 | 75 |
| 7 | Troubleshooting and Optimization | 10% | 40 | 10 | 50 |

## Local study-map skills

The guide states objectives as named bullet tasks rather than numbered skills. The IDs below are **local study-map IDs**, created to make coverage and exports auditable. They are not official numbers.

| Local ID | Official domain and local study area | Questions |
|---|---|---:|
| 1.1 | Prompting and Task Execution — Prompt Construction | 30 |
| 1.2 | Prompting and Task Execution — Task Decomposition | 28 |
| 1.3 | Prompting and Task Execution — Prompt Iteration | 28 |
| 1.4 | Prompting and Task Execution — Task-Type Strategy | 28 |
| 2.1 | Output Evaluation and Validation — Accuracy and Completeness | 23 |
| 2.2 | Output Evaluation and Validation — Hallucinations, Inconsistency, and Bias | 23 |
| 2.3 | Output Evaluation and Validation — Fact-Checking and Validation | 18 |
| 2.4 | Output Evaluation and Validation — Human Review Decisions | 19 |
| 2.5 | Output Evaluation and Validation — Audience Adaptation and Comparison | 19 |
| 2.6 | Output Evaluation and Validation — Information Organization and Output Formats | 19 |
| 3.1 | Product and Model Selection — Product Feature Selection | 16 |
| 3.2 | Product and Model Selection — Model Family Differentiation | 16 |
| 3.3 | Product and Model Selection — Quality, Speed, and Cost Alignment | 15 |
| 3.4 | Product and Model Selection — Context and Memory Management | 15 |
| 4.1 | Workflow Integration and Solution Design — Requirements and Use-Case Analysis | 23 |
| 4.2 | Workflow Integration and Solution Design — Research, Planning, and Process Optimization | 23 |
| 4.3 | Workflow Integration and Solution Design — Solution Design and Iteration | 23 |
| 4.4 | Workflow Integration and Solution Design — Workflow Integration and Redesign | 23 |
| 4.5 | Workflow Integration and Solution Design — Communicating Value and Limitations | 24 |
| 5.1 | Configuration and Knowledge Management — Project Instructions | 16 |
| 5.2 | Configuration and Knowledge Management — Knowledge Sources and Connectors | 16 |
| 5.3 | Configuration and Knowledge Management — System-Level Instructions | 15 |
| 5.4 | Configuration and Knowledge Management — Configuration Maintenance | 15 |
| 6.1 | Governance, Risk, and Responsible Use — Appropriate and Inappropriate Use Cases | 16 |
| 6.2 | Governance, Risk, and Responsible Use — Data Sensitivity, Regulatory, and Privacy | 16 |
| 6.3 | Governance, Risk, and Responsible Use — Organizational AI Policy and Governance | 16 |
| 6.4 | Governance, Risk, and Responsible Use — Ethical Implications | 16 |
| 6.5 | Governance, Risk, and Responsible Use — Escalation and Unsafe Requests | 11 |
| 7.1 | Troubleshooting and Optimization — Diagnosing Underperforming Prompts and Outputs | 18 |
| 7.2 | Troubleshooting and Optimization — Adjusting Approach from Feedback | 13 |
| 7.3 | Troubleshooting and Optimization — Limited or Conflicting Information | 9 |
| 7.4 | Troubleshooting and Optimization — Workflow Efficiency and Effectiveness | 10 |

All 32 local study areas have practice. This does not establish equal depth per bullet, independent factual certification, or calibrated difficulty.

## How the six tests were designed

- **Test 1 — Prompting and Task Execution:** all 100 items cover Domain 1, splitting across brief construction, decomposition, iteration, and task-type strategy.
- **Test 2 — Output Evaluation and Validation:** all 100 items cover Domain 2, the largest official domain at 21%.
- **Test 3 — Product, Model, and Configuration Decisions:** 50 items on Domain 3 and 50 on Domain 5. These are related practitioner decisions about choosing features and maintaining configured context.
- **Test 4 — Workflow Integration and Solution Design:** all 100 items cover Domain 4, including requirements, research, design, integration, and stakeholder communication.
- **Test 5 — Governance, Risk, and Troubleshooting:** 60 items on Domain 6 and 40 on Domain 7. Governance receives the larger share because it carries 15% of the blueprint versus 10% for troubleshooting.
- **Test 6 — Integrated review:** 14/21/12/16/12/15/10 across Domains 1–7.

### Why the aggregate is not blueprint-shaped

Five focused tests deliberately concentrate on their assigned areas, so the package total is not a 600-item proportional sample. Domain totals are 114 / 121 / 62 / 116 / 62 / 75 / 50. This is disclosed on the landing page, README, and each test's README. Only the integrated test approximates official weights.

## Item format and deliberate differences

- Every authored item has exactly four options and one best answer.
- Every option has an explanation; every overall explanation contains a case rationale and the official guide anchor.
- The actual exam includes multiple-response items and 60 items in 120 minutes. This package does not simulate that assembly, selection-count behavior, or proctoring.
- Suggested practice duration is 200 minutes per expanded 100-question test; the optional 80% target is a study convention.
- Correct-answer positions are deterministically shuffled to 25 per slot in each test. Slot balance is an export property, not difficulty calibration.

## Version and product-availability boundary

- The July 2026 guide is the baseline. The portal states that the Associate – Foundations exam will include updated content starting **December 7, 2026**, with updated guides available **November 17, 2026**. No claim is made about unpublished future scope.
- Product features vary by plan, rollout stage, administrator settings, and surface. Questions therefore test stable judgment (verify availability, permissions, scope, and actual support) rather than assert one universal menu path.
- Projects documentation currently describes both the established version and a staged new Projects beta. The bank avoids claiming that every account has the same project model, sharing controls, or memory behavior.
- Artifacts availability and template support differ by plan; the bank treats artifacts as a supported reusable-output option to verify, not as a universal guarantee.
- Model families (Haiku, Sonnet, Opus) are discussed as positioning candidates. No fixed pricing, release identifier, context size, or "always best" claim is made.
- Connector availability, retention, and data terms depend on the actual service, plan, contract, and configuration. The bank requires verification rather than repeating blanket assurances.

## Responsible-use design choices

- Prompts, retrieved documents, and model output are treated as untrusted inputs.
- Authorization, approvals, and policy are enforced in accountable human/process controls, not by asking the model to behave.
- Human review is tied to consequence and uncertainty, not added as a cosmetic disclaimer after a decision.
- Privacy scenarios distinguish de-identification from guaranteed anonymity and require purpose limitation and effective permissions.
- Escalation scenarios route implementation and enterprise architecture to Developer/Architect roles; the Associate scope is practical use, workflow judgment, and governance.
- Numerical examples are explicitly hypothetical or stated in the case; they are not live prices or service-level promises.

## Known limitations

- Structural validation is automated; independent factual, legal, privacy, or accessibility review is not performed.
- No psychometric calibration, difficulty equating, or scaled-score prediction.
- No exhaustive semantic-duplicate detection; related concepts and option definitions deliberately recur.
- No live Udemy import, account preview, or publication is claimed.
- No continuous link or product-interface verification.
- Not endorsed by Anthropic or Udemy; marks belong to their owners.

## Refresh triggers

Update and revalidate this package when:

1. The November 17, 2026 guide or any later guide is published.
2. Exam format, item count, time, fee, validity, or scoring changes.
3. Projects, artifacts, memory, connectors, model families, plan capabilities, or sharing controls change materially.
4. Organizational policy expectations or privacy law affecting the scenarios change.
5. A reviewer finds an ambiguous item, unsupported factual claim, or duplicated concept that weakens the bank.
