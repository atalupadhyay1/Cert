# PCEP – Certified Entry-Level Python Programmer (PCEP-30-02) — Full-Length Mock Exam 6

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 15 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). The live PCEP-30-02 exam has 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item set is an expanded 2x bank timed at 80 minutes to preserve the live pace of about 80 seconds per item. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. Version note: PCEP-30-03 is scheduled for release on October 31, 2026; PCEP-30-02 remains active and earned credentials retain their five-year validity. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. An ops engineer compares running a Python `cron_helper.py` script under CPython against shipping a compiled C binary. Which two statements accurately describe those execution models? Select two.

- A. Compiled native binaries require every end user to keep the original C compiler installed to launch the binary
- B. Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it
- C. A static linker merges Python modules into firmware without needing a runtime interpreter
- D. CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime
- E. Ahead-of-time compilation translates the entire program into native machine instructions once before execution

### 2. A schedule loader has `if hour == 12` with the trailing colon `:` forgotten, and Python refuses to run the file. Which language rule set did the missing colon violate?

- A. Syntax defines the grammar rules for combining tokens into legal statements
- B. Semantics determines whether a syntactically valid statement makes sense and what it computes
- C. Style formatting comments automatically bypass syntax checking during parsing
- D. Lexis defines the set of valid tokens and words recognized by the language

### 3. A developer is naming configuration fields in a task scheduler. Which two names are reserved Python keywords that cannot be used as variable identifiers? Select two.

- A. `pass`
- B. `_temp_value`
- C. `none`
- D. `continue`
- E. `list`

### 4. A cron bitmask config defines integer constants in Python 3. Which two numeric literals are syntactically valid? Select two.

- A. `0x1G`
- B. `0o18`
- C. `0b1011`
- D. `1_000_000`
- E. `017`

### 5. How does Python treat `# reload every 15 minutes` when it appears after code on a configuration line outside string quotes?

- A. Style formatting comments automatically bypass syntax checking during parsing
- B. Text after `#` outside string literals is ignored until the end of the physical line
- C. Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it
- D. Every statement in the same suite must share the exact same indentation width

### 6. A retry decay formula evaluates `factor = 2 ** -3` in Python 3. What exact value is assigned to `factor`?

- A. `0.125`
- B. `-6`
- C. Raises `ValueError`
- D. `-8`

### 7. A slot-duration expression evaluates `chunk = 24 / 4 / 2` in Python 3. What exact value is bound to `chunk`?

- A. `12`
- B. `3`
- C. `3.0`
- D. `12.5`

### 8. Complete `active = mask ____ 1` so `active` isolates strictly the lowest bit (`0` or `1`) of integer `mask`. Which bitwise operator fills the blank?

- A. `<<`
- B. `^`
- C. `&`
- D. `and`

### 9. An offset calculation evaluates `shift = -5.0 // 2` in Python 3. What exact value is bound to `shift`?

- A. `-3`
- B. `-3.0`
- C. `-2.0`
- D. `-2`

### 10. A calendar script executes `print(2026, 10, 29, sep='/')`. What text is written to standard output?

- A. Raises `TypeError`
- B. `red;green;blue`
- C. `a b`
- D. `2026/10/29`

### 11. An interactive prompt reads `'12'` from `a = input()` and `'3'` from `b = input()`, then runs `print(a + b)`. What is printed?

- A. Raises `ValueError`
- B. Raises `TypeError`
- C. `123`
- D. `15`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass

### 12. A shift router sets `hr = 9` and evaluates `slot = 'A' if hr < 6 else ('B' if hr < 12 else 'C')`. Which string does `slot` receive?

- A. `B`
- B. `D`
- C. `C`
- D. `A`

### 13. Complete `if env_name ____ 'prod':` so maintenance jobs run in every environment *except* `'prod'`. Which relational operator fills the blank?

- A. `!=`
- B. `is`
- C. `==`
- D. `=`

### 14. When a config loader tests `if overrides:`, which two values of `overrides` cause the condition to evaluate to `False`? Select two.

- A. `[0]`
- B. `None`
- C. `{}`
- D. `(7,)`
- E. `'False'`

### 15. A config flag holds string `enabled = 'False'` and runs `if enabled: print('A')` / `else: print('B')`. What does it print?

- A. Raises `TypeError`
- B. `A`
- C. Nothing is printed (zero iterations)
- D. `B`

### 16. A window rule evaluates `open_gate = not False and False`. What Boolean value does `open_gate` receive?

- A. Raises `SyntaxError`
- B. `0`
- C. `True`
- D. `False`

### 17. A nightly job runs only when neither `paused` (`a`) nor `holiday` (`b`) is truthy. Which two expressions implement that condition accurately? Select two.

- A. `(not a) or (not b)`
- B. `not a or b`
- C. `not (a or b)`
- D. `(not a) and (not b)`
- E. `(x >= 10) or (x <= 20)`

### 18. A backoff timer sets `wait = 1; steps = 0` and runs `while wait < 16: wait *= 2; steps += 1`. What is `steps` when the loop terminates?

- A. `16`
- B. `4`
- C. `5`
- D. `3`

### 19. Complete `delay = 1` / `while delay < 8:` / `    delay ____ 2` so `delay` doubles on each retry (`1 -> 2 -> 4 -> 8`). Which augmented operator fills the blank?

- A. `==`
- B. `+=`
- C. `//=`
- D. `*=`

### 20. A countdown scheduler must fire five consecutive daily reminders. Which two `range()` arguments generate a sequence of length five? Select two.

- A. `range(5, 0, -1)`
- B. `range(1, 6)`
- C. `range(1, 6, 2)`
- D. `range(5, 1)`
- E. `range(1, 3)`

### 21. A quarter-hour tick helper evaluates `sum(range(0, 10, 3))`. What integer does `sum()` return?

- A. `18`
- B. `9`
- C. `28`
- D. `15`

### 22. A weekday counter sets `work = 0` and runs `for d in ('Mon', 'Sat', 'Tue', 'Sun', 'Wed'):` / `    if not d.startswith('S'): work += 1`. What is `work` afterward?

- A. `3`
- B. Raises `TypeError`
- C. `5`
- D. `2`

### 23. A task runner sets `ran = 0` and runs `for job in ['sync', 'SKIP', 'clean', 'STOP', 'backup']:` / `    if job == 'SKIP': continue` / `    if job == 'STOP': break` / `    ran += 1`. What is `ran` afterward?

- A. `1`
- B. `3`
- C. `2`
- D. `4`

### 24. Complete `for line in raw_cfg:` / `    if line.startswith('#'): ____` / `    apply_setting(line)` so comment lines are skipped while later config lines are still applied. Which keyword fills the blank?

- A. `return`
- B. `continue`
- C. `pass`
- D. `break`

### 25. When validating cron entries inside a `for ... else` loop, which two statements inside the loop body prevent the `else:` suite from executing? Select two.

- A. When `return` exits the enclosing function from inside the loop body
- B. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- C. When a `for` loop consumes every item in its iterable without hitting `break`
- D. When `break` terminates the loop early before the condition turns `False`
- E. When a `while` condition initially or eventually evaluates to `False` without `break`

### 26. A conflict check runs `for slot in [9, 11, 14]:` / `    if slot == 12: print('FOUND'); break` / `else: print('DONE')`. What is printed?

- A. Nothing is printed (zero iterations)
- B. `DONE`
- C. `FOUND`
- D. Raises `SyntaxError`

### 27. A half-hour trigger count runs `triggers = 0` / `for h in [8, 12]:` / `    for m in [0, 15, 30, 45]:` / `        if m % 30 == 0: triggers += 1`. What is `triggers` afterward?

- A. `6`
- B. `4`
- C. `2`
- D. `8`

### 28. Complete `for day in week_plan:` / `    ____ task in day:` / `        run(task)` so every task inside each daily list is executed. Which keyword fills the blank?

- A. `in`
- B. `try`
- C. `while`
- D. `for`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations

### 29. A shift schedule stores `hours = [6, 9, 12, 15, 18]`. What does `hours[1:-1]` return?

- A. `[12, 15]`
- B. `[18, 12, 6]`
- C. Raises `IndexError`
- D. `[9, 12, 15]`

### 30. With `hours = [6, 9, 12, 15, 18]`, what does `hours[::-2]` evaluate to?

- A. `[]`
- B. `[9, 12, 15]`
- C. Raises `IndexError`
- D. `[18, 12, 6]`

### 31. Which two descriptions of `list` mutation methods in Python 3 are accurate? Select two.

- A. `sorted(items)` mutates `items` in place and returns `None`
- B. `items.pop()` removes the final element in place and returns that removed element
- C. `items.append(x)` mutates `items` in place and evaluates to `None`
- D. `items.remove(x)` deletes every occurrence of `x` across the entire list in one call
- E. `items.insert(0, x)` appends `x` after the last element of `items`

### 32. Complete `deadlines.____()` so list `deadlines` is reordered in ascending order *in place* without creating a new variable binding. Which `list` method fills the blank?

- A. `index()`
- B. `sort()`
- C. `sorted()`
- D. `pop()`

### 33. Complete `____ tasks[0]` so the first element of list `tasks` is deleted in place using a Python statement keyword rather than a method call. Which keyword fills the blank?

- A. `get()`
- B. `pop()`
- C. `del`
- D. `remove()`

### 34. A nested schedule sets `orig = [[1, 2], [3, 4]]`, makes a shallow slice `dup = orig[:]`, runs `dup[0][1] = 99`, and prints `orig[0][1]`. What is printed?

- A. Raises `IndexError`
- B. `2`
- C. `None`
- D. `99`

### 35. What does `[h for h in [6, 9, 12, 15] if h >= 10]` return?

- A. `[12, 15]`
- B. `2`
- C. `[9, 12, 15]`
- D. Raises `SyntaxError`

### 36. Complete `if key ____ required_keys:` so a config validator flags a missing setting whenever `key` is absent from `required_keys`. Which operator fills the blank?

- A. `not in`
- B. `is`
- C. `==`
- D. `in`

### 37. Which two statements about Python `tuple` objects are accurate? Select two.

- A. `(7)`
- B. Running `del t[0]` removes the first element while keeping the same tuple object
- C. `t = 5,`
- D. Assigning `t[0] = 9` on a tuple raises `TypeError` because tuple slot bindings are immutable
- E. `t = tuple(5)`

### 38. A schedule unpacks a tuple `(h, m) = (1, 15)` and evaluates `h * 10 + m`. What integer is produced?

- A. `25`
- B. `16`
- C. Raises `ValueError`
- D. Raises `TypeError`

### 39. Complete `timeout = cfg.____('timeout', 30)` so reading an optional `'timeout'` setting falls back to `30` instead of raising `KeyError`. Which `dict` method fills the blank?

- A. `keys()`
- B. `get()`
- C. `values()`
- D. `items()`

### 40. When looping over settings dictionary `d = {'host': 'db', 'port': '5432'}`, which two statements hold in Python 3? Select two.

- A. `'host' in cfg.values()`
- B. Iterating `for k, v in d:` unpacks keys and values directly without calling `.items()`
- C. Iterating `for k, v in d.values():` yields `(key, value)` tuples for every entry
- D. Iterating `for k, v in d.items():` unpacks each `(key, value)` pair cleanly
- E. Iterating `for x in d:` yields each dictionary key in insertion order

### 41. A Windows-style string literal writes `s = 'a\\tb'` with a doubled backslash and checks `len(s)`. What integer does `len(s)` return?

- A. `3`
- B. `4`
- C. Raises `SyntaxError`
- D. `5`

### 42. Complete `tokens = ____` on `line = 'host = db01'` so whitespace-separated words are broken into the three-element list `['host', '=', 'db01']`. Which expression fills the blank?

- A. `'-'.join(parts)`
- B. `extend()`
- C. `keys()`
- D. `line.split()`

### 43. When parsing INI-style configuration strings in Python 3, which two properties of `str` always hold? Select two.

- A. An escape sequence such as `\n` or `\\` counts as a single character in `len()`
- B. Running `del s[0]` deletes the first character from `s` in place
- C. Every string transformation method returns a brand-new `str` object and leaves the original string unchanged
- D. Assigning `s[0] = "X"` mutates the first character of `s` in place
- E. `sorted(items)` mutates `items` in place and returns `None`

---

## Block 4 — Functions and Exceptions (28%) — User-defined functions, generators, recursion, argument passing, scope/global, and exception handling

### 44. In a config-helper module, which two function execution paths return `None` to the caller? Select two.

- A. A function that reaches the end of its body without any `return` statement returns `None`
- B. A function executing a bare `return` statement evaluates to `None` at the call site
- C. Function parameter names are automatically registered in module-level global scope when the function returns
- D. Multiple `return` lines in the same branch all execute sequentially and concatenate their results
- E. Calling `t.append(9)` adds an element to the end of tuple `t` in place

### 45. Complete `def parse_port(text):` / `    ____ int(text.strip())` so calling `parse_port(' 8080 ')` hands integer `8080` back to the caller immediately. Which keyword fills the blank?

- A. `continue`
- B. `yield`
- C. `break`
- D. `return`

### 46. Complete `def port_range(base):` / `    ____ base` / `    ____ base + 1` so calling `sum(port_range(10))` lazily consumes two generated ports totaling `21`. Which single keyword fills both blanks?

- A. `yield`
- B. `return`
- C. `pass`
- D. `continue`

### 47. An interval alignment helper defines Euclid's algorithm `def gcd(a, b): return a if b == 0 else gcd(b, a % b)` and evaluates `gcd(18, 12)`. What integer does it return?

- A. `12`
- B. `6`
- C. Raises `RecursionError`
- D. `3`

### 48. Complete the base-case test `def gcd(a, b):` / `    if b ____ 0: return a` / `    return gcd(b, a % b)` so recursion stops as soon as remainder `b` reaches zero. Which operator fills the blank?

- A. `!=`
- B. `=`
- C. `==`
- D. `in`

### 49. Given `def calc(base, rate): return base * rate` in a billing-schedule module, which two calls are valid in Python 3? Select two.

- A. `calc(rate=2, base=10)`
- B. `calc(10, base=5)`
- C. `calc(10, rate=2)`
- D. `calc(10, tax=2)`
- E. `calc(base=10, 2)`

### 50. Given `def retry_cfg(tries, delay): return tries * delay`, what happens at runtime when a caller passes an undeclared keyword `retry_cfg(3, delay=2, jitter=1)`?

- A. `0`
- B. Raises `KeyError`
- C. Raises `TypeError`
- D. `None`

### 51. A helper header `def schedule_job(when='midnight', cmd):` fails with `SyntaxError` when imported. Which `def` parameter rule did it break?

- A. Positional arguments must appear before any keyword arguments in a function call
- B. Duplicate keys overwrite earlier entries, keeping the last value assigned to that key
- C. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- D. Parameters with default values must follow parameters without default values in `def`

### 52. Given `def window_sec(slots=3, length=10): return slots * length`, what does `window_sec()` with zero arguments return?

- A. `10`
- B. Raises `TypeError`
- C. `30`
- D. `20`

### 53. A config module sets `port = 50`, defines `def reload_cfg(): print(port); port = 60`, and calls `reload_cfg()`. Which exception is raised?

- A. `60`
- B. `50`
- C. Raises `UnboundLocalError`
- D. Raises `KeyError`

### 54. Complete `reload_count = 0` / `def mark_reload():` / `    ____ reload_count` / `    reload_count += 1` so `mark_reload()` mutates module-level `reload_count`. Which keyword fills the blank?

- A. `global`
- B. `import`
- C. `nonlocal`
- D. `from`

### 55. In a schedule runner's exception policy, which two statements accurately describe Python's abstract exception classes? Select two.

- A. Calling `t.append(9)` adds an element to the end of tuple `t` in place
- B. `True`, because Python stores decimal fractions exactly to two decimal places
- C. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler
- D. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- E. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`

### 56. Why does `sys.exit(0)` terminate a scheduled Python script cleanly even when the call sits inside `try: ... except Exception:`?

- A. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`
- B. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- C. `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`
- D. `TypeError` inherits directly from `Exception`

### 57. A config reader sets `env = {'HOST': 'localhost'}` and evaluates `env['PORT']` directly. Which exception is raised?

- A. Raises `KeyError`
- B. Raises `IndexError`
- C. Raises `AttributeError`
- D. `None`

### 58. Complete `if interval <= 0:` / `    ____ ValueError('interval must be > 0')` so non-positive intervals immediately signal `ValueError` to callers. Which keyword fills the blank?

- A. `pass`
- B. `finally`
- C. `except`
- D. `raise`

### 59. Which two `except`-clause orderings preserve reachability for both narrow and broad handlers in Python 3? Select two.

- A. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler
- B. Python runs every `except` clause whose class matches the raised exception from top to bottom
- C. Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch
- D. Place a bare `except:` clause above `except TypeError:` as a fallback default
- E. Place `except ZeroDivisionError:` above `except ArithmeticError:` so division by zero reaches the specific handler

### 60. A config lookup runs `d = {}` / `try: v = d['k']` / `except LookupError: print('A')` / `except KeyError: print('B')`. What does it print?

- A. `B`
- B. Raises `KeyError`
- C. `A`
- D. `A B`

---

## Answer key and explanations

### Question 1 — D, E

Answers: CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime; Ahead-of-time compilation translates the entire program into native machine instructions once before execution. CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. A compiler translates the whole program ahead of time into target machine code rather than interpreting source on each run. Local study-map skill 1.1 (Compilation vs Interpretation and Execution Model), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. A compiled standalone executable runs directly on the target OS without shipping the compiler. Why the correct answer wins: CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand.
- **B:** Incorrect for this question. `.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source. Why the correct answer wins: CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand.
- **C:** Incorrect for this question. Standard Python scripts still require a Python runtime rather than a static hardware linker. Why the correct answer wins: CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand.
- **D:** Correct. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. In this case: CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand.
- **E:** Correct. A compiler translates the whole program ahead of time into target machine code rather than interpreting source on each run. In this case: CPython compiles source to bytecode and runs it in a virtual machine at runtime, whereas an ahead-of-time compiler translates the full program into native machine instructions beforehand.

### Question 2 — A

Answer: Syntax defines the grammar rules for combining tokens into legal statements. Syntax governs the grammatical arrangement of valid tokens into statements, including the mandatory `:` introducing a compound block. Syntax checks whether tokens appear in a structurally valid arrangement such as matching parentheses and colons. Local study-map skill 1.2 (Lexis, Syntax, and Semantics Distinctions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Syntax checks whether tokens appear in a structurally valid arrangement such as matching parentheses and colons. In this case: Syntax governs the grammatical arrangement of valid tokens into statements, including the mandatory `:` introducing a compound block.
- **B:** Incorrect for this question. Semantics governs runtime meaning, so dividing a number by zero is syntactically legal yet fails semantically at runtime. Why the correct answer wins: Syntax governs the grammatical arrangement of valid tokens into statements, including the mandatory `:` introducing a compound block.
- **C:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Syntax governs the grammatical arrangement of valid tokens into statements, including the mandatory `:` introducing a compound block.
- **D:** Incorrect for this question. Lexis is the vocabulary layer governing legal identifiers, literals, operators, and keywords. Why the correct answer wins: Syntax governs the grammatical arrangement of valid tokens into statements, including the mandatory `:` introducing a compound block.

### Question 3 — A, D

Answers: `pass`; `continue`. `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Local study-map skill 1.3 (Keywords, Instructions, Indentation, and Comments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. In this case: `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier.
- **B:** Incorrect for this question. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. Why the correct answer wins: `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier.
- **C:** Incorrect for this question. Only capitalized `None` is a keyword; lowercase `none` is not reserved by Python. Why the correct answer wins: `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier.
- **D:** Correct. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. In this case: `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier.
- **E:** Incorrect for this question. `list` names a built-in type rather than a reserved keyword, so Python permits (but discourages) rebinding it. Why the correct answer wins: `pass` and `continue` are reserved keywords in Python 3, whereas `list` is a built-in type name, `none` is lowercase, and `_temp_value` is a legal identifier.

### Question 4 — C, D

Answers: `0b1011`; `1_000_000`. `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`. Prefix `0b` or `0B` denotes a base-2 integer literal (`11` in decimal). Single underscores between digits are legal visual separators in Python numeric literals. Local study-map skill 1.4 (Literals, Numeral Systems, and Scientific Notation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `G` is outside hexadecimal digits `0-9` and `A-F`, so `0x1G` raises `SyntaxError`. Why the correct answer wins: `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`.
- **B:** Incorrect for this question. Digit `8` is out of range for base-8 octal literals (`0` through `7`), causing `SyntaxError`. Why the correct answer wins: `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`.
- **C:** Correct. Prefix `0b` or `0B` denotes a base-2 integer literal (`11` in decimal). In this case: `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`.
- **D:** Correct. Single underscores between digits are legal visual separators in Python numeric literals. In this case: `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`.
- **E:** Incorrect for this question. Leading zeros on non-zero decimal integers are illegal in Python 3 and raise `SyntaxError`. Why the correct answer wins: `0b1011` and `1_000_000` follow Python 3 literal syntax, whereas `0o18`, `017`, and `0x1G` raise `SyntaxError`.

### Question 5 — B

Answer: Text after `#` outside string literals is ignored until the end of the physical line. Everything from `#` to the end of that physical line is treated as a comment and ignored by the parser without affecting adjacent statements. `#` starts a single-line comment; Python has no dedicated multi-line `/* ... */` comment delimiter. Local study-map skill 1.5 (Variable Naming Rules and PEP-8 Conventions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Everything from `#` to the end of that physical line is treated as a comment and ignored by the parser without affecting adjacent statements.
- **B:** Correct. `#` starts a single-line comment; Python has no dedicated multi-line `/* ... */` comment delimiter. In this case: Everything from `#` to the end of that physical line is treated as a comment and ignored by the parser without affecting adjacent statements.
- **C:** Incorrect for this question. `.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source. Why the correct answer wins: Everything from `#` to the end of that physical line is treated as a comment and ignored by the parser without affecting adjacent statements.
- **D:** Incorrect for this question. Python groups blocks by indentation level, and PEP-8 recommends four spaces per level. Why the correct answer wins: Everything from `#` to the end of that physical line is treated as a comment and ignored by the parser without affecting adjacent statements.

### Question 6 — A

Answer: `0.125`. Raising `2` to negative integer exponent `-3` computes `1 / (2 ** 3)`, returning the floating-point number `0.125`. Evaluates to the floating-point value `0.125` (for example `2 ** -3`). Local study-map skill 1.6 (Arithmetic Operators, Floor Division, Modulo, and Exponentiation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Evaluates to the floating-point value `0.125` (for example `2 ** -3`). In this case: Raising `2` to negative integer exponent `-3` computes `1 / (2 ** 3)`, returning the floating-point number `0.125`.
- **B:** Incorrect for this question. Evaluates to the negative integer `-6`. Why the correct answer wins: Raising `2` to negative integer exponent `-3` computes `1 / (2 ** 3)`, returning the floating-point number `0.125`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Raising `2` to negative integer exponent `-3` computes `1 / (2 ** 3)`, returning the floating-point number `0.125`.
- **D:** Incorrect for this question. Evaluates to the negative integer `-8`. Why the correct answer wins: Raising `2` to negative integer exponent `-3` computes `1 / (2 ** 3)`, returning the floating-point number `0.125`.

### Question 7 — C

Answer: `3.0`. True division `/` binds left-to-right and always returns a `float`, evaluating `(24 / 4) / 2 == 6.0 / 2 == 3.0`. Evaluates to the floating-point value `3.0` because any float operand promotes arithmetic output to `float`. Local study-map skill 1.7 (Operator Precedence, Unary Signs, and Right-Sided Binding), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: True division `/` binds left-to-right and always returns a `float`, evaluating `(24 / 4) / 2 == 6.0 / 2 == 3.0`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: True division `/` binds left-to-right and always returns a `float`, evaluating `(24 / 4) / 2 == 6.0 / 2 == 3.0`.
- **C:** Correct. Evaluates to the floating-point value `3.0` because any float operand promotes arithmetic output to `float`. In this case: True division `/` binds left-to-right and always returns a `float`, evaluating `(24 / 4) / 2 == 6.0 / 2 == 3.0`.
- **D:** Incorrect for this question. Evaluates to the floating-point value `12.5`. Why the correct answer wins: True division `/` binds left-to-right and always returns a `float`, evaluating `(24 / 4) / 2 == 6.0 / 2 == 3.0`.

### Question 8 — C

Answer: `&`. Bitwise AND `&` with `1` (`0b0001`) clears every upper bit and preserves bit `0`. Bitwise AND sets each bit to `1` only where both integer operands have `1`. Local study-map skill 1.8 (Bitwise, Relational, Boolean Operators, and Short-Circuiting), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Left bit-shift multiplies a non-negative integer by `2 ** n`. Why the correct answer wins: Bitwise AND `&` with `1` (`0b0001`) clears every upper bit and preserves bit `0`.
- **B:** Incorrect for this question. Bitwise XOR sets each bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Why the correct answer wins: Bitwise AND `&` with `1` (`0b0001`) clears every upper bit and preserves bit `0`.
- **C:** Correct. Bitwise AND sets each bit to `1` only where both integer operands have `1`. In this case: Bitwise AND `&` with `1` (`0b0001`) clears every upper bit and preserves bit `0`.
- **D:** Incorrect for this question. Logical `and` short-circuits: it returns the first falsy operand, or the right operand if the left is truthy. Why the correct answer wins: Bitwise AND `&` with `1` (`0b0001`) clears every upper bit and preserves bit `0`.

### Question 9 — B

Answer: `-3.0`. Floor division rounds `-2.5` down toward negative infinity to `-3`, and the presence of float `-5.0` makes the result the `float` `-3.0`. Evaluates to the floating-point value `-3.0` because floor division rounds toward negative infinity. Local study-map skill 1.9 (Floating-Point Accuracy, String Operators, and Shortcut Assignments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the negative integer `-3`. Why the correct answer wins: Floor division rounds `-2.5` down toward negative infinity to `-3`, and the presence of float `-5.0` makes the result the `float` `-3.0`.
- **B:** Correct. Evaluates to the floating-point value `-3.0` because floor division rounds toward negative infinity. In this case: Floor division rounds `-2.5` down toward negative infinity to `-3`, and the presence of float `-5.0` makes the result the `float` `-3.0`.
- **C:** Incorrect for this question. Evaluates to the floating-point value `-2.0`; floor division with a float operand returns a floored `float`. Why the correct answer wins: Floor division rounds `-2.5` down toward negative infinity to `-3`, and the presence of float `-5.0` makes the result the `float` `-3.0`.
- **D:** Incorrect for this question. Evaluates to the negative integer `-2`. Why the correct answer wins: Floor division rounds `-2.5` down toward negative infinity to `-3`, and the presence of float `-5.0` makes the result the `float` `-3.0`.

### Question 10 — D

Answer: `2026/10/29`. Passing `sep='/'` converts each integer argument to text and separates them with slashes as `2026/10/29`. Passing `sep="/"` formats year, month, and day separated by slashes. Local study-map skill 1.10 (Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Passing `sep='/'` converts each integer argument to text and separates them with slashes as `2026/10/29`.
- **B:** Incorrect for this question. Passing `sep=";"` joins the three arguments with semicolons. Why the correct answer wins: Passing `sep='/'` converts each integer argument to text and separates them with slashes as `2026/10/29`.
- **C:** Incorrect for this question. Default `sep` in `print()` is a single space and default `end` is `\n`. Why the correct answer wins: Passing `sep='/'` converts each integer argument to text and separates them with slashes as `2026/10/29`.
- **D:** Correct. Passing `sep="/"` formats year, month, and day separated by slashes. In this case: Passing `sep='/'` converts each integer argument to text and separates them with slashes as `2026/10/29`.

### Question 11 — C

Answer: `123`. Both `input()` calls return `str`, so `'12' + '3'` concatenates characters into `'123'` rather than adding numbers to `15`. Concatenating strings `"12" + "3"` yields `"123"` rather than numeric addition `15`. Local study-map skill 1.11 (Console Input with input() and Type Casting (int, float, str, bool)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Both `input()` calls return `str`, so `'12' + '3'` concatenates characters into `'123'` rather than adding numbers to `15`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Both `input()` calls return `str`, so `'12' + '3'` concatenates characters into `'123'` rather than adding numbers to `15`.
- **C:** Correct. Concatenating strings `"12" + "3"` yields `"123"` rather than numeric addition `15`. In this case: Both `input()` calls return `str`, so `'12' + '3'` concatenates characters into `'123'` rather than adding numbers to `15`.
- **D:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Both `input()` calls return `str`, so `'12' + '3'` concatenates characters into `'123'` rather than adding numbers to `15`.

### Question 12 — A

Answer: `B`. `9 < 6` is `False` so the outer `else` evaluates `9 < 12` (`True`), returning `'B'`. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: `9 < 6` is `False` so the outer `else` evaluates `9 < 12` (`True`), returning `'B'`.
- **B:** Incorrect for this question. Prints `D` via the final `else` fallback when every preceding condition is `False`. Why the correct answer wins: `9 < 6` is `False` so the outer `else` evaluates `9 < 12` (`True`), returning `'B'`.
- **C:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: `9 < 6` is `False` so the outer `else` evaluates `9 < 12` (`True`), returning `'B'`.
- **D:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: `9 < 6` is `False` so the outer `else` evaluates `9 < 12` (`True`), returning `'B'`.

### Question 13 — A

Answer: `!=`. `!=` evaluates to `True` whenever `env_name` is unequal in value to `'prod'`. `!=` evaluates to `True` when two operands do not compare equal. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `!=` evaluates to `True` when two operands do not compare equal. In this case: `!=` evaluates to `True` whenever `env_name` is unequal in value to `'prod'`.
- **B:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `!=` evaluates to `True` whenever `env_name` is unequal in value to `'prod'`.
- **C:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `!=` evaluates to `True` whenever `env_name` is unequal in value to `'prod'`.
- **D:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `!=` evaluates to `True` whenever `env_name` is unequal in value to `'prod'`.

### Question 14 — B, C

Answers: `{}`; `None`. An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy. An empty `{}` literal creates an empty `dict` (not a `set`). Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. Why the correct answer wins: An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy.
- **B:** Correct. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. In this case: An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy.
- **C:** Correct. An empty `{}` literal creates an empty `dict` (not a `set`). In this case: An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy.
- **D:** Incorrect for this question. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. Why the correct answer wins: An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy.
- **E:** Incorrect for this question. Any non-empty string, including `'False'`, is truthy in Python; only `''` is a falsy string. Why the correct answer wins: An empty dictionary `{}` and `None` are both falsy, whereas `'False'`, `[0]`, and `(7,)` are truthy.

### Question 15 — B

Answer: `A`. Non-empty string `'False'` has five characters and is truthy in Boolean contexts, so `if enabled:` prints `A`. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Non-empty string `'False'` has five characters and is truthy in Boolean contexts, so `if enabled:` prints `A`.
- **B:** Correct. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. In this case: Non-empty string `'False'` has five characters and is truthy in Boolean contexts, so `if enabled:` prints `A`.
- **C:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Non-empty string `'False'` has five characters and is truthy in Boolean contexts, so `if enabled:` prints `A`.
- **D:** Incorrect for this question. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Why the correct answer wins: Non-empty string `'False'` has five characters and is truthy in Boolean contexts, so `if enabled:` prints `A`.

### Question 16 — D

Answer: `False`. Unary `not` has higher precedence than `and`, so Python evaluates `(not False) and False` -> `True and False` -> `False`. Evaluates to Boolean `False`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Unary `not` has higher precedence than `and`, so Python evaluates `(not False) and False` -> `True and False` -> `False`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Unary `not` has higher precedence than `and`, so Python evaluates `(not False) and False` -> `True and False` -> `False`.
- **C:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Unary `not` has higher precedence than `and`, so Python evaluates `(not False) and False` -> `True and False` -> `False`.
- **D:** Correct. Evaluates to Boolean `False`. In this case: Unary `not` has higher precedence than `and`, so Python evaluates `(not False) and False` -> `True and False` -> `False`.

### Question 17 — C, D

Answers: `not (a or b)`; `(not a) and (not b)`. `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy. By De Morgan law, `not (a or b)` is True exactly when both `a` and `b` are falsy. Requiring both `not a` and `not b` is logically equivalent to `not (a or b)`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `(not a) or (not b)` is equivalent to `not (a and b)`, which still allows one operand to be truthy. Why the correct answer wins: `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy.
- **B:** Incorrect for this question. Because `not` binds tighter than `or`, `not a or b` parses as `(not a) or b`. Why the correct answer wins: `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy.
- **C:** Correct. By De Morgan law, `not (a or b)` is True exactly when both `a` and `b` are falsy. In this case: `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy.
- **D:** Correct. Requiring both `not a` and `not b` is logically equivalent to `not (a or b)`. In this case: `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy.
- **E:** Incorrect for this question. Using `or` here is `True` for *every* number (for example `x = 99` satisfies `x >= 10`). Why the correct answer wins: `not (a or b)` and `(not a) and (not b)` are true if and only if both `a` and `b` are falsy.

### Question 18 — B

Answer: `4`. Doubling `1` steps `wait` through `2, 4, 8, 16` across `4` cycles before `16 < 16` turns `False`. Evaluates to the integer `4`. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Doubling `1` steps `wait` through `2, 4, 8, 16` across `4` cycles before `16 < 16` turns `False`.
- **B:** Correct. Evaluates to the integer `4`. In this case: Doubling `1` steps `wait` through `2, 4, 8, 16` across `4` cycles before `16 < 16` turns `False`.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Doubling `1` steps `wait` through `2, 4, 8, 16` across `4` cycles before `16 < 16` turns `False`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Doubling `1` steps `wait` through `2, 4, 8, 16` across `4` cycles before `16 < 16` turns `False`.

### Question 19 — D

Answer: `*=`. `*=` multiplies `delay` by `2` and rebinds `delay` on every cycle. Augmented multiplication scales a number or repeats a sequence/string. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `*=` multiplies `delay` by `2` and rebinds `delay` on every cycle.
- **B:** Incorrect for this question. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). Why the correct answer wins: `*=` multiplies `delay` by `2` and rebinds `delay` on every cycle.
- **C:** Incorrect for this question. Augmented floor division replaces the variable with its floored quotient. Why the correct answer wins: `*=` multiplies `delay` by `2` and rebinds `delay` on every cycle.
- **D:** Correct. Augmented multiplication scales a number or repeats a sequence/string. In this case: `*=` multiplies `delay` by `2` and rebinds `delay` on every cycle.

### Question 20 — A, B

Answers: `range(5, 0, -1)`; `range(1, 6)`. `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each). A negative step counts downward from `start` while values remain strictly greater than `stop`. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. A negative step counts downward from `start` while values remain strictly greater than `stop`. In this case: `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each).
- **B:** Correct. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. In this case: `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each).
- **C:** Incorrect for this question. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). Why the correct answer wins: `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each).
- **D:** Incorrect for this question. With default step `+1` and `start >= stop`, `range(5, 1)` produces zero iterations. Why the correct answer wins: `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each).
- **E:** Incorrect for this question. `range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three). Why the correct answer wins: `range(5, 0, -1)` yields `5, 4, 3, 2, 1` and `range(1, 6)` yields `1, 2, 3, 4, 5` (five elements each).

### Question 21 — A

Answer: `18`. `range(0, 10, 3)` generates `0, 3, 6, 9` (stopping before `10`), whose sum is `18`. Evaluates to the integer `18`. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `18`. In this case: `range(0, 10, 3)` generates `0, 3, 6, 9` (stopping before `10`), whose sum is `18`.
- **B:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: `range(0, 10, 3)` generates `0, 3, 6, 9` (stopping before `10`), whose sum is `18`.
- **C:** Incorrect for this question. Evaluates to the integer `28`. Why the correct answer wins: `range(0, 10, 3)` generates `0, 3, 6, 9` (stopping before `10`), whose sum is `18`.
- **D:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: `range(0, 10, 3)` generates `0, 3, 6, 9` (stopping before `10`), whose sum is `18`.

### Question 22 — A

Answer: `3`. `'Mon'`, `'Tue'`, and `'Wed'` do not start with `'S'`, incrementing `work` to `3`. Evaluates to the integer `3`. Local study-map skill 2.6 (Iterating Directly Over Sequences and Enumerated Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: `'Mon'`, `'Tue'`, and `'Wed'` do not start with `'S'`, incrementing `work` to `3`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `'Mon'`, `'Tue'`, and `'Wed'` do not start with `'S'`, incrementing `work` to `3`.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: `'Mon'`, `'Tue'`, and `'Wed'` do not start with `'S'`, incrementing `work` to `3`.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `'Mon'`, `'Tue'`, and `'Wed'` do not start with `'S'`, incrementing `work` to `3`.

### Question 23 — C

Answer: `2`. `'sync'` increments `ran` to `1`, `'SKIP'` continues without incrementing, `'clean'` increments `ran` to `2`, and `'STOP'` breaks out before `'backup'`. Evaluates to the integer `2`. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: `'sync'` increments `ran` to `1`, `'SKIP'` continues without incrementing, `'clean'` increments `ran` to `2`, and `'STOP'` breaks out before `'backup'`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `'sync'` increments `ran` to `1`, `'SKIP'` continues without incrementing, `'clean'` increments `ran` to `2`, and `'STOP'` breaks out before `'backup'`.
- **C:** Correct. Evaluates to the integer `2`. In this case: `'sync'` increments `ran` to `1`, `'SKIP'` continues without incrementing, `'clean'` increments `ran` to `2`, and `'STOP'` breaks out before `'backup'`.
- **D:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `'sync'` increments `ran` to `1`, `'SKIP'` continues without incrementing, `'clean'` increments `ran` to `2`, and `'STOP'` breaks out before `'backup'`.

### Question 24 — B

Answer: `continue`. `continue` jumps directly to the next line in `raw_cfg` without exiting the loop. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `continue` jumps directly to the next line in `raw_cfg` without exiting the loop.
- **B:** Correct. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. In this case: `continue` jumps directly to the next line in `raw_cfg` without exiting the loop.
- **C:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `continue` jumps directly to the next line in `raw_cfg` without exiting the loop.
- **D:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `continue` jumps directly to the next line in `raw_cfg` without exiting the loop.

### Question 25 — A, D

Answers: When `break` terminates the loop early before the condition turns `False`; When `return` exits the enclosing function from inside the loop body. Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`. `break` bypasses the loop `else` suite completely. Returning out of the function exits both the loop and any attached `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Returning out of the function exits both the loop and any attached `else` suite. In this case: Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`.
- **B:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`.
- **C:** Incorrect for this question. Normal exhaustion of a `for` iterable runs the attached `else` suite. Why the correct answer wins: Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`.
- **D:** Correct. `break` bypasses the loop `else` suite completely. In this case: Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`.
- **E:** Incorrect for this question. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. Why the correct answer wins: Executing `break` or returning from the enclosing function via `return` exits before normal exhaustion and skips `else:`.

### Question 26 — B

Answer: `DONE`. Slot `12` never occurs so `break` never runs, and exhausting `[9, 11, 14]` executes `else:` to print `DONE`. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Slot `12` never occurs so `break` never runs, and exhausting `[9, 11, 14]` executes `else:` to print `DONE`.
- **B:** Correct. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. In this case: Slot `12` never occurs so `break` never runs, and exhausting `[9, 11, 14]` executes `else:` to print `DONE`.
- **C:** Incorrect for this question. Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early. Why the correct answer wins: Slot `12` never occurs so `break` never runs, and exhausting `[9, 11, 14]` executes `else:` to print `DONE`.
- **D:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Slot `12` never occurs so `break` never runs, and exhausting `[9, 11, 14]` executes `else:` to print `DONE`.

### Question 27 — B

Answer: `4`. Minutes `0` and `30` match `m % 30 == 0` in each of the `2` hours, totaling `2 * 2 == 4`. Evaluates to the integer `4`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Minutes `0` and `30` match `m % 30 == 0` in each of the `2` hours, totaling `2 * 2 == 4`.
- **B:** Correct. Evaluates to the integer `4`. In this case: Minutes `0` and `30` match `m % 30 == 0` in each of the `2` hours, totaling `2 * 2 == 4`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Minutes `0` and `30` match `m % 30 == 0` in each of the `2` hours, totaling `2 * 2 == 4`.
- **D:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: Minutes `0` and `30` match `m % 30 == 0` in each of the `2` hours, totaling `2 * 2 == 4`.

### Question 28 — D

Answer: `for`. `for` introduces the nested iteration over `day`. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `in` tests element or substring membership and also binds loop targets in `for` headers. Why the correct answer wins: `for` introduces the nested iteration over `day`.
- **B:** Incorrect for this question. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. Why the correct answer wins: `for` introduces the nested iteration over `day`.
- **C:** Incorrect for this question. `while` repeats its indented suite as long as its header condition evaluates to truthy. Why the correct answer wins: `for` introduces the nested iteration over `day`.
- **D:** Correct. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. In this case: `for` introduces the nested iteration over `day`.

### Question 29 — D

Answer: `[9, 12, 15]`. Start `1` begins at `9` and exclusive stop `-1` stops before `18`, slicing out the interior `[9, 12, 15]`. Slicing `hours[1:-1]` drops the first (`0`) and last (`-1`) elements. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Selects elements `>= 10` from `[6, 9, 12, 15]` in order. Why the correct answer wins: Start `1` begins at `9` and exclusive stop `-1` stops before `18`, slicing out the interior `[9, 12, 15]`.
- **B:** Incorrect for this question. Slicing `hours[::-2]` steps backward by `2` starting from the final element. Why the correct answer wins: Start `1` begins at `9` and exclusive stop `-1` stops before `18`, slicing out the interior `[9, 12, 15]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Start `1` begins at `9` and exclusive stop `-1` stops before `18`, slicing out the interior `[9, 12, 15]`.
- **D:** Correct. Slicing `hours[1:-1]` drops the first (`0`) and last (`-1`) elements. In this case: Start `1` begins at `9` and exclusive stop `-1` stops before `18`, slicing out the interior `[9, 12, 15]`.

### Question 30 — D

Answer: `[18, 12, 6]`. Omitting start and stop with negative step `-2` starts at the end (`18`) and steps backward by two indices (`4, 2, 0`), returning `[18, 12, 6]`. Slicing `hours[::-2]` steps backward by `2` starting from the final element. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Omitting start and stop with negative step `-2` starts at the end (`18`) and steps backward by two indices (`4, 2, 0`), returning `[18, 12, 6]`.
- **B:** Incorrect for this question. Slicing `hours[1:-1]` drops the first (`0`) and last (`-1`) elements. Why the correct answer wins: Omitting start and stop with negative step `-2` starts at the end (`18`) and steps backward by two indices (`4, 2, 0`), returning `[18, 12, 6]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Omitting start and stop with negative step `-2` starts at the end (`18`) and steps backward by two indices (`4, 2, 0`), returning `[18, 12, 6]`.
- **D:** Correct. Slicing `hours[::-2]` steps backward by `2` starting from the final element. In this case: Omitting start and stop with negative step `-2` starts at the end (`18`) and steps backward by two indices (`4, 2, 0`), returning `[18, 12, 6]`.

### Question 31 — B, C

Answers: `items.append(x)` mutates `items` in place and evaluates to `None`; `items.pop()` removes the final element in place and returns that removed element. `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front. In-place list mutators (`append`, `extend`, `insert`, `remove`, `sort`, `reverse`) return `None` except `pop()`. `pop()` both mutates the list and returns the removed value so callers can inspect it. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `sorted()` is a built-in function that returns a *new* sorted list without modifying `items`. Why the correct answer wins: `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front.
- **B:** Correct. `pop()` both mutates the list and returns the removed value so callers can inspect it. In this case: `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front.
- **C:** Correct. In-place list mutators (`append`, `extend`, `insert`, `remove`, `sort`, `reverse`) return `None` except `pop()`. In this case: `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front.
- **D:** Incorrect for this question. `list.remove(x)` deletes only the *first* matching occurrence of `x`. Why the correct answer wins: `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front.
- **E:** Incorrect for this question. `insert(0, x)` places `x` at the *front* (index `0`), shifting existing elements right. Why the correct answer wins: `append()` mutates in place and returns `None`, while `pop()` removes and returns the final item; `sorted()` is non-mutating, `remove()` deletes only the first match, and `insert(0, x)` inserts at the front.

### Question 32 — B

Answer: `sort()`. `deadlines.sort()` sorts `deadlines` in place (returning `None`). `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. Why the correct answer wins: `deadlines.sort()` sorts `deadlines` in place (returning `None`).
- **B:** Correct. `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. In this case: `deadlines.sort()` sorts `deadlines` in place (returning `None`).
- **C:** Incorrect for this question. `sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`. Why the correct answer wins: `deadlines.sort()` sorts `deadlines` in place (returning `None`).
- **D:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: `deadlines.sort()` sorts `deadlines` in place (returning `None`).

### Question 33 — C

Answer: `del`. `del tasks[0]` removes index `0` in place without returning it. `del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key. Local study-map skill 3.3 (Deleting Elements or Slices with del, len(), and sorted()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. Why the correct answer wins: `del tasks[0]` removes index `0` in place without returning it.
- **B:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: `del tasks[0]` removes index `0` in place without returning it.
- **C:** Correct. `del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key. In this case: `del tasks[0]` removes index `0` in place without returning it.
- **D:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: `del tasks[0]` removes index `0` in place without returning it.

### Question 34 — D

Answer: `99`. Full slice `orig[:]` copies only the outer list; both `orig[0]` and `dup[0]` still reference the *same* inner `[1, 2]` list, so `orig[0][1]` becomes `99`. Evaluates to the integer `99`. Local study-map skill 3.4 (List Aliasing vs Shallow Slicing/Copying and Nested Matrices), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Full slice `orig[:]` copies only the outer list; both `orig[0]` and `dup[0]` still reference the *same* inner `[1, 2]` list, so `orig[0][1]` becomes `99`.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Full slice `orig[:]` copies only the outer list; both `orig[0]` and `dup[0]` still reference the *same* inner `[1, 2]` list, so `orig[0][1]` becomes `99`.
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Full slice `orig[:]` copies only the outer list; both `orig[0]` and `dup[0]` still reference the *same* inner `[1, 2]` list, so `orig[0][1]` becomes `99`.
- **D:** Correct. Evaluates to the integer `99`. In this case: Full slice `orig[:]` copies only the outer list; both `orig[0]` and `dup[0]` still reference the *same* inner `[1, 2]` list, so `orig[0][1]` becomes `99`.

### Question 35 — A

Answer: `[12, 15]`. Filtering `[6, 9, 12, 15]` for `h >= 10` keeps `12` and `15` in order: `[12, 15]`. Selects elements `>= 10` from `[6, 9, 12, 15]` in order. Local study-map skill 3.5 (List Comprehensions with Filtering and Expressions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Selects elements `>= 10` from `[6, 9, 12, 15]` in order. In this case: Filtering `[6, 9, 12, 15]` for `h >= 10` keeps `12` and `15` in order: `[12, 15]`.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Filtering `[6, 9, 12, 15]` for `h >= 10` keeps `12` and `15` in order: `[12, 15]`.
- **C:** Incorrect for this question. Slicing `hours[1:-1]` drops the first (`0`) and last (`-1`) elements. Why the correct answer wins: Filtering `[6, 9, 12, 15]` for `h >= 10` keeps `12` and `15` in order: `[12, 15]`.
- **D:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Filtering `[6, 9, 12, 15]` for `h >= 10` keeps `12` and `15` in order: `[12, 15]`.

### Question 36 — A

Answer: `not in`. `not in` evaluates to `True` when `key` is missing from `required_keys`. `not in` evaluates to `True` when the left operand is absent from the right-hand container. Local study-map skill 3.6 (Membership Testing with in and not in Across Collections), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `not in` evaluates to `True` when the left operand is absent from the right-hand container. In this case: `not in` evaluates to `True` when `key` is missing from `required_keys`.
- **B:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `not in` evaluates to `True` when `key` is missing from `required_keys`.
- **C:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `not in` evaluates to `True` when `key` is missing from `required_keys`.
- **D:** Incorrect for this question. `in` tests element or substring membership and also binds loop targets in `for` headers. Why the correct answer wins: `not in` evaluates to `True` when `key` is missing from `required_keys`.

### Question 37 — C, D

Answers: Assigning `t[0] = 9` on a tuple raises `TypeError` because tuple slot bindings are immutable; `t = 5,`. Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`. Tuples do not support item assignment or item deletion. A trailing comma without parentheses packs a single-element tuple `(5,)`. Local study-map skill 3.7 (Tuple Construction, Single-Element Syntax, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Parentheses without a comma group an arithmetic expression rather than building a tuple. Why the correct answer wins: Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`.
- **B:** Incorrect for this question. `del t[0]` raises `TypeError` because tuples are immutable; only `del t` (unbinding the whole variable) is legal. Why the correct answer wins: Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`.
- **C:** Correct. A trailing comma without parentheses packs a single-element tuple `(5,)`. In this case: Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`.
- **D:** Correct. Tuples do not support item assignment or item deletion. In this case: Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`.
- **E:** Incorrect for this question. `tuple()` expects an iterable, so passing an integer `5` raises `TypeError`. Why the correct answer wins: Assigning `t[0] = 9` raises `TypeError`, and a trailing comma `t = 5,` creates a single-element tuple `(5,)`.

### Question 38 — A

Answer: `25`. Tuple unpacking binds `h = 1` and `m = 15`, so `1 * 10 + 15` evaluates to `25`. Evaluates to the integer `25`. Local study-map skill 3.8 (Mutable Lists Inside Tuples vs Tuples Inside Lists), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `25`. In this case: Tuple unpacking binds `h = 1` and `m = 15`, so `1 * 10 + 15` evaluates to `25`.
- **B:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Tuple unpacking binds `h = 1` and `m = 15`, so `1 * 10 + 15` evaluates to `25`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Tuple unpacking binds `h = 1` and `m = 15`, so `1 * 10 + 15` evaluates to `25`.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Tuple unpacking binds `h = 1` and `m = 15`, so `1 * 10 + 15` evaluates to `25`.

### Question 39 — B

Answer: `get()`. `cfg.get('timeout', 30)` returns the mapped value when present or `30` when absent. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. Local study-map skill 3.9 (Dictionary Creation, Key Lookup, Insertion, Update, and Deletion), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `dict.keys()` returns a dynamic view of the dictionary keys. Why the correct answer wins: `cfg.get('timeout', 30)` returns the mapped value when present or `30` when absent.
- **B:** Correct. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. In this case: `cfg.get('timeout', 30)` returns the mapped value when present or `30` when absent.
- **C:** Incorrect for this question. `dict.values()` returns a dynamic view of the dictionary values. Why the correct answer wins: `cfg.get('timeout', 30)` returns the mapped value when present or `30` when absent.
- **D:** Incorrect for this question. `dict.items()` yields `(key, value)` 2-tuples suitable for two-variable `for k, v in d.items():` unpacking. Why the correct answer wins: `cfg.get('timeout', 30)` returns the mapped value when present or `30` when absent.

### Question 40 — D, E

Answers: Iterating `for x in d:` yields each dictionary key in insertion order; Iterating `for k, v in d.items():` unpacks each `(key, value)` pair cleanly. `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs. Iterating directly over a `dict` iterates over its keys, identical to `for x in d.keys():`. `d.items()` yields 2-tuples pairing each key with its mapped value. Local study-map skill 3.10 (Dictionary Iteration with keys(), values(), items(), and get()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `cfg.values()` searches dictionary *values*, not dictionary keys. Why the correct answer wins: `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs.
- **B:** Incorrect for this question. Iterating bare `d` yields keys alone, so `for k, v in d:` fails unless the keys themselves happen to be 2-element iterables. Why the correct answer wins: `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs.
- **C:** Incorrect for this question. `d.values()` yields only the mapped values, not `(key, value)` pairs. Why the correct answer wins: `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs.
- **D:** Correct. `d.items()` yields 2-tuples pairing each key with its mapped value. In this case: `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs.
- **E:** Correct. Iterating directly over a `dict` iterates over its keys, identical to `for x in d.keys():`. In this case: `for x in d:` iterates keys in insertion order, and `for k, v in d.items():` unpacks `(key, value)` pairs.

### Question 41 — B

Answer: `4`. Doubled `\\` escapes the backslash itself into one literal `\` character followed by ordinary `'t'`, so `'a'`, `'\\'`, `'t'`, `'b'` has length `4`. Evaluates to the integer `4`. Local study-map skill 3.11 (String Literals, Escape Sequences, Quotes, and Multiline Strings), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Doubled `\\` escapes the backslash itself into one literal `\` character followed by ordinary `'t'`, so `'a'`, `'\\'`, `'t'`, `'b'` has length `4`.
- **B:** Correct. Evaluates to the integer `4`. In this case: Doubled `\\` escapes the backslash itself into one literal `\` character followed by ordinary `'t'`, so `'a'`, `'\\'`, `'t'`, `'b'` has length `4`.
- **C:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Doubled `\\` escapes the backslash itself into one literal `\` character followed by ordinary `'t'`, so `'a'`, `'\\'`, `'t'`, `'b'` has length `4`.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Doubled `\\` escapes the backslash itself into one literal `\` character followed by ordinary `'t'`, so `'a'`, `'\\'`, `'t'`, `'b'` has length `4`.

### Question 42 — D

Answer: `line.split()`. `line.split()` with no arguments splits on runs of whitespace and returns `['host', '=', 'db01']`. `str.split()` splits text into a `list` of substrings. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `sep.join(iterable)` is a method on the separator string, taking an iterable of strings. Why the correct answer wins: `line.split()` with no arguments splits on runs of whitespace and returns `['host', '=', 'db01']`.
- **B:** Incorrect for this question. `list.extend(iterable)` appends each element from `iterable` individually and returns `None`. Why the correct answer wins: `line.split()` with no arguments splits on runs of whitespace and returns `['host', '=', 'db01']`.
- **C:** Incorrect for this question. `dict.keys()` returns a dynamic view of the dictionary keys. Why the correct answer wins: `line.split()` with no arguments splits on runs of whitespace and returns `['host', '=', 'db01']`.
- **D:** Correct. `str.split()` splits text into a `list` of substrings. In this case: `line.split()` with no arguments splits on runs of whitespace and returns `['host', '=', 'db01']`.

### Question 43 — A, C

Answers: Every string transformation method returns a brand-new `str` object and leaves the original string unchanged; An escape sequence such as `\n` or `\\` counts as a single character in `len()`. Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In `"a\nb"`, the backslash-`n` pair represents one newline character, so `len("a\nb") == 3`. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. In `"a\nb"`, the backslash-`n` pair represents one newline character, so `len("a\nb") == 3`. In this case: Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`.
- **B:** Incorrect for this question. `str` is immutable, so `del s[0]` raises `TypeError`. Why the correct answer wins: Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`.
- **C:** Correct. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In this case: Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`.
- **D:** Incorrect for this question. `str` does not support item assignment; `s[0] = "X"` raises `TypeError`. Why the correct answer wins: Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`.
- **E:** Incorrect for this question. `sorted()` is a built-in function that returns a *new* sorted list without modifying `items`. Why the correct answer wins: Every string method returns a brand-new `str` because strings are immutable, and escape sequences such as `\n` count as a single character in `len()`.

### Question 44 — A, B

Answers: A function executing a bare `return` statement evaluates to `None` at the call site; A function that reaches the end of its body without any `return` statement returns `None`. Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`. Bare `return` exits immediately and returns the singleton `None`. Falling off the end of a Python function implicitly returns `None`. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Falling off the end of a Python function implicitly returns `None`. In this case: Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`.
- **B:** Correct. Bare `return` exits immediately and returns the singleton `None`. In this case: Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`.
- **C:** Incorrect for this question. Parameters are local variables of the function call frame and disappear when the frame exits. Why the correct answer wins: Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`.
- **D:** Incorrect for this question. The first `return` executed exits the function immediately; subsequent statements in that block are unreachable. Why the correct answer wins: Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`.
- **E:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: Executing a bare `return` statement and reaching the end of a function suite with no `return` both evaluate to `None`.

### Question 45 — D

Answer: `return`. `return` exits `parse_port` and returns the integer `8080` (whereas `yield` would return a generator object). `return` exits the current function immediately and sends a value back to the caller. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `return` exits `parse_port` and returns the integer `8080` (whereas `yield` would return a generator object).
- **B:** Incorrect for this question. `yield` is a reserved Python keyword that turns a function into a generator. Why the correct answer wins: `return` exits `parse_port` and returns the integer `8080` (whereas `yield` would return a generator object).
- **C:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `return` exits `parse_port` and returns the integer `8080` (whereas `yield` would return a generator object).
- **D:** Correct. `return` exits the current function immediately and sends a value back to the caller. In this case: `return` exits `parse_port` and returns the integer `8080` (whereas `yield` would return a generator object).

### Question 46 — A

Answer: `yield`. `yield` emits each port lazily one at a time and makes `port_range` a generator function. `yield` is a reserved Python keyword that turns a function into a generator. Local study-map skill 4.2 (Generator Functions Using yield and Lazy Iteration), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `yield` is a reserved Python keyword that turns a function into a generator. In this case: `yield` emits each port lazily one at a time and makes `port_range` a generator function.
- **B:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `yield` emits each port lazily one at a time and makes `port_range` a generator function.
- **C:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `yield` emits each port lazily one at a time and makes `port_range` a generator function.
- **D:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `yield` emits each port lazily one at a time and makes `port_range` a generator function.

### Question 47 — B

Answer: `6`. `gcd(18, 12)` calls `gcd(12, 6)` and then `gcd(6, 0)`, hitting the base case `b == 0` and returning `6`. Evaluates to the integer `6`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `gcd(18, 12)` calls `gcd(12, 6)` and then `gcd(6, 0)`, hitting the base case `b == 0` and returning `6`.
- **B:** Correct. Evaluates to the integer `6`. In this case: `gcd(18, 12)` calls `gcd(12, 6)` and then `gcd(6, 0)`, hitting the base case `b == 0` and returning `6`.
- **C:** Incorrect for this question. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Why the correct answer wins: `gcd(18, 12)` calls `gcd(12, 6)` and then `gcd(6, 0)`, hitting the base case `b == 0` and returning `6`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `gcd(18, 12)` calls `gcd(12, 6)` and then `gcd(6, 0)`, hitting the base case `b == 0` and returning `6`.

### Question 48 — C

Answer: `==`. `==` checks value equality with `0` to trigger the base case cleanly. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `!=` evaluates to `True` when two operands do not compare equal. Why the correct answer wins: `==` checks value equality with `0` to trigger the base case cleanly.
- **B:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `==` checks value equality with `0` to trigger the base case cleanly.
- **C:** Correct. `==` tests value equality rather than assignment (`=`) or object identity (`is`). In this case: `==` checks value equality with `0` to trigger the base case cleanly.
- **D:** Incorrect for this question. `in` tests element or substring membership and also binds loop targets in `for` headers. Why the correct answer wins: `==` checks value equality with `0` to trigger the base case cleanly.

### Question 49 — A, C

Answers: `calc(10, rate=2)`; `calc(rate=2, base=10)`. `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once. Positional arguments precede keyword arguments and bind each parameter once. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. In this case: `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once.
- **B:** Incorrect for this question. Passing `base` both positionally and by keyword raises `TypeError: got multiple values for argument`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once.
- **C:** Correct. Positional arguments precede keyword arguments and bind each parameter once. In this case: `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once.
- **D:** Incorrect for this question. Passing an unexpected keyword argument raises `TypeError` when the function has no `**kwargs`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once.
- **E:** Incorrect for this question. A positional argument after a keyword argument is a `SyntaxError`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` obey positional-before-keyword ordering and bind each parameter once.

### Question 50 — C

Answer: Raises `TypeError`. Passing an unexpected keyword argument (`jitter=1`) to a function without `**kwargs` raises `TypeError`. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Passing an unexpected keyword argument (`jitter=1`) to a function without `**kwargs` raises `TypeError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Passing an unexpected keyword argument (`jitter=1`) to a function without `**kwargs` raises `TypeError`.
- **C:** Correct. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. In this case: Passing an unexpected keyword argument (`jitter=1`) to a function without `**kwargs` raises `TypeError`.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Passing an unexpected keyword argument (`jitter=1`) to a function without `**kwargs` raises `TypeError`.

### Question 51 — D

Answer: Parameters with default values must follow parameters without default values in `def`. Non-default required parameters (`cmd`) cannot follow parameters with default values (`when='midnight'`) in a `def` signature. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. Why the correct answer wins: Non-default required parameters (`cmd`) cannot follow parameters with default values (`when='midnight'`) in a `def` signature.
- **B:** Incorrect for this question. In `{"a": 1, "a": 2}`, the final binding wins so `len` is `1` and `d["a"]` is `2`. Why the correct answer wins: Non-default required parameters (`cmd`) cannot follow parameters with default values (`when='midnight'`) in a `def` signature.
- **C:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Non-default required parameters (`cmd`) cannot follow parameters with default values (`when='midnight'`) in a `def` signature.
- **D:** Correct. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. In this case: Non-default required parameters (`cmd`) cannot follow parameters with default values (`when='midnight'`) in a `def` signature.

### Question 52 — C

Answer: `30`. Both parameters use their default values (`3` and `10`), returning `3 * 10 == 30`. Evaluates to the integer `30`. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Both parameters use their default values (`3` and `10`), returning `3 * 10 == 30`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Both parameters use their default values (`3` and `10`), returning `3 * 10 == 30`.
- **C:** Correct. Evaluates to the integer `30`. In this case: Both parameters use their default values (`3` and `10`), returning `3 * 10 == 30`.
- **D:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: Both parameters use their default values (`3` and `10`), returning `3 * 10 == 30`.

### Question 53 — C

Answer: Raises `UnboundLocalError`. Assigning `port = 60` anywhere inside `reload_cfg()` makes `port` local throughout `reload_cfg()`, so reading `port` beforehand raises `UnboundLocalError`. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `60`. Why the correct answer wins: Assigning `port = 60` anywhere inside `reload_cfg()` makes `port` local throughout `reload_cfg()`, so reading `port` beforehand raises `UnboundLocalError`.
- **B:** Incorrect for this question. Evaluates to the integer `50`. Why the correct answer wins: Assigning `port = 60` anywhere inside `reload_cfg()` makes `port` local throughout `reload_cfg()`, so reading `port` beforehand raises `UnboundLocalError`.
- **C:** Correct. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. In this case: Assigning `port = 60` anywhere inside `reload_cfg()` makes `port` local throughout `reload_cfg()`, so reading `port` beforehand raises `UnboundLocalError`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Assigning `port = 60` anywhere inside `reload_cfg()` makes `port` local throughout `reload_cfg()`, so reading `port` beforehand raises `UnboundLocalError`.

### Question 54 — A

Answer: `global`. `global reload_count` directs rebinding inside `mark_reload()` to the module-level variable. `global` is a reserved Python keyword that binds a name inside a function to module scope. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `global` is a reserved Python keyword that binds a name inside a function to module scope. In this case: `global reload_count` directs rebinding inside `mark_reload()` to the module-level variable.
- **B:** Incorrect for this question. `import` is a reserved keyword and therefore cannot be used as an ordinary variable name. Why the correct answer wins: `global reload_count` directs rebinding inside `mark_reload()` to the module-level variable.
- **C:** Incorrect for this question. `nonlocal` is a reserved Python keyword and cannot name an ordinary variable. Why the correct answer wins: `global reload_count` directs rebinding inside `mark_reload()` to the module-level variable.
- **D:** Incorrect for this question. `from` is a reserved keyword used in `from module import name` and `raise ... from ...`. Why the correct answer wins: `global reload_count` directs rebinding inside `mark_reload()` to the module-level variable.

### Question 55 — D, E

Answers: `LookupError` is the abstract parent class of both `IndexError` and `KeyError`; `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`. `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`.
- **B:** Incorrect for this question. Standard Python `float` uses binary IEEE-754 rather than exact base-10 representation. Why the correct answer wins: `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`.
- **C:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`.
- **D:** Correct. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). In this case: `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`.
- **E:** Correct. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. In this case: `LookupError` groups `IndexError` and `KeyError`, and `ArithmeticError` groups `ZeroDivisionError` and `OverflowError`.

### Question 56 — C

Answer: `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`. `SystemExit` inherits directly from `BaseException` rather than `Exception`, so `except Exception:` does not intercept it. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Why the correct answer wins: `SystemExit` inherits directly from `BaseException` rather than `Exception`, so `except Exception:` does not intercept it.
- **B:** Incorrect for this question. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Why the correct answer wins: `SystemExit` inherits directly from `BaseException` rather than `Exception`, so `except Exception:` does not intercept it.
- **C:** Correct. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. In this case: `SystemExit` inherits directly from `BaseException` rather than `Exception`, so `except Exception:` does not intercept it.
- **D:** Incorrect for this question. `TypeError` sits under `Exception` rather than under `LookupError` or `SyntaxError`. Why the correct answer wins: `SystemExit` inherits directly from `BaseException` rather than `Exception`, so `except Exception:` does not intercept it.

### Question 57 — A

Answer: Raises `KeyError`. Looking up a missing key on a `dict` with `[]` raises `KeyError`. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. In this case: Looking up a missing key on a `dict` with `[]` raises `KeyError`.
- **B:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Looking up a missing key on a `dict` with `[]` raises `KeyError`.
- **C:** Incorrect for this question. `AttributeError` is raised when accessing or calling a method that does not exist on that type (such as `tuple.append`). Why the correct answer wins: Looking up a missing key on a `dict` with `[]` raises `KeyError`.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Looking up a missing key on a `dict` with `[]` raises `KeyError`.

### Question 58 — D

Answer: `raise`. `raise` throws the specified exception instance immediately. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `raise` throws the specified exception instance immediately.
- **B:** Incorrect for this question. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Why the correct answer wins: `raise` throws the specified exception instance immediately.
- **C:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: `raise` throws the specified exception instance immediately.
- **D:** Correct. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. In this case: `raise` throws the specified exception instance immediately.

### Question 59 — C, E

Answers: Place `except ZeroDivisionError:` above `except ArithmeticError:` so division by zero reaches the specific handler; Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch. Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first. Because `ZeroDivisionError` is a subclass of `ArithmeticError`, putting `ZeroDivisionError` first lets both handlers stay reachable. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first.
- **B:** Incorrect for this question. At most *one* `except` branch executes for a single raised exception. Why the correct answer wins: Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first.
- **C:** Correct. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. In this case: Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first.
- **D:** Incorrect for this question. A bare `except:` must always be the *last* `except` clause in Python 3; placing it earlier is a `SyntaxError`. Why the correct answer wins: Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first.
- **E:** Correct. Because `ZeroDivisionError` is a subclass of `ArithmeticError`, putting `ZeroDivisionError` first lets both handlers stay reachable. In this case: Putting `ZeroDivisionError` above `ArithmeticError` and `KeyError` above `LookupError` lets subclass failures match their dedicated branch first.

### Question 60 — C

Answer: `A`. Because `KeyError` is a subclass of `LookupError` and `LookupError` appears first, the first `except` matches and prints `A`, leaving `except KeyError:` unreachable. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Why the correct answer wins: Because `KeyError` is a subclass of `LookupError` and `LookupError` appears first, the first `except` matches and prints `A`, leaving `except KeyError:` unreachable.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Because `KeyError` is a subclass of `LookupError` and `LookupError` appears first, the first `except` matches and prints `A`, leaving `except KeyError:` unreachable.
- **C:** Correct. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. In this case: Because `KeyError` is a subclass of `LookupError` and `LookupError` appears first, the first `except` matches and prints `A`, leaving `except KeyError:` unreachable.
- **D:** Incorrect for this question. Prints `A B` when two independent `if` statements (rather than `if`/`elif`) both evaluate to `True`. Why the correct answer wins: Because `KeyError` is a subclass of `LookupError` and `LookupError` appears first, the first `except` matches and prints `A`, leaving `except KeyError:` unreachable.
