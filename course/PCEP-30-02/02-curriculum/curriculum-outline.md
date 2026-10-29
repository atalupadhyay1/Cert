# Curriculum outline — PCEP™ – Certified Entry-Level Python Programmer (PCEP-30-02) practice course

**Six 60-item mock exams · 360 original questions · CPython 3.11 verified · 80-minute rehearsal at the live ~80 s/item pace**

Every exam is blueprint-weighted **11 / 17 / 15 / 17** against the published **18 / 29 / 25 / 28** percent across the four OpenEDG Python Institute syllabus blocks, so the sequence below builds code-tracing fluency across six distinct small-program contexts rather than shifting weights.

The live **PCEP-30-02** exam presents **30 questions in 40 minutes** (plus 5 minutes for NDA and tutorial), with **no case-study component**. Doubling each mock exam to 60 items in 80 minutes tests all 41 study-map skills on every sitting while preserving the exact **~80 seconds per item** pace.

## Learning arc

| Phase | Exam | Small-program emphasis | Study goal |
|---|---|---|---|
| Trace expressions cleanly | 1 | CLI utilities and number processing | Master operator precedence, binding, and loop termination |
| Spot subtle edge cases | 2 | Text cleaning and log inspection | Separate parse-time `SyntaxError` from runtime truthiness and shadowing |
| Control mutation and state | 3 | Inventory counters and cart totals | Distinguish in-place mutation (`None` return) from new objects |
| Reason about bits and bounds | 4 | Sensor readings and threshold checks | Handle negative floor/modulo, bitwise ops, and handler reachability |
| Combine collections and recursion | 5 | Gradebook tables and quiz scoring | Trace nested structures, generators, and exception hierarchies |
| Sit under strict exam pace | 6 | Schedule parsers and config helpers | Finish 60 items inside 80 minutes with zero shell assistance |

## Exam-by-exam study plan

### Exam 1 — CLI utilities and number processing (60 items)
- Official block split: 11 Fundamentals, 17 Control Flow, 15 Data Collections, 17 Functions & Exceptions.
- Focus: CPython bytecode model; lexis vs syntax vs semantics; reserved keywords vs built-ins; `0b` and `0x` literals; legal identifiers; `//` vs `/` vs `%`; right-sided `2 ** 3 ** 2`; `&` bitmasks; `0.1 + 0.2 == 0.3`; `print(..., sep=, end=)`; `int(input())`; `if`/`elif`/`else`; falsy values; chained comparisons and short-circuit `and`; `while` accumulators; countdown `range()`; string digit iteration; `continue` and `pass`; `for ... else`; triangular nested loops; list slicing and stride; `list.sort()` returning `None`; `del` on slices; shallow copies (`[:]`, `.copy()`); even-square comprehensions; `not in`; one-element `(7,)` tuples; mutating a list inside a tuple; duplicate dict keys; safe key membership; escaped `\n` length; `str.isdigit()`; implicit `None` returns; `yield` generators; recursive factorial and missing-base-case `RecursionError`; valid keyword call order; shared mutable default lists; `global` vs local rebinding; `BaseException` vs `Exception`; `LookupError`; `int('42.5')` `ValueError`; `15 % 0` `ZeroDivisionError`; `except` branch ordering.

### Exam 2 — Text cleaning and log inspection (60 items)
- Focus: interpreter portability vs ahead-of-time compilation; parse-time unclosed parentheses; `assert`/`from` keywords; scientific `2.5e-2` and octal `0o77`; PEP-8 `snake_case`; negative floor division `-7 // 2 == -4`; `-3 ** 2 == -9`; bitwise XOR `^`; string repetition; `end=' '`; `bool('False') == True`; severity `elif` chains; `==` vs `=`; whitespace `.strip()` truthiness; De Morgan laws; short-circuit `or` returning operand values; string-slicing `while` loops; empty `range(5, 1)`; `break` vs `continue` counts; `for ... else` suppression; 2D hit grids; negative-stride slices `cols[3:0:-1]`; `append([3, 4])` nesting; `sorted()` vs `.sort()`; `list()` shallow copies; comprehension word lengths; substring `in`; tuple swap `a, b = b, a`; `dict.get()` defaults; `.items()` unpacking; escaped `\'` and `\t` length; non-overlapping `str.count()`; `startswith()`; tuple-packing `return a, b`; single-pass generator exhaustion; recursive list sum; `UnboundLocalError`; `ArithmeticError` and `LookupError` subclasses; `KeyError`; `raise ValueError`; `finally` cleanup.

### Exam 3 — Inventory counters and cart totals (60 items)
- Focus: `.py` source files; lexis/syntax/semantics pairs; `import`/`class` keywords; `1_000_000` and `4e3`; consistent block indentation; `10 / 2 == 5.0`; `2 + 3 * 4 ** 2 == 50`; left shift `<<`; `*=` string repetition; `sep=';'`; `int(-3.9) == -3` truncation toward zero; independent `if` statements vs `elif`; `[0]` truthiness; `and` before `or` precedence; `while` packing loops; zero-trip `while ... else` still running `else`; clamping out-of-range slices `skus[10:20] == []`; `[::-1]` reversal; `extend()` vs `append()`; `pop()`; `len()`; tuple concatenation; `dict.pop()` and `sum(d.values())`; apostrophes inside strings; `'-'.join(parts)`; generator squares; recursive `power(base, exp)` and multiplicative identity `1`; keyword reordering; `None` default sentinel; mutating global list elements without `global`; `KeyboardInterrupt` under `BaseException`; `IndexError` vs slice clamping; `'Total: ' + 15` `TypeError`; `try ... except ... else`.

### Exam 4 — Sensor readings and threshold checks (60 items)
- Focus: CPython multi-platform execution; lexical `@$` failure; `nonlocal`/`yield` keywords; `0b110 + 0xA == 16`; negative divisor/dividend modulo `-7 % 3 == 2`; left-to-right `16 // 3 * 2 == 10`; bitwise inversion `~4 == -5`; `'#' * -2 == ''`; `print(..., sep='*')`; `float(input())`; nested conditional expressions; `-1` truthiness vs `0.0`; `not` vs `~`; `//=` halving loops; `range(10, 4, -2)`; peak-tracking loops; sensor noise `continue`; `for ... else` safety checks; nested zone matrices; negative indexing `temps[-2]`; `insert(1, 20)`; `del items[1:3]`; list aliasing `b = a`; odd-square comprehensions; `(0,) * 3`; `del sensors['old_probe']`; triple-quoted newline length; `str.endswith()`; `<class 'generator'>`; recursive Fibonacci `fib(6) == 8`; missing `return` in recursion; `AttributeError` on `tuple.append`; misspelled `NameError`; broad `ArithmeticError` masking `ZeroDivisionError`.

### Exam 5 — Gradebook tables and quiz scoring (60 items)
- Focus: CPython execution; `global`/`return` keywords; `3e2 == 300.0`; `17 % 5`; `-2 ** 4 == -16`; right shift `19 >> 2 == 4`; `+=`; two `print()` calls joined by `end='-'`; `str(95)`; `<=` boundaries; `False and True or True`; `sum(range(1, 11)) == 55`; sentinel `break`; `pass` inside `if`; 2D grade matrices; `marks[:2]` and `marks[-3:]`; `scores.remove(10)` deleting only the first match; `roster.index('Lin')`; `del qs[-1]`; `[ch.upper() ... if ch.isalpha()]`; indexing tuples inside a list `roster[1][1]`; updating vs inserting dict keys; `gradebook.items()`; `str.isalpha()`; `StopIteration` on exhausted `next()`; recursive `digit_sum(308)`; keyword-before-positional `SyntaxError`; mutable default `bag=[]`; local shadowing leaving module globals unchanged; `int('absent')` `ValueError`; `finally` lock release.

### Exam 6 — Schedule parsers and config helpers (60 items)
- Focus: bytecode VM vs native compilation; missing-colon `SyntaxError`; `pass`/`continue` keywords; `#` comments; negative exponent `2 ** -3 == 0.125`; left-to-right `24 / 4 / 2 == 3.0`; `& 1` bit masking; `-5.0 // 2 == -3.0`; `sep='/'`; `'12' + '3' == '123'`; `!=`; `'False'` string truthiness; `not False and False == False`; `*=` retry doubling; `range(5, 0, -1)`; `startswith()` filtering; combined `continue` and `break`; `hours[1:-1]` and `hours[::-2]`; in-place `deadlines.sort()`; shallow copy `orig[:]` sharing inner lists; tuple unpacking `(h, m) = (1, 15)`; `cfg.get('timeout', 30)`; doubled backslash `'a\\tb'` length `4`; `line.split()`; generator `yield` pairs; Euclid's recursive `gcd(18, 12)`; unexpected keyword `TypeError`; `UnboundLocalError` on `port`; `SystemExit` bypassing `except Exception:`; `LookupError` masking `KeyError`.

## Item formats and how to rehearse them

| Format in this package | Per exam | Live PCEP-30-02 counterpart |
|---|---:|---|
| Code-trace & concept `multiple-choice` | ~30 | Single-select code output, error diagnosis, and concept items |
| Single-blank `____` `multiple-choice` | >=15 | Single-slot gap-fill and code-fill items (approximated within 4 options) |
| Five-option `multi-select` ("Select two.") | 15 | Multiple-select items |
| Drag-and-drop, sort, multi-slot code insertion | 0 | **Excluded** by Udemy's 17-column CSV contract; rehearse syntax actively by typing snippets |

## Suggested six-week schedule

| Week | Work | Time |
|---:|---|---|
| 1 | Read the syllabus map; take Exam 1 untimed on paper without opening Python | ~2.5 h |
| 2 | Run every missed Exam 1 snippet in Python 3; take Exam 2 untimed | ~3 h |
| 3 | Drill Block 2 loops and Block 3 slicing/aliasing; take Exam 3 with a 95-minute clock | ~3 h |
| 4 | Drill Block 4 scope, defaults, and exception hierarchy; take Exam 4 in 85 minutes | ~3 h |
| 5 | Take Exam 5 under the full 80-minute clock; build a one-page personal trap sheet | ~2.5 h |
| 6 | Take Exam 6 under 80 minutes; review your trap sheet before TestNow™ | ~2.5 h |

## Scoring your own attempt

- Udemy awards 1 point per item (and all-or-nothing on `multi-select`).
- On the live PCEP-30-02 exam, each of the 30 items is worth up to 40 points, normalized to a percentage, and passing requires a **cumulative average score of at least 70% across all four blocks** (no separate per-block pass minimum).
- Aim for **85%+ (51 / 60)** on timed runs here so unfamiliar interactive widgets on exam day still leave comfortable margin above 70%.

## Time budget: 80-minute practice exam vs 40-minute live exam

| Phase | Practice (60 Q / 80 min) | Live exam (30 Q / 40 min) | Notes |
|---|---:|---:|---|
| First pass | 60 min (~60 s/item) | 30 min (~60 s/item) | Trace carefully; flag gnarly nested loops rather than stalling |
| Flagged review | 14 min | 7 min | Re-verify signs, off-by-one `range()` stops, and `None` returns |
| Final check | 6 min | 3 min | Confirm every `Select two.` item has two selections and nothing is blank |
