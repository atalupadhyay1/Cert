# CSV format specification

## File shape

- Six domains: designing and planning, managing and provisioning, security and compliance, analyzing and optimizing, managing implementation, and solution and operations excellence.
- One file per mock exam: `practice-set-1.csv` through `practice-set-6.csv`, plus a self-contained `case-embedded-set-N.csv`.
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
| 15 | Correct Answers | One index (`1`–`4`) or a comma-separated pair (`1,4`) |
| 16 | Overall Explanation | Answer label, case rationale, option meanings, exam-guide anchor, local skill, primary reference |
| 17 | Domain | Exact official domain label |

The exported header has **17 columns** because the six option/explanation pairs count as twelve fields. Validate against generated files rather than editing the header by hand.

## Item-type rules enforced

| Type | Options | Correct Answers | Extra rule |
|---|---:|---|---|
| `multiple-choice` | 4 | exactly one index, `1`–`4` | balanced across the four slots per exam |
| `multi-select` | 5 | exactly two comma-separated indices | stem must contain "Select two" matching the key |
| sequencing (exported as `multiple-choice`) | 4 | exactly one index, `1`–`4` | every option must contain `→`, because each option is a candidate order |

## Content rules enforced

- Four or five contiguous non-empty options; no gaps and no sixth option.
- No duplicate option text inside an item.
- Each populated option has a non-empty explanation beginning with `Correct.` or `Incorrect for this question.`
- No stem is duplicated anywhere in the bank, after casefold and punctuation stripping.
- Every option key resolves to an entry in `terms.py` or `sequences.py`; an unknown key fails the build rather than passing silently.

## Authoring source format

`questions/N.txt` holds one item per line, comments allowed:

```text
skill|kind|answer keys|distractor keys|stem|reason
```

- `kind` is `S` (single), `M2` (two answers) or `O` (ordering).
- Answer and distractor keys are comma-separated and must already exist in the option bank.
- The stem must end in `?` or `Select two.`
- The reason must be at least six words and is reused in every correct and incorrect explanation for that item.

## Sequencing items

Each sequencing item offers four complete candidate orders and exactly one is correct. All four options contain `→`. The distractors are plausible reorderings, usually created by moving the step that logically cannot move — inventory before waves, keys before encryption, plan before apply, or recovery before root-cause analysis. They are exported as `multiple-choice` because the importer accepts no other single-answer label.

## Case-study items

A case item's stem begins `Case study — <Scenario>: `. The scenario text lives once in `cases.py` and is published three ways: printed once per block in the review copy, repeated in each stem in the `case-embedded` variant, and listed in `case-studies.md`. All 24 scenarios are original; the four official Google case studies are named in the documentation but never reproduced.

## Regenerating

```bash
python3 build.py                 # CSVs, review copies, set READMEs, manifest
python3 build.py --embed-case    # self-contained case variants
python3 make_sample.py           # 05-sample-upload/case-study-sample.csv
python3 validate.py --report validation-report.json
python3 -m unittest test_course
python3 package.py
```

`build.py` refuses to run if any check in `check_source()` fails: unknown skill, wrong domain allocation, wrong type mix, wrong case count, duplicate key, unknown option key, short reason, bad stem ending, or duplicate stem.
