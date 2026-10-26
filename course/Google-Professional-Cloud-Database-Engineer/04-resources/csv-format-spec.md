# CSV format specification

## File shape

- Four domains: design; manage across database technologies; migrate; deploy.
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
- Every populated option has an explanation; an option without one fails validation.
- The stem ends in `?` or in `Select two.`, and a multi-select stem must state the selection count.
- The overall explanation must cite the exam-guide section (`sources.GUIDE`) and the domain reference.
- No stem or explanation may contain the phrase `case study`; `build.py`, `validate.py`, and `package.py` each reject it.
- No stem or explanation may become a console recipe: the test suite rejects `click`, `navigate to`, and `in the console, select`. Configuration items describe a choice and its consequence.
- No arrow character may appear in an option; this exam publishes no sequencing item type.
- Stems must be unique across all 600 items, and no pair of stems may exceed 0.72 token overlap on content words.

## Authoring source

Items are authored in `04-resources/questions/1.txt` … `6.txt`, one row per item, pipe-delimited:

```text
skill|kind|answer keys|distractor keys|stem|reason
```

`S` is one answer plus three distractors; `M2` is two answers plus three distractors and requires "Select two." in the stem. Option text lives in `terms.py` and is never written into the CSV by hand, so a label change propagates to every set on the next build. Every option is a product choice or an operational action, so an item can ask what a team should decide rather than what a term means.

## Regenerating

```bash
cd course/Google-Professional-Cloud-Database-Engineer/04-resources
python3 build.py                                      # writes the six CSVs, review copies, manifest
python3 make_sample.py                                # rebuilds the 8-item sample
python3 validate.py --report validation-report.json   # rewrites the validation report
```

Do not hand-edit a generated CSV. Edit the authored row, then rebuild; the tests compare each CSV against the builder output and fail on drift.
