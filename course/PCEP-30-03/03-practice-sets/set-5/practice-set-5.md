# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 5

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 16 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A marathon timing app imports `splits.py` and runs under standard CPython 3. Which two statements accurately describe `.pyc` bytecode caches and runtime error stops? Select two.

- A. When an unhandled runtime error occurs, CPython halts execution at the failing bytecode step after running earlier statements
- B. Cached `.pyc` files contain x86-64 machine instructions that run directly on the OS kernel without Python installed
- C. Cached `.pyc` files store compiled Python bytecode so unchanged imported modules skip reparsing on later runs
- D. Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production
- E. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes

### 2. In a cadence tracker, a coach writes `if rpm >= 90 print('Fast')` omitting the required colon `:` before `print`. Every individual token is valid, yet CPython refuses to compile the line. Which error layer is violated?

- A. A lexical error because the character or token itself does not belong to valid Python token forms
- B. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- C. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- D. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning

### 3. A developer building an interval stopwatch avoids variable names that are reserved keywords in Python 3. Which two identifiers are hard reserved keywords? Select two.

- A. `none`
- B. `match`
- C. `nonlocal`
- D. `max`
- E. `assert`

### 4. A cycling power meter stores constants for threshold watts and sensor status bits. Which two numeric literals are valid in Python 3? Select two.

- A. `045`
- B. `4e2`
- C. `500_`
- D. `0b1101`
- E. `0x1G`

### 5. Complete `____ = 0` at the top of a stopwatch helper so the counter variable uses a syntactically legal Python 3 identifier. Which variable name fills the blank?

- A. `2nd_quarter`
- B. `_lap_count`
- C. `user@host`
- D. `seat count`

### 6. Complete `extra_seconds = total_seconds ____ 60` in a workout stopwatch so `145` total seconds yields the remaining `25` seconds past two full minutes. Which arithmetic operator fills the blank?

- A. `/`
- B. `**`
- C. `//`
- D. `%`

### 7. A rowing stroke formula evaluates `cadence_bonus = 18 % 5 * 3` without parentheses. What integer is assigned to `cadence_bonus`?

- A. `3`
- B. `-9`
- C. `9`
- D. `19`

### 8. Complete `combined_zones = 9 ____ 5` in a heart-rate bitmask helper so setting bits present in either `0b1001` (`9`) or `0b0101` (`5`) produces `0b1101` (`13`). Which bitwise operator fills the blank?

- A. `>>`
- B. `&`
- C. `|`
- D. `^`

### 9. A workout rep logger accidentally keeps `'25'` as a string and evaluates `rep_banner = '25' * 3`. What value is bound to `rep_banner`?

- A. `TypeError`
- B. `'252525'`
- C. `'1212'`
- D. `36`

### 10. Complete `print('00', '42', '15', ____)` in a race-clock display helper so hours, minutes, and seconds print on one line as `00:42:15`. Which keyword argument fills the blank?

- A. `sep='/'`
- B. `end=', '`
- C. `end=''`
- D. `sep=':'`

### 11. An athlete types `180` when prompted by `resting_limit = input('Max HR: ')` and the script prints `type(resting_limit)`. What is printed and why?

- A. `2.0`
- B. `<class 'str'>` because `input()` always returns text even when the user types digits
- C. `0.0`
- D. `<class 'int'>` because `input()` automatically parses integer digits

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete `if pace < 4.5: group = 'A'` / `____ pace < 5.5: group = 'B'` / `else: group = 'C'` so runners under `5.5` min/km who are not under `4.5` land in group `'B'`. Which keyword fills the blank?

- A. `for`
- B. `elif`
- C. `else`
- D. `pass`

### 13. A step-streak tracker sets `days = 35` and runs `if days >= 30: print('GOLD')` / `elif days >= 14: print('SILVER')` / `elif days >= 7: print('BRONZE')` / `else: print('START')`. What is printed?

- A. `GOLD`
- B. `BRONZE`
- C. `SILVER`
- D. `GOLD` followed by `SILVER`

### 14. Complete the inline conditional expression `label = 'REST' if hr < 100 ____ 'WORK'` in a heart-rate monitor. Which keyword is mandatory before the fallback expression?

- A. `pass`
- B. `elif`
- C. `else`
- D. `while`

### 15. A hydration calculator sets `km = 22; ml_per_min = 20` and runs two separate `if` statements: `if km >= 10: ml_per_min += 3` followed by `if km >= 20: ml_per_min += 5`. What integer does `ml_per_min` hold afterward?

- A. `20`
- B. `25`
- C. `28`
- D. `23`

### 16. A workout-note parser checks `if memo:` before saving athlete comments. Which two values of `memo` evaluate to `False`? Select two.

- A. `['']`
- B. `'0'`
- C. `' '`
- D. `''`
- E. `None`

### 17. A recovery-score delta equals `-1` and the dashboard evaluates `changed = bool(-1)`. What value is bound to `changed`?

- A. `False`
- B. `TypeError`
- C. `-1`
- D. `True`

### 18. An aerobic zone monitor must evaluate to `True` when heart rate `bpm` is at least `120` and strictly below `160`. Which two expressions test that interval accurately? Select two.

- A. `120 <= bpm <= 160`
- B. `120 <= bpm < 160`
- C. `bpm >= 120 or bpm < 160`
- D. `bpm >= 120 and bpm < 160`
- E. `bpm >= 120 & bpm < 160`

### 19. A treadmill console reads `runner_name = ''` and sets `banner = runner_name or 'guest'`. What value is assigned to `banner`?

- A. `None`
- B. `''`
- C. `False`
- D. `'guest'`

### 20. Complete `seconds_left = 30` / `____ seconds_left > 0:` / `    seconds_left -= 10` so the plank countdown ticks down until `seconds_left` hits `0`. Which keyword fills the blank?

- A. `with`
- B. `for`
- C. `elif`
- D. `while`

### 21. A pyramid-rep counter sets `r = 1; reps = 0` and runs `while r <= 6: reps += r; r += 1`, then prints `reps`. What integer is printed?

- A. `28`
- B. `15`
- C. `6`
- D. `21`

### 22. A cooldown timer needs a `for` loop that chimes exactly three times. Which two `range()` calls generate three integers each? Select two.

- A. `range(3, 12, 3)`
- B. `range(0, 10, 2)`
- C. `range(2, 8, -2)`
- D. `range(3, 9, 3)`
- E. `range(9, 0, -3)`

### 23. An interval distance check evaluates `print(sum(range(2, 10, 2)))`. What integer does it print?

- A. `12`
- B. `30`
- C. `20`
- D. `10`

### 24. A kettlebell set stores `weights = [4, 6, 4]` and runs `moved = 0` / `for w in weights: moved += w` / `print(moved)`. What integer is printed?

- A. `3`
- B. `TypeError`
- C. `14`
- D. `12`

### 25. Complete `for split in [310, 0, 295, 0, 305]:` / `    if split == 0: ____` / `    recorded.append(split)` so paused `0` markers are skipped while later splits still record. Which keyword fills the blank?

- A. `continue`
- B. `return`
- C. `pass`
- D. `break`

### 26. A warmup loop runs `acc = 0` / `for mins in [3, 4, 9, 5]:` / `    if mins > 8: break` / `    acc += mins` / `print(acc)`. What integer is printed?

- A. `7`
- B. `16`
- C. `3`
- D. `9`

### 27. A pace-consistency audit attaches an `else:` block to its lap check loop. In which two scenarios does Python execute that loop `else:` block? Select two.

- A. When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`
- B. When a `for` loop finishes iterating over every element without executing `break`
- C. Whenever an unhandled exception aborts the loop body
- D. Immediately after a `break` statement jumps out of the loop body
- E. Right before a `return` statement inside the loop exits the enclosing function

### 28. A circuit planner counts pairings with `slots = 0` and runs `for station in ['row', 'bike', 'ski']:` / `    for round_no in range(3): slots += 1` / `print(slots)`. What integer is printed?

- A. `9`
- B. `6`
- C. `12`
- D. `3`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. Kilometer splits are stored in `splits = [10, 20, 30, 40, 50]`. What list does `splits[::2]` return?

- A. `[10, 30, 50]`
- B. `[20, 30]`
- C. `[40, 50]`
- D. `IndexError`

### 30. Given `splits = [10, 20, 30, 40, 50]`, what integer does negative index `splits[-4]` evaluate to?

- A. `20`
- B. `30`
- C. `IndexError`
- D. `10`

### 31. Complete `lanes = [2, 5, 8, 5]; lanes.____(5)` so the first element equal to value `5` (rather than index `5`) is deleted in place, leaving `[2, 8, 5]`. Which list method name fills the blank?

- A. `append`
- B. `remove`
- C. `insert`
- D. `pop`

### 32. A lap tracker holds `items = [62, 59, 61]`. Which two operations mutate the existing `items` list object in place? Select two.

- A. `items.extend(seq)`
- B. `items.pop()`
- C. `sorted(items)`
- D. `items + [x]`
- E. `items[:]`

### 33. A pace buffer stores `vals = [10, 20, 30, 40, 50]`, executes `del vals[1:4]`, and prints `vals`. What list is printed?

- A. `[10, 50]`
- B. `[]`
- C. `IndexError`
- D. `[20, 30]`

### 34. A coach holds `items = [100, 200, 400]` and wants a shallow copy so inserting warmup drills into the copy leaves `items` unchanged. Which two expressions create a shallow copy? Select two.

- A. `backup = items`
- B. `items.insert(0, x)`
- C. `items.sort()`
- D. `list(items)`
- E. `items.copy()`

### 35. Complete `fast = [s for s ____ splits if s < 240]` to build a filtered list comprehension of sub-4-minute splits. Which keyword fills the blank?

- A. `not`
- B. `in`
- C. `is`
- D. `with`

### 36. Complete `if lane ____ occupied_lanes: assign(lane)` so `assign(lane)` runs only when `lane` is absent from `occupied_lanes`. Which membership operator fills the blank?

- A. `elif`
- B. `and`
- C. `is`
- D. `not in`

### 37. A pace script writes `single = (42)` without a trailing comma inside the parentheses. Which expression in the options represents that exact non-tuple integer grouping, and why is `type(single)` `int` rather than `tuple`?

- A. `42,`
- B. `(42)`
- C. `(42,)`
- D. `tuple()`

### 38. A stopwatch tries to store a mutable list as a dictionary key via `best = {[5, 10]: 'relay'}`. Which exception does Python raise?

- A. `('A', [1, 2, 3])`
- B. `KeyError`
- C. `None`
- D. `TypeError`

### 39. A zone-rate dictionary `rates = {'Z1': 110, 'Z2': 135}` does NOT contain key `'CHF'`. Which two expressions read or remove `'CHF'` safely without raising `KeyError`? Select two.

- A. `rates.pop('CHF', 0)`
- B. `except KeyError, IndexError:`
- C. `rates['CHF']`
- D. `calc(base=100, 0.2)`
- E. `rates.get('CHF', 0)`

### 40. An athlete profile stores metrics in a Python 3 `dict`. Which two statements accurately describe dictionary literals and `.items()`? Select two.

- A. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- B. Membership `k in d` checks both keys and values simultaneously
- C. Curly braces `{ ... }` around `if` and `for` bodies so whitespace is completely ignored
- D. `.items()` yields `(key, value)` 2-tuples suitable for `for k, v in d.items():` unpacking
- E. Duplicate keys in a literal keep a single entry whose value is the last assignment evaluated

### 41. A bib-tag generator calls `ord('A')` and `chr(97)`. What integer does `ord('A')` return while `chr(97)` returns `'a'`?

- A. `65`
- B. `97`
- C. `TypeError`
- D. `42`

### 42. Given `parts = ['5K', '10K', '21K']`, complete `banner = ____` so the elements are joined with hyphens into `'5K-10K-21K'`. Which expression fills the blank?

- A. `'-'.join(parts)`
- B. `subtotal >= 50 ? 0 : 5`
- C. `parts.join('-')`
- D. `def quote(rate=1.1, amount, fee=0):`

### 43. A workout tag checker evaluates `'tempo-run'.find('swim')`. What is returned and why?

- A. `ValueError`
- B. `0`
- C. `None`
- D. `-1` because `.find()` returns `-1` instead of raising `ValueError` when a substring is absent

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Complete `def pace_sec(seconds, km):` / `    if km <= 0: ____ None` / `    return seconds / km` so invalid distances exit early with `None`. Which keyword fills the blank?

- A. `yield`
- B. `pass`
- C. `return`
- D. `continue`

### 45. A coach writes `def announce(laps): print(laps * 3)` with no `return` statement and runs `res = announce(6)`. What value is stored in `res`?

- A. `None`
- B. `0`
- C. `18`
- D. `TypeError`

### 46. Complete `def rep_counter(limit):` / `    n = 1` / `    while n <= limit:` / `        ____ n` / `        n += 1` so calling `rep_counter(4)` produces a lazy generator iterator. Which keyword fills the blank?

- A. `yield`
- B. `break`
- C. `return`
- D. `from`

### 47. A cadence helper defines `def pulses(): yield 10; yield 20`, binds `g = pulses()`, and prints `next(g)`. What integer is printed?

- A. `20`
- B. `[]`, because a generator iterator is single-pass and already exhausted after the first `list(g)` call
- C. `StopIteration`
- D. `10`

### 48. A recursive cooldown helper defines `def total_reps(r): return 0 if r <= 0 else r + total_reps(r - 1)` and evaluates `total_reps(5)`. What integer is returned?

- A. `5`
- B. `15`
- C. `RecursionError`
- D. `120`

### 49. A coaching app uses a recursive function to subdivide training blocks. Which two properties prevent infinite recursion and `RecursionError`? Select two.

- A. A reachable base case that returns directly without making another recursive call
- B. Declaring every parameter `global` inside the function header
- C. A recursive call whose arguments move strictly closer to the base case on each step
- D. Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production
- E. Replacing every `return` statement with `break` inside the `def` body

### 50. A calorie estimator defines `def calc(base, rate): return base * rate`. Which two calls are valid in Python 3? Select two.

- A. `calc(100, rate=0.2)`
- B. `calc(100, tax=0.2)`
- C. `calc(base=100, 0.2)`
- D. `calc(100, base=200)`
- E. `calc(rate=0.2, base=100)`

### 51. Given `def split_time(dist, mins=25): return mins / dist`, what happens at runtime when a caller invokes `split_time(5, dist=10)`?

- A. `TypeError` because the same parameter receives both a positional argument and a keyword argument
- B. `None`
- C. `SyntaxError` because a positional argument cannot follow a keyword argument at a call site
- D. `2.5`

### 52. Given `def pace(minutes, km=2.0): return minutes / km`, what float does `pace(5)` evaluate to?

- A. `6.0`
- B. `5`
- C. `2.5`
- D. `TypeError`

### 53. A lap helper defines `def save_lap(lap, log=[]): log.append(lap); return log` and runs `save_lap(1)` followed by `save_lap(2)`. What happens on the second call?

- A. `None`
- B. `[2]`
- C. `[[1, 2], [1, 2]]` or `[1, 2]` on the second call because both calls mutated the same default list
- D. `TypeError`

### 54. Module scope sets `streak = 7`, and `def step(): print(streak); streak += 1` is called without `global`. What happens and why?

- A. `None`
- B. `UnboundLocalError` because assigning to the variable anywhere in the function marks it local across the entire function body
- C. Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`
- D. Assigning to a name inside a function without `global` creates a separate local variable, leaving the module-level variable unchanged

### 55. In a workout tracker module, which two actions inside a function work on module-level objects WITHOUT a `global` declaration? Select two.

- A. Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`
- B. Calling `.append()` on a module-level list inside a function mutates that list in place without needing `global`
- C. Cached `.pyc` files contain x86-64 machine instructions that run directly on the OS kernel without Python installed
- D. `UnboundLocalError` because assigning to the variable anywhere in the function marks it local across the entire function body
- E. Declaring every parameter `global` inside the function header

### 56. Complete `try: parse_split(raw)` / `except ____:` / `    bad_rows += 1` so the handler catches `ValueError`, `TypeError`, `LookupError`, and `ArithmeticError` alike while still allowing `SystemExit` and `KeyboardInterrupt` to propagate. Which base class fills the blank?

- A. `ZeroDivisionError`
- B. `ArithmeticError`
- C. `LookupError`
- D. `Exception`

### 57. Which built-in exception class is a subclass of `SyntaxError` raised when lines inside a `def` or `for` block have misaligned indentation levels?

- A. `KeyError`
- B. `ValueError`
- C. `IndentationError`
- D. `ZeroDivisionError`

### 58. A timer script executes `assert laps > 0` when `laps` is `0`. Which exception is raised?

- A. `ValueError`
- B. `TypeError`
- C. `AssertionError`
- D. `KeyError`

### 59. Complete `if bpm > 240:` / `    ____ ValueError('sensor spike out of range')` to signal an invalid heart-rate spike explicitly. Which keyword fills the blank?

- A. `with`
- B. `raise`
- C. `finally`
- D. `except`

### 60. A pace parser chains multiple `except` clauses after one `try:` block. Which two statements accurately describe handler ordering in Python 3? Select two.

- A. An earlier `except Exception:` (or `except LookupError:`) catches subclass errors first, making a later subclass handler unreachable
- B. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes
- C. Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production
- D. Place specific subclass handlers (such as `except ZeroDivisionError:`) BEFORE broader parent handlers (such as `except ArithmeticError:` or `except Exception:`)
- E. `T-X-E-F`

---

## Answer key and explanations

### Question 1 — A, C

Answers: Cached `.pyc` files store compiled Python bytecode so unchanged imported modules skip reparsing on later runs; When an unhandled runtime error occurs, CPython halts execution at the failing bytecode step after running earlier statements. Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred. Files under `__pycache__` hold version-tagged bytecode that speeds up module imports without changing program semantics or removing the need for the PVM. Because CPython executes top-to-bottom at runtime, side effects from earlier statements have already happened when a later line raises an unhandled exception. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Because CPython executes top-to-bottom at runtime, side effects from earlier statements have already happened when a later line raises an unhandled exception. In this case: Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred.
- **B:** Incorrect for this question. `.pyc` files store portable CPython bytecode for the Python virtual machine, not standalone native CPU machine code. Why the correct answer wins: Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred.
- **C:** Correct. Files under `__pycache__` hold version-tagged bytecode that speeds up module imports without changing program semantics or removing the need for the PVM. In this case: Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred.
- **D:** Incorrect for this question. `.pyc` files are neither encrypted nor able to bypass syntax validation. Why the correct answer wins: Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred.
- **E:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Cached `.pyc` files save bytecode so unchanged imported modules skip reparsing, and an unhandled runtime exception halts at the failing step after earlier side effects have already occurred.

### Question 2 — B

Answer: A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules. Omitting `:` after an `if` condition breaks Python's compound-statement grammar even though every token is lexically legal, making it a syntactic error. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Why the correct answer wins: Omitting `:` after an `if` condition breaks Python's compound-statement grammar even though every token is lexically legal, making it a syntactic error.
- **B:** Correct. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. In this case: Omitting `:` after an `if` condition breaks Python's compound-statement grammar even though every token is lexically legal, making it a syntactic error.
- **C:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Omitting `:` after an `if` condition breaks Python's compound-statement grammar even though every token is lexically legal, making it a syntactic error.
- **D:** Incorrect for this question. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Why the correct answer wins: Omitting `:` after an `if` condition breaks Python's compound-statement grammar even though every token is lexically legal, making it a syntactic error.

### Question 3 — C, E

Answers: `nonlocal`; `assert`. `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Only capitalized `None` is a reserved keyword; lowercase `none` is a valid variable name. Why the correct answer wins: `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved.
- **B:** Incorrect for this question. `match` is a soft keyword in Python 3.10+, so unlike hard keywords it remains usable as a variable identifier. Why the correct answer wins: `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved.
- **C:** Correct. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. In this case: `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved.
- **D:** Incorrect for this question. `max` is a built-in function identifier, not a hard keyword in Python 3. Why the correct answer wins: `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved.
- **E:** Correct. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. In this case: `nonlocal` and `assert` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `max` is a built-in function name, and `none` in lowercase is unreserved.

### Question 4 — B, D

Answers: `4e2`; `0b1101`. `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`. `4e2` uses exponent notation and evaluates to the `float` `400.0`, not the `int` `400`. `0b1101` is a valid binary integer literal equal to `8 + 4 + 0 + 1 == 13`. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Non-zero decimal integer literals cannot start with a leading `0` in Python 3; octal requires `0o45`. Why the correct answer wins: `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`.
- **B:** Correct. `4e2` uses exponent notation and evaluates to the `float` `400.0`, not the `int` `400`. In this case: `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`.
- **C:** Incorrect for this question. Numeric literals cannot end with a trailing underscore (`500_` raises `SyntaxError`). Why the correct answer wins: `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`.
- **D:** Correct. `0b1101` is a valid binary integer literal equal to `8 + 4 + 0 + 1 == 13`. In this case: `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`.
- **E:** Incorrect for this question. Hexadecimal digits stop at `F`/`f`, so `0x1G` raises `SyntaxError`. Why the correct answer wins: `4e2` (`400.0`) is a valid scientific-notation float literal and `0b1101` (`13`) is a valid binary integer literal, whereas `045`, `500_`, and `0x1G` raise `SyntaxError`.

### Question 5 — B

Answer: `_lap_count`. `_lap_count` begins with an underscore and contains only lowercase letters and underscores, whereas `2nd_quarter`, `seat count`, and `user@host` violate identifier syntax. `_lap_count` begins with an underscore and follows valid identifier syntax. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier. Why the correct answer wins: `_lap_count` begins with an underscore and contains only lowercase letters and underscores, whereas `2nd_quarter`, `seat count`, and `user@host` violate identifier syntax.
- **B:** Correct. `_lap_count` begins with an underscore and follows valid identifier syntax. In this case: `_lap_count` begins with an underscore and contains only lowercase letters and underscores, whereas `2nd_quarter`, `seat count`, and `user@host` violate identifier syntax.
- **C:** Incorrect for this question. `@` is the matrix-multiplication / decorator token and cannot appear inside an identifier. Why the correct answer wins: `_lap_count` begins with an underscore and contains only lowercase letters and underscores, whereas `2nd_quarter`, `seat count`, and `user@host` violate identifier syntax.
- **D:** Incorrect for this question. Whitespace separates tokens and cannot appear inside a single variable name. Why the correct answer wins: `_lap_count` begins with an underscore and contains only lowercase letters and underscores, whereas `2nd_quarter`, `seat count`, and `user@host` violate identifier syntax.

### Question 6 — D

Answer: `%`. Modulo `145 % 60` returns the integer remainder `25`, whereas `145 // 60` returns the `2` full minutes. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. True division `/` always returns a `float` in Python 3, even when both operands divide evenly (`8 / 2 == 4.0`). Why the correct answer wins: Modulo `145 % 60` returns the integer remainder `25`, whereas `145 // 60` returns the `2` full minutes.
- **B:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: Modulo `145 % 60` returns the integer remainder `25`, whereas `145 // 60` returns the `2` full minutes.
- **C:** Incorrect for this question. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: Modulo `145 % 60` returns the integer remainder `25`, whereas `145 // 60` returns the `2` full minutes.
- **D:** Correct. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). In this case: Modulo `145 % 60` returns the integer remainder `25`, whereas `145 // 60` returns the `2` full minutes.

### Question 7 — C

Answer: `9`. Modulo `%` and multiplication `*` share the same precedence tier and bind left to right, computing `18 % 5` (`3`) first and then `3 * 3 == 9`. Evaluates to the integer `9`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Modulo `%` and multiplication `*` share the same precedence tier and bind left to right, computing `18 % 5` (`3`) first and then `3 * 3 == 9`.
- **B:** Incorrect for this question. Evaluates to the integer `-9`. Why the correct answer wins: Modulo `%` and multiplication `*` share the same precedence tier and bind left to right, computing `18 % 5` (`3`) first and then `3 * 3 == 9`.
- **C:** Correct. Evaluates to the integer `9`. In this case: Modulo `%` and multiplication `*` share the same precedence tier and bind left to right, computing `18 % 5` (`3`) first and then `3 * 3 == 9`.
- **D:** Incorrect for this question. Evaluates to the integer `19`. Why the correct answer wins: Modulo `%` and multiplication `*` share the same precedence tier and bind left to right, computing `18 % 5` (`3`) first and then `3 * 3 == 9`.

### Question 8 — C

Answer: `|`. Bitwise OR sets every bit position that is `1` in at least one operand (`0b1001` combined with `0b0101` equals `0b1101`, or `13`). Bitwise OR `|` sets each output bit to `1` whenever at least one integer operand has `1`. Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. Why the correct answer wins: Bitwise OR sets every bit position that is `1` in at least one operand (`0b1001` combined with `0b0101` equals `0b1101`, or `13`).
- **B:** Incorrect for this question. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. Why the correct answer wins: Bitwise OR sets every bit position that is `1` in at least one operand (`0b1001` combined with `0b0101` equals `0b1101`, or `13`).
- **C:** Correct. Bitwise OR `|` sets each output bit to `1` whenever at least one integer operand has `1`. In this case: Bitwise OR sets every bit position that is `1` in at least one operand (`0b1001` combined with `0b0101` equals `0b1101`, or `13`).
- **D:** Incorrect for this question. Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Why the correct answer wins: Bitwise OR sets every bit position that is `1` in at least one operand (`0b1001` combined with `0b0101` equals `0b1101`, or `13`).

### Question 9 — B

Answer: `'252525'`. Multiplying a `str` by integer `3` performs sequence repetition rather than numeric multiplication, producing `'252525'`. Multiplying string `'25'` by `3` repeats the characters to form `'252525'`. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Multiplying a `str` by integer `3` performs sequence repetition rather than numeric multiplication, producing `'252525'`.
- **B:** Correct. Multiplying string `'25'` by `3` repeats the characters to form `'252525'`. In this case: Multiplying a `str` by integer `3` performs sequence repetition rather than numeric multiplication, producing `'252525'`.
- **C:** Incorrect for this question. Repeating the two-character string `'12'` with `* 2` concatenates `'1212'` rather than multiplying numerically. Why the correct answer wins: Multiplying a `str` by integer `3` performs sequence repetition rather than numeric multiplication, producing `'252525'`.
- **D:** Incorrect for this question. Evaluates to the integer `36`. Why the correct answer wins: Multiplying a `str` by integer `3` performs sequence repetition rather than numeric multiplication, producing `'252525'`.

### Question 10 — D

Answer: `sep=':'`. Passing `sep=':'` joins the three two-digit strings with colons instead of spaces. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `sep='/'` joins multiple `print()` arguments with a forward slash instead of the default single space. Why the correct answer wins: Passing `sep=':'` joins the three two-digit strings with colons instead of spaces.
- **B:** Incorrect for this question. `end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line. Why the correct answer wins: Passing `sep=':'` joins the three two-digit strings with colons instead of spaces.
- **C:** Incorrect for this question. `end=''` suppresses the trailing newline at the end of a `print()` call. Why the correct answer wins: Passing `sep=':'` joins the three two-digit strings with colons instead of spaces.
- **D:** Correct. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. In this case: Passing `sep=':'` joins the three two-digit strings with colons instead of spaces.

### Question 11 — B

Answer: `<class 'str'>` because `input()` always returns text even when the user types digits. `input()` always returns user keystrokes as a `str` (`'180'`), never auto-converting digits to `int`. `input()` reads a line from standard input and strips the trailing newline, always returning a `str` object. Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the floating-point value `2.0`. Why the correct answer wins: `input()` always returns user keystrokes as a `str` (`'180'`), never auto-converting digits to `int`.
- **B:** Correct. `input()` reads a line from standard input and strips the trailing newline, always returning a `str` object. In this case: `input()` always returns user keystrokes as a `str` (`'180'`), never auto-converting digits to `int`.
- **C:** Incorrect for this question. Evaluates to the floating-point value `0.0`. Why the correct answer wins: `input()` always returns user keystrokes as a `str` (`'180'`), never auto-converting digits to `int`.
- **D:** Incorrect for this question. Unlike Python 2's `input()`, Python 3's `input()` never evaluates or auto-casts typed digits. Why the correct answer wins: `input()` always returns user keystrokes as a `str` (`'180'`), never auto-converting digits to `int`.

### Question 12 — B

Answer: `elif`. `elif` tests `pace < 5.5` only when `pace < 4.5` evaluated to `False`. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `elif` tests `pace < 5.5` only when `pace < 4.5` evaluated to `False`.
- **B:** Correct. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. In this case: `elif` tests `pace < 5.5` only when `pace < 4.5` evaluated to `False`.
- **C:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `elif` tests `pace < 5.5` only when `pace < 4.5` evaluated to `False`.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `elif` tests `pace < 5.5` only when `pace < 4.5` evaluated to `False`.

### Question 13 — A

Answer: `GOLD`. `days >= 30` matches immediately for `35`, printing `GOLD` and skipping the remaining `elif` and `else` clauses. Prints `GOLD`. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Prints `GOLD`. In this case: `days >= 30` matches immediately for `35`, printing `GOLD` and skipping the remaining `elif` and `else` clauses.
- **B:** Incorrect for this question. Prints `BRONZE`. Why the correct answer wins: `days >= 30` matches immediately for `35`, printing `GOLD` and skipping the remaining `elif` and `else` clauses.
- **C:** Incorrect for this question. Prints `SILVER`. Why the correct answer wins: `days >= 30` matches immediately for `35`, printing `GOLD` and skipping the remaining `elif` and `else` clauses.
- **D:** Incorrect for this question. Prints both `GOLD` and `SILVER` when two independent `if` statements both match. Why the correct answer wins: `days >= 30` matches immediately for `35`, printing `GOLD` and skipping the remaining `elif` and `else` clauses.

### Question 14 — C

Answer: `else`. `else` is required in every Python conditional expression (`<true_expr> if <cond> else <false_expr>`). `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `else` is required in every Python conditional expression (`<true_expr> if <cond> else <false_expr>`).
- **B:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `else` is required in every Python conditional expression (`<true_expr> if <cond> else <false_expr>`).
- **C:** Correct. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. In this case: `else` is required in every Python conditional expression (`<true_expr> if <cond> else <false_expr>`).
- **D:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: `else` is required in every Python conditional expression (`<true_expr> if <cond> else <false_expr>`).

### Question 15 — C

Answer: `28`. Both independent `if` statements evaluate to `True` for `22`, adding `3` and then `5` to reach `28`. Evaluates to the integer `28`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: Both independent `if` statements evaluate to `True` for `22`, adding `3` and then `5` to reach `28`.
- **B:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: Both independent `if` statements evaluate to `True` for `22`, adding `3` and then `5` to reach `28`.
- **C:** Correct. Evaluates to the integer `28`. In this case: Both independent `if` statements evaluate to `True` for `22`, adding `3` and then `5` to reach `28`.
- **D:** Incorrect for this question. Evaluates to the integer `23`. Why the correct answer wins: Both independent `if` statements evaluate to `True` for `22`, adding `3` and then `5` to reach `28`.

### Question 16 — D, E

Answers: `''`; `None`. Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`. An empty string `''` has length `0` and evaluates to `False` in a Boolean context. `None` always evaluates to `False` in a Boolean context. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `['']` is a 1-element list containing an empty string, so the list itself has length `1` and is truthy. Why the correct answer wins: Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`.
- **B:** Incorrect for this question. `'0'` is a 1-character string (`len('0') == 1`), so it is truthy (`bool('0') is True`). Why the correct answer wins: Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`.
- **C:** Incorrect for this question. `' '` contains one space character (`len(' ') == 1`), so it is truthy. Why the correct answer wins: Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`.
- **D:** Correct. An empty string `''` has length `0` and evaluates to `False` in a Boolean context. In this case: Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`.
- **E:** Correct. `None` always evaluates to `False` in a Boolean context. In this case: Empty string `''` and `None` are falsy, whereas `'0'`, `' '`, and `['']` all have length `1` and evaluate to `True`.

### Question 17 — D

Answer: `True`. For integers, only `0` is falsy; every non-zero integer including `-1` converts to `True` under `bool()`. Evaluates to Boolean `True`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: For integers, only `0` is falsy; every non-zero integer including `-1` converts to `True` under `bool()`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: For integers, only `0` is falsy; every non-zero integer including `-1` converts to `True` under `bool()`.
- **C:** Incorrect for this question. Evaluates to the integer `-1`. Why the correct answer wins: For integers, only `0` is falsy; every non-zero integer including `-1` converts to `True` under `bool()`.
- **D:** Correct. Evaluates to Boolean `True`. In this case: For integers, only `0` is falsy; every non-zero integer including `-1` converts to `True` under `bool()`.

### Question 18 — B, D

Answers: `120 <= bpm < 160`; `bpm >= 120 and bpm < 160`. `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`. Chained comparison `120 <= bpm < 160` is `True` when `bpm` is at least `120` and strictly below `160`. Joining both bounds with `and` checks `[120, 160)` accurately. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Using `<= 160` includes `160`, violating a strict upper bound `< 160`. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`.
- **B:** Correct. Chained comparison `120 <= bpm < 160` is `True` when `bpm` is at least `120` and strictly below `160`. In this case: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`.
- **C:** Incorrect for this question. Using `or` returns `True` for every number. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`.
- **D:** Correct. Joining both bounds with `and` checks `[120, 160)` accurately. In this case: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`.
- **E:** Incorrect for this question. Bitwise `&` binds tighter than comparisons, evaluating `120 & bpm` first. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`.

### Question 19 — D

Answer: `'guest'`. Because `''` is falsy, short-circuit `or` evaluates and returns its right-hand operand `'guest'`. Short-circuit `'' or 'guest'` returns `'guest'`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Because `''` is falsy, short-circuit `or` evaluates and returns its right-hand operand `'guest'`.
- **B:** Incorrect for this question. An empty string `''` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: Because `''` is falsy, short-circuit `or` evaluates and returns its right-hand operand `'guest'`.
- **C:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Because `''` is falsy, short-circuit `or` evaluates and returns its right-hand operand `'guest'`.
- **D:** Correct. Short-circuit `'' or 'guest'` returns `'guest'`. In this case: Because `''` is falsy, short-circuit `or` evaluates and returns its right-hand operand `'guest'`.

### Question 20 — D

Answer: `while`. `while` repeats the body as long as `seconds_left > 0` evaluates to `True`. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `while` repeats the body as long as `seconds_left > 0` evaluates to `True`.
- **B:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` repeats the body as long as `seconds_left > 0` evaluates to `True`.
- **C:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` repeats the body as long as `seconds_left > 0` evaluates to `True`.
- **D:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` repeats the body as long as `seconds_left > 0` evaluates to `True`.

### Question 21 — D

Answer: `21`. Summing integers `1 + 2 + 3 + 4 + 5 + 6` across six iterations produces `21` before `r` becomes `7`. Evaluates to the integer `21`. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `28`. Why the correct answer wins: Summing integers `1 + 2 + 3 + 4 + 5 + 6` across six iterations produces `21` before `r` becomes `7`.
- **B:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Summing integers `1 + 2 + 3 + 4 + 5 + 6` across six iterations produces `21` before `r` becomes `7`.
- **C:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Summing integers `1 + 2 + 3 + 4 + 5 + 6` across six iterations produces `21` before `r` becomes `7`.
- **D:** Correct. Evaluates to the integer `21`. In this case: Summing integers `1 + 2 + 3 + 4 + 5 + 6` across six iterations produces `21` before `r` becomes `7`.

### Question 22 — A, E

Answers: `range(3, 12, 3)`; `range(9, 0, -3)`. `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five. `range(3, 12, 3)` generates `3, 6, 9` (three integers). `range(9, 0, -3)` generates `9, 6, 3` (three integers). Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `range(3, 12, 3)` generates `3, 6, 9` (three integers). In this case: `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five.
- **B:** Incorrect for this question. `range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers). Why the correct answer wins: `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five.
- **C:** Incorrect for this question. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. Why the correct answer wins: `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five.
- **D:** Incorrect for this question. `range(3, 9, 3)` stops before `9`, yielding only `3, 6` (two integers). Why the correct answer wins: `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five.
- **E:** Correct. `range(9, 0, -3)` generates `9, 6, 3` (three integers). In this case: `range(3, 12, 3)` yields `3, 6, 9` and `range(9, 0, -3)` yields `9, 6, 3`, whereas `range(3, 9, 3)` yields two, `range(2, 8, -2)` yields zero, and `range(0, 10, 2)` yields five.

### Question 23 — C

Answer: `20`. `range(2, 10, 2)` generates even numbers `2, 4, 6, 8`, whose sum is `20`. Evaluates to the integer `20`. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `range(2, 10, 2)` generates even numbers `2, 4, 6, 8`, whose sum is `20`.
- **B:** Incorrect for this question. Evaluates to the integer `30`. Why the correct answer wins: `range(2, 10, 2)` generates even numbers `2, 4, 6, 8`, whose sum is `20`.
- **C:** Correct. Evaluates to the integer `20`. In this case: `range(2, 10, 2)` generates even numbers `2, 4, 6, 8`, whose sum is `20`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `range(2, 10, 2)` generates even numbers `2, 4, 6, 8`, whose sum is `20`.

### Question 24 — C

Answer: `14`. Iterating directly over `[4, 6, 4]` visits each integer weight in sequence and sums them to `14`. Evaluates to the integer `14`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Iterating directly over `[4, 6, 4]` visits each integer weight in sequence and sums them to `14`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Iterating directly over `[4, 6, 4]` visits each integer weight in sequence and sums them to `14`.
- **C:** Correct. Evaluates to the integer `14`. In this case: Iterating directly over `[4, 6, 4]` visits each integer weight in sequence and sums them to `14`.
- **D:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Iterating directly over `[4, 6, 4]` visits each integer weight in sequence and sums them to `14`.

### Question 25 — A

Answer: `continue`. `continue` skips `recorded.append(split)` when `split == 0` and advances to the next lap split. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. In this case: `continue` skips `recorded.append(split)` when `split == 0` and advances to the next lap split.
- **B:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `continue` skips `recorded.append(split)` when `split == 0` and advances to the next lap split.
- **C:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `continue` skips `recorded.append(split)` when `split == 0` and advances to the next lap split.
- **D:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `continue` skips `recorded.append(split)` when `split == 0` and advances to the next lap split.

### Question 26 — A

Answer: `7`. `3` and `4` add `7` to `acc`; when `mins` reaches `9`, `break` exits the loop immediately before `9` or `5` is added. Evaluates to the integer `7`. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `7`. In this case: `3` and `4` add `7` to `acc`; when `mins` reaches `9`, `break` exits the loop immediately before `9` or `5` is added.
- **B:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: `3` and `4` add `7` to `acc`; when `mins` reaches `9`, `break` exits the loop immediately before `9` or `5` is added.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `3` and `4` add `7` to `acc`; when `mins` reaches `9`, `break` exits the loop immediately before `9` or `5` is added.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: `3` and `4` add `7` to `acc`; when `mins` reaches `9`, `break` exits the loop immediately before `9` or `5` is added.

### Question 27 — A, B

Answers: When a `for` loop finishes iterating over every element without executing `break`; When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`. The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception. Normal exhaustion of a `for` iterable runs the attached `else:` suite. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. In this case: The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception.
- **B:** Correct. Normal exhaustion of a `for` iterable runs the attached `else:` suite. In this case: The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception.
- **C:** Incorrect for this question. An unhandled exception unwinds out of the loop without running its `else:` suite. Why the correct answer wins: The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception.
- **D:** Incorrect for this question. `break` bypasses both the remaining iterations AND the loop's `else:` suite. Why the correct answer wins: The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception.
- **E:** Incorrect for this question. `return` exits the whole function immediately and skips any loop `else:` suite. Why the correct answer wins: The loop `else:` suite runs when a `for` loop exhausts every lap or a `while` condition turns `False` without hitting `break`, `return`, or an uncaught exception.

### Question 28 — A

Answer: `9`. Three stations multiplied by three rounds increments `slots` `3 * 3 == 9` times. Evaluates to the integer `9`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `9`. In this case: Three stations multiplied by three rounds increments `slots` `3 * 3 == 9` times.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Three stations multiplied by three rounds increments `slots` `3 * 3 == 9` times.
- **C:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Three stations multiplied by three rounds increments `slots` `3 * 3 == 9` times.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Three stations multiplied by three rounds increments `slots` `3 * 3 == 9` times.

### Question 29 — A

Answer: `[10, 30, 50]`. Omitting start and stop with stride `2` selects indices `0, 2, 4`, returning `[10, 30, 50]`. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. In this case: Omitting start and stop with stride `2` selects indices `0, 2, 4`, returning `[10, 30, 50]`.
- **B:** Incorrect for this question. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0, 2, 4`, returning `[10, 30, 50]`.
- **C:** Incorrect for this question. Slice `[-2:]` returns the last two items `[40, 50]`. Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0, 2, 4`, returning `[10, 30, 50]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0, 2, 4`, returning `[10, 30, 50]`.

### Question 30 — A

Answer: `20`. In a 5-element list, `-4` corresponds to positive index `5 - 4 == 1`, returning `20`. Evaluates to the integer `20`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `20`. In this case: In a 5-element list, `-4` corresponds to positive index `5 - 4 == 1`, returning `20`.
- **B:** Incorrect for this question. Evaluates to the integer `30`. Why the correct answer wins: In a 5-element list, `-4` corresponds to positive index `5 - 4 == 1`, returning `20`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: In a 5-element list, `-4` corresponds to positive index `5 - 4 == 1`, returning `20`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: In a 5-element list, `-4` corresponds to positive index `5 - 4 == 1`, returning `20`.

### Question 31 — B

Answer: `remove`. `lanes.remove(5)` deletes the first matching value `5` in place, whereas `lanes.pop(5)` would treat `5` as an index and raise `IndexError`. `.remove(value)` removes the first matching `value` by equality. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.append(item)` adds `item` as a single element at the end of a list. Why the correct answer wins: `lanes.remove(5)` deletes the first matching value `5` in place, whereas `lanes.pop(5)` would treat `5` as an index and raise `IndexError`.
- **B:** Correct. `.remove(value)` removes the first matching `value` by equality. In this case: `lanes.remove(5)` deletes the first matching value `5` in place, whereas `lanes.pop(5)` would treat `5` as an index and raise `IndexError`.
- **C:** Incorrect for this question. `.insert(index, item)` places `item` before `index` in the list. Why the correct answer wins: `lanes.remove(5)` deletes the first matching value `5` in place, whereas `lanes.pop(5)` would treat `5` as an index and raise `IndexError`.
- **D:** Incorrect for this question. `.pop([index])` removes and returns the element at `index` (default `-1`). Why the correct answer wins: `lanes.remove(5)` deletes the first matching value `5` in place, whereas `lanes.pop(5)` would treat `5` as an index and raise `IndexError`.

### Question 32 — A, B

Answers: `items.extend(seq)`; `items.pop()`. `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists. `.extend(seq)` mutates `items` in place by appending every element of `seq` and returns `None`. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `.extend(seq)` mutates `items` in place by appending every element of `seq` and returns `None`. In this case: `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists.
- **B:** Correct. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. In this case: `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists.
- **C:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists.
- **D:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists.
- **E:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: `items.extend(seq)` and `items.pop()` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new outer lists.

### Question 33 — A

Answer: `[10, 50]`. Deleting slice `vals[1:4]` removes indices `1, 2, 3` (`20, 30, 40`) in place, leaving `[10, 50]`. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. In this case: Deleting slice `vals[1:4]` removes indices `1, 2, 3` (`20, 30, 40`) in place, leaving `[10, 50]`.
- **B:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: Deleting slice `vals[1:4]` removes indices `1, 2, 3` (`20, 30, 40`) in place, leaving `[10, 50]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Deleting slice `vals[1:4]` removes indices `1, 2, 3` (`20, 30, 40`) in place, leaving `[10, 50]`.
- **D:** Incorrect for this question. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Why the correct answer wins: Deleting slice `vals[1:4]` removes indices `1, 2, 3` (`20, 30, 40`) in place, leaving `[10, 50]`.

### Question 34 — D, E

Answers: `items.copy()`; `list(items)`. `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. `list(items)` constructs a new outer list containing the same element references (a shallow copy). Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list.
- **B:** Incorrect for this question. `.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place. Why the correct answer wins: `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list.
- **C:** Incorrect for this question. `items.sort()` sorts the list in place and returns `None` rather than a new list. Why the correct answer wins: `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list.
- **D:** Correct. `list(items)` constructs a new outer list containing the same element references (a shallow copy). In this case: `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list.
- **E:** Correct. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. In this case: `items.copy()` and `list(items)` each construct a distinct outer list object, whereas `backup = items` aliases the original list.

### Question 35 — B

Answer: `in`. List comprehension clauses iterate with `for <target> in <iterable>`. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `not` is Python's unary logical negation operator and returns `True` or `False`. Why the correct answer wins: List comprehension clauses iterate with `for <target> in <iterable>`.
- **B:** Correct. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. In this case: List comprehension clauses iterate with `for <target> in <iterable>`.
- **C:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: List comprehension clauses iterate with `for <target> in <iterable>`.
- **D:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: List comprehension clauses iterate with `for <target> in <iterable>`.

### Question 36 — D

Answer: `not in`. `not in` evaluates to `True` when `lane` does not equal any element of `occupied_lanes`. `not in` tests non-membership and evaluates to `True` when the left operand is absent from the container. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `not in` evaluates to `True` when `lane` does not equal any element of `occupied_lanes`.
- **B:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `not in` evaluates to `True` when `lane` does not equal any element of `occupied_lanes`.
- **C:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `not in` evaluates to `True` when `lane` does not equal any element of `occupied_lanes`.
- **D:** Correct. `not in` tests non-membership and evaluates to `True` when the left operand is absent from the container. In this case: `not in` evaluates to `True` when `lane` does not equal any element of `occupied_lanes`.

### Question 37 — B

Answer: `(42)`. Without a comma, parentheses around `(42)` only group an arithmetic expression of type `int`; creating a 1-element tuple requires `(42,)` or `42,`. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. Why the correct answer wins: Without a comma, parentheses around `(42)` only group an arithmetic expression of type `int`; creating a 1-element tuple requires `(42,)` or `42,`.
- **B:** Correct. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). In this case: Without a comma, parentheses around `(42)` only group an arithmetic expression of type `int`; creating a 1-element tuple requires `(42,)` or `42,`.
- **C:** Incorrect for this question. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). Why the correct answer wins: Without a comma, parentheses around `(42)` only group an arithmetic expression of type `int`; creating a 1-element tuple requires `(42,)` or `42,`.
- **D:** Incorrect for this question. `tuple()` with no arguments returns the empty 0-element tuple `()`, not a 1-element tuple. Why the correct answer wins: Without a comma, parentheses around `(42)` only group an arithmetic expression of type `int`; creating a 1-element tuple requires `(42,)` or `42,`.

### Question 38 — D

Answer: `TypeError`. Lists are mutable and unhashable (`TypeError: unhashable type: 'list'`), so they cannot serve as dictionary keys. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Although a tuple cannot rebind its slots, mutating an existing list element in place via `t[1].append(3)` succeeds. Why the correct answer wins: Lists are mutable and unhashable (`TypeError: unhashable type: 'list'`), so they cannot serve as dictionary keys.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Lists are mutable and unhashable (`TypeError: unhashable type: 'list'`), so they cannot serve as dictionary keys.
- **C:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Lists are mutable and unhashable (`TypeError: unhashable type: 'list'`), so they cannot serve as dictionary keys.
- **D:** Correct. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. In this case: Lists are mutable and unhashable (`TypeError: unhashable type: 'list'`), so they cannot serve as dictionary keys.

### Question 39 — A, E

Answers: `rates.get('CHF', 0)`; `rates.pop('CHF', 0)`. Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`. `.get('CHF', 0)` returns the value for `'CHF'` if present or `0` if `'CHF'` is missing without raising `KeyError`. `.pop(k, default)` removes and returns `rates[k]` if found, or returns `default` without `KeyError` when `k` is absent. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `.pop(k, default)` removes and returns `rates[k]` if found, or returns `default` without `KeyError` when `k` is absent. In this case: Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`.
- **B:** Incorrect for this question. Unparenthesized `except A, B:` was Python 2 syntax and raises `SyntaxError` in Python 3. Why the correct answer wins: Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`.
- **C:** Incorrect for this question. Direct indexing `rates['CHF']` raises `KeyError` when `'CHF'` is absent from `rates`. Why the correct answer wins: Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`.
- **D:** Incorrect for this question. Placing positional `0.2` after keyword `base=100` raises `SyntaxError`. Why the correct answer wins: Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`.
- **E:** Correct. `.get('CHF', 0)` returns the value for `'CHF'` if present or `0` if `'CHF'` is missing without raising `KeyError`. In this case: Both `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` return fallback `0` when `'CHF'` is missing, whereas `rates['CHF']` raises `KeyError`.

### Question 40 — D, E

Answers: `.items()` yields `(key, value)` 2-tuples suitable for `for k, v in d.items():` unpacking; Duplicate keys in a literal keep a single entry whose value is the last assignment evaluated. Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples. `d.items()` returns a dynamic view of `(key, value)` pairs. When a dictionary literal repeats an equal key (including `1` and `True`), the later value overwrites the earlier value. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples.
- **B:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples.
- **C:** Incorrect for this question. In Python, `{ ... }` builds dictionaries or sets rather than delimiting statement suites. Why the correct answer wins: Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples.
- **D:** Correct. `d.items()` returns a dynamic view of `(key, value)` pairs. In this case: Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples.
- **E:** Correct. When a dictionary literal repeats an equal key (including `1` and `True`), the later value overwrites the earlier value. In this case: Duplicate keys in a literal keep a single entry holding the last value assigned, and `.items()` yields `(key, value)` 2-tuples.

### Question 41 — A

Answer: `65`. In ASCII and Unicode, uppercase `'A'` has code point `65` (while lowercase `'a'` has code point `97`). Evaluates to the integer `65` (`ord('A')`). Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `65` (`ord('A')`). In this case: In ASCII and Unicode, uppercase `'A'` has code point `65` (while lowercase `'a'` has code point `97`).
- **B:** Incorrect for this question. Evaluates to the integer `97` (`ord('a')`). Why the correct answer wins: In ASCII and Unicode, uppercase `'A'` has code point `65` (while lowercase `'a'` has code point `97`).
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: In ASCII and Unicode, uppercase `'A'` has code point `65` (while lowercase `'a'` has code point `97`).
- **D:** Incorrect for this question. Evaluates to the integer `42`. Why the correct answer wins: In ASCII and Unicode, uppercase `'A'` has code point `65` (while lowercase `'a'` has code point `97`).

### Question 42 — A

Answer: `'-'.join(parts)`. `join` is a method on the separator string `'-'`, so `'-'.join(parts)` returns `'5K-10K-21K'`, whereas `parts.join('-')` raises `AttributeError`. `sep.join(iterable)` is a method on the separator string and requires every element of `iterable` to be a `str`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `sep.join(iterable)` is a method on the separator string and requires every element of `iterable` to be a `str`. In this case: `join` is a method on the separator string `'-'`, so `'-'.join(parts)` returns `'5K-10K-21K'`, whereas `parts.join('-')` raises `AttributeError`.
- **B:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: `join` is a method on the separator string `'-'`, so `'-'.join(parts)` returns `'5K-10K-21K'`, whereas `parts.join('-')` raises `AttributeError`.
- **C:** Incorrect for this question. `list` has no `.join()` method (`AttributeError`); `.join()` belongs to `str`. Why the correct answer wins: `join` is a method on the separator string `'-'`, so `'-'.join(parts)` returns `'5K-10K-21K'`, whereas `parts.join('-')` raises `AttributeError`.
- **D:** Incorrect for this question. Placing non-default `amount` after default `rate=1.1` raises `SyntaxError`. Why the correct answer wins: `join` is a method on the separator string `'-'`, so `'-'.join(parts)` returns `'5K-10K-21K'`, whereas `parts.join('-')` raises `AttributeError`.

### Question 43 — D

Answer: `-1` because `.find()` returns `-1` instead of raising `ValueError` when a substring is absent. Unlike `.index()`, which raises `ValueError` on a missing substring, `str.find()` returns `-1`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Unlike `.index()`, which raises `ValueError` on a missing substring, `str.find()` returns `-1`.
- **B:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Unlike `.index()`, which raises `ValueError` on a missing substring, `str.find()` returns `-1`.
- **C:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Unlike `.index()`, which raises `ValueError` on a missing substring, `str.find()` returns `-1`.
- **D:** Correct. In this case: Unlike `.index()`, which raises `ValueError` on a missing substring, `str.find()` returns `-1`.

### Question 44 — C

Answer: `return`. `return None` exits `pace_sec` immediately before `seconds / km` can divide by zero. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Why the correct answer wins: `return None` exits `pace_sec` immediately before `seconds / km` can divide by zero.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `return None` exits `pace_sec` immediately before `seconds / km` can divide by zero.
- **C:** Correct. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. In this case: `return None` exits `pace_sec` immediately before `seconds / km` can divide by zero.
- **D:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `return None` exits `pace_sec` immediately before `seconds / km` can divide by zero.

### Question 45 — A

Answer: `None`. Because `announce` executes no `return` expression, Python implicitly returns `None` into `res`. Evaluates to `None`, Python's singleton null value. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to `None`, Python's singleton null value. In this case: Because `announce` executes no `return` expression, Python implicitly returns `None` into `res`.
- **B:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Because `announce` executes no `return` expression, Python implicitly returns `None` into `res`.
- **C:** Incorrect for this question. Evaluates to the integer `18`. Why the correct answer wins: Because `announce` executes no `return` expression, Python implicitly returns `None` into `res`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Because `announce` executes no `return` expression, Python implicitly returns `None` into `res`.

### Question 46 — A

Answer: `yield`. `yield n` suspends the frame on each repetition and resumes at `n += 1` on the next step. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. In this case: `yield n` suspends the frame on each repetition and resumes at `n += 1` on the next step.
- **B:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `yield n` suspends the frame on each repetition and resumes at `n += 1` on the next step.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `yield n` suspends the frame on each repetition and resumes at `n += 1` on the next step.
- **D:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `yield n` suspends the frame on each repetition and resumes at `n += 1` on the next step.

### Question 47 — D

Answer: `10`. The first `next(g)` call runs `pulses` up to the first `yield 10` and returns `10`, pausing before `yield 20`. Evaluates to the integer `10`. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: The first `next(g)` call runs `pulses` up to the first `yield 10` and returns `10`, pausing before `yield 20`.
- **B:** Incorrect for this question. Unlike a `list` or `range`, a generator object cannot be rewound; iterating it a second time yields zero elements. Why the correct answer wins: The first `next(g)` call runs `pulses` up to the first `yield 10` and returns `10`, pausing before `yield 20`.
- **C:** Incorrect for this question. Calling `next()` on an exhausted generator raises `StopIteration`. Why the correct answer wins: The first `next(g)` call runs `pulses` up to the first `yield 10` and returns `10`, pausing before `yield 20`.
- **D:** Correct. Evaluates to the integer `10`. In this case: The first `next(g)` call runs `pulses` up to the first `yield 10` and returns `10`, pausing before `yield 20`.

### Question 48 — B

Answer: `15`. `total_reps(5)` sums `5 + 4 + 3 + 2 + 1 + 0`, terminating at `r <= 0` with `15`. Evaluates to the integer `15`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: `total_reps(5)` sums `5 + 4 + 3 + 2 + 1 + 0`, terminating at `r <= 0` with `15`.
- **B:** Correct. Evaluates to the integer `15`. In this case: `total_reps(5)` sums `5 + 4 + 3 + 2 + 1 + 0`, terminating at `r <= 0` with `15`.
- **C:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `total_reps(5)` sums `5 + 4 + 3 + 2 + 1 + 0`, terminating at `r <= 0` with `15`.
- **D:** Incorrect for this question. Evaluates to the integer `120`. Why the correct answer wins: `total_reps(5)` sums `5 + 4 + 3 + 2 + 1 + 0`, terminating at `r <= 0` with `15`.

### Question 49 — A, C

Answers: A reachable base case that returns directly without making another recursive call; A recursive call whose arguments move strictly closer to the base case on each step. A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination. Valid finite recursion requires at least one non-recursive base branch. Without progress toward the base condition, recursion never terminates cleanly. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Valid finite recursion requires at least one non-recursive base branch. In this case: A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination.
- **B:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination.
- **C:** Correct. Without progress toward the base condition, recursion never terminates cleanly. In this case: A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination.
- **D:** Incorrect for this question. `.pyc` files are neither encrypted nor able to bypass syntax validation. Why the correct answer wins: A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination.
- **E:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: A non-recursive base case and recursive arguments that progress toward that base case are both required for finite termination.

### Question 50 — A, E

Answers: `calc(rate=0.2, base=100)`; `calc(100, rate=0.2)`. `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. In this case: `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules.
- **B:** Incorrect for this question. Passing an unknown keyword parameter name `tax` when the signature is `def calc(base, rate):` raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules.
- **C:** Incorrect for this question. Placing positional `0.2` after keyword `base=100` raises `SyntaxError`. Why the correct answer wins: `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules.
- **D:** Incorrect for this question. Passing `100` to `base` positionally and `base=200` by keyword raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules.
- **E:** Correct. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. In this case: `calc(rate=0.2, base=100)` and `calc(100, rate=0.2)` both obey Python's positional-before-keyword and single-binding rules.

### Question 51 — A

Answer: `TypeError` because the same parameter receives both a positional argument and a keyword argument. `dist` receives `5` positionally and `10` by keyword in the same call, raising `TypeError`. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. In this case: `dist` receives `5` positionally and `10` by keyword in the same call, raising `TypeError`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: `dist` receives `5` positionally and `10` by keyword in the same call, raising `TypeError`.
- **C:** Incorrect for this question. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. Why the correct answer wins: `dist` receives `5` positionally and `10` by keyword in the same call, raising `TypeError`.
- **D:** Incorrect for this question. Evaluates to the floating-point value `2.5`. Why the correct answer wins: `dist` receives `5` positionally and `10` by keyword in the same call, raising `TypeError`.

### Question 52 — C

Answer: `2.5`. Omitting `km` uses default `2.0`, so `5 / 2.0` evaluates to `2.5`. Evaluates to the floating-point value `2.5`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the floating-point value `6.0`. Why the correct answer wins: Omitting `km` uses default `2.0`, so `5 / 2.0` evaluates to `2.5`.
- **B:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Omitting `km` uses default `2.0`, so `5 / 2.0` evaluates to `2.5`.
- **C:** Correct. Evaluates to the floating-point value `2.5`. In this case: Omitting `km` uses default `2.0`, so `5 / 2.0` evaluates to `2.5`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Omitting `km` uses default `2.0`, so `5 / 2.0` evaluates to `2.5`.

### Question 53 — C

Answer: `[[1, 2], [1, 2]]` or `[1, 2]` on the second call because both calls mutated the same default list. Because default `log=[]` is allocated once when `def` executes, both default calls share the same list and the second call returns `[1, 2]`. When `def add(x, acc=[]): acc.append(x); return acc` is called as `add(1)` then `add(2)`, the second call returns `[1, 2]`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Because default `log=[]` is allocated once when `def` executes, both default calls share the same list and the second call returns `[1, 2]`.
- **B:** Incorrect for this question. Evaluates to the single-element list `[2]`. Why the correct answer wins: Because default `log=[]` is allocated once when `def` executes, both default calls share the same list and the second call returns `[1, 2]`.
- **C:** Correct. When `def add(x, acc=[]): acc.append(x); return acc` is called as `add(1)` then `add(2)`, the second call returns `[1, 2]`. In this case: Because default `log=[]` is allocated once when `def` executes, both default calls share the same list and the second call returns `[1, 2]`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Because default `log=[]` is allocated once when `def` executes, both default calls share the same list and the second call returns `[1, 2]`.

### Question 54 — B

Answer: `UnboundLocalError` because assigning to the variable anywhere in the function marks it local across the entire function body. Augmented assignment `streak += 1` makes `streak` local across all of `step()`, so `print(streak)` reads an unassigned local and raises `UnboundLocalError`. Python determines local names at compile time; reading `x` before a later `x += 1` or `x = ...` in the same function raises `UnboundLocalError`. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Augmented assignment `streak += 1` makes `streak` local across all of `step()`, so `print(streak)` reads an unassigned local and raises `UnboundLocalError`.
- **B:** Correct. Python determines local names at compile time; reading `x` before a later `x += 1` or `x = ...` in the same function raises `UnboundLocalError`. In this case: Augmented assignment `streak += 1` makes `streak` local across all of `step()`, so `print(streak)` reads an unassigned local and raises `UnboundLocalError`.
- **C:** Incorrect for this question. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. Why the correct answer wins: Augmented assignment `streak += 1` makes `streak` local across all of `step()`, so `print(streak)` reads an unassigned local and raises `UnboundLocalError`.
- **D:** Incorrect for this question. Under Python's LEGB rule, local assignment binds in the function's local frame rather than mutating the module global. Why the correct answer wins: Augmented assignment `streak += 1` makes `streak` local across all of `step()`, so `print(streak)` reads an unassigned local and raises `UnboundLocalError`.

### Question 55 — A, B

Answers: Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`; Calling `.append()` on a module-level list inside a function mutates that list in place without needing `global`. Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. Method calls mutate an existing object rather than rebinding the variable name, so Python resolves the name in module scope. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. In this case: Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`.
- **B:** Correct. Method calls mutate an existing object rather than rebinding the variable name, so Python resolves the name in module scope. In this case: Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`.
- **C:** Incorrect for this question. `.pyc` files store portable CPython bytecode for the Python virtual machine, not standalone native CPU machine code. Why the correct answer wins: Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`.
- **D:** Incorrect for this question. Python determines local names at compile time; reading `x` before a later `x += 1` or `x = ...` in the same function raises `UnboundLocalError`. Why the correct answer wins: Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`.
- **E:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Reading a module-level scalar without rebinding it and calling `.append()` on a module-level list both work via LEGB lookup without `global`.

### Question 56 — D

Answer: `Exception`. `Exception` sits directly under `BaseException` as the parent of standard non-exit runtime errors, whereas `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly. `Exception` is the base class for almost all runtime non-exit errors (`ValueError`, `TypeError`, `LookupError`, `ArithmeticError`), inheriting from `BaseException`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `Exception` sits directly under `BaseException` as the parent of standard non-exit runtime errors, whereas `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly.
- **B:** Incorrect for this question. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Why the correct answer wins: `Exception` sits directly under `BaseException` as the parent of standard non-exit runtime errors, whereas `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly.
- **C:** Incorrect for this question. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Why the correct answer wins: `Exception` sits directly under `BaseException` as the parent of standard non-exit runtime errors, whereas `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly.
- **D:** Correct. `Exception` is the base class for almost all runtime non-exit errors (`ValueError`, `TypeError`, `LookupError`, `ArithmeticError`), inheriting from `BaseException`. In this case: `Exception` sits directly under `BaseException` as the parent of standard non-exit runtime errors, whereas `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly.

### Question 57 — C

Answer: `IndentationError`. `IndentationError` inherits from `SyntaxError` and reports invalid block indentation at parse time. `IndentationError` (a subclass of `SyntaxError`) is raised when suite indentation levels do not align validly. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `IndentationError` inherits from `SyntaxError` and reports invalid block indentation at parse time.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `IndentationError` inherits from `SyntaxError` and reports invalid block indentation at parse time.
- **C:** Correct. `IndentationError` (a subclass of `SyntaxError`) is raised when suite indentation levels do not align validly. In this case: `IndentationError` inherits from `SyntaxError` and reports invalid block indentation at parse time.
- **D:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `IndentationError` inherits from `SyntaxError` and reports invalid block indentation at parse time.

### Question 58 — C

Answer: `AssertionError`. When an `assert` statement's expression evaluates to `False`, Python raises `AssertionError`. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: When an `assert` statement's expression evaluates to `False`, Python raises `AssertionError`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: When an `assert` statement's expression evaluates to `False`, Python raises `AssertionError`.
- **C:** Correct. In this case: When an `assert` statement's expression evaluates to `False`, Python raises `AssertionError`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: When an `assert` statement's expression evaluates to `False`, Python raises `AssertionError`.

### Question 59 — B

Answer: `raise`. `raise` triggers the `ValueError` exception immediately. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `raise` triggers the `ValueError` exception immediately.
- **B:** Correct. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. In this case: `raise` triggers the `ValueError` exception immediately.
- **C:** Incorrect for this question. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Why the correct answer wins: `raise` triggers the `ValueError` exception immediately.
- **D:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `raise` triggers the `ValueError` exception immediately.

### Question 60 — A, D

Answers: An earlier `except Exception:` (or `except LookupError:`) catches subclass errors first, making a later subclass handler unreachable; Place specific subclass handlers (such as `except ZeroDivisionError:`) BEFORE broader parent handlers (such as `except ArithmeticError:` or `except Exception:`). Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes. `except` clauses are tested top to bottom using `isinstance`, so a parent exception handler placed first intercepts all its subclasses. Ordering narrow subclasses before broader superclasses lets specialized handlers run before general fallbacks. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `except` clauses are tested top to bottom using `isinstance`, so a parent exception handler placed first intercepts all its subclasses. In this case: Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes.
- **B:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes.
- **C:** Incorrect for this question. `.pyc` files are neither encrypted nor able to bypass syntax validation. Why the correct answer wins: Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes.
- **D:** Correct. Ordering narrow subclasses before broader superclasses lets specialized handlers run before general fallbacks. In this case: Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes.
- **E:** Incorrect for this question. `except:` and `else:` are mutually exclusive on any single execution of a `try` statement. Why the correct answer wins: Placing a broad parent class like `except Exception:` first shadows later subclass handlers, so narrow subclasses like `ZeroDivisionError` should precede broader parent classes.
