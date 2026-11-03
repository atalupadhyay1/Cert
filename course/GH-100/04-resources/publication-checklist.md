# ✅ Publication & QA Checklist — Exam GH-100 (`6 × 100 = 600` Questions)

## 1. Automated Verification Gates (All Must Pass `0` Errors)

- [x] `python3 course/GH-100/04-resources/build.py` — Deterministically compiles `practice-set-{1..6}.csv`, `practice-set-{1..6}.md`, and `answer-manifest.json` (`600` items).
- [x] `python3 course/GH-100/04-resources/make_sample.py` — Generates `05-sample-upload/sample-upload.csv` (`15` stratified rows: `3` per domain across Domains 1–5).
- [x] `python3 course/GH-100/04-resources/validate.py --report` — Verifies `600` unique stems (`max Jaccard 0.4595 <= 0.72`), `148/148` (`100%`) `TERMS` exercised, balanced `21/21/21/21` `A–D` distribution, `0` banned phrases, and `0` cross-course collisions across all `7,200` sibling Microsoft/GitHub items.
- [x] `python3 course/GH-100/04-resources/package.py` — Packages `GH-100-6x100.zip` (`45` files, deterministic timestamps, zero `__pycache__`).
- [x] `python3 -m unittest course/GH-100/04-resources/test_course.py -v` — Runs full unit test suite across CSVs, manifest, docs, landing page, and archive integrity.
- [x] `python3 course/check_csv_upload.py --all` & `sample-upload.csv` — Repo-wide Udemy 17-column upload verification (`162/162` CSVs).
- [x] `python3 course/check_landing_page_fields.py` — Repo-wide Udemy landing-page metadata verification (`27/27` courses).

---

## 2. Udemy Instructor Upload Steps

1. Create a **Practice Test-only course** on Udemy titled `GH-100 GitHub Administration: 6 Practice Exams (600 Qs)`.
2. Paste **Course Subtitle**, **Course Description**, **12 Learning Objectives** (`60–62` chars each), **Prerequisites**, and **Target Learners** from `01-landing-page/landing-page.md`.
3. Optional smoke test: upload `05-sample-upload/sample-upload.csv` (`15` questions) into a draft test first to preview formatting, then delete the draft test.
4. Create **6 Practice Tests**, paste each **Name** and **Full/Trimmed Description** from `01-landing-page/landing-page.md`, set timer to **100 minutes**, enable **Randomize question and answer order**, and bulk-upload `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`.
5. Configure **Welcome Message** and **Congratulations Message** under Course Messages from `01-landing-page/landing-page.md`.
