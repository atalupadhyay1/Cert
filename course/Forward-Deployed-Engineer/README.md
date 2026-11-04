# Forward Deployed Engineer (`CFDE` / Enterprise `FDE`) — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Production-ready Udemy practice-test package for **Forward Deployed Engineer (`CFDE` / `FDE`)** certifications, cloud-partner validations, and customer-embedded AI architecture loops:
- **GSDC Certified Forward Deployed Engineer (`CFDE`):** `13`-module syllabus (`40` MCQs, `90` minutes, `65%` passing score, **closed-book**, `5-year` validity)
- **AWS Partner Forward Deployed Engineer (`FDE`):** `Ground`, `Orchestrate`, and `Prove` pathways (`FDE Validated` & `FDE Advanced`, Oct 2026)
- **Anthropic Claude Frontier Academy & Enterprise FDE Competencies:** Canonical workflow/agent patterns, `MCP` servers, evaluation harnesses, `NIST AI RMF 1.0`, `OWASP Top 10 for LLM Applications`, `OpenTelemetry` GenAI observability, and CISO/SRE handover

---

## Course Telemetry at a Glance

| Metric | Value |
|---|---|
| **Practice sets** | `6 × 100 = 600` unique customer-embedded scenarios (`0` artificial case studies) |
| **Domain weights per set** | `15` / `16` / `18` / `20` / `15` / `16` across `6` domains & `37` skills (`1.1`–`6.6`) |
| **Question type split per set** | `84` `multiple-choice` (`76 S + 8 O`, balanced `21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13 M2 + 3 M3`) |
| **Code/API/config completions (`____`)** | `30–32` per set (`185` total across 6 sets) |
| **`Proposed solution:` evaluations** | `8–9` per set (`49` total across 6 sets) |
| **Canonical `TERMS` coverage** | `141 / 141` (`100.0%`) |
| **Max pairwise stem Jaccard** | `0.50` (`<= 0.72` threshold; `0` stem collisions across all `30` sibling courses / `180` CSVs) |
| **Sample smoke-test upload** | `05-sample-upload/sample-upload.csv` (`18` rows: `2 MC + 1 MS` per domain) |
| **Distribution archive** | `Forward-Deployed-Engineer-6x100.zip` |

---

## Directory Layout

- `01-landing-page/landing-page.md` — Complete Udemy publishing copy (Title, Subtitle, 2026 Credential Overview, Description, 12 `61–67` char learning outcomes, Prerequisites, Target Audience, 6 Full/Trimmed Exam Descriptions, Welcome & Congratulations messages)
- `02-curriculum/{curriculum-outline.md, blueprint-alignment.md}` — 37-skill map, 6 industry engagement themes, and verified domain/set telemetry
- `03-practice-sets/set-{1..6}/{practice-set-{1..6}.csv, practice-set-{1..6}.md, README.md}` — Six 100-question Udemy CSV uploads and full Markdown review keys
- `04-resources/` — Deterministic Python build/validation/test suite (`sources.py`, `sequences.py`, `terms.py`, `bank.py`, `build.py`, `make_sample.py`, `validate.py`, `package.py`, `test_course.py`, `questions/{1..6}.txt`, `SUMMARY.md`, `answer-manifest.json`, `validation-report.json`)
- `05-sample-upload/{sample-upload.csv, README.md}` — 18-question quick smoke-test CSV

## Rebuild & Validate

```bash
python3 course/Forward-Deployed-Engineer/04-resources/build.py
python3 course/Forward-Deployed-Engineer/04-resources/make_sample.py
python3 course/Forward-Deployed-Engineer/04-resources/validate.py --report
python3 course/Forward-Deployed-Engineer/04-resources/package.py
python3 -m unittest discover -s course/Forward-Deployed-Engineer/04-resources -p "test_*.py" -v
```
