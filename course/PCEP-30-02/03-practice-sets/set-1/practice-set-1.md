# PCEP – Certified Entry-Level Python Programmer (PCEP-30-02) — Full-Length Mock Exam 1

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 15 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). The live PCEP-30-02 exam has 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item set is an expanded 2x bank timed at 80 minutes to preserve the live pace of about 80 seconds per item. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. Version note: PCEP-30-03 is scheduled for release on October 31, 2026; PCEP-30-02 remains active and earned credentials retain their five-year validity. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A junior developer runs `python3 cli_tool.py` on a utility script and asks how standard CPython executes that `.py` file compared with an ahead-of-time C compiler. Which statement accurately describes CPython's execution model?

- A. Style formatting comments automatically bypass syntax checking during parsing
- B. CPython links source directly into a standalone machine-code binary before the user runs the script
- C. A static linker merges Python modules into firmware without needing a runtime interpreter
- D. CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime

### 2. In a command-line unit converter, the line `ratio = total_miles / 0` contains valid Python tokens and obeys every grammar rule, yet crashes as soon as execution reaches it. Which language layer does this runtime failure violate?

- A. Syntax defines the grammar rules for combining tokens into legal statements
- B. Lexis defines the set of valid tokens and words recognized by the language
- C. Style formatting comments automatically bypass syntax checking during parsing
- D. Semantics determines whether a syntactically valid statement makes sense and what it computes

### 3. A developer is choosing flag variable names for an argument-parsing script. Which two names are reserved Python keywords and therefore raise `SyntaxError` if assigned as variable identifiers? Select two.

- A. `elif`
- B. `list`
- C. `lambda`
- D. `true`
- E. `print`

### 4. A bitmask helper in a CLI utility defines integer constants in non-decimal bases. Which two literals are valid integer literals in Python 3? Select two.

- A. `0x1F`
- B. `017`
- C. `0o18`
- D. `0b1011`
- E. `2nd_total`

### 5. Which two identifiers are legal variable names in Python 3 for storing an intermediate counter in a number-processing script? Select two.

- A. `_temp_value`
- B. `2nd_total`
- C. `raw score`
- D. `user-count`
- E. `total_count_2`

### 6. Complete the CLI pagination expression `full_pages = 47 ____ 10` so `full_pages` is assigned the integer `4` rather than `4.7` or `7`. Which operator fills the blank?

- A. `/`
- B. `//`
- C. `**`
- D. `%`

### 7. An exponentiation check in a number-crunching script evaluates `result = 2 ** 3 ** 2` and displays `result`. Which integer is displayed due to right-sided binding?

- A. `512`
- B. `64`
- C. `18`
- D. `256`

### 8. A permission-flag utility runs `flags = 12 & 5` followed by `print(flags)`. Knowing `12` is `0b1100` and `5` is `0b0101`, what value is printed?

- A. `4`
- B. `15`
- C. `0`
- D. `11`

### 9. A currency helper evaluates `print(0.1 + 0.2 == 0.3)` in Python 3. What is printed and why?

- A. `True`, because Python stores decimal fractions exactly to two decimal places
- B. Raises `ValueError`
- C. Raises `TypeError`
- D. `False`, because binary IEEE-754 floats cannot represent `0.1` and `0.2` exactly

### 10. Complete the call `print('a', 'b', 'c', ____, end='!')` so the script outputs `a-b-c!` on one line. Which keyword argument fills the blank?

- A. `sep='-'`
- B. `end=' '`
- C. `sep=''`
- D. `-=`

### 11. Complete `qty = ____(input('Enter quantity: '))` so typing `12` at the terminal binds `qty` to the integer `12` instead of the string `'12'`. Which built-in callable fills the blank?

- A. `bool()`
- B. `len()`
- C. `str()`
- D. `int()`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass

### 12. Complete the CLI exit-code classifier `if code == 0: state = 'ok'` / `____ code < 100: state = 'warn'` / `else: state = 'fail'` so only the first matching branch runs. Which keyword fills the blank?

- A. `continue`
- B. `pass`
- C. `else`
- D. `elif`

### 13. A number classifier sets `n = 15` and runs: `if n > 20: print('A')` / `elif n >= 10: print('B')` / `elif n > 5: print('C')` / `else: print('D')`. What is printed?

- A. `C`
- B. `A B`
- C. `A`
- D. `B`

### 14. A utility checks `items = []` and `fallback = '0'` with: `if items: print('A')` / `elif not fallback: print('B')` / `else: print('C')`. What does it print?

- A. `A`
- B. Nothing is printed (zero iterations)
- C. `C`
- D. `B`

### 15. When Python evaluates an `if candidate:` header in a CLI validation helper, which two values of `candidate` evaluate to `False`? Select two.

- A. `[0]`
- B. `'False'`
- C. `0`
- D. `'0'`
- E. `[]`

### 16. A CLI range check must evaluate to `True` if and only if integer `x` lies inclusively between `10` and `20`. Which two expressions implement that check correctly? Select two.

- A. `x >= 10 and x = 20`
- B. `10 <= x & x <= 20`
- C. `(x >= 10) or (x <= 20)`
- D. `(x >= 10) and (x <= 20)`
- E. `10 <= x <= 20`

### 17. A short-circuit guard evaluates `outcome = 0 and (10 // 0)` in a CLI calculator. Which value is bound to `outcome` without raising an exception?

- A. `5`
- B. `0`
- C. Raises `ZeroDivisionError`
- D. `False`

### 18. A counter loop sets `n = 2; total = 0` and runs `while n <= 8: total += n; n += 3`, then executes `print(total)`. What is printed?

- A. `14`
- B. `25`
- C. `15`
- D. `7`

### 19. Complete the retry loop `attempts = 0` / `____ attempts < 3:` / `    attempts += 1` so the suite repeats as long as `attempts < 3` remains truthy. Which keyword fills the blank?

- A. `try`
- B. `while`
- C. `elif`
- D. `for`

### 20. Which two `range()` calls each produce exactly three iterations in a `for` loop? Select two.

- A. `range(5)`
- B. `range(0, 3, -1)`
- C. `range(0, 3)`
- D. `range(1, 6, 2)`
- E. `range(1, 3)`

### 21. A countdown tally runs `print(sum(range(5, 0, -2)))`. What integer does it print?

- A. `9`
- B. `15`
- C. `0`
- D. `8`

### 22. A digit-sum snippet runs `s = 0` / `for ch in '204': s += int(ch)` / `print(s)`. What is printed?

- A. Raises `TypeError`
- B. `24`
- C. `3`
- D. `6`

### 23. Complete the filter loop `for k in range(1, 7):` / `    if k % 2 == 0: ____` / `    print(k, end=' ')` so it prints `1 3 5 ` by skipping even numbers without leaving the loop. Which keyword fills the blank?

- A. `return`
- B. `break`
- C. `continue`
- D. `pass`

### 24. A developer stubs an empty branch `if debug_mode:` / `    ____` / `else: run_job()` so the file parses cleanly while doing nothing when `debug_mode` is true. Which statement fills the blank?

- A. `break`
- B. `continue`
- C. `pass`
- D. `return`

### 25. Under which two execution outcomes does the `else:` suite attached to a Python `for` or `while` loop execute? Select two.

- A. When `break` terminates the loop early before the condition turns `False`
- B. When an unhandled exception aborts the loop body
- C. When a `while` condition initially or eventually evaluates to `False` without `break`
- D. When a `for` loop consumes every item in its iterable without hitting `break`
- E. When `return` exits the enclosing function from inside the loop body

### 26. A search snippet runs `for x in [2, 4, 6]:` / `    if x == 5: print('FOUND'); break` / `else: print('DONE')`. What does it print?

- A. Raises `SyntaxError`
- B. `FOUND`
- C. Nothing is printed (zero iterations)
- D. `DONE`

### 27. A triangular counter sets `c = 0` and runs `for i in range(3):` / `    for j in range(i): c += 1` followed by `print(c)`. What is printed?

- A. `0`
- B. `3`
- C. `6`
- D. `9`

### 28. A threshold check sets `pairs = 0` and runs `for a in [1, 2]:` / `    for b in [10, 20, 30]:` / `        if a + b > 21: pairs += 1` / `print(pairs)`. What integer is printed?

- A. `3`
- B. `6`
- C. `5`
- D. `2`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations

### 29. A CLI batch window extracts a middle sublist from `buckets = [10, 20, 30, 40, 50]` using `buckets[1:3]`. Which list value does that slice return?

- A. `[20, 30, 40]`
- B. `[10, 20]`
- C. `[10, 30, 50]`
- D. `[20, 30]`

### 30. Sampling every alternate element from `samples = [10, 20, 30, 40, 50]` with `samples[::2]` produces which list?

- A. `[20, 30]`
- B. `[3, 2, 1]`
- C. `[10, 30, 50]`
- D. Raises `IndexError`

### 31. A number utility runs `data = [3, 1, 2]; result = data.sort(); print(result)`. What is printed?

- A. `None`
- B. `[3, 2, 1]`
- C. `[1, 2, 3]`
- D. Raises `TypeError`

### 32. Complete `queue = [10, 20]; queue.____(30)` so `30` is added at the end of `queue` in place, leaving `[10, 20, 30]`. Which list method fills the blank?

- A. `pop()`
- B. `extend()`
- C. `insert()`
- D. `append()`

### 33. Complete `items = [10, 20, 30, 40, 50]; ____ items[1:3]` so the slice at indices `1` and `2` is removed in place, leaving `[10, 40, 50]`. Which keyword fills the blank?

- A. `sorted()`
- B. `del`
- C. `pop()`
- D. `remove()`

### 34. Given `a = [1, 2, 3]`, which two statements bind `b` to a shallow copy so reassigning `b[0] = 99` leaves `a` equal to `[1, 2, 3]`? Select two.

- A. `b = a.copy()`
- B. `[]`
- C. `b = a.sort()`
- D. `b = a[:]`
- E. `b = a`

### 35. What does `print([x * x for x in range(5) if x % 2 == 0])` output in Python 3?

- A. Raises `SyntaxError`
- B. `[1, 9, 25]`
- C. `[0, 4, 16]`
- D. `[2, 4]`

### 36. Complete the guard `blocked = [401, 403, 500]` / `if status_code ____ blocked:` so the branch runs only when `status_code` is absent from `blocked`. Which operator fills the blank?

- A. `not in`
- B. `!=`
- C. `in`
- D. `is`

### 37. Which two assignments create a one-element `tuple` containing only the integer `7` or `5`? Select two.

- A. `(7)`
- B. `t = tuple([5])`
- C. `(7,)`
- D. `t = tuple()`
- E. `t = tuple(5)`

### 38. A record stores `rec = (1, [2]); rec[1].append(99); print(rec)`. What happens when this code runs?

- A. Raises `TypeError`
- B. `(1, [2, 99])`
- C. `(1, 2, 3)`
- D. Raises `AttributeError`

### 39. A CLI flag map sets `flags = {'v': 1, 'q': 0, 'v': 2}` and runs `print(len(flags))`. What does it print?

- A. Raises `SyntaxError`
- B. `2`
- C. Raises `KeyError`
- D. `3`

### 40. Before reading `cfg['host']` in a CLI startup check, which two expressions safely test whether `'host'` is a key in dictionary `cfg` without risking `KeyError`? Select two.

- A. `'host' in cfg.values()`
- B. `cfg['host']` without `try`
- C. `'host' in cfg.keys()`
- D. Raises `KeyError`
- E. `'host' in cfg`

### 41. A CLI banner sets `msg = 'a\nb'` and runs `print(len(msg))`. What integer is printed?

- A. `3`
- B. `5`
- C. `2`
- D. `4`

### 42. Which two statements accurately describe `str` objects in Python 3? Select two.

- A. Out-of-range string slice bounds such as `s[2:99]` clamp silently instead of raising `IndexError`
- B. Assigning `s[0] = "X"` mutates the first character of `s` in place
- C. Running `del s[0]` deletes the first character from `s` in place
- D. `[1, 99, 3]`
- E. Every string transformation method returns a brand-new `str` object and leaves the original string unchanged

### 43. Complete `if token.____():` so a CLI argument check returns `True` only when `token` is non-empty and consists exclusively of digit characters. Which `str` method fills the blank?

- A. `index()`
- B. `isdigit()`
- C. `startswith()`
- D. `isalpha()`

---

## Block 4 — Functions and Exceptions (28%) — User-defined functions, generators, recursion, argument passing, scope/global, and exception handling

### 44. Which two behaviours are true of `return` and return values in user-defined Python functions? Select two.

- A. Raises `SyntaxError`
- B. A function that reaches the end of its body without any `return` statement returns `None`
- C. Raises `TypeError`
- D. Multiple `return` lines in the same branch all execute sequentially and concatenate their results
- E. A function executing a bare `return` statement evaluates to `None` at the call site

### 45. Complete the header `____ clamp_zero(n):` / `    return n if n > 0 else 0` to define a named function `clamp_zero`. Which keyword fills the blank?

- A. `def`
- B. `lambda`
- C. `return`
- D. `yield`

### 46. Complete `def count_three():` / `    for i in range(3):` / `        ____ i` so calling `list(count_three())` lazily produces `[0, 1, 2]` via a generator. Which keyword fills the blank?

- A. `return`
- B. `yield`
- C. `pass`
- D. `continue`

### 47. A helper defines `def fact(n): return 1 if n <= 1 else n * fact(n - 1)` and runs `print(fact(5))`. What is printed?

- A. `24`
- B. `120`
- C. `60`
- D. Raises `RecursionError`

### 48. A broken countdown defines `def spin(n): return spin(n - 1)` with no base case and calls `spin(3)`. What happens at runtime?

- A. `0`
- B. `None`
- C. Raises `RecursionError`
- D. Raises `ValueError`

### 49. Given `def calc(base, rate): return base * rate`, which two invocations are valid calls in Python 3? Select two.

- A. `calc(10, rate=2)`
- B. `calc(rate=2, base=10)`
- C. `calc(10, base=5)`
- D. `calc(base=10, 2)`
- E. `calc(10, tax=2)`

### 50. Given `def add_pair(a, b): return a + b`, what happens when a caller executes `add_pair(5)` with only one argument?

- A. Raises `SyntaxError`
- B. `0`
- C. Raises `TypeError`
- D. `None`

### 51. A helper defines `def push(v, acc=[]): acc.append(v); return list(acc)` and runs `print(push(1), push(2))`. What does this snippet print?

- A. Raises `TypeError`
- B. `None`
- C. `[1] [2]`
- D. `[1] [1, 2]` (default list is evaluated once at `def` time and shared across calls)

### 52. Why does defining `def format_num(prefix='$', amount): return prefix + str(amount)` fail before the script runs?

- A. Parameters with default values must follow parameters without default values in `def`
- B. Assigning to a variable inside a function creates a new local name unless `global` is declared
- C. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- D. Positional arguments must appear before any keyword arguments in a function call

### 53. A script sets `val = 10`, defines `def bump(): val = 25`, calls `bump()`, and then runs `print(val)`. What is printed?

- A. Raises `UnboundLocalError`
- B. Raises `NameError`
- C. `10`
- D. `25`

### 54. Complete `counter = 0` / `def inc():` / `    ____ counter` / `    counter += 1` so calling `inc()` increments module-level `counter` instead of raising `UnboundLocalError`. Which keyword fills the blank?

- A. `nonlocal`
- B. `return`
- C. `global`
- D. `import`

### 55. Which two built-in exceptions inherit directly from `BaseException` rather than from `Exception`, so a standard `except Exception:` block does not swallow them? Select two.

- A. `TypeError` inherits directly from `Exception`
- B. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- C. `SystemExit` inherits directly from `BaseException`, not from `Exception`
- D. `KeyboardInterrupt` inherits directly from `BaseException`, not from `Exception`
- E. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)

### 56. In Python's built-in exception hierarchy, which relationship links `LookupError`, `IndexError`, and `KeyError`?

- A. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- B. `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`
- C. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)
- D. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`

### 57. A CLI parser executes `int('42.5')` on user text containing a decimal point. What happens at runtime?

- A. Raises `SyntaxError`
- B. Raises `ValueError`
- C. Raises `TypeError`
- D. `0`

### 58. A rate calculator runs `print(15 % 0)` in Python 3. What happens when that expression is evaluated?

- A. `0.0`
- B. `None`
- C. Raises `ZeroDivisionError`
- D. Raises `ValueError`

### 59. When ordering multiple `except` branches on a single `try` block, which two principles govern how Python matches handlers? Select two.

- A. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- B. Duplicate keys overwrite earlier entries, keeping the last value assigned to that key
- C. Positional arguments must appear before any keyword arguments in a function call
- D. Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`
- E. Only the first matching `except` branch runs, so a leading broad superclass handler swallows subclass exceptions before later branches are checked

### 60. Complete `try:` / `    n = int(raw)` / `____ ValueError:` / `    n = 0` so invalid integer strings fall back to `0` without crashing. Which keyword fills the blank?

- A. `except`
- B. `raise`
- C. `else`
- D. `finally`

---

## Answer key and explanations

### Question 1 — D

Answer: CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime. Standard CPython translates `.py` source into bytecode at runtime and executes that bytecode inside the Python virtual machine rather than linking a standalone native executable ahead of time. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. Local study-map skill 1.1 (Compilation vs Interpretation and Execution Model), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Standard CPython translates `.py` source into bytecode at runtime and executes that bytecode inside the Python virtual machine rather than linking a standalone native executable ahead of time.
- **B:** Incorrect for this question. Ahead-of-time native machine-code compilation is what a C or Rust compiler performs, not standard CPython. Why the correct answer wins: Standard CPython translates `.py` source into bytecode at runtime and executes that bytecode inside the Python virtual machine rather than linking a standalone native executable ahead of time.
- **C:** Incorrect for this question. Standard Python scripts still require a Python runtime rather than a static hardware linker. Why the correct answer wins: Standard CPython translates `.py` source into bytecode at runtime and executes that bytecode inside the Python virtual machine rather than linking a standalone native executable ahead of time.
- **D:** Correct. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. In this case: Standard CPython translates `.py` source into bytecode at runtime and executes that bytecode inside the Python virtual machine rather than linking a standalone native executable ahead of time.

### Question 2 — D

Answer: Semantics determines whether a syntactically valid statement makes sense and what it computes. The tokens (lexis) and grammar structure (syntax) are completely legal, so dividing by zero violates runtime semantics when Python actually evaluates the operation. Semantics governs runtime meaning, so dividing a number by zero is syntactically legal yet fails semantically at runtime. Local study-map skill 1.2 (Lexis, Syntax, and Semantics Distinctions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Syntax checks whether tokens appear in a structurally valid arrangement such as matching parentheses and colons. Why the correct answer wins: The tokens (lexis) and grammar structure (syntax) are completely legal, so dividing by zero violates runtime semantics when Python actually evaluates the operation.
- **B:** Incorrect for this question. Lexis is the vocabulary layer governing legal identifiers, literals, operators, and keywords. Why the correct answer wins: The tokens (lexis) and grammar structure (syntax) are completely legal, so dividing by zero violates runtime semantics when Python actually evaluates the operation.
- **C:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: The tokens (lexis) and grammar structure (syntax) are completely legal, so dividing by zero violates runtime semantics when Python actually evaluates the operation.
- **D:** Correct. Semantics governs runtime meaning, so dividing a number by zero is syntactically legal yet fails semantically at runtime. In this case: The tokens (lexis) and grammar structure (syntax) are completely legal, so dividing by zero violates runtime semantics when Python actually evaluates the operation.

### Question 3 — A, C

Answers: `elif`; `lambda`. `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name. `elif` is a reserved Python keyword that introduces an additional conditional branch. `lambda` is a reserved Python keyword and therefore cannot be used as a variable identifier. Local study-map skill 1.3 (Keywords, Instructions, Indentation, and Comments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `elif` is a reserved Python keyword that introduces an additional conditional branch. In this case: `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name.
- **B:** Incorrect for this question. `list` names a built-in type rather than a reserved keyword, so Python permits (but discourages) rebinding it. Why the correct answer wins: `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name.
- **C:** Correct. `lambda` is a reserved Python keyword and therefore cannot be used as a variable identifier. In this case: `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name.
- **D:** Incorrect for this question. Keywords are case-sensitive: `True` is reserved, whereas lowercase `true` is an ordinary identifier. Why the correct answer wins: `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name.
- **E:** Incorrect for this question. `print` is a built-in function name rather than a hard keyword, though shadowing it is poor practice. Why the correct answer wins: `elif` and `lambda` are hard keywords in Python 3, whereas `print` and `list` are built-in identifiers and lowercase `true` is an ordinary unreserved name.

### Question 4 — A, D

Answers: `0b1011`; `0x1F`. `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal. Prefix `0b` or `0B` denotes a base-2 integer literal (`11` in decimal). Prefix `0x` or `0X` denotes a base-16 integer literal (`31` in decimal). Local study-map skill 1.4 (Literals, Numeral Systems, and Scientific Notation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Prefix `0x` or `0X` denotes a base-16 integer literal (`31` in decimal). In this case: `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal.
- **B:** Incorrect for this question. Leading zeros on non-zero decimal integers are illegal in Python 3 and raise `SyntaxError`. Why the correct answer wins: `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal.
- **C:** Incorrect for this question. Digit `8` is out of range for base-8 octal literals (`0` through `7`), causing `SyntaxError`. Why the correct answer wins: `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal.
- **D:** Correct. Prefix `0b` or `0B` denotes a base-2 integer literal (`11` in decimal). In this case: `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal.
- **E:** Incorrect for this question. An identifier cannot begin with a decimal digit, so `2nd_total` fails lexical analysis with `SyntaxError`. Why the correct answer wins: `0b1011` (binary `11`) and `0x1F` (hexadecimal `31`) use legal base prefixes and digits, whereas `0o18` uses digit `8` in octal and `017` uses an illegal leading zero on a decimal literal.

### Question 5 — A, E

Answers: `total_count_2`; `_temp_value`. `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error. Identifiers may contain letters, digits, and underscores provided they do not start with a digit or match a keyword. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. Local study-map skill 1.5 (Variable Naming Rules and PEP-8 Conventions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. In this case: `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error.
- **B:** Incorrect for this question. An identifier cannot begin with a decimal digit, so `2nd_total` fails lexical analysis with `SyntaxError`. Why the correct answer wins: `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error.
- **C:** Incorrect for this question. Whitespace separates tokens and is illegal inside a Python variable name. Why the correct answer wins: `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error.
- **D:** Incorrect for this question. A hyphen is parsed as the subtraction operator rather than part of an identifier. Why the correct answer wins: `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error.
- **E:** Correct. Identifiers may contain letters, digits, and underscores provided they do not start with a digit or match a keyword. In this case: `total_count_2` and `_temp_value` start with a letter or underscore and contain only letters, digits, and underscores; starting with a digit, using `-`, or including a space is a syntax error.

### Question 6 — B

Answer: `//`. Floor division `47 // 10` discards the fractional part toward negative infinity and returns the `int` `4`, whereas `/` yields `4.7` and `%` yields the remainder `7`. Floor division rounds the quotient down toward negative infinity (`math.floor`). Local study-map skill 1.6 (Arithmetic Operators, Floor Division, Modulo, and Exponentiation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. True division always returns a `float`, even when the numerator is an exact multiple of the denominator. Why the correct answer wins: Floor division `47 // 10` discards the fractional part toward negative infinity and returns the `int` `4`, whereas `/` yields `4.7` and `%` yields the remainder `7`.
- **B:** Correct. Floor division rounds the quotient down toward negative infinity (`math.floor`). In this case: Floor division `47 // 10` discards the fractional part toward negative infinity and returns the `int` `4`, whereas `/` yields `4.7` and `%` yields the remainder `7`.
- **C:** Incorrect for this question. Exponentiation has higher precedence than unary minus on its left and binds right-to-left (`2 ** 3 ** 2 == 512`). Why the correct answer wins: Floor division `47 // 10` discards the fractional part toward negative infinity and returns the `int` `4`, whereas `/` yields `4.7` and `%` yields the remainder `7`.
- **D:** Incorrect for this question. Modulo returns the remainder `a - (a // b) * b`, taking the sign of the divisor `b` in Python. Why the correct answer wins: Floor division `47 // 10` discards the fractional part toward negative infinity and returns the `int` `4`, whereas `/` yields `4.7` and `%` yields the remainder `7`.

### Question 7 — A

Answer: `512`. Exponentiation `**` binds from right to left (right-sided binding), so Python evaluates `3 ** 2` (`9`) first and then `2 ** 9`, producing `512` rather than `(2 ** 3) ** 2 == 64`. Evaluates to the integer `512`. Local study-map skill 1.7 (Operator Precedence, Unary Signs, and Right-Sided Binding), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Evaluates to the integer `512`. In this case: Exponentiation `**` binds from right to left (right-sided binding), so Python evaluates `3 ** 2` (`9`) first and then `2 ** 9`, producing `512` rather than `(2 ** 3) ** 2 == 64`.
- **B:** Incorrect for this question. Evaluates to the integer `64`. Why the correct answer wins: Exponentiation `**` binds from right to left (right-sided binding), so Python evaluates `3 ** 2` (`9`) first and then `2 ** 9`, producing `512` rather than `(2 ** 3) ** 2 == 64`.
- **C:** Incorrect for this question. Evaluates to the integer `18`. Why the correct answer wins: Exponentiation `**` binds from right to left (right-sided binding), so Python evaluates `3 ** 2` (`9`) first and then `2 ** 9`, producing `512` rather than `(2 ** 3) ** 2 == 64`.
- **D:** Incorrect for this question. Evaluates to the integer `256`. Why the correct answer wins: Exponentiation `**` binds from right to left (right-sided binding), so Python evaluates `3 ** 2` (`9`) first and then `2 ** 9`, producing `512` rather than `(2 ** 3) ** 2 == 64`.

### Question 8 — A

Answer: `4`. Bitwise AND `&` keeps only bit positions set to `1` in both operands (`0b1100 & 0b0101 == 0b0100`), which evaluates to `4`. Evaluates to the integer `4`. Local study-map skill 1.8 (Bitwise, Relational, Boolean Operators, and Short-Circuiting), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Evaluates to the integer `4`. In this case: Bitwise AND `&` keeps only bit positions set to `1` in both operands (`0b1100 & 0b0101 == 0b0100`), which evaluates to `4`.
- **B:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Bitwise AND `&` keeps only bit positions set to `1` in both operands (`0b1100 & 0b0101 == 0b0100`), which evaluates to `4`.
- **C:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Bitwise AND `&` keeps only bit positions set to `1` in both operands (`0b1100 & 0b0101 == 0b0100`), which evaluates to `4`.
- **D:** Incorrect for this question. Evaluates to the integer `11`. Why the correct answer wins: Bitwise AND `&` keeps only bit positions set to `1` in both operands (`0b1100 & 0b0101 == 0b0100`), which evaluates to `4`.

### Question 9 — D

Answer: `False`, because binary IEEE-754 floats cannot represent `0.1` and `0.2` exactly. IEEE-754 binary floating-point numbers represent `0.1` and `0.2` with tiny rounding residuals whose sum is `0.30000000000000004`, so exact equality with `0.3` prints `False`. `0.1 + 0.2` produces `0.30000000000000004` in binary floating point, so `0.1 + 0.2 == 0.3` evaluates to `False`. Local study-map skill 1.9 (Floating-Point Accuracy, String Operators, and Shortcut Assignments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Standard Python `float` uses binary IEEE-754 rather than exact base-10 representation. Why the correct answer wins: IEEE-754 binary floating-point numbers represent `0.1` and `0.2` with tiny rounding residuals whose sum is `0.30000000000000004`, so exact equality with `0.3` prints `False`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: IEEE-754 binary floating-point numbers represent `0.1` and `0.2` with tiny rounding residuals whose sum is `0.30000000000000004`, so exact equality with `0.3` prints `False`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: IEEE-754 binary floating-point numbers represent `0.1` and `0.2` with tiny rounding residuals whose sum is `0.30000000000000004`, so exact equality with `0.3` prints `False`.
- **D:** Correct. `0.1 + 0.2` produces `0.30000000000000004` in binary floating point, so `0.1 + 0.2 == 0.3` evaluates to `False`. In this case: IEEE-754 binary floating-point numbers represent `0.1` and `0.2` with tiny rounding residuals whose sum is `0.30000000000000004`, so exact equality with `0.3` prints `False`.

### Question 10 — A

Answer: `sep='-'`. Passing `sep='-'` replaces the default space between positional arguments in `print()`, joining `'a'`, `'b'`, and `'c'` as `a-b-c` before `end='!'` appends `!`. The `sep` keyword argument sets the string placed between positional arguments passed to `print()`. Local study-map skill 1.10 (Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. The `sep` keyword argument sets the string placed between positional arguments passed to `print()`. In this case: Passing `sep='-'` replaces the default space between positional arguments in `print()`, joining `'a'`, `'b'`, and `'c'` as `a-b-c` before `end='!'` appends `!`.
- **B:** Incorrect for this question. The `end` keyword argument replaces the default trailing newline `\n` emitted after `print()`. Why the correct answer wins: Passing `sep='-'` replaces the default space between positional arguments in `print()`, joining `'a'`, `'b'`, and `'c'` as `a-b-c` before `end='!'` appends `!`.
- **C:** Incorrect for this question. Passing an empty separator concatenates `print()` arguments with no intervening space. Why the correct answer wins: Passing `sep='-'` replaces the default space between positional arguments in `print()`, joining `'a'`, `'b'`, and `'c'` as `a-b-c` before `end='!'` appends `!`.
- **D:** Incorrect for this question. Augmented subtraction subtracts the right-hand expression from the target variable. Why the correct answer wins: Passing `sep='-'` replaces the default space between positional arguments in `print()`, joining `'a'`, `'b'`, and `'c'` as `a-b-c` before `end='!'` appends `!`.

### Question 11 — D

Answer: `int()`. `input()` always returns a `str`, so wrapping it in `int(...)` parses the decimal digits into an `int` ready for arithmetic. `int()` converts a base-10 integer string or truncates a `float` toward zero (`int(-3.9) == -3`). Local study-map skill 1.11 (Console Input with input() and Type Casting (int, float, str, bool)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `bool()` returns `False` only for `0`, `0.0`, empty collections/strings, and `None`; non-empty strings like `"False"` or `"0"` are `True`. Why the correct answer wins: `input()` always returns a `str`, so wrapping it in `int(...)` parses the decimal digits into an `int` ready for arithmetic.
- **B:** Incorrect for this question. `len(obj)` returns the item or character count of a sequence or collection. Why the correct answer wins: `input()` always returns a `str`, so wrapping it in `int(...)` parses the decimal digits into an `int` ready for arithmetic.
- **C:** Incorrect for this question. `str()` converts numbers or collections to text so `+` can concatenate them with strings without `TypeError`. Why the correct answer wins: `input()` always returns a `str`, so wrapping it in `int(...)` parses the decimal digits into an `int` ready for arithmetic.
- **D:** Correct. `int()` converts a base-10 integer string or truncates a `float` toward zero (`int(-3.9) == -3`). In this case: `input()` always returns a `str`, so wrapping it in `int(...)` parses the decimal digits into an `int` ready for arithmetic.

### Question 12 — D

Answer: `elif`. `elif` chains an additional condition onto the preceding `if` block so `state` is set by at most one branch. `elif` is a reserved Python keyword that introduces an additional conditional branch. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `elif` chains an additional condition onto the preceding `if` block so `state` is set by at most one branch.
- **B:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `elif` chains an additional condition onto the preceding `if` block so `state` is set by at most one branch.
- **C:** Incorrect for this question. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Why the correct answer wins: `elif` chains an additional condition onto the preceding `if` block so `state` is set by at most one branch.
- **D:** Correct. `elif` is a reserved Python keyword that introduces an additional conditional branch. In this case: `elif` chains an additional condition onto the preceding `if` block so `state` is set by at most one branch.

### Question 13 — D

Answer: `B`. `n > 20` is `False`, the first true branch `n >= 10` prints `B`, and Python skips the remaining `elif n > 5` and `else` clauses even though `15 > 5` is also true. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: `n > 20` is `False`, the first true branch `n >= 10` prints `B`, and Python skips the remaining `elif n > 5` and `else` clauses even though `15 > 5` is also true.
- **B:** Incorrect for this question. Prints `A B` when two independent `if` statements (rather than `if`/`elif`) both evaluate to `True`. Why the correct answer wins: `n > 20` is `False`, the first true branch `n >= 10` prints `B`, and Python skips the remaining `elif n > 5` and `else` clauses even though `15 > 5` is also true.
- **C:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: `n > 20` is `False`, the first true branch `n >= 10` prints `B`, and Python skips the remaining `elif n > 5` and `else` clauses even though `15 > 5` is also true.
- **D:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: `n > 20` is `False`, the first true branch `n >= 10` prints `B`, and Python skips the remaining `elif n > 5` and `else` clauses even though `15 > 5` is also true.

### Question 14 — C

Answer: `C`. An empty list `[]` is falsy, whereas the non-empty string `'0'` is truthy (so `not fallback` is `False`), sending execution to `else` and printing `C`. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: An empty list `[]` is falsy, whereas the non-empty string `'0'` is truthy (so `not fallback` is `False`), sending execution to `else` and printing `C`.
- **B:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: An empty list `[]` is falsy, whereas the non-empty string `'0'` is truthy (so `not fallback` is `False`), sending execution to `else` and printing `C`.
- **C:** Correct. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. In this case: An empty list `[]` is falsy, whereas the non-empty string `'0'` is truthy (so `not fallback` is `False`), sending execution to `else` and printing `C`.
- **D:** Incorrect for this question. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Why the correct answer wins: An empty list `[]` is falsy, whereas the non-empty string `'0'` is truthy (so `not fallback` is `False`), sending execution to `else` and printing `C`.

### Question 15 — C, E

Answers: `[]`; `0`. Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`. Evaluates to an empty `list` of length `0`. Evaluates to the integer zero. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. Why the correct answer wins: Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`.
- **B:** Incorrect for this question. Any non-empty string, including `'False'`, is truthy in Python; only `''` is a falsy string. Why the correct answer wins: Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`.
- **C:** Correct. Evaluates to the integer zero. In this case: Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`.
- **D:** Incorrect for this question. A non-empty string `'0'` has length `1` and therefore evaluates to `True` in Boolean contexts. Why the correct answer wins: Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`.
- **E:** Correct. Evaluates to an empty `list` of length `0`. In this case: Empty collections such as `[]` and numeric zero `0` are falsy, whereas non-empty strings (`'0'`, `'False'`) and non-empty lists (`[0]`) have length `1` and evaluate to `True`.

### Question 16 — D, E

Answers: `10 <= x <= 20`; `(x >= 10) and (x <= 20)`. Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. Combining two relational checks with `and` requires both bounds to hold. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Single `=` is assignment rather than comparison and raises `SyntaxError` inside a Boolean expression. Why the correct answer wins: Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error.
- **B:** Incorrect for this question. Bitwise `&` binds tighter than `<=`, so `10 <= x & x <= 20` parses as `10 <= (x & x) <= 20` rather than logical `and`. Why the correct answer wins: Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error.
- **C:** Incorrect for this question. Using `or` here is `True` for *every* number (for example `x = 99` satisfies `x >= 10`). Why the correct answer wins: Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error.
- **D:** Correct. Combining two relational checks with `and` requires both bounds to hold. In this case: Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error.
- **E:** Correct. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. In this case: Both chained `10 <= x <= 20` and `(x >= 10) and (x <= 20)` test both bounds; `or` matches every integer, `&` binds tighter than `<=`, and `=` is a syntax error.

### Question 17 — B

Answer: `0`. Logical `and` short-circuits on the falsy left operand `0` and returns `0` immediately without ever evaluating `10 // 0`. Evaluates to the integer zero. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Logical `and` short-circuits on the falsy left operand `0` and returns `0` immediately without ever evaluating `10 // 0`.
- **B:** Correct. Evaluates to the integer zero. In this case: Logical `and` short-circuits on the falsy left operand `0` and returns `0` immediately without ever evaluating `10 // 0`.
- **C:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised by `/`, `//`, or `%` when the right operand is `0` or `0.0`. Why the correct answer wins: Logical `and` short-circuits on the falsy left operand `0` and returns `0` immediately without ever evaluating `10 // 0`.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Logical `and` short-circuits on the falsy left operand `0` and returns `0` immediately without ever evaluating `10 // 0`.

### Question 18 — C

Answer: `15`. The loop runs for `n = 2`, `n = 5`, and `n = 8`, adding `2 + 5 + 8 = 15` before `n` becomes `11` and terminates the `while` condition. Evaluates to the integer `15`. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `14`. Why the correct answer wins: The loop runs for `n = 2`, `n = 5`, and `n = 8`, adding `2 + 5 + 8 = 15` before `n` becomes `11` and terminates the `while` condition.
- **B:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: The loop runs for `n = 2`, `n = 5`, and `n = 8`, adding `2 + 5 + 8 = 15` before `n` becomes `11` and terminates the `while` condition.
- **C:** Correct. Evaluates to the integer `15`. In this case: The loop runs for `n = 2`, `n = 5`, and `n = 8`, adding `2 + 5 + 8 = 15` before `n` becomes `11` and terminates the `while` condition.
- **D:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: The loop runs for `n = 2`, `n = 5`, and `n = 8`, adding `2 + 5 + 8 = 15` before `n` becomes `11` and terminates the `while` condition.

### Question 19 — B

Answer: `while`. `while` evaluates a Boolean condition before each cycle and repeats the suite until that condition becomes falsy. `while` repeats its indented suite as long as its header condition evaluates to truthy. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. Why the correct answer wins: `while` evaluates a Boolean condition before each cycle and repeats the suite until that condition becomes falsy.
- **B:** Correct. `while` repeats its indented suite as long as its header condition evaluates to truthy. In this case: `while` evaluates a Boolean condition before each cycle and repeats the suite until that condition becomes falsy.
- **C:** Incorrect for this question. `elif` is a reserved Python keyword that introduces an additional conditional branch. Why the correct answer wins: `while` evaluates a Boolean condition before each cycle and repeats the suite until that condition becomes falsy.
- **D:** Incorrect for this question. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. Why the correct answer wins: `while` evaluates a Boolean condition before each cycle and repeats the suite until that condition becomes falsy.

### Question 20 — C, D

Answers: `range(1, 6, 2)`; `range(0, 3)`. `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). `range(0, 3)` produces `0, 1, 2` (three iterations). Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded). Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five.
- **B:** Incorrect for this question. Starting at `0` with stop `3` and step `-1` moves away from `3` and yields zero iterations. Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five.
- **C:** Correct. `range(0, 3)` produces `0, 1, 2` (three iterations). In this case: `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five.
- **D:** Correct. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). In this case: `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five.
- **E:** Incorrect for this question. `range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three). Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(0, 3)` yields `0, 1, 2`; `range(1, 3)` yields two items, `range(0, 3, -1)` yields zero, and `range(5)` yields five.

### Question 21 — A

Answer: `9`. With start `5`, exclusive stop `0`, and step `-2`, `range(5, 0, -2)` generates `5, 3, 1`, whose sum is `9`. Evaluates to the integer `9`. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `9`. In this case: With start `5`, exclusive stop `0`, and step `-2`, `range(5, 0, -2)` generates `5, 3, 1`, whose sum is `9`.
- **B:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: With start `5`, exclusive stop `0`, and step `-2`, `range(5, 0, -2)` generates `5, 3, 1`, whose sum is `9`.
- **C:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: With start `5`, exclusive stop `0`, and step `-2`, `range(5, 0, -2)` generates `5, 3, 1`, whose sum is `9`.
- **D:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: With start `5`, exclusive stop `0`, and step `-2`, `range(5, 0, -2)` generates `5, 3, 1`, whose sum is `9`.

### Question 22 — D

Answer: `6`. Iterating directly over `'204'` yields `'2'`, `'0'`, and `'4'` in order, and summing their integer conversions produces `6`. Evaluates to the integer `6`. Local study-map skill 2.6 (Iterating Directly Over Sequences and Enumerated Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Iterating directly over `'204'` yields `'2'`, `'0'`, and `'4'` in order, and summing their integer conversions produces `6`.
- **B:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: Iterating directly over `'204'` yields `'2'`, `'0'`, and `'4'` in order, and summing their integer conversions produces `6`.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Iterating directly over `'204'` yields `'2'`, `'0'`, and `'4'` in order, and summing their integer conversions produces `6`.
- **D:** Correct. Evaluates to the integer `6`. In this case: Iterating directly over `'204'` yields `'2'`, `'0'`, and `'4'` in order, and summing their integer conversions produces `6`.

### Question 23 — C

Answer: `continue`. `continue` jumps immediately to the next iteration of the `for` loop, whereas `break` stops the loop at `2` and `pass` still prints even numbers. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `continue` jumps immediately to the next iteration of the `for` loop, whereas `break` stops the loop at `2` and `pass` still prints even numbers.
- **B:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `continue` jumps immediately to the next iteration of the `for` loop, whereas `break` stops the loop at `2` and `pass` still prints even numbers.
- **C:** Correct. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. In this case: `continue` jumps immediately to the next iteration of the `for` loop, whereas `break` stops the loop at `2` and `pass` still prints even numbers.
- **D:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `continue` jumps immediately to the next iteration of the `for` loop, whereas `break` stops the loop at `2` and `pass` still prints even numbers.

### Question 24 — C

Answer: `pass`. `pass` is Python's syntactic no-op placeholder required whenever an indented suite cannot be left empty. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `pass` is Python's syntactic no-op placeholder required whenever an indented suite cannot be left empty.
- **B:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `pass` is Python's syntactic no-op placeholder required whenever an indented suite cannot be left empty.
- **C:** Correct. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. In this case: `pass` is Python's syntactic no-op placeholder required whenever an indented suite cannot be left empty.
- **D:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `pass` is Python's syntactic no-op placeholder required whenever an indented suite cannot be left empty.

### Question 25 — C, D

Answers: When a `for` loop consumes every item in its iterable without hitting `break`; When a `while` condition initially or eventually evaluates to `False` without `break`. A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception. Normal exhaustion of a `for` iterable runs the attached `else` suite. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` bypasses the loop `else` suite completely. Why the correct answer wins: A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception.
- **B:** Incorrect for this question. An unhandled exception unwinds the stack rather than running the loop `else` clause. Why the correct answer wins: A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception.
- **C:** Correct. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. In this case: A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception.
- **D:** Correct. Normal exhaustion of a `for` iterable runs the attached `else` suite. In this case: A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception.
- **E:** Incorrect for this question. Returning out of the function exits both the loop and any attached `else` suite. Why the correct answer wins: A loop's `else` clause runs whenever the `for` iterable is exhausted or the `while` condition turns `False` without hitting `break`, `return`, or an unhandled exception.

### Question 26 — D

Answer: `DONE`. Because `5` is never found, `break` never executes; when the list is exhausted normally, the `for ... else` clause runs and prints `DONE`. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Because `5` is never found, `break` never executes; when the list is exhausted normally, the `for ... else` clause runs and prints `DONE`.
- **B:** Incorrect for this question. Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early. Why the correct answer wins: Because `5` is never found, `break` never executes; when the list is exhausted normally, the `for ... else` clause runs and prints `DONE`.
- **C:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Because `5` is never found, `break` never executes; when the list is exhausted normally, the `for ... else` clause runs and prints `DONE`.
- **D:** Correct. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. In this case: Because `5` is never found, `break` never executes; when the list is exhausted normally, the `for ... else` clause runs and prints `DONE`.

### Question 27 — B

Answer: `3`. For `i = 0`, `range(0)` is empty; for `i = 1`, `j = 0` runs once; for `i = 2`, `j = 0, 1` runs twice, giving `0 + 1 + 2 = 3`. Evaluates to the integer `3`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: For `i = 0`, `range(0)` is empty; for `i = 1`, `j = 0` runs once; for `i = 2`, `j = 0, 1` runs twice, giving `0 + 1 + 2 = 3`.
- **B:** Correct. Evaluates to the integer `3`. In this case: For `i = 0`, `range(0)` is empty; for `i = 1`, `j = 0` runs once; for `i = 2`, `j = 0, 1` runs twice, giving `0 + 1 + 2 = 3`.
- **C:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: For `i = 0`, `range(0)` is empty; for `i = 1`, `j = 0` runs once; for `i = 2`, `j = 0, 1` runs twice, giving `0 + 1 + 2 = 3`.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: For `i = 0`, `range(0)` is empty; for `i = 1`, `j = 0` runs once; for `i = 2`, `j = 0, 1` runs twice, giving `0 + 1 + 2 = 3`.

### Question 28 — A

Answer: `3`. The pairs `(2, 20)`, `(1, 30)`, and `(2, 30)` exceed `21`, incrementing `pairs` to `3` across the six `2 x 3` combinations. Evaluates to the integer `3`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: The pairs `(2, 20)`, `(1, 30)`, and `(2, 30)` exceed `21`, incrementing `pairs` to `3` across the six `2 x 3` combinations.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: The pairs `(2, 20)`, `(1, 30)`, and `(2, 30)` exceed `21`, incrementing `pairs` to `3` across the six `2 x 3` combinations.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: The pairs `(2, 20)`, `(1, 30)`, and `(2, 30)` exceed `21`, incrementing `pairs` to `3` across the six `2 x 3` combinations.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: The pairs `(2, 20)`, `(1, 30)`, and `(2, 30)` exceed `21`, incrementing `pairs` to `3` across the six `2 x 3` combinations.

### Question 29 — D

Answer: `[20, 30]`. List slicing starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`. Slicing `items[1:3]` starts at index `1` and stops before index `3`. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Produces the three-element slice `[20, 30, 40]`. Why the correct answer wins: List slicing starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **B:** Incorrect for this question. Produces the two-element list `[10, 20]`. Why the correct answer wins: List slicing starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **C:** Incorrect for this question. Slicing `[::2]` selects every second element starting at index `0`. Why the correct answer wins: List slicing starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **D:** Correct. Slicing `items[1:3]` starts at index `1` and stops before index `3`. In this case: List slicing starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.

### Question 30 — C

Answer: `[10, 30, 50]`. Omitting start and stop with stride `2` selects indices `0`, `2`, and `4`, returning `[10, 30, 50]`. Slicing `[::2]` selects every second element starting at index `0`. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Slicing `items[1:3]` starts at index `1` and stops before index `3`. Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0`, `2`, and `4`, returning `[10, 30, 50]`.
- **B:** Incorrect for this question. Slicing with `[::-1]` or calling `.reverse()` reverses the element order. Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0`, `2`, and `4`, returning `[10, 30, 50]`.
- **C:** Correct. Slicing `[::2]` selects every second element starting at index `0`. In this case: Omitting start and stop with stride `2` selects indices `0`, `2`, and `4`, returning `[10, 30, 50]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Omitting start and stop with stride `2` selects indices `0`, `2`, and `4`, returning `[10, 30, 50]`.

### Question 31 — A

Answer: `None`. `list.sort()` sorts `data` in place and returns `None`, unlike the built-in `sorted(data)` function which returns a new sorted list. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. In this case: `list.sort()` sorts `data` in place and returns `None`, unlike the built-in `sorted(data)` function which returns a new sorted list.
- **B:** Incorrect for this question. Slicing with `[::-1]` or calling `.reverse()` reverses the element order. Why the correct answer wins: `list.sort()` sorts `data` in place and returns `None`, unlike the built-in `sorted(data)` function which returns a new sorted list.
- **C:** Incorrect for this question. Produces the three-element list `[1, 2, 3]`. Why the correct answer wins: `list.sort()` sorts `data` in place and returns `None`, unlike the built-in `sorted(data)` function which returns a new sorted list.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `list.sort()` sorts `data` in place and returns `None`, unlike the built-in `sorted(data)` function which returns a new sorted list.

### Question 32 — D

Answer: `append()`. `append(30)` adds a single element to the tail of `queue` in place, whereas `extend(30)` raises `TypeError` because `30` is not iterable. `list.append(x)` adds `x` as a single element at the end of the list in place and returns `None`. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: `append(30)` adds a single element to the tail of `queue` in place, whereas `extend(30)` raises `TypeError` because `30` is not iterable.
- **B:** Incorrect for this question. `list.extend(iterable)` appends each element from `iterable` individually and returns `None`. Why the correct answer wins: `append(30)` adds a single element to the tail of `queue` in place, whereas `extend(30)` raises `TypeError` because `30` is not iterable.
- **C:** Incorrect for this question. `list.insert(i, x)` places `x` before index `i` in place and returns `None`. Why the correct answer wins: `append(30)` adds a single element to the tail of `queue` in place, whereas `extend(30)` raises `TypeError` because `30` is not iterable.
- **D:** Correct. `list.append(x)` adds `x` as a single element at the end of the list in place and returns `None`. In this case: `append(30)` adds a single element to the tail of `queue` in place, whereas `extend(30)` raises `TypeError` because `30` is not iterable.

### Question 33 — B

Answer: `del`. The `del` statement deletes an entire slice `items[1:3]` in place, whereas `.remove()` deletes one matching value and `.pop()` takes a single integer index. `del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key. Local study-map skill 3.3 (Deleting Elements or Slices with del, len(), and sorted()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`. Why the correct answer wins: The `del` statement deletes an entire slice `items[1:3]` in place, whereas `.remove()` deletes one matching value and `.pop()` takes a single integer index.
- **B:** Correct. `del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key. In this case: The `del` statement deletes an entire slice `items[1:3]` in place, whereas `.remove()` deletes one matching value and `.pop()` takes a single integer index.
- **C:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: The `del` statement deletes an entire slice `items[1:3]` in place, whereas `.remove()` deletes one matching value and `.pop()` takes a single integer index.
- **D:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: The `del` statement deletes an entire slice `items[1:3]` in place, whereas `.remove()` deletes one matching value and `.pop()` takes a single integer index.

### Question 34 — A, D

Answers: `b = a[:]`; `b = a.copy()`. Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`. Full-slice notation `a[:]` creates a new shallow copy of list `a`. `list.copy()` allocates a new shallow copy of `a`. Local study-map skill 3.4 (List Aliasing vs Shallow Slicing/Copying and Nested Matrices), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `list.copy()` allocates a new shallow copy of `a`. In this case: Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **B:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **C:** Incorrect for this question. `a.sort()` sorts `a` in place and assigns `None` to `b`. Why the correct answer wins: Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **D:** Correct. Full-slice notation `a[:]` creates a new shallow copy of list `a`. In this case: Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **E:** Incorrect for this question. Plain assignment `b = a` creates an alias to the exact same list object rather than copying. Why the correct answer wins: Both `b = a[:]` and `b = a.copy()` allocate a separate outer list, whereas `b = a` aliases the same list and `a.sort()` returns `None`.

### Question 35 — C

Answer: `[0, 4, 16]`. From `0, 1, 2, 3, 4`, the `if x % 2 == 0` filter keeps `0, 2, 4` and the comprehension squares each to `[0, 4, 16]`. Squares only the even elements selected by the comprehension filter. Local study-map skill 3.5 (List Comprehensions with Filtering and Expressions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: From `0, 1, 2, 3, 4`, the `if x % 2 == 0` filter keeps `0, 2, 4` and the comprehension squares each to `[0, 4, 16]`.
- **B:** Incorrect for this question. Squares only the odd elements selected by the comprehension filter. Why the correct answer wins: From `0, 1, 2, 3, 4`, the `if x % 2 == 0` filter keeps `0, 2, 4` and the comprehension squares each to `[0, 4, 16]`.
- **C:** Correct. Squares only the even elements selected by the comprehension filter. In this case: From `0, 1, 2, 3, 4`, the `if x % 2 == 0` filter keeps `0, 2, 4` and the comprehension squares each to `[0, 4, 16]`.
- **D:** Incorrect for this question. Produces the filtered two-element list `[2, 4]`. Why the correct answer wins: From `0, 1, 2, 3, 4`, the `if x % 2 == 0` filter keeps `0, 2, 4` and the comprehension squares each to `[0, 4, 16]`.

### Question 36 — A

Answer: `not in`. `not in` tests non-membership across sequences and collections, returning `True` when `status_code` does not match any element of `blocked`. `not in` evaluates to `True` when the left operand is absent from the right-hand container. Local study-map skill 3.6 (Membership Testing with in and not in Across Collections), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `not in` evaluates to `True` when the left operand is absent from the right-hand container. In this case: `not in` tests non-membership across sequences and collections, returning `True` when `status_code` does not match any element of `blocked`.
- **B:** Incorrect for this question. `!=` evaluates to `True` when two operands do not compare equal. Why the correct answer wins: `not in` tests non-membership across sequences and collections, returning `True` when `status_code` does not match any element of `blocked`.
- **C:** Incorrect for this question. `in` tests element or substring membership and also binds loop targets in `for` headers. Why the correct answer wins: `not in` tests non-membership across sequences and collections, returning `True` when `status_code` does not match any element of `blocked`.
- **D:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `not in` tests non-membership across sequences and collections, returning `True` when `status_code` does not match any element of `blocked`.

### Question 37 — B, C

Answers: `(7,)`; `t = tuple([5])`. `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. `tuple([5])` converts a one-element list into the one-element tuple `(5,)`. Local study-map skill 3.7 (Tuple Construction, Single-Element Syntax, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Parentheses without a comma group an arithmetic expression rather than building a tuple. Why the correct answer wins: `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **B:** Correct. `tuple([5])` converts a one-element list into the one-element tuple `(5,)`. In this case: `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **C:** Correct. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. In this case: `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **D:** Incorrect for this question. `tuple()` with no arguments returns the empty tuple `()`. Why the correct answer wins: `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **E:** Incorrect for this question. `tuple()` expects an iterable, so passing an integer `5` raises `TypeError`. Why the correct answer wins: `(7,)` uses the required trailing comma and `tuple([5])` converts a one-element iterable; `(7)` is a plain `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.

### Question 38 — B

Answer: `(1, [2, 99])`. Tuple `rec` cannot rebind slot `0` or slot `1`, but slot `1` references a mutable `list` whose `.append(99)` mutates that list in place, printing `(1, [2, 99])`. Although a tuple cannot rebind its slots, a mutable list stored inside a tuple can still be mutated in place. Local study-map skill 3.8 (Mutable Lists Inside Tuples vs Tuples Inside Lists), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Tuple `rec` cannot rebind slot `0` or slot `1`, but slot `1` references a mutable `list` whose `.append(99)` mutates that list in place, printing `(1, [2, 99])`.
- **B:** Correct. Although a tuple cannot rebind its slots, a mutable list stored inside a tuple can still be mutated in place. In this case: Tuple `rec` cannot rebind slot `0` or slot `1`, but slot `1` references a mutable `list` whose `.append(99)` mutates that list in place, printing `(1, [2, 99])`.
- **C:** Incorrect for this question. Evaluates to the three-element tuple `(1, 2, 3)`. Why the correct answer wins: Tuple `rec` cannot rebind slot `0` or slot `1`, but slot `1` references a mutable `list` whose `.append(99)` mutates that list in place, printing `(1, [2, 99])`.
- **D:** Incorrect for this question. `AttributeError` is raised when accessing or calling a method that does not exist on that type (such as `tuple.append`). Why the correct answer wins: Tuple `rec` cannot rebind slot `0` or slot `1`, but slot `1` references a mutable `list` whose `.append(99)` mutates that list in place, printing `(1, [2, 99])`.

### Question 39 — B

Answer: `2`. Dictionary keys are unique; repeating key `'v'` overwrites its earlier value `1` with `2`, leaving two entries (`'v'` and `'q'`) and length `2`. Evaluates to the integer `2`. Local study-map skill 3.9 (Dictionary Creation, Key Lookup, Insertion, Update, and Deletion), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Dictionary keys are unique; repeating key `'v'` overwrites its earlier value `1` with `2`, leaving two entries (`'v'` and `'q'`) and length `2`.
- **B:** Correct. Evaluates to the integer `2`. In this case: Dictionary keys are unique; repeating key `'v'` overwrites its earlier value `1` with `2`, leaving two entries (`'v'` and `'q'`) and length `2`.
- **C:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Dictionary keys are unique; repeating key `'v'` overwrites its earlier value `1` with `2`, leaving two entries (`'v'` and `'q'`) and length `2`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Dictionary keys are unique; repeating key `'v'` overwrites its earlier value `1` with `2`, leaving two entries (`'v'` and `'q'`) and length `2`.

### Question 40 — C, E

Answers: `'host' in cfg`; `'host' in cfg.keys()`. `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys. The `in` operator on a dictionary checks membership among its *keys* in O(1) average time. Checking membership against `cfg.keys()` tests whether the key exists without raising `KeyError`. Local study-map skill 3.10 (Dictionary Iteration with keys(), values(), items(), and get()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `cfg.values()` searches dictionary *values*, not dictionary keys. Why the correct answer wins: `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys.
- **B:** Incorrect for this question. Direct subscripting `cfg[k]` raises `KeyError` immediately when `k` is missing. Why the correct answer wins: `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys.
- **C:** Correct. Checking membership against `cfg.keys()` tests whether the key exists without raising `KeyError`. In this case: `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys.
- **E:** Correct. The `in` operator on a dictionary checks membership among its *keys* in O(1) average time. In this case: `'host' in cfg` and `'host' in cfg.keys()` both check key membership safely, whereas `cfg['host']` raises `KeyError` if absent and `cfg.values()` inspects values rather than keys.

### Question 41 — A

Answer: `3`. Inside a standard string literal, `\n` is a single escaped newline character rather than two characters, so `'a'`, `'\n'`, and `'b'` give length `3`. Evaluates to the integer `3`. Local study-map skill 3.11 (String Literals, Escape Sequences, Quotes, and Multiline Strings), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: Inside a standard string literal, `\n` is a single escaped newline character rather than two characters, so `'a'`, `'\n'`, and `'b'` give length `3`.
- **B:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Inside a standard string literal, `\n` is a single escaped newline character rather than two characters, so `'a'`, `'\n'`, and `'b'` give length `3`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Inside a standard string literal, `\n` is a single escaped newline character rather than two characters, so `'a'`, `'\n'`, and `'b'` give length `3`.
- **D:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Inside a standard string literal, `\n` is a single escaped newline character rather than two characters, so `'a'`, `'\n'`, and `'b'` give length `3`.

### Question 42 — A, E

Answers: Every string transformation method returns a brand-new `str` object and leaves the original string unchanged; Out-of-range string slice bounds such as `s[2:99]` clamp silently instead of raising `IndexError`. Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. Slicing clamps start and stop indices to valid string bounds, whereas out-of-range single-index `s[99]` raises `IndexError`. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slicing clamps start and stop indices to valid string bounds, whereas out-of-range single-index `s[99]` raises `IndexError`. In this case: Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`.
- **B:** Incorrect for this question. `str` does not support item assignment; `s[0] = "X"` raises `TypeError`. Why the correct answer wins: Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`.
- **C:** Incorrect for this question. `str` is immutable, so `del s[0]` raises `TypeError`. Why the correct answer wins: Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`.
- **D:** Incorrect for this question. Assigning `b = a` binds both names to the same list object, so mutating `b` mutates `a`. Why the correct answer wins: Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`.
- **E:** Correct. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In this case: Strings are immutable (every method returns a new `str`) and out-of-range slices clamp without error, whereas `s[0] = 'X'` and `del s[0]` both raise `TypeError`.

### Question 43 — B

Answer: `isdigit()`. `str.isdigit()` returns `True` when every character in a non-empty string is a digit and `False` otherwise. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. Why the correct answer wins: `str.isdigit()` returns `True` when every character in a non-empty string is a digit and `False` otherwise.
- **B:** Correct. In this case: `str.isdigit()` returns `True` when every character in a non-empty string is a digit and `False` otherwise.
- **C:** Incorrect for this question. `str.startswith(prefix)` checks whether a string begins with `prefix` without manual slicing. Why the correct answer wins: `str.isdigit()` returns `True` when every character in a non-empty string is a digit and `False` otherwise.
- **D:** Incorrect for this question. `str.isalpha()` returns `True` only when the string is non-empty and all characters are alphabetic. Why the correct answer wins: `str.isdigit()` returns `True` when every character in a non-empty string is a digit and `False` otherwise.

### Question 44 — B, E

Answers: A function executing a bare `return` statement evaluates to `None` at the call site; A function that reaches the end of its body without any `return` statement returns `None`. Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site. Bare `return` exits immediately and returns the singleton `None`. Falling off the end of a Python function implicitly returns `None`. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site.
- **B:** Correct. Falling off the end of a Python function implicitly returns `None`. In this case: Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site.
- **D:** Incorrect for this question. The first `return` executed exits the function immediately; subsequent statements in that block are unreachable. Why the correct answer wins: Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site.
- **E:** Correct. Bare `return` exits immediately and returns the singleton `None`. In this case: Both a bare `return` and reaching the end of a function body without hitting `return` evaluate to `None` at the call site.

### Question 45 — A

Answer: `def`. `def` binds a named user-defined function object to `clamp_zero` when the statement executes. `def` introduces a function or generator definition. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `def` introduces a function or generator definition. In this case: `def` binds a named user-defined function object to `clamp_zero` when the statement executes.
- **B:** Incorrect for this question. `lambda` is a reserved Python keyword and therefore cannot be used as a variable identifier. Why the correct answer wins: `def` binds a named user-defined function object to `clamp_zero` when the statement executes.
- **C:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `def` binds a named user-defined function object to `clamp_zero` when the statement executes.
- **D:** Incorrect for this question. `yield` is a reserved Python keyword that turns a function into a generator. Why the correct answer wins: `def` binds a named user-defined function object to `clamp_zero` when the statement executes.

### Question 46 — B

Answer: `yield`. `yield` suspends the function frame and emits one value per iteration, turning `count_three` into a generator function. `yield` is a reserved Python keyword that turns a function into a generator. Local study-map skill 4.2 (Generator Functions Using yield and Lazy Iteration), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `yield` suspends the function frame and emits one value per iteration, turning `count_three` into a generator function.
- **B:** Correct. `yield` is a reserved Python keyword that turns a function into a generator. In this case: `yield` suspends the function frame and emits one value per iteration, turning `count_three` into a generator function.
- **C:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `yield` suspends the function frame and emits one value per iteration, turning `count_three` into a generator function.
- **D:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `yield` suspends the function frame and emits one value per iteration, turning `count_three` into a generator function.

### Question 47 — B

Answer: `120`. Each recursive call multiplies `n` down to the base case `fact(1) == 1`, computing `5 * 4 * 3 * 2 * 1 = 120`. Evaluates to the integer `120` (for example `5!`). Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: Each recursive call multiplies `n` down to the base case `fact(1) == 1`, computing `5 * 4 * 3 * 2 * 1 = 120`.
- **B:** Correct. Evaluates to the integer `120` (for example `5!`). In this case: Each recursive call multiplies `n` down to the base case `fact(1) == 1`, computing `5 * 4 * 3 * 2 * 1 = 120`.
- **C:** Incorrect for this question. Evaluates to the integer `60`. Why the correct answer wins: Each recursive call multiplies `n` down to the base case `fact(1) == 1`, computing `5 * 4 * 3 * 2 * 1 = 120`.
- **D:** Incorrect for this question. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Why the correct answer wins: Each recursive call multiplies `n` down to the base case `fact(1) == 1`, computing `5 * 4 * 3 * 2 * 1 = 120`.

### Question 48 — C

Answer: Raises `RecursionError`. Without a terminating base case, `spin` calls itself until Python exceeds the call-stack limit and raises `RecursionError`. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Without a terminating base case, `spin` calls itself until Python exceeds the call-stack limit and raises `RecursionError`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Without a terminating base case, `spin` calls itself until Python exceeds the call-stack limit and raises `RecursionError`.
- **C:** Correct. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. In this case: Without a terminating base case, `spin` calls itself until Python exceeds the call-stack limit and raises `RecursionError`.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Without a terminating base case, `spin` calls itself until Python exceeds the call-stack limit and raises `RecursionError`.

### Question 49 — A, B

Answers: `calc(10, rate=2)`; `calc(rate=2, base=10)`. `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail. Positional arguments precede keyword arguments and bind each parameter once. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Positional arguments precede keyword arguments and bind each parameter once. In this case: `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail.
- **B:** Correct. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. In this case: `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail.
- **C:** Incorrect for this question. Passing `base` both positionally and by keyword raises `TypeError: got multiple values for argument`. Why the correct answer wins: `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail.
- **D:** Incorrect for this question. A positional argument after a keyword argument is a `SyntaxError`. Why the correct answer wins: `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail.
- **E:** Incorrect for this question. Passing an unexpected keyword argument raises `TypeError` when the function has no `**kwargs`. Why the correct answer wins: `calc(10, rate=2)` places positional before keyword and `calc(rate=2, base=10)` passes both by keyword; keyword-before-positional, duplicate binding of `base`, and unknown keyword `tax` all fail.

### Question 50 — C

Answer: Raises `TypeError`. Calling a two-parameter function with no defaults using one argument raises `TypeError` for the missing required positional argument `b`. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Calling a two-parameter function with no defaults using one argument raises `TypeError` for the missing required positional argument `b`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Calling a two-parameter function with no defaults using one argument raises `TypeError` for the missing required positional argument `b`.
- **C:** Correct. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. In this case: Calling a two-parameter function with no defaults using one argument raises `TypeError` for the missing required positional argument `b`.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Calling a two-parameter function with no defaults using one argument raises `TypeError` for the missing required positional argument `b`.

### Question 51 — D

Answer: `[1] [1, 2]` (default list is evaluated once at `def` time and shared across calls). Default list `acc` is created once when `def` executes and shared across calls that omit `acc`, so the first call returns `[1]` and the second mutates it to `[1, 2]`. Default parameter expressions are evaluated once when `def` executes, so mutating a default list persists across subsequent calls. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Default list `acc` is created once when `def` executes and shared across calls that omit `acc`, so the first call returns `[1]` and the second mutates it to `[1, 2]`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Default list `acc` is created once when `def` executes and shared across calls that omit `acc`, so the first call returns `[1]` and the second mutates it to `[1, 2]`.
- **C:** Incorrect for this question. A fresh list per call happens only when the function uses `None` as the sentinel default and creates `[]` inside the body. Why the correct answer wins: Default list `acc` is created once when `def` executes and shared across calls that omit `acc`, so the first call returns `[1]` and the second mutates it to `[1, 2]`.
- **D:** Correct. Default parameter expressions are evaluated once when `def` executes, so mutating a default list persists across subsequent calls. In this case: Default list `acc` is created once when `def` executes and shared across calls that omit `acc`, so the first call returns `[1]` and the second mutates it to `[1, 2]`.

### Question 52 — A

Answer: Parameters with default values must follow parameters without default values in `def`. In a `def` parameter list, parameters with default values (`prefix='$'`) must come *after* required parameters without defaults (`amount`), or Python raises `SyntaxError`. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. In this case: In a `def` parameter list, parameters with default values (`prefix='$'`) must come *after* required parameters without defaults (`amount`), or Python raises `SyntaxError`.
- **B:** Incorrect for this question. Without `global x`, an assignment `x = ...` inside a function shadows the outer `x` and leaves the module-level variable unchanged. Why the correct answer wins: In a `def` parameter list, parameters with default values (`prefix='$'`) must come *after* required parameters without defaults (`amount`), or Python raises `SyntaxError`.
- **C:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: In a `def` parameter list, parameters with default values (`prefix='$'`) must come *after* required parameters without defaults (`amount`), or Python raises `SyntaxError`.
- **D:** Incorrect for this question. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. Why the correct answer wins: In a `def` parameter list, parameters with default values (`prefix='$'`) must come *after* required parameters without defaults (`amount`), or Python raises `SyntaxError`.

### Question 53 — C

Answer: `10`. Assigning `val = 25` inside `bump()` without `global val` creates a local variable that is discarded on return, leaving module-level `val` equal to `10`. Evaluates to the integer `10`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. Why the correct answer wins: Assigning `val = 25` inside `bump()` without `global val` creates a local variable that is discarded on return, leaving module-level `val` equal to `10`.
- **B:** Incorrect for this question. `NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Assigning `val = 25` inside `bump()` without `global val` creates a local variable that is discarded on return, leaving module-level `val` equal to `10`.
- **C:** Correct. Evaluates to the integer `10`. In this case: Assigning `val = 25` inside `bump()` without `global val` creates a local variable that is discarded on return, leaving module-level `val` equal to `10`.
- **D:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: Assigning `val = 25` inside `bump()` without `global val` creates a local variable that is discarded on return, leaving module-level `val` equal to `10`.

### Question 54 — C

Answer: `global`. `global counter` instructs Python to read and rebind `counter` in module scope rather than treating `counter` as an uninitialized local name. `global` is a reserved Python keyword that binds a name inside a function to module scope. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `nonlocal` is a reserved Python keyword and cannot name an ordinary variable. Why the correct answer wins: `global counter` instructs Python to read and rebind `counter` in module scope rather than treating `counter` as an uninitialized local name.
- **B:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `global counter` instructs Python to read and rebind `counter` in module scope rather than treating `counter` as an uninitialized local name.
- **C:** Correct. `global` is a reserved Python keyword that binds a name inside a function to module scope. In this case: `global counter` instructs Python to read and rebind `counter` in module scope rather than treating `counter` as an uninitialized local name.
- **D:** Incorrect for this question. `import` is a reserved keyword and therefore cannot be used as an ordinary variable name. Why the correct answer wins: `global counter` instructs Python to read and rebind `counter` in module scope rather than treating `counter` as an uninitialized local name.

### Question 55 — C, D

Answers: `SystemExit` inherits directly from `BaseException`, not from `Exception`; `KeyboardInterrupt` inherits directly from `BaseException`, not from `Exception`. `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`. Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`. `KeyboardInterrupt` sits directly under `BaseException` so user Ctrl-C interrupts are not swallowed by `except Exception:`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` sits under `Exception` rather than under `LookupError` or `SyntaxError`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`.
- **B:** Incorrect for this question. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`.
- **C:** Correct. Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`. In this case: `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`.
- **D:** Correct. `KeyboardInterrupt` sits directly under `BaseException` so user Ctrl-C interrupts are not swallowed by `except Exception:`. In this case: `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`.
- **E:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` sit directly under `BaseException`, whereas `ValueError`, `TypeError`, and `LookupError` inherit from `Exception`.

### Question 56 — A

Answer: `LookupError` is the abstract parent class of both `IndexError` and `KeyError`. `LookupError` is the abstract parent class of both `IndexError` (sequence index out of range) and `KeyError` (missing dictionary key). Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). In this case: `LookupError` is the abstract parent class of both `IndexError` (sequence index out of range) and `KeyError` (missing dictionary key).
- **B:** Incorrect for this question. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. Why the correct answer wins: `LookupError` is the abstract parent class of both `IndexError` (sequence index out of range) and `KeyError` (missing dictionary key).
- **C:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: `LookupError` is the abstract parent class of both `IndexError` (sequence index out of range) and `KeyError` (missing dictionary key).
- **D:** Incorrect for this question. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Why the correct answer wins: `LookupError` is the abstract parent class of both `IndexError` (sequence index out of range) and `KeyError` (missing dictionary key).

### Question 57 — B

Answer: Raises `ValueError`. `'42.5'` has an accepted type (`str`), so `int()` rejects its non-integer digits at runtime by raising `ValueError` rather than `TypeError`. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: `'42.5'` has an accepted type (`str`), so `int()` rejects its non-integer digits at runtime by raising `ValueError` rather than `TypeError`.
- **B:** Correct. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). In this case: `'42.5'` has an accepted type (`str`), so `int()` rejects its non-integer digits at runtime by raising `ValueError` rather than `TypeError`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `'42.5'` has an accepted type (`str`), so `int()` rejects its non-integer digits at runtime by raising `ValueError` rather than `TypeError`.
- **D:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: `'42.5'` has an accepted type (`str`), so `int()` rejects its non-integer digits at runtime by raising `ValueError` rather than `TypeError`.

### Question 58 — C

Answer: Raises `ZeroDivisionError`. Modulo `15 % 0` divides by zero just like `/` and `//`, raising `ZeroDivisionError` at runtime. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised by `/`, `//`, or `%` when the right operand is `0` or `0.0`. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the floating-point value `0.0`; true division `/` and scientific notation always yield `float`. Why the correct answer wins: Modulo `15 % 0` divides by zero just like `/` and `//`, raising `ZeroDivisionError` at runtime.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Modulo `15 % 0` divides by zero just like `/` and `//`, raising `ZeroDivisionError` at runtime.
- **C:** Correct. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised by `/`, `//`, or `%` when the right operand is `0` or `0.0`. In this case: Modulo `15 % 0` divides by zero just like `/` and `//`, raising `ZeroDivisionError` at runtime.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Modulo `15 % 0` divides by zero just like `/` and `//`, raising `ZeroDivisionError` at runtime.

### Question 59 — D, E

Answers: Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`; Only the first matching `except` branch runs, so a leading broad superclass handler swallows subclass exceptions before later branches are checked. Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`). `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. Python executes at most one `except` suite per `try` statement, matched in source order. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`).
- **B:** Incorrect for this question. In `{"a": 1, "a": 2}`, the final binding wins so `len` is `1` and `d["a"]` is `2`. Why the correct answer wins: Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`).
- **C:** Incorrect for this question. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. Why the correct answer wins: Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`).
- **D:** Correct. `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. In this case: Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`).
- **E:** Correct. Python executes at most one `except` suite per `try` statement, matched in source order. In this case: Python tests `except` clauses top-to-bottom and executes only the first match, so specific subclasses (like `ZeroDivisionError`) must precede broader superclasses (like `ArithmeticError` or `Exception`).

### Question 60 — A

Answer: `except`. `except` introduces the handler for `ValueError` raised inside the `try` suite. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). In this case: `except` introduces the handler for `ValueError` raised inside the `try` suite.
- **B:** Incorrect for this question. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. Why the correct answer wins: `except` introduces the handler for `ValueError` raised inside the `try` suite.
- **C:** Incorrect for this question. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Why the correct answer wins: `except` introduces the handler for `ValueError` raised inside the `try` suite.
- **D:** Incorrect for this question. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Why the correct answer wins: `except` introduces the handler for `ValueError` raised inside the `try` suite.
