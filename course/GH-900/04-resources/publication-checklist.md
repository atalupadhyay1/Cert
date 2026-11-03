# Udemy Publication Checklist — `GH-900: GitHub Foundations`

- [x] **1. Automated Build, Validation & Repo-Wide Gates Passed:**
  - `python3 course/GH-900/04-resources/build.py`
  - `python3 course/GH-900/04-resources/make_sample.py`
  - `python3 course/GH-900/04-resources/validate.py --report` (`600` unique Qs, `169/169` terms, max Jaccard `0.5263`)
  - `python3 course/GH-900/04-resources/package.py` (`GH-900-6x100.zip`)
  - `python3 course/GH-900/04-resources/test_course.py` (`6/6` unit tests passing)
  - `python3 course/check_csv_upload.py --all`
  - `python3 course/check_landing_page_fields.py GH-900`
- [x] **2. Smoke-Test Import Verified (`05-sample-upload/sample-upload.csv`):**
  - Upload `sample-upload.csv` (`14` rows — `2` per domain across all 7 domains, `1` `multiple-choice` + `1` `multi-select` per domain) into a draft Udemy Practice Test to confirm clean UTF-8 rendering before bulk-uploading all 6 exams.
- [x] **3. Course Landing Page Metadata Copied (`01-landing-page/landing-page.md`):**
  - Title (`59` chars <= `60`), Subtitle (`97` chars <= `120`), Description (January 2026 blueprint, closed-book 100-minute format, lifetime validity without renewal, `700 / 1000` scaled score), `12` concise `59–61`-char learning bullets, Prerequisites, Target Audience, `Welcome Message`, and `Congratulations Message`.
- [x] **4. Six Full-Length Practice Tests Uploaded (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`):**
  - Copy each exam's Name and Full/Trimmed Description from `01-landing-page/landing-page.md`.
  - Set timer = **`100` minutes** (matching the official 100-minute GH-900 exam duration) and passing benchmark = **`75%`** (with explicit disclaimer that raw percentages do not equal Microsoft's `700 / 1000` scaled score).
  - Enable both **Randomize Question Order** and **Randomize Answer Order** (live GH-900 has zero case studies, so every item is completely standalone).
