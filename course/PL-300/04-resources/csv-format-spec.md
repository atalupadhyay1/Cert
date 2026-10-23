# CSV format specification

## File shape

- Four domains: prepare the data, model the data, visualize and analyze the data, and manage and secure Power BI.
- One file per mock exam: `practice-set-1.csv` through `practice-set-6.csv`.
- UTF-8 with BOM, LF line endings, comma-delimited, 17 columns, 100 data rows.
- Header order is fixed and validated; reordering is rejected.

## Columns

| # | Column | Content |
|---:|---|---|
| 1 | Question | Question stem; ends in a question mark, or in "Select two." / "Select three." for multi-select |
| 2 | Question Type | `multiple-choice` or `multi-select` only (Udemy importer constraint) |
| 3–4 | Answer Option 1 / Explanation 1 | First populated option and its explanation |
| 5–6 | Answer Option 2 / Explanation 2 | Second populated option and its explanation |
| 7–8 | Answer Option 3 / Explanation 3 | Third populated option and its explanation |
| 9–10 | Answer Option 4 / Explanation 4 | Fourth populated option and its explanation |
| 11–12 | Answer Option 5 / Explanation 5 | Fifth option for multi-select; blank otherwise |
| 13–14 | Answer Option 6 / Explanation 6 | Reserved; blank in this package |
| 15 | Correct Answers | One index (`1`–`4`) or a comma-separated list (`2,4`) |
| 16 | Overall Explanation | Answer label, case rationale, definition, study-guide anchor, local skill, primary reference |
| 17 | Domain | Exact official domain label |

The exported header has **17 columns** because the six option/explanation pairs count as twelve fields. Validate against generated files rather than editing the header by hand.

## Item-type rules enforced

| Type | Options | Correct Answers | Extra rule |
|---|---:|---|---|
| `multiple-choice` | 4 | exactly one index, `1`–`4` | balanced across the four slots per exam |
| `multi-select` | 5 | two comma-separated indices in this package | stem must contain "Select two" matching the key |
| sequencing (exported as `multiple-choice`) | 4 | exactly one index, `1`–`4` | every option must contain `→`, because each option is a candidate sequence |

## Content rules enforced

- Four or five contiguous non-empty options; no gaps and no sixth option.
- No duplicate option text inside an item.
- Each populated option has a non-empty explanation beginning with `Correct.` or `Incorrect for this question.`
- Multi-select items mark every keyed option as `Correct.`
- Overall explanation contains the official PL-300 study-guide anchor, the local skill, and a primary reference.
- Domain label must match the authored source and the per-exam allocation (28/28/28/16).
- 100 unique normalized stems per exam and 600 across the package.
- 84 single-answer keys (76 multiple-choice plus 8 sequencing, all exported as multiple-choice) distributed across slots 1–4 with a max-minus-min of at most one.

## Reading and scoring multi-select items

`Correct Answers = 3,5` means options 3 and 5 are required. There is no partial credit: an answer missing one key or containing an extra key is incorrect. The stem always states the count, so scoring code can reject an answer with the wrong number of selections before comparing indices.

## Reading sequencing items

Each option is a full candidate sequence using `→` between steps, for example:

```text
Profile the column → correct the data type → shape the table → load only needed columns
```

Each option is a complete candidate sequence and exactly one is in the correct order. These items are exported with `Question Type` set to `multiple-choice` because the importer accepts no other single-answer label. The others are plausible reorderings, usually by moving the step that logically cannot move — profiling before shaping, typing before loading, testing a role before release.

## Case-study text

Case-study scenarios are authored in `cases.py` and injected at build time; never hand-edit the generated copies.

- `practice-set-N.md` prints the scenario above the three questions of its case.
- `case-studies.md` collects all 24 scenarios with questions and answer letters.
- `case-embedded-set-N.csv` (built with `--embed-case`) repeats the scenario in every case-item stem and keeps the same answer keys.

`build.py` fails if a `Case study — <Name>:` stem has no scenario in `cases.py`, or if a scenario is never used.

## Editing workflow

1. Edit the authored source in `04-resources/questions/1.txt`–`6.txt`, never the generated CSV.
2. Run `python 04-resources/build.py`.
3. Run `python 04-resources/validate.py --report 04-resources/validation-report.json`.
4. Run `python 04-resources/package.py` only after validation passes.
5. Re-run the unittest suite and inspect the platform import preview.

Do not open and resave CSVs in spreadsheet software without checking encoding, line endings, option order, and formula-like text.
