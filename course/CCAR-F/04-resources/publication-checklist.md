# CCAR-F — Instructor publication checklist

The package is prepared for instructor review. No actual Udemy account import, publication, or certification registration was performed.

## Content review

- [ ] Read every question, key, option explanation, and overall rationale.
- [ ] Check ambiguity and distractor plausibility, especially alternatives that are useful but do not address the stated requirement.
- [ ] Confirm current official guide and program details.
- [ ] Verify installed-version differences: Task/Agent, inspection commands, skills, hooks, schema support, and CLI options.
- [ ] Keep financial and scheduling assumptions explicitly illustrative, not live prices or guaranteed SLAs.
- [ ] Retain no-endorsement, originality, repeated-concept, and no-guarantee disclosures.

## Listing

- [ ] Copy the six landing-page metadata blocks into matching instructor fields.
- [ ] Add the welcome and congratulations messages where supported.
- [ ] Explain five domain tests plus one integrated review, not six identical weighted mocks.
- [ ] Explain that all package items are single-answer although the official exam also has multiple-response items.
- [ ] Do not promise included videos, provisioned labs, API credits, vouchers, identical exam difficulty, or certification.
- [ ] Treat 200 minutes and 80% as custom practice settings; never equate a raw percentage with 720 scaled.

## Imports

| Test | CSV under `03-practice-sets/` | Expected count | Imported | Previewed |
|---|---|---:|---|---|
| 1 | `set-1/practice-set-1.csv` | 100 | [ ] | [ ] |
| 2 | `set-2/practice-set-2.csv` | 100 | [ ] | [ ] |
| 3 | `set-3/practice-set-3.csv` | 100 | [ ] | [ ] |
| 4 | `set-4/practice-set-4.csv` | 100 | [ ] | [ ] |
| 5 | `set-5/practice-set-5.csv` | 100 | [ ] | [ ] |
| 6 | `set-6/practice-set-6.csv` | 100 | [ ] | [ ] |

Compare a fresh template with the supplied CSVs. Upload each file separately, not the ZIP.

## Preview every test

- [ ] Exactly 100 questions, four visible choices, and one correct selection.
- [ ] Test 1–5 domain labels match the respective focus; Test 6 counts are 27/18/20/20/15.
- [ ] Keys match the offline review and manifest.
- [ ] Unused fifth and sixth options do not appear.
- [ ] Explanations, punctuation, code identifiers, and links render correctly.
- [ ] Learner-visible question text does not expose the answer key.
- [ ] Practice settings and format differences are clearly disclosed.

## Troubleshooting

| Issue | Check |
|---|---|
| Import rejected | Latest template, exact headers, supported type, encoding, and row-level errors |
| Shifted columns | Preserve CSV quoting; do not split on commas manually |
| Wrong answer | Keys are 1-based positions; rebuild after changing options |
| Fewer than 100 questions | Resolve rejected rows before publishing |
| Stale companion files | Run build, validate with report, tests, then package |

## Final sign-off

- [ ] Subject-matter and editorial review complete.
- [ ] All six imports previewed in the instructor account.
- [ ] Listing accurate and disclosures retained.
- [ ] Source and published version retained.

Reviewer: ____________________  Date: ____________________

Publication version: ____________________
