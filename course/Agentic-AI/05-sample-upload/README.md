# Quick-Smoke Udemy Sample Upload (`sample-upload.csv`)

`sample-upload.csv` contains **18 representative questions** (`3` items per domain: `2` `multiple-choice` + `1` `multi-select` across all `6` Agentic AI domains) extracted deterministically from **Mock Exam 1 (`QuantaPay Autonomous Disputes`)** by `04-resources/make_sample.py`.

## Purpose

Upload `sample-upload.csv` into a temporary Udemy Practice Test section first to verify:
1. **UTF-8 BOM (`\xef\xbb\xbf`) & LF encoding:** `→` sequence arrows, backtick code spans, and currency symbols render cleanly without mojibake.
2. **17-Column Schema:** `multiple-choice` (`4` options, `1` keyed answer) and `multi-select` (`5–6` options, `2–3` keyed answers) import with zero warnings.
3. **Explanations & Domain Tags:** Per-option rationales, overall `Skill X.Y` synthesis + HTTPS documentation URLs, and all `6` Domain labels populate Udemy's review analytics view properly.

Regenerate anytime with:

```bash
python3 course/Agentic-AI/04-resources/make_sample.py
```
