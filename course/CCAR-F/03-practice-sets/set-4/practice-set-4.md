# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 4

Prompt Engineering & Structured Output

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A review prompt says only 'be conservative' and produces many harmless style findings. What should replace vague caution?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Define severity using impact and concrete examples
- D. Temporarily disable a noisy category while repairing and evaluating it

### 2. Reviewers label the same issue critical or minor unpredictably. What rubric should the prompt provide?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. State explicit reportable and non-reportable criteria
- C. Calibrate field-confidence thresholds against labeled examples
- D. Define severity using impact and concrete examples

### 3. One noisy finding category destroys trust while other categories remain useful. What temporary control may help during repair?

Domain: Prompt Engineering & Structured Output

- A. State explicit reportable and non-reportable criteria
- B. Temporarily disable a noisy category while repairing and evaluating it
- C. Include valid examples that should not be flagged
- D. Record detected_pattern and dismissal reasons

### 4. A bot flags every outdated comment, including harmless wording changes. What should its review rule state?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. Define severity using impact and concrete examples
- C. Use representative few-shot examples with boundaries
- D. State explicit reportable and non-reportable criteria

### 5. A prompt repeatedly flags a valid local exception that the team intentionally permits. What demonstration should be added?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. State explicit reportable and non-reportable criteria
- C. Use representative few-shot examples with boundaries
- D. Record detected_pattern and dismissal reasons

### 6. Developers dismiss many findings, but the team cannot identify which code constructs trigger them. What diagnostic field helps?

Domain: Prompt Engineering & Structured Output

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. Record detected_pattern and dismissal reasons
- C. State explicit reportable and non-reportable criteria
- D. Define severity using impact and concrete examples

### 7. A prompt asks for only 'high-confidence' findings without defining what counts as a defect. What improvement is most direct?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. State explicit reportable and non-reportable criteria
- C. Define severity using impact and concrete examples
- D. Use representative few-shot examples with boundaries

### 8. A highly certain cosmetic observation receives the highest severity. What distinction should the rubric enforce?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. Record detected_pattern and dismissal reasons
- C. State explicit reportable and non-reportable criteria
- D. Define severity using impact and concrete examples

### 9. A team wants security defects reported but not formatting preferences. What instruction structure is appropriate?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. State explicit reportable and non-reportable criteria
- C. Use representative few-shot examples with boundaries
- D. Temporarily disable a noisy category while repairing and evaluating it

### 10. A flaky style-warning category is being revised and tested while genuine bug detection must continue. What scoped rollout choice fits?

Domain: Prompt Engineering & Structured Output

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. Record detected_pattern and dismissal reasons
- C. Include valid examples that should not be flagged
- D. State explicit reportable and non-reportable criteria

### 11. A review output must consistently include location, issue, severity, and suggested fix. What prompt addition can demonstrate that pattern?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Provide concrete input–output examples
- C. Include valid examples that should not be flagged
- D. State explicit reportable and non-reportable criteria

### 12. Examples show only bugs, so Claude flags valid similar patterns as well. What should the demonstration set include?

Domain: Prompt Engineering & Structured Output

- A. State explicit reportable and non-reportable criteria
- B. Define severity using impact and concrete examples
- C. Use representative few-shot examples with boundaries
- D. Include valid examples that should not be flagged

### 13. Extraction works on tables but fails on narrative descriptions containing equivalent facts. What prompt enrichment is useful?

Domain: Prompt Engineering & Structured Output

- A. State explicit reportable and non-reportable criteria
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use representative few-shot examples with boundaries
- D. Allow explicit unknown or absent values in the schema

### 14. A model inconsistently chooses between two valid task tools for ambiguous requests. What instructional evidence can teach the intended distinction?

Domain: Prompt Engineering & Structured Output

- A. Use tool_choice with type any
- B. Use representative few-shot examples with boundaries
- C. Use tool_choice with type auto
- D. Force the required named tool for that turn

### 15. A requirement describes units informally, and the model normalizes them inconsistently. What would clarify expected transformations?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Provide concrete input–output examples

### 16. A model extracts references only from bibliographies and misses inline citations. What should the examples cover?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Include valid examples that should not be flagged
- D. Allow explicit unknown or absent values in the schema

### 17. A reviewer mistakes an approved test double for a production security defect. What demonstration is most targeted?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. State explicit reportable and non-reportable criteria
- C. Define severity using impact and concrete examples
- D. Include valid examples that should not be flagged

### 18. A prompt describes actionable findings clearly, but output remains inconsistent in shape. What small addition should be tested?

Domain: Prompt Engineering & Structured Output

- A. Validate extracted values against evidence and business rules
- B. Use representative few-shot examples with boundaries
- C. Specify deterministic normalization rules and preserve originals when needed
- D. State explicit reportable and non-reportable criteria

### 19. A team uses one perfect example and sees failures on edge cases. What should a stronger demonstration set represent?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Provide concrete input–output examples
- C. State explicit reportable and non-reportable criteria
- D. Include valid examples that should not be flagged

### 20. The assistant learned to flag every use of a named API even when it is safely configured. What example type can repair that distinction?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. State explicit reportable and non-reportable criteria
- C. Include valid examples that should not be flagged
- D. Temporarily disable a noisy category while repairing and evaluating it

### 21. A downstream parser requires a supported schema-constrained response. What mechanism most directly targets structural compliance?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use supported strict structured output with a schema
- D. State explicit reportable and non-reportable criteria

### 22. An extraction is valid JSON with correct field types, but its customer ID is from another page. What validation is missing?

Domain: Prompt Engineering & Structured Output

- A. Validate extracted values against evidence and business rules
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 23. Some source documents never state a delivery date. What schema design avoids forcing an invented date?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Use supported strict structured output with a schema
- D. Allow explicit unknown or absent values in the schema

### 24. A valid category exists outside the initial enum, and the system must retain its description. What schema pattern fits?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Use supported strict structured output with a schema
- D. Allow explicit unknown or absent values in the schema

### 25. Every result must use the named extract_contract tool rather than another available tool. What selection mode fits?

Domain: Prompt Engineering & Structured Output

- A. Use supported strict structured output with a schema
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Use tool_choice with type auto

### 26. Document type is unknown, several extraction schema tools are valid, and ordinary prose is not allowed. What selection mode fits?

Domain: Prompt Engineering & Structured Output

- A. Use tool_choice with type auto
- B. Give each specialist only task-relevant tools
- C. Force the required named tool for that turn
- D. Use tool_choice with type any

### 27. A caller permits direct text or a tool response depending on the request. Which mode allows that discretion?

Domain: Prompt Engineering & Structured Output

- A. Use tool_choice with type any
- B. Use supported strict structured output with a schema
- C. Force the required named tool for that turn
- D. Use tool_choice with type auto

### 28. A schema allows a date string, but sources mix day-first and month-first notation. What additional instruction is needed?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 29. The extracted line items do not add up to the extracted total, although every field satisfies its schema. What check is needed?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Validate extracted values against evidence and business rules
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 30. A key is required to exist, but the source may omit its value. What schema distinction matters?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use an extensible category plus a detail field
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 31. The source clearly states a new document type not listed in the enum. Which representation preserves that fact?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Allow explicit unknown or absent values in the schema
- C. Use an extensible category plus a detail field
- D. Use supported strict structured output with a schema

### 32. The document is too ambiguous to identify a category confidently. Which design principle should represent that uncertainty?

Domain: Prompt Engineering & Structured Output

- A. Use supported strict structured output with a schema
- B. Use an extensible category plus a detail field
- C. Allow explicit unknown or absent values in the schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 33. A tool is called correctly but its arguments are not constrained by the integration's schema mechanism. What should be assessed?

Domain: Prompt Engineering & Structured Output

- A. Use tool_choice with type any
- B. Force the required named tool for that turn
- C. Use supported strict structured output with a schema
- D. Use tool_choice with type auto

### 34. A result contains a real product code, but not one authorized for the current account. What must be checked?

Domain: Prompt Engineering & Structured Output

- A. Use supported strict structured output with a schema
- B. Allow explicit unknown or absent values in the schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Validate extracted values against evidence and business rules

### 35. A source gives kilograms while the downstream field expects grams. What transformation requirement should be explicit?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Validate extracted values against evidence and business rules

### 36. A form does not contain a phone number, but a non-nullable field demands one. What schema change addresses the incentive to fabricate?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use an extensible category plus a detail field

### 37. A schema-constrained response is cut short by an output limit. What guarantee must not be assumed from using structured output?

Domain: Prompt Engineering & Structured Output

- A. Force the required named tool for that turn
- B. Structural constraints do not guarantee complete or factual output
- C. Validate extracted values against evidence and business rules
- D. Use tool_choice with type any

### 38. An identifier has the correct format but belongs to the wrong source document. Which validation dimension catches that?

Domain: Prompt Engineering & Structured Output

- A. Use supported strict structured output with a schema
- B. Use an extensible category plus a detail field
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Validate extracted values against evidence and business rules

### 39. There is one required extraction tool plus unrelated optional tools. The first step must use the required tool. What mode is appropriate?

Domain: Prompt Engineering & Structured Output

- A. Use tool_choice with type auto
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Use supported strict structured output with a schema

### 40. A JSON object is schema-compliant, but its currency differs from the source invoice. What additional check is required?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Validate extracted values against evidence and business rules
- D. Specify deterministic normalization rules and preserve originals when needed

### 41. The source clearly contains a value, but extraction placed it in the wrong field. What retry input is most useful?

Domain: Prompt Engineering & Structured Output

- A. Retry with the document, failed result, and specific validation errors
- B. Validate extracted values against evidence and business rules
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 42. Repeated retries fail because the requested fact exists only in an unavailable attachment. What should happen instead?

Domain: Prompt Engineering & Structured Output

- A. Validate extracted values against evidence and business rules
- B. Retry with the document, failed result, and specific validation errors
- C. Allow explicit unknown or absent values in the schema
- D. Mark missing evidence and route for retrieval or review

### 43. An invoice states one total while the listed line items imply another. What extraction design helps expose the inconsistency?

Domain: Prompt Engineering & Structured Output

- A. Validate extracted values against evidence and business rules
- B. Compare independently calculated and source-stated totals
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 44. Two pages give different values for the same field and neither is clearly authoritative. What should the output preserve?

Domain: Prompt Engineering & Structured Output

- A. Preserve conflicting source values with an explicit flag
- B. Use supported strict structured output with a schema
- C. Validate extracted values against evidence and business rules
- D. Compare independently calculated and source-stated totals

### 45. Review findings are often dismissed, but only the final score is stored. What metadata would enable targeted improvement?

Domain: Prompt Engineering & Structured Output

- A. Define severity using impact and concrete examples
- B. Record detected_pattern and dismissal reasons
- C. Temporarily disable a noisy category while repairing and evaluating it
- D. State explicit reportable and non-reportable criteria

### 46. A retry prompt says only 'try harder' after a precise unit error was detected. What should replace it?

Domain: Prompt Engineering & Structured Output

- A. Retry with the document, failed result, and specific validation errors
- B. Use supported strict structured output with a schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Mark missing evidence and route for retrieval or review

### 47. A document never states the required legal entity, but the model keeps guessing plausible names. What handling is appropriate?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Use supported strict structured output with a schema
- C. Mark missing evidence and route for retrieval or review
- D. Retry with the document, failed result, and specific validation errors

### 48. A corrected extraction now parses but still uses a value from the wrong column. What must the loop do before acceptance?

Domain: Prompt Engineering & Structured Output

- A. Validate extracted values against evidence and business rules
- B. Use supported strict structured output with a schema
- C. Allow explicit unknown or absent values in the schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 49. A source contradicts itself, and the pipeline overwrites the first value with the second without explanation. What output control is needed?

Domain: Prompt Engineering & Structured Output

- A. Compare independently calculated and source-stated totals
- B. Validate extracted values against evidence and business rules
- C. Record detected_pattern and dismissal reasons
- D. Preserve conflicting source values with an explicit flag

### 50. A field is present but formatted inconsistently with the requested normalized representation. Which corrective approach is reasonable?

Domain: Prompt Engineering & Structured Output

- A. Retry with the document, failed result, and specific validation errors
- B. Use representative few-shot examples with boundaries
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 51. A validation loop keeps making calls after the same correction fails repeatedly. What safeguard should be added?

Domain: Prompt Engineering & Structured Output

- A. Mark missing evidence and route for retrieval or review
- B. Retry with the document, failed result, and specific validation errors
- C. Enforce task, iteration, and spending safeguards
- D. Use supported strict structured output with a schema

### 52. A team wants to know which constructs trigger spurious null-pointer warnings. What structured finding field helps?

Domain: Prompt Engineering & Structured Output

- A. State explicit reportable and non-reportable criteria
- B. Temporarily disable a noisy category while repairing and evaluating it
- C. Record detected_pattern and dismissal reasons
- D. Use representative few-shot examples with boundaries

### 53. A pipeline overwrites the document's total with its recalculated total, hiding disagreement. What design is better?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use supported strict structured output with a schema
- C. Compare independently calculated and source-stated totals
- D. Validate extracted values against evidence and business rules

### 54. A source contains two incompatible dates for the same event. Which output behavior supports safe downstream handling?

Domain: Prompt Engineering & Structured Output

- A. Preserve conflicting source values with an explicit flag
- B. Use an extensible category plus a detail field
- C. Allow explicit unknown or absent values in the schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 55. The original document was omitted from a self-correction request. What evidence should be restored?

Domain: Prompt Engineering & Structured Output

- A. Retry with the document, failed result, and specific validation errors
- B. Use representative few-shot examples with boundaries
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 56. A reviewer confirms the source simply lacks the requested figure. What should terminate repeated model correction attempts?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Mark missing evidence and route for retrieval or review
- C. Retry with the document, failed result, and specific validation errors
- D. Validate extracted values against evidence and business rules

### 57. A revised response passes every type check but changes a verified identifier. What acceptance check is essential?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Validate extracted values against evidence and business rules
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 58. A systematic extraction problem is discovered before a large asynchronous run. What should the team do first?

Domain: Prompt Engineering & Structured Output

- A. Correlate batch outcomes by custom_id
- B. Tune and validate on a representative sample before large submission
- C. Use Message Batches for latency-tolerant independent requests
- D. Resubmit only failed items after diagnosing their errors

### 59. A prompt improvement effort needs evidence about why developers rejected findings. What should be captured?

Domain: Prompt Engineering & Structured Output

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. Define severity using impact and concrete examples
- C. Record detected_pattern and dismissal reasons
- D. State explicit reportable and non-reportable criteria

### 60. An extraction must represent a known disagreement rather than merely an unknown field. Which design principle fits?

Domain: Prompt Engineering & Structured Output

- A. Use an extensible category plus a detail field
- B. Allow explicit unknown or absent values in the schema
- C. Compare independently calculated and source-stated totals
- D. Preserve conflicting source values with an explicit flag

### 61. A nightly audit can wait for asynchronous completion and contains independent requests. Which API approach fits?

Domain: Prompt Engineering & Structured Output

- A. Use synchronous requests for blocking latency-sensitive work
- B. Use Message Batches for latency-tolerant independent requests
- C. Tune and validate on a representative sample before large submission
- D. Orchestrate client-tool follow-up outside a single batch request

### 62. A pre-merge check must respond within the interactive blocking workflow. Which approach is preferable to asynchronous batches?

Domain: Prompt Engineering & Structured Output

- A. Tune and validate on a representative sample before large submission
- B. Resubmit only failed items after diagnosing their errors
- C. Use Message Batches for latency-tolerant independent requests
- D. Use synchronous requests for blocking latency-sensitive work

### 63. Batch outcomes arrive in a different order from submitted documents. How should results be matched?

Domain: Prompt Engineering & Structured Output

- A. Use Message Batches for latency-tolerant independent requests
- B. Correlate batch outcomes by custom_id
- C. Tune and validate on a representative sample before large submission
- D. Resubmit only failed items after diagnosing their errors

### 64. A batch finishes with most documents successful and a few oversized failures. What should be resubmitted?

Domain: Prompt Engineering & Structured Output

- A. Use Message Batches for latency-tolerant independent requests
- B. Tune and validate on a representative sample before large submission
- C. Correlate batch outcomes by custom_id
- D. Resubmit only failed items after diagnosing their errors

### 65. A team plans to process a huge dataset with an untested extraction prompt. What should happen before full submission?

Domain: Prompt Engineering & Structured Output

- A. Resubmit only failed items after diagnosing their errors
- B. Use Message Batches for latency-tolerant independent requests
- C. Tune and validate on a representative sample before large submission
- D. Correlate batch outcomes by custom_id

### 66. A batch item requests a client tool and expects the API to execute it and continue interactively inside that same item. What must the application handle?

Domain: Prompt Engineering & Structured Output

- A. Orchestrate client-tool follow-up outside a single batch request
- B. Correlate batch outcomes by custom_id
- C. Use synchronous requests for blocking latency-sensitive work
- D. Use Message Batches for latency-tolerant independent requests

### 67. A weekly reporting task does not block users and prioritizes processing efficiency over immediate response. Which path should be evaluated?

Domain: Prompt Engineering & Structured Output

- A. Resubmit only failed items after diagnosing their errors
- B. Tune and validate on a representative sample before large submission
- C. Use Message Batches for latency-tolerant independent requests
- D. Use synchronous requests for blocking latency-sensitive work

### 68. An agent's next action depends on a live tool result during an ongoing customer interaction. Which request path is more appropriate?

Domain: Prompt Engineering & Structured Output

- A. Use synchronous requests for blocking latency-sensitive work
- B. Use Message Batches for latency-tolerant independent requests
- C. Orchestrate client-tool follow-up outside a single batch request
- D. Tune and validate on a representative sample before large submission

### 69. An asynchronous extraction job needs to trace each returned record to the correct source file. What identifier design matters?

Domain: Prompt Engineering & Structured Output

- A. Resubmit only failed items after diagnosing their errors
- B. Tune and validate on a representative sample before large submission
- C. Correlate batch outcomes by custom_id
- D. Record detected_pattern and dismissal reasons

### 70. A team resubmits an entire batch after one transient item error, repeating successful downstream work. What strategy is better?

Domain: Prompt Engineering & Structured Output

- A. Use Message Batches for latency-tolerant independent requests
- B. Resubmit only failed items after diagnosing their errors
- C. Correlate batch outcomes by custom_id
- D. Tune and validate on a representative sample before large submission

### 71. A model repeatedly approves a flawed design because it remembers defending it earlier. What review setup may reduce that anchoring?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Calibrate field-confidence thresholds against labeled examples
- C. State explicit reportable and non-reportable criteria
- D. Use an independent reviewer without the generator rationale

### 72. A large code review misses local bugs when every file is supplied at once. What review decomposition should be evaluated?

Domain: Prompt Engineering & Structured Output

- A. Run independent branches concurrently and join checked results
- B. Wait for validated prerequisite outputs
- C. Use an independent reviewer without the generator rationale
- D. Separate local analysis from cross-file integration review

### 73. Separate file reviewers miss an incompatible interface change between two modules. What additional pass is needed?

Domain: Prompt Engineering & Structured Output

- A. Separate local analysis from cross-file integration review
- B. Add a cross-file or cross-component integration pass
- C. Run independent branches concurrently and join checked results
- D. Assign distinct scopes and explicit coverage responsibilities

### 74. A second reviewer should be independent of the generator's reasoning but still judge correctness. What should its input include?

Domain: Prompt Engineering & Structured Output

- A. Use an independent reviewer without the generator rationale
- B. Record detected_pattern and dismissal reasons
- C. Calibrate field-confidence thresholds against labeled examples
- D. State explicit reportable and non-reportable criteria

### 75. A review creates contradictory findings because one giant pass mixes local and global concerns. What architecture can help?

Domain: Prompt Engineering & Structured Output

- A. Separate local analysis from cross-file integration review
- B. Use an independent reviewer without the generator rationale
- C. Temporarily disable a noisy category while repairing and evaluating it
- D. State explicit reportable and non-reportable criteria

### 76. A reviewer reports confidence for each finding, and leaders want to automate acceptance. What must precede trusting those scores?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. Define severity using impact and concrete examples
- C. State explicit reportable and non-reportable criteria
- D. Record detected_pattern and dismissal reasons

### 77. An instruction says 'review your own work more carefully,' but subtle assumptions persist. What review change may be more effective?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. State explicit reportable and non-reportable criteria
- C. Use an independent reviewer without the generator rationale
- D. Use representative few-shot examples with boundaries

### 78. Every local review passes, but data changes meaning when passed between services. Which review scope is missing?

Domain: Prompt Engineering & Structured Output

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Run independent branches concurrently and join checked results
- C. Separate local analysis from cross-file integration review
- D. Add a cross-file or cross-component integration pass

### 79. A repository-wide review produces repeated and inconsistent comments across files. What should coordinate its outputs?

Domain: Prompt Engineering & Structured Output

- A. State explicit reportable and non-reportable criteria
- B. Use an independent reviewer without the generator rationale
- C. Separate local analysis from cross-file integration review
- D. Use representative few-shot examples with boundaries

### 80. Two fresh reviewers agree, but both rely on the same incomplete specification. What limitation remains important?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. Define severity using impact and concrete examples
- C. Independent agreement does not prove correctness
- D. State explicit reportable and non-reportable criteria

### 81. Assume eligible processing would cost $120 synchronously and receives an illustrative 50% batch discount. What is the discounted processing cost?

Domain: Prompt Engineering & Structured Output

- A. $120
- B. $60
- C. $90
- D. $30

### 82. For planning only, assume processing takes at most 24 hours and total allowance is 30 hours. What maximum submission wait fits that model?

Domain: Prompt Engineering & Structured Output

- A. 12 hours
- B. 6 hours
- C. 30 hours
- D. 24 hours

### 83. A completed 100-item batch has 75 successful items and 25 recoverable failures. How many items should targeted resubmission contain?

Domain: Prompt Engineering & Structured Output

- A. 0 items
- B. 100 items
- C. 25 items
- D. 75 items

### 84. Duplicate custom IDs make two asynchronous outcomes indistinguishable in the application's manifest. What correlation design should be repaired?

Domain: Prompt Engineering & Structured Output

- A. Tune and validate on a representative sample before large submission
- B. Record detected_pattern and dismissal reasons
- C. Correlate batch outcomes by custom_id
- D. Resubmit only failed items after diagnosing their errors

### 85. Some batch items fail because documents exceed context capacity, not because of temporary service errors. What recovery is appropriate?

Domain: Prompt Engineering & Structured Output

- A. Tune and validate on a representative sample before large submission
- B. Resubmit only failed items after diagnosing their errors
- C. Use Message Batches for latency-tolerant independent requests
- D. Correlate batch outcomes by custom_id

### 86. A production prompt fails on scanned layouts absent from its development examples. What pre-batch validation design should improve?

Domain: Prompt Engineering & Structured Output

- A. Correlate batch outcomes by custom_id
- B. Resubmit only failed items after diagnosing their errors
- C. Tune and validate on a representative sample before large submission
- D. Use Message Batches for latency-tolerant independent requests

### 87. A team proposes discounted asynchronous batches for an immediately blocking customer checkout decision. What API approach better matches the requirement?

Domain: Prompt Engineering & Structured Output

- A. Use synchronous requests for blocking latency-sensitive work
- B. Orchestrate client-tool follow-up outside a single batch request
- C. Tune and validate on a representative sample before large submission
- D. Use Message Batches for latency-tolerant independent requests

### 88. A batch output proposes a client-side lookup needed for extraction. What must orchestrate the actual lookup and subsequent request?

Domain: Prompt Engineering & Structured Output

- A. Orchestrate client-tool follow-up outside a single batch request
- B. Use synchronous requests for blocking latency-sensitive work
- C. Use Message Batches for latency-tolerant independent requests
- D. Correlate batch outcomes by custom_id

### 89. A caller associates results by list position and assigns records to the wrong documents. What should replace that association?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. Resubmit only failed items after diagnosing their errors
- C. Tune and validate on a representative sample before large submission
- D. Correlate batch outcomes by custom_id

### 90. An overnight classification workload tolerates asynchronous completion but must not promise a precise minute of delivery. Which approach fits?

Domain: Prompt Engineering & Structured Output

- A. Resubmit only failed items after diagnosing their errors
- B. Use Message Batches for latency-tolerant independent requests
- C. Tune and validate on a representative sample before large submission
- D. Use synchronous requests for blocking latency-sensitive work

### 91. Developers reject a reviewer that equates all unfamiliar patterns with bugs. What should its prompt define?

Domain: Prompt Engineering & Structured Output

- A. Define severity using impact and concrete examples
- B. Calibrate field-confidence thresholds against labeled examples
- C. Temporarily disable a noisy category while repairing and evaluating it
- D. State explicit reportable and non-reportable criteria

### 92. A few-shot set contains only vulnerable examples of an API and omits safe usage. What addition best teaches the intended boundary?

Domain: Prompt Engineering & Structured Output

- A. Provide concrete input–output examples
- B. State explicit reportable and non-reportable criteria
- C. Use representative few-shot examples with boundaries
- D. Include valid examples that should not be flagged

### 93. A pipeline confuses a missing key with a key explicitly set to null. What schema distinction must be designed?

Domain: Prompt Engineering & Structured Output

- A. Use an extensible category plus a detail field
- B. Allow explicit unknown or absent values in the schema
- C. Use supported strict structured output with a schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 94. A constrained extraction satisfies types but assigns tax to the subtotal field. What check must catch this?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Validate extracted values against evidence and business rules
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 95. An error message identifies exactly which source-backed field is wrong, but the retry omits that message. What should be fed back?

Domain: Prompt Engineering & Structured Output

- A. Retry with the document, failed result, and specific validation errors
- B. Allow explicit unknown or absent values in the schema
- C. Mark missing evidence and route for retrieval or review
- D. Use supported strict structured output with a schema

### 96. Two credible source sections disagree on contract start date. What result should support downstream review?

Domain: Prompt Engineering & Structured Output

- A. Compare independently calculated and source-stated totals
- B. Use an extensible category plus a detail field
- C. Preserve conflicting source values with an explicit flag
- D. Allow explicit unknown or absent values in the schema

### 97. A code generator's explanation biases its reviewer toward defending the patch. What input separation may improve review?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. Separate local analysis from cross-file integration review
- C. State explicit reportable and non-reportable criteria
- D. Use an independent reviewer without the generator rationale

### 98. A per-file pass misses that one module returns a unit different from another module's expectation. What pass is needed?

Domain: Prompt Engineering & Structured Output

- A. Run independent branches concurrently and join checked results
- B. Separate local analysis from cross-file integration review
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Add a cross-file or cross-component integration pass

### 99. A prompt revision should target one frequently dismissed warning pattern. What data makes the revision evidence-based?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. Temporarily disable a noisy category while repairing and evaluating it
- C. State explicit reportable and non-reportable criteria
- D. Define severity using impact and concrete examples

### 100. A team says merely writing 'JSON only' guarantees a supported schema. What mechanism addresses the actual structural requirement?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

---

## Answer key and explanations

### Question 1 — B

Answer: State explicit reportable and non-reportable criteria. Define reportable defect categories and explicit exclusions instead of relying on tone. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Define reportable defect categories and explicit exclusions instead of relying on tone.
- **B:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Define reportable defect categories and explicit exclusions instead of relying on tone.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Define reportable defect categories and explicit exclusions instead of relying on tone.
- **D:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Define reportable defect categories and explicit exclusions instead of relying on tone.

### Question 2 — D

Answer: Define severity using impact and concrete examples. Concrete impact-based severity examples improve consistency beyond uncalibrated confidence. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Concrete impact-based severity examples improve consistency beyond uncalibrated confidence.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete impact-based severity examples improve consistency beyond uncalibrated confidence.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Concrete impact-based severity examples improve consistency beyond uncalibrated confidence.
- **D:** Correct. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Concrete impact-based severity examples improve consistency beyond uncalibrated confidence.

### Question 3 — B

Answer: Temporarily disable a noisy category while repairing and evaluating it. Pause the specific noisy category while improving and evaluating it, not all review output. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Pause the specific noisy category while improving and evaluating it, not all review output.
- **B:** Correct. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Pause the specific noisy category while improving and evaluating it, not all review output.
- **C:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Pause the specific noisy category while improving and evaluating it, not all review output.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Pause the specific noisy category while improving and evaluating it, not all review output.

### Question 4 — D

Answer: State explicit reportable and non-reportable criteria. Specify the actual behavioral contradiction required for a reportable comment defect. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Specify the actual behavioral contradiction required for a reportable comment defect.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Specify the actual behavioral contradiction required for a reportable comment defect.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Specify the actual behavioral contradiction required for a reportable comment defect.
- **D:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Specify the actual behavioral contradiction required for a reportable comment defect.

### Question 5 — A

Answer: Include valid examples that should not be flagged. Show an acceptable near-miss that should not be reported, with the boundary explained. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Show an acceptable near-miss that should not be reported, with the boundary explained.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Show an acceptable near-miss that should not be reported, with the boundary explained.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Show an acceptable near-miss that should not be reported, with the boundary explained.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Show an acceptable near-miss that should not be reported, with the boundary explained.

### Question 6 — B

Answer: Record detected_pattern and dismissal reasons. A detected-pattern field enables analysis of recurring false-positive causes. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: A detected-pattern field enables analysis of recurring false-positive causes.
- **B:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: A detected-pattern field enables analysis of recurring false-positive causes.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A detected-pattern field enables analysis of recurring false-positive causes.
- **D:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: A detected-pattern field enables analysis of recurring false-positive causes.

### Question 7 — B

Answer: State explicit reportable and non-reportable criteria. Explicit categorical criteria define correctness more usefully than an unsupported confidence adjective. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Explicit categorical criteria define correctness more usefully than an unsupported confidence adjective.
- **B:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Explicit categorical criteria define correctness more usefully than an unsupported confidence adjective.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Explicit categorical criteria define correctness more usefully than an unsupported confidence adjective.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Explicit categorical criteria define correctness more usefully than an unsupported confidence adjective.

### Question 8 — D

Answer: Define severity using impact and concrete examples. Severity should reflect impact, not merely confidence in the observation. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Severity should reflect impact, not merely confidence in the observation.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Severity should reflect impact, not merely confidence in the observation.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Severity should reflect impact, not merely confidence in the observation.
- **D:** Correct. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Severity should reflect impact, not merely confidence in the observation.

### Question 9 — B

Answer: State explicit reportable and non-reportable criteria. State included and excluded categories so the review's purpose is checkable. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: State included and excluded categories so the review's purpose is checkable.
- **B:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: State included and excluded categories so the review's purpose is checkable.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: State included and excluded categories so the review's purpose is checkable.
- **D:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: State included and excluded categories so the review's purpose is checkable.

### Question 10 — A

Answer: Temporarily disable a noisy category while repairing and evaluating it. Disable only the affected category during controlled repair instead of suppressing all findings. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Disable only the affected category during controlled repair instead of suppressing all findings.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Disable only the affected category during controlled repair instead of suppressing all findings.
- **C:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Disable only the affected category during controlled repair instead of suppressing all findings.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Disable only the affected category during controlled repair instead of suppressing all findings.

### Question 11 — A

Answer: Use representative few-shot examples with boundaries. Representative demonstrations show the requested complete output structure and judgment. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Representative demonstrations show the requested complete output structure and judgment.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Representative demonstrations show the requested complete output structure and judgment.
- **C:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Representative demonstrations show the requested complete output structure and judgment.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative demonstrations show the requested complete output structure and judgment.

### Question 12 — D

Answer: Include valid examples that should not be flagged. Valid negatives teach the boundary between a real defect and an acceptable near-miss. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Valid negatives teach the boundary between a real defect and an acceptable near-miss.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Valid negatives teach the boundary between a real defect and an acceptable near-miss.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Valid negatives teach the boundary between a real defect and an acceptable near-miss.
- **D:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Valid negatives teach the boundary between a real defect and an acceptable near-miss.

### Question 13 — C

Answer: Use representative few-shot examples with boundaries. Include varied document-format examples instead of only one ideal layout. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Include varied document-format examples instead of only one ideal layout.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Include varied document-format examples instead of only one ideal layout.
- **C:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Include varied document-format examples instead of only one ideal layout.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Include varied document-format examples instead of only one ideal layout.

### Question 14 — B

Answer: Use representative few-shot examples with boundaries. Demonstrations can show why a particular boundary favors one action over alternatives. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Demonstrations can show why a particular boundary favors one action over alternatives.
- **B:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Demonstrations can show why a particular boundary favors one action over alternatives.
- **C:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Demonstrations can show why a particular boundary favors one action over alternatives.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Demonstrations can show why a particular boundary favors one action over alternatives.

### Question 15 — D

Answer: Provide concrete input–output examples. Concrete before-and-after examples make the intended unit interpretation visible. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Concrete before-and-after examples make the intended unit interpretation visible.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete before-and-after examples make the intended unit interpretation visible.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Concrete before-and-after examples make the intended unit interpretation visible.
- **D:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Concrete before-and-after examples make the intended unit interpretation visible.

### Question 16 — A

Answer: Use representative few-shot examples with boundaries. Demonstrate the same target fields across structurally different source documents. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Demonstrate the same target fields across structurally different source documents.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Demonstrate the same target fields across structurally different source documents.
- **C:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Demonstrate the same target fields across structurally different source documents.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Demonstrate the same target fields across structurally different source documents.

### Question 17 — D

Answer: Include valid examples that should not be flagged. Show the permitted test-only pattern as a non-finding and explain its boundary. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Show the permitted test-only pattern as a non-finding and explain its boundary.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Show the permitted test-only pattern as a non-finding and explain its boundary.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Show the permitted test-only pattern as a non-finding and explain its boundary.
- **D:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Show the permitted test-only pattern as a non-finding and explain its boundary.

### Question 18 — B

Answer: Use representative few-shot examples with boundaries. A few representative complete outputs can reinforce the expected format without replacing validation. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: A few representative complete outputs can reinforce the expected format without replacing validation.
- **B:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: A few representative complete outputs can reinforce the expected format without replacing validation.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: A few representative complete outputs can reinforce the expected format without replacing validation.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A few representative complete outputs can reinforce the expected format without replacing validation.

### Question 19 — A

Answer: Use representative few-shot examples with boundaries. Cover important variation and ambiguous boundaries rather than only an ideal successful case. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Cover important variation and ambiguous boundaries rather than only an ideal successful case.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Cover important variation and ambiguous boundaries rather than only an ideal successful case.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Cover important variation and ambiguous boundaries rather than only an ideal successful case.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Cover important variation and ambiguous boundaries rather than only an ideal successful case.

### Question 20 — C

Answer: Include valid examples that should not be flagged. Include safe configurations that resemble risky ones but should not be reported. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Include safe configurations that resemble risky ones but should not be reported.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Include safe configurations that resemble risky ones but should not be reported.
- **C:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Include safe configurations that resemble risky ones but should not be reported.
- **D:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Include safe configurations that resemble risky ones but should not be reported.

### Question 21 — C

Answer: Use supported strict structured output with a schema. Use supported strict structured output rather than rely only on a prose JSON request. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use supported strict structured output rather than rely only on a prose JSON request.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use supported strict structured output rather than rely only on a prose JSON request.
- **C:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use supported strict structured output rather than rely only on a prose JSON request.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported strict structured output rather than rely only on a prose JSON request.

### Question 22 — A

Answer: Validate extracted values against evidence and business rules. Schema validity does not prove that values match the intended source evidence. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Schema validity does not prove that values match the intended source evidence.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Schema validity does not prove that values match the intended source evidence.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Schema validity does not prove that values match the intended source evidence.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Schema validity does not prove that values match the intended source evidence.

### Question 23 — D

Answer: Allow explicit unknown or absent values in the schema. Represent absence or unknown explicitly instead of requiring a fabricated concrete value. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Represent absence or unknown explicitly instead of requiring a fabricated concrete value.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Represent absence or unknown explicitly instead of requiring a fabricated concrete value.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Represent absence or unknown explicitly instead of requiring a fabricated concrete value.
- **D:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Represent absence or unknown explicitly instead of requiring a fabricated concrete value.

### Question 24 — B

Answer: Use an extensible category plus a detail field. An other category with details represents known-but-uncatalogued values. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: An other category with details represents known-but-uncatalogued values.
- **B:** Correct. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: An other category with details represents known-but-uncatalogued values.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: An other category with details represents known-but-uncatalogued values.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: An other category with details represents known-but-uncatalogued values.

### Question 25 — C

Answer: Force the required named tool for that turn. Force the named tool where supported; any leaves the specific selection open. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Force the named tool where supported; any leaves the specific selection open.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Force the named tool where supported; any leaves the specific selection open.
- **C:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Force the named tool where supported; any leaves the specific selection open.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Force the named tool where supported; any leaves the specific selection open.

### Question 26 — D

Answer: Use tool_choice with type any. Any requires a tool while permitting choice among the available schemas. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Any requires a tool while permitting choice among the available schemas.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Any requires a tool while permitting choice among the available schemas.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Any requires a tool while permitting choice among the available schemas.
- **D:** Correct. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Any requires a tool while permitting choice among the available schemas.

### Question 27 — D

Answer: Use tool_choice with type auto. Auto does not enforce tool output for every turn. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto does not enforce tool output for every turn.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Auto does not enforce tool output for every turn.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto does not enforce tool output for every turn.
- **D:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto does not enforce tool output for every turn.

### Question 28 — A

Answer: Specify deterministic normalization rules and preserve originals when needed. Specify normalization and uncertainty handling rather than silently guess ambiguous locale. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Specify normalization and uncertainty handling rather than silently guess ambiguous locale.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Specify normalization and uncertainty handling rather than silently guess ambiguous locale.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Specify normalization and uncertainty handling rather than silently guess ambiguous locale.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Specify normalization and uncertainty handling rather than silently guess ambiguous locale.

### Question 29 — B

Answer: Validate extracted values against evidence and business rules. Business arithmetic validation is separate from syntactic and type compliance. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Business arithmetic validation is separate from syntactic and type compliance.
- **B:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Business arithmetic validation is separate from syntactic and type compliance.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Business arithmetic validation is separate from syntactic and type compliance.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Business arithmetic validation is separate from syntactic and type compliance.

### Question 30 — A

Answer: Allow explicit unknown or absent values in the schema. A required nullable field may be present as null; optionality concerns omission of the key. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: A required nullable field may be present as null; optionality concerns omission of the key.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: A required nullable field may be present as null; optionality concerns omission of the key.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: A required nullable field may be present as null; optionality concerns omission of the key.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: A required nullable field may be present as null; optionality concerns omission of the key.

### Question 31 — C

Answer: Use an extensible category plus a detail field. Use an extensible category with detail rather than falsely label a known value as uncertain. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use an extensible category with detail rather than falsely label a known value as uncertain.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use an extensible category with detail rather than falsely label a known value as uncertain.
- **C:** Correct. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Use an extensible category with detail rather than falsely label a known value as uncertain.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use an extensible category with detail rather than falsely label a known value as uncertain.

### Question 32 — C

Answer: Allow explicit unknown or absent values in the schema. An explicit unknown or unclear path differs from a confidently known category outside the list. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: An explicit unknown or unclear path differs from a confidently known category outside the list.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: An explicit unknown or unclear path differs from a confidently known category outside the list.
- **C:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: An explicit unknown or unclear path differs from a confidently known category outside the list.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: An explicit unknown or unclear path differs from a confidently known category outside the list.

### Question 33 — C

Answer: Use supported strict structured output with a schema. Tool selection alone is not identical to supported strict schema-constrained decoding. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Tool selection alone is not identical to supported strict schema-constrained decoding.
- **B:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Tool selection alone is not identical to supported strict schema-constrained decoding.
- **C:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Tool selection alone is not identical to supported strict schema-constrained decoding.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Tool selection alone is not identical to supported strict schema-constrained decoding.

### Question 34 — D

Answer: Validate extracted values against evidence and business rules. Semantic and permission validation remain necessary after structural compliance. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Semantic and permission validation remain necessary after structural compliance.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Semantic and permission validation remain necessary after structural compliance.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Semantic and permission validation remain necessary after structural compliance.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Semantic and permission validation remain necessary after structural compliance.

### Question 35 — C

Answer: Specify deterministic normalization rules and preserve originals when needed. Normalize units deliberately and validate the conversion against the original evidence. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Normalize units deliberately and validate the conversion against the original evidence.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Normalize units deliberately and validate the conversion against the original evidence.
- **C:** Correct. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Normalize units deliberately and validate the conversion against the original evidence.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Normalize units deliberately and validate the conversion against the original evidence.

### Question 36 — A

Answer: Allow explicit unknown or absent values in the schema. Allow absent information to remain explicitly missing or unknown. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Allow absent information to remain explicitly missing or unknown.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Allow absent information to remain explicitly missing or unknown.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Allow absent information to remain explicitly missing or unknown.
- **D:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Allow absent information to remain explicitly missing or unknown.

### Question 37 — B

Answer: Structural constraints do not guarantee complete or factual output. Truncation and response status still need handling even when the intended schema is supported. Supported strict schema modes address shape under supported conditions. Handle truncation, refusal, and status, then separately validate meaning and evidence. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Truncation and response status still need handling even when the intended schema is supported.
- **B:** Correct. Supported strict schema modes address shape under supported conditions. Handle truncation, refusal, and status, then separately validate meaning and evidence. In this case: Truncation and response status still need handling even when the intended schema is supported.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Truncation and response status still need handling even when the intended schema is supported.
- **D:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Truncation and response status still need handling even when the intended schema is supported.

### Question 38 — D

Answer: Validate extracted values against evidence and business rules. Compare extracted values and provenance with the intended source, not only their shape. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Compare extracted values and provenance with the intended source, not only their shape.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Compare extracted values and provenance with the intended source, not only their shape.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Compare extracted values and provenance with the intended source, not only their shape.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Compare extracted values and provenance with the intended source, not only their shape.

### Question 39 — C

Answer: Force the required named tool for that turn. Select the named required operation explicitly before later enrichment steps. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Select the named required operation explicitly before later enrichment steps.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Select the named required operation explicitly before later enrichment steps.
- **C:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Select the named required operation explicitly before later enrichment steps.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Select the named required operation explicitly before later enrichment steps.

### Question 40 — C

Answer: Validate extracted values against evidence and business rules. Verify units and source meaning instead of treating valid syntax as factual correctness. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Verify units and source meaning instead of treating valid syntax as factual correctness.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Verify units and source meaning instead of treating valid syntax as factual correctness.
- **C:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Verify units and source meaning instead of treating valid syntax as factual correctness.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Verify units and source meaning instead of treating valid syntax as factual correctness.

### Question 41 — A

Answer: Retry with the document, failed result, and specific validation errors. Include the document, failed result, and specific error so the model can correct the placement. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Include the document, failed result, and specific error so the model can correct the placement.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Include the document, failed result, and specific error so the model can correct the placement.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Include the document, failed result, and specific error so the model can correct the placement.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Include the document, failed result, and specific error so the model can correct the placement.

### Question 42 — D

Answer: Mark missing evidence and route for retrieval or review. A missing source requires retrieval, clarification, unknown status, or review rather than repeated invention. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: A missing source requires retrieval, clarification, unknown status, or review rather than repeated invention.
- **B:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: A missing source requires retrieval, clarification, unknown status, or review rather than repeated invention.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: A missing source requires retrieval, clarification, unknown status, or review rather than repeated invention.
- **D:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: A missing source requires retrieval, clarification, unknown status, or review rather than repeated invention.

### Question 43 — B

Answer: Compare independently calculated and source-stated totals. Keep independently calculated and source-stated totals separate for comparison. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Keep independently calculated and source-stated totals separate for comparison.
- **B:** Correct. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Keep independently calculated and source-stated totals separate for comparison.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Keep independently calculated and source-stated totals separate for comparison.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Keep independently calculated and source-stated totals separate for comparison.

### Question 44 — A

Answer: Preserve conflicting source values with an explicit flag. Flag and retain the conflict instead of silently choosing a convenient value. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Flag and retain the conflict instead of silently choosing a convenient value.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Flag and retain the conflict instead of silently choosing a convenient value.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Flag and retain the conflict instead of silently choosing a convenient value.
- **D:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Flag and retain the conflict instead of silently choosing a convenient value.

### Question 45 — B

Answer: Record detected_pattern and dismissal reasons. Record detected patterns and dismissal reasons to identify systematic false positives. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Record detected patterns and dismissal reasons to identify systematic false positives.
- **B:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Record detected patterns and dismissal reasons to identify systematic false positives.
- **C:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Record detected patterns and dismissal reasons to identify systematic false positives.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Record detected patterns and dismissal reasons to identify systematic false positives.

### Question 46 — A

Answer: Retry with the document, failed result, and specific validation errors. Feed the specific validation error and failed extraction back with the source. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Feed the specific validation error and failed extraction back with the source.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Feed the specific validation error and failed extraction back with the source.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Feed the specific validation error and failed extraction back with the source.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Feed the specific validation error and failed extraction back with the source.

### Question 47 — C

Answer: Mark missing evidence and route for retrieval or review. Mark missing evidence and seek an authorized source or reviewer instead of retrying blindly. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Mark missing evidence and seek an authorized source or reviewer instead of retrying blindly.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Mark missing evidence and seek an authorized source or reviewer instead of retrying blindly.
- **C:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Mark missing evidence and seek an authorized source or reviewer instead of retrying blindly.
- **D:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Mark missing evidence and seek an authorized source or reviewer instead of retrying blindly.

### Question 48 — A

Answer: Validate extracted values against evidence and business rules. Revalidate semantic accuracy after every correction, not only parsing success. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Revalidate semantic accuracy after every correction, not only parsing success.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Revalidate semantic accuracy after every correction, not only parsing success.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Revalidate semantic accuracy after every correction, not only parsing success.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Revalidate semantic accuracy after every correction, not only parsing success.

### Question 49 — D

Answer: Preserve conflicting source values with an explicit flag. Preserve source disagreement explicitly so review can resolve it knowingly. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Preserve source disagreement explicitly so review can resolve it knowingly.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Preserve source disagreement explicitly so review can resolve it knowingly.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Preserve source disagreement explicitly so review can resolve it knowingly.
- **D:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Preserve source disagreement explicitly so review can resolve it knowingly.

### Question 50 — A

Answer: Retry with the document, failed result, and specific validation errors. A specific bounded retry can correct recoverable formatting when evidence actually exists. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: A specific bounded retry can correct recoverable formatting when evidence actually exists.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: A specific bounded retry can correct recoverable formatting when evidence actually exists.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: A specific bounded retry can correct recoverable formatting when evidence actually exists.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: A specific bounded retry can correct recoverable formatting when evidence actually exists.

### Question 51 — C

Answer: Enforce task, iteration, and spending safeguards. Bound repair attempts and route unresolved cases instead of allowing indefinite retry. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Bound repair attempts and route unresolved cases instead of allowing indefinite retry.
- **B:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Bound repair attempts and route unresolved cases instead of allowing indefinite retry.
- **C:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound repair attempts and route unresolved cases instead of allowing indefinite retry.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Bound repair attempts and route unresolved cases instead of allowing indefinite retry.

### Question 52 — C

Answer: Record detected_pattern and dismissal reasons. Detected-pattern metadata connects dismissed warnings to the underlying code constructs. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Detected-pattern metadata connects dismissed warnings to the underlying code constructs.
- **B:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Detected-pattern metadata connects dismissed warnings to the underlying code constructs.
- **C:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Detected-pattern metadata connects dismissed warnings to the underlying code constructs.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Detected-pattern metadata connects dismissed warnings to the underlying code constructs.

### Question 53 — C

Answer: Compare independently calculated and source-stated totals. Store both stated and calculated values so discrepancies remain visible. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Store both stated and calculated values so discrepancies remain visible.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Store both stated and calculated values so discrepancies remain visible.
- **C:** Correct. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Store both stated and calculated values so discrepancies remain visible.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Store both stated and calculated values so discrepancies remain visible.

### Question 54 — A

Answer: Preserve conflicting source values with an explicit flag. Preserve both attributed values and mark the conflict for resolution. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Preserve both attributed values and mark the conflict for resolution.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Preserve both attributed values and mark the conflict for resolution.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Preserve both attributed values and mark the conflict for resolution.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Preserve both attributed values and mark the conflict for resolution.

### Question 55 — A

Answer: Retry with the document, failed result, and specific validation errors. The model needs the source as well as the failed output and specific error. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: The model needs the source as well as the failed output and specific error.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: The model needs the source as well as the failed output and specific error.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: The model needs the source as well as the failed output and specific error.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: The model needs the source as well as the failed output and specific error.

### Question 56 — B

Answer: Mark missing evidence and route for retrieval or review. No amount of rewording supplies absent evidence without another legitimate information source. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: No amount of rewording supplies absent evidence without another legitimate information source.
- **B:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: No amount of rewording supplies absent evidence without another legitimate information source.
- **C:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: No amount of rewording supplies absent evidence without another legitimate information source.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: No amount of rewording supplies absent evidence without another legitimate information source.

### Question 57 — B

Answer: Validate extracted values against evidence and business rules. Verify source correctness and field relationships after the revision. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Verify source correctness and field relationships after the revision.
- **B:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Verify source correctness and field relationships after the revision.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Verify source correctness and field relationships after the revision.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Verify source correctness and field relationships after the revision.

### Question 58 — B

Answer: Tune and validate on a representative sample before large submission. Refine and validate on a representative sample before multiplying the failure. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Refine and validate on a representative sample before multiplying the failure.
- **B:** Correct. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Refine and validate on a representative sample before multiplying the failure.
- **C:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Refine and validate on a representative sample before multiplying the failure.
- **D:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Refine and validate on a representative sample before multiplying the failure.

### Question 59 — C

Answer: Record detected_pattern and dismissal reasons. Structured patterns and dismissal reasons enable targeted fixes rather than guessing from aggregate counts. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Structured patterns and dismissal reasons enable targeted fixes rather than guessing from aggregate counts.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Structured patterns and dismissal reasons enable targeted fixes rather than guessing from aggregate counts.
- **C:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Structured patterns and dismissal reasons enable targeted fixes rather than guessing from aggregate counts.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Structured patterns and dismissal reasons enable targeted fixes rather than guessing from aggregate counts.

### Question 60 — D

Answer: Preserve conflicting source values with an explicit flag. A conflict flag and attributed alternatives preserve disagreement distinctly from absence. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: A conflict flag and attributed alternatives preserve disagreement distinctly from absence.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: A conflict flag and attributed alternatives preserve disagreement distinctly from absence.
- **C:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: A conflict flag and attributed alternatives preserve disagreement distinctly from absence.
- **D:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: A conflict flag and attributed alternatives preserve disagreement distinctly from absence.

### Question 61 — B

Answer: Use Message Batches for latency-tolerant independent requests. Latency-tolerant non-blocking work is suitable for batch processing. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Latency-tolerant non-blocking work is suitable for batch processing.
- **B:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Latency-tolerant non-blocking work is suitable for batch processing.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Latency-tolerant non-blocking work is suitable for batch processing.
- **D:** Incorrect for this question. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: Latency-tolerant non-blocking work is suitable for batch processing.

### Question 62 — D

Answer: Use synchronous requests for blocking latency-sensitive work. Choose a latency-appropriate synchronous path with defined timeout and failure behavior. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Choose a latency-appropriate synchronous path with defined timeout and failure behavior.
- **B:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Choose a latency-appropriate synchronous path with defined timeout and failure behavior.
- **C:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Choose a latency-appropriate synchronous path with defined timeout and failure behavior.
- **D:** Correct. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Choose a latency-appropriate synchronous path with defined timeout and failure behavior.

### Question 63 — B

Answer: Correlate batch outcomes by custom_id. Stable custom IDs correlate inputs and results without relying on ordering. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Stable custom IDs correlate inputs and results without relying on ordering.
- **B:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Stable custom IDs correlate inputs and results without relying on ordering.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Stable custom IDs correlate inputs and results without relying on ordering.
- **D:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Stable custom IDs correlate inputs and results without relying on ordering.

### Question 64 — D

Answer: Resubmit only failed items after diagnosing their errors. Retry only failed items after repairing the oversized inputs and retaining request identity. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Retry only failed items after repairing the oversized inputs and retaining request identity.
- **B:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Retry only failed items after repairing the oversized inputs and retaining request identity.
- **C:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Retry only failed items after repairing the oversized inputs and retaining request identity.
- **D:** Correct. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Retry only failed items after repairing the oversized inputs and retaining request identity.

### Question 65 — C

Answer: Tune and validate on a representative sample before large submission. Representative sample refinement reduces widespread first-pass errors and resubmission work. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Representative sample refinement reduces widespread first-pass errors and resubmission work.
- **B:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Representative sample refinement reduces widespread first-pass errors and resubmission work.
- **C:** Correct. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Representative sample refinement reduces widespread first-pass errors and resubmission work.
- **D:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Representative sample refinement reduces widespread first-pass errors and resubmission work.

### Question 66 — A

Answer: Orchestrate client-tool follow-up outside a single batch request. Client execution and follow-up requests require explicit orchestration outside that single batch request. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: Client execution and follow-up requests require explicit orchestration outside that single batch request.
- **B:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Client execution and follow-up requests require explicit orchestration outside that single batch request.
- **C:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Client execution and follow-up requests require explicit orchestration outside that single batch request.
- **D:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Client execution and follow-up requests require explicit orchestration outside that single batch request.

### Question 67 — C

Answer: Use Message Batches for latency-tolerant independent requests. Asynchronous batch processing fits the stated latency tolerance. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Asynchronous batch processing fits the stated latency tolerance.
- **B:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Asynchronous batch processing fits the stated latency tolerance.
- **C:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Asynchronous batch processing fits the stated latency tolerance.
- **D:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Asynchronous batch processing fits the stated latency tolerance.

### Question 68 — A

Answer: Use synchronous requests for blocking latency-sensitive work. Use a latency-appropriate interactive orchestration path rather than assume one asynchronous item handles the entire conversation. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Use a latency-appropriate interactive orchestration path rather than assume one asynchronous item handles the entire conversation.
- **B:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Use a latency-appropriate interactive orchestration path rather than assume one asynchronous item handles the entire conversation.
- **C:** Incorrect for this question. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: Use a latency-appropriate interactive orchestration path rather than assume one asynchronous item handles the entire conversation.
- **D:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Use a latency-appropriate interactive orchestration path rather than assume one asynchronous item handles the entire conversation.

### Question 69 — C

Answer: Correlate batch outcomes by custom_id. Unique stable custom IDs connect each outcome to its submission manifest. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Unique stable custom IDs connect each outcome to its submission manifest.
- **B:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Unique stable custom IDs connect each outcome to its submission manifest.
- **C:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Unique stable custom IDs connect each outcome to its submission manifest.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Unique stable custom IDs connect each outcome to its submission manifest.

### Question 70 — B

Answer: Resubmit only failed items after diagnosing their errors. Target failed items and protect processing against duplicates instead of replaying every success. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Target failed items and protect processing against duplicates instead of replaying every success.
- **B:** Correct. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Target failed items and protect processing against duplicates instead of replaying every success.
- **C:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Target failed items and protect processing against duplicates instead of replaying every success.
- **D:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Target failed items and protect processing against duplicates instead of replaying every success.

### Question 71 — D

Answer: Use an independent reviewer without the generator rationale. Use an independent reviewer without the generation rationale but with requirements and artifacts. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use an independent reviewer without the generation rationale but with requirements and artifacts.
- **B:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Use an independent reviewer without the generation rationale but with requirements and artifacts.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use an independent reviewer without the generation rationale but with requirements and artifacts.
- **D:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Use an independent reviewer without the generation rationale but with requirements and artifacts.

### Question 72 — D

Answer: Separate local analysis from cross-file integration review. Focused local passes plus integration review reduce attention dilution while retaining cross-file checks. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Focused local passes plus integration review reduce attention dilution while retaining cross-file checks.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Focused local passes plus integration review reduce attention dilution while retaining cross-file checks.
- **C:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Focused local passes plus integration review reduce attention dilution while retaining cross-file checks.
- **D:** Correct. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Focused local passes plus integration review reduce attention dilution while retaining cross-file checks.

### Question 73 — B

Answer: Add a cross-file or cross-component integration pass. Cross-file integration analysis checks contracts that isolated review cannot establish. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Cross-file integration analysis checks contracts that isolated review cannot establish.
- **B:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Cross-file integration analysis checks contracts that isolated review cannot establish.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Cross-file integration analysis checks contracts that isolated review cannot establish.
- **D:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Cross-file integration analysis checks contracts that isolated review cannot establish.

### Question 74 — A

Answer: Use an independent reviewer without the generator rationale. Provide the specification and relevant artifacts, not an empty context or the generator's defense. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Provide the specification and relevant artifacts, not an empty context or the generator's defense.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Provide the specification and relevant artifacts, not an empty context or the generator's defense.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Provide the specification and relevant artifacts, not an empty context or the generator's defense.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Provide the specification and relevant artifacts, not an empty context or the generator's defense.

### Question 75 — A

Answer: Separate local analysis from cross-file integration review. Separate focused passes and reconcile their outputs in an integration step. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Separate focused passes and reconcile their outputs in an integration step.
- **B:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Separate focused passes and reconcile their outputs in an integration step.
- **C:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Separate focused passes and reconcile their outputs in an integration step.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Separate focused passes and reconcile their outputs in an integration step.

### Question 76 — A

Answer: Calibrate field-confidence thresholds against labeled examples. Validate confidence against labeled outcomes instead of treating self-reported numbers as probabilities. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Validate confidence against labeled outcomes instead of treating self-reported numbers as probabilities.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Validate confidence against labeled outcomes instead of treating self-reported numbers as probabilities.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Validate confidence against labeled outcomes instead of treating self-reported numbers as probabilities.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Validate confidence against labeled outcomes instead of treating self-reported numbers as probabilities.

### Question 77 — C

Answer: Use an independent reviewer without the generator rationale. A separate context can challenge assumptions without inheriting the original rationale. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: A separate context can challenge assumptions without inheriting the original rationale.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A separate context can challenge assumptions without inheriting the original rationale.
- **C:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: A separate context can challenge assumptions without inheriting the original rationale.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: A separate context can challenge assumptions without inheriting the original rationale.

### Question 78 — D

Answer: Add a cross-file or cross-component integration pass. Cross-component data-flow review checks interactions and shared assumptions. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Cross-component data-flow review checks interactions and shared assumptions.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Cross-component data-flow review checks interactions and shared assumptions.
- **C:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Cross-component data-flow review checks interactions and shared assumptions.
- **D:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Cross-component data-flow review checks interactions and shared assumptions.

### Question 79 — C

Answer: Separate local analysis from cross-file integration review. Use focused analysis plus an explicit reconciliation and integration stage. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use focused analysis plus an explicit reconciliation and integration stage.
- **B:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Use focused analysis plus an explicit reconciliation and integration stage.
- **C:** Correct. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Use focused analysis plus an explicit reconciliation and integration stage.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use focused analysis plus an explicit reconciliation and integration stage.

### Question 80 — C

Answer: Independent agreement does not prove correctness. Independent contexts reduce anchoring but do not create missing requirements or guarantee correctness. Fresh reviewers can share incomplete requirements, model limitations, or missing evidence. Review independence reduces anchoring but does not create omitted facts or guarantee truth. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Independent contexts reduce anchoring but do not create missing requirements or guarantee correctness.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Independent contexts reduce anchoring but do not create missing requirements or guarantee correctness.
- **C:** Correct. Fresh reviewers can share incomplete requirements, model limitations, or missing evidence. Review independence reduces anchoring but does not create omitted facts or guarantee truth. In this case: Independent contexts reduce anchoring but do not create missing requirements or guarantee correctness.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Independent contexts reduce anchoring but do not create missing requirements or guarantee correctness.

### Question 81 — B

Answer: $60. Half of the stated $120 baseline is $60; these are illustrative figures, not live prices. Under an illustrative 50% discount on $120 of eligible processing, cost is $120 × 0.5 = $60. Actual billing depends on current terms and eligible usage. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The undiscounted baseline is not the discounted result when the entire stated workload is eligible. In this case: Half of the stated $120 baseline is $60; these are illustrative figures, not live prices.
- **B:** Correct. Under an illustrative 50% discount on $120 of eligible processing, cost is $120 × 0.5 = $60. Actual billing depends on current terms and eligible usage. In this case: Half of the stated $120 baseline is $60; these are illustrative figures, not live prices.
- **C:** Incorrect for this question. A 25% discount on $120 would leave $90; a 50% discount has a different result. In this case: Half of the stated $120 baseline is $60; these are illustrative figures, not live prices.
- **D:** Incorrect for this question. A dollar result must follow the specified workload and discount. A 50% discount is one half off, not two successive halvings. In this case: Half of the stated $120 baseline is $60; these are illustrative figures, not live prices.

### Question 82 — B

Answer: 6 hours. The remaining modeled allowance is 30 minus 24, or 6 hours; this does not establish a service SLA. Under the stated planning assumption, a 30-hour total allowance minus 24-hour processing leaves 6 hours for submission delay. This arithmetic is not a provider latency guarantee. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A submission interval must fit the remaining allowance after the assumed processing duration, not an arbitrary half-day cadence. In this case: The remaining modeled allowance is 30 minus 24, or 6 hours; this does not establish a service SLA.
- **B:** Correct. Under the stated planning assumption, a 30-hour total allowance minus 24-hour processing leaves 6 hours for submission delay. This arithmetic is not a provider latency guarantee. In this case: The remaining modeled allowance is 30 minus 24, or 6 hours; this does not establish a service SLA.
- **C:** Incorrect for this question. The total turnaround allowance includes both submission wait and assumed processing time; it cannot all be spent waiting. In this case: The remaining modeled allowance is 30 minus 24, or 6 hours; this does not establish a service SLA.
- **D:** Incorrect for this question. The processing assumption itself is not the remaining budget for waiting until submission. In this case: The remaining modeled allowance is 30 minus 24, or 6 hours; this does not establish a service SLA.

### Question 83 — C

Answer: 25 items. Resubmit the 25 failed items after diagnosis, not the 75 successes or all 100. If a completed 100-item batch has 75 successes, 25 items remain unsuccessful. Diagnose those failures rather than replay successful inputs. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Failed items may still need correction or retry when processing requirements call for completion; inspect failure causes rather than silently discard them. In this case: Resubmit the 25 failed items after diagnosis, not the 75 successes or all 100.
- **B:** Incorrect for this question. Resubmitting every item repeats successful work when the problem is limited to a subset. In this case: Resubmit the 25 failed items after diagnosis, not the 75 successes or all 100.
- **C:** Correct. If a completed 100-item batch has 75 successes, 25 items remain unsuccessful. Diagnose those failures rather than replay successful inputs. In this case: Resubmit the 25 failed items after diagnosis, not the 75 successes or all 100.
- **D:** Incorrect for this question. Successful items should not normally be resubmitted solely because other items in the same batch failed. In this case: Resubmit the 25 failed items after diagnosis, not the 75 successes or all 100.

### Question 84 — C

Answer: Correlate batch outcomes by custom_id. Each request needs a unique stable identifier to match results safely. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Each request needs a unique stable identifier to match results safely.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Each request needs a unique stable identifier to match results safely.
- **C:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Each request needs a unique stable identifier to match results safely.
- **D:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Each request needs a unique stable identifier to match results safely.

### Question 85 — B

Answer: Resubmit only failed items after diagnosing their errors. Modify the failed inputs, such as coherent chunking, before targeted resubmission. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Modify the failed inputs, such as coherent chunking, before targeted resubmission.
- **B:** Correct. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Modify the failed inputs, such as coherent chunking, before targeted resubmission.
- **C:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Modify the failed inputs, such as coherent chunking, before targeted resubmission.
- **D:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Modify the failed inputs, such as coherent chunking, before targeted resubmission.

### Question 86 — C

Answer: Tune and validate on a representative sample before large submission. The sample should represent important document variation before large-scale processing. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: The sample should represent important document variation before large-scale processing.
- **B:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: The sample should represent important document variation before large-scale processing.
- **C:** Correct. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: The sample should represent important document variation before large-scale processing.
- **D:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: The sample should represent important document variation before large-scale processing.

### Question 87 — A

Answer: Use synchronous requests for blocking latency-sensitive work. A latency-appropriate synchronous path is more suitable than a non-guaranteed asynchronous turnaround. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: A latency-appropriate synchronous path is more suitable than a non-guaranteed asynchronous turnaround.
- **B:** Incorrect for this question. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: A latency-appropriate synchronous path is more suitable than a non-guaranteed asynchronous turnaround.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: A latency-appropriate synchronous path is more suitable than a non-guaranteed asynchronous turnaround.
- **D:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: A latency-appropriate synchronous path is more suitable than a non-guaranteed asynchronous turnaround.

### Question 88 — A

Answer: Orchestrate client-tool follow-up outside a single batch request. The application handles tool execution and follow-up turns outside the individual batch request. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: The application handles tool execution and follow-up turns outside the individual batch request.
- **B:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: The application handles tool execution and follow-up turns outside the individual batch request.
- **C:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: The application handles tool execution and follow-up turns outside the individual batch request.
- **D:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: The application handles tool execution and follow-up turns outside the individual batch request.

### Question 89 — D

Answer: Correlate batch outcomes by custom_id. Match by custom_id against the submission manifest rather than assume result ordering. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Match by custom_id against the submission manifest rather than assume result ordering.
- **B:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Match by custom_id against the submission manifest rather than assume result ordering.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Match by custom_id against the submission manifest rather than assume result ordering.
- **D:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Match by custom_id against the submission manifest rather than assume result ordering.

### Question 90 — B

Answer: Use Message Batches for latency-tolerant independent requests. Batch processing matches latency tolerance, while its documented window should not be represented as a guaranteed SLA. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Batch processing matches latency tolerance, while its documented window should not be represented as a guaranteed SLA.
- **B:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Batch processing matches latency tolerance, while its documented window should not be represented as a guaranteed SLA.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Batch processing matches latency tolerance, while its documented window should not be represented as a guaranteed SLA.
- **D:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Batch processing matches latency tolerance, while its documented window should not be represented as a guaranteed SLA.

### Question 91 — D

Answer: State explicit reportable and non-reportable criteria. Reportable behavior and permitted local patterns need explicit boundaries rather than novelty-based flags. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Reportable behavior and permitted local patterns need explicit boundaries rather than novelty-based flags.
- **B:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Reportable behavior and permitted local patterns need explicit boundaries rather than novelty-based flags.
- **C:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Reportable behavior and permitted local patterns need explicit boundaries rather than novelty-based flags.
- **D:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Reportable behavior and permitted local patterns need explicit boundaries rather than novelty-based flags.

### Question 92 — D

Answer: Include valid examples that should not be flagged. A valid negative demonstrates safe usage so the model does not generalize to blanket rejection. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: A valid negative demonstrates safe usage so the model does not generalize to blanket rejection.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A valid negative demonstrates safe usage so the model does not generalize to blanket rejection.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: A valid negative demonstrates safe usage so the model does not generalize to blanket rejection.
- **D:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: A valid negative demonstrates safe usage so the model does not generalize to blanket rejection.

### Question 93 — B

Answer: Allow explicit unknown or absent values in the schema. Optionality and nullability represent different allowed structures and should be specified deliberately. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Optionality and nullability represent different allowed structures and should be specified deliberately.
- **B:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Optionality and nullability represent different allowed structures and should be specified deliberately.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Optionality and nullability represent different allowed structures and should be specified deliberately.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Optionality and nullability represent different allowed structures and should be specified deliberately.

### Question 94 — B

Answer: Validate extracted values against evidence and business rules. Semantic field placement must be verified against the source, not inferred from schema success. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Semantic field placement must be verified against the source, not inferred from schema success.
- **B:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Semantic field placement must be verified against the source, not inferred from schema success.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Semantic field placement must be verified against the source, not inferred from schema success.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Semantic field placement must be verified against the source, not inferred from schema success.

### Question 95 — A

Answer: Retry with the document, failed result, and specific validation errors. Specific error evidence helps a bounded correction more than an unchanged request. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Specific error evidence helps a bounded correction more than an unchanged request.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Specific error evidence helps a bounded correction more than an unchanged request.
- **C:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Specific error evidence helps a bounded correction more than an unchanged request.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Specific error evidence helps a bounded correction more than an unchanged request.

### Question 96 — C

Answer: Preserve conflicting source values with an explicit flag. Preserve and flag the incompatible values rather than fabricate one resolved date. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Preserve and flag the incompatible values rather than fabricate one resolved date.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Preserve and flag the incompatible values rather than fabricate one resolved date.
- **C:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Preserve and flag the incompatible values rather than fabricate one resolved date.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Preserve and flag the incompatible values rather than fabricate one resolved date.

### Question 97 — D

Answer: Use an independent reviewer without the generator rationale. Give an independent reviewer requirements and code without the generator's rationale. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Give an independent reviewer requirements and code without the generator's rationale.
- **B:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Give an independent reviewer requirements and code without the generator's rationale.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Give an independent reviewer requirements and code without the generator's rationale.
- **D:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Give an independent reviewer requirements and code without the generator's rationale.

### Question 98 — D

Answer: Add a cross-file or cross-component integration pass. Integration review checks cross-file contracts and data meaning. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Integration review checks cross-file contracts and data meaning.
- **B:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Integration review checks cross-file contracts and data meaning.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Integration review checks cross-file contracts and data meaning.
- **D:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Integration review checks cross-file contracts and data meaning.

### Question 99 — A

Answer: Record detected_pattern and dismissal reasons. Detected-pattern and dismissal metadata reveal the specific recurring source of false positives. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Detected-pattern and dismissal metadata reveal the specific recurring source of false positives.
- **B:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Detected-pattern and dismissal metadata reveal the specific recurring source of false positives.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Detected-pattern and dismissal metadata reveal the specific recurring source of false positives.
- **D:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Detected-pattern and dismissal metadata reveal the specific recurring source of false positives.

### Question 100 — D

Answer: Use supported strict structured output with a schema. Use supported constrained schema output and validate response status instead of relying solely on prose. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use supported constrained schema output and validate response status instead of relying solely on prose.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported constrained schema output and validate response status instead of relying solely on prose.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use supported constrained schema output and validate response status instead of relying solely on prose.
- **D:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use supported constrained schema output and validate response status instead of relying solely on prose.
