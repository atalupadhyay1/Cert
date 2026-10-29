# PCEP – Certified Entry-Level Python Programmer (PCEP-30-02) — Full-Length Mock Exam 5

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 15 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). The live PCEP-30-02 exam has 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item set is an expanded 2x bank timed at 80 minutes to preserve the live pace of about 80 seconds per item. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. Version note: PCEP-30-03 is scheduled for release on October 31, 2026; PCEP-30-02 remains active and earned credentials retain their five-year validity. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. An instructor runs `python3 score_quiz.py` to grade student submissions. Which statement accurately describes how standard CPython executes `score_quiz.py`?

- A. CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime
- B. A static linker merges Python modules into firmware without needing a runtime interpreter
- C. Compiled native binaries require every end user to keep the original C compiler installed to launch the binary
- D. CPython links source directly into a standalone machine-code binary before the user runs the script

### 2. While explaining error messages to a programming class, which two statements accurately contrast lexis, syntax, and semantics? Select two.

- A. Style formatting comments automatically bypass syntax checking during parsing
- B. Compiled native binaries require every end user to keep the original C compiler installed to launch the binary
- C. Semantics determines runtime meaning, so `10 / 0` passes lexis and syntax yet fails at runtime
- D. Lexis checks that each individual token is legal, whereas syntax checks how tokens are arranged into statements
- E. Lexis runs only after the program finishes printing its output

### 3. A student drafts variable names for a quiz-scoring worksheet. Which two names are reserved Python keywords that raise `SyntaxError` if assigned as variable identifiers? Select two.

- A. `total_count_2`
- B. `return`
- C. `global`
- D. `true`
- E. `print`

### 4. A curved-score formula defines `max_points = 3e2` and prints `max_points`. What exact output is printed?

- A. Raises `SyntaxError`
- B. `256`
- C. `300.0`
- D. `30`

### 5. Which two names are syntactically legal variable identifiers for holding a quiz average in Python 3? Select two.

- A. `user-count`
- B. `_temp_value`
- C. `raw score`
- D. `2nd_total`
- E. `item_price_usd`

### 6. Complete `leftover_seats = 17 ____ 5` so dividing `17` students into groups of `5` binds `leftover_seats` to the remainder `2`. Which arithmetic operator fills the blank?

- A. `**`
- B. `%`
- C. `//`
- D. `/`

### 7. A penalty calculation evaluates `deduction = -2 ** 4` without parentheses around `-2`. What integer is bound to `deduction`?

- A. `16`
- B. `-8`
- C. `8`
- D. `-16`

### 8. Complete `bucket = 19 ____ 2` so shifting `19` (`0b10011`) two bit positions to the right floor-divides it by `4` to yield `4`. Which bitwise operator fills the blank?

- A. `^`
- B. `>>`
- C. `<<`
- D. `&`

### 9. Complete `bonus_total = 10` / `bonus_total ____ 5` so the shortcut operator adds `5` and rebinds `bonus_total` to `15`. Which augmented assignment operator fills the blank?

- A. `==`
- B. `+=`
- C. `-=`
- D. `*=`

### 10. A grading script executes `print('OK', end='-')` on one line and `print('DONE')` on the next line. What does the console display?

- A. `a b`
- B. `a-b-c!`
- C. Raises `TypeError`
- D. `OK-DONE`

### 11. Complete `banner = 'Score: ' + ____(95)` so integer `95` is converted to text and concatenated without raising `TypeError`. Which built-in callable fills the blank?

- A. `str()`
- B. `float()`
- C. `len()`
- D. `int()`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass

### 12. A letter-grade rule sets `score = 80` and runs `if score >= 90: g = 'A'` / `elif score >= 80: g = 'B'` / `elif score >= 70: g = 'C'` / `else: g = 'D'`. What value is assigned to `g`?

- A. `C`
- B. `B`
- C. `D`
- D. `A`

### 13. Complete `if absences ____ 2:` so students with `0`, `1`, or `2` absences qualify for attendance credit while `3` does not. Which relational operator fills the blank?

- A. `=`
- B. `>=`
- C. `<=`
- D. `<`

### 14. In a gradebook check `if comment:`, which two values of `comment` evaluate to `False`? Select two.

- A. `''` (the empty string)
- B. `0`
- C. `[0]`
- D. `'0'`
- E. `'False'`

### 15. A roster check sets `roster = []` and runs `if roster:` / `    print('A')` / `else:` / `    print('B')`. What does it print?

- A. `B`
- B. Nothing is printed (zero iterations)
- C. `C`
- D. `A`

### 16. A merit badge requires quiz score `x` to fall inclusively from `10` through `20`. Which two Python conditions test that requirement accurately? Select two.

- A. `(x >= 10) and (x <= 20)`
- B. `10 <= x <= 20`
- C. `(x >= 10) or (x <= 20)`
- D. `10 <= x & x <= 20`
- E. `x >= 10 and x = 20`

### 17. A retake condition evaluates `allow = False and True or True`. What Boolean value does `allow` receive?

- A. Raises `SyntaxError`
- B. `0`
- C. `True`
- D. `False`

### 18. A curve loop sets `pts = 62; boosts = 0` and runs `while pts < 70: pts += 3; boosts += 1`. What is `boosts` after termination?

- A. `3`
- B. `2`
- C. `4`
- D. `9`

### 19. Complete `____ ungraded > 0:` / `    grade_next()` / `    ungraded -= 1` so `grade_next()` repeats until `ungraded` reaches `0`. Which keyword fills the blank?

- A. `elif`
- B. `try`
- C. `for`
- D. `while`

### 20. A 5-question quiz loop needs to execute its body five times. Which two `range()` expressions each produce five iterations? Select two.

- A. `range(0, 3, -1)`
- B. `range(1, 3)`
- C. `range(1, 6, 2)`
- D. `range(1, 6)`
- E. `range(5)`

### 21. A bonus-point progression evaluates `sum(range(1, 11))`. What integer does `sum()` return?

- A. `45`
- B. `50`
- C. `55`
- D. `10`

### 22. A pass counter sets `passed = 0` and runs `for g in [58, 72, 91, 69, 84]:` / `    if g >= 70: passed += 1`. What is `passed` afterward?

- A. `4`
- B. `5`
- C. `3`
- D. `2`

### 23. A sentinel sum sets `acc = 0` and runs `for s in [10, 15, -1, 20]:` / `    if s < 0: break` / `    acc += s`. What is `acc` when the loop ends?

- A. `24`
- B. `10`
- C. `25`
- D. `45`

### 24. Complete `for s in scores:` / `    if s == 100:` / `        ____  # TODO: award honour badge` / `    total += s` so `total += s` still runs even when `s == 100` while keeping the `if` suite syntactically valid. Which keyword fills the blank?

- A. `break`
- B. `return`
- C. `continue`
- D. `pass`

### 25. In a plagiarism-check loop with an attached `else:` clause, which two execution paths run the `else:` suite? Select two.

- A. When `break` terminates the loop early before the condition turns `False`
- B. When a `while` condition initially or eventually evaluates to `False` without `break`
- C. When `return` exits the enclosing function from inside the loop body
- D. When an unhandled exception aborts the loop body
- E. When a `for` loop consumes every item in its iterable without hitting `break`

### 26. A missing-submission check runs `for m in [88, 0, 92]:` / `    if m == 0: print('FOUND'); break` / `else: print('DONE')`. What does it print?

- A. `DONE`
- B. `FOUND`
- C. Raises `SyntaxError`
- D. Nothing is printed (zero iterations)

### 27. A grade grid runs `perfect = 0` / `for row in [[8, 10, 9], [10, 10, 7]]:` / `    for q in row:` / `        if q == 10: perfect += 1`. What is `perfect` afterward?

- A. `3`
- B. `6`
- C. `1`
- D. `2`

### 28. How many cell evaluations occur inside `for student in range(3):` / `    for quiz in range(4): checks += 1`?

- A. `12`
- B. `7`
- C. `24`
- D. `10`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations

### 29. A quiz sheet stores five ascending scores `marks = [65, 70, 75, 80, 85]` and takes the prefix slice `marks[:2]`. Which two-item list is returned?

- A. `[]`
- B. Raises `IndexError`
- C. `[65, 70]`
- D. `[75, 80, 85]`

### 30. From a student's sorted results `marks = [65, 70, 75, 80, 85]`, extracting the top three entries via negative-start slice `marks[-3:]` produces which list?

- A. `[75, 80, 85]`
- B. `72`
- C. Raises `IndexError`
- D. `[65, 70]`

### 31. A cleanup step sets `scores = [10, 5, 10, 8]`, calls `scores.remove(10)`, and prints `scores`. What is printed?

- A. `[2, 4]`
- B. `None`
- C. Raises `ValueError`
- D. `[5, 10, 8]`

### 32. Complete `pos = roster.____('Lin')` so `pos` receives the zero-based position of `'Lin'` inside list `roster` without modifying `roster`. Which `list` method fills the blank?

- A. `remove()`
- B. `index()`
- C. `pop()`
- D. `sort()`

### 33. A grade list sets `qs = [8, 9, 7, 10, 6]`, executes `del qs[-1]`, and evaluates `len(qs)`. What integer does `len(qs)` return?

- A. `5`
- B. Raises `TypeError`
- C. `4`
- D. `3`

### 34. An instructor holds `a = [80, 85, 90]` and wants a separate copy `b` for curve experiments without altering `a`. Which two statements create that shallow copy? Select two.

- A. `b = a[:]`
- B. `b = a.copy()`
- C. `b = a.sort()`
- D. `[[9, 2], [9, 2]]`
- E. `b = a`

### 35. What does `[ch.upper() for ch in 'a1b2' if ch.isalpha()]` return?

- A. `['A', 'B']`
- B. `[1, 2, 3]`
- C. Raises `AttributeError`
- D. `[]`

### 36. Complete `if student_id ____ enrolled_ids:` so the portal grants quiz access only when `student_id` is a member of `enrolled_ids`. Which operator fills the blank?

- A. `==`
- B. `not in`
- C. `is`
- D. `in`

### 37. Which two statements about building or slicing tuples in Python 3 are accurate? Select two.

- A. Slicing a tuple such as `t[1:3]` returns a new `tuple` containing those elements
- B. `(7)`
- C. `t = tuple(5)`
- D. `t = tuple([5])`
- E. Calling `t.append(9)` adds an element to the end of tuple `t` in place

### 38. A gradebook stores tuples inside a list: `roster = [('Ada', 99), ('Lin', 88)]`. What does `roster[1][1]` evaluate to?

- A. Raises `IndexError`
- B. Raises `TypeError`
- C. `88`
- D. `99`

### 39. A quiz dictionary sets `grades = {'q1': 8, 'q2': 9}`, executes `grades['q1'] = 10` and `grades['q3'] = 7`, and checks `len(grades)`. What integer is returned?

- A. `3`
- B. `4`
- C. `2`
- D. Raises `KeyError`

### 40. Complete `for name, mark in gradebook.____():` so each loop pass unpacks both the student key and the numeric score from dictionary `gradebook`. Which `dict` method fills the blank?

- A. `items()`
- B. `keys()`
- C. `get()`
- D. `values()`

### 41. A rubric label needs to store `Item's price` with an apostrophe. Which two string literals parse cleanly in Python 3? Select two.

- A. `"Item price'`
- B. `'C:\temp\'`
- C. `"Item's price"`
- D. `'Item's price'`
- E. `'Item\'s price'`

### 42. Which two statements hold true when formatting student name strings in Python 3? Select two.

- A. Assigning `s[0] = "X"` mutates the first character of `s` in place
- B. Running `del s[0]` deletes the first character from `s` in place
- C. Running `del t[0]` removes the first element while keeping the same tuple object
- D. Every string transformation method returns a brand-new `str` object and leaves the original string unchanged
- E. Out-of-range string slice bounds such as `s[2:99]` clamp silently instead of raising `IndexError`

### 43. Complete `if surname.____():` so a roster importer verifies that non-empty string `surname` contains only alphabetic letters. Which `str` method fills the blank?

- A. `sort()`
- B. `isalpha()`
- C. `endswith()`
- D. `isdigit()`

---

## Block 4 — Functions and Exceptions (28%) — User-defined functions, generators, recursion, argument passing, scope/global, and exception handling

### 44. Which two statements accurately describe Python functions and generator functions? Select two.

- A. Function parameter names are automatically registered in module-level global scope when the function returns
- B. Multiple `return` lines in the same branch all execute sequentially and concatenate their results
- C. `sorted(items)` mutates `items` in place and returns `None`
- D. Adding `yield` anywhere in a function body makes calling it return a generator object instead of running the body immediately
- E. A function that reaches the end of its body without any `return` statement returns `None`

### 45. Complete `____ curve_score(raw):` / `    return min(100, raw + 5)` to define function `curve_score`. Which keyword fills the blank?

- A. `yield`
- B. `return`
- C. `def`
- D. `import`

### 46. A script defines `def one_mark(): yield 95`, binds `it = one_mark()`, calls `next(it)` once (getting `95`), and immediately calls `next(it)` a second time. Which exception does the second `next(it)` raise?

- A. Raises `StopIteration`
- B. `0`
- C. `None`
- D. Raises `IndexError`

### 47. A checksum helper defines `def digit_sum(n): return n if n < 10 else (n % 10) + digit_sum(n // 10)` and evaluates `digit_sum(308)`. What integer does it return?

- A. `24`
- B. Raises `RecursionError`
- C. `30`
- D. `11`

### 48. A student forgets the base case in `def bad_fact(n): return n * bad_fact(n - 1)` and calls `bad_fact(4)`. Which runtime exception occurs?

- A. `0`
- B. Raises `RecursionError`
- C. Raises `TypeError`
- D. `None`

### 49. A student writes `grade_exam(curve=5, 82)` and hits `SyntaxError` before execution starts. Which call-site rule was broken?

- A. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- B. Positional arguments must appear before any keyword arguments in a function call
- C. Duplicate keys overwrite earlier entries, keeping the last value assigned to that key
- D. Parameters with default values must follow parameters without default values in `def`

### 50. Given `def weighted(quiz, exam): return quiz + 2 * exam`, what does `weighted(exam=7, quiz=4)` return?

- A. Raises `TypeError`
- B. `18`
- C. Raises `SyntaxError`
- D. `12`

### 51. Which two function headers place default parameter values legally in Python 3? Select two.

- A. `def connect("localhost", port=80):`
- B. `def connect(host="localhost", port):`
- C. `def connect(host="localhost", port=5432):`
- D. `def connect(host, host=80):`
- E. `def connect(host, port=5432):`

### 52. A student writes `def add_mark(m, bag=[]): bag.append(m); return list(bag)` and runs `print(add_mark(1), add_mark(2))`. What is printed?

- A. `[1] [2]`
- B. `None`
- C. Raises `TypeError`
- D. `[1] [1, 2]` (default list is evaluated once at `def` time and shared across calls)

### 53. A grading module sets `pass_cutoff = 60`, defines `def preview_strict(): pass_cutoff = 100`, calls `preview_strict()`, and prints module-level `pass_cutoff`. What integer is printed?

- A. Raises `UnboundLocalError`
- B. `60`
- C. Raises `NameError`
- D. `100`

### 54. Complete `graded_papers = 0` / `def record_paper():` / `    ____ graded_papers` / `    graded_papers += 1` so `record_paper()` increments module-level `graded_papers`. Which keyword fills the blank?

- A. `class`
- B. `yield`
- C. `global`
- D. `nonlocal`

### 55. Which two built-in exceptions sit directly beneath `BaseException` rather than `Exception` in Python 3? Select two.

- A. `IndexError` is a direct subclass of `LookupError`
- B. `KeyboardInterrupt` inherits directly from `BaseException`, not from `Exception`
- C. `TypeError` inherits directly from `Exception`
- D. `SystemExit` inherits directly from `BaseException`, not from `Exception`
- E. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)

### 56. When averaging scores over an empty section triggers `ZeroDivisionError`, which abstract parent class between `Exception` and `ZeroDivisionError` also matches that error?

- A. `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`
- B. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)
- C. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- D. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`

### 57. An importer runs `int('absent')` when a quiz cell contains the word `'absent'`. Which exception does `int()` raise?

- A. `0`
- B. Raises `TypeError`
- C. Raises `KeyError`
- D. Raises `ValueError`

### 58. Complete `try:` / `    avg = total / count` / `____ ZeroDivisionError:` / `    avg = 0.0` so empty sections set `avg = 0.0` cleanly. Which keyword fills the blank?

- A. `try`
- B. `finally`
- C. `raise`
- D. `except`

### 59. When handling missing student IDs and bad row indices on a `try` block, which two guidelines keep every `except` handler reachable? Select two.

- A. Place a bare `except:` clause above `except TypeError:` as a fallback default
- B. Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch
- C. Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`
- D. Python runs every `except` clause whose class matches the raised exception from top to bottom
- E. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler

### 60. Complete `try:` / `    save_gradebook(sheet)` / `____:` / `    release_lock()` so `release_lock()` runs unconditionally whether `save_gradebook` finishes normally or raises an error. Which keyword fills the blank?

- A. `finally`
- B. `except`
- C. `else`
- D. `return`

---

## Answer key and explanations

### Question 1 — A

Answer: CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime. CPython compiles `.py` source to bytecode and runs it inside the Python virtual machine at runtime rather than ahead-of-time linking a native OS binary. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. Local study-map skill 1.1 (Compilation vs Interpretation and Execution Model), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable. In this case: CPython compiles `.py` source to bytecode and runs it inside the Python virtual machine at runtime rather than ahead-of-time linking a native OS binary.
- **B:** Incorrect for this question. Standard Python scripts still require a Python runtime rather than a static hardware linker. Why the correct answer wins: CPython compiles `.py` source to bytecode and runs it inside the Python virtual machine at runtime rather than ahead-of-time linking a native OS binary.
- **C:** Incorrect for this question. A compiled standalone executable runs directly on the target OS without shipping the compiler. Why the correct answer wins: CPython compiles `.py` source to bytecode and runs it inside the Python virtual machine at runtime rather than ahead-of-time linking a native OS binary.
- **D:** Incorrect for this question. Ahead-of-time native machine-code compilation is what a C or Rust compiler performs, not standard CPython. Why the correct answer wins: CPython compiles `.py` source to bytecode and runs it inside the Python virtual machine at runtime rather than ahead-of-time linking a native OS binary.

### Question 2 — C, D

Answers: Lexis checks that each individual token is legal, whereas syntax checks how tokens are arranged into statements; Semantics determines runtime meaning, so `10 / 0` passes lexis and syntax yet fails at runtime. Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution. Lexical analysis validates vocabulary tokens; syntactic analysis validates statement grammar. A statement can be lexically and syntactically valid while still failing semantically during execution. Local study-map skill 1.2 (Lexis, Syntax, and Semantics Distinctions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution.
- **B:** Incorrect for this question. A compiled standalone executable runs directly on the target OS without shipping the compiler. Why the correct answer wins: Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution.
- **C:** Correct. A statement can be lexically and syntactically valid while still failing semantically during execution. In this case: Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution.
- **D:** Correct. Lexical analysis validates vocabulary tokens; syntactic analysis validates statement grammar. In this case: Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution.
- **E:** Incorrect for this question. Tokenization happens before bytecode compilation and execution. Why the correct answer wins: Lexis validates individual tokens, syntax validates statement grammar, and semantics governs runtime meaning so division by zero passes parsing yet fails during execution.

### Question 3 — B, C

Answers: `global`; `return`. `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier. `global` is a reserved Python keyword that binds a name inside a function to module scope. `return` exits the current function immediately and sends a value back to the caller. Local study-map skill 1.3 (Keywords, Instructions, Indentation, and Comments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Identifiers may contain letters, digits, and underscores provided they do not start with a digit or match a keyword. Why the correct answer wins: `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier.
- **B:** Correct. `return` exits the current function immediately and sends a value back to the caller. In this case: `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier.
- **C:** Correct. `global` is a reserved Python keyword that binds a name inside a function to module scope. In this case: `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier.
- **D:** Incorrect for this question. Keywords are case-sensitive: `True` is reserved, whereas lowercase `true` is an ordinary identifier. Why the correct answer wins: `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier.
- **E:** Incorrect for this question. `print` is a built-in function name rather than a hard keyword, though shadowing it is poor practice. Why the correct answer wins: `global` and `return` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `total_count_2` is a legal identifier.

### Question 4 — C

Answer: `300.0`. Scientific notation `3e2` means `3 * 10**2` and *always* produces a `float` in Python 3, printing `300.0`. Scientific notation such as `3e2` always creates a `float` (`300.0`), never an `int`. Local study-map skill 1.4 (Literals, Numeral Systems, and Scientific Notation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Scientific notation `3e2` means `3 * 10**2` and *always* produces a `float` in Python 3, printing `300.0`.
- **B:** Incorrect for this question. Evaluates to the integer `256`. Why the correct answer wins: Scientific notation `3e2` means `3 * 10**2` and *always* produces a `float` in Python 3, printing `300.0`.
- **C:** Correct. Scientific notation such as `3e2` always creates a `float` (`300.0`), never an `int`. In this case: Scientific notation `3e2` means `3 * 10**2` and *always* produces a `float` in Python 3, printing `300.0`.
- **D:** Incorrect for this question. Evaluates to the integer `30`. Why the correct answer wins: Scientific notation `3e2` means `3 * 10**2` and *always* produces a `float` in Python 3, printing `300.0`.

### Question 5 — B, E

Answers: `_temp_value`; `item_price_usd`. `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. Lowercase words separated by underscores (`snake_case`) follow PEP-8 variable naming recommendations. Local study-map skill 1.5 (Variable Naming Rules and PEP-8 Conventions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. A hyphen is parsed as the subtraction operator rather than part of an identifier. Why the correct answer wins: `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal.
- **B:** Correct. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. In this case: `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal.
- **C:** Incorrect for this question. Whitespace separates tokens and is illegal inside a Python variable name. Why the correct answer wins: `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal.
- **D:** Incorrect for this question. An identifier cannot begin with a decimal digit, so `2nd_total` fails lexical analysis with `SyntaxError`. Why the correct answer wins: `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal.
- **E:** Correct. Lowercase words separated by underscores (`snake_case`) follow PEP-8 variable naming recommendations. In this case: `_temp_value` and `item_price_usd` begin with an underscore or letter and use only letters, digits, and underscores; leading digits, hyphens, and spaces are illegal.

### Question 6 — B

Answer: `%`. Modulo `%` returns the remainder `17 - (17 // 5) * 5 == 2`, whereas `//` returns the group count `3`. Modulo returns the remainder `a - (a // b) * b`, taking the sign of the divisor `b` in Python. Local study-map skill 1.6 (Arithmetic Operators, Floor Division, Modulo, and Exponentiation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Exponentiation has higher precedence than unary minus on its left and binds right-to-left (`2 ** 3 ** 2 == 512`). Why the correct answer wins: Modulo `%` returns the remainder `17 - (17 // 5) * 5 == 2`, whereas `//` returns the group count `3`.
- **B:** Correct. Modulo returns the remainder `a - (a // b) * b`, taking the sign of the divisor `b` in Python. In this case: Modulo `%` returns the remainder `17 - (17 // 5) * 5 == 2`, whereas `//` returns the group count `3`.
- **C:** Incorrect for this question. Floor division rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: Modulo `%` returns the remainder `17 - (17 // 5) * 5 == 2`, whereas `//` returns the group count `3`.
- **D:** Incorrect for this question. True division always returns a `float`, even when the numerator is an exact multiple of the denominator. Why the correct answer wins: Modulo `%` returns the remainder `17 - (17 // 5) * 5 == 2`, whereas `//` returns the group count `3`.

### Question 7 — D

Answer: `-16`. Because `**` binds tighter than unary `-` on its left, Python computes `-(2 ** 4)` and assigns `-16` rather than `(-2) ** 4 == 16`. Evaluates to the negative integer `-16`. Local study-map skill 1.7 (Operator Precedence, Unary Signs, and Right-Sided Binding), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Because `**` binds tighter than unary `-` on its left, Python computes `-(2 ** 4)` and assigns `-16` rather than `(-2) ** 4 == 16`.
- **B:** Incorrect for this question. Evaluates to the negative integer `-8`. Why the correct answer wins: Because `**` binds tighter than unary `-` on its left, Python computes `-(2 ** 4)` and assigns `-16` rather than `(-2) ** 4 == 16`.
- **C:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: Because `**` binds tighter than unary `-` on its left, Python computes `-(2 ** 4)` and assigns `-16` rather than `(-2) ** 4 == 16`.
- **D:** Correct. Evaluates to the negative integer `-16`. In this case: Because `**` binds tighter than unary `-` on its left, Python computes `-(2 ** 4)` and assigns `-16` rather than `(-2) ** 4 == 16`.

### Question 8 — B

Answer: `>>`. Right bit-shift `>>` shifts bits right by `2` positions, computing `19 // (2 ** 2) == 4`. Right bit-shift floor-divides an integer by `2 ** n`. Local study-map skill 1.8 (Bitwise, Relational, Boolean Operators, and Short-Circuiting), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Bitwise XOR sets each bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Why the correct answer wins: Right bit-shift `>>` shifts bits right by `2` positions, computing `19 // (2 ** 2) == 4`.
- **B:** Correct. Right bit-shift floor-divides an integer by `2 ** n`. In this case: Right bit-shift `>>` shifts bits right by `2` positions, computing `19 // (2 ** 2) == 4`.
- **C:** Incorrect for this question. Left bit-shift multiplies a non-negative integer by `2 ** n`. Why the correct answer wins: Right bit-shift `>>` shifts bits right by `2` positions, computing `19 // (2 ** 2) == 4`.
- **D:** Incorrect for this question. Bitwise AND sets each bit to `1` only where both integer operands have `1`. Why the correct answer wins: Right bit-shift `>>` shifts bits right by `2` positions, computing `19 // (2 ** 2) == 4`.

### Question 9 — B

Answer: `+=`. `+=` adds the right-hand operand and updates `bonus_total` to `15`. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). Local study-map skill 1.9 (Floating-Point Accuracy, String Operators, and Shortcut Assignments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `+=` adds the right-hand operand and updates `bonus_total` to `15`.
- **B:** Correct. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). In this case: `+=` adds the right-hand operand and updates `bonus_total` to `15`.
- **C:** Incorrect for this question. Augmented subtraction subtracts the right-hand expression from the target variable. Why the correct answer wins: `+=` adds the right-hand operand and updates `bonus_total` to `15`.
- **D:** Incorrect for this question. Augmented multiplication scales a number or repeats a sequence/string. Why the correct answer wins: `+=` adds the right-hand operand and updates `bonus_total` to `15`.

### Question 10 — D

Answer: `OK-DONE`. `end='-'` replaces the first `print()`'s trailing newline with `'-'`, so the second `print()` continues on the same line to output `OK-DONE`. Setting `end="-"` on the first `print()` keeps the second `print()` output on the same line right after `-`. Local study-map skill 1.10 (Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Default `sep` in `print()` is a single space and default `end` is `\n`. Why the correct answer wins: `end='-'` replaces the first `print()`'s trailing newline with `'-'`, so the second `print()` continues on the same line to output `OK-DONE`.
- **B:** Incorrect for this question. Joining three arguments with `-` and ending with `!` prints `a-b-c!`. Why the correct answer wins: `end='-'` replaces the first `print()`'s trailing newline with `'-'`, so the second `print()` continues on the same line to output `OK-DONE`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `end='-'` replaces the first `print()`'s trailing newline with `'-'`, so the second `print()` continues on the same line to output `OK-DONE`.
- **D:** Correct. Setting `end="-"` on the first `print()` keeps the second `print()` output on the same line right after `-`. In this case: `end='-'` replaces the first `print()`'s trailing newline with `'-'`, so the second `print()` continues on the same line to output `OK-DONE`.

### Question 11 — A

Answer: `str()`. `str(95)` converts the integer to `'95'` so `+` performs string concatenation cleanly. `str()` converts numbers or collections to text so `+` can concatenate them with strings without `TypeError`. Local study-map skill 1.11 (Console Input with input() and Type Casting (int, float, str, bool)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `str()` converts numbers or collections to text so `+` can concatenate them with strings without `TypeError`. In this case: `str(95)` converts the integer to `'95'` so `+` performs string concatenation cleanly.
- **B:** Incorrect for this question. `float()` parses numeric strings (including decimal points or scientific notation) into `float`. Why the correct answer wins: `str(95)` converts the integer to `'95'` so `+` performs string concatenation cleanly.
- **C:** Incorrect for this question. `len(obj)` returns the item or character count of a sequence or collection. Why the correct answer wins: `str(95)` converts the integer to `'95'` so `+` performs string concatenation cleanly.
- **D:** Incorrect for this question. `int()` converts a base-10 integer string or truncates a `float` toward zero (`int(-3.9) == -3`). Why the correct answer wins: `str(95)` converts the integer to `'95'` so `+` performs string concatenation cleanly.

### Question 12 — B

Answer: `B`. `80 >= 90` is `False` and `80 >= 80` is `True`, so `g` receives `'B'` and remaining branches are skipped. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: `80 >= 90` is `False` and `80 >= 80` is `True`, so `g` receives `'B'` and remaining branches are skipped.
- **B:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: `80 >= 90` is `False` and `80 >= 80` is `True`, so `g` receives `'B'` and remaining branches are skipped.
- **C:** Incorrect for this question. Prints `D` via the final `else` fallback when every preceding condition is `False`. Why the correct answer wins: `80 >= 90` is `False` and `80 >= 80` is `True`, so `g` receives `'B'` and remaining branches are skipped.
- **D:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: `80 >= 90` is `False` and `80 >= 80` is `True`, so `g` receives `'B'` and remaining branches are skipped.

### Question 13 — C

Answer: `<=`. `<=` includes boundary `2` as well as smaller integers. Less-than-or-equal relational operator. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `<=` includes boundary `2` as well as smaller integers.
- **B:** Incorrect for this question. Greater-than-or-equal relational operator. Why the correct answer wins: `<=` includes boundary `2` as well as smaller integers.
- **C:** Correct. Less-than-or-equal relational operator. In this case: `<=` includes boundary `2` as well as smaller integers.
- **D:** Incorrect for this question. Strictly-less-than relational operator. Why the correct answer wins: `<=` includes boundary `2` as well as smaller integers.

### Question 14 — A, B

Answers: `''` (the empty string); `0`. Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values. Evaluates to an empty `str` of length `0`, which is falsy in Boolean contexts. Evaluates to the integer zero. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to an empty `str` of length `0`, which is falsy in Boolean contexts. In this case: Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values.
- **B:** Correct. Evaluates to the integer zero. In this case: Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values.
- **C:** Incorrect for this question. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. Why the correct answer wins: Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values.
- **D:** Incorrect for this question. A non-empty string `'0'` has length `1` and therefore evaluates to `True` in Boolean contexts. Why the correct answer wins: Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values.
- **E:** Incorrect for this question. Any non-empty string, including `'False'`, is truthy in Python; only `''` is a falsy string. Why the correct answer wins: Empty string `''` and integer `0` are falsy, whereas `'0'`, `'False'`, and `[0]` are non-empty truthy values.

### Question 15 — A

Answer: `B`. An empty list `[]` has length `0` and evaluates to `False`, so execution enters `else:` and prints `B`. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. In this case: An empty list `[]` has length `0` and evaluates to `False`, so execution enters `else:` and prints `B`.
- **B:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: An empty list `[]` has length `0` and evaluates to `False`, so execution enters `else:` and prints `B`.
- **C:** Incorrect for this question. Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause. Why the correct answer wins: An empty list `[]` has length `0` and evaluates to `False`, so execution enters `else:` and prints `B`.
- **D:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: An empty list `[]` has length `0` and evaluates to `False`, so execution enters `else:` and prints `B`.

### Question 16 — A, B

Answers: `10 <= x <= 20`; `(x >= 10) and (x <= 20)`. Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. Combining two relational checks with `and` requires both bounds to hold. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Combining two relational checks with `and` requires both bounds to hold. In this case: Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax.
- **B:** Correct. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. In this case: Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax.
- **C:** Incorrect for this question. Using `or` here is `True` for *every* number (for example `x = 99` satisfies `x >= 10`). Why the correct answer wins: Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax.
- **D:** Incorrect for this question. Bitwise `&` binds tighter than `<=`, so `10 <= x & x <= 20` parses as `10 <= (x & x) <= 20` rather than logical `and`. Why the correct answer wins: Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax.
- **E:** Incorrect for this question. Single `=` is assignment rather than comparison and raises `SyntaxError` inside a Boolean expression. Why the correct answer wins: Both `10 <= x <= 20` and `(x >= 10) and (x <= 20)` verify both bounds; `or` is always true, `&` binds tighter than `<=`, and `=` is invalid syntax.

### Question 17 — C

Answer: `True`. `and` binds tighter than `or`, so `(False and True) or True` simplifies to `False or True`, which evaluates to `True`. Evaluates to Boolean `True`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: `and` binds tighter than `or`, so `(False and True) or True` simplifies to `False or True`, which evaluates to `True`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: `and` binds tighter than `or`, so `(False and True) or True` simplifies to `False or True`, which evaluates to `True`.
- **C:** Correct. Evaluates to Boolean `True`. In this case: `and` binds tighter than `or`, so `(False and True) or True` simplifies to `False or True`, which evaluates to `True`.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: `and` binds tighter than `or`, so `(False and True) or True` simplifies to `False or True`, which evaluates to `True`.

### Question 18 — A

Answer: `3`. Adding `3` steps `pts` through `65 -> 68 -> 71` across `3` passes before `71 < 70` becomes `False`. Evaluates to the integer `3`. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: Adding `3` steps `pts` through `65 -> 68 -> 71` across `3` passes before `71 < 70` becomes `False`.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Adding `3` steps `pts` through `65 -> 68 -> 71` across `3` passes before `71 < 70` becomes `False`.
- **C:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Adding `3` steps `pts` through `65 -> 68 -> 71` across `3` passes before `71 < 70` becomes `False`.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: Adding `3` steps `pts` through `65 -> 68 -> 71` across `3` passes before `71 < 70` becomes `False`.

### Question 19 — D

Answer: `while`. `while` repeats its suite while `ungraded > 0` evaluates to truthy. `while` repeats its indented suite as long as its header condition evaluates to truthy. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `elif` is a reserved Python keyword that introduces an additional conditional branch. Why the correct answer wins: `while` repeats its suite while `ungraded > 0` evaluates to truthy.
- **B:** Incorrect for this question. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. Why the correct answer wins: `while` repeats its suite while `ungraded > 0` evaluates to truthy.
- **C:** Incorrect for this question. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. Why the correct answer wins: `while` repeats its suite while `ungraded > 0` evaluates to truthy.
- **D:** Correct. `while` repeats its indented suite as long as its header condition evaluates to truthy. In this case: `while` repeats its suite while `ungraded > 0` evaluates to truthy.

### Question 20 — D, E

Answers: `range(1, 6)`; `range(5)`. `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. `range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded). Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Starting at `0` with stop `3` and step `-1` moves away from `3` and yields zero iterations. Why the correct answer wins: `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three.
- **B:** Incorrect for this question. `range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three). Why the correct answer wins: `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three.
- **C:** Incorrect for this question. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). Why the correct answer wins: `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three.
- **D:** Correct. `range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive. In this case: `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three.
- **E:** Correct. `range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded). In this case: `range(1, 6)` (`1..5`) and `range(5)` (`0..4`) each yield five integers, whereas `range(1, 3)` yields two, `range(0, 3, -1)` yields zero, and `range(1, 6, 2)` yields three.

### Question 21 — C

Answer: `55`. `range(1, 11)` generates integers `1` through `10` inclusive (`11` is excluded), whose sum is `55`. Evaluates to the integer `55`. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `45`. Why the correct answer wins: `range(1, 11)` generates integers `1` through `10` inclusive (`11` is excluded), whose sum is `55`.
- **B:** Incorrect for this question. Evaluates to the integer `50`. Why the correct answer wins: `range(1, 11)` generates integers `1` through `10` inclusive (`11` is excluded), whose sum is `55`.
- **C:** Correct. Evaluates to the integer `55`. In this case: `range(1, 11)` generates integers `1` through `10` inclusive (`11` is excluded), whose sum is `55`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `range(1, 11)` generates integers `1` through `10` inclusive (`11` is excluded), whose sum is `55`.

### Question 22 — C

Answer: `3`. Scores `72`, `91`, and `84` meet `>= 70`, incrementing `passed` to `3`. Evaluates to the integer `3`. Local study-map skill 2.6 (Iterating Directly Over Sequences and Enumerated Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Scores `72`, `91`, and `84` meet `>= 70`, incrementing `passed` to `3`.
- **B:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Scores `72`, `91`, and `84` meet `>= 70`, incrementing `passed` to `3`.
- **C:** Correct. Evaluates to the integer `3`. In this case: Scores `72`, `91`, and `84` meet `>= 70`, incrementing `passed` to `3`.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Scores `72`, `91`, and `84` meet `>= 70`, incrementing `passed` to `3`.

### Question 23 — C

Answer: `25`. `10` and `15` bring `acc` to `25`, and `-1` triggers `break`, stopping before `20` is visited. Evaluates to the integer `25`. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: `10` and `15` bring `acc` to `25`, and `-1` triggers `break`, stopping before `20` is visited.
- **B:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `10` and `15` bring `acc` to `25`, and `-1` triggers `break`, stopping before `20` is visited.
- **C:** Correct. Evaluates to the integer `25`. In this case: `10` and `15` bring `acc` to `25`, and `-1` triggers `break`, stopping before `20` is visited.
- **D:** Incorrect for this question. Evaluates to the integer `45`. Why the correct answer wins: `10` and `15` bring `acc` to `25`, and `-1` triggers `break`, stopping before `20` is visited.

### Question 24 — D

Answer: `pass`. `pass` satisfies the indented-suite grammar without skipping `total += s` (unlike `continue` or `break`). `pass` is a reserved null-operation keyword required where syntax expects an indented suite. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `pass` satisfies the indented-suite grammar without skipping `total += s` (unlike `continue` or `break`).
- **B:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `pass` satisfies the indented-suite grammar without skipping `total += s` (unlike `continue` or `break`).
- **C:** Incorrect for this question. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Why the correct answer wins: `pass` satisfies the indented-suite grammar without skipping `total += s` (unlike `continue` or `break`).
- **D:** Correct. `pass` is a reserved null-operation keyword required where syntax expects an indented suite. In this case: `pass` satisfies the indented-suite grammar without skipping `total += s` (unlike `continue` or `break`).

### Question 25 — B, E

Answers: When a `for` loop consumes every item in its iterable without hitting `break`; When a `while` condition initially or eventually evaluates to `False` without `break`. Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite. Normal exhaustion of a `for` iterable runs the attached `else` suite. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` bypasses the loop `else` suite completely. Why the correct answer wins: Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite.
- **B:** Correct. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. In this case: Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite.
- **C:** Incorrect for this question. Returning out of the function exits both the loop and any attached `else` suite. Why the correct answer wins: Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite.
- **D:** Incorrect for this question. An unhandled exception unwinds the stack rather than running the loop `else` clause. Why the correct answer wins: Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite.
- **E:** Correct. Normal exhaustion of a `for` iterable runs the attached `else` suite. In this case: Both exhausting a `for` iterable without `break` and a `while` condition evaluating to `False` without `break` execute the loop `else:` suite.

### Question 26 — B

Answer: `FOUND`. Encountering `0` prints `FOUND` and executes `break`, bypassing the `else:` clause. Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. Why the correct answer wins: Encountering `0` prints `FOUND` and executes `break`, bypassing the `else:` clause.
- **B:** Correct. Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early. In this case: Encountering `0` prints `FOUND` and executes `break`, bypassing the `else:` clause.
- **C:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Encountering `0` prints `FOUND` and executes `break`, bypassing the `else:` clause.
- **D:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Encountering `0` prints `FOUND` and executes `break`, bypassing the `else:` clause.

### Question 27 — A

Answer: `3`. One `10` in the first row plus two `10`s in the second row increment `perfect` to `3`. Evaluates to the integer `3`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: One `10` in the first row plus two `10`s in the second row increment `perfect` to `3`.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: One `10` in the first row plus two `10`s in the second row increment `perfect` to `3`.
- **C:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: One `10` in the first row plus two `10`s in the second row increment `perfect` to `3`.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: One `10` in the first row plus two `10`s in the second row increment `perfect` to `3`.

### Question 28 — A

Answer: `12`. Three outer iterations multiplied by four inner iterations run `checks += 1` `3 * 4 == 12` times. Evaluates to the integer `12`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `12`. In this case: Three outer iterations multiplied by four inner iterations run `checks += 1` `3 * 4 == 12` times.
- **B:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: Three outer iterations multiplied by four inner iterations run `checks += 1` `3 * 4 == 12` times.
- **C:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: Three outer iterations multiplied by four inner iterations run `checks += 1` `3 * 4 == 12` times.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Three outer iterations multiplied by four inner iterations run `checks += 1` `3 * 4 == 12` times.

### Question 29 — C

Answer: `[65, 70]`. Omitting `start` defaults to `0` and `stop` `2` is exclusive, returning indices `0` and `1`: `[65, 70]`. Slicing `marks[:2]` takes indices `0` and `1`, stopping before exclusive index `2`. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Omitting `start` defaults to `0` and `stop` `2` is exclusive, returning indices `0` and `1`: `[65, 70]`.
- **B:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Omitting `start` defaults to `0` and `stop` `2` is exclusive, returning indices `0` and `1`: `[65, 70]`.
- **C:** Correct. Slicing `marks[:2]` takes indices `0` and `1`, stopping before exclusive index `2`. In this case: Omitting `start` defaults to `0` and `stop` `2` is exclusive, returning indices `0` and `1`: `[65, 70]`.
- **D:** Incorrect for this question. Slicing `marks[-3:]` collects the final three elements through the end of the list. Why the correct answer wins: Omitting `start` defaults to `0` and `stop` `2` is exclusive, returning indices `0` and `1`: `[65, 70]`.

### Question 30 — A

Answer: `[75, 80, 85]`. Starting at `-3` (`75`) and omitting `stop` slices through the end of the list, returning `[75, 80, 85]`. Slicing `marks[-3:]` collects the final three elements through the end of the list. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slicing `marks[-3:]` collects the final three elements through the end of the list. In this case: Starting at `-3` (`75`) and omitting `stop` slices through the end of the list, returning `[75, 80, 85]`.
- **B:** Incorrect for this question. Evaluates to the integer `72`. Why the correct answer wins: Starting at `-3` (`75`) and omitting `stop` slices through the end of the list, returning `[75, 80, 85]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Starting at `-3` (`75`) and omitting `stop` slices through the end of the list, returning `[75, 80, 85]`.
- **D:** Incorrect for this question. Slicing `marks[:2]` takes indices `0` and `1`, stopping before exclusive index `2`. Why the correct answer wins: Starting at `-3` (`75`) and omitting `stop` slices through the end of the list, returning `[75, 80, 85]`.

### Question 31 — D

Answer: `[5, 10, 8]`. `list.remove(10)` deletes only the *first* matching `10` (at index `0`), leaving the second `10` intact in `[5, 10, 8]`. `scores.remove(10)` removes only the *first* matching `10` at index `0`, leaving the later `10` intact. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Produces the filtered two-element list `[2, 4]`. Why the correct answer wins: `list.remove(10)` deletes only the *first* matching `10` (at index `0`), leaving the second `10` intact in `[5, 10, 8]`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: `list.remove(10)` deletes only the *first* matching `10` (at index `0`), leaving the second `10` intact in `[5, 10, 8]`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: `list.remove(10)` deletes only the *first* matching `10` (at index `0`), leaving the second `10` intact in `[5, 10, 8]`.
- **D:** Correct. `scores.remove(10)` removes only the *first* matching `10` at index `0`, leaving the later `10` intact. In this case: `list.remove(10)` deletes only the *first* matching `10` (at index `0`), leaving the second `10` intact in `[5, 10, 8]`.

### Question 32 — B

Answer: `index()`. `list.index(value)` returns the first zero-based index of `'Lin'` (or raises `ValueError` if missing). `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: `list.index(value)` returns the first zero-based index of `'Lin'` (or raises `ValueError` if missing).
- **B:** Correct. `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. In this case: `list.index(value)` returns the first zero-based index of `'Lin'` (or raises `ValueError` if missing).
- **C:** Incorrect for this question. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Why the correct answer wins: `list.index(value)` returns the first zero-based index of `'Lin'` (or raises `ValueError` if missing).
- **D:** Incorrect for this question. `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. Why the correct answer wins: `list.index(value)` returns the first zero-based index of `'Lin'` (or raises `ValueError` if missing).

### Question 33 — C

Answer: `4`. `del qs[-1]` deletes the final element `6` in place, reducing the five-element list to length `4`. Evaluates to the integer `4`. Local study-map skill 3.3 (Deleting Elements or Slices with del, len(), and sorted()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: `del qs[-1]` deletes the final element `6` in place, reducing the five-element list to length `4`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `del qs[-1]` deletes the final element `6` in place, reducing the five-element list to length `4`.
- **C:** Correct. Evaluates to the integer `4`. In this case: `del qs[-1]` deletes the final element `6` in place, reducing the five-element list to length `4`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `del qs[-1]` deletes the final element `6` in place, reducing the five-element list to length `4`.

### Question 34 — A, B

Answers: `b = a[:]`; `b = a.copy()`. `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched. Full-slice notation `a[:]` creates a new shallow copy of list `a`. `list.copy()` allocates a new shallow copy of `a`. Local study-map skill 3.4 (List Aliasing vs Shallow Slicing/Copying and Nested Matrices), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Full-slice notation `a[:]` creates a new shallow copy of list `a`. In this case: `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched.
- **B:** Correct. `list.copy()` allocates a new shallow copy of `a`. In this case: `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched.
- **C:** Incorrect for this question. `a.sort()` sorts `a` in place and assigns `None` to `b`. Why the correct answer wins: `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched.
- **D:** Incorrect for this question. Multiplying `[[1, 2]] * 2` duplicates references to the same inner list rather than cloning inner rows. Why the correct answer wins: `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched.
- **E:** Incorrect for this question. Plain assignment `b = a` creates an alias to the exact same list object rather than copying. Why the correct answer wins: `b = a[:]` and `b = a.copy()` create new outer lists so rebinding an index in `b` leaves `a` untouched.

### Question 35 — A

Answer: `['A', 'B']`. Filtering `'a1b2'` with `.isalpha()` keeps `'a'` and `'b'`, and `.upper()` transforms them to `['A', 'B']`. Transforms filtered characters to uppercase in a list comprehension. Local study-map skill 3.5 (List Comprehensions with Filtering and Expressions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Transforms filtered characters to uppercase in a list comprehension. In this case: Filtering `'a1b2'` with `.isalpha()` keeps `'a'` and `'b'`, and `.upper()` transforms them to `['A', 'B']`.
- **B:** Incorrect for this question. Produces the three-element list `[1, 2, 3]`. Why the correct answer wins: Filtering `'a1b2'` with `.isalpha()` keeps `'a'` and `'b'`, and `.upper()` transforms them to `['A', 'B']`.
- **C:** Incorrect for this question. `AttributeError` is raised when accessing or calling a method that does not exist on that type (such as `tuple.append`). Why the correct answer wins: Filtering `'a1b2'` with `.isalpha()` keeps `'a'` and `'b'`, and `.upper()` transforms them to `['A', 'B']`.
- **D:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Filtering `'a1b2'` with `.isalpha()` keeps `'a'` and `'b'`, and `.upper()` transforms them to `['A', 'B']`.

### Question 36 — D

Answer: `in`. `in` returns `True` when `student_id` matches a member of `enrolled_ids`. `in` tests element or substring membership and also binds loop targets in `for` headers. Local study-map skill 3.6 (Membership Testing with in and not in Across Collections), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `in` returns `True` when `student_id` matches a member of `enrolled_ids`.
- **B:** Incorrect for this question. `not in` evaluates to `True` when the left operand is absent from the right-hand container. Why the correct answer wins: `in` returns `True` when `student_id` matches a member of `enrolled_ids`.
- **C:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `in` returns `True` when `student_id` matches a member of `enrolled_ids`.
- **D:** Correct. `in` tests element or substring membership and also binds loop targets in `for` headers. In this case: `in` returns `True` when `student_id` matches a member of `enrolled_ids`.

### Question 37 — A, D

Answers: Slicing a tuple such as `t[1:3]` returns a new `tuple` containing those elements; `t = tuple([5])`. Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`. Slicing a tuple produces another tuple rather than converting it to a list. `tuple([5])` converts a one-element list into the one-element tuple `(5,)`. Local study-map skill 3.7 (Tuple Construction, Single-Element Syntax, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slicing a tuple produces another tuple rather than converting it to a list. In this case: Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`.
- **B:** Incorrect for this question. Parentheses without a comma group an arithmetic expression rather than building a tuple. Why the correct answer wins: Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`.
- **C:** Incorrect for this question. `tuple()` expects an iterable, so passing an integer `5` raises `TypeError`. Why the correct answer wins: Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`.
- **D:** Correct. `tuple([5])` converts a one-element list into the one-element tuple `(5,)`. In this case: Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`.
- **E:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: Slicing a tuple returns a new `tuple` and `t = tuple([5])` builds `(5,)`, whereas `(7)` is an `int`, `tuple(5)` raises `TypeError`, and tuples have no `.append()`.

### Question 38 — C

Answer: `88`. `roster[1]` selects the second tuple `('Lin', 88)`, and `[1]` selects its second element `88`. Evaluates to the integer `88`. Local study-map skill 3.8 (Mutable Lists Inside Tuples vs Tuples Inside Lists), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: `roster[1]` selects the second tuple `('Lin', 88)`, and `[1]` selects its second element `88`.
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `roster[1]` selects the second tuple `('Lin', 88)`, and `[1]` selects its second element `88`.
- **C:** Correct. Evaluates to the integer `88`. In this case: `roster[1]` selects the second tuple `('Lin', 88)`, and `[1]` selects its second element `88`.
- **D:** Incorrect for this question. Evaluates to the integer `99`. Why the correct answer wins: `roster[1]` selects the second tuple `('Lin', 88)`, and `[1]` selects its second element `88`.

### Question 39 — A

Answer: `3`. Assigning to existing key `'q1'` updates its value in place while assigning `'q3'` inserts one new entry, bringing `len(grades)` from `2` to `3`. Evaluates to the integer `3`. Local study-map skill 3.9 (Dictionary Creation, Key Lookup, Insertion, Update, and Deletion), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: Assigning to existing key `'q1'` updates its value in place while assigning `'q3'` inserts one new entry, bringing `len(grades)` from `2` to `3`.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Assigning to existing key `'q1'` updates its value in place while assigning `'q3'` inserts one new entry, bringing `len(grades)` from `2` to `3`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Assigning to existing key `'q1'` updates its value in place while assigning `'q3'` inserts one new entry, bringing `len(grades)` from `2` to `3`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Assigning to existing key `'q1'` updates its value in place while assigning `'q3'` inserts one new entry, bringing `len(grades)` from `2` to `3`.

### Question 40 — A

Answer: `items()`. `gradebook.items()` yields `(key, value)` 2-tuples suitable for `name, mark` unpacking. `dict.items()` yields `(key, value)` 2-tuples suitable for two-variable `for k, v in d.items():` unpacking. Local study-map skill 3.10 (Dictionary Iteration with keys(), values(), items(), and get()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `dict.items()` yields `(key, value)` 2-tuples suitable for two-variable `for k, v in d.items():` unpacking. In this case: `gradebook.items()` yields `(key, value)` 2-tuples suitable for `name, mark` unpacking.
- **B:** Incorrect for this question. `dict.keys()` returns a dynamic view of the dictionary keys. Why the correct answer wins: `gradebook.items()` yields `(key, value)` 2-tuples suitable for `name, mark` unpacking.
- **C:** Incorrect for this question. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. Why the correct answer wins: `gradebook.items()` yields `(key, value)` 2-tuples suitable for `name, mark` unpacking.
- **D:** Incorrect for this question. `dict.values()` returns a dynamic view of the dictionary values. Why the correct answer wins: `gradebook.items()` yields `(key, value)` 2-tuples suitable for `name, mark` unpacking.

### Question 41 — C, E

Answers: `"Item's price"`; `'Item\'s price'`. `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`. Wrapping a string in double quotes lets an apostrophe appear inside without a backslash. Escaping the inner single quote with `\` keeps a single-quoted string literal valid. Local study-map skill 3.11 (String Literals, Escape Sequences, Quotes, and Multiline Strings), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Opening with `"` and closing with an apostrophe leaves the string literal unterminated and raises `SyntaxError`. Why the correct answer wins: `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`.
- **B:** Incorrect for this question. A trailing single backslash escapes the closing quote itself, causing `SyntaxError: unterminated string literal`. Why the correct answer wins: `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`.
- **C:** Correct. Wrapping a string in double quotes lets an apostrophe appear inside without a backslash. In this case: `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`.
- **D:** Incorrect for this question. An unescaped apostrophe inside single quotes terminates the literal early and raises `SyntaxError`. Why the correct answer wins: `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`.
- **E:** Correct. Escaping the inner single quote with `\` keeps a single-quoted string literal valid. In this case: `"Item's price"` and `'Item\'s price'` are valid string literals, whereas unescaped inner single quotes, mismatched quotes, and trailing single backslashes fail with `SyntaxError`.

### Question 42 — D, E

Answers: Every string transformation method returns a brand-new `str` object and leaves the original string unchanged; Out-of-range string slice bounds such as `s[2:99]` clamp silently instead of raising `IndexError`. Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. Slicing clamps start and stop indices to valid string bounds, whereas out-of-range single-index `s[99]` raises `IndexError`. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `str` does not support item assignment; `s[0] = "X"` raises `TypeError`. Why the correct answer wins: Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`.
- **B:** Incorrect for this question. `str` is immutable, so `del s[0]` raises `TypeError`. Why the correct answer wins: Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`.
- **C:** Incorrect for this question. `del t[0]` raises `TypeError` because tuples are immutable; only `del t` (unbinding the whole variable) is legal. Why the correct answer wins: Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`.
- **D:** Correct. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In this case: Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`.
- **E:** Correct. Slicing clamps start and stop indices to valid string bounds, whereas out-of-range single-index `s[99]` raises `IndexError`. In this case: Every string method returns a new `str` without mutating the original, and out-of-range slices such as `name[5:99]` clamp silently instead of raising `IndexError`.

### Question 43 — B

Answer: `isalpha()`. `str.isalpha()` returns `True` when `surname` has at least one character and every character is alphabetic. `str.isalpha()` returns `True` only when the string is non-empty and all characters are alphabetic. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. Why the correct answer wins: `str.isalpha()` returns `True` when `surname` has at least one character and every character is alphabetic.
- **B:** Correct. `str.isalpha()` returns `True` only when the string is non-empty and all characters are alphabetic. In this case: `str.isalpha()` returns `True` when `surname` has at least one character and every character is alphabetic.
- **C:** Incorrect for this question. `str.endswith(suffix)` checks whether a string ends with `suffix`. Why the correct answer wins: `str.isalpha()` returns `True` when `surname` has at least one character and every character is alphabetic.
- **D:** Incorrect for this question. `str.isdigit()` returns `True` when the string is non-empty and every character is a digit. Why the correct answer wins: `str.isalpha()` returns `True` when `surname` has at least one character and every character is alphabetic.

### Question 44 — D, E

Answers: A function that reaches the end of its body without any `return` statement returns `None`; Adding `yield` anywhere in a function body makes calling it return a generator object instead of running the body immediately. Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator. Falling off the end of a Python function implicitly returns `None`. Presence of `yield` compiles the function as a generator factory. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Parameters are local variables of the function call frame and disappear when the frame exits. Why the correct answer wins: Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator.
- **B:** Incorrect for this question. The first `return` executed exits the function immediately; subsequent statements in that block are unreachable. Why the correct answer wins: Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator.
- **C:** Incorrect for this question. `sorted()` is a built-in function that returns a *new* sorted list without modifying `items`. Why the correct answer wins: Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator.
- **D:** Correct. Presence of `yield` compiles the function as a generator factory. In this case: Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator.
- **E:** Correct. Falling off the end of a Python function implicitly returns `None`. In this case: Reaching the end of a regular function without `return` returns `None`, and placing `yield` anywhere in `def` compiles it into a generator function returning a generator iterator.

### Question 45 — C

Answer: `def`. `def` introduces a user-defined function header. `def` introduces a function or generator definition. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `yield` is a reserved Python keyword that turns a function into a generator. Why the correct answer wins: `def` introduces a user-defined function header.
- **B:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `def` introduces a user-defined function header.
- **C:** Correct. `def` introduces a function or generator definition. In this case: `def` introduces a user-defined function header.
- **D:** Incorrect for this question. `import` is a reserved keyword and therefore cannot be used as an ordinary variable name. Why the correct answer wins: `def` introduces a user-defined function header.

### Question 46 — A

Answer: Raises `StopIteration`. Calling `next()` on an exhausted generator iterator raises `StopIteration`. Local study-map skill 4.2 (Generator Functions Using yield and Lazy Iteration), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. In this case: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.

### Question 47 — D

Answer: `11`. Peeling base-10 digits adds `8 + 0 + 3` down to base case `3 < 10`, returning `11`. Evaluates to the integer `11`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: Peeling base-10 digits adds `8 + 0 + 3` down to base case `3 < 10`, returning `11`.
- **B:** Incorrect for this question. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Why the correct answer wins: Peeling base-10 digits adds `8 + 0 + 3` down to base case `3 < 10`, returning `11`.
- **C:** Incorrect for this question. Evaluates to the integer `30`. Why the correct answer wins: Peeling base-10 digits adds `8 + 0 + 3` down to base case `3 < 10`, returning `11`.
- **D:** Correct. Evaluates to the integer `11`. In this case: Peeling base-10 digits adds `8 + 0 + 3` down to base case `3 < 10`, returning `11`.

### Question 48 — B

Answer: Raises `RecursionError`. With no stopping condition, recursive frames accumulate past `0` into negative numbers until Python raises `RecursionError`. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: With no stopping condition, recursive frames accumulate past `0` into negative numbers until Python raises `RecursionError`.
- **B:** Correct. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. In this case: With no stopping condition, recursive frames accumulate past `0` into negative numbers until Python raises `RecursionError`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: With no stopping condition, recursive frames accumulate past `0` into negative numbers until Python raises `RecursionError`.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: With no stopping condition, recursive frames accumulate past `0` into negative numbers until Python raises `RecursionError`.

### Question 49 — B

Answer: Positional arguments must appear before any keyword arguments in a function call. Positional arguments (`82`) must always appear before keyword arguments (`curve=5`) in a function call. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Positional arguments (`82`) must always appear before keyword arguments (`curve=5`) in a function call.
- **B:** Correct. Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time. In this case: Positional arguments (`82`) must always appear before keyword arguments (`curve=5`) in a function call.
- **C:** Incorrect for this question. In `{"a": 1, "a": 2}`, the final binding wins so `len` is `1` and `d["a"]` is `2`. Why the correct answer wins: Positional arguments (`82`) must always appear before keyword arguments (`curve=5`) in a function call.
- **D:** Incorrect for this question. Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter. Why the correct answer wins: Positional arguments (`82`) must always appear before keyword arguments (`curve=5`) in a function call.

### Question 50 — B

Answer: `18`. Keyword arguments bind by parameter name (`quiz=4`, `exam=7`), computing `4 + 2 * 7 == 18`. Evaluates to the integer `18`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Keyword arguments bind by parameter name (`quiz=4`, `exam=7`), computing `4 + 2 * 7 == 18`.
- **B:** Correct. Evaluates to the integer `18`. In this case: Keyword arguments bind by parameter name (`quiz=4`, `exam=7`), computing `4 + 2 * 7 == 18`.
- **C:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Keyword arguments bind by parameter name (`quiz=4`, `exam=7`), computing `4 + 2 * 7 == 18`.
- **D:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Keyword arguments bind by parameter name (`quiz=4`, `exam=7`), computing `4 + 2 * 7 == 18`.

### Question 51 — C, E

Answers: `def connect(host, port=5432):`; `def connect(host="localhost", port=5432):`. `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter. Required parameter `host` precedes defaulted parameter `port=5432`, which is valid Python syntax. Every parameter may carry a default value when no non-default parameter follows. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Function parameters in `def` must be identifiers, never string literals. Why the correct answer wins: `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter.
- **B:** Incorrect for this question. Placing required parameter `port` after defaulted `host="localhost"` raises `SyntaxError`. Why the correct answer wins: `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter.
- **C:** Correct. Every parameter may carry a default value when no non-default parameter follows. In this case: `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter.
- **D:** Incorrect for this question. Duplicate parameter names in a `def` signature raise `SyntaxError`. Why the correct answer wins: `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter.
- **E:** Correct. Required parameter `host` precedes defaulted parameter `port=5432`, which is valid Python syntax. In this case: `def connect(host, port=5432):` and `def connect(host="localhost", port=5432):` never place a non-default parameter after a default parameter.

### Question 52 — D

Answer: `[1] [1, 2]` (default list is evaluated once at `def` time and shared across calls). Default list `bag` is allocated once when `def` runs and reused across calls that omit `bag`, outputting `[1] [1, 2]`. Default parameter expressions are evaluated once when `def` executes, so mutating a default list persists across subsequent calls. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. A fresh list per call happens only when the function uses `None` as the sentinel default and creates `[]` inside the body. Why the correct answer wins: Default list `bag` is allocated once when `def` runs and reused across calls that omit `bag`, outputting `[1] [1, 2]`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Default list `bag` is allocated once when `def` runs and reused across calls that omit `bag`, outputting `[1] [1, 2]`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Default list `bag` is allocated once when `def` runs and reused across calls that omit `bag`, outputting `[1] [1, 2]`.
- **D:** Correct. Default parameter expressions are evaluated once when `def` executes, so mutating a default list persists across subsequent calls. In this case: Default list `bag` is allocated once when `def` runs and reused across calls that omit `bag`, outputting `[1] [1, 2]`.

### Question 53 — B

Answer: `60`. Without `global pass_cutoff`, assigning inside `preview_strict()` creates and discards a local variable, leaving module-level `pass_cutoff` at `60`. Evaluates to the integer `60`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. Why the correct answer wins: Without `global pass_cutoff`, assigning inside `preview_strict()` creates and discards a local variable, leaving module-level `pass_cutoff` at `60`.
- **B:** Correct. Evaluates to the integer `60`. In this case: Without `global pass_cutoff`, assigning inside `preview_strict()` creates and discards a local variable, leaving module-level `pass_cutoff` at `60`.
- **C:** Incorrect for this question. `NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Without `global pass_cutoff`, assigning inside `preview_strict()` creates and discards a local variable, leaving module-level `pass_cutoff` at `60`.
- **D:** Incorrect for this question. Evaluates to the integer `100`. Why the correct answer wins: Without `global pass_cutoff`, assigning inside `preview_strict()` creates and discards a local variable, leaving module-level `pass_cutoff` at `60`.

### Question 54 — C

Answer: `global`. `global graded_papers` binds `graded_papers` inside the function to the module-level variable. `global` is a reserved Python keyword that binds a name inside a function to module scope. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `class` is a reserved keyword and cannot be used as a variable identifier. Why the correct answer wins: `global graded_papers` binds `graded_papers` inside the function to the module-level variable.
- **B:** Incorrect for this question. `yield` is a reserved Python keyword that turns a function into a generator. Why the correct answer wins: `global graded_papers` binds `graded_papers` inside the function to the module-level variable.
- **C:** Correct. `global` is a reserved Python keyword that binds a name inside a function to module scope. In this case: `global graded_papers` binds `graded_papers` inside the function to the module-level variable.
- **D:** Incorrect for this question. `nonlocal` is a reserved Python keyword and cannot name an ordinary variable. Why the correct answer wins: `global graded_papers` binds `graded_papers` inside the function to the module-level variable.

### Question 55 — B, D

Answers: `SystemExit` inherits directly from `BaseException`, not from `Exception`; `KeyboardInterrupt` inherits directly from `BaseException`, not from `Exception`. `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught. Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`. `KeyboardInterrupt` sits directly under `BaseException` so user Ctrl-C interrupts are not swallowed by `except Exception:`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `LookupError` groups `IndexError` and `KeyError` under `Exception`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught.
- **B:** Correct. `KeyboardInterrupt` sits directly under `BaseException` so user Ctrl-C interrupts are not swallowed by `except Exception:`. In this case: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught.
- **C:** Incorrect for this question. `TypeError` sits under `Exception` rather than under `LookupError` or `SyntaxError`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught.
- **D:** Correct. Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`. In this case: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught.
- **E:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` so `except Exception:` leaves process exits and Ctrl-C interrupts uncaught.

### Question 56 — D

Answer: `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`. `ArithmeticError` is the direct abstract parent class of `ZeroDivisionError`. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. Why the correct answer wins: `ArithmeticError` is the direct abstract parent class of `ZeroDivisionError`.
- **B:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: `ArithmeticError` is the direct abstract parent class of `ZeroDivisionError`.
- **C:** Incorrect for this question. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Why the correct answer wins: `ArithmeticError` is the direct abstract parent class of `ZeroDivisionError`.
- **D:** Correct. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. In this case: `ArithmeticError` is the direct abstract parent class of `ZeroDivisionError`.

### Question 57 — D

Answer: Raises `ValueError`. Passing a `str` whose characters are not a valid integer literal raises `ValueError` (`'absent'` has the right type `str` but invalid content). `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Passing a `str` whose characters are not a valid integer literal raises `ValueError` (`'absent'` has the right type `str` but invalid content).
- **B:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Passing a `str` whose characters are not a valid integer literal raises `ValueError` (`'absent'` has the right type `str` but invalid content).
- **C:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Passing a `str` whose characters are not a valid integer literal raises `ValueError` (`'absent'` has the right type `str` but invalid content).
- **D:** Correct. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). In this case: Passing a `str` whose characters are not a valid integer literal raises `ValueError` (`'absent'` has the right type `str` but invalid content).

### Question 58 — D

Answer: `except`. `except` catches the `ZeroDivisionError` raised inside the `try` block. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. Why the correct answer wins: `except` catches the `ZeroDivisionError` raised inside the `try` block.
- **B:** Incorrect for this question. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Why the correct answer wins: `except` catches the `ZeroDivisionError` raised inside the `try` block.
- **C:** Incorrect for this question. `raise` triggers an exception or re-raises the active exception when used bare inside `except`. Why the correct answer wins: `except` catches the `ZeroDivisionError` raised inside the `try` block.
- **D:** Correct. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). In this case: `except` catches the `ZeroDivisionError` raised inside the `try` block.

### Question 59 — B, C

Answers: Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch; Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`. Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. A bare `except:` must always be the *last* `except` clause in Python 3; placing it earlier is a `SyntaxError`. Why the correct answer wins: Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes.
- **B:** Correct. `KeyError` inherits from `LookupError`, so the narrower handler must appear earlier. In this case: Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes.
- **C:** Correct. `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. In this case: Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes.
- **D:** Incorrect for this question. At most *one* `except` branch executes for a single raised exception. Why the correct answer wins: Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes.
- **E:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: Place `except KeyError:` above `except LookupError:` and always order narrower subclasses before broader parent classes.

### Question 60 — A

Answer: `finally`. `finally` runs its cleanup block regardless of whether the `try` suite succeeded or raised an exception. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. In this case: `finally` runs its cleanup block regardless of whether the `try` suite succeeded or raised an exception.
- **B:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: `finally` runs its cleanup block regardless of whether the `try` suite succeeded or raised an exception.
- **C:** Incorrect for this question. `else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks. Why the correct answer wins: `finally` runs its cleanup block regardless of whether the `try` suite succeeded or raised an exception.
- **D:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `finally` runs its cleanup block regardless of whether the `try` suite succeeded or raised an exception.
