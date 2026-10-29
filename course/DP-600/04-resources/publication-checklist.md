# ✅ Udemy Publication Checklist — Microsoft Exam DP-600 (`6 × 100 = 600` Questions)

Step-by-step verification and publishing workflow for **DP-600 Microsoft Fabric: 6 Full-Length Practice Exams (600Q)**.

---

## 1. Pre-Upload Automated Gate Checks

Run all four verification suites from `/home/user/Cert` and confirm zero errors:

- [x] `python3 course/DP-600/04-resources/build.py` — regenerates all 12 practice/embedded CSVs, 6 Markdown review sets, `answer-manifest.json`, `case-studies.md`, and `case-study-sample.csv`
- [x] `python3 course/DP-600/04-resources/validate.py --report course/DP-600/04-resources/validation-report.json` — `0` errors across 13 CSVs, `206 / 206` (`100%`) terms exercised, max Jaccard `0.6667 <= 0.72`
- [x] `python3 course/DP-600/04-resources/package.py` — packages `course/DP-600/DP-600-6x100.zip`
- [x] `python3 -m unittest discover -s course/DP-600/04-resources -p 'test_*.py' -v` — all 14 unit tests pass
- [x] `python3 course/check_csv_upload.py --all` — repo-wide CSV upload validator passes (`108 / 108` CSVs)
- [x] `python3 course/check_landing_page_fields.py` — repo-wide landing-page validator passes (`18 / 18` courses)

---

## 2. Udemy Course Shell Setup (`01-landing-page/landing-page.md`)

1. Create a **Practice Test Only** course on Udemy.
2. Paste **Field 1 (Course Title)** (`60` chars): `DP-600 Microsoft Fabric: 6 Full-Length Practice Exams (600Q)`
3. Paste **Field 2 (Course Subtitle)** (`97` chars): `600 original questions • Lakehouse, Warehouse, Eventhouse, Direct Lake, SQL, KQL & DAX • Oct 2026`
4. Paste **Field 3 (Course Description)**, **Field 4 (12 learning objectives, each <= 160 chars)**, **Field 5 (Requirements)**, and **Field 6 (Target Audience)**.
5. Paste the **Welcome Message** and **Congratulations Message** under *Course Messages*.

---

## 3. Creating & Uploading the Six Practice Tests

For each exam `N` in `1..6`:

1. Add Practice Test `N` and paste the **Name** and **Full description** (or **Trimmed description** `<= 200` chars where constrained) from `01-landing-page/landing-page.md`.
2. Set **Time limit** = `100 minutes`, **Minimum score to pass** = `80%` (Sets 1–3) / `82%` (Set 4) / `85%` (Sets 5–6), and **Randomize question & answer order** = `ON`.
3. Click **Bulk Upload Questions** and upload `03-practice-sets/set-N/case-embedded-set-N.csv`.
4. Spot-check 2 standalone items, 1 `____` code-completion item, 1 `→` sequence item, and 1 `[Case Study — ...]` item in Udemy's previewer before publishing.
