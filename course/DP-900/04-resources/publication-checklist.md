# Udemy Publication Checklist — `DP-900: Microsoft Azure Data Fundamentals`

- [x] **1. Automated Build, Validation & Repo-Wide Gates Passed:**
  - `python3 course/DP-900/04-resources/build.py`
  - `python3 course/DP-900/04-resources/make_sample.py`
  - `python3 course/DP-900/04-resources/validate.py --report` (`600` unique Qs, `143/143` terms, max Jaccard `0.542`)
  - `python3 course/DP-900/04-resources/package.py` (`DP-900-6x100.zip`)
  - `python3 course/DP-900/04-resources/test_course.py` (`6/6` unit tests passing)
  - `python3 course/check_csv_upload.py --all`
  - `python3 course/check_landing_page_fields.py DP-900`
- [x] **2. Smoke-Test Import Verified (`05-sample-upload/sample-upload.csv`):**
  - Upload `sample-upload.csv` (`12` rows — `3` per domain, mixing `multiple-choice` and `multi-select`) into a draft Udemy Practice Test to confirm clean UTF-8 rendering before bulk-uploading all 6 exams.
- [x] **3. Course Landing Page Metadata Copied (`01-landing-page/landing-page.md`):**
  - Title (`55` chars <= `60`), Subtitle (`98` chars <= `120`), Description (July 21, 2026 blueprint, closed-book 45-minute format, lifetime validity, `700 / 1000` scaled score), `12` concise `59–62`-char learning bullets, Prerequisites, Target Audience, `Welcome Message`, and `Congratulations Message`.
- [x] **4. Six Full-Length Practice Tests Uploaded (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`):**
  - Copy each exam's Name and Full/Trimmed Description from `01-landing-page/landing-page.md`.
  - Set timer = **`75` minutes** (`45 sec/question` live pace) and passing benchmark = **`75%`** (with explicit disclaimer that raw percentages do not equal Microsoft's `700 / 1000` scaled score).
  - Enable both **Randomize Question Order** and **Randomize Answer Order** (live DP-900 has zero case studies, so every item is completely standalone).
