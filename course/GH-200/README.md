# Microsoft / GitHub Exam GH-200: GitHub Actions — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Complete, production-ready Udemy Bulk Question Upload package for **Microsoft / GitHub Exam GH-200: GitHub Actions** awarding the **GitHub Actions** certification (`Intermediate` · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification · `$99 USD` · `100 minutes` exam / `120 minutes` seat · `700 / 1000` scaled score · **English, Spanish, Portuguese (Brazil), Korean, and Japanese** · **closed-book: NO Microsoft Learn or GitHub Docs access** · **0 case studies / 0 live labs**).

Aligned strictly to the official **January 2026** (*Last updated February 5, 2026*; certification page updated *August 7, 2026*) Microsoft Learn `GH-200` study guide across all **5 functional domains** and **48 official skills**:

| # | Official GH-200 Domain | Published Weight | Items / Set | Multi-Select / Set | 6-Set Total |
|---:|---|---:|---:|---:|---:|
| 1 | Author and manage workflows | 20–25% | `24` (`24.0%`) | `4` | `144` |
| 2 | Consume and troubleshoot workflows | 15–20% | `19` (`19.0%`) | `3` | `114` |
| 3 | Author and maintain actions | 15–20% | `19` (`19.0%`) | `3` | `114` |
| 4 | Manage GitHub Actions for the enterprise | 20–25% | `24` (`24.0%`) | `4` | `144` |
| 5 | Secure and optimize automation | 10–15% | `14` (`14.0%`) | `2` | `84` |
| **Total** | **All 5 Domains · 48 Official Skills** | **100%** | **`100`** | **`16`** | **`600`** |

## Package Structure

- `01-landing-page/landing-page.md` — Complete Udemy publishing copy (`Course Title`, `Subtitle`, `Description`, `12` concise 60–70 char learning objectives, `Prerequisites`, `Target Audience`, `6` Full + Trimmed exam descriptions, `Welcome Message`, and `Congratulations Message`)
- `02-curriculum/curriculum-outline.md` — Complete 5-domain, 48-skill curriculum map and 6-set architectural matrix
- `02-curriculum/blueprint-alignment.md` — Auto-generated per-domain and per-set telemetry table
- `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` — Six 100-question Udemy UTF-8-BOM 17-column CSV files (`84` `multiple-choice` balanced `21/21/21/21` across `A–D` + `16` `multi-select`; `0` case studies)
- `03-practice-sets/set-{1..6}/practice-set-{1..6}.md` — Human-readable review keys with full per-option and overall explanations
- `04-resources/` — Deterministic Python build, sample, validation, packaging, and unit-test suite (`sources.py`, `sequences.py`, `terms.py`, `bank.py`, `build.py`, `make_sample.py`, `validate.py`, `package.py`, `test_course.py`, `questions/1.txt`..`6.txt`)
- `05-sample-upload/sample-upload.csv` — 15-question quick-smoke Udemy CSV (`3` items per domain: `2 MC + 1 MS`)
- `GH-200-6x100.zip` — Self-contained deterministic distribution archive

## Rebuilding & Verifying

```bash
python3 course/GH-200/04-resources/build.py
python3 course/GH-200/04-resources/make_sample.py
python3 course/GH-200/04-resources/validate.py --report
python3 course/GH-200/04-resources/package.py
python3 -m unittest discover -s course/GH-200/04-resources -p 'test_*.py' -v
```

> **Disclaimer:** Independent educational practice material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with, sponsored by, or endorsed by Microsoft Corporation or GitHub, Inc. Practice test scores do not predict or equate to Microsoft's `700 / 1000` scaled exam score.
