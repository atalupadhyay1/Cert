# AWS Certified AI Practitioner (AIF-C01) — Udemy practice-test package

**6 sets × 100 questions = 600 questions.** Fresh AWS course; existing Microsoft course files are unchanged.

## Download and upload

Use **[AWS-AIF-C01-Udemy-6x100.zip](AWS-AIF-C01-Udemy-6x100.zip)** for the complete package. Extract it before uploading.

| Test | Udemy CSV | Offline questions and explanations |
|---|---|---|
| 1 | [Set 1 CSV](03-practice-sets/set-1/practice-set-1.csv) | [Read Set 1](03-practice-sets/set-1/practice-set-1.md) |
| 2 | [Set 2 CSV](03-practice-sets/set-2/practice-set-2.csv) | [Read Set 2](03-practice-sets/set-2/practice-set-2.md) |
| 3 | [Set 3 CSV](03-practice-sets/set-3/practice-set-3.csv) | [Read Set 3](03-practice-sets/set-3/practice-set-3.md) |
| 4 | [Set 4 CSV](03-practice-sets/set-4/practice-set-4.csv) | [Read Set 4](03-practice-sets/set-4/practice-set-4.md) |
| 5 | [Set 5 CSV](03-practice-sets/set-5/practice-set-5.csv) | [Read Set 5](03-practice-sets/set-5/practice-set-5.md) |
| 6 | [Set 6 CSV](03-practice-sets/set-6/practice-set-6.csv) | [Read Set 6](03-practice-sets/set-6/practice-set-6.md) |

1. Create a practice-test course in your Udemy instructor account.
2. Copy the [landing-page content](01-landing-page/landing-page.md) and [curriculum](02-curriculum/curriculum-outline.md).
3. Add six practice tests, then import the corresponding CSV into each test. Upload CSVs individually, not the ZIP.
4. Compare the columns with the current template downloaded from your instructor account. Preview each imported test, especially multiple-select keys and explanations.
5. Use a suggested **140-minute** duration and **80% practice target** if appropriate for your audience. These are course settings, not official exam settings or score conversions.
6. Review technical accuracy, platform formatting, and current service availability before publication. No Udemy account upload or publication has been performed here.

Use the [instructor publication checklist](04-resources/publication-checklist.md) to track content review, imports, and final sign-off.

## Included in every set

- 90 single-answer questions with four choices.
- 10 select-two questions with five choices, explicit selection counts, and all-or-nothing answer keys.
- Feedback for each answer option, overall rationale, and an AWS exam-guide reference. Service-specific further reading is included where mapped.
- Mixed domain order and shuffled options. Single-answer positions are balanced: 23/23/22/22.
- Questions first and an answer/explanation section afterward in the Markdown review copy.

| AWS domain | Per set | Across six sets |
|---|---:|---:|
| Fundamentals of AI and ML | 20 | 120 |
| Fundamentals of GenAI | 24 | 144 |
| Applications of Foundation Models | 28 | 168 |
| Guidelines for Responsible AI | 14 | 84 |
| Security, Compliance, and Governance for AI Solutions | 14 | 84 |
| **Total** | **100** | **600** |

## Important scope and originality notes

These are original educational questions, not recalled exam content, exam dumps, or official AWS questions. The tests revisit shared learning objectives using different scenarios and wording. Thirty targeted extensions add coverage such as MCP, agent memory, multi-agent coordination, model evaluation, and governance services. **600 distinct question texts does not mean 600 unrelated concepts or six statistically independent exam forms.** Some options and explanations intentionally recur to reinforce concepts.

The current AWS guide lists multiple choice, multiple response, ordering, and matching formats. This package uses Udemy-compatible single-answer and multiple-select formats only. It does not reproduce native interactive ordering or matching. These are expanded 100-question learning tests, not exact replicas of the official exam length or scoring system. A raw 80% practice result does not establish an AWS scaled score or guarantee passing.

## Validation and maintenance

Requires Python **3.10+**, with no external packages:

```bash
python course/AIF-C01/04-resources/build.py
python course/AIF-C01/04-resources/validate.py --report course/AIF-C01/04-resources/validation-report.json
python -m unittest discover -s course/AIF-C01/04-resources -p 'test_*.py' -v
python course/AIF-C01/04-resources/package.py
```

Edit `04-resources/bank.py` and regenerate; do not edit generated CSV keys separately. The validator checks formatting, counts, answer bounds, source consistency, and normalized duplicate wording. It cannot independently certify factual accuracy, detect all semantic repetition, verify live reference availability, or guarantee Udemy acceptance. See [validation report](04-resources/validation-report.json), [sources and coverage](04-resources/sources-and-coverage.md), and [CSV specification](04-resources/csv-format-spec.md).

Independent educational material. Not affiliated with or endorsed by AWS or Udemy. AWS product names and certification marks belong to their respective owners.
