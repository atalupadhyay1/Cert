# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 1

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 17 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A finance analyst runs `python3 budget_report.py`, which imports a helper module `fx_rates.py` and creates `__pycache__` files. Which two statements accurately describe how standard CPython translates and runs this budget utility? Select two.

- A. Cached `.pyc` files store compiled Python bytecode so unchanged imported modules skip reparsing on later runs
- B. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- C. Cached `.pyc` files contain x86-64 machine instructions that run directly on the OS kernel without Python installed
- D. CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime
- E. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes

### 2. In a monthly expense splitter, the statement `share_per_member = rent_total / roommate_count` parses into valid Python tokens and obeys grammar rules, yet raises `ZeroDivisionError` when `roommate_count` is `0`. Which language layer does this runtime failure violate?

- A. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- B. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning
- C. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- D. A lexical error because the character or token itself does not belong to valid Python token forms

### 3. A developer naming variables in a payroll tax calculator wants to avoid reserved words that raise `SyntaxError` on assignment. Which two names are hard reserved keywords in Python 3? Select two.

- A. `yield`
- B. `false`
- C. `sum`
- D. `global`
- E. `match`

### 4. An accounting ledger script defines integer constants for cents and bit flags. Which two literals are valid integer literals in Python 3? Select two.

- A. `0x2A`
- B. `1_250_000`
- C. `0o19`
- D. `500_`
- E. `045`

### 5. Which identifier is a valid variable name in Python 3 and follows PEP-8 naming conventions for storing a currency exchange rate?

- A. `fx-rate`
- B. `2nd_quarter`
- C. `total$usd`
- D. `fx_rate_2`

### 6. Complete the bill-splitting expression `twenty_notes = 135 ____ 20` so `twenty_notes` receives the integer count of full twenty-dollar bills (`6`) rather than `6.75` or `15`. Which operator fills the blank?

- A. `/`
- B. `%`
- C. `//`
- D. `**`

### 7. A ledger adjustment expression evaluates `delta = -4 ** 2` in Python 3. Because exponentiation binds tighter than unary negation, what integer is assigned to `delta`?

- A. `SyntaxError`
- B. `-16`
- C. `16`
- D. `-7`

### 8. Complete the fixed-point scaling snippet `scaled_cents = 7 ____ 2` so shifting the binary representation of `7` two positions multiplies it by `4` to produce `28`. Which bitwise operator fills the blank?

- A. `^`
- B. `&`
- C. `>>`
- D. `<<`

### 9. A petty-cash checker runs `print(0.1 * 3 == 0.3)` in standard Python 3 without importing `decimal`. What happens and why?

- A. `ZeroDivisionError`
- B. It prints `False` because binary IEEE-754 floats store tenths like `0.1` and `0.2` with tiny rounding residuals
- C. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- D. `TypeError`

### 10. Complete `print('USD', 'EUR', 'JPY', ____)` in a currency ticker utility so it outputs `USD:EUR:JPY` on a single line. Which keyword argument fills the blank?

- A. `sep=':'`
- B. `end=''`
- C. `sep=''`
- D. `end=', '`

### 11. Complete `unit_price = ____(input('Enter price: '))` so typing `19.95` at the prompt converts the returned string into the numeric value `19.95` without raising `ValueError`. Which built-in callable fills the blank?

- A. `bool`
- B. `int`
- C. `str`
- D. `float`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete the rebate tier branch `if spend >= 500: rate = 10` / `____ spend >= 200: rate = 5` / `else: rate = 1` so at most one rebate rate is assigned. Which keyword fills the blank?

- A. `pass`
- B. `else`
- C. `elif`
- D. `while`

### 13. A budget loyalty script sets `spend = 320` and runs `if spend >= 500: print('GOLD')` / `elif spend >= 250: print('SILVER')` / `elif spend >= 100: print('BRONZE')` / `else: print('NONE')`. What is printed?

- A. `GOLD` followed by `SILVER`
- B. `GOLD`
- C. `SILVER`
- D. `BRONZE`

### 14. A bonus script sets `points = 600` and runs two separate `if` statements: `if points >= 500: print('GOLD')` followed on the next line by `if points >= 200: print('SILVER')`. What is printed?

- A. `GOLD`
- B. `SILVER`
- C. `GOLD` followed by `SILVER`
- D. Nothing is printed

### 15. A checkout calculator computes a shipping fee or account badge in a single inline expression. Which two expressions are syntactically valid Python conditional expressions? Select two.

- A. `0 if subtotal >= 50 else 5`
- B. `if subtotal >= 50 then 0 else 5`
- C. `subtotal >= 50 ? 0 : 5`
- D. `0 if subtotal >= 50`
- E. `'VIP' if points >= 100 else 'STD'`

### 16. An invoice validator checks `if payload:` on incoming values. Which two values of `payload` evaluate to `False` in a Boolean context? Select two.

- A. `{}`
- B. `-1`
- C. `(0,)`
- D. `0.0`
- E. `'0'`

### 17. A ledger check sets `pending = []` and `currency = '0'` and runs `if pending: print('OK')` / `elif currency: print('WARN')` / `else: print('ALERT')`. What does it print?

- A. Nothing is printed
- B. `WARN`
- C. `OK`
- D. `ALERT`

### 18. Complete the tax-bracket guard `if income >= 40000 ____ income < 85000:` so the suite runs only when both comparisons are `True`. Which logical operator fills the blank?

- A. `not`
- B. `and`
- C. `is`
- D. `or`

### 19. A currency config loader sets `user_ccy = ''` and evaluates `active_ccy = user_ccy or 'USD'`. What value is bound to `active_ccy`?

- A. `True`
- B. `''`
- C. `'USD'`
- D. `False`

### 20. Complete the savings accumulator `balance = 100` / `____ balance < 250:` / `    balance += 50` so deposits repeat as long as `balance < 250` holds. Which keyword fills the blank?

- A. `elif`
- B. `except`
- C. `for`
- D. `while`

### 21. A debt-paydown counter runs `step = 3; paid = 0` and `while step <= 9: paid += step; step += 3`, then executes `print(paid)`. What integer is printed?

- A. `18`
- B. `21`
- C. `9`
- D. `12`

### 22. A quarterly amortization loop must execute its body exactly four times. Which two `range()` calls generate exactly four integers? Select two.

- A. `range(10, 2, -2)`
- B. `range(0, 10, 2)`
- C. `range(8, 2)`
- D. `range(2, 8, -2)`
- E. `range(2, 10, 2)`

### 23. An installment schedule runs `print(sum(range(2, 8, 2)))`. What integer does it print?

- A. `20`
- B. `6`
- C. `16`
- D. `12`

### 24. A voucher checksum helper runs `total = 0` / `for digit in '1405': total += int(digit)` / `print(total)`. What integer is printed?

- A. `24`
- B. `TypeError`
- C. `4`
- D. `10`

### 25. Complete the expense loop `for amt in [25, -10, 15, -5]:` / `    if amt < 0: ____` / `    net += amt` so negative refunds are skipped without stopping the loop. Which keyword fills the blank?

- A. `continue`
- B. `pass`
- C. `break`
- D. `return`

### 26. A developer writes `if audit_enabled:` / `    ____` as a temporary no-op placeholder in a ledger script so Python parses the indented block without error. Which keyword fills the blank?

- A. `raise`
- B. `break`
- C. `continue`
- D. `pass`

### 27. In an invoice search routine that attaches an `else:` suite to a loop, under which two conditions does that loop `else:` suite execute? Select two.

- A. Immediately after a `break` statement jumps out of the loop body
- B. Whenever an unhandled exception aborts the loop body
- C. When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`
- D. When a `for` loop finishes iterating over every element without executing `break`
- E. Right before a `return` statement inside the loop exits the enclosing function

### 28. A cross-currency matrix script sets `pairs = 0` and runs `for src in ['USD', 'EUR', 'GBP']:` / `    for dst in ['USD', 'EUR', 'GBP']:` / `        if src != dst: pairs += 1` / `print(pairs)`. What integer is printed?

- A. `5`
- B. `3`
- C. `6`
- D. `9`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. A budget history list stores `quarters = [10, 20, 30, 40, 50]`. What list is returned by `quarters[1:3]`?

- A. `[10, 30, 50]`
- B. `[40, 50]`
- C. `[20, 30]`
- D. `IndexError`

### 30. Given `quarters = [10, 20, 30, 40, 50]`, what list does `quarters[::-2]` evaluate to?

- A. `[40, 30, 20, 10]`
- B. `[50, 30, 10]`
- C. `[10, 30, 50]`
- D. `IndexError`

### 31. Complete `fees = [1, 2]; fees.____([3, 4])` so `fees` becomes the flat four-element list `[1, 2, 3, 4]` instead of `[1, 2, [3, 4]]`. Which list method name fills the blank?

- A. `pop`
- B. `extend`
- C. `append`
- D. `insert`

### 32. An analyst holds `items = [30, 10, 20]` in memory. Which two expressions mutate the existing `items` list object in place rather than allocating a new outer list? Select two.

- A. `items.sort()`
- B. `items[:]`
- C. `items + [x]`
- D. `items.pop()`
- E. `sorted(items)`

### 33. Complete `vals = [10, 20, 30, 40, 50]; ____ vals[1:4]` so indices `1` through `3` are removed in place, leaving `vals` equal to `[10, 50]`. Which keyword fills the blank?

- A. `del`
- B. `return`
- C. `from`
- D. `pass`

### 34. A budget planner has a flat list `items = [100, 200, 300]` and needs a shallow copy so appending to the copy does not alter `items`. Which two expressions create a new shallow-copied list? Select two.

- A. `items.pop()`
- B. `items[:]`
- C. `items.sort()`
- D. `backup = items`
- E. `items.copy()`

### 35. What list is produced by `[n ** 2 for n in range(6) if n % 2 == 0]` in a variance helper script?

- A. `[0, 4, 16]`
- B. `SyntaxError`
- C. `[]`
- D. `[1, 9, 25]`

### 36. A currency map stores `rates = {'EUR': 100, 'GBP': 120}` and evaluates `print(100 in rates)`. What is printed?

- A. `None`
- B. `KeyError`
- C. `False`
- D. `True`

### 37. A currency calculator needs to pack the single integer `42` into a 1-element `tuple`. Which two right-hand-side expressions evaluate to a `tuple` of length `1`? Select two.

- A. `(42)`
- B. `(42,)`
- C. `{}`
- D. `42,`
- E. `tuple()`

### 38. A record stores `entry = ('A', [1, 2])` and runs `entry[1].append(3)` followed by `print(entry)`. What happens?

- A. `ValueError`
- B. `('A', [1, 2, 3])`
- C. `AttributeError`
- D. `TypeError`

### 39. Complete `rates = {'EUR': 0.92}; chf = rates.____('CHF', 0.0)` so looking up missing key `'CHF'` returns fallback `0.0` instead of raising `KeyError`. Which dictionary method name fills the blank?

- A. `values`
- B. `keys`
- C. `get`
- D. `items`

### 40. A fee lookup defines `fees = {'wire': 4, 'ach': 2}` and runs `print(sum(fees.values()))`. What integer is printed?

- A. `6`
- B. `TypeError`
- C. `2`
- D. `3`

### 41. A receipt formatter needs a valid Python string literal representing the text `Chef's kiss`. Which two literals parse without `SyntaxError`? Select two.

- A. `'Chef's kiss'`
- B. C-style `/* ... */` delimiters comment out multi-line blocks in Python
- C. `"Chef's kiss"`
- D. `'Chef\'s kiss'`
- E. `'C:\temp\'`

### 42. Complete `pos = memo.____('REFUND')` so searching a transaction memo returns `-1` instead of raising `ValueError` when `'REFUND'` is absent. Which string method name fills the blank?

- A. `find`
- B. `strip`
- C. `index`
- D. `split`

### 43. An account-code script sets `code = 'usd'` and executes `code[0] = 'U'`. What happens at runtime?

- A. `None`
- B. `'token-42'`
- C. `TypeError` because `str` objects are immutable and do not support item assignment
- D. `IndexError`

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Complete the function header `____ add_tax(subtotal, rate):` / `    return subtotal * (1 + rate)` in a billing module. Which keyword starts a named Python function definition?

- A. `return`
- B. `function`
- C. `lambda`
- D. `def`

### 45. A developer writes `def show_fee(x): print(x + 5)` with no `return` statement, then executes `saved = show_fee(20)` and checks `saved`. What value is bound to `saved`?

- A. `25`
- B. `TypeError`
- C. `None`
- D. `0`

### 46. Complete `def installments(n):` / `    for i in range(1, n + 1):` / `        ____ i * 50` so calling `installments(3)` returns a lazy generator iterator instead of exiting on the first iteration. Which keyword fills the blank?

- A. `yield`
- B. `pass`
- C. `raise`
- D. `return`

### 47. A script defines `def two_fees(): yield 1; yield 2`, binds `g = two_fees()`, discards `first = list(g)`, and then prints `list(g)` a second time. What does the second `list(g)` evaluate to?

- A. `StopIteration`
- B. `[1, 2]`
- C. `ValueError`
- D. `[]`, because a generator iterator is single-pass and already exhausted after the first `list(g)` call

### 48. A recursive budget helper defines `def tri(n): return 0 if n == 0 else n + tri(n - 1)` and prints `tri(4)`. What integer is printed?

- A. `10`
- B. `24`
- C. `RecursionError`
- D. `4`

### 49. Which two design elements are essential so a recursive Python function computes a result and terminates without raising `RecursionError`? Select two.

- A. Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument
- B. Replacing every `return` statement with `break` inside the `def` body
- C. A reachable base case that returns directly without making another recursive call
- D. A recursive call whose arguments move strictly closer to the base case on each step
- E. Declaring every parameter `global` inside the function header

### 50. Given `def net_bill(amount, fee=5, discount=2): return amount + fee - discount`, what integer does `net_bill(20, discount=4)` return?

- A. `21`
- B. `SyntaxError`
- C. `23`
- D. `TypeError`

### 51. A tax helper defines `def calc(base, rate): return base * rate`. Which two invocations execute cleanly without raising `SyntaxError` or `TypeError`? Select two.

- A. `calc(rate=0.2, base=100)`
- B. `calc(100, rate=0.2)`
- C. `calc(100, tax=0.2)`
- D. `calc(base=100, 0.2)`
- E. `calc(100, base=200)`

### 52. A developer writes `def apply_rebate(rate=0.05, subtotal): return subtotal * (1 - rate)` in a billing script. What happens when Python parses this definition?

- A. `def quote(amount, rate=1.1, fee=0):`
- B. `SyntaxError` because a parameter without a default value cannot follow a parameter with a default value
- C. `NameError`
- D. `TypeError`

### 53. A ledger helper defines `def log_tx(amt, acc=[]): acc.append(amt); return acc`, calls `log_tx(1)`, and then prints `log_tx(2)`. What list is printed on the second call?

- A. `[1, 2]`
- B. `TypeError`
- C. `[2]`
- D. `[1]`

### 54. Complete `budget_cap = 500` / `def raise_cap():` / `    ____ budget_cap` / `    budget_cap += 100` so calling `raise_cap()` updates the module-level `budget_cap` to `600` instead of raising `UnboundLocalError`. Which keyword fills the blank?

- A. `return`
- B. `global`
- C. `nonlocal`
- D. `from`

### 55. Which two operations on a module-level variable inside a Python function succeed WITHOUT declaring `global`? Select two.

- A. Calling `.append()` on a module-level list inside a function mutates that list in place without needing `global`
- B. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- C. `UnboundLocalError` because assigning to the variable anywhere in the function marks it local across the entire function body
- D. Declaring every parameter `global` inside the function header
- E. Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`

### 56. In Python's built-in exception hierarchy, `ZeroDivisionError` is a direct subclass of which intermediate exception class under `Exception`?

- A. `ValueError`
- B. `ArithmeticError`
- C. `SyntaxError`
- D. `LookupError`

### 57. Which two built-in exceptions inherit directly from `BaseException` rather than `Exception`, so an `except Exception:` handler intentionally lets them propagate? Select two.

- A. `ValueError`
- B. `ZeroDivisionError`
- C. `SystemExit`
- D. `KeyError`
- E. `KeyboardInterrupt`

### 58. Complete `if deposit < 0:` / `    ____ ValueError('deposit must be non-negative')` so negative deposits immediately trigger a `ValueError`. Which keyword fills the blank?

- A. `finally`
- B. `except`
- C. `assert`
- D. `raise`

### 59. A budget importer executes `cents = int('45.00')` on a decimal-formatted string. Which exception is raised?

- A. `ValueError`
- B. `KeyError`
- C. `TypeError`
- D. `ZeroDivisionError`

### 60. A script runs `log = []` then `try: log.append('T'); x = 20 // 5` / `except ZeroDivisionError: log.append('X')` / `else: log.append('E')` / `finally: log.append('F')` and prints `'-'.join(log)`. What is printed?

- A. `T-F`
- B. `T-X-F`
- C. `T-X-E-F`
- D. `T-E-F`

---

## Answer key and explanations

### Question 1 — A, D

Answers: CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime; Cached `.pyc` files store compiled Python bytecode so unchanged imported modules skip reparsing on later runs. CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs. Standard CPython translates source code into bytecode instructions executed by its runtime virtual machine rather than linking a native OS binary ahead of time. Files under `__pycache__` hold version-tagged bytecode that speeds up module imports without changing program semantics or removing the need for the PVM. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Files under `__pycache__` hold version-tagged bytecode that speeds up module imports without changing program semantics or removing the need for the PVM. In this case: CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs.
- **B:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs.
- **C:** Incorrect for this question. `.pyc` files store portable CPython bytecode for the Python virtual machine, not standalone native CPU machine code. Why the correct answer wins: CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs.
- **D:** Correct. Standard CPython translates source code into bytecode instructions executed by its runtime virtual machine rather than linking a native OS binary ahead of time. In this case: CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs.
- **E:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: CPython compiles `.py` source into bytecode executed at runtime by the Python virtual machine and caches imported module bytecode inside `.pyc` files so unchanged helpers skip reparsing on subsequent runs.

### Question 2 — B

Answer: A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning. The tokens (lexis) and statement grammar (syntax) are completely legal, so attempting division by zero fails at runtime semantics when the expression is evaluated. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: The tokens (lexis) and statement grammar (syntax) are completely legal, so attempting division by zero fails at runtime semantics when the expression is evaluated.
- **B:** Correct. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. In this case: The tokens (lexis) and statement grammar (syntax) are completely legal, so attempting division by zero fails at runtime semantics when the expression is evaluated.
- **C:** Incorrect for this question. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Why the correct answer wins: The tokens (lexis) and statement grammar (syntax) are completely legal, so attempting division by zero fails at runtime semantics when the expression is evaluated.
- **D:** Incorrect for this question. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Why the correct answer wins: The tokens (lexis) and statement grammar (syntax) are completely legal, so attempting division by zero fails at runtime semantics when the expression is evaluated.

### Question 3 — A, D

Answers: `global`; `yield`. `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. In this case: `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier.
- **B:** Incorrect for this question. Python keywords are case-sensitive: `False` is reserved, whereas lowercase `false` is an ordinary identifier. Why the correct answer wins: `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier.
- **C:** Incorrect for this question. `sum` is a built-in function name rather than a reserved keyword, though shadowing it is discouraged. Why the correct answer wins: `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier.
- **D:** Correct. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. In this case: `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier.
- **E:** Incorrect for this question. `match` is a soft keyword in Python 3.10+, so unlike hard keywords it remains usable as a variable identifier. Why the correct answer wins: `global` and `yield` are hard reserved keywords in Python 3, whereas `match` is a soft keyword, `sum` is a built-in function name, and lowercase `false` is an unreserved identifier.

### Question 4 — A, B

Answers: `1_250_000`; `0x2A`. `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore. Single underscores between digits such as `1_250_000` are legal visual separators in Python 3.6+ numeric literals. `0x2A` is a valid hexadecimal integer literal equal to `2 * 16 + 10 == 42`. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `0x2A` is a valid hexadecimal integer literal equal to `2 * 16 + 10 == 42`. In this case: `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore.
- **B:** Correct. Single underscores between digits such as `1_250_000` are legal visual separators in Python 3.6+ numeric literals. In this case: `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore.
- **C:** Incorrect for this question. Octal literals allow only digits `0` through `7`, so `9` in `0o19` raises `SyntaxError`. Why the correct answer wins: `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore.
- **D:** Incorrect for this question. Numeric literals cannot end with a trailing underscore (`500_` raises `SyntaxError`). Why the correct answer wins: `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore.
- **E:** Incorrect for this question. Non-zero decimal integer literals cannot start with a leading `0` in Python 3; octal requires `0o45`. Why the correct answer wins: `1_250_000` uses legal single-underscore digit separators and `0x2A` is a valid hexadecimal literal (`42`), whereas `045` uses an illegal leading zero, `0o19` uses `9` in octal, and `500_` ends with a trailing underscore.

### Question 5 — D

Answer: `fx_rate_2`. Identifiers must begin with a letter or underscore and contain only letters, digits, and underscores, so `fx_rate_2` is valid while `2nd_quarter`, `fx-rate`, and `total$usd` are illegal. `fx_rate_2` starts with a letter and uses only lowercase letters, underscores, and digits, obeying both Python grammar and PEP-8. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `fx-rate` is parsed as subtraction `fx - rate` because hyphens are illegal in Python identifiers. Why the correct answer wins: Identifiers must begin with a letter or underscore and contain only letters, digits, and underscores, so `fx_rate_2` is valid while `2nd_quarter`, `fx-rate`, and `total$usd` are illegal.
- **B:** Incorrect for this question. `2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier. Why the correct answer wins: Identifiers must begin with a letter or underscore and contain only letters, digits, and underscores, so `fx_rate_2` is valid while `2nd_quarter`, `fx-rate`, and `total$usd` are illegal.
- **C:** Incorrect for this question. `$` is not a valid identifier character in Python 3. Why the correct answer wins: Identifiers must begin with a letter or underscore and contain only letters, digits, and underscores, so `fx_rate_2` is valid while `2nd_quarter`, `fx-rate`, and `total$usd` are illegal.
- **D:** Correct. `fx_rate_2` starts with a letter and uses only lowercase letters, underscores, and digits, obeying both Python grammar and PEP-8. In this case: Identifiers must begin with a letter or underscore and contain only letters, digits, and underscores, so `fx_rate_2` is valid while `2nd_quarter`, `fx-rate`, and `total$usd` are illegal.

### Question 6 — C

Answer: `//`. Floor division `135 // 20` rounds the quotient down to the integer `6`, whereas `/` returns `6.75` and `%` returns the leftover `15`. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. True division `/` always returns a `float` in Python 3, even when both operands divide evenly (`8 / 2 == 4.0`). Why the correct answer wins: Floor division `135 // 20` rounds the quotient down to the integer `6`, whereas `/` returns `6.75` and `%` returns the leftover `15`.
- **B:** Incorrect for this question. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Why the correct answer wins: Floor division `135 // 20` rounds the quotient down to the integer `6`, whereas `/` returns `6.75` and `%` returns the leftover `15`.
- **C:** Correct. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). In this case: Floor division `135 // 20` rounds the quotient down to the integer `6`, whereas `/` returns `6.75` and `%` returns the leftover `15`.
- **D:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: Floor division `135 // 20` rounds the quotient down to the integer `6`, whereas `/` returns `6.75` and `%` returns the leftover `15`.

### Question 7 — B

Answer: `-16`. Exponentiation `**` has higher precedence than unary `-`, so Python evaluates `-(4 ** 2)` and assigns `-16` rather than `(-4) ** 2 == 16`. Evaluates to the integer `-16`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Exponentiation `**` has higher precedence than unary `-`, so Python evaluates `-(4 ** 2)` and assigns `-16` rather than `(-4) ** 2 == 16`.
- **B:** Correct. Evaluates to the integer `-16`. In this case: Exponentiation `**` has higher precedence than unary `-`, so Python evaluates `-(4 ** 2)` and assigns `-16` rather than `(-4) ** 2 == 16`.
- **C:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Exponentiation `**` has higher precedence than unary `-`, so Python evaluates `-(4 ** 2)` and assigns `-16` rather than `(-4) ** 2 == 16`.
- **D:** Incorrect for this question. Evaluates to the integer `-7`. Why the correct answer wins: Exponentiation `**` has higher precedence than unary `-`, so Python evaluates `-(4 ** 2)` and assigns `-16` rather than `(-4) ** 2 == 16`.

### Question 8 — D

Answer: `<<`. Left shift `7 << 2` shifts bits left by two places, multiplying `7` by `2 ** 2` (`4`) to produce `28`. Left shift `x << n` multiplies integer `x` by `2 ** n`. Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Why the correct answer wins: Left shift `7 << 2` shifts bits left by two places, multiplying `7` by `2 ** 2` (`4`) to produce `28`.
- **B:** Incorrect for this question. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. Why the correct answer wins: Left shift `7 << 2` shifts bits left by two places, multiplying `7` by `2 ** 2` (`4`) to produce `28`.
- **C:** Incorrect for this question. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. Why the correct answer wins: Left shift `7 << 2` shifts bits left by two places, multiplying `7` by `2 ** 2` (`4`) to produce `28`.
- **D:** Correct. Left shift `x << n` multiplies integer `x` by `2 ** n`. In this case: Left shift `7 << 2` shifts bits left by two places, multiplying `7` by `2 ** 2` (`4`) to produce `28`.

### Question 9 — B

Answer: It prints `False` because binary IEEE-754 floats store tenths like `0.1` and `0.2` with tiny rounding residuals. IEEE-754 binary floats store `0.1` with a tiny binary rounding residual so `0.1 * 3` evaluates to `0.30000000000000004`, making `== 0.3` print `False`. Base-2 floating-point cannot represent most base-10 tenths exactly, so `0.1 * 3` (`0.30000000000000004`) is not `== 0.3`. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: IEEE-754 binary floats store `0.1` with a tiny binary rounding residual so `0.1 * 3` evaluates to `0.30000000000000004`, making `== 0.3` print `False`.
- **B:** Correct. Base-2 floating-point cannot represent most base-10 tenths exactly, so `0.1 * 3` (`0.30000000000000004`) is not `== 0.3`. In this case: IEEE-754 binary floats store `0.1` with a tiny binary rounding residual so `0.1 * 3` evaluates to `0.30000000000000004`, making `== 0.3` print `False`.
- **C:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: IEEE-754 binary floats store `0.1` with a tiny binary rounding residual so `0.1 * 3` evaluates to `0.30000000000000004`, making `== 0.3` print `False`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: IEEE-754 binary floats store `0.1` with a tiny binary rounding residual so `0.1 * 3` evaluates to `0.30000000000000004`, making `== 0.3` print `False`.

### Question 10 — A

Answer: `sep=':'`. `sep=':'` replaces the default space between positional arguments in `print()`, joining the three currency codes as `USD:EUR:JPY`. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. In this case: `sep=':'` replaces the default space between positional arguments in `print()`, joining the three currency codes as `USD:EUR:JPY`.
- **B:** Incorrect for this question. `end=''` suppresses the trailing newline at the end of a `print()` call. Why the correct answer wins: `sep=':'` replaces the default space between positional arguments in `print()`, joining the three currency codes as `USD:EUR:JPY`.
- **C:** Incorrect for this question. `sep=''` concatenates positional arguments in `print()` with no separator characters between them. Why the correct answer wins: `sep=':'` replaces the default space between positional arguments in `print()`, joining the three currency codes as `USD:EUR:JPY`.
- **D:** Incorrect for this question. `end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line. Why the correct answer wins: `sep=':'` replaces the default space between positional arguments in `print()`, joining the three currency codes as `USD:EUR:JPY`.

### Question 11 — D

Answer: `float`. `input()` returns `'19.95'` as a `str`; `float('19.95')` parses the decimal point cleanly, whereas `int('19.95')` raises `ValueError`. `float(...)` parses a numeric string such as `'19.95'` into a floating-point number. Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `bool(...)` tests truthiness; for ANY non-empty string — including `'0'` and `'False'` — `bool(...)` returns `True`. Why the correct answer wins: `input()` returns `'19.95'` as a `str`; `float('19.95')` parses the decimal point cleanly, whereas `int('19.95')` raises `ValueError`.
- **B:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: `input()` returns `'19.95'` as a `str`; `float('19.95')` parses the decimal point cleanly, whereas `int('19.95')` raises `ValueError`.
- **C:** Incorrect for this question. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. Why the correct answer wins: `input()` returns `'19.95'` as a `str`; `float('19.95')` parses the decimal point cleanly, whereas `int('19.95')` raises `ValueError`.
- **D:** Correct. `float(...)` parses a numeric string such as `'19.95'` into a floating-point number. In this case: `input()` returns `'19.95'` as a `str`; `float('19.95')` parses the decimal point cleanly, whereas `int('19.95')` raises `ValueError`.

### Question 12 — C

Answer: `elif`. `elif` attaches an exclusive secondary test to the preceding `if` statement so `else` serves only as the final fallback. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `elif` attaches an exclusive secondary test to the preceding `if` statement so `else` serves only as the final fallback.
- **B:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `elif` attaches an exclusive secondary test to the preceding `if` statement so `else` serves only as the final fallback.
- **C:** Correct. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. In this case: `elif` attaches an exclusive secondary test to the preceding `if` statement so `else` serves only as the final fallback.
- **D:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: `elif` attaches an exclusive secondary test to the preceding `if` statement so `else` serves only as the final fallback.

### Question 13 — C

Answer: `SILVER`. `spend >= 500` is `False`, the first matching branch `spend >= 250` prints `SILVER`, and Python skips the remaining `elif` and `else` branches. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints both `GOLD` and `SILVER` when two independent `if` statements both match. Why the correct answer wins: `spend >= 500` is `False`, the first matching branch `spend >= 250` prints `SILVER`, and Python skips the remaining `elif` and `else` branches.
- **B:** Incorrect for this question. Prints `GOLD`. Why the correct answer wins: `spend >= 500` is `False`, the first matching branch `spend >= 250` prints `SILVER`, and Python skips the remaining `elif` and `else` branches.
- **C:** Correct. In this case: `spend >= 500` is `False`, the first matching branch `spend >= 250` prints `SILVER`, and Python skips the remaining `elif` and `else` branches.
- **D:** Incorrect for this question. Prints `BRONZE`. Why the correct answer wins: `spend >= 500` is `False`, the first matching branch `spend >= 250` prints `SILVER`, and Python skips the remaining `elif` and `else` branches.

### Question 14 — C

Answer: `GOLD` followed by `SILVER`. Because the second check uses a fresh `if` rather than `elif`, Python evaluates both conditions independently and prints `GOLD` followed by `SILVER`. Prints both `GOLD` and `SILVER` when two independent `if` statements both match. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `GOLD`. Why the correct answer wins: Because the second check uses a fresh `if` rather than `elif`, Python evaluates both conditions independently and prints `GOLD` followed by `SILVER`.
- **B:** Incorrect for this question. Prints `SILVER`. Why the correct answer wins: Because the second check uses a fresh `if` rather than `elif`, Python evaluates both conditions independently and prints `GOLD` followed by `SILVER`.
- **C:** Correct. Prints both `GOLD` and `SILVER` when two independent `if` statements both match. In this case: Because the second check uses a fresh `if` rather than `elif`, Python evaluates both conditions independently and prints `GOLD` followed by `SILVER`.
- **D:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: Because the second check uses a fresh `if` rather than `elif`, Python evaluates both conditions independently and prints `GOLD` followed by `SILVER`.

### Question 15 — A, E

Answers: `0 if subtotal >= 50 else 5`; `'VIP' if points >= 100 else 'STD'`. Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`. Python's conditional expression has the form `<when_true> if <cond> else <when_false>`. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Python's conditional expression has the form `<when_true> if <cond> else <when_false>`. In this case: Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`.
- **B:** Incorrect for this question. Python has no `then` keyword and does not start an inline conditional expression with `if`. Why the correct answer wins: Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`.
- **C:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`.
- **D:** Incorrect for this question. A conditional expression (unlike a list comprehension filter) requires an `else` clause or raises `SyntaxError`. Why the correct answer wins: Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`.
- **E:** Correct. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. In this case: Python's inline conditional syntax is `<true_val> if <cond> else <false_val>`; `? :` syntax, omitting `else`, or writing `if ... then ...` raises `SyntaxError`.

### Question 16 — A, D

Answers: `{}`; `0.0`. An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. Numeric zero `0.0` evaluates to `False` in a Boolean context. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. In this case: An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy.
- **B:** Incorrect for this question. Every non-zero integer, including negative integers such as `-1`, is truthy in Python. Why the correct answer wins: An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy.
- **C:** Incorrect for this question. `(0,)` is a 1-element tuple (`len((0,)) == 1`), so it evaluates to `True` even though its element is `0`. Why the correct answer wins: An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy.
- **D:** Correct. Numeric zero `0.0` evaluates to `False` in a Boolean context. In this case: An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy.
- **E:** Incorrect for this question. `'0'` is a 1-character string (`len('0') == 1`), so it is truthy (`bool('0') is True`). Why the correct answer wins: An empty dictionary `{}` and float zero `0.0` are falsy, whereas non-empty string `'0'`, 1-element tuple `(0,)`, and `-1` are all truthy.

### Question 17 — B

Answer: `WARN`. `pending` (`[]`) has length `0` and is falsy, whereas `currency` (`'0'`) is a 1-character string and therefore truthy, so the `elif` branch prints `WARN`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: `pending` (`[]`) has length `0` and is falsy, whereas `currency` (`'0'`) is a 1-character string and therefore truthy, so the `elif` branch prints `WARN`.
- **B:** Correct. In this case: `pending` (`[]`) has length `0` and is falsy, whereas `currency` (`'0'`) is a 1-character string and therefore truthy, so the `elif` branch prints `WARN`.
- **C:** Incorrect for this question. Prints `OK`. Why the correct answer wins: `pending` (`[]`) has length `0` and is falsy, whereas `currency` (`'0'`) is a 1-character string and therefore truthy, so the `elif` branch prints `WARN`.
- **D:** Incorrect for this question. Prints `ALERT`. Why the correct answer wins: `pending` (`[]`) has length `0` and is falsy, whereas `currency` (`'0'`) is a 1-character string and therefore truthy, so the `elif` branch prints `WARN`.

### Question 18 — B

Answer: `and`. `and` evaluates to `True` only when both the lower-bound and upper-bound comparisons hold simultaneously. `and` is Python's short-circuit logical conjunction operator. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `not` is Python's unary logical negation operator and returns `True` or `False`. Why the correct answer wins: `and` evaluates to `True` only when both the lower-bound and upper-bound comparisons hold simultaneously.
- **B:** Correct. `and` is Python's short-circuit logical conjunction operator. In this case: `and` evaluates to `True` only when both the lower-bound and upper-bound comparisons hold simultaneously.
- **C:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `and` evaluates to `True` only when both the lower-bound and upper-bound comparisons hold simultaneously.
- **D:** Incorrect for this question. `or` is Python's short-circuit logical disjunction operator. Why the correct answer wins: `and` evaluates to `True` only when both the lower-bound and upper-bound comparisons hold simultaneously.

### Question 19 — C

Answer: `'USD'`. Logical `or` returns its first truthy operand (or the right operand if the left is falsy); since `''` is falsy, `'' or 'USD'` evaluates to `'USD'`. Short-circuit `'' or 'USD'` returns the right-hand truthy string `'USD'`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Logical `or` returns its first truthy operand (or the right operand if the left is falsy); since `''` is falsy, `'' or 'USD'` evaluates to `'USD'`.
- **B:** Incorrect for this question. An empty string `''` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: Logical `or` returns its first truthy operand (or the right operand if the left is falsy); since `''` is falsy, `'' or 'USD'` evaluates to `'USD'`.
- **C:** Correct. Short-circuit `'' or 'USD'` returns the right-hand truthy string `'USD'`. In this case: Logical `or` returns its first truthy operand (or the right operand if the left is falsy); since `''` is falsy, `'' or 'USD'` evaluates to `'USD'`.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Logical `or` returns its first truthy operand (or the right operand if the left is falsy); since `''` is falsy, `'' or 'USD'` evaluates to `'USD'`.

### Question 20 — D

Answer: `while`. `while` re-checks `balance < 250` before each iteration and exits once `balance` reaches `250`. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` re-checks `balance < 250` before each iteration and exits once `balance` reaches `250`.
- **B:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `while` re-checks `balance < 250` before each iteration and exits once `balance` reaches `250`.
- **C:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` re-checks `balance < 250` before each iteration and exits once `balance` reaches `250`.
- **D:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` re-checks `balance < 250` before each iteration and exits once `balance` reaches `250`.

### Question 21 — A

Answer: `18`. The loop runs for `step = 3`, `6`, and `9`, adding `3 + 6 + 9 = 18` before `step` becomes `12` and ends the loop. Evaluates to the integer `18`. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `18`. In this case: The loop runs for `step = 3`, `6`, and `9`, adding `3 + 6 + 9 = 18` before `step` becomes `12` and ends the loop.
- **B:** Incorrect for this question. Evaluates to the integer `21`. Why the correct answer wins: The loop runs for `step = 3`, `6`, and `9`, adding `3 + 6 + 9 = 18` before `step` becomes `12` and ends the loop.
- **C:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: The loop runs for `step = 3`, `6`, and `9`, adding `3 + 6 + 9 = 18` before `step` becomes `12` and ends the loop.
- **D:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: The loop runs for `step = 3`, `6`, and `9`, adding `3 + 6 + 9 = 18` before `step` becomes `12` and ends the loop.

### Question 22 — A, E

Answers: `range(2, 10, 2)`; `range(10, 2, -2)`. `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). `range(10, 2, -2)` generates `10, 8, 6, 4` (four integers). Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `range(10, 2, -2)` generates `10, 8, 6, 4` (four integers). In this case: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers.
- **B:** Incorrect for this question. `range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers). Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers.
- **C:** Incorrect for this question. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers.
- **D:** Incorrect for this question. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. Why the correct answer wins: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers.
- **E:** Correct. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). In this case: `range(2, 10, 2)` yields `2, 4, 6, 8` and `range(10, 2, -2)` yields `10, 8, 6, 4`; `range(8, 2)` and `range(2, 8, -2)` are empty, and `range(0, 10, 2)` yields five integers.

### Question 23 — D

Answer: `12`. `range(2, 8, 2)` starts at `2`, steps by `2`, and stops before exclusive `8`, generating `2, 4, 6` whose sum is `12`. Evaluates to the integer `12`. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: `range(2, 8, 2)` starts at `2`, steps by `2`, and stops before exclusive `8`, generating `2, 4, 6` whose sum is `12`.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: `range(2, 8, 2)` starts at `2`, steps by `2`, and stops before exclusive `8`, generating `2, 4, 6` whose sum is `12`.
- **C:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: `range(2, 8, 2)` starts at `2`, steps by `2`, and stops before exclusive `8`, generating `2, 4, 6` whose sum is `12`.
- **D:** Correct. Evaluates to the integer `12`. In this case: `range(2, 8, 2)` starts at `2`, steps by `2`, and stops before exclusive `8`, generating `2, 4, 6` whose sum is `12`.

### Question 24 — D

Answer: `10`. Iterating directly over `'1405'` yields characters `'1'`, `'4'`, `'0'`, and `'5'`, whose integer sum is `10`. Evaluates to the integer `10`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: Iterating directly over `'1405'` yields characters `'1'`, `'4'`, `'0'`, and `'5'`, whose integer sum is `10`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Iterating directly over `'1405'` yields characters `'1'`, `'4'`, `'0'`, and `'5'`, whose integer sum is `10`.
- **C:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Iterating directly over `'1405'` yields characters `'1'`, `'4'`, `'0'`, and `'5'`, whose integer sum is `10`.
- **D:** Correct. Evaluates to the integer `10`. In this case: Iterating directly over `'1405'` yields characters `'1'`, `'4'`, `'0'`, and `'5'`, whose integer sum is `10`.

### Question 25 — A

Answer: `continue`. `continue` skips the rest of the current iteration for negative amounts while advancing the loop to the remaining items. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. In this case: `continue` skips the rest of the current iteration for negative amounts while advancing the loop to the remaining items.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `continue` skips the rest of the current iteration for negative amounts while advancing the loop to the remaining items.
- **C:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `continue` skips the rest of the current iteration for negative amounts while advancing the loop to the remaining items.
- **D:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `continue` skips the rest of the current iteration for negative amounts while advancing the loop to the remaining items.

### Question 26 — D

Answer: `pass`. `pass` satisfies Python's requirement for a non-empty indented suite while performing no runtime action. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Why the correct answer wins: `pass` satisfies Python's requirement for a non-empty indented suite while performing no runtime action.
- **B:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `pass` satisfies Python's requirement for a non-empty indented suite while performing no runtime action.
- **C:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `pass` satisfies Python's requirement for a non-empty indented suite while performing no runtime action.
- **D:** Correct. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. In this case: `pass` satisfies Python's requirement for a non-empty indented suite while performing no runtime action.

### Question 27 — C, D

Answers: When a `for` loop finishes iterating over every element without executing `break`; When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`. A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception. Normal exhaustion of a `for` iterable runs the attached `else:` suite. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `break` bypasses both the remaining iterations AND the loop's `else:` suite. Why the correct answer wins: A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception.
- **B:** Incorrect for this question. An unhandled exception unwinds out of the loop without running its `else:` suite. Why the correct answer wins: A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception.
- **C:** Correct. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. In this case: A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception.
- **D:** Correct. Normal exhaustion of a `for` iterable runs the attached `else:` suite. In this case: A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception.
- **E:** Incorrect for this question. `return` exits the whole function immediately and skips any loop `else:` suite. Why the correct answer wins: A loop's `else:` block runs whenever a `for` loop exhausts its iterable or a `while` condition evaluates to `False` without hitting `break`, `return`, or an unhandled exception.

### Question 28 — C

Answer: `6`. Across `3 * 3 = 9` ordered currency combinations, excluding the `3` identical diagonal pairs (`src == dst`) leaves `6` distinct pairs. Evaluates to the integer `6`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Across `3 * 3 = 9` ordered currency combinations, excluding the `3` identical diagonal pairs (`src == dst`) leaves `6` distinct pairs.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Across `3 * 3 = 9` ordered currency combinations, excluding the `3` identical diagonal pairs (`src == dst`) leaves `6` distinct pairs.
- **C:** Correct. Evaluates to the integer `6`. In this case: Across `3 * 3 = 9` ordered currency combinations, excluding the `3` identical diagonal pairs (`src == dst`) leaves `6` distinct pairs.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: Across `3 * 3 = 9` ordered currency combinations, excluding the `3` identical diagonal pairs (`src == dst`) leaves `6` distinct pairs.

### Question 29 — C

Answer: `[20, 30]`. Slice `quarters[1:3]` starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. Why the correct answer wins: Slice `quarters[1:3]` starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **B:** Incorrect for this question. Slice `[-2:]` returns the last two items `[40, 50]`. Why the correct answer wins: Slice `quarters[1:3]` starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **C:** Correct. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. In this case: Slice `quarters[1:3]` starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Slice `quarters[1:3]` starts at inclusive index `1` (`20`) and stops before exclusive index `3` (`40`), returning `[20, 30]`.

### Question 30 — B

Answer: `[50, 30, 10]`. A negative stride `-2` with omitted bounds starts at the last element (`50`) and steps backward by `2`, yielding `[50, 30, 10]`. Slice `[::-2]` walks backward from the end by `-2`, yielding `[50, 30, 10]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. Why the correct answer wins: A negative stride `-2` with omitted bounds starts at the last element (`50`) and steps backward by `2`, yielding `[50, 30, 10]`.
- **B:** Correct. Slice `[::-2]` walks backward from the end by `-2`, yielding `[50, 30, 10]`. In this case: A negative stride `-2` with omitted bounds starts at the last element (`50`) and steps backward by `2`, yielding `[50, 30, 10]`.
- **C:** Incorrect for this question. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. Why the correct answer wins: A negative stride `-2` with omitted bounds starts at the last element (`50`) and steps backward by `2`, yielding `[50, 30, 10]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: A negative stride `-2` with omitted bounds starts at the last element (`50`) and steps backward by `2`, yielding `[50, 30, 10]`.

### Question 31 — B

Answer: `extend`. `.extend([3, 4])` iterates its argument and appends `3` and `4` individually, whereas `.append([3, 4])` nests the list as one element. `.extend(iterable)` appends each element yielded by `iterable` to the list. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.pop([index])` removes and returns the element at `index` (default `-1`). Why the correct answer wins: `.extend([3, 4])` iterates its argument and appends `3` and `4` individually, whereas `.append([3, 4])` nests the list as one element.
- **B:** Correct. `.extend(iterable)` appends each element yielded by `iterable` to the list. In this case: `.extend([3, 4])` iterates its argument and appends `3` and `4` individually, whereas `.append([3, 4])` nests the list as one element.
- **C:** Incorrect for this question. `.append(item)` adds `item` as a single element at the end of a list. Why the correct answer wins: `.extend([3, 4])` iterates its argument and appends `3` and `4` individually, whereas `.append([3, 4])` nests the list as one element.
- **D:** Incorrect for this question. `.insert(index, item)` places `item` before `index` in the list. Why the correct answer wins: `.extend([3, 4])` iterates its argument and appends `3` and `4` individually, whereas `.append([3, 4])` nests the list as one element.

### Question 32 — A, D

Answers: `items.sort()`; `items.pop()`. `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists. `items.sort()` sorts the list in place and returns `None` rather than a new list. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `items.sort()` sorts the list in place and returns `None` rather than a new list. In this case: `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists.
- **B:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists.
- **C:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists.
- **D:** Correct. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. In this case: `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists.
- **E:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: `items.sort()` reorders `items` in place and `items.pop()` removes its last element in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` build new lists.

### Question 33 — A

Answer: `del`. `del vals[1:4]` deletes the specified slice directly from `vals` in place without returning the removed elements. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. In this case: `del vals[1:4]` deletes the specified slice directly from `vals` in place without returning the removed elements.
- **B:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `del vals[1:4]` deletes the specified slice directly from `vals` in place without returning the removed elements.
- **C:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `del vals[1:4]` deletes the specified slice directly from `vals` in place without returning the removed elements.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `del vals[1:4]` deletes the specified slice directly from `vals` in place without returning the removed elements.

### Question 34 — B, E

Answers: `items[:]`; `items.copy()`. Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`. `items[:]` creates a shallow copy as a new outer list object. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Why the correct answer wins: Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`.
- **B:** Correct. `items[:]` creates a shallow copy as a new outer list object. In this case: Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`.
- **C:** Incorrect for this question. `items.sort()` sorts the list in place and returns `None` rather than a new list. Why the correct answer wins: Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`.
- **D:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`.
- **E:** Correct. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. In this case: Both `items[:]` and `items.copy()` construct a new outer list with the same elements, whereas `backup = items` aliases the same list and `.sort()` / `.pop()` mutate `items`.

### Question 35 — A

Answer: `[0, 4, 16]`. `range(6)` yields `0..5`, `n % 2 == 0` keeps `0, 2, 4`, and squaring each produces `[0, 4, 16]`. Filtering even numbers `0, 2, 4` from `range(6)` and squaring them produces `[0, 4, 16]`. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Filtering even numbers `0, 2, 4` from `range(6)` and squaring them produces `[0, 4, 16]`. In this case: `range(6)` yields `0..5`, `n % 2 == 0` keeps `0, 2, 4`, and squaring each produces `[0, 4, 16]`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `range(6)` yields `0..5`, `n % 2 == 0` keeps `0, 2, 4`, and squaring each produces `[0, 4, 16]`.
- **C:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: `range(6)` yields `0..5`, `n % 2 == 0` keeps `0, 2, 4`, and squaring each produces `[0, 4, 16]`.
- **D:** Incorrect for this question. Filtering odd numbers `1, 3, 5` from `range(6)` and squaring them produces `[1, 9, 25]`. Why the correct answer wins: `range(6)` yields `0..5`, `n % 2 == 0` keeps `0, 2, 4`, and squaring each produces `[0, 4, 16]`.

### Question 36 — C

Answer: `False`. On a dictionary, `in` checks keys (`'EUR'`, `'GBP'`) rather than values (`100`, `120`), so `100 in rates` evaluates to `False`. Evaluates to Boolean `False`. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: On a dictionary, `in` checks keys (`'EUR'`, `'GBP'`) rather than values (`100`, `120`), so `100 in rates` evaluates to `False`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: On a dictionary, `in` checks keys (`'EUR'`, `'GBP'`) rather than values (`100`, `120`), so `100 in rates` evaluates to `False`.
- **C:** Correct. Evaluates to Boolean `False`. In this case: On a dictionary, `in` checks keys (`'EUR'`, `'GBP'`) rather than values (`100`, `120`), so `100 in rates` evaluates to `False`.
- **D:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: On a dictionary, `in` checks keys (`'EUR'`, `'GBP'`) rather than values (`100`, `120`), so `100 in rates` evaluates to `False`.

### Question 37 — B, D

Answers: `(42,)`; `42,`. Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Why the correct answer wins: Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty.
- **B:** Correct. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). In this case: Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty.
- **C:** Incorrect for this question. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty.
- **D:** Correct. Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. In this case: Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty.
- **E:** Incorrect for this question. `tuple()` with no arguments returns the empty 0-element tuple `()`, not a 1-element tuple. Why the correct answer wins: Both `(42,)` and `42,` include a trailing comma that constructs a 1-element `tuple`, whereas `(42)` evaluates to the `int` `42` and `tuple()` is empty.

### Question 38 — B

Answer: `('A', [1, 2, 3])`. Although `entry` is a tuple whose element references cannot be rebound, `entry[1]` refers to a mutable `list`, so `.append(3)` mutates that list in place and prints `('A', [1, 2, 3])`. Although a tuple cannot rebind its slots, mutating an existing list element in place via `t[1].append(3)` succeeds. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Although `entry` is a tuple whose element references cannot be rebound, `entry[1]` refers to a mutable `list`, so `.append(3)` mutates that list in place and prints `('A', [1, 2, 3])`.
- **B:** Correct. Although a tuple cannot rebind its slots, mutating an existing list element in place via `t[1].append(3)` succeeds. In this case: Although `entry` is a tuple whose element references cannot be rebound, `entry[1]` refers to a mutable `list`, so `.append(3)` mutates that list in place and prints `('A', [1, 2, 3])`.
- **C:** Incorrect for this question. `AttributeError` is raised when accessing a method or attribute name that does not exist on that object's type. Why the correct answer wins: Although `entry` is a tuple whose element references cannot be rebound, `entry[1]` refers to a mutable `list`, so `.append(3)` mutates that list in place and prints `('A', [1, 2, 3])`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Although `entry` is a tuple whose element references cannot be rebound, `entry[1]` refers to a mutable `list`, so `.append(3)` mutates that list in place and prints `('A', [1, 2, 3])`.

### Question 39 — C

Answer: `get`. `rates.get('CHF', 0.0)` returns `0.0` when `'CHF'` is absent, whereas direct `rates['CHF']` raises `KeyError`. `d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `d.values()` returns a view of the dictionary's values. Why the correct answer wins: `rates.get('CHF', 0.0)` returns `0.0` when `'CHF'` is absent, whereas direct `rates['CHF']` raises `KeyError`.
- **B:** Incorrect for this question. `d.keys()` returns a view of the dictionary's keys. Why the correct answer wins: `rates.get('CHF', 0.0)` returns `0.0` when `'CHF'` is absent, whereas direct `rates['CHF']` raises `KeyError`.
- **C:** Correct. `d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing. In this case: `rates.get('CHF', 0.0)` returns `0.0` when `'CHF'` is absent, whereas direct `rates['CHF']` raises `KeyError`.
- **D:** Incorrect for this question. `d.items()` returns a view of `(key, value)` pairs. Why the correct answer wins: `rates.get('CHF', 0.0)` returns `0.0` when `'CHF'` is absent, whereas direct `rates['CHF']` raises `KeyError`.

### Question 40 — A

Answer: `6`. `fees.values()` yields a view of the dictionary values `4` and `2`, and `sum(...)` totals them to `6`. Evaluates to the integer `6`. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `6`. In this case: `fees.values()` yields a view of the dictionary values `4` and `2`, and `sum(...)` totals them to `6`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `fees.values()` yields a view of the dictionary values `4` and `2`, and `sum(...)` totals them to `6`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `fees.values()` yields a view of the dictionary values `4` and `2`, and `sum(...)` totals them to `6`.
- **D:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `fees.values()` yields a view of the dictionary values `4` and `2`, and `sum(...)` totals them to `6`.

### Question 41 — C, D

Answers: `'Chef\'s kiss'`; `"Chef's kiss"`. Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal. Backslash-escaping `\'` inside single quotes produces a valid string literal containing an apostrophe. Wrapping a string containing `'` inside double quotes `"..."` needs no backslash escape. Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. An unescaped single quote inside single quotes closes the string early and raises `SyntaxError`. Why the correct answer wins: Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal.
- **B:** Incorrect for this question. Python has no `/* ... */` comment syntax and raises `SyntaxError` if those tokens appear as code. Why the correct answer wins: Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal.
- **C:** Correct. Wrapping a string containing `'` inside double quotes `"..."` needs no backslash escape. In this case: Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal.
- **D:** Correct. Backslash-escaping `\'` inside single quotes produces a valid string literal containing an apostrophe. In this case: Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal.
- **E:** Incorrect for this question. A single trailing backslash escapes the closing quote and raises `SyntaxError`. Why the correct answer wins: Escaping the apostrophe inside single quotes (`'Chef\'s kiss'`) or enclosing the text in double quotes (`"Chef's kiss"`) produces a valid `str` literal.

### Question 42 — A

Answer: `find`. `str.find()` returns `-1` when the target substring is missing, whereas `str.index()` raises `ValueError`. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. In this case: `str.find()` returns `-1` when the target substring is missing, whereas `str.index()` raises `ValueError`.
- **B:** Incorrect for this question. `s.strip()` returns a new string with leading and trailing whitespace removed. Why the correct answer wins: `str.find()` returns `-1` when the target substring is missing, whereas `str.index()` raises `ValueError`.
- **C:** Incorrect for this question. `s.index(sub)` returns the lowest index of `sub`, or raises `ValueError` if `sub` is absent. Why the correct answer wins: `str.find()` returns `-1` when the target substring is missing, whereas `str.index()` raises `ValueError`.
- **D:** Incorrect for this question. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. Why the correct answer wins: `str.find()` returns `-1` when the target substring is missing, whereas `str.index()` raises `ValueError`.

### Question 43 — C

Answer: `TypeError` because `str` objects are immutable and do not support item assignment. Python `str` objects are immutable sequences, so attempting item assignment `code[0] = 'U'` raises `TypeError`. Assigning to `s[0] = ...` raises `TypeError: 'str' object does not support item assignment`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Python `str` objects are immutable sequences, so attempting item assignment `code[0] = 'U'` raises `TypeError`.
- **B:** Incorrect for this question. `.strip()` removes leading and trailing whitespace characters while leaving internal hyphens intact. Why the correct answer wins: Python `str` objects are immutable sequences, so attempting item assignment `code[0] = 'U'` raises `TypeError`.
- **C:** Correct. Assigning to `s[0] = ...` raises `TypeError: 'str' object does not support item assignment`. In this case: Python `str` objects are immutable sequences, so attempting item assignment `code[0] = 'U'` raises `TypeError`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Python `str` objects are immutable sequences, so attempting item assignment `code[0] = 'U'` raises `TypeError`.

### Question 44 — D

Answer: `def`. `def` defines a named function in Python; `function` is not a Python keyword and `lambda` creates anonymous single-expression callables. `def` introduces a named function definition in Python; `function` and `func` are not Python keywords. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `def` defines a named function in Python; `function` is not a Python keyword and `lambda` creates anonymous single-expression callables.
- **B:** Incorrect for this question. `function` is a JavaScript keyword, not a Python keyword; Python uses `def`. Why the correct answer wins: `def` defines a named function in Python; `function` is not a Python keyword and `lambda` creates anonymous single-expression callables.
- **C:** Incorrect for this question. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. Why the correct answer wins: `def` defines a named function in Python; `function` is not a Python keyword and `lambda` creates anonymous single-expression callables.
- **D:** Correct. `def` introduces a named function definition in Python; `function` and `func` are not Python keywords. In this case: `def` defines a named function in Python; `function` is not a Python keyword and `lambda` creates anonymous single-expression callables.

### Question 45 — C

Answer: `None`. After `print(25)` writes to stdout, execution falls off the end of `show_fee`, implicitly returning `None` into `saved`. Evaluates to `None`, Python's singleton null value. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: After `print(25)` writes to stdout, execution falls off the end of `show_fee`, implicitly returning `None` into `saved`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: After `print(25)` writes to stdout, execution falls off the end of `show_fee`, implicitly returning `None` into `saved`.
- **C:** Correct. Evaluates to `None`, Python's singleton null value. In this case: After `print(25)` writes to stdout, execution falls off the end of `show_fee`, implicitly returning `None` into `saved`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: After `print(25)` writes to stdout, execution falls off the end of `show_fee`, implicitly returning `None` into `saved`.

### Question 46 — A

Answer: `yield`. `yield` turns `installments` into a generator function that produces `50`, `100`, and `150` lazily across iterations. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. In this case: `yield` turns `installments` into a generator function that produces `50`, `100`, and `150` lazily across iterations.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `yield` turns `installments` into a generator function that produces `50`, `100`, and `150` lazily across iterations.
- **C:** Incorrect for this question. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Why the correct answer wins: `yield` turns `installments` into a generator function that produces `50`, `100`, and `150` lazily across iterations.
- **D:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `yield` turns `installments` into a generator function that produces `50`, `100`, and `150` lazily across iterations.

### Question 47 — D

Answer: `[]`, because a generator iterator is single-pass and already exhausted after the first `list(g)` call. Generator iterators are single-pass: the first `list(g)` consumes both yielded items (`[1, 2]`), leaving `g` exhausted so the second `list(g)` returns `[]`. Unlike a `list` or `range`, a generator object cannot be rewound; iterating it a second time yields zero elements. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Calling `next()` on an exhausted generator raises `StopIteration`. Why the correct answer wins: Generator iterators are single-pass: the first `list(g)` consumes both yielded items (`[1, 2]`), leaving `g` exhausted so the second `list(g)` returns `[]`.
- **B:** Incorrect for this question. Evaluates to the two-element list `[1, 2]`. Why the correct answer wins: Generator iterators are single-pass: the first `list(g)` consumes both yielded items (`[1, 2]`), leaving `g` exhausted so the second `list(g)` returns `[]`.
- **C:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Generator iterators are single-pass: the first `list(g)` consumes both yielded items (`[1, 2]`), leaving `g` exhausted so the second `list(g)` returns `[]`.
- **D:** Correct. Unlike a `list` or `range`, a generator object cannot be rewound; iterating it a second time yields zero elements. In this case: Generator iterators are single-pass: the first `list(g)` consumes both yielded items (`[1, 2]`), leaving `g` exhausted so the second `list(g)` returns `[]`.

### Question 48 — A

Answer: `10`. `tri(4)` expands to `4 + 3 + 2 + 1 + 0`, terminating at base case `n == 0` and returning `10`. Evaluates to the integer `10`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `10`. In this case: `tri(4)` expands to `4 + 3 + 2 + 1 + 0`, terminating at base case `n == 0` and returning `10`.
- **B:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: `tri(4)` expands to `4 + 3 + 2 + 1 + 0`, terminating at base case `n == 0` and returning `10`.
- **C:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `tri(4)` expands to `4 + 3 + 2 + 1 + 0`, terminating at base case `n == 0` and returning `10`.
- **D:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: `tri(4)` expands to `4 + 3 + 2 + 1 + 0`, terminating at base case `n == 0` and returning `10`.

### Question 49 — C, D

Answers: A reachable base case that returns directly without making another recursive call; A recursive call whose arguments move strictly closer to the base case on each step. Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case. Valid finite recursion requires at least one non-recursive base branch. Without progress toward the base condition, recursion never terminates cleanly. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. Why the correct answer wins: Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case.
- **B:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case.
- **C:** Correct. Valid finite recursion requires at least one non-recursive base branch. In this case: Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case.
- **D:** Correct. Without progress toward the base condition, recursion never terminates cleanly. In this case: Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case.
- **E:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Finite recursion requires at least one non-recursive base case and recursive steps whose arguments converge toward that base case.

### Question 50 — A

Answer: `21`. `amount` receives `20` positionally, `fee` keeps its default `5`, and keyword `discount=4` overrides `2`, returning `20 + 5 - 4 == 21`. Evaluates to the integer `21`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `21`. In this case: `amount` receives `20` positionally, `fee` keeps its default `5`, and keyword `discount=4` overrides `2`, returning `20 + 5 - 4 == 21`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `amount` receives `20` positionally, `fee` keeps its default `5`, and keyword `discount=4` overrides `2`, returning `20 + 5 - 4 == 21`.
- **C:** Incorrect for this question. Evaluates to the integer `23`. Why the correct answer wins: `amount` receives `20` positionally, `fee` keeps its default `5`, and keyword `discount=4` overrides `2`, returning `20 + 5 - 4 == 21`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `amount` receives `20` positionally, `fee` keeps its default `5`, and keyword `discount=4` overrides `2`, returning `20 + 5 - 4 == 21`.

### Question 51 — A, B

Answers: `calc(rate=0.2, base=100)`; `calc(100, rate=0.2)`. `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. In this case: `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail.
- **B:** Correct. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. In this case: `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail.
- **C:** Incorrect for this question. Passing an unknown keyword parameter name `tax` when the signature is `def calc(base, rate):` raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail.
- **D:** Incorrect for this question. Placing positional `0.2` after keyword `base=100` raises `SyntaxError`. Why the correct answer wins: `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail.
- **E:** Incorrect for this question. Passing `100` to `base` positionally and `base=200` by keyword raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` passes both known names by keyword and `calc(100, rate=0.2)` places positional before keyword, whereas positional-after-keyword, duplicate `base`, and unknown `tax` fail.

### Question 52 — B

Answer: `SyntaxError` because a parameter without a default value cannot follow a parameter with a default value. Placing required parameter `subtotal` after defaulted parameter `rate=0.05` violates Python's parameter-order grammar and raises `SyntaxError`. In a `def` signature (`def f(a=1, b):`), required positional-or-keyword parameters must precede parameters with default values. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Placing required parameter `amount` before defaulted parameters `rate=1.1` and `fee=0` is valid Python signature order. Why the correct answer wins: Placing required parameter `subtotal` after defaulted parameter `rate=0.05` violates Python's parameter-order grammar and raises `SyntaxError`.
- **B:** Correct. In a `def` signature (`def f(a=1, b):`), required positional-or-keyword parameters must precede parameters with default values. In this case: Placing required parameter `subtotal` after defaulted parameter `rate=0.05` violates Python's parameter-order grammar and raises `SyntaxError`.
- **C:** Incorrect for this question. `NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Placing required parameter `subtotal` after defaulted parameter `rate=0.05` violates Python's parameter-order grammar and raises `SyntaxError`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Placing required parameter `subtotal` after defaulted parameter `rate=0.05` violates Python's parameter-order grammar and raises `SyntaxError`.

### Question 53 — A

Answer: `[1, 2]`. Default list `acc=[]` is created once at `def` time and shared across calls that omit `acc`, so after `log_tx(1)` appends `1`, `log_tx(2)` appends `2` and returns `[1, 2]`. Evaluates to the two-element list `[1, 2]`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the two-element list `[1, 2]`. In this case: Default list `acc=[]` is created once at `def` time and shared across calls that omit `acc`, so after `log_tx(1)` appends `1`, `log_tx(2)` appends `2` and returns `[1, 2]`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Default list `acc=[]` is created once at `def` time and shared across calls that omit `acc`, so after `log_tx(1)` appends `1`, `log_tx(2)` appends `2` and returns `[1, 2]`.
- **C:** Incorrect for this question. Evaluates to the single-element list `[2]`. Why the correct answer wins: Default list `acc=[]` is created once at `def` time and shared across calls that omit `acc`, so after `log_tx(1)` appends `1`, `log_tx(2)` appends `2` and returns `[1, 2]`.
- **D:** Incorrect for this question. Evaluates to the single-element list `[1]`. Why the correct answer wins: Default list `acc=[]` is created once at `def` time and shared across calls that omit `acc`, so after `log_tx(1)` appends `1`, `log_tx(2)` appends `2` and returns `[1, 2]`.

### Question 54 — B

Answer: `global`. `global budget_cap` tells Python that assignments to `budget_cap` inside `raise_cap` target the module-level variable. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `global budget_cap` tells Python that assignments to `budget_cap` inside `raise_cap` target the module-level variable.
- **B:** Correct. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. In this case: `global budget_cap` tells Python that assignments to `budget_cap` inside `raise_cap` target the module-level variable.
- **C:** Incorrect for this question. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. Why the correct answer wins: `global budget_cap` tells Python that assignments to `budget_cap` inside `raise_cap` target the module-level variable.
- **D:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `global budget_cap` tells Python that assignments to `budget_cap` inside `raise_cap` target the module-level variable.

### Question 55 — A, E

Answers: Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`; Calling `.append()` on a module-level list inside a function mutates that list in place without needing `global`. Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. Method calls mutate an existing object rather than rebinding the variable name, so Python resolves the name in module scope. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Method calls mutate an existing object rather than rebinding the variable name, so Python resolves the name in module scope. In this case: Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`.
- **B:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`.
- **C:** Incorrect for this question. Python determines local names at compile time; reading `x` before a later `x += 1` or `x = ...` in the same function raises `UnboundLocalError`. Why the correct answer wins: Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`.
- **D:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`.
- **E:** Correct. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. In this case: Reading a module-level variable without assigning to it and mutating a module-level list in place via `.append()` both resolve the module name via LEGB without needing `global`.

### Question 56 — B

Answer: `ArithmeticError`. `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`.
- **B:** Correct. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. In this case: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`.
- **D:** Incorrect for this question. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Why the correct answer wins: `ZeroDivisionError` inherits directly from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`.

### Question 57 — C, E

Answers: `SystemExit`; `KeyboardInterrupt`. `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts. `SystemExit` inherits directly from `BaseException` (NOT `Exception`) so `except Exception:` does not accidentally swallow `sys.exit()`. `KeyboardInterrupt` inherits directly from `BaseException` (NOT `Exception`) so Ctrl-C interrupts are not swallowed by `except Exception:`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts.
- **B:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts.
- **C:** Correct. `SystemExit` inherits directly from `BaseException` (NOT `Exception`) so `except Exception:` does not accidentally swallow `sys.exit()`. In this case: `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts.
- **E:** Correct. `KeyboardInterrupt` inherits directly from `BaseException` (NOT `Exception`) so Ctrl-C interrupts are not swallowed by `except Exception:`. In this case: `SystemExit` and `KeyboardInterrupt` subclass `BaseException` directly so normal error handlers do not swallow interpreter exit or user interrupts.

### Question 58 — D

Answer: `raise`. `raise` instantiates or triggers the specified exception object and begins stack unwinding. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Why the correct answer wins: `raise` instantiates or triggers the specified exception object and begins stack unwinding.
- **B:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `raise` instantiates or triggers the specified exception object and begins stack unwinding.
- **C:** Incorrect for this question. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. Why the correct answer wins: `raise` instantiates or triggers the specified exception object and begins stack unwinding.
- **D:** Correct. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. In this case: `raise` instantiates or triggers the specified exception object and begins stack unwinding.

### Question 59 — A

Answer: `ValueError`. `'45.00'` has the valid type `str`, so `int()` accepts the type yet rejects the non-integer character `'.'` with `ValueError`. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). In this case: `'45.00'` has the valid type `str`, so `int()` accepts the type yet rejects the non-integer character `'.'` with `ValueError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `'45.00'` has the valid type `str`, so `int()` accepts the type yet rejects the non-integer character `'.'` with `ValueError`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `'45.00'` has the valid type `str`, so `int()` accepts the type yet rejects the non-integer character `'.'` with `ValueError`.
- **D:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `'45.00'` has the valid type `str`, so `int()` accepts the type yet rejects the non-integer character `'.'` with `ValueError`.

### Question 60 — D

Answer: `T-E-F`. Because `20 // 5` succeeds without raising an exception, `except` is skipped, `else` appends `'E'`, and `finally` appends `'F'`, printing `T-E-F`. When no exception occurs in `try:`, Python runs `try` (`T`), then `else` (`E`), and finally `finally` (`F`), skipping `except`. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Would omit either `else` (on success) or `except` (on caught failure). Why the correct answer wins: Because `20 // 5` succeeds without raising an exception, `except` is skipped, `else` appends `'E'`, and `finally` appends `'F'`, printing `T-E-F`.
- **B:** Incorrect for this question. When `try:` raises a caught exception after printing `T`, Python runs the matching `except` (`X`) and then `finally` (`F`), skipping `else`. Why the correct answer wins: Because `20 // 5` succeeds without raising an exception, `except` is skipped, `else` appends `'E'`, and `finally` appends `'F'`, printing `T-E-F`.
- **C:** Incorrect for this question. `except:` and `else:` are mutually exclusive on any single execution of a `try` statement. Why the correct answer wins: Because `20 // 5` succeeds without raising an exception, `except` is skipped, `else` appends `'E'`, and `finally` appends `'F'`, printing `T-E-F`.
- **D:** Correct. When no exception occurs in `try:`, Python runs `try` (`T`), then `else` (`E`), and finally `finally` (`F`), skipping `except`. In this case: Because `20 // 5` succeeds without raising an exception, `except` is skipped, `else` appends `'E'`, and `finally` appends `'F'`, printing `T-E-F`.
