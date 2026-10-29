# Udemy Publication Checklist — Exam PL-400 (`6 × 100 = 600` Questions)

1. **Course Metadata (`01-landing-page/landing-page.md`):**
   - [x] Paste **Course Title** (`58` chars `<= 60`).
   - [x] Paste **Course Subtitle** (`94` chars `<= 120`).
   - [x] Paste **Course Description** (discloses October 16, 2026 blueprint, October 30, 2026 PL-400 -> AB-400 transition, `700 / 1000` scaled score, no prerequisite exam, and Udemy CSV adaptations).
   - [x] Paste **What will students learn** (`12` concise bullets), **Requirements / Prerequisites** (`3` bullets), and **Who this course is for** (`4` bullets).
   - [x] Paste **Welcome Message** and **Congratulations Message** in Udemy Course Messages.

2. **Six Practice Test Uploads (`03-practice-sets/set-{1..6}/`):**
   - [x] Create Practice Tests 1–6 using the exact **Name** and **Full / Trimmed description** (`<= 200` chars) in `01-landing-page/landing-page.md`.
   - [x] Set timing to **100 minutes** per test.
   - [x] Upload **`case-embedded-set-{1..6}.csv`** (recommended when randomization is enabled) or `practice-set-{1..6}.csv` (sequential mode only).

3. **Automated Quality Gates Verified:**
   - [x] `python3 course/PL-400/04-resources/build.py` (`600` questions generated)
   - [x] `python3 course/PL-400/04-resources/validate.py --report course/PL-400/04-resources/validation-report.json` (`0` errors, `170/170` terms exercised, max Jaccard `0.6818 <= 0.72`)
   - [x] `python3 course/PL-400/04-resources/package.py` (`PL-400-6x100.zip` packaged)
   - [x] `python3 -m unittest discover -s course/PL-400/04-resources -p 'test_*.py' -v`
   - [x] `python3 course/check_csv_upload.py --all`
   - [x] `python3 course/check_landing_page_fields.py`
