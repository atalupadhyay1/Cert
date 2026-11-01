# ✅ Udemy Publication Checklist — Microsoft Exam DP-300 (`6 × 100 = 600` Questions)

Step-by-step verification and publishing workflow for **DP-300 Azure SQL Admin: 6 Full-Length Practice Exams (600Q)**.

---

## 1. Pre-Upload Automated Gate Checks

Run all verification suites from `/home/user/Cert` and confirm zero errors:

- [x] `python3 course/DP-300/04-resources/build.py` — regenerates all 12 practice/embedded CSVs, 6 Markdown review sets, `answer-manifest.json`, `case-studies.md`, and `case-study-sample.csv`
- [x] `python3 course/DP-300/04-resources/validate.py --report` — `0` errors across 13 CSVs, `187 / 187` (`100.0%`) terms exercised, max Jaccard `0.552 <= 0.72`, `0` collisions against `6,000` sibling Microsoft items
- [x] `python3 course/DP-300/04-resources/package.py` — packages `course/DP-300/DP-300-6x100.zip`
- [x] `python3 -m unittest discover -s course/DP-300/04-resources -p 'test_*.py' -v` — all 7 unit tests pass
- [x] `python3 course/check_csv_upload.py --all` — repo-wide CSV upload validator passes (`150 / 150` full-set CSVs)
- [x] `python3 course/check_landing_page_fields.py` — repo-wide landing-page validator passes (`25 / 25` courses)

---

## 2. Udemy Course Shell Setup (`01-landing-page/landing-page.md`)

1. Create a **Practice Test Only** course on Udemy.
2. Paste **Field 1 (Course Title)** (`59` chars): `DP-300 Azure SQL Admin: 6 Full-Length Practice Exams (600Q)`
3. Paste **Field 2 (Course Subtitle)** (`98` chars): `600 original questions • Azure SQL DB, SQL MI, SQL VMs, T-SQL, Security, Tuning & HA/DR • Oct 2026`
4. Paste **Field 3 (Course Description)**, **Field 4 (10 learning objectives, 60–69 chars each)**, **Field 5 (Requirements)**, and **Field 6 (Target Audience)**.
5. Paste the **Welcome Message** and **Congratulations Message** under *Course Messages*.

---

## 3. Creating & Uploading the Six Practice Tests

For each exam `N` in `1..6`:

1. Add Practice Test `N` and paste the **Name** and **Full description** (or **Trimmed description** `<= 200` chars where constrained) from `01-landing-page/landing-page.md`.
2. Set **Time limit** = `100 minutes`, **Minimum score to pass** = `80%` (Sets 1–3) / `82%` (Set 4) / `85%` (Sets 5–6), and **Randomize question & answer order** = `ON`.
3. Click **Bulk Upload Questions** and upload `03-practice-sets/set-N/case-embedded-set-N.csv` (smoke-test first with `05-sample-upload/case-study-sample.csv` if desired).
4. Spot-check 2 standalone items, 1 `____` code-completion item, 1 `→` sequence item, and 1 `Case study — ...` item in Udemy's previewer before publishing.
