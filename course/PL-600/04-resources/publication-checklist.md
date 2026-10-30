# Instructor Publication Checklist (`PL-600`)

Run through these steps before publishing **PL-600 Power Platform Architect: 6 Practice Exams (600 Q)** on Udemy:

- [x] **1. Automated Validation & Unit Tests Pass (`0` errors, `0` notes):**
  - `python3 course/PL-600/04-resources/build.py`
  - `python3 course/PL-600/04-resources/validate.py --report`
  - `python3 course/PL-600/04-resources/package.py`
  - `python3 course/PL-600/04-resources/test_course.py`
  - `python3 course/check_csv_upload.py --all`
  - `python3 course/check_landing_page_fields.py PL-600`
- [x] **2. Mandatory Udemy Landing-Page Copy Populated (`01-landing-page/landing-page.md`):**
  - Course Title (`<= 60` chars) & Subtitle (`<= 120` chars)
  - Course Description disclosing the **September 23, 2024** final blueprint (`46 / 37 / 17`), **`PL-200` / `PL-400` prerequisite**, **June 30, 2026** retirement, **Exam AB-100** successor credential, and honest platform boundaries
  - 10 concise "What will students learn" bullets (`57–61` chars each)
  - Course Requirements/Prerequisites & Target Audience
  - Welcome Message & Congratulations Message configured in Udemy Course Messages
- [x] **3. Smoke-Test Import (`05-sample-upload/case-study-sample.csv`):**
  - Verified 12-row sample CSV imports cleanly with inline `[Case Study — <Name>]` briefs.
- [x] **4. Six Full-Length Practice Tests Uploaded (`03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`):**
  - Recommended time limit per exam: **`100 minutes`**
  - Question & answer randomization: **Enabled** (safe with `case-embedded-set-{1..6}.csv`)
  - Suggested self-study target: **`80%`**, paired with explicit note that raw Udemy percentages never equate to Microsoft's `700 / 1000` scaled score.
