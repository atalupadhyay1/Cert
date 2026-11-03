# Microsoft / GitHub Exam GH-300: GitHub Copilot — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Complete, production-ready Udemy Bulk Question Upload package for **Microsoft / GitHub Exam GH-300: GitHub Copilot** awarding the **GitHub Copilot** certification (`Intermediate` · **no prerequisite** · **2-year validity** with a 6-month transition extension toward Microsoft Learn recertification · `$99 USD` · `100 minutes` exam / `120 minutes` seat · `700 / 1000` scaled score · **English, Spanish, Portuguese (Brazil), Korean, and Japanese** · **closed-book: NO Microsoft Learn or GitHub Docs access** · **0 case studies / 0 live labs**).

Aligned strictly to the official **August 7, 2026** (*Last updated July 9, 2026*; certification page updated *August 7, 2026*) Microsoft Learn `GH-300` study guide across all **6 functional domains** and **41 official skills**:

| # | Official GH-300 Domain | Published Weight | Items / Set | Multi-Select / Set | 6-Set Total |
|---:|---|---:|---:|---:|---:|
| 1 | Use GitHub Copilot responsibly | 15–20% | `18` (`18.0%`) | `3` | `108` |
| 2 | Use GitHub Copilot features | 25–30% | `28` (`28.0%`) | `5` | `168` |
| 3 | Understand GitHub Copilot data and architecture | 10–15% | `14` (`14.0%`) | `2` | `84` |
| 4 | Apply prompt engineering and context crafting | 10–15% | `13` (`13.0%`) | `2` | `78` |
| 5 | Improve developer productivity with GitHub Copilot | 10–15% | `14` (`14.0%`) | `2` | `84` |
| 6 | Configure privacy, content exclusions, and safeguards | 10–15% | `13` (`13.0%`) | `2` | `78` |
| **Total** | **All 6 Domains · 41 Official Skills** | **100%** | **`100`** | **`16`** | **`600`** |

## Package Structure

- `01-landing-page/landing-page.md` — Complete Udemy publishing copy (`Course Title`, `Subtitle`, `Description`, `12` concise 65–67 char learning objectives, `Prerequisites`, `Target Audience`, `6` Full + Trimmed exam descriptions, `Welcome Message`, and `Congratulations Message`)
- `02-curriculum/curriculum-outline.md` — Complete 6-domain, 41-skill curriculum map and 6-set architectural matrix
- `02-curriculum/blueprint-alignment.md` — Auto-generated per-domain and per-set telemetry table
- `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` — Six 100-question Udemy UTF-8-BOM 17-column CSV files (`84` `multiple-choice` balanced `21/21/21/21` across `A–D` + `16` `multi-select`; `0` case studies)
- `03-practice-sets/set-{1..6}/practice-set-{1..6}.md` — Human-readable review keys with full per-option and overall explanations
- `04-resources/` — Deterministic Python build, sample, validation, packaging, and unit-test suite (`sources.py`, `sequences.py`, `terms.py`, `bank.py`, `build.py`, `make_sample.py`, `validate.py`, `package.py`, `test_course.py`, `questions/1.txt`..`6.txt`)
- `05-sample-upload/sample-upload.csv` — 18-question quick-smoke Udemy CSV (`3` items per domain: `2 MC + 1 MS`)
- `GH-300-6x100.zip` — Self-contained deterministic distribution archive

## Rebuilding & Verifying

```bash
python3 course/GH-300/04-resources/build.py
python3 course/GH-300/04-resources/make_sample.py
python3 course/GH-300/04-resources/validate.py --report
python3 course/GH-300/04-resources/package.py
python3 -m unittest discover -s course/GH-300/04-resources -p 'test_*.py' -v
```

> **Disclaimer:** Independent educational practice material authored from public Microsoft Learn and GitHub Copilot documentation — not affiliated with, sponsored by, or endorsed by Microsoft Corporation or GitHub, Inc. Practice test scores do not predict or equate to Microsoft's `700 / 1000` scaled exam score.
