# Udemy Publication Checklist — Microsoft Exam AZ-400 (6 × 100 = 600 Questions)

Use this step-by-step checklist when publishing the **AZ-400: Designing and Implementing Microsoft DevOps Solutions** practice-test course on Udemy.

## 1. Pre-Upload Verification Gates

- [x] **600 Unique Original Questions:** `6` sets × `100` questions (`0` duplicates; max stem Jaccard similarity `0.6364 <= 0.72`).
- [x] **Official July 27, 2026 Weight Alignment:** `12 / 13 / 52 / 14 / 9` inside `10–15% / 10–15% / 50–55% / 10–15% / 5–10%` on every set.
- [x] **13 CSVs Validated:** UTF-8 BOM, LF line endings, 17 columns, contiguous options, `21 A / 21 B / 21 C / 21 D` single-choice slot balance, zero banned phrases.
- [x] **Mandatory Landing-Page Fields Populated:** `What will students learn` (10 concise bullets), `Requirements` (4 bullets), and `Who is this course for` (4 bullets) verified via `course/check_landing_page_fields.py`.
- [x] **Transparent Lifecycle & Prerequisite Disclosures:** States `July 27, 2026` study guide, `AZ-104` / pre-retirement `AZ-204` Expert prerequisite, `February 1, 2027` scheduled retirement, `AZ-401` successor, and `700 / 1000` scaled passing score.

## 2. Udemy Curriculum Setup Steps

1. Create a new **Practice TestOnly** course in Udemy Instructor Dashboard and paste metadata from `01-landing-page/landing-page.md`.
2. Smoke-test CSV import by uploading `05-sample-upload/case-study-sample.csv` (`12` rows) into Practice Test 1, verifying `→` arrows, backticks, and explanations render cleanly, then replace with the full 100-item CSV.
3. For each Practice Test `N` (`1..6`):
   - **Title:** Copy from `02-curriculum/curriculum-outline.md`
   - **Bulk Upload CSV:** `03-practice-sets/set-N/case-embedded-set-N.csv` (recommended so Udemy question randomization keeps every case study self-contained)
   - **Duration:** `100 minutes`
   - **Minimum Score to Pass (Practice Target):** `80%` (remind learners in the test description that Microsoft's live exam uses a `700 / 1000` scaled score)
   - **Randomize Question & Answer Order:** Enabled
4. Preview all 6 practice tests in Student View and submit for Udemy Quality Review.
