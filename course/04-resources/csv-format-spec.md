# CSV Format Specification — Udemy v2 Bulk Question Upload Template

> This is the format every practice set CSV in this course follows. Drop the CSV straight into Udemy's **Bulk Question Upload** importer — no manual editing required.

---

## 📋 Column order (17 columns, exact order)

| # | Column | Required? | Notes |
|---|---|---|---|
| 1 | `Question` | Yes | The question text |
| 2 | `Question Type` | Yes | `multiple-choice` (single answer) or `multi-select` (choose all that apply) |
| 3 | `Answer Option 1` | Yes | First option text |
| 4 | `Explanation 1` | Yes | Why option 1 is correct or incorrect (one sentence) |
| 5 | `Answer Option 2` | Yes | Second option text |
| 6 | `Explanation 2` | Yes | Why option 2 is correct or incorrect |
| 7 | `Answer Option 3` | Yes | Third option text |
| 8 | `Explanation 3` | Yes | Why option 3 is correct or incorrect |
| 9 | `Answer Option 4` | Yes | Fourth option text |
| 10 | `Explanation 4` | Yes | Why option 4 is correct or incorrect |
| 11 | `Answer Option 5` | Optional | Fifth option text (used for multi-select) |
| 12 | `Explanation 5` | Optional | Why option 5 is correct or incorrect |
| 13 | `Answer Option 6` | Optional | Sixth option text (used for multi-select) |
| 14 | `Explanation 6` | Optional | Why option 6 is correct or incorrect |
| 15 | `Correct Answers` | Yes | Comma-separated, 1-based option indices. e.g. `2` or `1,3,4` |
| 16 | `Overall Explanation` | Yes | Comprehensive explanation of the answer, with a Microsoft Learn reference URL |
| 17 | `Domain` | Yes | One of the three AB-900 skills measured (see below) |

---

## 🎯 Question Type values

| Value | Use case |
|---|---|
| `multiple-choice` | Single correct answer. Correct Answers column has one index (e.g. `2`). |
| `multi-select` | Multiple correct answers. Correct Answers column has multiple comma-separated indices (e.g. `1,3,4`). |

---

## 🌐 AB-900 Domain values (exact strings, case-sensitive)

Use **exactly** one of these three strings for the `Domain` column:

1. `Identify the Core Features and Objects of Microsoft 365 Services`
2. `Understand Data Protection and Governance Tasks for Microsoft 365 and Copilot`
3. `Perform Basic Administrative Tasks for Copilot and Agents`

> These strings are matched against the official AB-900 study guide (skills measured as of October 14, 2026) and verified by the `validate_csv.py` script.

---

## ✅ Per-option explanation rules

For every option, write one sentence explaining **why** it is correct (if it's the right answer) or **why it is wrong** (if it's a distractor). A good explanation is:

- **Specific** — names the exact rule, threshold, or feature being tested
- **Comparable** — explains how the distractor relates to the correct answer ("X does Y, while Z does W")
- **Memorable** — uses the precise Microsoft Learn terminology so the candidate remembers it

### ✅ Good example
```
Question: Which Microsoft Purview feature prevents sensitive data from being shared via email?
A) Microsoft Purview DLP — correct. DLP policies detect sensitive data and block email sends that violate policy.
B) Microsoft Purview Information Protection — close, but IP provides classification (labels) and protection, not block-on-transit.
C) Microsoft Purview Insider Risk Management — detects risky user behavior, not data-in-transit blocking.
D) Microsoft Purview Communication Compliance — monitors communications for policy violations, not real-time DLP blocking.
Correct Answers: 1
```

### ❌ Bad example
```
A) Microsoft Purview DLP — correct.
B) Microsoft Purview Information Protection — wrong.
C) Microsoft Purview Insider Risk Management — wrong.
D) Microsoft Purview Communication Compliance — wrong.
```

---

## 🔗 Microsoft Learn URL requirement

Every question's `Overall Explanation` **must** include a `https://learn.microsoft.com/...` URL. The validator enforces this.

Common URL patterns used in this course:

- `https://learn.microsoft.com/en-us/microsoft-365/admin/...`
- `https://learn.microsoft.com/en-us/microsoft-365/...`
- `https://learn.microsoft.com/en-us/exchange/...`
- `https://learn.microsoft.com/en-us/sharepoint/...`
- `https://learn.microsoft.com/en-us/microsoftteams/...`
- `https://learn.microsoft.com/en-us/entra/...`
- `https://learn.microsoft.com/en-us/purview/...`
- `https://learn.microsoft.com/en-us/copilot/...`
- `https://learn.microsoft.com/en-us/defender-xdr/...`
- `https://learn.microsoft.com/en-us/power-platform/admin/...`

---

## 📐 Multiple-choice vs multi-select layout

| Question type | Options | Correct Answers format |
|---|---|---|
| `multiple-choice` | 4 options (A–D) | `2` |
| `multiple-choice` | 5 options (A–E) | `3` |
| `multi-select` | 4 options, 2 correct | `1,3` |
| `multi-select` | 5 options, 3 correct | `1,3,5` |

---

## 🧪 Validation

Run `python validate_csv.py <file.csv>` to verify a CSV before uploading to Udemy.
