# Udemy Bulk-Upload CSV Format Specification (`Agentic-AI`)

Every CSV file produced in `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` and `05-sample-upload/sample-upload.csv` strictly conforms to Udemy's 17-column practice-test import specification and passes both `04-resources/validate.py` and the repository-wide `course/check_csv_upload.py` validator.

## 1. File-Level Encoding & Delimiters

- **Encoding:** `UTF-8 with BOM` (`\xef\xbb\xbf` leading bytes so Excel and Udemy's parser never mojibake `→`, `×`, `€`, or `§`).
- **Line endings:** Unix `LF` (`\n`) only — zero `CR` or `CRLF` bytes.
- **Quoting:** `csv.QUOTE_MINIMAL` (RFC 4180 compliant).
- **Row count:** `1` header row + `100` question rows = `101` records per full mock exam (`1` header + `18` rows = `19` records in `sample-upload.csv`).

## 2. Exact 17-Column Header Schema

| Col # | Header Name | Rules Enforced by `build.py` & `validate.py` |
| :---: | :--- | :--- |
| 1 | `Question` | Non-empty scenario stem (`<= 540` chars in source, well within Udemy limits); includes `"Select two."` on `M2` and `"Select three."` on `M3`. |
| 2 | `Question Type` | Strictly `multiple-choice` (`84` rows/set) or `multi-select` (`16` rows/set). |
| 3 | `Answer Option 1` | Non-empty (`<= 245` chars), contiguous options from slot 1 upward. |
| 4 | `Explanation 1` | Non-empty (`Correct. ...` or `Incorrect. ...`, `<= 560` chars). |
| 5 | `Answer Option 2` | Non-empty. |
| 6 | `Explanation 2` | Non-empty. |
| 7 | `Answer Option 3` | Non-empty. |
| 8 | `Explanation 3` | Non-empty. |
| 9 | `Answer Option 4` | Non-empty (`all multiple-choice rows stop at Option 4`). |
| 10 | `Explanation 4` | Non-empty. |
| 11 | `Answer Option 5` | Populated on `5`- and `6`-option `multi-select` rows; empty on `multiple-choice` rows. |
| 12 | `Explanation 5` | Populated iff `Answer Option 5` is non-empty. |
| 13 | `Answer Option 6` | Populated on `6`-option `multi-select` (`M3`) rows; empty otherwise. |
| 14 | `Explanation 6` | Populated iff `Answer Option 6` is non-empty. |
| 15 | `Correct Answers` | 1-based sorted comma-separated indices (`1`..`4` for `multiple-choice` balanced `21/21/21/21`; `2` or `3` indices for `multi-select`). |
| 16 | `Overall Explanation` | Synthesizes why the keyed option(s) win, names the exact `Skill X.Y`, and cites two authoritative `https://` primary reference URLs. |
| 17 | `Domain` | Exact match to one of the 6 consolidated Agentic AI domain titles. |

## 3. Interactive Item-Pattern Approximations in Udemy CSV

- **Code / Protocol / CLI Slot Completions (`____`):** `23–31` items per set test `LangGraph` `interrupt()`/`Send()`/`Annotated` reducers, `MCP 2026-07-28` headers & OAuth 2.1, `A2A v1.0` `/.well-known/agent-card.json`, `NVIDIA NIM` / `vLLM` flags, `OpenTelemetry` `gen_ai.agent.*` attributes, `OPA` policies, and `Pass^k` math.
- **Ordered 4-Step Sequences (`→`):** `8` items per set (`kind = O`) present four 4-step lifecycle pipelines rendered as `multiple-choice` options (`Step 1 → Step 2 → Step 3 → Step 4`).
- **Architecture Evaluations (`Proposed solution:`):** `6–8` items per set state a concrete problem + `Proposed solution:` + `Does this meet the goal?` (`mixing valid sol_yes architectures and specific sol_no_* failure diagnoses — never bare Yes/No options`).
