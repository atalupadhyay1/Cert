# CSV format specification

## File shape

- Four domains: Data Preparation and Ingestion; Data Analysis and Presentation; Data Pipeline Orchestration; Data Management.
- One file per mock exam: `practice-set-1.csv` through `practice-set-6.csv`. There is no case-embedded variant, because this exam has no case studies.
- UTF-8 with BOM, LF line endings, comma-delimited, 17 columns, 100 data rows.
- Header order is fixed and validated; reordering is rejected.

## Columns

| # | Column | Content |
|---:|---|---|
| 1 | Question | Question stem; ends in a question mark, or in "Select two." for multi-select |
| 2 | Question Type | `multiple-choice` or `multi-select` only (Udemy importer constraint) |
| 3–4 | Answer Option 1 / Explanation 1 | First populated option and its explanation |
| 5–6 | Answer Option 2 / Explanation 2 | Second populated option and its explanation |
| 7–8 | Answer Option 3 / Explanation 3 | Third populated option and its explanation |
| 9–10 | Answer Option 4 / Explanation 4 | Fourth populated option and its explanation |
| 11–12 | Answer Option 5 / Explanation 5 | Fifth option for multi-select; blank otherwise |
| 13–14 | Answer Option 6 / Explanation 6 | Reserved; blank in this package |
| 15 | Correct Answers | One index (`1`–`4`) or a comma-separated pair (`1,5`) |
| 16 | Overall Explanation | Answer label, rationale, option meanings, exam-guide anchor, local skill, primary reference |
| 17 | Domain | Exact official domain label |

The exported header has **17 columns** because the six option/explanation pairs count as twelve fields. Validate against generated files rather than editing the header by hand.

## Item-type rules enforced

| Type | Options | Correct Answers | Extra rule |
|---|---:|---|---|
| `multiple-choice` | 4 | exactly one index, `1`–`4` | balanced across the four slots per exam |
| `multi-select` | 5 | exactly two comma-separated indices | stem must contain "Select two" matching the key |

No other item type exists in this package.

## Content rules enforced

- Four or five contiguous non-empty options; no gaps and no sixth option.
- No duplicate option text inside an item.
- Each populated option has a non-empty explanation beginning with `Correct.` or `Incorrect for this question.`
- No stem is duplicated anywhere in the bank, after casefold and punctuation stripping.
- No two stems are near-duplicates either: `build.py` compares content words across the whole bank and fails above a 0.72 Jaccard overlap, so a paraphrase of the same decision cannot ship.
- No stem or rationale contains the phrase "case study", and no overall explanation claims a case-study context.
- Every option key resolves to an entry in `terms.py`; an unknown key fails the build rather than passing silently.
- Per exam the domain counts must be exactly **30 / 27 / 18 / 25**, the per-skill counts must match `SKILL_PLAN`, and multi-select items must be spread **5 / 4 / 3 / 4** across domains 1–4.

## Blueprint note

The four published weights total exactly **100%**, so the 100-item allocation *is* the published weight for every domain. There is no rounding step and no ±1 tolerance: the build and the tests assert equality. If Google ever republishes weights that do not sum to 100, the build fails loudly rather than quietly absorbing the drift.

## Authoring source format

`questions/N.txt` holds one item per line, comments allowed:

```text
skill|kind|answer keys|distractor keys|stem|reason
```

- `kind` is `S` (single) or `M2` (two answers).
- Answer and distractor keys are comma-separated and must already exist in the option bank.
- The stem must end in `?` or `Select two.`
- The reason must be at least six words and is reused in every correct and incorrect explanation for that item.

## Why there is no case-study section in this file

The Associate Data Practitioner exam publishes 50–60 multiple choice and multiple select questions and no case-study component. A self-contained case variant, a case brief, and a case upload guide would all describe a format this exam does not use, so none of them exists in this folder. `package.py` fails if `04-resources/case-studies.md` or `04-resources/case-study-upload-guide.md` reappears.

## Regenerating

```bash
python3 build.py                 # CSVs, review copies, set READMEs, manifest
python3 make_sample.py           # 05-sample-upload/sample-upload.csv
python3 validate.py --report validation-report.json
python3 -m unittest test_course
python3 package.py
```

`build.py` refuses to run if any check in `check_source()` fails: unknown skill, wrong domain allocation, per-skill plan mismatch, wrong multi-select spread, wrong type mix, duplicate key, unknown option key, short reason, bad stem ending, case-study wording, or duplicate stem.
