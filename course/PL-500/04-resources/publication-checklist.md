# Udemy Instructor Publication Checklist (`PL-500`)

## 1. Automated Gate Verification

- [x] `build.py` deterministically builds `6 × 100 = 600` questions across `12` full CSVs, `1` sample CSV, `6` Markdown reviewer keys, `case-studies.md`, `SUMMARY.md`, and `answer-manifest.json`.
- [x] `validate.py` reports `0` errors: UTF-8 BOM, LF line endings, 17-column header, exact `28 / 48 / 24` domain weights, exact `84 multiple-choice` (`21/21/21/21` `A/B/C/D`) + `16 multi-select` per set, `148/148` (`100%`) `TERMS` coverage, `max Jaccard = 0.5556` (`<= 0.72`), zero banned phrases, and zero Microsoft fictional company names.
- [x] `check_csv_upload.py` passes all `13` CSV files (`practice-set-{1..6}.csv`, `case-embedded-set-{1..6}.csv`, and `05-sample-upload/case-study-sample.csv`) with **zero warnings and zero notes**.
- [x] `check_landing_page_fields.py` passes `01-landing-page/landing-page.md` (Title `<= 60` chars, Subtitle `<= 120` chars, Fields 1–6, Welcome Message, Congratulations Message, and 6 Practice Test Full + Trimmed descriptions).
- [x] `test_course.py` passes all `8` end-to-end unit tests, including zero stem overlap against `PL-900`, `PL-200`, `PL-400`, `AZ-204`, `AZ-400`, `AZ-401`, and `DP-600`.
- [x] `package.py` generates deterministic `PL-500-6x100.zip`.

## 2. Udemy Publishing Steps

1. **Create Practice-Test-Only Course:** Paste Fields `1`–`6` from `01-landing-page/landing-page.md` into Udemy Course Landing Page & Intended Learners forms (confirming transparent **June 30, 2026** PL-500 retirement disclosure is visible in the description).
2. **Create 6 Practice Tests (`100 minutes` each):** Paste the Name and Trimmed/Full description for Practice Tests `1`–`6` from `01-landing-page/landing-page.md`, set time limit to `100` minutes, and bulk-upload `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` (Option B).
3. **Configure Automated Course Messages:** Paste the `Welcome Message` and `Congratulations Message` from `01-landing-page/landing-page.md` under Udemy *Communications -> Course messages*.
