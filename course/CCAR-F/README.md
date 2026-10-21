# Claude Certified Architect – Foundations (CCAR-F)

**6 practice tests × 100 questions = 600 original questions.** Concept checks, short production scenarios, four options, and one best answer, following the established course-package format.

## Download and use

**[Download the complete ZIP](Claude-CCAR-F-Udemy-6x100.zip)**. Extract it and upload each CSV separately to its corresponding Udemy practice test. Do not upload the ZIP or Markdown as a question import.

| Test | CSV upload | Offline questions, key, and explanations |
|---|---|---|
| 1 | [Test 1 CSV](03-practice-sets/set-1/practice-set-1.csv) | [Test 1 review](03-practice-sets/set-1/practice-set-1.md) |
| 2 | [Test 2 CSV](03-practice-sets/set-2/practice-set-2.csv) | [Test 2 review](03-practice-sets/set-2/practice-set-2.md) |
| 3 | [Test 3 CSV](03-practice-sets/set-3/practice-set-3.csv) | [Test 3 review](03-practice-sets/set-3/practice-set-3.md) |
| 4 | [Test 4 CSV](03-practice-sets/set-4/practice-set-4.csv) | [Test 4 review](03-practice-sets/set-4/practice-set-4.md) |
| 5 | [Test 5 CSV](03-practice-sets/set-5/practice-set-5.csv) | [Test 5 review](03-practice-sets/set-5/practice-set-5.md) |
| 6 | [Test 6 CSV](03-practice-sets/set-6/practice-set-6.csv) | [Test 6 review](03-practice-sets/set-6/practice-set-6.md) |

## Test organization

| Test | Focus | Questions |
|---|---|---:|
| 1 | Agentic Architecture & Orchestration | 100 |
| 2 | Tool Design & MCP Integration | 100 |
| 3 | Claude Code Configuration & Workflows | 100 |
| 4 | Prompt Engineering & Structured Output | 100 |
| 5 | Context Management & Reliability | 100 |
| 6 | Integrated Architecture Scenarios & Final Review | 100 |

These are independent learning tests, not actual or recalled exam questions. Tests 1–5 are domain deep dives; Test 6 is an expanded mixed-domain review with 27/18/20/20/15 questions. The overall 600-question package is deliberately not weighted like one exam.

## Included

- 600 individually authored question texts; no copied commercial questions, official sample items, or recalled exam content.
- Per-option feedback combines an explanation of the alternative with the case-specific deciding requirement. Every item also has an overall rationale and official guide objective anchor.
- Four answer options, ONE best answer, and correct positions balanced at 25 each per test.
- Tests 1–5 progress by subject; Test 6 mixes its domains using deterministic order and option shuffling.
- Offline Markdown versions put all questions before the answer key.
- [Comprehensive instructor landing page](01-landing-page/landing-page.md), [curriculum](02-curriculum/curriculum-outline.md), [source notes](04-resources/sources-and-coverage.md), [CSV guide](04-resources/csv-format-spec.md), and [publication checklist](04-resources/publication-checklist.md).
- Source bank, deterministic builder, displayed-answer manifest, validator, regression tests, [validation report](04-resources/validation-report.json), and ZIP.

## Coverage and relationship to the exam

| Official domain | Approximate exam weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| Agentic Architecture & Orchestration | 27% | 100 | 27 | 127 |
| Tool Design & MCP Integration | 18% | 100 | 18 | 118 |
| Claude Code Configuration & Workflows | 20% | 100 | 20 | 120 |
| Prompt Engineering & Structured Output | 20% | 100 | 20 | 120 |
| Context Management & Reliability | 15% | 100 | 15 | 115 |

The retrieved July 2026 v1.0 guide lists **60 items, 120 minutes, multiple-choice and multiple-response**, with four scenarios drawn from six published scenario themes. The passing score is **720 on a 100–1,000 scaled scale**, not a published raw 72% threshold. This package instead has 100 questions per test, all **single-answer with four options**. Its mini-scenarios do not reproduce the official four-of-six scenario structure. Optional **200 minutes and an 80% study target** are custom guidance, not official timing, scaled-score equivalents, or a passing guarantee.

Concepts, option definitions, and distinctions intentionally recur across tests. The exports have 600 normalized-distinct stems, not 600 unrelated concepts or six statistically independent readiness assessments. Difficulty is not psychometrically calibrated. Final subject-matter review and actual account-level Udemy imports remain required.

## Version-sensitive terminology

Research retrieved October 21, 2026. The official guide calls the subagent launcher `Task`; current SDK documentation uses `Agent`. Questions emphasize the version-appropriate mechanism rather than falsely asserting one identifier works in every release. Instruction-file inspection commands, skills, permission behavior, strict-schema support, and model compatibility also require installed-version checks. Read [source notes](04-resources/sources-and-coverage.md) before implementation or publication.

## Rebuild and verify

Python **3.10+**, standard library only. From the repository root:

```bash
python course/CCAR-F/04-resources/build.py
python course/CCAR-F/04-resources/validate.py --report course/CCAR-F/04-resources/validation-report.json
python -m unittest discover -s course/CCAR-F/04-resources -p 'test_*.py' -v
python course/CCAR-F/04-resources/package.py
```

Edit `04-resources/questions/1.txt` through `6.txt` and the shared explanations in `terms.py`. Each source row contains objective, four term keys (correct first), question, and rationale. Rebuild instead of manually reordering exported options or keys. Packaging rejects stale manifests, review copies, and invalid CSVs.

## Recommended official references

- [Official certification portal](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification)
- [Official CCAR-F exam guide, v1.0 effective July 2026](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)
- [Agent SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents)
- [Claude API tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- [Claude Code project memory and rules](https://code.claude.com/docs/en/memory)

This package is not a video course, included lab subscription, certification award, or guarantee. No API account is needed to read or answer the questions; practical experience with Claude, tools, coding workflows, and JSON is recommended. Not affiliated with or endorsed by Anthropic or Udemy. Product and certification marks belong to their owners.
