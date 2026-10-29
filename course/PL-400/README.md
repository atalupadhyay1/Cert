# Microsoft Exam PL-400: Microsoft Power Platform Developer — Practice-Test Course (`6 × 100 = 600` Questions)

Complete Udemy-ready mock-exam package for **Exam PL-400: Microsoft Power Platform Developer** (`Microsoft Certified: Power Platform Developer Associate`), strictly aligned to Microsoft Learn's **October 16, 2026** study-guide update and its seamless portfolio transition to **Exam AB-400: Extending Microsoft Power Platform Solutions with Code and AI**.

> **Credential, Blueprint & AB-400 Transition Disclosure:**
> - **Credential Earned:** `Microsoft Certified: Power Platform Developer Associate` (Associate-level — **no prerequisite certification required**; free annual online renewal on Microsoft Learn).
> - **PL-400 -> AB-400 Portfolio Transition:** Microsoft closed new `PL-400` exam registrations on **October 16, 2026**; scheduled `PL-400` appointments run through **October 30, 2026** (11:59 PM CST), after which **Exam AB-400** continues `Power Platform Developer Associate` on the **identical October 16, 2026 4-domain skills outline**.
> - **Scoring & Format:** Live exam delivers `40–60` questions in `100 minutes` (`~120 minutes` total seat time), open-book `learn.microsoft.com` access during non-lab sections, `$165 USD` (US), and a criterion-referenced **`700 / 1000`** scaled passing score (not `70%` raw accuracy).

---

## Blueprint Weighting (`6 × 100 = 600` Original Questions)

| # | Official PL-400 / AB-400 Functional Group (Effective October 16, 2026) | Official Weight | Per Exam | Total (6 Exams) |
|---:|---|---:|---:|---:|
| 1 | Build Microsoft Power Platform solutions (`1.1`–`1.8`) | 15–20% | 18 | 108 |
| 2 | Extend the user experience (`2.1`–`2.9`) | 25–30% | 28 | 168 |
| 3 | Extend Microsoft Power Platform (`3.1`–`3.13`) | 35–40% | 39 | 234 |
| 4 | Develop integrations (`4.1`–`4.6`) | 10–15% | 15 | 90 |
| **Total** | **36 Local Study-Map Skills (`1.1`–`4.6`)** | **100%** | **100** | **600** |

---

## Per-Exam Item-Type & Pattern Mix

- **`84` `multiple-choice` items** (`21` A / `21` B / `21` C / `21` D exact answer-slot balance):
  - `76` standalone & case-study single-answer engineering questions
  - `8` ordered 4-step (`→`) workflow sequence questions
  - `18–27` (`126` total) `____` code/CLI/OData/WDL completion items across **C#**, **TypeScript**, **JavaScript**, **Power Fx**, **Python**, **PAC / `pa` CLI**, **PowerShell**, **OData v4**, **WDL**, and **OpenAPI**
  - `6–7` (`41` total) `Proposed solution:` architectural evaluation items
- **`16` `multi-select` items** (`3 / 4 / 6 / 3` across Domains 1–4):
  - `13` five-option `Select two.` questions
  - `3` six-option `Select three.` questions
- **`4` original enterprise case studies × `3` questions = `12` case items per exam** (`24` scenarios total; zero Microsoft named sample scenarios).

---

## Directory Layout

- `01-landing-page/landing-page.md` — Udemy metadata (Title, Subtitle, Description, Learning Objectives, Prerequisites, Target Audience), 6 exam descriptions (Full + `<=200`-char Trimmed), Welcome & Congratulations messages, 36-skill map, and FAQs.
- `02-curriculum/curriculum-outline.md` — 6-exam curriculum structure, 24 case-study index, and skill-to-domain study plan.
- `03-practice-sets/set-{1..6}/`:
  - `case-embedded-set-{1..6}.csv` — **Recommended for Udemy randomized mode** (scenario brief embedded in each case question).
  - `practice-set-{1..6}.csv` — Compact case stems (`Case study — <Name>: ...`) for sequential mode.
  - `practice-set-{1..6}.md` — Full human-readable study key with rationales and Microsoft Learn links.
  - `README.md` — Per-exam domain breakdown and upload notes.
- `04-resources/` — Deterministic Python 3.10+ stdlib generator (`build.py`), validator (`validate.py`), packager (`package.py`), unit test suite (`test_course.py`), authored question bank (`questions/1.txt`–`6.txt`, `terms.py`, `sequences.py`, `cases.py`, `sources.py`), `case-studies.md`, `sources-and-coverage.md`, `csv-format-spec.md`, `case-study-upload-guide.md`, `publication-checklist.md`, `SUMMARY.md`, `answer-manifest.json`, and `validation-report.json`.
- `05-sample-upload/` — 12-question `case-study-sample.csv` smoke-test upload file and instructions.
- `PL-400-6x100.zip` — Self-contained distribution archive regenerated via `04-resources/package.py`.

---

## Rebuilding, Validating & Testing

```bash
python3 course/PL-400/04-resources/build.py
python3 course/PL-400/04-resources/validate.py --report course/PL-400/04-resources/validation-report.json
python3 course/PL-400/04-resources/package.py
python3 -m unittest discover -s course/PL-400/04-resources -p 'test_*.py' -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py PL-400
```
