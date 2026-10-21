# Instructor publication checklist

The files are prepared locally; the Udemy steps below have not been performed on your behalf.

## Content and sources

- [ ] Review the current Google certification page, exam guide, study guide, and branding.
- [ ] Read every question, key, and explanation for correctness, ambiguity, and appropriate business-level difficulty.
- [ ] Open the source references and update moved links.
- [ ] Confirm product purposes and account/edition availability where relevant.
- [ ] Keep financial examples explicitly illustrative rather than representing actual service prices.
- [ ] Retain originality, no-endorsement, repeated-concept, and no-guarantee disclosures.
- [ ] Do not advertise real exam questions or identical calibrated exam difficulty.

## Listing

- [ ] Copy the six metadata blocks from `01-landing-page/landing-page.md` into the corresponding fields.
- [ ] Add the welcome and congratulations messages where supported.
- [ ] Verify title/subtitle limits and current publication requirements.
- [ ] Do not advertise included video lessons, cloud credits, or labs.
- [ ] Explain that the 100-question sets are longer than the official exam format.

## Import

Compare a fresh template from your instructor account with the supplied 17-column CSVs.

| Set | CSV under `03-practice-sets/` | Expected count | Imported | Previewed |
|---|---|---:|---|---|
| 1 | `set-1/practice-set-1.csv` | 100 | [ ] | [ ] |
| 2 | `set-2/practice-set-2.csv` | 100 | [ ] | [ ] |
| 3 | `set-3/practice-set-3.csv` | 100 | [ ] | [ ] |
| 4 | `set-4/practice-set-4.csv` | 100 | [ ] | [ ] |
| 5 | `set-5/practice-set-5.csv` | 100 | [ ] | [ ] |
| 6 | `set-6/practice-set-6.csv` | 100 | [ ] | [ ] |

Upload each CSV separately, not the ZIP, Markdown files, or manifest.

## Preview checks for every test

- [ ] Exactly 100 single-answer multiple-choice questions, four options each.
- [ ] Section counts of **30 / 35 / 20 / 15**.
- [ ] Exactly one correct selection, matching the offline review copy.
- [ ] No empty fifth or sixth option appears after import.
- [ ] Explanations, punctuation, and source links display correctly.
- [ ] Answers are not inadvertently inserted into learner-visible question text.
- [ ] Suggested custom duration of 160 minutes is labeled as practice guidance, not official timing.
- [ ] Any 80% practice target is not described as Google's passing threshold.

## Troubleshooting

| Issue | Check |
|---|---|
| Import rejects file | Latest header, required fields, supported type values, encoding, and row-level error report |
| Shifted columns | Preserve CSV quoting; do not manually split lines on commas |
| Wrong key | Keys are 1-based numeric positions; regenerate if options are reordered |
| Fewer questions imported | Resolve rejected rows before publication |
| Corrupted characters | Keep UTF-8 encoding; prefer the original generated file |

Edit `04-resources/bank.py`, then rebuild, validate, test, package, and preview the revised import. Do not independently edit shuffled keys.

## Sign-off

- [ ] Subject-matter review complete.
- [ ] All six imports previewed.
- [ ] Listing accurate and disclosures retained.
- [ ] Current platform requirements satisfied.
- [ ] Source and published version retained.

Reviewer: ____________________  Review date: ____________________

Publication version/date: ____________________
