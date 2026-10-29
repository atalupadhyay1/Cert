# PCEP™ – Certified Entry-Level Python Programmer (PCEP-30-03) — Curriculum Outline & Study Plan

## Course structure

Six 60-item blueprint-weighted mock exams (**360 original questions total**, zero stem overlap with `PCEP-30-02`), each timed at **80 minutes** to match the published `PCEP-30-0x` pace of **~80 seconds per item** (30 live questions in 40 minutes, plus a 5-minute NDA and tutorial).

> **Pre-release & baseline notice (checked October 29, 2026).** OpenEDG Python Institute lists **PCEP-30-03** as **Pending Release (scheduled for October 31, 2026)** and describes it as a routine exam-version update under `PCEP-30-0x` that does not affect the five-year validity of credentials already earned. Because no standalone `PCEP-30-03` syllabus table has been published ahead of October 31, 2026, all six exams baseline against the published `PCEP-30-0x` block weights (**18 / 29 / 25 / 28 percent**) and make no claim about unpublished future blueprint changes.

| Section | Practice test | Everyday Python problem theme | Items | Timer | Pass target |
|---:|---|---|---:|---:|---:|
| 1 | Mock Exam 1 | Budget Trackers and Currency Calculators | 60 | 80 min (take untimed first) | 70% cumulative |
| 2 | Mock Exam 2 | URL Builders and Input Validators | 60 | 80 min | 70% cumulative |
| 3 | Mock Exam 3 | Ticket Queues and Seat Booking | 60 | 80 min | 70% cumulative |
| 4 | Mock Exam 4 | Weather Stations and Unit Converters | 60 | 80 min | 70% cumulative |
| 5 | Mock Exam 5 | Workout Timers and Pace Trackers | 60 | 80 min | 70% cumulative |
| 6 | Mock Exam 6 | Recipe Scalers and Pantry Audits | 60 | 80 min (strict dress rehearsal) | 80%+ safety margin |

## Identical blueprint allocation on every exam

| Block | Official PCEP-30-0x block title | Weight | Live (30) | Mock (60) | Single-choice | Multi-select |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Computer Programming and Python Fundamentals | 18% | 7 | 11 | 8 | 3 |
| 2 | Control Flow – Conditional Blocks and Loops | 29% | 8 | 17 | 13 | 4 |
| 3 | Data Collections – Tuples, Dictionaries, Lists, and Strings | 25% | 7 | 15 | 11 | 4 |
| 4 | Functions and Exceptions | 28% | 8 | 17 | 13 | 4 |
| **All** | **Total** | **100%** | **30** | **60** | **45** | **15** |

At least **15 single-choice items per exam** (16–18 in this package) contain a single `____` code-fill / gap-fill blank inside a Python snippet.

## Six-week preparation schedule

1. **Week 1 — Diagnostic & Fundamentals (Exam 1 + Block 1 drill):** Sit Mock Exam 1 untimed on paper without opening a Python REPL. Review bytecode vs compilation, lexical/syntactic/semantic errors, hard vs soft keywords (`match`/`case`), base prefixes (`0b`, `0o`, `0x`), negative floor division and modulo, precedence (`-4 ** 2` vs `(-4) ** 2`, `2 ** 2 ** 3`), bitwise shifts/masks, IEEE-754 float residuals, and `print(..., sep=, end=)` / `input()` casts.
2. **Week 2 — Control Flow & Iteration (Exam 2 + Block 2 drill):** Sit Mock Exam 2 in 80 minutes. Drill `if`/`elif`/`else` vs sequential `if` chains, inline conditional expressions (`a if cond else b`), container and string truthiness (`'0'`, `(0,)`, `['']` vs `''`, `()`, `0.0`), `not > and > or` precedence, chained comparisons, terminating `while` loops, negative-step and empty `range()` calls, `break`/`continue`/`pass`, and `for-else` / `while-else`.
3. **Week 3 — Collections & String Mechanics (Exam 3 + Block 3 drill):** Sit Mock Exam 3 in 80 minutes. Review positive/negative stride slicing, clamping out-of-range slices vs subscript `IndexError`, in-place mutators returning `None` vs `sorted()`, aliasing vs shallow copies (`[:]`, `.copy()`, `list()`), comprehensions, `in` on dicts (keys only), singleton tuple commas `(42,)`, lists inside tuples, tuple hashability, safe `.get()`/`.pop()`, escape lengths, and string methods.
4. **Week 4 — Functions, Scope & Exceptions (Exam 4 + Block 4 drill):** Sit Mock Exam 4 in 80 minutes. Review `def` / implicit `None` returns, `yield` lazy generators and single-pass exhaustion, recursive base cases vs `RecursionError`, positional-before-keyword rules, mutable default parameter traps (`acc=[]` vs `None`), LEGB / `UnboundLocalError` / `global`, and the `BaseException` / `Exception` / `LookupError` / `ArithmeticError` tree.
5. **Week 5 — Targeted Weak-Block Remediation (Exam 5):** Re-test every missed skill in an interactive Python 3.11 interpreter, then sit Mock Exam 5 under strict 80-minute timing.
6. **Week 6 — Dress Rehearsal & Live-Interface Check (Exam 6):** Sit Mock Exam 6 in one uninterrupted 80-minute block with no notes or terminal open (aiming for **80%+** on Udemy's stricter all-or-nothing multi-select scoring to build cushion above the live **70%** cumulative passing bar). Review TestNow™ policies (desktop/laptop browser only, no scheduled breaks, 7-day retake wait) and check `https://pythoninstitute.org/pcep` for any post-October 31, 2026 syllabus updates.

## Pacing & scoring notes

- **80-minute mock pace vs 40-minute live pace:** Spend ~60 seconds on direct operator, keyword, and exception-tree items so you bank ~95–100 seconds for nested loops, negative slices, recursion traces, and 5-option `Select two.` items.
- **Scoring difference:** On the live OpenEDG exam, each item carries up to 40 raw points normalized to an overall percentage (cumulative 70% passing threshold, no per-block minimum). Udemy awards 1 point per item with all-or-nothing credit on `multi-select`.
