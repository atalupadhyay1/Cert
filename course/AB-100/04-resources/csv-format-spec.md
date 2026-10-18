# 📄 AB-100 CSV Format Spec (Udemy v2 Bulk Question Uploader)

This is the v2 Bulk Question Upload Template format used by all AB-100 practice sets. Drop the CSV straight into Udemy's importer — no manual editing required.

## Column order (17 columns, exact)

| # | Column | Required | Notes |
|---|---|---|---|
| 1 | `Question` | Yes | The question text. |
| 2 | `Question Type` | Yes | Exactly `multiple-choice` or `multi-select` (no hyphen in the type name, lowercase). |
| 3 | `Answer Option 1` | Yes | First option text. |
| 4 | `Explanation 1` | Yes | One-sentence explanation of why option 1 is right OR why it is wrong. |
| 5 | `Answer Option 2` | Yes | Second option text. |
| 6 | `Explanation 2` | Yes | One-sentence explanation. |
| 7 | `Answer Option 3` | Yes | Third option text. |
| 8 | `Explanation 3` | Yes | One-sentence explanation. |
| 9 | `Answer Option 4` | Yes | Fourth option text. |
| 10 | `Explanation 4` | Yes | One-sentence explanation. |
| 11 | `Answer Option 5` | Optional | Fifth option text. |
| 12 | `Explanation 5` | Optional | One-sentence explanation. |
| 13 | `Answer Option 6` | Optional | Sixth option text. |
| 14 | `Explanation 6` | Optional | One-sentence explanation. |
| 15 | `Correct Answers` | Yes | 1-based comma-separated indices. `2` for single-answer multiple-choice; `1,3,4` for multi-select. |
| 16 | `Overall Explanation` | Yes | Comprehensive explanation that links to a Microsoft Learn reference URL. |
| 17 | `Domain` | Yes | Exactly one of the three AB-100 domain strings (see below). |

## Question Type

- `multiple-choice` — exactly one correct option (single 1-based index in `Correct Answers`, e.g. `3`).
- `multi-select` — two or more correct options (comma-separated 1-based indices in `Correct Answers`, e.g. `1,3,4`).

## AB-100 Domain strings (case-sensitive, exact match)

Use exactly one of these three values in column 17:

- `Plan AI-powered Business Solutions`
- `Design AI-powered Business Solutions`
- `Deploy AI-powered Business Solutions`

These match the official study guide wording (the words `AI-powered` are hyphenated and `Business Solutions` is capitalized).

## Per-option inline explanations

Every option (correct and wrong) gets a one-sentence explanation in its `Explanation N` column. For the **correct** option the explanation is the "why this is right" sentence. For **distractors** it is the "why this is wrong / what it really is" sentence. The Overall Explanation then ties it together and links to a Microsoft Learn reference URL.

## Microsoft Learn reference URL

Every question's `Overall Explanation` (or any per-option explanation) must contain at least one `https://learn.microsoft.com/...` URL. The validator checks for this.

## Row format (typical)

```csv
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
Which Microsoft framework should you follow when designing an AI adoption strategy for an enterprise?,"multiple-choice",Azure DevOps,"Azure DevOps is for build and release pipelines, not AI adoption strategy.",Cloud Adoption Framework for Azure,"The Cloud Adoption Framework for Azure is the canonical starting point for AI adoption strategy.",Microsoft Power Platform Well-Architected Framework,"The Power Platform Well-Architected Framework covers intelligent application workloads but is narrower than the Cloud Adoption Framework.",Azure Architecture Center,"The Azure Architecture Center is reference architecture patterns, not an adoption framework.",,,,,,"2","Cloud Adoption Framework for Azure is the correct answer because it provides the Strategy, Plan, Ready, Adopt, Govern, and Manage phases for AI adoption. Reference: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/","Plan AI-powered Business Solutions"
```

## Common mistakes to avoid

- ❌ Using "multi-select" as a Question Type but only putting one number in `Correct Answers`. (Use a 1-based comma-separated list.)
- ❌ Leaving `Correct Answers` blank or non-numeric.
- ❌ Putting text in `Correct Answers` instead of 1-based indices.
- ❌ Spelling the domain string slightly differently (`Plan AI Powered Business Solutions` — wrong; `Plan AI-powered Business Solutions` — correct).
- ❌ Including URLs that are not from `learn.microsoft.com`.
- ❌ Using 0-based indices in `Correct Answers` (Udemy expects 1-based).
- ❌ Using more than 6 options (Udemy's max is 6).

## How the validator enforces this spec

`validate_csv.py` enforces every check above. Run it after building each set:

```bash
python validate_csv.py ../03-practice-sets/set-1/practice-set-1.csv
```
