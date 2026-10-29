# PCEP – Certified Entry-Level Python Programmer (PCEP-30-02) — Full-Length Mock Exam 2

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 15 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). The live PCEP-30-02 exam has 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item set is an expanded 2x bank timed at 80 minutes to preserve the live pace of about 80 seconds per item. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. Version note: PCEP-30-03 is scheduled for release on October 31, 2026; PCEP-30-02 remains active and earned credentials retain their five-year validity. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. An engineering trainee compares distributing a log-cleaning script for CPython against compiling a C tool ahead of time. Which two statements accurately contrast interpretation and compilation? Select two.

- A. Ahead-of-time compilation translates the entire program into native machine instructions once before execution
- B. Compiled native binaries require every end user to keep the original C compiler installed to launch the binary
- C. An interpreter executes source cross-platform wherever a compatible Python runtime is installed without recompiling per CPU
- D. A static linker merges Python modules into firmware without needing a runtime interpreter
- E. Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it

### 2. A log parser contains `print("WARN"` with the closing parenthesis omitted on line 40, and Python aborts immediately without executing line 1. Why does line 1 never run?

- A. Semantics determines whether a syntactically valid statement makes sense and what it computes
- B. Leaving an unclosed parenthesis in `print("WARN"` violates syntax and stops the file before any line runs
- C. Lexis defines the set of valid tokens and words recognized by the language
- D. Style formatting comments automatically bypass syntax checking during parsing

### 3. While naming columns in a log-summary script, which two identifiers are reserved Python keywords that cannot be used as variable names? Select two.

- A. `from`
- B. `list`
- C. `assert`
- D. `none`
- E. `total_count_2`

### 4. A log-sampling config defines numeric thresholds in Python source. Which two numeric literals are valid in Python 3? Select two.

- A. `0x1G`
- B. `0o77`
- C. `2.5e-2`
- D. `017`
- E. `0o18`

### 5. Complete the assignment `____ = 'access.log'` so the identifier obeys Python lexical rules and PEP-8 `snake_case` naming for a local variable. Which name fills the blank?

- A. `2nd_total`
- B. `item_price_usd`
- C. `user-count`
- D. `global`

### 6. A timestamp bucketing formula evaluates `bucket = -7 // 2`. What value is assigned to `bucket` in Python 3?

- A. `-3`
- B. `-3.0`
- C. `3`
- D. `-4`

### 7. A log-score adjustment evaluates `penalty = -3 ** 2`. Which integer is assigned to `penalty`?

- A. `-6`
- B. `9`
- C. `-9`
- D. Raises `SyntaxError`

### 8. Complete `diff_bits = mask_a ____ mask_b` so `diff_bits` has a `1` bit only in positions where integers `mask_a` and `mask_b` differ (for example `6` and `3` yield `5`). Which bitwise operator fills the blank?

- A. `^`
- B. `|` (bitwise OR)
- C. `&`
- D. `**`

### 9. A separator banner evaluates `banner = 'ab' * 3`. What string value does `banner` hold?

- A. `'ababab'`
- B. `6`
- C. Raises `TypeError`
- D. `''` (the empty string)

### 10. Complete `print('INFO', ____)` followed on the next line by `print('ready')` so the console displays `INFO ready` on a single output line. Which keyword argument fills the blank?

- A. `end=' '`
- B. `sep='-'`
- C. `+=`
- D. `sep=''`

### 11. A configuration loader reads the non-empty string `'False'` from a text line and evaluates `flag = bool('False')`. What value does `flag` hold?

- A. `True`
- B. Raises `ValueError`
- C. `None`
- D. `False`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass

### 12. A log-severity router sets `lvl = 35` and runs `if lvl >= 50: tag = 'A'` / `elif lvl >= 30: tag = 'B'` / `elif lvl >= 10: tag = 'C'` / `else: tag = 'D'`. Which value is bound to `tag`?

- A. `A`
- B. `D`
- C. `C`
- D. `B`

### 13. Complete `if severity ____ 'CRITICAL':` so Python compares whether `severity` has the same character value as `'CRITICAL'` without a syntax error. Which operator fills the blank?

- A. `!=`
- B. `=`
- C. `==`
- D. `is`

### 14. A whitespace cleaner sets `msg = '   '` (three spaces) and runs `if msg:` / `    print('A' if msg.strip() else 'B')` / `else: print('C')`. What does it print?

- A. Nothing is printed (zero iterations)
- B. `C`
- C. `A`
- D. `B`

### 15. In a log-filter guard `if token:`, which two values of `token` evaluate to `True` in Python 3? Select two.

- A. `''` (the empty string)
- B. `'0'`
- C. `[0]`
- D. `None`
- E. `{}`

### 16. A log line should be archived only when neither `is_debug` (`a`) nor `is_empty` (`b`) is truthy. Which two Boolean expressions are true exactly when both `a` and `b` are falsy? Select two.

- A. `not a or b`
- B. `not (a or b)`
- C. `~`
- D. `(not a) and (not b)`
- E. `(not a) or (not b)`

### 17. A fallback expression evaluates `status = 'ERR' or (1 // 0)`. What value is assigned to `status`?

- A. Raises `ZeroDivisionError`
- B. `False`
- C. `True`
- D. `'ERR'`

### 18. A chunk consumer sets `s = 'abcd'; steps = 0` and runs `while s: s = s[2:]; steps += 1`. What value does `steps` hold when the loop finishes?

- A. `0`
- B. `4`
- C. `2`
- D. `1`

### 19. Complete `remaining = 6` / `while remaining > 0:` / `    remaining ____ 2` so `remaining` decreases by `2` on each pass and terminates after three passes. Which augmented operator fills the blank?

- A. `=`
- B. `!=`
- C. `+=`
- D. `-=`

### 20. Which two `range()` expressions each iterate exactly five times in a `for` loop? Select two.

- A. `range(5)`
- B. `range(1, 3)`
- C. `range(1, 6)`
- D. `range(2, 9, 2)`
- E. `range(5, 1)`

### 21. A script runs `for n in range(5, 1): print(n, end=' ')`. What appears on standard output?

- A. Raises `ValueError`
- B. `0 1 2`
- C. Nothing is printed (zero iterations)
- D. `5`

### 22. Complete `for ch ____ 'ERROR_LOG':` so `ch` takes each character of `'ERROR_LOG'` from left to right. Which keyword fills the blank?

- A. `==`
- B. `from`
- C. `is`
- D. `in`

### 23. Complete `seen = 0` / `for line in ['ok', 'ok', 'STOP', 'ok']:` / `    if line == 'STOP': ____` / `    seen += 1` so `seen` equals `2` when the loop ends. Which keyword fills the blank?

- A. `else`
- B. `break`
- C. `continue`
- D. `pass`

### 24. If the snippet in a log filter instead runs `seen = 0` / `for line in ['ok', 'STOP', 'ok', 'ok']:` / `    if line == 'STOP': continue` / `    seen += 1`, what is the final value of `seen`?

- A. `3`
- B. `0`
- C. `2`
- D. `4`

### 25. Which two events inside a `while` or `for` loop body prevent that loop's attached `else:` suite from running? Select two.

- A. When `return` exits the enclosing function from inside the loop body
- B. When a `for` loop consumes every item in its iterable without hitting `break`
- C. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- D. When a `while` condition initially or eventually evaluates to `False` without `break`
- E. When `break` terminates the loop early before the condition turns `False`

### 26. Complete `for entry in lines:` / `    if 'FATAL' in entry: break` / `____:` / `    print('clean log')` so `'clean log'` prints only when no entry triggered `break`. Which keyword fills the blank?

- A. `elif`
- B. `except`
- C. `else`
- D. `finally`

### 27. A matrix check runs `hits = 0` / `for r in ['a', 'b']:` / `    for c in ['1', '2', '3']:` / `        if r == 'b' or c == '1': hits += 1`. What is `hits` afterward?

- A. `2`
- B. `3`
- C. `6`
- D. `4`

### 28. How many times does `total += 1` execute inside `for row in range(2):` / `    for col in range(3): total += 1`?

- A. `5`
- B. `9`
- C. `3`
- D. `6`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations

### 29. A log tail buffer holds `cols = [10, 20, 30, 40, 50]`. What does `cols[-4:-1]` evaluate to?

- A. Raises `IndexError`
- B. `[20, 30]`
- C. `[20, 30, 40]`
- D. `[40, 30, 20]`

### 30. With `cols = [10, 20, 30, 40, 50]`, what does the negative-stride slice `cols[3:0:-1]` return?

- A. `[20, 30, 40]`
- B. `[3, 2, 1]`
- C. `[]`
- D. `[40, 30, 20]`

### 31. Which two statements accurately describe standard `list` methods and built-in functions in Python 3? Select two.

- A. `items.append(x)` mutates `items` in place and evaluates to `None`
- B. `items.insert(0, x)` appends `x` after the last element of `items`
- C. `sorted(items)` mutates `items` in place and returns `None`
- D. `items.pop()` removes the final element in place and returns that removed element
- E. `items.remove(x)` deletes every occurrence of `x` across the entire list in one call

### 32. A collector runs `buf = [1, 2]; buf.append([3, 4])` and inspects `buf`. What does `buf` contain?

- A. `None`
- B. `[1, 2, [3, 4]]`
- C. `[1, 2, 3, 4]`
- D. Raises `TypeError`

### 33. Complete `ordered = ____(raw_lines)` so `ordered` receives a brand-new sorted list while `raw_lines` keeps its original arrival order. Which built-in callable fills the blank?

- A. `pop()`
- B. `sort()`
- C. `sorted()`
- D. `len()`

### 34. A log buffer holds `a = ['INFO', 'WARN']`. Which two statements create an independent shallow copy `b` so appending to `b` leaves `a` with two items? Select two.

- A. `b = a[:]`
- B. `[[9, 2], [9, 2]]`
- C. `b = list(a)`
- D. `b = a.sort()`
- E. `b = a`

### 35. A log tokenizer evaluates `[len(w) for w in ['err', 'warn', 'ok']]`. Which list does this comprehension build?

- A. `9`
- B. `[3, 4, 2]`
- C. Raises `TypeError`
- D. `[1, 2, 3]`

### 36. What does `'err' in 'kernel_error_42'` evaluate to when filtering log messages in Python 3?

- A. `False`
- B. `True`
- C. Raises `TypeError`
- D. `7`

### 37. Which two statements hold true for `tuple` objects in Python 3? Select two.

- A. Assigning `t[0] = 9` on a tuple raises `TypeError` because tuple slot bindings are immutable
- B. Running `del t[0]` removes the first element while keeping the same tuple object
- C. Calling `t.append(9)` adds an element to the end of tuple `t` in place
- D. `(7)`
- E. Slicing a tuple such as `t[1:3]` returns a new `tuple` containing those elements

### 38. A parser sets `a, b = 10, 20`, runs `a, b = b, a`, and executes `print(a, b)`. What is printed?

- A. `20 10`
- B. `a b`
- C. Raises `ValueError`
- D. Raises `TypeError`

### 39. Complete `hits = counts.____('fail', 0)` so looking up a missing `'fail'` key returns `0` without raising `KeyError` or modifying `counts`. Which `dict` method fills the blank?

- A. `keys()`
- B. `pop()` on a dictionary
- C. `get()`
- D. `values()`

### 40. Given a non-empty dictionary `d = {'ok': 5, 'err': 1}`, which two iteration patterns work as described in Python 3? Select two.

- A. Iterating `for k, v in d.values():` yields `(key, value)` tuples for every entry
- B. Iterating `for k, v in d:` unpacks keys and values directly without calling `.items()`
- C. Iterating `for x in d:` yields each dictionary key in insertion order
- D. Raises `KeyError`
- E. Iterating `for k, v in d.items():` unpacks each `(key, value)` pair cleanly

### 41. A log formatter defines `tag = 'it\'s\t1'` and checks `len(tag)`. What integer does `len(tag)` return?

- A. `6`
- B. Raises `SyntaxError`
- C. `8`
- D. `7`

### 42. A pattern counter evaluates `'aaaa'.count('aa')`. What value does Python return and why?

- A. `3`
- B. `4`
- C. `2` (non-overlapping occurrences counted by `str.count()`)
- D. `1`

### 43. Complete `if line.____('ERROR:'):` so the filter checks whether `line` begins with `'ERROR:'` cleanly without manual index slicing. Which `str` method fills the blank?

- A. `endswith()`
- B. `isdigit()`
- C. `remove()`
- D. `startswith()`

---

## Block 4 — Functions and Exceptions (28%) — User-defined functions, generators, recursion, argument passing, scope/global, and exception handling

### 44. A log summary helper ends with `return ok_count, err_count`. What single object does Python actually return to the caller?

- A. Raises `SyntaxError`
- B. Writing `return a, b` returns a single `tuple` `(a, b)` that the caller can unpack
- C. Multiple `return` lines in the same branch all execute sequentially and concatenate their results
- D. `None`

### 45. Complete `def first_error(lines):` / `    for ln in lines:` / `        if 'ERR' in ln: ____ ln` / `    return None` so the function exits immediately with the matching line. Which keyword fills the blank?

- A. `return`
- B. `yield`
- C. `pass`
- D. `break`

### 46. A script defines `def emit(): yield 10; yield 20`, binds `g = emit()`, runs `first = list(g)`, and then runs `print(list(g))`. What does the second `list(g)` print?

- A. Raises `TypeError`
- B. Raises `StopIteration`
- C. `[]` (a generator iterator can only be consumed once; a second `list(g)` is empty)
- D. `[0, 1, 2]`

### 47. A recursive tally defines `def rec_sum(ns): return 0 if not ns else ns[0] + rec_sum(ns[1:])` and evaluates `rec_sum([4, 5, 7])`. What value does it return?

- A. Raises `RecursionError`
- B. `16`
- C. `0`
- D. `12`

### 48. In `def rec_sum(ns):` / `    if not ns: return ____` / `    return ns[0] + rec_sum(ns[1:])`, which integer literal must fill the blank so `rec_sum([4, 5])` evaluates to `9`?

- A. `0`
- B. `1`
- C. `None`
- D. Raises `IndexError`

### 49. Why does calling `parse_line(sep=',', 'a,b,c')` fail with `SyntaxError` before `parse_line` is ever entered?

- A. Writing `return a, b` returns a single `tuple` `(a, b)` that the caller can unpack
- B. Positional arguments must appear before any keyword arguments in a function call
- C. Parameters with default values must follow parameters without default values in `def`
- D. Assigning to a variable inside a function creates a new local name unless `global` is declared

### 50. Given `def tag_line(msg, level='INFO'): return f'{level}:{msg}'`, what happens when a caller invokes `tag_line('boot', msg='ready')`?

- A. Raises `TypeError`
- B. `None`
- C. Raises `ValueError`
- D. Raises `NameError`

### 51. Which two `def` headers are syntactically valid function signatures in Python 3? Select two.

- A. `def connect(host, port=5432):`
- B. `def connect(host="localhost", port=5432):`
- C. `def connect(host="localhost", port):`
- D. `def connect("localhost", port=80):`
- E. `def connect(host, host=80):`

### 52. Given `def scale(x, factor=3): return x * factor`, what value does `scale(5)` return when the second argument is omitted?

- A. `15`
- B. Raises `TypeError`
- C. `10`
- D. `5`

### 53. A script sets `count = 5`, defines `def step(): print(count); count = 6`, and calls `step()`. What happens at runtime?

- A. `5`
- B. Raises `NameError`
- C. Raises `UnboundLocalError`
- D. `6`

### 54. Which two rules govern variable scope inside a user-defined function when `global` is NOT used? Select two.

- A. Assigning to a variable inside a function creates a new local name unless `global` is declared
- B. Multiple `return` lines in the same branch all execute sequentially and concatenate their results
- C. Raises `UnboundLocalError` because assigning to the name later in the function marks it local throughout the body
- D. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- E. Duplicate keys overwrite earlier entries, keeping the last value assigned to that key

### 55. Which built-in exception class is the direct abstract parent of `ZeroDivisionError` in Python 3?

- A. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- B. `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`
- C. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)
- D. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`

### 56. Which two relationships in Python's built-in exception hierarchy explain why `except LookupError:` catches both bad list indices and missing dict keys? Select two.

- A. `TypeError` inherits directly from `Exception`
- B. `KeyError` is a direct subclass of `LookupError`
- C. `SystemExit` inherits directly from `BaseException`, not from `Exception`
- D. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)
- E. `IndexError` is a direct subclass of `LookupError`

### 57. A log counter sets `levels = {'INFO': 3}` and evaluates `levels['WARN']` directly with square brackets. Which exception is raised?

- A. `None`
- B. Raises `KeyError`
- C. Raises `ValueError`
- D. Raises `IndexError`

### 58. Complete `if port < 1:` / `    ____ ValueError('port must be positive')` so an invalid port immediately triggers a `ValueError`. Which keyword fills the blank?

- A. `raise`
- B. `return`
- C. `assert`
- D. `except`

### 59. Which two `except`-branch orderings keep both the specific handler and the broader parent handler reachable? Select two.

- A. Place a bare `except:` clause above `except TypeError:` as a fallback default
- B. Place `except ZeroDivisionError:` above `except ArithmeticError:` so division by zero reaches the specific handler
- C. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler
- D. Python runs every `except` clause whose class matches the raised exception from top to bottom
- E. Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch

### 60. Complete `try:` / `    process(log_file)` / `____:` / `    cleanup_temp()` so `cleanup_temp()` runs whether `process()` returns normally or raises an exception. Which keyword fills the blank?

- A. `pass`
- B. `finally`
- C. `except`
- D. `else`

---

## Answer key and explanations

### Question 1 — A, C

Answers: An interpreter executes source cross-platform wherever a compatible Python runtime is installed without recompiling per CPU; Ahead-of-time compilation translates the entire program into native machine instructions once before execution. An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution. Interpreted Python scripts run unchanged across operating systems that provide the matching Python interpreter. A compiler translates the whole program ahead of time into target machine code rather than interpreting source on each run. Local study-map skill 1.1 (Compilation vs Interpretation and Execution Model), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. A compiler translates the whole program ahead of time into target machine code rather than interpreting source on each run. In this case: An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution.
- **B:** Incorrect for this question. A compiled standalone executable runs directly on the target OS without shipping the compiler. Why the correct answer wins: An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution.
- **C:** Correct. Interpreted Python scripts run unchanged across operating systems that provide the matching Python interpreter. In this case: An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution.
- **D:** Incorrect for this question. Standard Python scripts still require a Python runtime rather than a static hardware linker. Why the correct answer wins: An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution.
- **E:** Incorrect for this question. `.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source. Why the correct answer wins: An interpreter runs the `.py` source wherever a compatible Python runtime exists without per-CPU recompilation, whereas an ahead-of-time compiler translates the whole program into native machine code before execution.

### Question 2 — B

Answer: Leaving an unclosed parenthesis in `print("WARN"` violates syntax and stops the file before any line runs. CPython parses the entire file for grammar rules (syntax) before executing bytecode, so an unclosed parenthesis raises `SyntaxError` prior to running line 1. Unbalanced delimiters break Python grammar rules during the parsing phase before line 1 executes. Local study-map skill 1.2 (Lexis, Syntax, and Semantics Distinctions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Semantics governs runtime meaning, so dividing a number by zero is syntactically legal yet fails semantically at runtime. Why the correct answer wins: CPython parses the entire file for grammar rules (syntax) before executing bytecode, so an unclosed parenthesis raises `SyntaxError` prior to running line 1.
- **B:** Correct. Unbalanced delimiters break Python grammar rules during the parsing phase before line 1 executes. In this case: CPython parses the entire file for grammar rules (syntax) before executing bytecode, so an unclosed parenthesis raises `SyntaxError` prior to running line 1.
- **C:** Incorrect for this question. Lexis is the vocabulary layer governing legal identifiers, literals, operators, and keywords. Why the correct answer wins: CPython parses the entire file for grammar rules (syntax) before executing bytecode, so an unclosed parenthesis raises `SyntaxError` prior to running line 1.
- **D:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: CPython parses the entire file for grammar rules (syntax) before executing bytecode, so an unclosed parenthesis raises `SyntaxError` prior to running line 1.

### Question 3 — A, C

Answers: `assert`; `from`. `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier. `assert` is a reserved Python keyword used for debugging checks. `from` is a reserved keyword used in `from module import name` and `raise ... from ...`. Local study-map skill 1.3 (Keywords, Instructions, Indentation, and Comments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `from` is a reserved keyword used in `from module import name` and `raise ... from ...`. In this case: `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier.
- **B:** Incorrect for this question. `list` names a built-in type rather than a reserved keyword, so Python permits (but discourages) rebinding it. Why the correct answer wins: `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier.
- **C:** Correct. `assert` is a reserved Python keyword used for debugging checks. In this case: `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier.
- **D:** Incorrect for this question. Only capitalized `None` is a keyword; lowercase `none` is not reserved by Python. Why the correct answer wins: `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier.
- **E:** Incorrect for this question. Identifiers may contain letters, digits, and underscores provided they do not start with a digit or match a keyword. Why the correct answer wins: `assert` and `from` are reserved keywords in Python 3, whereas `list` is a built-in type name, lowercase `none` is unreserved, and `total_count_2` is an ordinary identifier.

### Question 4 — B, C

Answers: `2.5e-2`; `0o77`. `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex. `2.5e-2` is valid scientific notation representing `0.025` as a `float`. `0o77` is a valid base-8 integer literal equal to `63` in decimal. Local study-map skill 1.4 (Literals, Numeral Systems, and Scientific Notation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `G` is outside hexadecimal digits `0-9` and `A-F`, so `0x1G` raises `SyntaxError`. Why the correct answer wins: `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex.
- **B:** Correct. `0o77` is a valid base-8 integer literal equal to `63` in decimal. In this case: `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex.
- **C:** Correct. `2.5e-2` is valid scientific notation representing `0.025` as a `float`. In this case: `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex.
- **D:** Incorrect for this question. Leading zeros on non-zero decimal integers are illegal in Python 3 and raise `SyntaxError`. Why the correct answer wins: `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex.
- **E:** Incorrect for this question. Digit `8` is out of range for base-8 octal literals (`0` through `7`), causing `SyntaxError`. Why the correct answer wins: `2.5e-2` (float `0.025`) and `0o77` (octal `63`) follow Python literal rules, whereas `0o18` has an invalid octal digit, `017` has an illegal leading zero, and `0x1G` uses `G` in hex.

### Question 5 — B

Answer: `item_price_usd`. `item_price_usd` uses lowercase letters and underscores as PEP-8 recommends, whereas `user-count` contains `-`, `2nd_total` starts with a digit, and `global` is a keyword. Lowercase words separated by underscores (`snake_case`) follow PEP-8 variable naming recommendations. Local study-map skill 1.5 (Variable Naming Rules and PEP-8 Conventions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. An identifier cannot begin with a decimal digit, so `2nd_total` fails lexical analysis with `SyntaxError`. Why the correct answer wins: `item_price_usd` uses lowercase letters and underscores as PEP-8 recommends, whereas `user-count` contains `-`, `2nd_total` starts with a digit, and `global` is a keyword.
- **B:** Correct. Lowercase words separated by underscores (`snake_case`) follow PEP-8 variable naming recommendations. In this case: `item_price_usd` uses lowercase letters and underscores as PEP-8 recommends, whereas `user-count` contains `-`, `2nd_total` starts with a digit, and `global` is a keyword.
- **C:** Incorrect for this question. A hyphen is parsed as the subtraction operator rather than part of an identifier. Why the correct answer wins: `item_price_usd` uses lowercase letters and underscores as PEP-8 recommends, whereas `user-count` contains `-`, `2nd_total` starts with a digit, and `global` is a keyword.
- **D:** Incorrect for this question. `global` is a reserved Python keyword that binds a name inside a function to module scope. Why the correct answer wins: `item_price_usd` uses lowercase letters and underscores as PEP-8 recommends, whereas `user-count` contains `-`, `2nd_total` starts with a digit, and `global` is a keyword.

### Question 6 — D

Answer: `-4`. Floor division `//` rounds toward negative infinity rather than toward zero, so `-3.5` floors to the integer `-4`. `-7 // 2` rounds `-3.5` down toward negative infinity to `-4`, not `-3`. Local study-map skill 1.6 (Arithmetic Operators, Floor Division, Modulo, and Exponentiation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the negative integer `-3`. Why the correct answer wins: Floor division `//` rounds toward negative infinity rather than toward zero, so `-3.5` floors to the integer `-4`.
- **B:** Incorrect for this question. Evaluates to the floating-point value `-3.0` because floor division rounds toward negative infinity. Why the correct answer wins: Floor division `//` rounds toward negative infinity rather than toward zero, so `-3.5` floors to the integer `-4`.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Floor division `//` rounds toward negative infinity rather than toward zero, so `-3.5` floors to the integer `-4`.
- **D:** Correct. `-7 // 2` rounds `-3.5` down toward negative infinity to `-4`, not `-3`. In this case: Floor division `//` rounds toward negative infinity rather than toward zero, so `-3.5` floors to the integer `-4`.

### Question 7 — C

Answer: `-9`. Exponentiation `**` has higher precedence than unary negation `-` on its left, so Python computes `-(3 ** 2)` and binds `-9` rather than `(-3) ** 2 == 9`. Evaluates to the negative integer `-9`. Local study-map skill 1.7 (Operator Precedence, Unary Signs, and Right-Sided Binding), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the negative integer `-6`. Why the correct answer wins: Exponentiation `**` has higher precedence than unary negation `-` on its left, so Python computes `-(3 ** 2)` and binds `-9` rather than `(-3) ** 2 == 9`.
- **B:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: Exponentiation `**` has higher precedence than unary negation `-` on its left, so Python computes `-(3 ** 2)` and binds `-9` rather than `(-3) ** 2 == 9`.
- **C:** Correct. Evaluates to the negative integer `-9`. In this case: Exponentiation `**` has higher precedence than unary negation `-` on its left, so Python computes `-(3 ** 2)` and binds `-9` rather than `(-3) ** 2 == 9`.
- **D:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Exponentiation `**` has higher precedence than unary negation `-` on its left, so Python computes `-(3 ** 2)` and binds `-9` rather than `(-3) ** 2 == 9`.

### Question 8 — A

Answer: `^`. Bitwise exclusive-OR `^` sets each output bit to `1` when the two operand bits differ (`0b110 ^ 0b011 == 0b101 == 5`), whereas `**` is exponentiation. Bitwise XOR sets each bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Local study-map skill 1.8 (Bitwise, Relational, Boolean Operators, and Short-Circuiting), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Bitwise XOR sets each bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). In this case: Bitwise exclusive-OR `^` sets each output bit to `1` when the two operand bits differ (`0b110 ^ 0b011 == 0b101 == 5`), whereas `**` is exponentiation.
- **B:** Incorrect for this question. Bitwise OR sets each bit to `1` where at least one integer operand has `1`. Why the correct answer wins: Bitwise exclusive-OR `^` sets each output bit to `1` when the two operand bits differ (`0b110 ^ 0b011 == 0b101 == 5`), whereas `**` is exponentiation.
- **C:** Incorrect for this question. Bitwise AND sets each bit to `1` only where both integer operands have `1`. Why the correct answer wins: Bitwise exclusive-OR `^` sets each output bit to `1` when the two operand bits differ (`0b110 ^ 0b011 == 0b101 == 5`), whereas `**` is exponentiation.
- **D:** Incorrect for this question. Exponentiation has higher precedence than unary minus on its left and binds right-to-left (`2 ** 3 ** 2 == 512`). Why the correct answer wins: Bitwise exclusive-OR `^` sets each output bit to `1` when the two operand bits differ (`0b110 ^ 0b011 == 0b101 == 5`), whereas `**` is exponentiation.

### Question 9 — A

Answer: `'ababab'`. Multiplying a `str` by positive integer `3` concatenates three copies in sequence, producing `'ababab'`. Repeating `'ab' * 3` produces the six-character string `'ababab'`. Local study-map skill 1.9 (Floating-Point Accuracy, String Operators, and Shortcut Assignments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Repeating `'ab' * 3` produces the six-character string `'ababab'`. In this case: Multiplying a `str` by positive integer `3` concatenates three copies in sequence, producing `'ababab'`.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Multiplying a `str` by positive integer `3` concatenates three copies in sequence, producing `'ababab'`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Multiplying a `str` by positive integer `3` concatenates three copies in sequence, producing `'ababab'`.
- **D:** Incorrect for this question. Evaluates to an empty `str` of length `0`, which is falsy in Boolean contexts. Why the correct answer wins: Multiplying a `str` by positive integer `3` concatenates three copies in sequence, producing `'ababab'`.

### Question 10 — A

Answer: `end=' '`. `end=' '` replaces `print()`'s default trailing newline `\n` with a single space, keeping the next `print()` output on the same line. The `end` keyword argument replaces the default trailing newline `\n` emitted after `print()`. Local study-map skill 1.10 (Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. The `end` keyword argument replaces the default trailing newline `\n` emitted after `print()`. In this case: `end=' '` replaces `print()`'s default trailing newline `\n` with a single space, keeping the next `print()` output on the same line.
- **B:** Incorrect for this question. The `sep` keyword argument sets the string placed between positional arguments passed to `print()`. Why the correct answer wins: `end=' '` replaces `print()`'s default trailing newline `\n` with a single space, keeping the next `print()` output on the same line.
- **C:** Incorrect for this question. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). Why the correct answer wins: `end=' '` replaces `print()`'s default trailing newline `\n` with a single space, keeping the next `print()` output on the same line.
- **D:** Incorrect for this question. Passing an empty separator concatenates `print()` arguments with no intervening space. Why the correct answer wins: `end=' '` replaces `print()`'s default trailing newline `\n` with a single space, keeping the next `print()` output on the same line.

### Question 11 — A

Answer: `True`. `bool()` on any non-empty `str` returns `True` regardless of the characters inside; only the empty string `''` converts to `False`. Evaluates to Boolean `True`. Local study-map skill 1.11 (Console Input with input() and Type Casting (int, float, str, bool)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Evaluates to Boolean `True`. In this case: `bool()` on any non-empty `str` returns `True` regardless of the characters inside; only the empty string `''` converts to `False`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: `bool()` on any non-empty `str` returns `True` regardless of the characters inside; only the empty string `''` converts to `False`.
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: `bool()` on any non-empty `str` returns `True` regardless of the characters inside; only the empty string `''` converts to `False`.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: `bool()` on any non-empty `str` returns `True` regardless of the characters inside; only the empty string `''` converts to `False`.

### Question 12 — D

Answer: `B`. `35 >= 50` is `False` and `35 >= 30` is `True`, so `tag` becomes `'B'` and later branches are skipped. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: `35 >= 50` is `False` and `35 >= 30` is `True`, so `tag` becomes `'B'` and later branches are skipped.
- **B:** Incorrect for this question. Prints `D` via the final `else` fallback when every preceding condition is `False`. Why the correct answer wins: `35 >= 50` is `False` and `35 >= 30` is `True`, so `tag` becomes `'B'` and later branches are skipped.
- **C:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: `35 >= 50` is `False` and `35 >= 30` is `True`, so `tag` becomes `'B'` and later branches are skipped.
- **D:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: `35 >= 50` is `False` and `35 >= 30` is `True`, so `tag` becomes `'B'` and later branches are skipped.

### Question 13 — C

Answer: `==`. `==` tests value equality in expressions, whereas a single `=` is assignment (illegal as a bare `if` condition) and `is` checks object identity rather than string value equality. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `!=` evaluates to `True` when two operands do not compare equal. Why the correct answer wins: `==` tests value equality in expressions, whereas a single `=` is assignment (illegal as a bare `if` condition) and `is` checks object identity rather than string value equality.
- **B:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `==` tests value equality in expressions, whereas a single `=` is assignment (illegal as a bare `if` condition) and `is` checks object identity rather than string value equality.
- **C:** Correct. `==` tests value equality rather than assignment (`=`) or object identity (`is`). In this case: `==` tests value equality in expressions, whereas a single `=` is assignment (illegal as a bare `if` condition) and `is` checks object identity rather than string value equality.
- **D:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `==` tests value equality in expressions, whereas a single `=` is assignment (illegal as a bare `if` condition) and `is` checks object identity rather than string value equality.

### Question 14 — D

Answer: `B`. `' '` has length `3` so outer `if msg:` is `True`, but `msg.strip()` returns `''` which is falsy, choosing `'B'`. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: `'   '` has length `3` so outer `if msg:` is `True`, but `msg.strip()` returns `''` which is falsy, choosing `'B'`.
- **B:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: `'   '` has length `3` so outer `if msg:` is `True`, but `msg.strip()` returns `''` which is falsy, choosing `'B'`.
- **C:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: `'   '` has length `3` so outer `if msg:` is `True`, but `msg.strip()` returns `''` which is falsy, choosing `'B'`.
- **D:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: `'   '` has length `3` so outer `if msg:` is `True`, but `msg.strip()` returns `''` which is falsy, choosing `'B'`.

### Question 15 — B, C

Answers: `'0'`; `[0]`. Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy. A non-empty string `'0'` has length `1` and therefore evaluates to `True` in Boolean contexts. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to an empty `str` of length `0`, which is falsy in Boolean contexts. Why the correct answer wins: Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy.
- **B:** Correct. A non-empty string `'0'` has length `1` and therefore evaluates to `True` in Boolean contexts. In this case: Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy.
- **C:** Correct. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. In this case: Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy.
- **E:** Incorrect for this question. An empty `{}` literal creates an empty `dict` (not a `set`). Why the correct answer wins: Non-empty `'0'` and one-element `[0]` both have length `1` and evaluate to `True`, whereas `''`, `{}`, and `None` are falsy.

### Question 16 — B, D

Answers: `not (a or b)`; `(not a) and (not b)`. By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`. By De Morgan law, `not (a or b)` is True exactly when both `a` and `b` are falsy. Requiring both `not a` and `not b` is logically equivalent to `not (a or b)`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Because `not` binds tighter than `or`, `not a or b` parses as `(not a) or b`. Why the correct answer wins: By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`.
- **B:** Correct. By De Morgan law, `not (a or b)` is True exactly when both `a` and `b` are falsy. In this case: By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`.
- **C:** Incorrect for this question. Bitwise inversion computes `-(x + 1)` in two-complement integer arithmetic. Why the correct answer wins: By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`.
- **D:** Correct. Requiring both `not a` and `not b` is logically equivalent to `not (a or b)`. In this case: By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`.
- **E:** Incorrect for this question. `(not a) or (not b)` is equivalent to `not (a and b)`, which still allows one operand to be truthy. Why the correct answer wins: By De Morgan's law, `not (a or b)` and `(not a) and (not b)` are both true only when `a` and `b` are both falsy; `(not a) or (not b)` allows one flag to be truthy, and `not a or b` parses as `(not a) or b`.

### Question 17 — D

Answer: `'ERR'`. Logical `or` returns its left operand `'ERR'` immediately whenever it is truthy, short-circuiting before `1 // 0` is ever evaluated. Evaluates to the non-empty string `'ERR'`; `or` returns its first truthy operand directly rather than converting it to `True`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised by `/`, `//`, or `%` when the right operand is `0` or `0.0`. Why the correct answer wins: Logical `or` returns its left operand `'ERR'` immediately whenever it is truthy, short-circuiting before `1 // 0` is ever evaluated.
- **B:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Logical `or` returns its left operand `'ERR'` immediately whenever it is truthy, short-circuiting before `1 // 0` is ever evaluated.
- **C:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Logical `or` returns its left operand `'ERR'` immediately whenever it is truthy, short-circuiting before `1 // 0` is ever evaluated.
- **D:** Correct. Evaluates to the non-empty string `'ERR'`; `or` returns its first truthy operand directly rather than converting it to `True`. In this case: Logical `or` returns its left operand `'ERR'` immediately whenever it is truthy, short-circuiting before `1 // 0` is ever evaluated.

### Question 18 — C

Answer: `2`. Iteration 1 slices `'abcd'` to `'cd'` (`steps = 1`); iteration 2 slices `'cd'` to `''` (`steps = 2`), making `while s:` falsy and stopping. Evaluates to the integer `2`. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Iteration 1 slices `'abcd'` to `'cd'` (`steps = 1`); iteration 2 slices `'cd'` to `''` (`steps = 2`), making `while s:` falsy and stopping.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Iteration 1 slices `'abcd'` to `'cd'` (`steps = 1`); iteration 2 slices `'cd'` to `''` (`steps = 2`), making `while s:` falsy and stopping.
- **C:** Correct. Evaluates to the integer `2`. In this case: Iteration 1 slices `'abcd'` to `'cd'` (`steps = 1`); iteration 2 slices `'cd'` to `''` (`steps = 2`), making `while s:` falsy and stopping.
- **D:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Iteration 1 slices `'abcd'` to `'cd'` (`steps = 1`); iteration 2 slices `'cd'` to `''` (`steps = 2`), making `while s:` falsy and stopping.

### Question 19 — D

Answer: `-=`. `-=` subtracts `2` from `remaining` on each cycle (`6 -> 4 -> 2 -> 0`), whereas `+=` grows infinitely and `=` assigns `2` forever. Augmented subtraction subtracts the right-hand expression from the target variable. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `-=` subtracts `2` from `remaining` on each cycle (`6 -> 4 -> 2 -> 0`), whereas `+=` grows infinitely and `=` assigns `2` forever.
- **B:** Incorrect for this question. `!=` evaluates to `True` when two operands do not compare equal. Why the correct answer wins: `-=` subtracts `2` from `remaining` on each cycle (`6 -> 4 -> 2 -> 0`), whereas `+=` grows infinitely and `=` assigns `2` forever.
- **C:** Incorrect for this question. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). Why the correct answer wins: `-=` subtracts `2` from `remaining` on each cycle (`6 -> 4 -> 2 -> 0`), whereas `+=` grows infinitely and `=` assigns `2` forever.
- **D:** Correct. Augmented subtraction subtracts the right-hand expression from the target variable. In this case: `-=` subtracts `2` from `remaining` on each cycle (`6 -> 4 -> 2 -> 0`), whereas `+=` grows infinitely and `=` assigns `2` forever.

### Question 20 — A, C

Answers: `range(1, 6)`; `range(5)`. `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. `range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded). Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded). In this case: `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **B:** Incorrect for this question. `range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three). Why the correct answer wins: `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **C:** Correct. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. In this case: `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **D:** Incorrect for this question. `range(2, 9, 2)` yields `2, 4, 6, 8`, stopping before `9`. Why the correct answer wins: `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **E:** Incorrect for this question. With default step `+1` and `start >= stop`, `range(5, 1)` produces zero iterations. Why the correct answer wins: `range(1, 6)` yields `1, 2, 3, 4, 5` and `range(5)` yields `0, 1, 2, 3, 4` (five values each), whereas `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.

### Question 21 — C

Answer: Nothing is printed (zero iterations). With default step `+1` and `start` (`5`) already greater than `stop` (`1`), `range(5, 1)` is empty and the loop body executes zero times. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: With default step `+1` and `start` (`5`) already greater than `stop` (`1`), `range(5, 1)` is empty and the loop body executes zero times.
- **B:** Incorrect for this question. Prints `0 1 2` across iterations. Why the correct answer wins: With default step `+1` and `start` (`5`) already greater than `stop` (`1`), `range(5, 1)` is empty and the loop body executes zero times.
- **C:** Correct. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. In this case: With default step `+1` and `start` (`5`) already greater than `stop` (`1`), `range(5, 1)` is empty and the loop body executes zero times.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: With default step `+1` and `start` (`5`) already greater than `stop` (`1`), `range(5, 1)` is empty and the loop body executes zero times.

### Question 22 — D

Answer: `in`. In a `for target in iterable:` header, `in` binds the loop variable to each item produced by the sequence. `in` tests element or substring membership and also binds loop targets in `for` headers. Local study-map skill 2.6 (Iterating Directly Over Sequences and Enumerated Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: In a `for target in iterable:` header, `in` binds the loop variable to each item produced by the sequence.
- **B:** Incorrect for this question. `from` is a reserved keyword used in `from module import name` and `raise ... from ...`. Why the correct answer wins: In a `for target in iterable:` header, `in` binds the loop variable to each item produced by the sequence.
- **C:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: In a `for target in iterable:` header, `in` binds the loop variable to each item produced by the sequence.
- **D:** Correct. `in` tests element or substring membership and also binds loop targets in `for` headers. In this case: In a `for target in iterable:` header, `in` binds the loop variable to each item produced by the sequence.

### Question 23 — B

Answer: `break`. `break` terminates the `for` loop immediately upon encountering `'STOP'`, whereas `continue` would skip `'STOP'` and still count the final `'ok'` (`seen == 3`). `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Why the correct answer wins: `break` terminates the `for` loop immediately upon encountering `'STOP'`, whereas `continue` would skip `'STOP'` and still count the final `'ok'` (`seen == 3`).
- **B:** Correct. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. In this case: `break` terminates the `for` loop immediately upon encountering `'STOP'`, whereas `continue` would skip `'STOP'` and still count the final `'ok'` (`seen == 3`).
- **C:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `break` terminates the `for` loop immediately upon encountering `'STOP'`, whereas `continue` would skip `'STOP'` and still count the final `'ok'` (`seen == 3`).
- **D:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `break` terminates the `for` loop immediately upon encountering `'STOP'`, whereas `continue` would skip `'STOP'` and still count the final `'ok'` (`seen == 3`).

### Question 24 — A

Answer: `3`. `continue` skips incrementing `seen` only on `'STOP'` and continues with the remaining two `'ok'` entries, producing `seen == 3`. Evaluates to the integer `3`. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: `continue` skips incrementing `seen` only on `'STOP'` and continues with the remaining two `'ok'` entries, producing `seen == 3`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: `continue` skips incrementing `seen` only on `'STOP'` and continues with the remaining two `'ok'` entries, producing `seen == 3`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `continue` skips incrementing `seen` only on `'STOP'` and continues with the remaining two `'ok'` entries, producing `seen == 3`.
- **D:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `continue` skips incrementing `seen` only on `'STOP'` and continues with the remaining two `'ok'` entries, producing `seen == 3`.

### Question 25 — A, E

Answers: When `break` terminates the loop early before the condition turns `False`; When `return` exits the enclosing function from inside the loop body. Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`. `break` bypasses the loop `else` suite completely. Returning out of the function exits both the loop and any attached `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Returning out of the function exits both the loop and any attached `else` suite. In this case: Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`.
- **B:** Incorrect for this question. Normal exhaustion of a `for` iterable runs the attached `else` suite. Why the correct answer wins: Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`.
- **C:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`.
- **D:** Incorrect for this question. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. Why the correct answer wins: Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`.
- **E:** Correct. `break` bypasses the loop `else` suite completely. In this case: Executing `break` or exiting the enclosing function with `return` skips the loop `else:` suite, whereas normal exhaustion or a `False` loop condition executes `else:`.

### Question 26 — C

Answer: `else`. Attaching `else:` at the same indentation level as `for` runs its suite only if the loop completes without `break`. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `elif` is a reserved Python keyword that introduces an additional conditional branch. Why the correct answer wins: Attaching `else:` at the same indentation level as `for` runs its suite only if the loop completes without `break`.
- **B:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: Attaching `else:` at the same indentation level as `for` runs its suite only if the loop completes without `break`.
- **C:** Correct. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. In this case: Attaching `else:` at the same indentation level as `for` runs its suite only if the loop completes without `break`.
- **D:** Incorrect for this question. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Why the correct answer wins: Attaching `else:` at the same indentation level as `for` runs its suite only if the loop completes without `break`.

### Question 27 — D

Answer: `4`. Pair `('a', '1')` matches `c == '1'` and all three `'b'` pairs `('b', '1')`, `('b', '2')`, `('b', '3')` match `r == 'b'`, totaling `4` hits out of `6`. Evaluates to the integer `4`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Pair `('a', '1')` matches `c == '1'` and all three `'b'` pairs `('b', '1')`, `('b', '2')`, `('b', '3')` match `r == 'b'`, totaling `4` hits out of `6`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Pair `('a', '1')` matches `c == '1'` and all three `'b'` pairs `('b', '1')`, `('b', '2')`, `('b', '3')` match `r == 'b'`, totaling `4` hits out of `6`.
- **C:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Pair `('a', '1')` matches `c == '1'` and all three `'b'` pairs `('b', '1')`, `('b', '2')`, `('b', '3')` match `r == 'b'`, totaling `4` hits out of `6`.
- **D:** Correct. Evaluates to the integer `4`. In this case: Pair `('a', '1')` matches `c == '1'` and all three `'b'` pairs `('b', '1')`, `('b', '2')`, `('b', '3')` match `r == 'b'`, totaling `4` hits out of `6`.

### Question 28 — D

Answer: `6`. The outer loop runs `2` times and for each outer pass the inner loop runs `3` times, executing `total += 1` a total of `2 * 3 = 6` times. Evaluates to the integer `6`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: The outer loop runs `2` times and for each outer pass the inner loop runs `3` times, executing `total += 1` a total of `2 * 3 = 6` times.
- **B:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: The outer loop runs `2` times and for each outer pass the inner loop runs `3` times, executing `total += 1` a total of `2 * 3 = 6` times.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: The outer loop runs `2` times and for each outer pass the inner loop runs `3` times, executing `total += 1` a total of `2 * 3 = 6` times.
- **D:** Correct. Evaluates to the integer `6`. In this case: The outer loop runs `2` times and for each outer pass the inner loop runs `3` times, executing `total += 1` a total of `2 * 3 = 6` times.

### Question 29 — C

Answer: `[20, 30, 40]`. Negative index `-4` refers to `20` (index `1`) and exclusive stop `-1` refers to `50` (index `4`), slicing out `[20, 30, 40]`. Produces the three-element slice `[20, 30, 40]`. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Negative index `-4` refers to `20` (index `1`) and exclusive stop `-1` refers to `50` (index `4`), slicing out `[20, 30, 40]`.
- **B:** Incorrect for this question. Slicing `items[1:3]` starts at index `1` and stops before index `3`. Why the correct answer wins: Negative index `-4` refers to `20` (index `1`) and exclusive stop `-1` refers to `50` (index `4`), slicing out `[20, 30, 40]`.
- **C:** Correct. Produces the three-element slice `[20, 30, 40]`. In this case: Negative index `-4` refers to `20` (index `1`) and exclusive stop `-1` refers to `50` (index `4`), slicing out `[20, 30, 40]`.
- **D:** Incorrect for this question. Negative-step slicing steps backward from the higher index toward the lower exclusive stop. Why the correct answer wins: Negative index `-4` refers to `20` (index `1`) and exclusive stop `-1` refers to `50` (index `4`), slicing out `[20, 30, 40]`.

### Question 30 — D

Answer: `[40, 30, 20]`. Starting at index `3` (`40`) and stepping by `-1` down toward exclusive index `0` (`10`) collects indices `3, 2, 1`, returning `[40, 30, 20]`. Negative-step slicing steps backward from the higher index toward the lower exclusive stop. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Produces the three-element slice `[20, 30, 40]`. Why the correct answer wins: Starting at index `3` (`40`) and stepping by `-1` down toward exclusive index `0` (`10`) collects indices `3, 2, 1`, returning `[40, 30, 20]`.
- **B:** Incorrect for this question. Slicing with `[::-1]` or calling `.reverse()` reverses the element order. Why the correct answer wins: Starting at index `3` (`40`) and stepping by `-1` down toward exclusive index `0` (`10`) collects indices `3, 2, 1`, returning `[40, 30, 20]`.
- **C:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Starting at index `3` (`40`) and stepping by `-1` down toward exclusive index `0` (`10`) collects indices `3, 2, 1`, returning `[40, 30, 20]`.
- **D:** Correct. Negative-step slicing steps backward from the higher index toward the lower exclusive stop. In this case: Starting at index `3` (`40`) and stepping by `-1` down toward exclusive index `0` (`10`) collects indices `3, 2, 1`, returning `[40, 30, 20]`.

### Question 31 — A, D

Answers: `items.append(x)` mutates `items` in place and evaluates to `None`; `items.pop()` removes the final element in place and returns that removed element. `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`. In-place list mutators (`append`, `extend`, `insert`, `remove`, `sort`, `reverse`) return `None` except `pop()`. `pop()` both mutates the list and returns the removed value so callers can inspect it. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. In-place list mutators (`append`, `extend`, `insert`, `remove`, `sort`, `reverse`) return `None` except `pop()`. In this case: `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`.
- **B:** Incorrect for this question. `insert(0, x)` places `x` at the *front* (index `0`), shifting existing elements right. Why the correct answer wins: `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`.
- **C:** Incorrect for this question. `sorted()` is a built-in function that returns a *new* sorted list without modifying `items`. Why the correct answer wins: `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`.
- **D:** Correct. `pop()` both mutates the list and returns the removed value so callers can inspect it. In this case: `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`.
- **E:** Incorrect for this question. `list.remove(x)` deletes only the *first* matching occurrence of `x`. Why the correct answer wins: `items.append(x)` mutates in place and returns `None`, and `items.pop()` removes and returns the last item; `sorted()` creates a new list, `remove()` deletes only the first match, and `insert(0, x)` prepends at index `0`.

### Question 32 — B

Answer: `[1, 2, [3, 4]]`. `append()` always adds its argument as a single element rather than unpacking it, producing the three-element list `[1, 2, [3, 4]]`. `append([3, 4])` inserts the inner list as one nested element rather than flattening its items. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: `append()` always adds its argument as a single element rather than unpacking it, producing the three-element list `[1, 2, [3, 4]]`.
- **B:** Correct. `append([3, 4])` inserts the inner list as one nested element rather than flattening its items. In this case: `append()` always adds its argument as a single element rather than unpacking it, producing the three-element list `[1, 2, [3, 4]]`.
- **C:** Incorrect for this question. `extend([3, 4])` or `+=` iterates the argument and appends each item individually. Why the correct answer wins: `append()` always adds its argument as a single element rather than unpacking it, producing the three-element list `[1, 2, [3, 4]]`.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `append()` always adds its argument as a single element rather than unpacking it, producing the three-element list `[1, 2, [3, 4]]`.

### Question 33 — C

Answer: `sorted()`. `sorted(raw_lines)` returns a newly allocated sorted `list` without mutating `raw_lines`, whereas `raw_lines.sort()` mutates in place and returns `None`. `sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`. Local study-map skill 3.3 (Deleting Elements or Slices with del, len(), and sorted()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: `sorted(raw_lines)` returns a newly allocated sorted `list` without mutating `raw_lines`, whereas `raw_lines.sort()` mutates in place and returns `None`.
- **B:** Incorrect for this question. `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. Why the correct answer wins: `sorted(raw_lines)` returns a newly allocated sorted `list` without mutating `raw_lines`, whereas `raw_lines.sort()` mutates in place and returns `None`.
- **C:** Correct. `sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`. In this case: `sorted(raw_lines)` returns a newly allocated sorted `list` without mutating `raw_lines`, whereas `raw_lines.sort()` mutates in place and returns `None`.
- **D:** Incorrect for this question. `len(obj)` returns the item or character count of a sequence or collection. Why the correct answer wins: `sorted(raw_lines)` returns a newly allocated sorted `list` without mutating `raw_lines`, whereas `raw_lines.sort()` mutates in place and returns `None`.

### Question 34 — A, C

Answers: `b = a[:]`; `b = list(a)`. Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`. Full-slice notation `a[:]` creates a new shallow copy of list `a`. Passing `a` to `list(a)` constructs a distinct outer list with the same element references. Local study-map skill 3.4 (List Aliasing vs Shallow Slicing/Copying and Nested Matrices), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Full-slice notation `a[:]` creates a new shallow copy of list `a`. In this case: Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **B:** Incorrect for this question. Multiplying `[[1, 2]] * 2` duplicates references to the same inner list rather than cloning inner rows. Why the correct answer wins: Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **C:** Correct. Passing `a` to `list(a)` constructs a distinct outer list with the same element references. In this case: Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **D:** Incorrect for this question. `a.sort()` sorts `a` in place and assigns `None` to `b`. Why the correct answer wins: Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`.
- **E:** Incorrect for this question. Plain assignment `b = a` creates an alias to the exact same list object rather than copying. Why the correct answer wins: Both `b = a[:]` and `b = list(a)` allocate a new outer list object, whereas `b = a` aliases the same list and `a.sort()` returns `None`.

### Question 35 — B

Answer: `[3, 4, 2]`. The comprehension applies `len()` to each string in order (`'err' -> 3`, `'warn' -> 4`, `'ok' -> 2`), producing `[3, 4, 2]`. Maps `len()` across three short strings in a list comprehension. Local study-map skill 3.5 (List Comprehensions with Filtering and Expressions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: The comprehension applies `len()` to each string in order (`'err' -> 3`, `'warn' -> 4`, `'ok' -> 2`), producing `[3, 4, 2]`.
- **B:** Correct. Maps `len()` across three short strings in a list comprehension. In this case: The comprehension applies `len()` to each string in order (`'err' -> 3`, `'warn' -> 4`, `'ok' -> 2`), producing `[3, 4, 2]`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: The comprehension applies `len()` to each string in order (`'err' -> 3`, `'warn' -> 4`, `'ok' -> 2`), producing `[3, 4, 2]`.
- **D:** Incorrect for this question. Produces the three-element list `[1, 2, 3]`. Why the correct answer wins: The comprehension applies `len()` to each string in order (`'err' -> 3`, `'warn' -> 4`, `'ok' -> 2`), producing `[3, 4, 2]`.

### Question 36 — B

Answer: `True`. For two `str` operands, `in` performs contiguous substring matching; `'err'` occurs inside `'kernel_error_42'`, returning `True`. Evaluates to Boolean `True`. Local study-map skill 3.6 (Membership Testing with in and not in Across Collections), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: For two `str` operands, `in` performs contiguous substring matching; `'err'` occurs inside `'kernel_error_42'`, returning `True`.
- **B:** Correct. Evaluates to Boolean `True`. In this case: For two `str` operands, `in` performs contiguous substring matching; `'err'` occurs inside `'kernel_error_42'`, returning `True`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: For two `str` operands, `in` performs contiguous substring matching; `'err'` occurs inside `'kernel_error_42'`, returning `True`.
- **D:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: For two `str` operands, `in` performs contiguous substring matching; `'err'` occurs inside `'kernel_error_42'`, returning `True`.

### Question 37 — A, E

Answers: Assigning `t[0] = 9` on a tuple raises `TypeError` because tuple slot bindings are immutable; Slicing a tuple such as `t[1:3]` returns a new `tuple` containing those elements. Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`. Tuples do not support item assignment or item deletion. Slicing a tuple produces another tuple rather than converting it to a list. Local study-map skill 3.7 (Tuple Construction, Single-Element Syntax, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Tuples do not support item assignment or item deletion. In this case: Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`.
- **B:** Incorrect for this question. `del t[0]` raises `TypeError` because tuples are immutable; only `del t` (unbinding the whole variable) is legal. Why the correct answer wins: Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`.
- **C:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`.
- **D:** Incorrect for this question. Parentheses without a comma group an arithmetic expression rather than building a tuple. Why the correct answer wins: Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`.
- **E:** Correct. Slicing a tuple produces another tuple rather than converting it to a list. In this case: Assigning to `t[0]` raises `TypeError` and slicing `t[1:3]` returns a new `tuple`; tuples have no `.append()`, `del t[0]` raises `TypeError`, and `(7)` without a comma is an `int`.

### Question 38 — A

Answer: `20 10`. Python evaluates the right-hand tuple `(b, a)` (`(20, 10)`) completely before unpacking into `a` and `b`, printing `20 10`. Tuple assignment `a, b = b, a` evaluates the right-hand side first and swaps bindings cleanly. Local study-map skill 3.8 (Mutable Lists Inside Tuples vs Tuples Inside Lists), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Tuple assignment `a, b = b, a` evaluates the right-hand side first and swaps bindings cleanly. In this case: Python evaluates the right-hand tuple `(b, a)` (`(20, 10)`) completely before unpacking into `a` and `b`, printing `20 10`.
- **B:** Incorrect for this question. Default `sep` in `print()` is a single space and default `end` is `\n`. Why the correct answer wins: Python evaluates the right-hand tuple `(b, a)` (`(20, 10)`) completely before unpacking into `a` and `b`, printing `20 10`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Python evaluates the right-hand tuple `(b, a)` (`(20, 10)`) completely before unpacking into `a` and `b`, printing `20 10`.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Python evaluates the right-hand tuple `(b, a)` (`(20, 10)`) completely before unpacking into `a` and `b`, printing `20 10`.

### Question 39 — C

Answer: `get()`. `dict.get(key, default)` returns `default` (`0`) when `key` is absent while leaving the dictionary unchanged. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. Local study-map skill 3.9 (Dictionary Creation, Key Lookup, Insertion, Update, and Deletion), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `dict.keys()` returns a dynamic view of the dictionary keys. Why the correct answer wins: `dict.get(key, default)` returns `default` (`0`) when `key` is absent while leaving the dictionary unchanged.
- **B:** Incorrect for this question. `dict.pop(key)` removes `key` and returns its associated value. Why the correct answer wins: `dict.get(key, default)` returns `default` (`0`) when `key` is absent while leaving the dictionary unchanged.
- **C:** Correct. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. In this case: `dict.get(key, default)` returns `default` (`0`) when `key` is absent while leaving the dictionary unchanged.
- **D:** Incorrect for this question. `dict.values()` returns a dynamic view of the dictionary values. Why the correct answer wins: `dict.get(key, default)` returns `default` (`0`) when `key` is absent while leaving the dictionary unchanged.

### Question 40 — C, E

Answers: Iterating `for x in d:` yields each dictionary key in insertion order; Iterating `for k, v in d.items():` unpacks each `(key, value)` pair cleanly. `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs. Iterating directly over a `dict` iterates over its keys, identical to `for x in d.keys():`. `d.items()` yields 2-tuples pairing each key with its mapped value. Local study-map skill 3.10 (Dictionary Iteration with keys(), values(), items(), and get()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `d.values()` yields only the mapped values, not `(key, value)` pairs. Why the correct answer wins: `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs.
- **B:** Incorrect for this question. Iterating bare `d` yields keys alone, so `for k, v in d:` fails unless the keys themselves happen to be 2-element iterables. Why the correct answer wins: `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs.
- **C:** Correct. Iterating directly over a `dict` iterates over its keys, identical to `for x in d.keys():`. In this case: `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs.
- **E:** Correct. `d.items()` yields 2-tuples pairing each key with its mapped value. In this case: `for x in d:` iterates keys in insertion order and `for k, v in d.items():` unpacks `(key, value)` pairs; bare `d` and `d.values()` do not yield `(key, value)` pairs.

### Question 41 — A

Answer: `6`. `\'` is one apostrophe character and `\t` is one tab character, so `'i'`, `'t'`, `"'"`, `'s'`, `'\t'`, `'1'` total `6` characters. Evaluates to the integer `6`. Local study-map skill 3.11 (String Literals, Escape Sequences, Quotes, and Multiline Strings), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `6`. In this case: `\'` is one apostrophe character and `\t` is one tab character, so `'i'`, `'t'`, `"'"`, `'s'`, `'\t'`, `'1'` total `6` characters.
- **B:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: `\'` is one apostrophe character and `\t` is one tab character, so `'i'`, `'t'`, `"'"`, `'s'`, `'\t'`, `'1'` total `6` characters.
- **C:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: `\'` is one apostrophe character and `\t` is one tab character, so `'i'`, `'t'`, `"'"`, `'s'`, `'\t'`, `'1'` total `6` characters.
- **D:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: `\'` is one apostrophe character and `\t` is one tab character, so `'i'`, `'t'`, `"'"`, `'s'`, `'\t'`, `'1'` total `6` characters.

### Question 42 — C

Answer: `2` (non-overlapping occurrences counted by `str.count()`). `str.count()` counts *non-overlapping* matches from left to right (`'aa'` at `0:2` and `'aa'` at `2:4`), returning `2` rather than `3`. `str.count(sub)` counts *non-overlapping* occurrences, so `"aaaa".count("aa")` is `2`, not `3`. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `str.count()` counts *non-overlapping* matches from left to right (`'aa'` at `0:2` and `'aa'` at `2:4`), returning `2` rather than `3`.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `str.count()` counts *non-overlapping* matches from left to right (`'aa'` at `0:2` and `'aa'` at `2:4`), returning `2` rather than `3`.
- **C:** Correct. `str.count(sub)` counts *non-overlapping* occurrences, so `"aaaa".count("aa")` is `2`, not `3`. In this case: `str.count()` counts *non-overlapping* matches from left to right (`'aa'` at `0:2` and `'aa'` at `2:4`), returning `2` rather than `3`.
- **D:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: `str.count()` counts *non-overlapping* matches from left to right (`'aa'` at `0:2` and `'aa'` at `2:4`), returning `2` rather than `3`.

### Question 43 — D

Answer: `startswith()`. `str.startswith('ERROR:')` returns `True` when `line` starts with that exact prefix and never raises `IndexError` on short strings. `str.startswith(prefix)` checks whether a string begins with `prefix` without manual slicing. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `str.endswith(suffix)` checks whether a string ends with `suffix`. Why the correct answer wins: `str.startswith('ERROR:')` returns `True` when `line` starts with that exact prefix and never raises `IndexError` on short strings.
- **B:** Incorrect for this question. `str.isdigit()` returns `True` when the string is non-empty and every character is a digit. Why the correct answer wins: `str.startswith('ERROR:')` returns `True` when `line` starts with that exact prefix and never raises `IndexError` on short strings.
- **C:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: `str.startswith('ERROR:')` returns `True` when `line` starts with that exact prefix and never raises `IndexError` on short strings.
- **D:** Correct. `str.startswith(prefix)` checks whether a string begins with `prefix` without manual slicing. In this case: `str.startswith('ERROR:')` returns `True` when `line` starts with that exact prefix and never raises `IndexError` on short strings.

### Question 44 — B

Answer: Writing `return a, b` returns a single `tuple` `(a, b)` that the caller can unpack. Comma-separated expressions after `return` pack a single `tuple` `(ok_count, err_count)` that the caller can keep or unpack into two variables. Comma-separated expressions after `return` pack a `tuple` object. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Comma-separated expressions after `return` pack a single `tuple` `(ok_count, err_count)` that the caller can keep or unpack into two variables.
- **B:** Correct. Comma-separated expressions after `return` pack a `tuple` object. In this case: Comma-separated expressions after `return` pack a single `tuple` `(ok_count, err_count)` that the caller can keep or unpack into two variables.
- **C:** Incorrect for this question. The first `return` executed exits the function immediately; subsequent statements in that block are unreachable. Why the correct answer wins: Comma-separated expressions after `return` pack a single `tuple` `(ok_count, err_count)` that the caller can keep or unpack into two variables.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Comma-separated expressions after `return` pack a single `tuple` `(ok_count, err_count)` that the caller can keep or unpack into two variables.

### Question 45 — A

Answer: `return`. `return ln` terminates `first_error` right away and hands `ln` back to the caller, whereas `yield` would turn the function into a generator. `return` exits the current function immediately and sends a value back to the caller. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `return` exits the current function immediately and sends a value back to the caller. In this case: `return ln` terminates `first_error` right away and hands `ln` back to the caller, whereas `yield` would turn the function into a generator.
- **B:** Incorrect for this question. `yield` is a reserved Python keyword that turns a function into a generator. Why the correct answer wins: `return ln` terminates `first_error` right away and hands `ln` back to the caller, whereas `yield` would turn the function into a generator.
- **C:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `return ln` terminates `first_error` right away and hands `ln` back to the caller, whereas `yield` would turn the function into a generator.
- **D:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `return ln` terminates `first_error` right away and hands `ln` back to the caller, whereas `yield` would turn the function into a generator.

### Question 46 — C

Answer: `[]` (a generator iterator can only be consumed once; a second `list(g)` is empty). A generator iterator `g` is single-pass; once `first = list(g)` exhausts it, iterating `g` a second time yields zero elements and `list(g)` returns `[]`. Once a generator reaches exhaustion, subsequent iterations over the same generator object yield zero items. Local study-map skill 4.2 (Generator Functions Using yield and Lazy Iteration), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: A generator iterator `g` is single-pass; once `first = list(g)` exhausts it, iterating `g` a second time yields zero elements and `list(g)` returns `[]`.
- **B:** Incorrect for this question. `StopIteration` is raised by `next()` when a generator or iterator is exhausted. Why the correct answer wins: A generator iterator `g` is single-pass; once `first = list(g)` exhausts it, iterating `g` a second time yields zero elements and `list(g)` returns `[]`.
- **C:** Correct. Once a generator reaches exhaustion, subsequent iterations over the same generator object yield zero items. In this case: A generator iterator `g` is single-pass; once `first = list(g)` exhausts it, iterating `g` a second time yields zero elements and `list(g)` returns `[]`.
- **D:** Incorrect for this question. Consuming the generator with `list(...)` collects every yielded value until exhaustion. Why the correct answer wins: A generator iterator `g` is single-pass; once `first = list(g)` exhausts it, iterating `g` a second time yields zero elements and `list(g)` returns `[]`.

### Question 47 — B

Answer: `16`. The calls add `4 + (5 + (7 + 0))` until `ns` becomes `[]` at the base case, returning `16`. Evaluates to the integer `16`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Why the correct answer wins: The calls add `4 + (5 + (7 + 0))` until `ns` becomes `[]` at the base case, returning `16`.
- **B:** Correct. Evaluates to the integer `16`. In this case: The calls add `4 + (5 + (7 + 0))` until `ns` becomes `[]` at the base case, returning `16`.
- **C:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: The calls add `4 + (5 + (7 + 0))` until `ns` becomes `[]` at the base case, returning `16`.
- **D:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: The calls add `4 + (5 + (7 + 0))` until `ns` becomes `[]` at the base case, returning `16`.

### Question 48 — A

Answer: `0`. Returning `0` (the additive identity) on the empty-list base case terminates recursion cleanly so `4 + 5 + 0 == 9`. Evaluates to the integer zero. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer zero. In this case: Returning `0` (the additive identity) on the empty-list base case terminates recursion cleanly so `4 + 5 + 0 == 9`.
- **B:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Returning `0` (the additive identity) on the empty-list base case terminates recursion cleanly so `4 + 5 + 0 == 9`.
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Returning `0` (the additive identity) on the empty-list base case terminates recursion cleanly so `4 + 5 + 0 == 9`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Returning `0` (the additive identity) on the empty-list base case terminates recursion cleanly so `4 + 5 + 0 == 9`.

### Question 49 — B

Answer: Positional arguments must appear before any keyword arguments in a function call. In every Python function call, positional arguments (`'a,b,c'`) must appear before keyword arguments (`sep=','`). Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Comma-separated expressions after `return` pack a `tuple` object. Why the correct answer wins: In every Python function call, positional arguments (`'a,b,c'`) must appear before keyword arguments (`sep=','`).
- **B:** Correct. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. In this case: In every Python function call, positional arguments (`'a,b,c'`) must appear before keyword arguments (`sep=','`).
- **C:** Incorrect for this question. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. Why the correct answer wins: In every Python function call, positional arguments (`'a,b,c'`) must appear before keyword arguments (`sep=','`).
- **D:** Incorrect for this question. Without `global x`, an assignment `x = ...` inside a function shadows the outer `x` and leaves the module-level variable unchanged. Why the correct answer wins: In every Python function call, positional arguments (`'a,b,c'`) must appear before keyword arguments (`sep=','`).

### Question 50 — A

Answer: Raises `TypeError`. Positional `'boot'` already binds parameter `msg`, so also passing `msg='ready'` raises `TypeError` for multiple values of `msg`. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. In this case: Positional `'boot'` already binds parameter `msg`, so also passing `msg='ready'` raises `TypeError` for multiple values of `msg`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Positional `'boot'` already binds parameter `msg`, so also passing `msg='ready'` raises `TypeError` for multiple values of `msg`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Positional `'boot'` already binds parameter `msg`, so also passing `msg='ready'` raises `TypeError` for multiple values of `msg`.
- **D:** Incorrect for this question. `NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Positional `'boot'` already binds parameter `msg`, so also passing `msg='ready'` raises `TypeError` for multiple values of `msg`.

### Question 51 — A, B

Answers: `def connect(host, port=5432):`; `def connect(host="localhost", port=5432):`. `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`. Required parameter `host` precedes defaulted parameter `port=5432`, which is valid Python syntax. Every parameter may carry a default value when no non-default parameter follows. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Required parameter `host` precedes defaulted parameter `port=5432`, which is valid Python syntax. In this case: `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`.
- **B:** Correct. Every parameter may carry a default value when no non-default parameter follows. In this case: `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`.
- **C:** Incorrect for this question. Placing required parameter `port` after defaulted `host="localhost"` raises `SyntaxError`. Why the correct answer wins: `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`.
- **D:** Incorrect for this question. Function parameters in `def` must be identifiers, never string literals. Why the correct answer wins: `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`.
- **E:** Incorrect for this question. Duplicate parameter names in a `def` signature raise `SyntaxError`. Why the correct answer wins: `def connect(host, port=5432):` puts the required parameter first and `def connect(host="localhost", port=5432):` defaults both; defaulted-before-required, duplicate parameter names, and literal parameters all raise `SyntaxError`.

### Question 52 — A

Answer: `15`. Omitting `factor` uses its default value `3`, computing `5 * 3 == 15`. Evaluates to the integer `15`. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `15`. In this case: Omitting `factor` uses its default value `3`, computing `5 * 3 == 15`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Omitting `factor` uses its default value `3`, computing `5 * 3 == 15`.
- **C:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Omitting `factor` uses its default value `3`, computing `5 * 3 == 15`.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Omitting `factor` uses its default value `3`, computing `5 * 3 == 15`.

### Question 53 — C

Answer: Raises `UnboundLocalError`. Because `count = 6` appears inside `step()`, Python compiles `count` as a local variable across all of `step()`, so `print(count)` reads an unassigned local and raises `UnboundLocalError`. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Because `count = 6` appears inside `step()`, Python compiles `count` as a local variable across all of `step()`, so `print(count)` reads an unassigned local and raises `UnboundLocalError`.
- **B:** Incorrect for this question. `NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Because `count = 6` appears inside `step()`, Python compiles `count` as a local variable across all of `step()`, so `print(count)` reads an unassigned local and raises `UnboundLocalError`.
- **C:** Correct. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. In this case: Because `count = 6` appears inside `step()`, Python compiles `count` as a local variable across all of `step()`, so `print(count)` reads an unassigned local and raises `UnboundLocalError`.
- **D:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Because `count = 6` appears inside `step()`, Python compiles `count` as a local variable across all of `step()`, so `print(count)` reads an unassigned local and raises `UnboundLocalError`.

### Question 54 — A, C

Answers: Assigning to a variable inside a function creates a new local name unless `global` is declared; Raises `UnboundLocalError` because assigning to the name later in the function marks it local throughout the body. Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`. Without `global x`, an assignment `x = ...` inside a function shadows the outer `x` and leaves the module-level variable unchanged. Reading a variable before assigning to it in the same function (without `global`) raises `UnboundLocalError`, a subclass of `NameError`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Without `global x`, an assignment `x = ...` inside a function shadows the outer `x` and leaves the module-level variable unchanged. In this case: Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`.
- **B:** Incorrect for this question. The first `return` executed exits the function immediately; subsequent statements in that block are unreachable. Why the correct answer wins: Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`.
- **C:** Correct. Reading a variable before assigning to it in the same function (without `global`) raises `UnboundLocalError`, a subclass of `NameError`. In this case: Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`.
- **D:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`.
- **E:** Incorrect for this question. In `{"a": 1, "a": 2}`, the final binding wins so `len` is `1` and `d["a"]` is `2`. Why the correct answer wins: Assigning to a name binds a new local variable (shadowing any outer name), and reading that same name earlier in the function raises `UnboundLocalError`.

### Question 55 — D

Answer: `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`. `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception`.
- **B:** Incorrect for this question. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception`.
- **C:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception`.
- **D:** Correct. In this case: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception`.

### Question 56 — B, E

Answers: `IndexError` is a direct subclass of `LookupError`; `KeyError` is a direct subclass of `LookupError`. Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`. `LookupError` groups `IndexError` and `KeyError` under `Exception`. Catching `LookupError` handles `KeyError` as well as `IndexError`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` sits under `Exception` rather than under `LookupError` or `SyntaxError`. Why the correct answer wins: Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`.
- **B:** Correct. Catching `LookupError` handles `KeyError` as well as `IndexError`. In this case: Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`.
- **C:** Incorrect for this question. Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`. Why the correct answer wins: Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`.
- **D:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`.
- **E:** Correct. `LookupError` groups `IndexError` and `KeyError` under `Exception`. In this case: Both `IndexError` and `KeyError` are direct subclasses of `LookupError`, whereas `ValueError` and `TypeError` inherit directly from `Exception` and `SystemExit` inherits from `BaseException`.

### Question 57 — B

Answer: Raises `KeyError`. Subscripting a dictionary with a key that does not exist (`'WARN'`) raises `KeyError` (use `.get()` when a fallback default is desired). `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Subscripting a dictionary with a key that does not exist (`'WARN'`) raises `KeyError` (use `.get()` when a fallback default is desired).
- **B:** Correct. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. In this case: Subscripting a dictionary with a key that does not exist (`'WARN'`) raises `KeyError` (use `.get()` when a fallback default is desired).
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Subscripting a dictionary with a key that does not exist (`'WARN'`) raises `KeyError` (use `.get()` when a fallback default is desired).
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Subscripting a dictionary with a key that does not exist (`'WARN'`) raises `KeyError` (use `.get()` when a fallback default is desired).

### Question 58 — A

Answer: `raise`. `raise` instantiates or throws the specified exception object up the call stack. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. In this case: `raise` instantiates or throws the specified exception object up the call stack.
- **B:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `raise` instantiates or throws the specified exception object up the call stack.
- **C:** Incorrect for this question. `assert` is a reserved Python keyword used for debugging checks. Why the correct answer wins: `raise` instantiates or throws the specified exception object up the call stack.
- **D:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: `raise` instantiates or throws the specified exception object up the call stack.

### Question 59 — B, E

Answers: Place `except ZeroDivisionError:` above `except ArithmeticError:` so division by zero reaches the specific handler; Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch. Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax. Because `ZeroDivisionError` is a subclass of `ArithmeticError`, putting `ZeroDivisionError` first lets both handlers stay reachable. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. A bare `except:` must always be the *last* `except` clause in Python 3; placing it earlier is a `SyntaxError`. Why the correct answer wins: Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax.
- **B:** Correct. Because `ZeroDivisionError` is a subclass of `ArithmeticError`, putting `ZeroDivisionError` first lets both handlers stay reachable. In this case: Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax.
- **C:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax.
- **D:** Incorrect for this question. At most *one* `except` branch executes for a single raised exception. Why the correct answer wins: Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax.
- **E:** Correct. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. In this case: Putting `ZeroDivisionError` before `ArithmeticError` and `KeyError` before `LookupError` lets subclass errors hit the narrow handler while sibling errors reach the parent; leading `Exception:` or non-final bare `except:` breaks reachability or syntax.

### Question 60 — B

Answer: `finally`. `finally` executes its cleanup suite unconditionally on normal exit, `return`, or exception propagation. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Why the correct answer wins: `finally` executes its cleanup suite unconditionally on normal exit, `return`, or exception propagation.
- **B:** Correct. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. In this case: `finally` executes its cleanup suite unconditionally on normal exit, `return`, or exception propagation.
- **C:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: `finally` executes its cleanup suite unconditionally on normal exit, `return`, or exception propagation.
- **D:** Incorrect for this question. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Why the correct answer wins: `finally` executes its cleanup suite unconditionally on normal exit, `return`, or exception propagation.
