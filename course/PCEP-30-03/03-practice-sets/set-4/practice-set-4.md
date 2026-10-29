# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 4

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 16 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A meteorology station runs `python3 station_logger.py` on a Linux logger box. Which two statements accurately describe how standard CPython compiles and runs that `.py` script? Select two.

- A. CPython flattens all imported modules into static ROM microcode before parsing syntax
- B. CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime
- C. CPython parses the entire `.py` file for syntax errors before executing even the first top-level statement
- D. CPython executes `.py` source only inside an HTML5 browser DOM engine
- E. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime

### 2. In a wind-chill converter, `summary = 'Wind: ' + 18` uses legal tokens and legal binary-operator grammar, yet raises `TypeError` when executed because Python refuses to add `int` directly to `str`. Which error category does this represent?

- A. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- B. A lexical error because the character or token itself does not belong to valid Python token forms
- C. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- D. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning

### 3. An engineer writing a barometer archive script checks whether candidate variable names collide with Python 3 keywords. Which two identifiers are hard reserved keywords? Select two.

- A. `case`
- B. `sum`
- C. `from`
- D. `false`
- E. `with`

### 4. A pressure-sensor calibration file defines numeric literals for microbar offsets and sea-level pascals. Which two literals are valid numeric literals in Python 3? Select two.

- A. `1_250_000`
- B. `2.5e-3`
- C. `045`
- D. `1__000`
- E. `0o19`

### 5. Which variable name is legal in Python 3 and follows PEP-8 snake_case style for storing a dew-point reading in degrees Celsius?

- A. `fx-rate`
- B. `dew_point_c`
- C. `unit.temp`
- D. `2nd_quarter`

### 6. A sub-zero temperature bucketing formula evaluates `bucket = -17 // 5` in Python 3. Because floor division rounds toward negative infinity, what integer is assigned to `bucket`?

- A. `4`
- B. `-4`
- C. `-3`
- D. `-3.0`

### 7. A frost-index formula parenthesizes the base before squaring: `score = (-4) ** 2`. What integer is bound to `score`?

- A. `4.0`
- B. `-16`
- C. `16`
- D. `8`

### 8. Complete `inverted = ____5` in a weather-register mask helper so two's-complement bit inversion flips every bit of `5` and evaluates to `-6`. Which unary bitwise operator fills the blank?

- A. `&`
- B. `^`
- C. `<<`
- D. `~`

### 9. Complete `kelvin_step = 29; kelvin_step ____ 4` so floor-dividing `29` by `4` updates `kelvin_step` in place to the integer `7`. Which augmented assignment operator fills the blank?

- A. `//=`
- B. `+=`
- C. `/`
- D. `*=`

### 10. Complete `print('Temp: 12C', ____)` followed by `print('RH: 60%')` so both readings appear on one line as `Temp: 12C, RH: 60%`. Which keyword argument fills the blank?

- A. `sep='/'`
- B. `sep=':'`
- C. `end=', '`
- D. `end='!'`

### 11. Complete `code_point = ____('A')` in a weather-beacon frame encoder so single-character string `'A'` converts to its integer ASCII/Unicode code point `65`. Which built-in callable fills the blank?

- A. `ord`
- B. `int`
- C. `str`
- D. `chr`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete the frost alert selector `if temp_c <= 0: state = 'FREEZE'` / `____ temp_c <= 4: state = 'FROST'` / `else: state = 'SAFE'` so `temp_c = 2` assigns `'FROST'` exclusively. Which keyword fills the blank?

- A. `elif`
- B. `while`
- C. `from`
- D. `else`

### 13. A wind-gust monitor sets `knots = 62` and runs `if knots >= 55: print('CRIT')` / `elif knots >= 40: print('ALERT')` / `elif knots >= 25: print('WARN')` / `else: print('OK')`. What is printed?

- A. `ALERT`
- B. `CRIT`
- C. `OK`
- D. `WARN`

### 14. A telemetry formatter chooses inline conditional expressions in Python 3. Which two expressions obey valid Python conditional-expression grammar? Select two.

- A. `0 if subtotal >= 50 else 5`
- B. `'VIP' if points >= 100 else 'STD'`
- C. `subtotal >= 50 ? 0 : 5`
- D. `0 if subtotal >= 50`
- E. `if subtotal >= 50 then 0 else 5`

### 15. A rain-gauge script sets `mm = 45; level = 'OK'` and executes two separate `if` statements: `if mm >= 20: level = 'WARN'` followed on the next line by `if mm >= 40: level = 'ALERT'`, then prints `level`. What is printed?

- A. `WARN`
- B. `ALERT`
- C. `OK`
- D. Nothing is printed

### 16. A telemetry filter tests `if reading:` before archiving sensor samples. Which two values of `reading` evaluate to `True` in Python? Select two.

- A. `None`
- B. `-1`
- C. `{}`
- D. `0.0`
- E. `'0'`

### 17. A barometer check sets `delta_hpa = 0.0` and runs `if delta_hpa: print('OK')` / `else: print('IDLE')`. What does it print?

- A. `WARN`
- B. `OK`
- C. `TypeError`
- D. `IDLE`

### 18. A UV sensor classifier needs an expression that evaluates to `True` when numeric variable `bpm` (sensor pulse rate) is at least `120` and strictly less than `160`. Which two expressions implement that check? Select two.

- A. `120 <= bpm < 160`
- B. `bpm >= 120 or bpm < 160`
- C. `120 <= bpm <= 160`
- D. `bpm >= 120 & bpm < 160`
- E. `bpm >= 120 and bpm < 160`

### 19. Complete `if count > 0 ____ (total / count) > 25.0: trigger_fan()` so short-circuit evaluation prevents `total / count` from running when `count` is `0`. Which logical operator fills the blank?

- A. `not`
- B. `is`
- C. `and`
- D. `or`

### 20. Complete `snow_cm = 12` / `____ snow_cm >= 3:` / `    snow_cm -= 3` so melt cycles repeat as long as at least `3` cm remain. Which keyword fills the blank?

- A. `elif`
- B. `for`
- C. `while`
- D. `pass`

### 21. A humidity decay loop sets `rh = 80; hours = 0` and runs `while rh > 50: rh -= 10; hours += 1`, then prints `hours`. What integer is printed?

- A. `4`
- B. `2`
- C. `3`
- D. `0`

### 22. A weather balloon samples altitude four times in a `for` loop. Which two `range()` expressions each produce exactly four iterations? Select two.

- A. `range(3, 9, 3)`
- B. `range(10, 2, -2)`
- C. `range(2, 10, 2)`
- D. `range(0, 10, 2)`
- E. `range(8, 2)`

### 23. A defrost countdown script runs `print(sum(range(7, 0, -3)))`. What integer does it print?

- A. `12`
- B. `7`
- C. `15`
- D. `8`

### 24. A daily rainfall tuple stores `drops = (4, 0, 11)` and a logger runs `acc = 0` / `for val in drops: acc += val` / `print(acc)`. What integer is printed?

- A. `15`
- B. `3`
- C. `5`
- D. `TypeError`

### 25. Complete `for probe in [-999, 14, -999, 18]:` / `    if probe == -999: ____` / `    valid_sum += probe` so sentinel `-999` readings are skipped without terminating the loop. Which keyword fills the blank?

- A. `continue`
- B. `break`
- C. `return`
- D. `pass`

### 26. Complete `for deg in readings:` / `    if deg == 0:` / `        ____` so the calibration branch parses cleanly as an intentional no-op without skipping later lines in the loop body. Which keyword fills the blank?

- A. `break`
- B. `continue`
- C. `return`
- D. `pass`

### 27. A storm detector runs `for gust in [18, 52, 24]:` / `    if gust >= 50: print('HALT'); break` / `else: print('CLEAN')`. What does it print?

- A. Nothing is printed
- B. `CLEAN`
- C. `SyntaxError`
- D. `HALT`

### 28. A two-sensor drift check sets `alerts = 0` and runs `for baseline in [10, 20]:` / `    for sample in [5, 15, 25]:` / `        if sample > baseline: alerts += 1` / `print(alerts)`. What integer is printed?

- A. `2`
- B. `4`
- C. `6`
- D. `3`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. Hourly temperatures are stored in `temps = [5, 15, 25, 35, 45]`. What list does `temps[1::2]` return?

- A. `[15, 35]`
- B. `[10, 30, 50]`
- C. `[20, 30]`
- D. `IndexError`

### 30. Given `temps = [5, 15, 25, 35, 45]`, what integer does negative subscript `temps[-1]` evaluate to?

- A. `45`
- B. `IndexError`
- C. `5`
- D. `25`

### 31. A weather buffer starts as `buf = [1, 2]`, executes `buf.append([3, 4])`, and prints `buf`. What list is printed?

- A. `TypeError`
- B. `None`
- C. `[1, 2, [3, 4]]`
- D. `[1, 2, 3, 4]`

### 32. A station archiver holds `items = [22, 18, 25]`. Which two calls mutate `items` in place and return `None`? Select two.

- A. `items[:]`
- B. `items.sort()`
- C. `sorted(items)`
- D. `items.append(x)`
- E. `items + [x]`

### 33. Complete `hourly = [10, 20, 30, 40, 50]; ____ hourly[1:4]` so middle readings at indices `1, 2, 3` are removed in place from `hourly`. Which keyword fills the blank?

- A. `with`
- B. `pass`
- C. `from`
- D. `del`

### 34. A forecaster holds flat list `items = [12, 15, 19]` and wants an independent shallow copy before sorting test scenarios. Which two expressions create a new shallow copy? Select two.

- A. `items.pop()`
- B. `items.append(x)`
- C. `backup = items`
- D. `items[:]`
- E. `items.copy()`

### 35. A frost counter builds `subzero = [t for t in [-4, 2, -1, 0, -7] if t < 0]` and prints `len(subzero)`. What integer is printed?

- A. `2`
- B. `3`
- C. `SyntaxError`
- D. `5`

### 36. A station lookup stores `stations = {'KORD': 204, 'KSEA': 132}` and evaluates `print('KORD' in stations)`. What is printed?

- A. `False`
- B. `None`
- C. `True`
- D. `KeyError`

### 37. A coordinate tuple `coord = (10, 20)` is unpacked via `lat, lon = coord` and the script prints `lat + lon`. What integer is printed?

- A. `20`
- B. `ValueError`
- C. `30`
- D. `10`

### 38. A climate grid maps `(latitude, longitude)` keys to station names in a `dict`. Which two statements accurately describe tuple hashability as dictionary keys? Select two.

- A. Membership `k in d` checks both keys and values simultaneously
- B. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- C. A tuple of immutable values (`(10, 20)`) can be used as a `dict` key, whereas a `list` (`[10, 20]`) raises `TypeError`
- D. A tuple containing a `list` (`(10, [20])`) cannot be used as a `dict` key and raises `TypeError`
- E. Curly braces `{ ... }` around `if` and `for` bodies so whitespace is completely ignored

### 39. Complete `elev_m = stations.____('KDEN', 1655)` so reading `'KDEN'` returns `1655` safely when `'KDEN'` is not yet in `stations`. Which dictionary method name fills the blank?

- A. `values`
- B. `get`
- C. `items`
- D. `keys`

### 40. A rain summary stores `totals = {'north': 12, 'south': 15}` and runs `acc = 0` / `for k, v in totals.items(): acc += v` / `print(acc)`. What integer is printed?

- A. `2`
- B. `27`
- C. `TypeError`
- D. `15`

### 41. A station display board stores a string literal containing an apostrophe (`Chef's kiss` in a test banner). Which two Python 3 string literals are syntactically valid? Select two.

- A. `"Chef's kiss"`
- B. `'Chef's kiss'`
- C. C-style `/* ... */` delimiters comment out multi-line blocks in Python
- D. `'Chef\'s kiss'`
- E. `'C:\temp\'`

### 42. Complete `fields = csv_line.____(',')` so `'12.4,65,1013'` is broken at commas into the three-element list `['12.4', '65', '1013']`. Which string method name fills the blank?

- A. `split`
- B. `strip`
- C. `replace`
- D. `find`

### 43. A beacon label stores `word = 'Python'` and evaluates `word[::2]`. Which string does that slice return?

- A. `'nohtyP'`
- B. `None`
- C. `IndexError`
- D. `'Pto'`

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Complete `____ c_to_f(celsius):` / `    return celsius * 9 / 5 + 32` to declare a named temperature-conversion function. Which keyword fills the blank?

- A. `lambda`
- B. `function`
- C. `def`
- D. `var`

### 45. An engineer reviews how functions exit in a unit-conversion library. Which two statements accurately describe `return` in a non-generator Python function? Select two.

- A. Declaring every parameter `global` inside the function header
- B. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- C. The first executed `return` exits the function immediately and skips all remaining statements in its body
- D. Replacing every `return` statement with `break` inside the `def` body
- E. `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`

### 46. Complete `stream = hourly_ticks(); first_tick = ____(stream)` so only the first yielded reading is pulled from generator `stream`. Which built-in callable fills the blank?

- A. `ord`
- B. `len`
- C. `int`
- D. `next`

### 47. A sensor daemon uses a generator function with `yield` to stream readings. Which two statements accurately describe how that generator works? Select two.

- A. Replacing every `return` statement with `break` inside the `def` body
- B. `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call
- C. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- D. Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet
- E. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes

### 48. A digit-checksum helper defines `def dsum(n): return n if n < 10 else (n % 10) + dsum(n // 10)` and evaluates `dsum(205)`. What integer is returned?

- A. `7`
- B. `RecursionError`
- C. `12`
- D. `3`

### 49. A tide simulator defines `def step(h): return step(h + 1)` without any terminating branch and calls `step(0)`. What happens?

- A. `SyntaxError`
- B. `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit
- C. `None`
- D. `0`

### 50. Given `def calibrate(raw, offset=0.5, scale=1.0): return (raw + offset) * scale`, what float does `calibrate(4.0)` return?

- A. `TypeError`
- B. `4.5`
- C. `SyntaxError`
- D. `3.5`

### 51. When calling `calibrate(offset=0.5, 4.0)` with a positional argument placed after a keyword argument, what happens?

- A. `TypeError` because the same parameter receives both a positional argument and a keyword argument
- B. `None`
- C. `SyntaxError` because a positional argument cannot follow a keyword argument at a call site
- D. `4.5`

### 52. A logger defines `def record(v, history=[]): history.append(v); return history` and observes readings persisting across independent calls. Which two statements describe why and how to fix it? Select two.

- A. Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument
- B. Declaring every parameter `global` inside the function header
- C. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- D. Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body
- E. Membership `k in d` checks both keys and values simultaneously

### 53. A converter header reads `def convert(unit='C', reading): return reading`. What happens when CPython parses the file?

- A. `TypeError`
- B. `SyntaxError` because a parameter without a default value cannot follow a parameter with a default value
- C. `def quote(amount, rate=1.1, fee=0):`
- D. `KeyError`

### 54. Complete `alert_count = 0` / `def mark_alert():` / `    ____ alert_count` / `    alert_count += 1` so `mark_alert()` updates module-level `alert_count` instead of failing with `UnboundLocalError`. Which keyword fills the blank?

- A. `global`
- B. `from`
- C. `nonlocal`
- D. `pass`

### 55. A module sets `offset = 5`, defines `def apply(x): return x + offset` with no assignment to `offset`, and prints `apply(20)`. What happens?

- A. `10`
- B. `UnboundLocalError`
- C. `25`
- D. `NameError`

### 56. Which two built-in exceptions subclass `BaseException` directly rather than inheriting from `Exception`? Select two.

- A. `ZeroDivisionError`
- B. `SystemExit`
- C. `TypeError`
- D. `KeyboardInterrupt`
- E. `IndexError`

### 57. Which built-in exception class is a subclass of `RuntimeError` raised when a function calls itself past Python's maximum call-stack depth?

- A. `KeyError`
- B. `IndexError`
- C. `ZeroDivisionError`
- D. `RecursionError`

### 58. A rainfall rate formula evaluates `rate = 12.0 / elapsed_hours` when `elapsed_hours` is `0.0`. Which concrete exception is raised?

- A. `KeyError`
- B. `ZeroDivisionError`
- C. `TypeError`
- D. `ValueError`

### 59. A unit-converter script runs `print(kelvin_offset)` before `kelvin_offset` has ever been assigned anywhere in scope. Which exception is raised?

- A. `NameError`
- B. `KeyError`
- C. `AttributeError`
- D. `ValueError`

### 60. Complete `try: val = table[key][idx]` / `____` / `    val = 0` so a single `except` header catches both `KeyError` and `IndexError` in Python 3. Which clause header fills the blank?

- A. `def quote(rate=1.1, amount, fee=0):`
- B. `subtotal >= 50 ? 0 : 5`
- C. `except KeyError, IndexError:`
- D. `except (KeyError, IndexError):`

---

## Answer key and explanations

### Question 1 — B, C

Answers: CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime; CPython parses the entire `.py` file for syntax errors before executing even the first top-level statement. CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable. Standard CPython translates source code into bytecode instructions executed by its runtime virtual machine rather than linking a native OS binary ahead of time. Because CPython compiles a script unit to bytecode before running it, a `SyntaxError` on line 50 prevents line 1 from executing at all. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. CPython parses source into an AST and bytecode at import or execution time rather than burning microcode. Why the correct answer wins: CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable.
- **B:** Correct. Standard CPython translates source code into bytecode instructions executed by its runtime virtual machine rather than linking a native OS binary ahead of time. In this case: CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable.
- **C:** Correct. Because CPython compiles a script unit to bytecode before running it, a `SyntaxError` on line 50 prevents line 1 from executing at all. In this case: CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable.
- **D:** Incorrect for this question. CPython is a native host process written in C, not a browser-embedded DOM engine. Why the correct answer wins: CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable.
- **E:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: CPython parses the full file for syntax errors into bytecode first and then runs that bytecode inside the Python virtual machine at runtime rather than producing a standalone native CPU executable.

### Question 2 — D

Answer: A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning. Both lexis and syntax are valid; applying `+` to incompatible runtime types (`str` and `int`) violates Python's runtime semantics. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Both lexis and syntax are valid; applying `+` to incompatible runtime types (`str` and `int`) violates Python's runtime semantics.
- **B:** Incorrect for this question. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Why the correct answer wins: Both lexis and syntax are valid; applying `+` to incompatible runtime types (`str` and `int`) violates Python's runtime semantics.
- **C:** Incorrect for this question. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Why the correct answer wins: Both lexis and syntax are valid; applying `+` to incompatible runtime types (`str` and `int`) violates Python's runtime semantics.
- **D:** Correct. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. In this case: Both lexis and syntax are valid; applying `+` to incompatible runtime types (`str` and `int`) violates Python's runtime semantics.

### Question 3 — C, E

Answers: `from`; `with`. `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `case` is a soft keyword in Python 3.10+, so assigning `case = 1` remains legal outside `match` headers. Why the correct answer wins: `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier.
- **B:** Incorrect for this question. `sum` is a built-in function name rather than a reserved keyword, though shadowing it is discouraged. Why the correct answer wins: `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier.
- **C:** Correct. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. In this case: `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier.
- **D:** Incorrect for this question. Python keywords are case-sensitive: `False` is reserved, whereas lowercase `false` is an ordinary identifier. Why the correct answer wins: `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier.
- **E:** Correct. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. In this case: `from` and `with` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an ordinary identifier.

### Question 4 — A, B

Answers: `2.5e-3`; `1_250_000`. `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`. Scientific-notation literals always evaluate to `float` in Python 3 (`2.5e-3 == 0.0025`). Single underscores between digits such as `1_250_000` are legal visual separators in Python 3.6+ numeric literals. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Single underscores between digits such as `1_250_000` are legal visual separators in Python 3.6+ numeric literals. In this case: `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`.
- **B:** Correct. Scientific-notation literals always evaluate to `float` in Python 3 (`2.5e-3 == 0.0025`). In this case: `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`.
- **C:** Incorrect for this question. Non-zero decimal integer literals cannot start with a leading `0` in Python 3; octal requires `0o45`. Why the correct answer wins: `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`.
- **D:** Incorrect for this question. Consecutive underscores inside a numeric literal (`1__000`) raise `SyntaxError`. Why the correct answer wins: `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`.
- **E:** Incorrect for this question. Octal literals allow only digits `0` through `7`, so `9` in `0o19` raises `SyntaxError`. Why the correct answer wins: `2.5e-3` (`0.0025`) is a valid scientific-notation float literal and `1_250_000` is a valid underscored integer literal, whereas `045`, `0o19`, and `1__000` raise `SyntaxError`.

### Question 5 — B

Answer: `dew_point_c`. `dew_point_c` starts with a lowercase letter and uses only letters and underscores, whereas `unit.temp`, `fx-rate`, and `2nd_quarter` are invalid variable identifiers. `dew_point_c` is a legal snake_case identifier starting with a letter. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `fx-rate` is parsed as subtraction `fx - rate` because hyphens are illegal in Python identifiers. Why the correct answer wins: `dew_point_c` starts with a lowercase letter and uses only letters and underscores, whereas `unit.temp`, `fx-rate`, and `2nd_quarter` are invalid variable identifiers.
- **B:** Correct. `dew_point_c` is a legal snake_case identifier starting with a letter. In this case: `dew_point_c` starts with a lowercase letter and uses only letters and underscores, whereas `unit.temp`, `fx-rate`, and `2nd_quarter` are invalid variable identifiers.
- **C:** Incorrect for this question. A dot `.` performs attribute lookup rather than forming part of one variable name. Why the correct answer wins: `dew_point_c` starts with a lowercase letter and uses only letters and underscores, whereas `unit.temp`, `fx-rate`, and `2nd_quarter` are invalid variable identifiers.
- **D:** Incorrect for this question. `2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier. Why the correct answer wins: `dew_point_c` starts with a lowercase letter and uses only letters and underscores, whereas `unit.temp`, `fx-rate`, and `2nd_quarter` are invalid variable identifiers.

### Question 6 — B

Answer: `-4`. `-17 / 5` is `-3.4`, and flooring toward negative infinity (`math.floor(-3.4)`) yields `-4` rather than truncating toward zero (`-3`). Evaluates to the integer `-4`. Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `-17 / 5` is `-3.4`, and flooring toward negative infinity (`math.floor(-3.4)`) yields `-4` rather than truncating toward zero (`-3`).
- **B:** Correct. Evaluates to the integer `-4`. In this case: `-17 / 5` is `-3.4`, and flooring toward negative infinity (`math.floor(-3.4)`) yields `-4` rather than truncating toward zero (`-3`).
- **C:** Incorrect for this question. Evaluates to the integer `-3`. Why the correct answer wins: `-17 / 5` is `-3.4`, and flooring toward negative infinity (`math.floor(-3.4)`) yields `-4` rather than truncating toward zero (`-3`).
- **D:** Incorrect for this question. Evaluates to the floating-point value `-3.0`. Why the correct answer wins: `-17 / 5` is `-3.4`, and flooring toward negative infinity (`math.floor(-3.4)`) yields `-4` rather than truncating toward zero (`-3`).

### Question 7 — C

Answer: `16`. Parentheses override `**`'s higher precedence over unary `-`, so Python squares `-4` directly (`(-4) * (-4)`) and produces `16`. Evaluates to the integer `16`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the floating-point value `4.0`. Why the correct answer wins: Parentheses override `**`'s higher precedence over unary `-`, so Python squares `-4` directly (`(-4) * (-4)`) and produces `16`.
- **B:** Incorrect for this question. Evaluates to the integer `-16`. Why the correct answer wins: Parentheses override `**`'s higher precedence over unary `-`, so Python squares `-4` directly (`(-4) * (-4)`) and produces `16`.
- **C:** Correct. Evaluates to the integer `16`. In this case: Parentheses override `**`'s higher precedence over unary `-`, so Python squares `-4` directly (`(-4) * (-4)`) and produces `16`.
- **D:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: Parentheses override `**`'s higher precedence over unary `-`, so Python squares `-4` directly (`(-4) * (-4)`) and produces `16`.

### Question 8 — D

Answer: `~`. Unary `~x` computes two's-complement bitwise inversion `-(x + 1)`, so `~5` evaluates to `-6`. Bitwise inversion `~x` flips all bits in two's-complement arithmetic and equals `-(x + 1)`. Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. Why the correct answer wins: Unary `~x` computes two's-complement bitwise inversion `-(x + 1)`, so `~5` evaluates to `-6`.
- **B:** Incorrect for this question. Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Why the correct answer wins: Unary `~x` computes two's-complement bitwise inversion `-(x + 1)`, so `~5` evaluates to `-6`.
- **C:** Incorrect for this question. Left shift `x << n` multiplies integer `x` by `2 ** n`. Why the correct answer wins: Unary `~x` computes two's-complement bitwise inversion `-(x + 1)`, so `~5` evaluates to `-6`.
- **D:** Correct. Bitwise inversion `~x` flips all bits in two's-complement arithmetic and equals `-(x + 1)`. In this case: Unary `~x` computes two's-complement bitwise inversion `-(x + 1)`, so `~5` evaluates to `-6`.

### Question 9 — A

Answer: `//=`. `kelvin_step //= 4` computes `29 // 4` (`7`) and assigns `7` back to `kelvin_step`. `//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable. In this case: `kelvin_step //= 4` computes `29 // 4` (`7`) and assigns `7` back to `kelvin_step`.
- **B:** Incorrect for this question. `+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets. Why the correct answer wins: `kelvin_step //= 4` computes `29 // 4` (`7`) and assigns `7` back to `kelvin_step`.
- **C:** Incorrect for this question. True division `/` always returns a `float` in Python 3, even when both operands divide evenly (`8 / 2 == 4.0`). Why the correct answer wins: `kelvin_step //= 4` computes `29 // 4` (`7`) and assigns `7` back to `kelvin_step`.
- **D:** Incorrect for this question. `*=` scales a number or repeats a sequence in place / by rebinding. Why the correct answer wins: `kelvin_step //= 4` computes `29 // 4` (`7`) and assigns `7` back to `kelvin_step`.

### Question 10 — C

Answer: `end=', '`. Passing `end=', '` replaces the first `print()`'s trailing newline with `', '` before the second `print()` outputs `RH: 60%`. `end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `sep='/'` joins multiple `print()` arguments with a forward slash instead of the default single space. Why the correct answer wins: Passing `end=', '` replaces the first `print()`'s trailing newline with `', '` before the second `print()` outputs `RH: 60%`.
- **B:** Incorrect for this question. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. Why the correct answer wins: Passing `end=', '` replaces the first `print()`'s trailing newline with `', '` before the second `print()` outputs `RH: 60%`.
- **C:** Correct. `end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line. In this case: Passing `end=', '` replaces the first `print()`'s trailing newline with `', '` before the second `print()` outputs `RH: 60%`.
- **D:** Incorrect for this question. `end='!'` finishes the printed line with `!` instead of `'\n'`. Why the correct answer wins: Passing `end=', '` replaces the first `print()`'s trailing newline with `', '` before the second `print()` outputs `RH: 60%`.

### Question 11 — A

Answer: `ord`. Built-in `ord('A')` returns integer code point `65`, whereas `int('A')` raises `ValueError` and `chr` expects an integer argument. `ord(ch)` returns the integer Unicode code point of a 1-character string (for example `ord('A') == 65`). Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `ord(ch)` returns the integer Unicode code point of a 1-character string (for example `ord('A') == 65`). In this case: Built-in `ord('A')` returns integer code point `65`, whereas `int('A')` raises `ValueError` and `chr` expects an integer argument.
- **B:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: Built-in `ord('A')` returns integer code point `65`, whereas `int('A')` raises `ValueError` and `chr` expects an integer argument.
- **C:** Incorrect for this question. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. Why the correct answer wins: Built-in `ord('A')` returns integer code point `65`, whereas `int('A')` raises `ValueError` and `chr` expects an integer argument.
- **D:** Incorrect for this question. `chr(code)` returns the 1-character string for integer Unicode code point `code` (for example `chr(65) == 'A'`). Why the correct answer wins: Built-in `ord('A')` returns integer code point `65`, whereas `int('A')` raises `ValueError` and `chr` expects an integer argument.

### Question 12 — A

Answer: `elif`. `elif` chains a mutually exclusive secondary condition after `if temp_c <= 0:`. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. In this case: `elif` chains a mutually exclusive secondary condition after `if temp_c <= 0:`.
- **B:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: `elif` chains a mutually exclusive secondary condition after `if temp_c <= 0:`.
- **C:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `elif` chains a mutually exclusive secondary condition after `if temp_c <= 0:`.
- **D:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `elif` chains a mutually exclusive secondary condition after `if temp_c <= 0:`.

### Question 13 — B

Answer: `CRIT`. The very first condition `knots >= 55` is `True` for `62`, so Python prints `CRIT` and skips every subsequent `elif` and `else` branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `ALERT`. Why the correct answer wins: The very first condition `knots >= 55` is `True` for `62`, so Python prints `CRIT` and skips every subsequent `elif` and `else` branch.
- **B:** Correct. In this case: The very first condition `knots >= 55` is `True` for `62`, so Python prints `CRIT` and skips every subsequent `elif` and `else` branch.
- **C:** Incorrect for this question. Prints `OK`. Why the correct answer wins: The very first condition `knots >= 55` is `True` for `62`, so Python prints `CRIT` and skips every subsequent `elif` and `else` branch.
- **D:** Incorrect for this question. Prints `WARN`. Why the correct answer wins: The very first condition `knots >= 55` is `True` for `62`, so Python prints `CRIT` and skips every subsequent `elif` and `else` branch.

### Question 14 — A, B

Answers: `0 if subtotal >= 50 else 5`; `'VIP' if points >= 100 else 'STD'`. `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`. Python's conditional expression has the form `<when_true> if <cond> else <when_false>`. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Python's conditional expression has the form `<when_true> if <cond> else <when_false>`. In this case: `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`.
- **B:** Correct. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. In this case: `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`.
- **C:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`.
- **D:** Incorrect for this question. A conditional expression (unlike a list comprehension filter) requires an `else` clause or raises `SyntaxError`. Why the correct answer wins: `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`.
- **E:** Incorrect for this question. Python has no `then` keyword and does not start an inline conditional expression with `if`. Why the correct answer wins: `<val_if_true> if <cond> else <val_if_false>` is required in Python; `? :` operators, missing `else`, and `if ... then` raise `SyntaxError`.

### Question 15 — B

Answer: `ALERT`. Because both `if` headers are independent, `mm = 45` triggers both assignments in sequence and `level` ends as `'ALERT'`. Prints `ALERT`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `WARN`. Why the correct answer wins: Because both `if` headers are independent, `mm = 45` triggers both assignments in sequence and `level` ends as `'ALERT'`.
- **B:** Correct. Prints `ALERT`. In this case: Because both `if` headers are independent, `mm = 45` triggers both assignments in sequence and `level` ends as `'ALERT'`.
- **C:** Incorrect for this question. Prints `OK`. Why the correct answer wins: Because both `if` headers are independent, `mm = 45` triggers both assignments in sequence and `level` ends as `'ALERT'`.
- **D:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: Because both `if` headers are independent, `mm = 45` triggers both assignments in sequence and `level` ends as `'ALERT'`.

### Question 16 — B, E

Answers: `'0'`; `-1`. Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy. `'0'` is a 1-character string (`len('0') == 1`), so it is truthy (`bool('0') is True`). Every non-zero integer, including negative integers such as `-1`, is truthy in Python. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `None` always evaluates to `False` in a Boolean context. Why the correct answer wins: Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy.
- **B:** Correct. Every non-zero integer, including negative integers such as `-1`, is truthy in Python. In this case: Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy.
- **C:** Incorrect for this question. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy.
- **D:** Incorrect for this question. Numeric zero `0.0` evaluates to `False` in a Boolean context. Why the correct answer wins: Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy.
- **E:** Correct. `'0'` is a 1-character string (`len('0') == 1`), so it is truthy (`bool('0') is True`). In this case: Non-empty string `'0'` (`len == 1`) and non-zero negative integer `-1` are both truthy, whereas `{}`, `0.0`, and `None` are falsy.

### Question 17 — D

Answer: `IDLE`. Floating-point zero `0.0` is falsy in Python, so execution enters the `else` suite and prints `IDLE`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `WARN`. Why the correct answer wins: Floating-point zero `0.0` is falsy in Python, so execution enters the `else` suite and prints `IDLE`.
- **B:** Incorrect for this question. Prints `OK`. Why the correct answer wins: Floating-point zero `0.0` is falsy in Python, so execution enters the `else` suite and prints `IDLE`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Floating-point zero `0.0` is falsy in Python, so execution enters the `else` suite and prints `IDLE`.
- **D:** Correct. In this case: Floating-point zero `0.0` is falsy in Python, so execution enters the `else` suite and prints `IDLE`.

### Question 18 — A, E

Answers: `120 <= bpm < 160`; `bpm >= 120 and bpm < 160`. `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`. Chained comparison `120 <= bpm < 160` is `True` when `bpm` is at least `120` and strictly below `160`. Joining both bounds with `and` checks `[120, 160)` accurately. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Chained comparison `120 <= bpm < 160` is `True` when `bpm` is at least `120` and strictly below `160`. In this case: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`.
- **B:** Incorrect for this question. Using `or` returns `True` for every number. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`.
- **C:** Incorrect for this question. Using `<= 160` includes `160`, violating a strict upper bound `< 160`. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`.
- **D:** Incorrect for this question. Bitwise `&` binds tighter than comparisons, evaluating `120 & bpm` first. Why the correct answer wins: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`.
- **E:** Correct. Joining both bounds with `and` checks `[120, 160)` accurately. In this case: `120 <= bpm < 160` and `bpm >= 120 and bpm < 160` both enforce `[120, 160)`, whereas `or` is always `True`, `&` binds tighter than `<`, and `<= 160` includes `160`.

### Question 19 — C

Answer: `and`. `and` evaluates its right operand only when `count > 0` is truthy, preventing `ZeroDivisionError` when `count == 0`. `and` is Python's short-circuit logical conjunction operator. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `not` is Python's unary logical negation operator and returns `True` or `False`. Why the correct answer wins: `and` evaluates its right operand only when `count > 0` is truthy, preventing `ZeroDivisionError` when `count == 0`.
- **B:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `and` evaluates its right operand only when `count > 0` is truthy, preventing `ZeroDivisionError` when `count == 0`.
- **C:** Correct. `and` is Python's short-circuit logical conjunction operator. In this case: `and` evaluates its right operand only when `count > 0` is truthy, preventing `ZeroDivisionError` when `count == 0`.
- **D:** Incorrect for this question. `or` is Python's short-circuit logical disjunction operator. Why the correct answer wins: `and` evaluates its right operand only when `count > 0` is truthy, preventing `ZeroDivisionError` when `count == 0`.

### Question 20 — C

Answer: `while`. `while` checks `snow_cm >= 3` prior to each iteration until `snow_cm` drops to `0`. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` checks `snow_cm >= 3` prior to each iteration until `snow_cm` drops to `0`.
- **B:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` checks `snow_cm >= 3` prior to each iteration until `snow_cm` drops to `0`.
- **C:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` checks `snow_cm >= 3` prior to each iteration until `snow_cm` drops to `0`.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `while` checks `snow_cm >= 3` prior to each iteration until `snow_cm` drops to `0`.

### Question 21 — C

Answer: `3`. `rh` steps `80 -> 70 -> 60 -> 50` across `3` iterations, at which point `50 > 50` is `False` and `hours` prints `3`. Evaluates to the integer `3`. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `rh` steps `80 -> 70 -> 60 -> 50` across `3` iterations, at which point `50 > 50` is `False` and `hours` prints `3`.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `rh` steps `80 -> 70 -> 60 -> 50` across `3` iterations, at which point `50 > 50` is `False` and `hours` prints `3`.
- **C:** Correct. Evaluates to the integer `3`. In this case: `rh` steps `80 -> 70 -> 60 -> 50` across `3` iterations, at which point `50 > 50` is `False` and `hours` prints `3`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: `rh` steps `80 -> 70 -> 60 -> 50` across `3` iterations, at which point `50 > 50` is `False` and `hours` prints `3`.

### Question 22 — B, C

Answers: `range(2, 10, 2)`; `range(10, 2, -2)`. `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). `range(10, 2, -2)` generates `10, 8, 6, 4` (four integers). Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `range(3, 9, 3)` stops before `9`, yielding only `3, 6` (two integers). Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five.
- **B:** Correct. `range(10, 2, -2)` generates `10, 8, 6, 4` (four integers). In this case: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five.
- **C:** Correct. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). In this case: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five.
- **D:** Incorrect for this question. `range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers). Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five.
- **E:** Incorrect for this question. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`, whereas `range(8, 2)` yields zero, `range(3, 9, 3)` yields two, and `range(0, 10, 2)` yields five.

### Question 23 — A

Answer: `12`. `range(7, 0, -3)` starts at `7`, steps by `-3`, and stops above exclusive `0`, yielding `7, 4, 1` whose sum is `12`. Evaluates to the integer `12`. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `12`. In this case: `range(7, 0, -3)` starts at `7`, steps by `-3`, and stops above exclusive `0`, yielding `7, 4, 1` whose sum is `12`.
- **B:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: `range(7, 0, -3)` starts at `7`, steps by `-3`, and stops above exclusive `0`, yielding `7, 4, 1` whose sum is `12`.
- **C:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: `range(7, 0, -3)` starts at `7`, steps by `-3`, and stops above exclusive `0`, yielding `7, 4, 1` whose sum is `12`.
- **D:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: `range(7, 0, -3)` starts at `7`, steps by `-3`, and stops above exclusive `0`, yielding `7, 4, 1` whose sum is `12`.

### Question 24 — A

Answer: `15`. Iterating directly over tuple `(4, 0, 11)` visits `4`, `0`, and `11` in order, summing to `15`. Evaluates to the integer `15`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `15`. In this case: Iterating directly over tuple `(4, 0, 11)` visits `4`, `0`, and `11` in order, summing to `15`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Iterating directly over tuple `(4, 0, 11)` visits `4`, `0`, and `11` in order, summing to `15`.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Iterating directly over tuple `(4, 0, 11)` visits `4`, `0`, and `11` in order, summing to `15`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Iterating directly over tuple `(4, 0, 11)` visits `4`, `0`, and `11` in order, summing to `15`.

### Question 25 — A

Answer: `continue`. `continue` skips `valid_sum += probe` for `-999` and moves to the next sensor reading. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. In this case: `continue` skips `valid_sum += probe` for `-999` and moves to the next sensor reading.
- **B:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `continue` skips `valid_sum += probe` for `-999` and moves to the next sensor reading.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `continue` skips `valid_sum += probe` for `-999` and moves to the next sensor reading.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `continue` skips `valid_sum += probe` for `-999` and moves to the next sensor reading.

### Question 26 — D

Answer: `pass`. `pass` is Python's no-op statement; unlike `continue`, lines below `if deg == 0:` inside the loop still execute. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `pass` is Python's no-op statement; unlike `continue`, lines below `if deg == 0:` inside the loop still execute.
- **B:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `pass` is Python's no-op statement; unlike `continue`, lines below `if deg == 0:` inside the loop still execute.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `pass` is Python's no-op statement; unlike `continue`, lines below `if deg == 0:` inside the loop still execute.
- **D:** Correct. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. In this case: `pass` is Python's no-op statement; unlike `continue`, lines below `if deg == 0:` inside the loop still execute.

### Question 27 — D

Answer: `HALT`. When `gust` reaches `52`, the suite prints `HALT` and executes `break`, which exits the loop and skips the `else:` suite completely. Prints `HALT` before `break` skips the loop `else` suite. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: When `gust` reaches `52`, the suite prints `HALT` and executes `break`, which exits the loop and skips the `else:` suite completely.
- **B:** Incorrect for this question. Prints `CLEAN` from the loop `else` suite. Why the correct answer wins: When `gust` reaches `52`, the suite prints `HALT` and executes `break`, which exits the loop and skips the `else:` suite completely.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: When `gust` reaches `52`, the suite prints `HALT` and executes `break`, which exits the loop and skips the `else:` suite completely.
- **D:** Correct. Prints `HALT` before `break` skips the loop `else` suite. In this case: When `gust` reaches `52`, the suite prints `HALT` and executes `break`, which exits the loop and skips the `else:` suite completely.

### Question 28 — D

Answer: `3`. For `baseline = 10`, `15` and `25` exceed it (`2`); for `baseline = 20`, `25` exceeds it (`1`), giving `2 + 1 == 3`. Evaluates to the integer `3`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: For `baseline = 10`, `15` and `25` exceed it (`2`); for `baseline = 20`, `25` exceeds it (`1`), giving `2 + 1 == 3`.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: For `baseline = 10`, `15` and `25` exceed it (`2`); for `baseline = 20`, `25` exceeds it (`1`), giving `2 + 1 == 3`.
- **C:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: For `baseline = 10`, `15` and `25` exceed it (`2`); for `baseline = 20`, `25` exceeds it (`1`), giving `2 + 1 == 3`.
- **D:** Correct. Evaluates to the integer `3`. In this case: For `baseline = 10`, `15` and `25` exceed it (`2`); for `baseline = 20`, `25` exceeds it (`1`), giving `2 + 1 == 3`.

### Question 29 — A

Answer: `[15, 35]`. Starting at index `1` (`15`) with stride `2` selects indices `1` and `3`, returning `[15, 35]`. Slice `[1::2]` picks indices `1` and `3`: `[15, 35]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slice `[1::2]` picks indices `1` and `3`: `[15, 35]`. In this case: Starting at index `1` (`15`) with stride `2` selects indices `1` and `3`, returning `[15, 35]`.
- **B:** Incorrect for this question. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. Why the correct answer wins: Starting at index `1` (`15`) with stride `2` selects indices `1` and `3`, returning `[15, 35]`.
- **C:** Incorrect for this question. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Why the correct answer wins: Starting at index `1` (`15`) with stride `2` selects indices `1` and `3`, returning `[15, 35]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Starting at index `1` (`15`) with stride `2` selects indices `1` and `3`, returning `[15, 35]`.

### Question 30 — A

Answer: `45`. Negative index `-1` addresses the final element of a non-empty sequence, returning `45`. Evaluates to the integer `45`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `45`. In this case: Negative index `-1` addresses the final element of a non-empty sequence, returning `45`.
- **B:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Negative index `-1` addresses the final element of a non-empty sequence, returning `45`.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Negative index `-1` addresses the final element of a non-empty sequence, returning `45`.
- **D:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: Negative index `-1` addresses the final element of a non-empty sequence, returning `45`.

### Question 31 — C

Answer: `[1, 2, [3, 4]]`. `.append([3, 4])` inserts its argument as a single nested third element, producing `[1, 2, [3, 4]]`. `.append([3, 4])` adds the entire list object as a single nested third element. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `.append([3, 4])` inserts its argument as a single nested third element, producing `[1, 2, [3, 4]]`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: `.append([3, 4])` inserts its argument as a single nested third element, producing `[1, 2, [3, 4]]`.
- **C:** Correct. `.append([3, 4])` adds the entire list object as a single nested third element. In this case: `.append([3, 4])` inserts its argument as a single nested third element, producing `[1, 2, [3, 4]]`.
- **D:** Incorrect for this question. `.extend([3, 4])` iterates its argument and appends each element individually. Why the correct answer wins: `.append([3, 4])` inserts its argument as a single nested third element, producing `[1, 2, [3, 4]]`.

### Question 32 — B, D

Answers: `items.append(x)`; `items.sort()`. Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists. `.append(x)` mutates `items` in place by adding `x` at the end and returns `None`. `items.sort()` sorts the list in place and returns `None` rather than a new list. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **B:** Correct. `items.sort()` sorts the list in place and returns `None` rather than a new list. In this case: Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **C:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **D:** Correct. `.append(x)` mutates `items` in place by adding `x` at the end and returns `None`. In this case: Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **E:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: Both `items.append(x)` and `items.sort()` modify `items` in place and evaluate to `None`, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.

### Question 33 — D

Answer: `del`. `del hourly[1:4]` removes the slice `[20, 30, 40]` directly from `hourly`, leaving `[10, 50]`. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `del hourly[1:4]` removes the slice `[20, 30, 40]` directly from `hourly`, leaving `[10, 50]`.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `del hourly[1:4]` removes the slice `[20, 30, 40]` directly from `hourly`, leaving `[10, 50]`.
- **C:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `del hourly[1:4]` removes the slice `[20, 30, 40]` directly from `hourly`, leaving `[10, 50]`.
- **D:** Correct. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. In this case: `del hourly[1:4]` removes the slice `[20, 30, 40]` directly from `hourly`, leaving `[10, 50]`.

### Question 34 — D, E

Answers: `items.copy()`; `items[:]`. `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. `items[:]` creates a shallow copy as a new outer list object. Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Why the correct answer wins: `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object.
- **B:** Incorrect for this question. `.append(x)` mutates `items` in place by adding `x` at the end and returns `None`. Why the correct answer wins: `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object.
- **C:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object.
- **D:** Correct. `items[:]` creates a shallow copy as a new outer list object. In this case: `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object.
- **E:** Correct. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. In this case: `items.copy()` and `items[:]` each construct a separate outer list, whereas `backup = items` binds an alias to the same list object.

### Question 35 — B

Answer: `3`. The comprehension filter `t < 0` retains `-4`, `-1`, and `-7` (excluding `0` and `2`), giving length `3`. Evaluates to the integer `3`. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: The comprehension filter `t < 0` retains `-4`, `-1`, and `-7` (excluding `0` and `2`), giving length `3`.
- **B:** Correct. Evaluates to the integer `3`. In this case: The comprehension filter `t < 0` retains `-4`, `-1`, and `-7` (excluding `0` and `2`), giving length `3`.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: The comprehension filter `t < 0` retains `-4`, `-1`, and `-7` (excluding `0` and `2`), giving length `3`.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: The comprehension filter `t < 0` retains `-4`, `-1`, and `-7` (excluding `0` and `2`), giving length `3`.

### Question 36 — C

Answer: `True`. `'KORD'` is a key in `stations`, and `in` on a dictionary tests key membership, printing `True`. Evaluates to Boolean `True`. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: `'KORD'` is a key in `stations`, and `in` on a dictionary tests key membership, printing `True`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: `'KORD'` is a key in `stations`, and `in` on a dictionary tests key membership, printing `True`.
- **C:** Correct. Evaluates to Boolean `True`. In this case: `'KORD'` is a key in `stations`, and `in` on a dictionary tests key membership, printing `True`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `'KORD'` is a key in `stations`, and `in` on a dictionary tests key membership, printing `True`.

### Question 37 — C

Answer: `30`. Tuple unpacking binds `lat = 10` and `lon = 20`, so `lat + lon` prints `30`. Evaluates to the integer `30`. Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: Tuple unpacking binds `lat = 10` and `lon = 20`, so `lat + lon` prints `30`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Tuple unpacking binds `lat = 10` and `lon = 20`, so `lat + lon` prints `30`.
- **C:** Correct. Evaluates to the integer `30`. In this case: Tuple unpacking binds `lat = 10` and `lon = 20`, so `lat + lon` prints `30`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Tuple unpacking binds `lat = 10` and `lon = 20`, so `lat + lon` prints `30`.

### Question 38 — C, D

Answers: A tuple of immutable values (`(10, 20)`) can be used as a `dict` key, whereas a `list` (`[10, 20]`) raises `TypeError`; A tuple containing a `list` (`(10, [20])`) cannot be used as a `dict` key and raises `TypeError`. A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`. Tuples containing only hashable objects are hashable, whereas lists are mutable and unhashable. A tuple is hashable only when every element inside it is also hashable. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`.
- **B:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`.
- **C:** Correct. Tuples containing only hashable objects are hashable, whereas lists are mutable and unhashable. In this case: A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`.
- **D:** Correct. A tuple is hashable only when every element inside it is also hashable. In this case: A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`.
- **E:** Incorrect for this question. In Python, `{ ... }` builds dictionaries or sets rather than delimiting statement suites. Why the correct answer wins: A tuple of immutable numbers `(10, 20)` is hashable and works as a `dict` key, whereas a tuple containing a mutable list `(10, [20])` is unhashable and raises `TypeError`.

### Question 39 — B

Answer: `get`. `stations.get('KDEN', 1655)` returns `1655` if `'KDEN'` is missing without raising `KeyError`. `d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `d.values()` returns a view of the dictionary's values. Why the correct answer wins: `stations.get('KDEN', 1655)` returns `1655` if `'KDEN'` is missing without raising `KeyError`.
- **B:** Correct. `d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing. In this case: `stations.get('KDEN', 1655)` returns `1655` if `'KDEN'` is missing without raising `KeyError`.
- **C:** Incorrect for this question. `d.items()` returns a view of `(key, value)` pairs. Why the correct answer wins: `stations.get('KDEN', 1655)` returns `1655` if `'KDEN'` is missing without raising `KeyError`.
- **D:** Incorrect for this question. `d.keys()` returns a view of the dictionary's keys. Why the correct answer wins: `stations.get('KDEN', 1655)` returns `1655` if `'KDEN'` is missing without raising `KeyError`.

### Question 40 — B

Answer: `27`. `totals.items()` yields `('north', 12)` and `('south', 15)`, so adding each `v` prints `27`. Evaluates to the integer `27`. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `totals.items()` yields `('north', 12)` and `('south', 15)`, so adding each `v` prints `27`.
- **B:** Correct. Evaluates to the integer `27`. In this case: `totals.items()` yields `('north', 12)` and `('south', 15)`, so adding each `v` prints `27`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `totals.items()` yields `('north', 12)` and `('south', 15)`, so adding each `v` prints `27`.
- **D:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: `totals.items()` yields `('north', 12)` and `('south', 15)`, so adding each `v` prints `27`.

### Question 41 — A, D

Answers: `'Chef\'s kiss'`; `"Chef's kiss"`. `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes. Backslash-escaping `\'` inside single quotes produces a valid string literal containing an apostrophe. Wrapping a string containing `'` inside double quotes `"..."` needs no backslash escape. Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Wrapping a string containing `'` inside double quotes `"..."` needs no backslash escape. In this case: `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes.
- **B:** Incorrect for this question. An unescaped single quote inside single quotes closes the string early and raises `SyntaxError`. Why the correct answer wins: `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes.
- **C:** Incorrect for this question. Python has no `/* ... */` comment syntax and raises `SyntaxError` if those tokens appear as code. Why the correct answer wins: `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes.
- **D:** Correct. Backslash-escaping `\'` inside single quotes produces a valid string literal containing an apostrophe. In this case: `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes.
- **E:** Incorrect for this question. A single trailing backslash escapes the closing quote and raises `SyntaxError`. Why the correct answer wins: `'Chef\'s kiss'` escapes the inner single quote and `"Chef's kiss"` wraps the apostrophe inside double quotes.

### Question 42 — A

Answer: `split`. `str.split(',')` splits the string wherever `','` occurs and returns the resulting substrings in a `list`. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. In this case: `str.split(',')` splits the string wherever `','` occurs and returns the resulting substrings in a `list`.
- **B:** Incorrect for this question. `s.strip()` returns a new string with leading and trailing whitespace removed. Why the correct answer wins: `str.split(',')` splits the string wherever `','` occurs and returns the resulting substrings in a `list`.
- **C:** Incorrect for this question. `s.replace(old, new)` returns a new string where occurrences of `old` are replaced with `new`. Why the correct answer wins: `str.split(',')` splits the string wherever `','` occurs and returns the resulting substrings in a `list`.
- **D:** Incorrect for this question. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Why the correct answer wins: `str.split(',')` splits the string wherever `','` occurs and returns the resulting substrings in a `list`.

### Question 43 — D

Answer: `'Pto'`. Stepping from index `0` to the end by `2` picks indices `0` (`'P'`), `2` (`'t'`), and `4` (`'o'`), returning `'Pto'`. `'Python'[::2]` picks characters at indices `0`, `2`, and `4`, returning `'Pto'`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `'Python'[::-1]` steps backward from the end and returns `'nohtyP'`. Why the correct answer wins: Stepping from index `0` to the end by `2` picks indices `0` (`'P'`), `2` (`'t'`), and `4` (`'o'`), returning `'Pto'`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Stepping from index `0` to the end by `2` picks indices `0` (`'P'`), `2` (`'t'`), and `4` (`'o'`), returning `'Pto'`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Stepping from index `0` to the end by `2` picks indices `0` (`'P'`), `2` (`'t'`), and `4` (`'o'`), returning `'Pto'`.
- **D:** Correct. `'Python'[::2]` picks characters at indices `0`, `2`, and `4`, returning `'Pto'`. In this case: Stepping from index `0` to the end by `2` picks indices `0` (`'P'`), `2` (`'t'`), and `4` (`'o'`), returning `'Pto'`.

### Question 44 — C

Answer: `def`. `def` begins a named function definition in Python 3. `def` introduces a named function definition in Python; `function` and `func` are not Python keywords. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. Why the correct answer wins: `def` begins a named function definition in Python 3.
- **B:** Incorrect for this question. `function` is a JavaScript keyword, not a Python keyword; Python uses `def`. Why the correct answer wins: `def` begins a named function definition in Python 3.
- **C:** Correct. `def` introduces a named function definition in Python; `function` and `func` are not Python keywords. In this case: `def` begins a named function definition in Python 3.
- **D:** Incorrect for this question. `var` is not a Python keyword; Python binds variables directly on assignment. Why the correct answer wins: `def` begins a named function definition in Python 3.

### Question 45 — C, E

Answers: `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`; The first executed `return` exits the function immediately and skips all remaining statements in its body. Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. Code after an executed `return` inside the same branch does not run (except an enclosing `finally:` block). Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`.
- **B:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`.
- **C:** Correct. Code after an executed `return` inside the same branch does not run (except an enclosing `finally:` block). In this case: Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`.
- **D:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`.
- **E:** Correct. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. In this case: Executing `return` immediately exits the function, and omitting an expression (or reaching the end of the suite) returns `None`.

### Question 46 — D

Answer: `next`. `next(stream)` advances the generator iterator to its first `yield` and returns that value. Built-in `next(gen)` advances a generator to its next `yield` expression and returns the yielded value. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ord(ch)` returns the integer Unicode code point of a 1-character string (for example `ord('A') == 65`). Why the correct answer wins: `next(stream)` advances the generator iterator to its first `yield` and returns that value.
- **B:** Incorrect for this question. Built-in `len(s)` returns the element count of collection `s`. Why the correct answer wins: `next(stream)` advances the generator iterator to its first `yield` and returns that value.
- **C:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: `next(stream)` advances the generator iterator to its first `yield` and returns that value.
- **D:** Correct. Built-in `next(gen)` advances a generator to its next `yield` expression and returns the yielded value. In this case: `next(stream)` advances the generator iterator to its first `yield` and returns that value.

### Question 47 — B, D

Answers: Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet; `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call. Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call.
- **B:** Correct. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. In this case: Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call.
- **C:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call.
- **D:** Correct. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. In this case: Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call.
- **E:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Calling the function returns a generator iterator without running the body yet, and each `yield` pauses local execution state until the next `next()` call.

### Question 48 — A

Answer: `7`. `dsum(205)` computes `5 + dsum(20)` -> `5 + 0 + dsum(2)` -> `5 + 0 + 2 == 7`. Evaluates to the integer `7`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `7`. In this case: `dsum(205)` computes `5 + dsum(20)` -> `5 + 0 + dsum(2)` -> `5 + 0 + 2 == 7`.
- **B:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `dsum(205)` computes `5 + dsum(20)` -> `5 + 0 + dsum(2)` -> `5 + 0 + 2 == 7`.
- **C:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `dsum(205)` computes `5 + dsum(20)` -> `5 + 0 + dsum(2)` -> `5 + 0 + 2 == 7`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `dsum(205)` computes `5 + dsum(20)` -> `5 + 0 + dsum(2)` -> `5 + 0 + 2 == 7`.

### Question 49 — B

Answer: `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit. Because no base case stops the recursive calls, Python hits the recursion limit and raises `RecursionError`. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Because no base case stops the recursive calls, Python hits the recursion limit and raises `RecursionError`.
- **B:** Correct. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). In this case: Because no base case stops the recursive calls, Python hits the recursion limit and raises `RecursionError`.
- **C:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Because no base case stops the recursive calls, Python hits the recursion limit and raises `RecursionError`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Because no base case stops the recursive calls, Python hits the recursion limit and raises `RecursionError`.

### Question 50 — B

Answer: `4.5`. `offset` defaults to `0.5` and `scale` defaults to `1.0`, so `(4.0 + 0.5) * 1.0` returns `4.5`. Evaluates to the floating-point value `4.5`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `offset` defaults to `0.5` and `scale` defaults to `1.0`, so `(4.0 + 0.5) * 1.0` returns `4.5`.
- **B:** Correct. Evaluates to the floating-point value `4.5`. In this case: `offset` defaults to `0.5` and `scale` defaults to `1.0`, so `(4.0 + 0.5) * 1.0` returns `4.5`.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `offset` defaults to `0.5` and `scale` defaults to `1.0`, so `(4.0 + 0.5) * 1.0` returns `4.5`.
- **D:** Incorrect for this question. Evaluates to the floating-point value `3.5`. Why the correct answer wins: `offset` defaults to `0.5` and `scale` defaults to `1.0`, so `(4.0 + 0.5) * 1.0` returns `4.5`.

### Question 51 — C

Answer: `SyntaxError` because a positional argument cannot follow a keyword argument at a call site. Python's call grammar rejects positional arguments after keyword arguments with `SyntaxError`. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. Why the correct answer wins: Python's call grammar rejects positional arguments after keyword arguments with `SyntaxError`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Python's call grammar rejects positional arguments after keyword arguments with `SyntaxError`.
- **C:** Correct. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. In this case: Python's call grammar rejects positional arguments after keyword arguments with `SyntaxError`.
- **D:** Incorrect for this question. Evaluates to the floating-point value `4.5`. Why the correct answer wins: Python's call grammar rejects positional arguments after keyword arguments with `SyntaxError`.

### Question 52 — A, D

Answers: Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument; Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body. Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. In this case: Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call.
- **B:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call.
- **C:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call.
- **D:** Correct. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. In this case: Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call.
- **E:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: Default `history=[]` is created once at `def` time and shared across default calls; using `history=None` and `if history is None: history = []` allocates a new list each call.

### Question 53 — B

Answer: `SyntaxError` because a parameter without a default value cannot follow a parameter with a default value. Non-default parameter `reading` follows defaulted parameter `unit='C'`, raising `SyntaxError`. In a `def` signature (`def f(a=1, b):`), required positional-or-keyword parameters must precede parameters with default values. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Non-default parameter `reading` follows defaulted parameter `unit='C'`, raising `SyntaxError`.
- **B:** Correct. In a `def` signature (`def f(a=1, b):`), required positional-or-keyword parameters must precede parameters with default values. In this case: Non-default parameter `reading` follows defaulted parameter `unit='C'`, raising `SyntaxError`.
- **C:** Incorrect for this question. Placing required parameter `amount` before defaulted parameters `rate=1.1` and `fee=0` is valid Python signature order. Why the correct answer wins: Non-default parameter `reading` follows defaulted parameter `unit='C'`, raising `SyntaxError`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Non-default parameter `reading` follows defaulted parameter `unit='C'`, raising `SyntaxError`.

### Question 54 — A

Answer: `global`. `global alert_count` binds `alert_count` inside `mark_alert` to the module-level variable. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. In this case: `global alert_count` binds `alert_count` inside `mark_alert` to the module-level variable.
- **B:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `global alert_count` binds `alert_count` inside `mark_alert` to the module-level variable.
- **C:** Incorrect for this question. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. Why the correct answer wins: `global alert_count` binds `alert_count` inside `mark_alert` to the module-level variable.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `global alert_count` binds `alert_count` inside `mark_alert` to the module-level variable.

### Question 55 — C

Answer: `25`. `apply` only reads `offset`, so LEGB resolves `offset` in module scope (`5`) without needing `global`, printing `25`. Evaluates to the integer `25`. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `apply` only reads `offset`, so LEGB resolves `offset` in module scope (`5`) without needing `global`, printing `25`.
- **B:** Incorrect for this question. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. Why the correct answer wins: `apply` only reads `offset`, so LEGB resolves `offset` in module scope (`5`) without needing `global`, printing `25`.
- **C:** Correct. Evaluates to the integer `25`. In this case: `apply` only reads `offset`, so LEGB resolves `offset` in module scope (`5`) without needing `global`, printing `25`.
- **D:** Incorrect for this question. `NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope. Why the correct answer wins: `apply` only reads `offset`, so LEGB resolves `offset` in module scope (`5`) without needing `global`, printing `25`.

### Question 56 — B, D

Answers: `SystemExit`; `KeyboardInterrupt`. `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C. `SystemExit` inherits directly from `BaseException` (NOT `Exception`) so `except Exception:` does not accidentally swallow `sys.exit()`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C.
- **B:** Correct. `SystemExit` inherits directly from `BaseException` (NOT `Exception`) so `except Exception:` does not accidentally swallow `sys.exit()`. In this case: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C.
- **D:** Correct. In this case: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C.
- **E:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` does not intercept process termination or Ctrl-C.

### Question 57 — D

Answer: `RecursionError`. `RecursionError` inherits from `RuntimeError` under `Exception`. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `RecursionError` inherits from `RuntimeError` under `Exception`.
- **B:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: `RecursionError` inherits from `RuntimeError` under `Exception`.
- **C:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `RecursionError` inherits from `RuntimeError` under `Exception`.
- **D:** Correct. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. In this case: `RecursionError` inherits from `RuntimeError` under `Exception`.

### Question 58 — B

Answer: `ZeroDivisionError`. Dividing an `int` or `float` by `0` or `0.0` raises `ZeroDivisionError`. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Dividing an `int` or `float` by `0` or `0.0` raises `ZeroDivisionError`.
- **B:** Correct. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. In this case: Dividing an `int` or `float` by `0` or `0.0` raises `ZeroDivisionError`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Dividing an `int` or `float` by `0` or `0.0` raises `ZeroDivisionError`.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Dividing an `int` or `float` by `0` or `0.0` raises `ZeroDivisionError`.

### Question 59 — A

Answer: `NameError`. Referencing an identifier that is unbound in local, enclosing, global, and built-in scopes raises `NameError`. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. In this case: Referencing an identifier that is unbound in local, enclosing, global, and built-in scopes raises `NameError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Referencing an identifier that is unbound in local, enclosing, global, and built-in scopes raises `NameError`.
- **C:** Incorrect for this question. `AttributeError` is raised when accessing a method or attribute name that does not exist on that object's type. Why the correct answer wins: Referencing an identifier that is unbound in local, enclosing, global, and built-in scopes raises `NameError`.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Referencing an identifier that is unbound in local, enclosing, global, and built-in scopes raises `NameError`.

### Question 60 — D

Answer: `except (KeyError, IndexError):`. In Python 3, catching multiple exception classes in one clause requires a parenthesized tuple: `except (KeyError, IndexError):`. To catch multiple exception classes in one handler, pass a parenthesized tuple of exception types after `except`. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Placing non-default `amount` after default `rate=1.1` raises `SyntaxError`. Why the correct answer wins: In Python 3, catching multiple exception classes in one clause requires a parenthesized tuple: `except (KeyError, IndexError):`.
- **B:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: In Python 3, catching multiple exception classes in one clause requires a parenthesized tuple: `except (KeyError, IndexError):`.
- **C:** Incorrect for this question. Unparenthesized `except A, B:` was Python 2 syntax and raises `SyntaxError` in Python 3. Why the correct answer wins: In Python 3, catching multiple exception classes in one clause requires a parenthesized tuple: `except (KeyError, IndexError):`.
- **D:** Correct. To catch multiple exception classes in one handler, pass a parenthesized tuple of exception types after `except`. In this case: In Python 3, catching multiple exception classes in one clause requires a parenthesized tuple: `except (KeyError, IndexError):`.
