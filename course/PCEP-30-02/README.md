# PCEP™ – Certified Entry-Level Python Programmer (PCEP-30-02) — practice course

**6 mock exams × 60 original questions = 360 · 45 multiple-choice (including `____` code-fill / gap-fill items) + 15 multiple-response · every option explained · CPython 3.11 verified · 80-minute clock matching the live ~80 s/item pace**

This package is an independent study aid for the **PCEP™ – Certified Entry-Level Python Programmer (Exam PCEP-30-02)** certification from the OpenEDG Python Institute. Every code-trace output, exception behaviour, and filler expression was verified against CPython 3.11 before entering the bank, and every answer option — right or wrong — carries its own written explanation.

> **Version notice.** Baseline: the OpenEDG Python Institute PCEP certification page and the PCEP-30-02 exam syllabus, retrieved **October 2026** — **40 minutes** exam clock (**+5 minutes** NDA/tutorial), **30 questions**, **70% cumulative average passing score** across four blocks (**18 / 29 / 25 / 28 percent**), **from $69 USD** ($86 with retake, $95 with retake + practice test), delivered via **OpenEDG Testing Service (TestNow™)**, offered in **English, Spanish, Portuguese, Polish, and Japanese**, **no prerequisites**, and **five-year validity**. **PCEP-30-03 is scheduled for release on October 31, 2026**; PCEP-30-02 remains active and the Python Institute states that this routine version update **does not affect the five-year validity of credentials already earned**.

Independent educational content — not actual, recalled, or copied OpenEDG Python Institute exam items. No OpenEDG endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste Udemy metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 41-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, six-week schedule, scoring method, 80-minute / 40-minute time budget |
| `03-practice-sets/set-1…6/` | Per exam: 17-column Udemy CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One twelve-question mixed sample (three per block: one code-trace multiple-choice, one `____` gap-fill multiple-choice, and one multiple-response) to test player rendering |

## The six exams

| Exam | Small-program scenario emphasis | Items |
|---:|---|---:|
| 1 | CLI utilities and number processing | 60 |
| 2 | Text cleaning and log inspection | 60 |
| 3 | Inventory counters and cart totals | 60 |
| 4 | Sensor readings and threshold checks | 60 |
| 5 | Gradebook tables and quiz scoring | 60 |
| 6 | Schedule parsers and config helpers | 60 |

Every exam uses the exact same block split (**11 / 17 / 15 / 17**) and the same 41-skill plan, so the emphasis column describes the everyday Python utility contexts used in that set's snippets rather than a different syllabus weighting. All four syllabus blocks are examined in all six sets.

## Format boundary: interactive items vs the 17-column CSV contract

The live PCEP-30-02 exam mixes single-select and multiple-select questions with **drag-and-drop, gap-fill, sort, code-fill, and code-insertion** items, and has **no case-study component**. Udemy's 17-column bulk-upload CSV supports only `multiple-choice` and `multi-select`. Accordingly:

- **Single-blank gap-fill and code-fill items are approximated faithfully**: at least 15 `multiple-choice` stems per exam embed a `____` placeholder directly inside a Python statement or header, with four candidate tokens or expressions as options.
- **Drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed**, because they cannot exist in a bulk-upload CSV.
- **No case studies exist anywhere in this folder**: `build.py`, `validate.py`, and `package.py` each reject case-study wording or case files.

## Entry-level Python scope, not PCAP

Object-oriented programming (`class` hierarchies, `__init__`), third-party package management (`pip`), file streams (`open()`), closures, and decorators belong to **PCAP-31-03**, not PCEP-30-02, and are kept out of scope. Every item stays inside the four PCEP-30-02 blocks: fundamentals, control flow, collections (`list`, `tuple`, `dict`, `str`), and user-defined functions, generators, recursion, scope, and built-in exceptions.

## Blueprint allocation

| Official syllabus block | Published weight | Live items (30) | Per exam (60) | Percent | Package total |
|---|---:|---:|---:|---:|---:|
| 1. Computer Programming and Python Fundamentals | 18% | 7 | 11 | 18.3% | 66 |
| 2. Control Flow – Conditional Blocks and Loops | 29% | 8 | 17 | 28.3% | 102 |
| 3. Data Collections – Tuples, Dictionaries, Lists, and Strings | 25% | 7 | 15 | 25.0% | 90 |
| 4. Functions and Exceptions | 28% | 8 | 17 | 28.3% | 102 |
| **Total** | **100%** | **30** | **60** | **100.0%** | **360** |

**The published weights total exactly 100%.** Applied to 60 items they give 10.8 / 17.4 / 15.0 / 16.8. Largest-remainder rounding assigns the two spare items to Blocks 1 and 4 (whose fractional parts `.8` are largest), yielding **11 / 17 / 15 / 17** — every count within 0.4 items of its published weight.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Multiple choice (`multiple-choice`) | 45 | 4 | One correct index in slots 1–4, balanced across the bank; at least 15 use a `____` code-fill / gap-fill blank |
| Multiple response (`multi-select`) | 15 | 5 | Two correct indices, three distractors, "Select two." in the stem; spread 3 / 4 / 4 / 4 across Blocks 1–4 |
| Drag-and-drop, sort, multi-slot code insertion | 0 | — | Excluded by the 17-column Udemy CSV contract and disclosed |

**The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items**, so the 45 / 15 split and the `____` gap-fill count are authoring choices and are labelled as such everywhere they appear.

## Time pressure: expanded 2× bank at live per-item pace

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Published PCEP-30-02 exam | 30 | 40 minutes (+5 min NDA/tutorial) | ~80 |
| Each practice exam here | 60 | 80 minutes | ~80 |

Because the live syllabus is compact (30 items), each mock exam doubles the item count to 60 so all 41 study-map skills are tested on every sitting, and doubles the timer to **80 minutes** so a timed run rehearses the exact ~80-second-per-item pace rather than pretending 60 items fit in 40 minutes.

## Scoring: what 70% means

The Python Institute publishes a **cumulative average passing score of at least 70% across all exam blocks** (each live item is worth up to 40 raw points, normalized to a percentage), with **no separate per-block pass mark**. Never read 70% as "pass each block at 70%" or equate a Udemy all-or-nothing score directly to live partial/weighted item scoring.

## Verification

```bash
cd course/PCEP-30-02/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 360 questions
python3 -m unittest test_course                       # 39 structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py
```

Current status: **360 items, 6 sets, all structural checks passing, all snippet outputs verified on CPython 3.11**.

## Rights and attribution

All 360 questions and all documentation in this folder are original work for this repository. PCEP™, PCAP™, PCPP™, TestNow™, and OpenEDG Python Institute are trademarks of OpenEDG (Open Education and Development Group); Python® is a registered trademark of the Python Software Foundation. This package is independent and makes no claim of affiliation or endorsement.
