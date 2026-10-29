# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 3

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 17 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A cinema kiosk script prints `'Welcome to Gate 4'` on line 1, reserves a counter in memory on line 2, and hits an unhandled `ZeroDivisionError` on line 3. How does standard CPython behave?

- A. CPython executes `.py` source only inside an HTML5 browser DOM engine
- B. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes
- C. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- D. When an unhandled runtime error occurs, CPython halts execution at the failing bytecode step after running earlier statements

### 2. In a seat-pricing script, a developer accidentally types `price = 0o19` using digit `9` inside an octal literal. Because `0o19` cannot even be formed into a valid Python token, which error layer is violated first?

- A. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- B. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- C. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning
- D. A lexical error because the character or token itself does not belong to valid Python token forms

### 3. A developer writing a concert-ticket reservation module chooses variable names for error counters. Which two names are hard reserved keywords in Python 3 and cannot be assigned as variable names? Select two.

- A. `none`
- B. `dict`
- C. `match`
- D. `finally`
- E. `except`

### 4. A turnstile gate controller encodes aisle bitmasks using non-decimal integer literals. Which two literals are valid integer literals in Python 3? Select two.

- A. `1__000`
- B. `0x1G`
- C. `0b1101`
- D. `0o27`
- E. `0b102`

### 5. When naming variables in a seat-map script, which two identifiers are syntactically valid variable names in Python 3 (even if shadowing built-ins is discouraged)? Select two.

- A. `2nd_quarter`
- B. `row_14_a`
- C. `max`
- D. `assert`
- E. `seat count`

### 6. Complete `avg_group = 18 ____ 6` in a shuttle boarding script so `avg_group` evaluates to the `float` `3.0` rather than the `int` `3`. Which operator fills the blank?

- A. `//`
- B. `**`
- C. `/`
- D. `%`

### 7. A coach-seating calculation evaluates `seats = 20 // 3 * 2`. Because `//` and `*` share the same precedence tier, what integer is assigned to `seats`?

- A. `3.0`
- B. `12`
- C. `3`
- D. `13`

### 8. Complete `zone_id = 28 ____ 2` in a stadium ticket decoder so shifting bits right by two places floor-divides `28` by `4` to yield `7`. Which bitwise operator fills the blank?

- A. `~`
- B. `&`
- C. `<<`
- D. `>>`

### 9. Complete `waitlist = 14; waitlist ____ 5` so adding five late arrivals updates `waitlist` in place to `19`. Which augmented assignment operator fills the blank?

- A. `//=`
- B. `%`
- C. `*=`
- D. `+=`

### 10. A boarding-pass printer runs `print('A', 'B', sep='-', end='/')` followed on the next line by `print('C')`. What text is written to standard output?

- A. `A-B` on line 1 and `C` on line 2
- B. `A B/C`
- C. `TypeError`
- D. `A-B/C`

### 11. Complete `party_size = ____(input('Guests: '))` so typing `4` at the terminal stores the integer `4` (`int`) rather than `'4'` (`str`) or `4.0` (`float`). Which built-in callable fills the blank?

- A. `str`
- B. `bool`
- C. `int`
- D. `float`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete the cabin fare selector `if age < 12: fare = 8` / `____ age >= 65: fare = 10` / `else: fare = 15` so senior passengers pay `10` while adults pay `15`. Which keyword fills the blank?

- A. `elif`
- B. `else`
- C. `for`
- D. `with`

### 13. A stadium loyalty gate sets `visits = 4` and runs `if visits >= 20: print('GOLD')` / `elif visits >= 10: print('SILVER')` / `elif visits >= 3: print('BRONZE')` / `else: print('GUEST')`. What is printed?

- A. Nothing is printed
- B. `BRONZE`
- C. `SILVER`
- D. `GOLD`

### 14. A booking cart sets `subtotal = 35` and evaluates `booking_fee = 0 if subtotal >= 50 else 5`. What integer is assigned to `booking_fee`?

- A. `False`
- B. `SyntaxError`
- C. `5`
- D. `0`

### 15. A baggage surcharge script sets `weight = 28; fee = 10` and runs two independent `if` blocks: `if weight > 20: fee += 2` followed by `if weight > 25: fee += 5`. What is `fee` afterward?

- A. `17`
- B. `12`
- C. `10`
- D. `15`

### 16. A waitlist dispatcher checks `if queue_state:` before paging a kiosk. Which two values of `queue_state` evaluate to `False`? Select two.

- A. `' '`
- B. `()`
- C. `[]`
- D. `(0,)`
- E. `{0: None}`

### 17. A seat-hold check sets `reserved = (0,)` and runs `if reserved: print('OK')` / `else: print('IDLE')`. What does it print?

- A. Nothing is printed
- B. `OK`
- C. `TypeError`
- D. `IDLE`

### 18. Complete `if vip_pass ____ promo_code == 'EARLY': allow_entry()` so boarding is granted whenever at least one of the two conditions is truthy. Which logical operator fills the blank?

- A. `or`
- B. `and`
- C. `not`
- D. `in`

### 19. A kiosk gate evaluates `allowed = True or False and False` without parentheses. Because `and` has higher precedence than `or`, what Boolean value is bound to `allowed`?

- A. `False`
- B. `TypeError`
- C. `True`
- D. `0`

### 20. Complete `seats_left = 6` / `____ seats_left > 0:` / `    seats_left -= 2` so tickets are allocated in pairs until `seats_left` reaches `0`. Which keyword fills the blank?

- A. `while`
- B. `except`
- C. `elif`
- D. `for`

### 21. A queue worker inspects five `while` loops that drain ticket batches. Which two loops are guaranteed to terminate after finitely many steps? Select two.

- A. `n = 16` followed by `while n >= 2: n //= 2`
- B. `n = 4` followed by `while n % 2 == 0: n += 2`
- C. `n = 1` followed by `while n > 0: n += 1`
- D. `n = 6` followed by `while n > 0: n -= 2`
- E. `n = 5` followed by `while n > 0: pass`

### 22. Complete `____ row_num in range(1, 11):` / `    assign_row(row_num)` so `row_num` takes each integer `1` through `10` in turn. Which keyword fills the blank?

- A. `while`
- B. `from`
- C. `with`
- D. `for`

### 23. A seat-numbering script accidentally passes mismatched start, stop, and step bounds to `range()`. Which two `range()` calls produce zero iterations? Select two.

- A. `range(2, 10, 2)`
- B. `range(0, 10, 2)`
- C. `range(2, 8, -2)`
- D. `range(3, 12, 3)`
- E. `range(8, 2)`

### 24. A voucher-code analyzer runs `vowels = 0` / `for ch in 'QUEUE1':` / `    if ch in 'AEIOU': vowels += 1` / `print(vowels)`. What integer is printed?

- A. `2`
- B. `4`
- C. `TypeError`
- D. `6`

### 25. Complete `for seat in ['1A', '1B', 'OPEN', '1D']:` / `    if seat == 'OPEN': chosen = seat; ____` so the seat finder stops scanning as soon as `'OPEN'` is matched. Which keyword fills the blank?

- A. `break`
- B. `pass`
- C. `return`
- D. `continue`

### 26. A shuttle capacity counter runs `total = 0` / `for grp in [3, 6, 5]:` / `    if grp > 5: continue` / `    total += grp` / `print(total)`. What integer is printed?

- A. `6`
- B. `8`
- C. `14`
- D. `2`

### 27. A manifest scanner attaches an `else:` block to its passenger lookup loop. Under which two outcomes does Python execute that loop `else:` block? Select two.

- A. When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`
- B. Whenever an unhandled exception aborts the loop body
- C. Immediately after a `break` statement jumps out of the loop body
- D. When a `for` loop finishes iterating over every element without executing `break`
- E. Right before a `return` statement inside the loop exits the enclosing function

### 28. A ferry cabin generator sets `berths = 0` and runs `for deck in range(3):` / `    for slot in range(4): berths += 1` / `print(berths)`. What integer is printed?

- A. `6`
- B. `7`
- C. `12`
- D. `16`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. A boarding queue stores `coaches = [10, 20, 30, 40, 50]`. What list is returned by `coaches[-2:]`?

- A. `[40, 50]`
- B. `[20, 30]`
- C. `IndexError`
- D. `[10, 30, 50]`

### 30. Given `coaches = [10, 20, 30, 40, 50]`, what happens when a seat lookup evaluates `coaches[5]`?

- A. `48`
- B. `[]`
- C. `None`
- D. `IndexError`

### 31. Complete `next_guest = waitlist.____(0)` so the element at index `0` is removed from `waitlist` and returned into `next_guest`. Which list method name fills the blank?

- A. `append`
- B. `pop`
- C. `extend`
- D. `insert`

### 32. A gate agent manages `items = ['B2', 'C3', 'D4']`. Which two operations mutate the existing `items` list object in place? Select two.

- A. `items[:]`
- B. `items.remove(x)`
- C. `items.insert(0, x)`
- D. `sorted(items)`
- E. `items + [x]`

### 33. Complete `remaining = ____(seat_pool)` after `del seat_pool[:2]` so `remaining` receives the integer count of elements left in `seat_pool`. Which built-in function name fills the blank?

- A. `len`
- B. `str`
- C. `sorted`
- D. `int`

### 34. A seat-booking worker wants a shallow copy of flat list `items = [1, 2, 3]` so popping from the copy leaves `items` intact. Which two expressions build a shallow copy? Select two.

- A. `list(items)`
- B. `backup = items`
- C. `items[:]`
- D. `items.remove(x)`
- E. `items.pop()`

### 35. What list does `[k ** 2 for k in range(6) if k % 2 == 1]` evaluate to in a seat-zone weight table?

- A. `[]`
- B. `[0, 4, 16]`
- C. `[1, 9, 25]`
- D. `SyntaxError`

### 36. Complete `if 'VIP' ____ ticket_code: open_fast_lane()` so the fast lane opens whenever `'VIP'` appears as a substring of `ticket_code`. Which operator fills the blank?

- A. `and`
- B. `for`
- C. `is`
- D. `in`

### 37. A seat coordinate helper wraps integer `42` into a 1-element `tuple`. Which two expressions create a `tuple` of length `1`? Select two.

- A. `(42,)`
- B. `42,`
- C. `[]`
- D. `tuple()`
- E. `(42)`

### 38. A manifest stores `row_data = ('Row1', [10, 20])`, executes `row_data[1].append(30)`, and prints `len(row_data[1])`. What happens?

- A. `AttributeError`
- B. `TypeError`
- C. `3`
- D. `2`

### 39. A booth counter stores `sold = {'VIP': 12, 'GA': 40}` and evaluates `print(sold.pop('BALCONY', 0))`. What happens?

- A. `1`
- B. `None`
- C. `0`
- D. `KeyError`

### 40. A kiosk dashboard inspects seat counts stored in dictionary `d`. Which two statements accurately describe `d.values()` and `d.keys()` in Python 3? Select two.

- A. `.values()` yields every stored value in insertion order
- B. `.keys()` yields every key in insertion order
- C. Membership `k in d` checks both keys and values simultaneously
- D. `(42)`
- E. `backup = items`

### 41. A ticket printer defines raw string `tag = r'A\nB'` and evaluates `len(tag)`. What integer does `len(tag)` return?

- A. `SyntaxError`
- B. `5`
- C. `3`
- D. `4`

### 42. Complete `clean_seat = raw_seat.____('-', '')` so `'14-A'` produces the new string `'14A'`. Which string method name fills the blank?

- A. `strip`
- B. `replace`
- C. `split`
- D. `find`

### 43. A gate-sorting check evaluates `print('9' < 'A' < 'a')`. What does Python print and why?

- A. `True`, because code-point order places digits (`'0'`–`'9'`) before uppercase (`'A'`–`'Z'`) and uppercase before lowercase (`'a'`–`'z'`)
- B. `TypeError`
- C. `False`, because Python compares strings case-insensitively by alphabetical order
- D. `None`

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Complete `def seat_price(zone):` / `    if zone == 'VIP': ____ 120` / `    return 45` so calling `seat_price('VIP')` immediately hands back `120` to the caller. Which keyword fills the blank?

- A. `pass`
- B. `yield`
- C. `return`
- D. `break`

### 45. A helper defines `def bounds(): return 1, 30` with a comma between `1` and `30`. What does calling `bounds()` return?

- A. Returning `a, b` packs and returns a 2-element `tuple` `(a, b)` that the caller can unpack
- B. `SyntaxError`
- C. `TypeError`
- D. `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`

### 46. Complete `def boarding_groups():` / `    for grp in ('A', 'B', 'C'):` / `        ____ grp` so iterating `boarding_groups()` lazily produces `'A'`, `'B'`, and `'C'` one at a time. Which keyword fills the blank?

- A. `from`
- B. `yield`
- C. `return`
- D. `continue`

### 47. A kiosk helper defines `def one_pass(): yield 'P1'`, binds `it = one_pass()`, consumes `next(it)`, and then calls `next(it)` a second time with no default argument. Which exception is raised?

- A. `StopIteration`
- B. `ValueError`
- C. `IndexError`
- D. `None`

### 48. A binary seat-halving helper defines `def two_pow(e): return 1 if e == 0 else 2 * two_pow(e - 1)` and evaluates `two_pow(3)`. What integer is returned?

- A. `RecursionError`
- B. `6`
- C. `8`
- D. `16`

### 49. A seat-allocation tree routine uses recursion. Which two conditions are needed so recursive calls finish without triggering `RecursionError`? Select two.

- A. A recursive call whose arguments move strictly closer to the base case on each step
- B. A reachable base case that returns directly without making another recursive call
- C. Declaring every parameter `global` inside the function header
- D. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- E. Replacing every `return` statement with `break` inside the `def` body

### 50. A kiosk defines `def book(row, seat): return f'{row}{seat}'` with two required parameters and a caller invokes `book(14)` with only one argument. Which exception is raised?

- A. `SyntaxError`
- B. `None`
- C. `TypeError`
- D. `10`

### 51. A ticket fee helper defines `def calc(base, rate): return base + rate`. Which two call expressions invoke `calc` without raising `SyntaxError` or `TypeError`? Select two.

- A. `calc(rate=0.2, base=100)`
- B. `calc(100, tax=0.2)`
- C. `calc(base=100, 0.2)`
- D. `calc(100, base=200)`
- E. `calc(100, rate=0.2)`

### 52. Given `def hold_fee(tickets, per_ticket=5): return tickets * per_ticket`, what integer does `hold_fee(3)` return?

- A. `TypeError`
- B. `15`
- C. `25`
- D. `10`

### 53. A baggage pricing helper defines `def allowance(passengers, bags_each=1): return passengers * bags_each`. When an agent calls `allowance(3, 2)` with an explicit second argument, which integer is returned?

- A. `TypeError`
- B. `SyntaxError`
- C. `15`
- D. `6`

### 54. Complete `issued_count = 0` / `def issue_one():` / `    ____ issued_count` / `    issued_count += 1` so calling `issue_one()` increments module-level `issued_count` to `1`. Which keyword fills the blank?

- A. `nonlocal`
- B. `global`
- C. `pass`
- D. `with`

### 55. When a ticket script defines module-level variables and plain top-level functions, which two statements accurately describe Python's LEGB variable lookup? Select two.

- A. Declaring every parameter `global` inside the function header
- B. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- C. Assigning to a name inside a function without `global` creates a separate local variable, leaving the module-level variable unchanged
- D. Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`
- E. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects

### 56. An agent writes `except LookupError:` around `seat_map[row][col]` where `seat_map` is a `dict` of `list` objects. Why does that single handler catch both missing `row` keys and out-of-range `col` indices?

- A. `LookupError`
- B. `ValueError`
- C. `ArithmeticError`
- D. `SyntaxError`

### 57. In Python's exception tree, which built-in exception is a direct subclass of `NameError` raised specifically inside functions when a local name is read before assignment?

- A. `KeyError`
- B. `UnboundLocalError`
- C. `IndexError`
- D. `ZeroDivisionError`

### 58. Complete `if seats_requested > capacity:` / `    ____ ValueError('capacity exceeded')` so overbooking immediately signals `ValueError`. Which keyword fills the blank?

- A. `raise`
- B. `except`
- C. `pass`
- D. `finally`

### 59. A gate lookup stores `gates = {'FL10': 'B4'}` and evaluates `gates['FL99']` directly with square brackets. Which exception is raised?

- A. `ValueError`
- B. `IndexError`
- C. `TypeError`
- D. `KeyError`

### 60. A seat reservation block uses `try / except / else / finally`. Which two statements accurately describe when `else:` and `finally:` execute? Select two.

- A. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes
- B. `T-X-E-F`
- C. The `finally:` block always runs on the way out — whether `try:` succeeded, an `except:` ran, an uncaught exception propagated, or `return` executed
- D. The `else:` block runs only when the `try:` block completes normally without raising an exception
- E. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects

---

## Answer key and explanations

### Question 1 — D

Answer: When an unhandled runtime error occurs, CPython halts execution at the failing bytecode step after running earlier statements. Because CPython executes bytecode sequentially at runtime without transaction rollback, `'Welcome to Gate 4'` has already been printed before execution halts at line 3 with a traceback. Because CPython executes top-to-bottom at runtime, side effects from earlier statements have already happened when a later line raises an unhandled exception. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. CPython is a native host process written in C, not a browser-embedded DOM engine. Why the correct answer wins: Because CPython executes bytecode sequentially at runtime without transaction rollback, `'Welcome to Gate 4'` has already been printed before execution halts at line 3 with a traceback.
- **B:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Because CPython executes bytecode sequentially at runtime without transaction rollback, `'Welcome to Gate 4'` has already been printed before execution halts at line 3 with a traceback.
- **C:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Because CPython executes bytecode sequentially at runtime without transaction rollback, `'Welcome to Gate 4'` has already been printed before execution halts at line 3 with a traceback.
- **D:** Correct. Because CPython executes top-to-bottom at runtime, side effects from earlier statements have already happened when a later line raises an unhandled exception. In this case: Because CPython executes bytecode sequentially at runtime without transaction rollback, `'Welcome to Gate 4'` has already been printed before execution halts at line 3 with a traceback.

### Question 2 — D

Answer: A lexical error because the character or token itself does not belong to valid Python token forms. Digit `9` is outside the legal octal alphabet `0`–`7`, so the scanner rejects the malformed token at the lexical layer before grammar or runtime checks apply. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Why the correct answer wins: Digit `9` is outside the legal octal alphabet `0`–`7`, so the scanner rejects the malformed token at the lexical layer before grammar or runtime checks apply.
- **B:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Digit `9` is outside the legal octal alphabet `0`–`7`, so the scanner rejects the malformed token at the lexical layer before grammar or runtime checks apply.
- **C:** Incorrect for this question. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Why the correct answer wins: Digit `9` is outside the legal octal alphabet `0`–`7`, so the scanner rejects the malformed token at the lexical layer before grammar or runtime checks apply.
- **D:** Correct. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. In this case: Digit `9` is outside the legal octal alphabet `0`–`7`, so the scanner rejects the malformed token at the lexical layer before grammar or runtime checks apply.

### Question 3 — D, E

Answers: `except`; `finally`. `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Only capitalized `None` is a reserved keyword; lowercase `none` is a valid variable name. Why the correct answer wins: `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved.
- **B:** Incorrect for this question. `dict` is a built-in type name in `builtins`, not a reserved keyword. Why the correct answer wins: `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved.
- **C:** Incorrect for this question. `match` is a soft keyword in Python 3.10+, so unlike hard keywords it remains usable as a variable identifier. Why the correct answer wins: `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved.
- **D:** Correct. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. In this case: `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved.
- **E:** Correct. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. In this case: `except` and `finally` are hard keywords in Python 3, whereas `match` is a soft keyword, `dict` is a built-in type identifier, and lowercase `none` is not reserved.

### Question 4 — C, D

Answers: `0b1101`; `0o27`. `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`. `0b1101` is a valid binary integer literal equal to `8 + 4 + 0 + 1 == 13`. `0o27` is a valid octal integer literal equal to `2 * 8 + 7 == 23`. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Consecutive underscores inside a numeric literal (`1__000`) raise `SyntaxError`. Why the correct answer wins: `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`.
- **B:** Incorrect for this question. Hexadecimal digits stop at `F`/`f`, so `0x1G` raises `SyntaxError`. Why the correct answer wins: `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`.
- **C:** Correct. `0b1101` is a valid binary integer literal equal to `8 + 4 + 0 + 1 == 13`. In this case: `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`.
- **D:** Correct. `0o27` is a valid octal integer literal equal to `2 * 8 + 7 == 23`. In this case: `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`.
- **E:** Incorrect for this question. Binary literals allow only `0` and `1`, so `2` in `0b102` raises `SyntaxError`. Why the correct answer wins: `0b1101` (`13` in binary) and `0o27` (`23` in octal) use legal base prefixes and digits, whereas `0b102`, `1__000`, and `0x1G` raise `SyntaxError`.

### Question 5 — B, C

Answers: `row_14_a`; `max`. `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword. `row_14_a` starts with an ASCII letter and contains only letters, digits, and underscores. `max` is a built-in function identifier, not a hard keyword in Python 3. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier. Why the correct answer wins: `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword.
- **B:** Correct. `row_14_a` starts with an ASCII letter and contains only letters, digits, and underscores. In this case: `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword.
- **C:** Correct. `max` is a built-in function identifier, not a hard keyword in Python 3. In this case: `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword.
- **D:** Incorrect for this question. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. Why the correct answer wins: `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword.
- **E:** Incorrect for this question. Whitespace separates tokens and cannot appear inside a single variable name. Why the correct answer wins: `row_14_a` is a clean snake_case identifier and `max` is a legal non-keyword identifier, whereas `seat count` has a space, `2nd_quarter` starts with a digit, and `assert` is a hard keyword.

### Question 6 — C

Answer: `/`. In Python 3, true division `/` always returns a `float` (`18 / 6 == 3.0`), whereas floor division `//` returns `int` `3` when both operands are `int`. Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: In Python 3, true division `/` always returns a `float` (`18 / 6 == 3.0`), whereas floor division `//` returns `int` `3` when both operands are `int`.
- **B:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: In Python 3, true division `/` always returns a `float` (`18 / 6 == 3.0`), whereas floor division `//` returns `int` `3` when both operands are `int`.
- **C:** Correct. In this case: In Python 3, true division `/` always returns a `float` (`18 / 6 == 3.0`), whereas floor division `//` returns `int` `3` when both operands are `int`.
- **D:** Incorrect for this question. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Why the correct answer wins: In Python 3, true division `/` always returns a `float` (`18 / 6 == 3.0`), whereas floor division `//` returns `int` `3` when both operands are `int`.

### Question 7 — B

Answer: `12`. Operators `//` and `*` associate left to right: Python computes `20 // 3` (`6`) first and then `6 * 2`, assigning `12` rather than `20 // (3 * 2) == 3`. Evaluates to the integer `12`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the floating-point value `3.0`. Why the correct answer wins: Operators `//` and `*` associate left to right: Python computes `20 // 3` (`6`) first and then `6 * 2`, assigning `12` rather than `20 // (3 * 2) == 3`.
- **B:** Correct. Evaluates to the integer `12`. In this case: Operators `//` and `*` associate left to right: Python computes `20 // 3` (`6`) first and then `6 * 2`, assigning `12` rather than `20 // (3 * 2) == 3`.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Operators `//` and `*` associate left to right: Python computes `20 // 3` (`6`) first and then `6 * 2`, assigning `12` rather than `20 // (3 * 2) == 3`.
- **D:** Incorrect for this question. Evaluates to the integer `13`. Why the correct answer wins: Operators `//` and `*` associate left to right: Python computes `20 // 3` (`6`) first and then `6 * 2`, assigning `12` rather than `20 // (3 * 2) == 3`.

### Question 8 — D

Answer: `>>`. Right shift `28 >> 2` shifts the binary representation two bits right, computing `28 // (2 ** 2) == 7`. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Bitwise inversion `~x` flips all bits in two's-complement arithmetic and equals `-(x + 1)`. Why the correct answer wins: Right shift `28 >> 2` shifts the binary representation two bits right, computing `28 // (2 ** 2) == 7`.
- **B:** Incorrect for this question. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. Why the correct answer wins: Right shift `28 >> 2` shifts the binary representation two bits right, computing `28 // (2 ** 2) == 7`.
- **C:** Incorrect for this question. Left shift `x << n` multiplies integer `x` by `2 ** n`. Why the correct answer wins: Right shift `28 >> 2` shifts the binary representation two bits right, computing `28 // (2 ** 2) == 7`.
- **D:** Correct. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. In this case: Right shift `28 >> 2` shifts the binary representation two bits right, computing `28 // (2 ** 2) == 7`.

### Question 9 — D

Answer: `+=`. `waitlist += 5` adds `5` to `14` and rebinds `waitlist` to `19`. `+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable. Why the correct answer wins: `waitlist += 5` adds `5` to `14` and rebinds `waitlist` to `19`.
- **B:** Incorrect for this question. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Why the correct answer wins: `waitlist += 5` adds `5` to `14` and rebinds `waitlist` to `19`.
- **C:** Incorrect for this question. `*=` scales a number or repeats a sequence in place / by rebinding. Why the correct answer wins: `waitlist += 5` adds `5` to `14` and rebinds `waitlist` to `19`.
- **D:** Correct. `+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets. In this case: `waitlist += 5` adds `5` to `14` and rebinds `waitlist` to `19`.

### Question 10 — D

Answer: `A-B/C`. The first `print()` joins `'A'` and `'B'` with `'-'` and finishes with `'/'` instead of a newline, so the second `print('C')` appends `C` immediately after `'/'` to output `A-B/C`. First `print('A', 'B', sep='-', end='/')` writes `A-B/`, and the second `print('C')` appends `C` on the same line. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. A line break between `B` and `C` appears only when `end` is left at its default newline. Why the correct answer wins: The first `print()` joins `'A'` and `'B'` with `'-'` and finishes with `'/'` instead of a newline, so the second `print('C')` appends `C` immediately after `'/'` to output `A-B/C`.
- **B:** Incorrect for this question. That output would occur only if `sep` were left at its default single space. Why the correct answer wins: The first `print()` joins `'A'` and `'B'` with `'-'` and finishes with `'/'` instead of a newline, so the second `print('C')` appends `C` immediately after `'/'` to output `A-B/C`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: The first `print()` joins `'A'` and `'B'` with `'-'` and finishes with `'/'` instead of a newline, so the second `print('C')` appends `C` immediately after `'/'` to output `A-B/C`.
- **D:** Correct. First `print('A', 'B', sep='-', end='/')` writes `A-B/`, and the second `print('C')` appends `C` on the same line. In this case: The first `print()` joins `'A'` and `'B'` with `'-'` and finishes with `'/'` instead of a newline, so the second `print('C')` appends `C` immediately after `'/'` to output `A-B/C`.

### Question 11 — C

Answer: `int`. `int(...)` parses a base-10 integer string from `input()` into an `int` suitable for list indexing and integer arithmetic. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. Why the correct answer wins: `int(...)` parses a base-10 integer string from `input()` into an `int` suitable for list indexing and integer arithmetic.
- **B:** Incorrect for this question. `bool(...)` tests truthiness; for ANY non-empty string — including `'0'` and `'False'` — `bool(...)` returns `True`. Why the correct answer wins: `int(...)` parses a base-10 integer string from `input()` into an `int` suitable for list indexing and integer arithmetic.
- **C:** Correct. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. In this case: `int(...)` parses a base-10 integer string from `input()` into an `int` suitable for list indexing and integer arithmetic.
- **D:** Incorrect for this question. `float(...)` parses a numeric string such as `'19.95'` into a floating-point number. Why the correct answer wins: `int(...)` parses a base-10 integer string from `input()` into an `int` suitable for list indexing and integer arithmetic.

### Question 12 — A

Answer: `elif`. `elif` tests `age >= 65` only when `age < 12` was `False`, keeping the three pricing tiers mutually exclusive. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. In this case: `elif` tests `age >= 65` only when `age < 12` was `False`, keeping the three pricing tiers mutually exclusive.
- **B:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `elif` tests `age >= 65` only when `age < 12` was `False`, keeping the three pricing tiers mutually exclusive.
- **C:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `elif` tests `age >= 65` only when `age < 12` was `False`, keeping the three pricing tiers mutually exclusive.
- **D:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `elif` tests `age >= 65` only when `age < 12` was `False`, keeping the three pricing tiers mutually exclusive.

### Question 13 — B

Answer: `BRONZE`. `visits >= 20` and `visits >= 10` are both `False`, so the third check `visits >= 3` runs and prints `BRONZE`. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: `visits >= 20` and `visits >= 10` are both `False`, so the third check `visits >= 3` runs and prints `BRONZE`.
- **B:** Correct. In this case: `visits >= 20` and `visits >= 10` are both `False`, so the third check `visits >= 3` runs and prints `BRONZE`.
- **C:** Incorrect for this question. Prints `SILVER`. Why the correct answer wins: `visits >= 20` and `visits >= 10` are both `False`, so the third check `visits >= 3` runs and prints `BRONZE`.
- **D:** Incorrect for this question. Prints `GOLD`. Why the correct answer wins: `visits >= 20` and `visits >= 10` are both `False`, so the third check `visits >= 3` runs and prints `BRONZE`.

### Question 14 — C

Answer: `5`. Because `35 >= 50` is `False`, the conditional expression skips `0` and evaluates the `else` branch, assigning `5`. Evaluates to the integer `5`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Because `35 >= 50` is `False`, the conditional expression skips `0` and evaluates the `else` branch, assigning `5`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Because `35 >= 50` is `False`, the conditional expression skips `0` and evaluates the `else` branch, assigning `5`.
- **C:** Correct. Evaluates to the integer `5`. In this case: Because `35 >= 50` is `False`, the conditional expression skips `0` and evaluates the `else` branch, assigning `5`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Because `35 >= 50` is `False`, the conditional expression skips `0` and evaluates the `else` branch, assigning `5`.

### Question 15 — A

Answer: `17`. Both independent `if` conditions hold for `28`, so `fee` increases first by `2` (`12`) and then by `5` (`17`). Evaluates to the integer `17`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `17`. In this case: Both independent `if` conditions hold for `28`, so `fee` increases first by `2` (`12`) and then by `5` (`17`).
- **B:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Both independent `if` conditions hold for `28`, so `fee` increases first by `2` (`12`) and then by `5` (`17`).
- **C:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Both independent `if` conditions hold for `28`, so `fee` increases first by `2` (`12`) and then by `5` (`17`).
- **D:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Both independent `if` conditions hold for `28`, so `fee` increases first by `2` (`12`) and then by `5` (`17`).

### Question 16 — B, C

Answers: `()`; `[]`. Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy. An empty tuple `()` has length `0` and evaluates to `False` in a Boolean context. An empty list `[]` has length `0` and evaluates to `False` in a Boolean context. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `' '` contains one space character (`len(' ') == 1`), so it is truthy. Why the correct answer wins: Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy.
- **B:** Correct. An empty tuple `()` has length `0` and evaluates to `False` in a Boolean context. In this case: Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy.
- **C:** Correct. An empty list `[]` has length `0` and evaluates to `False` in a Boolean context. In this case: Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy.
- **D:** Incorrect for this question. `(0,)` is a 1-element tuple (`len((0,)) == 1`), so it evaluates to `True` even though its element is `0`. Why the correct answer wins: Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy.
- **E:** Incorrect for this question. `{0: None}` has one key-value entry (`len == 1`), so it evaluates to `True`. Why the correct answer wins: Empty tuple `()` and empty list `[]` both have length `0` and evaluate to `False`, whereas `' '` (one space), `(0,)` (one element), and `{0: None}` (one entry) are all truthy.

### Question 17 — B

Answer: `OK`. `(0,)` is a 1-element tuple (`len((0,)) == 1`), so its truthiness is `True` even though its sole element is `0`, printing `OK`. Prints `OK`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: `(0,)` is a 1-element tuple (`len((0,)) == 1`), so its truthiness is `True` even though its sole element is `0`, printing `OK`.
- **B:** Correct. Prints `OK`. In this case: `(0,)` is a 1-element tuple (`len((0,)) == 1`), so its truthiness is `True` even though its sole element is `0`, printing `OK`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `(0,)` is a 1-element tuple (`len((0,)) == 1`), so its truthiness is `True` even though its sole element is `0`, printing `OK`.
- **D:** Incorrect for this question. Prints `IDLE`. Why the correct answer wins: `(0,)` is a 1-element tuple (`len((0,)) == 1`), so its truthiness is `True` even though its sole element is `0`, printing `OK`.

### Question 18 — A

Answer: `or`. `or` returns truthy as soon as either `vip_pass` is truthy or `promo_code == 'EARLY'` holds. `or` is Python's short-circuit logical disjunction operator. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `or` is Python's short-circuit logical disjunction operator. In this case: `or` returns truthy as soon as either `vip_pass` is truthy or `promo_code == 'EARLY'` holds.
- **B:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `or` returns truthy as soon as either `vip_pass` is truthy or `promo_code == 'EARLY'` holds.
- **C:** Incorrect for this question. `not` is Python's unary logical negation operator and returns `True` or `False`. Why the correct answer wins: `or` returns truthy as soon as either `vip_pass` is truthy or `promo_code == 'EARLY'` holds.
- **D:** Incorrect for this question. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. Why the correct answer wins: `or` returns truthy as soon as either `vip_pass` is truthy or `promo_code == 'EARLY'` holds.

### Question 19 — C

Answer: `True`. Python parses `True or (False and False)`, which evaluates `False and False` (`False`) and then `True or False`, binding `True`. Evaluates to Boolean `True`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Python parses `True or (False and False)`, which evaluates `False and False` (`False`) and then `True or False`, binding `True`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Python parses `True or (False and False)`, which evaluates `False and False` (`False`) and then `True or False`, binding `True`.
- **C:** Correct. Evaluates to Boolean `True`. In this case: Python parses `True or (False and False)`, which evaluates `False and False` (`False`) and then `True or False`, binding `True`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Python parses `True or (False and False)`, which evaluates `False and False` (`False`) and then `True or False`, binding `True`.

### Question 20 — A

Answer: `while`. `while` repeats the suite while `seats_left > 0` remains `True`. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` repeats the suite while `seats_left > 0` remains `True`.
- **B:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `while` repeats the suite while `seats_left > 0` remains `True`.
- **C:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` repeats the suite while `seats_left > 0` remains `True`.
- **D:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` repeats the suite while `seats_left > 0` remains `True`.

### Question 21 — A, D

Answers: `n = 6` followed by `while n > 0: n -= 2`; `n = 16` followed by `while n >= 2: n //= 2`. `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. In this case: `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever.
- **B:** Incorrect for this question. Adding `2` to an even integer keeps `n` even on every step, so `n % 2 == 0` never turns `False`. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever.
- **C:** Incorrect for this question. Incrementing a positive integer keeps `n > 0` forever, producing an infinite loop. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever.
- **D:** Correct. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. In this case: `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever.
- **E:** Incorrect for this question. Because `pass` never updates `n`, `n > 0` remains `True` indefinitely. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` and `n = 16` with `n //= 2` reaches `1`, whereas incrementing positive `n`, running `pass`, or adding `2` to an even `n` runs forever.

### Question 22 — D

Answer: `for`. `for <target> in <iterable>:` iterates sequentially over every value produced by `range(1, 11)`. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: `for <target> in <iterable>:` iterates sequentially over every value produced by `range(1, 11)`.
- **B:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `for <target> in <iterable>:` iterates sequentially over every value produced by `range(1, 11)`.
- **C:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `for <target> in <iterable>:` iterates sequentially over every value produced by `range(1, 11)`.
- **D:** Correct. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. In this case: `for <target> in <iterable>:` iterates sequentially over every value produced by `range(1, 11)`.

### Question 23 — C, E

Answers: `range(8, 2)`; `range(2, 8, -2)`. `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). Why the correct answer wins: `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`.
- **B:** Incorrect for this question. `range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers). Why the correct answer wins: `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`.
- **C:** Correct. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. In this case: `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`.
- **D:** Incorrect for this question. `range(3, 12, 3)` generates `3, 6, 9` (three integers). Why the correct answer wins: `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`.
- **E:** Correct. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. In this case: `range(8, 2)` steps upward from `8` toward `2` and `range(2, 8, -2)` steps downward from `2` away from `8`, so both ranges have length `0`.

### Question 24 — B

Answer: `4`. Iterating over `'QUEUE1'` visits `'U'`, `'E'`, `'U'`, and `'E'` as members of `'AEIOU'`, incrementing `vowels` to `4`. Evaluates to the integer `4`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Iterating over `'QUEUE1'` visits `'U'`, `'E'`, `'U'`, and `'E'` as members of `'AEIOU'`, incrementing `vowels` to `4`.
- **B:** Correct. Evaluates to the integer `4`. In this case: Iterating over `'QUEUE1'` visits `'U'`, `'E'`, `'U'`, and `'E'` as members of `'AEIOU'`, incrementing `vowels` to `4`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Iterating over `'QUEUE1'` visits `'U'`, `'E'`, `'U'`, and `'E'` as members of `'AEIOU'`, incrementing `vowels` to `4`.
- **D:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Iterating over `'QUEUE1'` visits `'U'`, `'E'`, `'U'`, and `'E'` as members of `'AEIOU'`, incrementing `vowels` to `4`.

### Question 25 — A

Answer: `break`. `break` exits the `for` loop immediately without checking `'1D'`. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. In this case: `break` exits the `for` loop immediately without checking `'1D'`.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `break` exits the `for` loop immediately without checking `'1D'`.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `break` exits the `for` loop immediately without checking `'1D'`.
- **D:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `break` exits the `for` loop immediately without checking `'1D'`.

### Question 26 — B

Answer: `8`. `grp == 6` triggers `continue` and is skipped, so `total` adds `3 + 5` and prints `8`. Evaluates to the integer `8`. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: `grp == 6` triggers `continue` and is skipped, so `total` adds `3 + 5` and prints `8`.
- **B:** Correct. Evaluates to the integer `8`. In this case: `grp == 6` triggers `continue` and is skipped, so `total` adds `3 + 5` and prints `8`.
- **C:** Incorrect for this question. Evaluates to the integer `14`. Why the correct answer wins: `grp == 6` triggers `continue` and is skipped, so `total` adds `3 + 5` and prints `8`.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: `grp == 6` triggers `continue` and is skipped, so `total` adds `3 + 5` and prints `8`.

### Question 27 — A, D

Answers: When a `for` loop finishes iterating over every element without executing `break`; When a `while` loop's condition evaluates to `False` (including on the very first check) without executing `break`. The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception. Normal exhaustion of a `for` iterable runs the attached `else:` suite. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs. In this case: The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception.
- **B:** Incorrect for this question. An unhandled exception unwinds out of the loop without running its `else:` suite. Why the correct answer wins: The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception.
- **C:** Incorrect for this question. `break` bypasses both the remaining iterations AND the loop's `else:` suite. Why the correct answer wins: The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception.
- **D:** Correct. Normal exhaustion of a `for` iterable runs the attached `else:` suite. In this case: The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception.
- **E:** Incorrect for this question. `return` exits the whole function immediately and skips any loop `else:` suite. Why the correct answer wins: The loop `else:` block runs when a `for` loop exhausts all passengers or a `while` condition turns `False` without executing `break`, `return`, or raising an uncaught exception.

### Question 28 — C

Answer: `12`. Each of the `3` outer iterations runs `4` inner iterations, incrementing `berths` `3 * 4 == 12` times. Evaluates to the integer `12`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Each of the `3` outer iterations runs `4` inner iterations, incrementing `berths` `3 * 4 == 12` times.
- **B:** Incorrect for this question. Evaluates to the integer `7`. Why the correct answer wins: Each of the `3` outer iterations runs `4` inner iterations, incrementing `berths` `3 * 4 == 12` times.
- **C:** Correct. Evaluates to the integer `12`. In this case: Each of the `3` outer iterations runs `4` inner iterations, incrementing `berths` `3 * 4 == 12` times.
- **D:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Each of the `3` outer iterations runs `4` inner iterations, incrementing `berths` `3 * 4 == 12` times.

### Question 29 — A

Answer: `[40, 50]`. Negative index `-2` points to `40`, and omitting the stop index slices through the end of the list, returning `[40, 50]`. Slice `[-2:]` returns the last two items `[40, 50]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slice `[-2:]` returns the last two items `[40, 50]`. In this case: Negative index `-2` points to `40`, and omitting the stop index slices through the end of the list, returning `[40, 50]`.
- **B:** Incorrect for this question. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Why the correct answer wins: Negative index `-2` points to `40`, and omitting the stop index slices through the end of the list, returning `[40, 50]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Negative index `-2` points to `40`, and omitting the stop index slices through the end of the list, returning `[40, 50]`.
- **D:** Incorrect for this question. Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`. Why the correct answer wins: Negative index `-2` points to `40`, and omitting the stop index slices through the end of the list, returning `[40, 50]`.

### Question 30 — D

Answer: `IndexError`. Valid non-negative indices for a 5-element list are `0` through `4`, so `coaches[5]` raises `IndexError`. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `48`. Why the correct answer wins: Valid non-negative indices for a 5-element list are `0` through `4`, so `coaches[5]` raises `IndexError`.
- **B:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: Valid non-negative indices for a 5-element list are `0` through `4`, so `coaches[5]` raises `IndexError`.
- **C:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Valid non-negative indices for a 5-element list are `0` through `4`, so `coaches[5]` raises `IndexError`.
- **D:** Correct. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. In this case: Valid non-negative indices for a 5-element list are `0` through `4`, so `coaches[5]` raises `IndexError`.

### Question 31 — B

Answer: `pop`. `waitlist.pop(0)` removes and returns the element at index `0`, shifting remaining elements left. `.pop([index])` removes and returns the element at `index` (default `-1`). Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.append(item)` adds `item` as a single element at the end of a list. Why the correct answer wins: `waitlist.pop(0)` removes and returns the element at index `0`, shifting remaining elements left.
- **B:** Correct. `.pop([index])` removes and returns the element at `index` (default `-1`). In this case: `waitlist.pop(0)` removes and returns the element at index `0`, shifting remaining elements left.
- **C:** Incorrect for this question. `.extend(iterable)` appends each element yielded by `iterable` to the list. Why the correct answer wins: `waitlist.pop(0)` removes and returns the element at index `0`, shifting remaining elements left.
- **D:** Incorrect for this question. `.insert(index, item)` places `item` before `index` in the list. Why the correct answer wins: `waitlist.pop(0)` removes and returns the element at index `0`, shifting remaining elements left.

### Question 32 — B, C

Answers: `items.insert(0, x)`; `items.remove(x)`. `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists. `.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place. `items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists.
- **B:** Correct. `items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent. In this case: `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists.
- **C:** Correct. `.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place. In this case: `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists.
- **D:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists.
- **E:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: `items.insert(0, x)` and `items.remove(x)` modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` allocate new lists.

### Question 33 — A

Answer: `len`. Built-in `len(seat_pool)` returns the current number of elements in the list as an `int`. Built-in `len(s)` returns the element count of collection `s`. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Built-in `len(s)` returns the element count of collection `s`. In this case: Built-in `len(seat_pool)` returns the current number of elements in the list as an `int`.
- **B:** Incorrect for this question. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. Why the correct answer wins: Built-in `len(seat_pool)` returns the current number of elements in the list as an `int`.
- **C:** Incorrect for this question. Built-in `sorted(iterable)` returns a new sorted list without mutating its input. Why the correct answer wins: Built-in `len(seat_pool)` returns the current number of elements in the list as an `int`.
- **D:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: Built-in `len(seat_pool)` returns the current number of elements in the list as an `int`.

### Question 34 — A, C

Answers: `items[:]`; `list(items)`. Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list. `items[:]` creates a shallow copy as a new outer list object. `list(items)` constructs a new outer list containing the same element references (a shallow copy). Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `list(items)` constructs a new outer list containing the same element references (a shallow copy). In this case: Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list.
- **B:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list.
- **C:** Correct. `items[:]` creates a shallow copy as a new outer list object. In this case: Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list.
- **D:** Incorrect for this question. `items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent. Why the correct answer wins: Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list.
- **E:** Incorrect for this question. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Why the correct answer wins: Both `items[:]` and `list(items)` return a new outer list with the same elements, whereas `backup = items` creates an alias to the same list.

### Question 35 — C

Answer: `[1, 9, 25]`. Filtering odd values from `0..5` selects `1, 3, 5`, and squaring each produces `[1, 9, 25]`. Filtering odd numbers `1, 3, 5` from `range(6)` and squaring them produces `[1, 9, 25]`. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: Filtering odd values from `0..5` selects `1, 3, 5`, and squaring each produces `[1, 9, 25]`.
- **B:** Incorrect for this question. Filtering even numbers `0, 2, 4` from `range(6)` and squaring them produces `[0, 4, 16]`. Why the correct answer wins: Filtering odd values from `0..5` selects `1, 3, 5`, and squaring each produces `[1, 9, 25]`.
- **C:** Correct. Filtering odd numbers `1, 3, 5` from `range(6)` and squaring them produces `[1, 9, 25]`. In this case: Filtering odd values from `0..5` selects `1, 3, 5`, and squaring each produces `[1, 9, 25]`.
- **D:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Filtering odd values from `0..5` selects `1, 3, 5`, and squaring each produces `[1, 9, 25]`.

### Question 36 — D

Answer: `in`. On strings, `sub in text` checks contiguous substring membership and returns `True` when `'VIP'` occurs in `ticket_code`. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: On strings, `sub in text` checks contiguous substring membership and returns `True` when `'VIP'` occurs in `ticket_code`.
- **B:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: On strings, `sub in text` checks contiguous substring membership and returns `True` when `'VIP'` occurs in `ticket_code`.
- **C:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: On strings, `sub in text` checks contiguous substring membership and returns `True` when `'VIP'` occurs in `ticket_code`.
- **D:** Correct. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. In this case: On strings, `sub in text` checks contiguous substring membership and returns `True` when `'VIP'` occurs in `ticket_code`.

### Question 37 — A, B

Answers: `(42,)`; `42,`. `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). In this case: `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`.
- **B:** Correct. Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. In this case: `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`.
- **C:** Incorrect for this question. An empty list `[]` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`.
- **D:** Incorrect for this question. `tuple()` with no arguments returns the empty 0-element tuple `()`, not a 1-element tuple. Why the correct answer wins: `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`.
- **E:** Incorrect for this question. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Why the correct answer wins: `(42,)` and `42,` both use a trailing comma to build a 1-element tuple, whereas `(42)` is `int` `42` and `tuple()` has length `0`.

### Question 38 — C

Answer: `3`. Although `row_data` is an immutable tuple, `row_data[1]` references a mutable list whose `.append(30)` succeeds in place, so `len(row_data[1])` prints `3`. Evaluates to the integer `3`. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `AttributeError` is raised when accessing a method or attribute name that does not exist on that object's type. Why the correct answer wins: Although `row_data` is an immutable tuple, `row_data[1]` references a mutable list whose `.append(30)` succeeds in place, so `len(row_data[1])` prints `3`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Although `row_data` is an immutable tuple, `row_data[1]` references a mutable list whose `.append(30)` succeeds in place, so `len(row_data[1])` prints `3`.
- **C:** Correct. Evaluates to the integer `3`. In this case: Although `row_data` is an immutable tuple, `row_data[1]` references a mutable list whose `.append(30)` succeeds in place, so `len(row_data[1])` prints `3`.
- **D:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Although `row_data` is an immutable tuple, `row_data[1]` references a mutable list whose `.append(30)` succeeds in place, so `len(row_data[1])` prints `3`.

### Question 39 — C

Answer: `0`. Providing fallback `0` to `dict.pop(key, default)` prevents `KeyError` when `'BALCONY'` is absent and returns `0`. Evaluates to the integer `0`. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Providing fallback `0` to `dict.pop(key, default)` prevents `KeyError` when `'BALCONY'` is absent and returns `0`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Providing fallback `0` to `dict.pop(key, default)` prevents `KeyError` when `'BALCONY'` is absent and returns `0`.
- **C:** Correct. Evaluates to the integer `0`. In this case: Providing fallback `0` to `dict.pop(key, default)` prevents `KeyError` when `'BALCONY'` is absent and returns `0`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Providing fallback `0` to `dict.pop(key, default)` prevents `KeyError` when `'BALCONY'` is absent and returns `0`.

### Question 40 — A, B

Answers: `.values()` yields every stored value in insertion order; `.keys()` yields every key in insertion order. `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order. `d.values()` returns a view over the dictionary's values. `d.keys()` returns a view over the dictionary's keys. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `d.values()` returns a view over the dictionary's values. In this case: `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order.
- **B:** Correct. `d.keys()` returns a view over the dictionary's keys. In this case: `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order.
- **C:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order.
- **D:** Incorrect for this question. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Why the correct answer wins: `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order.
- **E:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: `d.values()` yields stored values in insertion order and `d.keys()` yields stored keys in insertion order.

### Question 41 — D

Answer: `4`. In a raw string `r'A\nB'`, backslashes are kept literally instead of forming escape sequences, so `'A'`, `'\\'`, `'n'`, and `'B'` give length `4`. Evaluates to the integer `4`. Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: In a raw string `r'A\nB'`, backslashes are kept literally instead of forming escape sequences, so `'A'`, `'\\'`, `'n'`, and `'B'` give length `4`.
- **B:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: In a raw string `r'A\nB'`, backslashes are kept literally instead of forming escape sequences, so `'A'`, `'\\'`, `'n'`, and `'B'` give length `4`.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: In a raw string `r'A\nB'`, backslashes are kept literally instead of forming escape sequences, so `'A'`, `'\\'`, `'n'`, and `'B'` give length `4`.
- **D:** Correct. Evaluates to the integer `4`. In this case: In a raw string `r'A\nB'`, backslashes are kept literally instead of forming escape sequences, so `'A'`, `'\\'`, `'n'`, and `'B'` give length `4`.

### Question 42 — B

Answer: `replace`. `str.replace('-', '')` returns a new string with every hyphen replaced by the empty string. `s.replace(old, new)` returns a new string where occurrences of `old` are replaced with `new`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `s.strip()` returns a new string with leading and trailing whitespace removed. Why the correct answer wins: `str.replace('-', '')` returns a new string with every hyphen replaced by the empty string.
- **B:** Correct. `s.replace(old, new)` returns a new string where occurrences of `old` are replaced with `new`. In this case: `str.replace('-', '')` returns a new string with every hyphen replaced by the empty string.
- **C:** Incorrect for this question. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. Why the correct answer wins: `str.replace('-', '')` returns a new string with every hyphen replaced by the empty string.
- **D:** Incorrect for this question. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Why the correct answer wins: `str.replace('-', '')` returns a new string with every hyphen replaced by the empty string.

### Question 43 — A

Answer: `True`, because code-point order places digits (`'0'`–`'9'`) before uppercase (`'A'`–`'Z'`) and uppercase before lowercase (`'a'`–`'z'`). String comparisons compare Unicode code points (`ord('9') == 57`, `ord('A') == 65`, `ord('a') == 97`), so `'9' < 'A' < 'a'` prints `True`. Python compares strings lexicographically by Unicode code point (`'9' (57) < 'A' (65) < 'a' (97)`). Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Python compares strings lexicographically by Unicode code point (`'9' (57) < 'A' (65) < 'a' (97)`). In this case: String comparisons compare Unicode code points (`ord('9') == 57`, `ord('A') == 65`, `ord('a') == 97`), so `'9' < 'A' < 'a'` prints `True`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: String comparisons compare Unicode code points (`ord('9') == 57`, `ord('A') == 65`, `ord('a') == 97`), so `'9' < 'A' < 'a'` prints `True`.
- **C:** Incorrect for this question. Standard `<` and `>` on strings are case-sensitive code-point comparisons. Why the correct answer wins: String comparisons compare Unicode code points (`ord('9') == 57`, `ord('A') == 65`, `ord('a') == 97`), so `'9' < 'A' < 'a'` prints `True`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: String comparisons compare Unicode code points (`ord('9') == 57`, `ord('A') == 65`, `ord('a') == 97`), so `'9' < 'A' < 'a'` prints `True`.

### Question 44 — C

Answer: `return`. `return 120` exits `seat_price` immediately and delivers `120` as the call's value. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `return 120` exits `seat_price` immediately and delivers `120` as the call's value.
- **B:** Incorrect for this question. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Why the correct answer wins: `return 120` exits `seat_price` immediately and delivers `120` as the call's value.
- **C:** Correct. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. In this case: `return 120` exits `seat_price` immediately and delivers `120` as the call's value.
- **D:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `return 120` exits `seat_price` immediately and delivers `120` as the call's value.

### Question 45 — A

Answer: Returning `a, b` packs and returns a 2-element `tuple` `(a, b)` that the caller can unpack. A comma-separated expression after `return` packs the values into a 2-element `tuple` `(1, 30)`. A comma-separated expression after `return` returns a single `tuple` object. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. A comma-separated expression after `return` returns a single `tuple` object. In this case: A comma-separated expression after `return` packs the values into a 2-element `tuple` `(1, 30)`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: A comma-separated expression after `return` packs the values into a 2-element `tuple` `(1, 30)`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: A comma-separated expression after `return` packs the values into a 2-element `tuple` `(1, 30)`.
- **D:** Incorrect for this question. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. Why the correct answer wins: A comma-separated expression after `return` packs the values into a 2-element `tuple` `(1, 30)`.

### Question 46 — B

Answer: `yield`. `yield` pauses the generator function at each group letter and resumes on the next iteration step. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `yield` pauses the generator function at each group letter and resumes on the next iteration step.
- **B:** Correct. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. In this case: `yield` pauses the generator function at each group letter and resumes on the next iteration step.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `yield` pauses the generator function at each group letter and resumes on the next iteration step.
- **D:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `yield` pauses the generator function at each group letter and resumes on the next iteration step.

### Question 47 — A

Answer: `StopIteration`. Calling `next()` on an exhausted generator iterator raises `StopIteration`. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. In this case: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Calling `next()` on an exhausted generator iterator raises `StopIteration`.

### Question 48 — C

Answer: `8`. `two_pow(3)` computes `2 * 2 * 2 * 1`, hitting base case `e == 0` and returning `8`. Evaluates to the integer `8`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `two_pow(3)` computes `2 * 2 * 2 * 1`, hitting base case `e == 0` and returning `8`.
- **B:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: `two_pow(3)` computes `2 * 2 * 2 * 1`, hitting base case `e == 0` and returning `8`.
- **C:** Correct. Evaluates to the integer `8`. In this case: `two_pow(3)` computes `2 * 2 * 2 * 1`, hitting base case `e == 0` and returning `8`.
- **D:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: `two_pow(3)` computes `2 * 2 * 2 * 1`, hitting base case `e == 0` and returning `8`.

### Question 49 — A, B

Answers: A reachable base case that returns directly without making another recursive call; A recursive call whose arguments move strictly closer to the base case on each step. Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch. Valid finite recursion requires at least one non-recursive base branch. Without progress toward the base condition, recursion never terminates cleanly. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Without progress toward the base condition, recursion never terminates cleanly. In this case: Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch.
- **B:** Correct. Valid finite recursion requires at least one non-recursive base branch. In this case: Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch.
- **C:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch.
- **D:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch.
- **E:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Every terminating recursive routine needs a reachable non-recursive base branch and recursive calls whose inputs step toward that base branch.

### Question 50 — C

Answer: `TypeError`. Omitting required positional argument `seat` raises `TypeError` at call time. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Omitting required positional argument `seat` raises `TypeError` at call time.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Omitting required positional argument `seat` raises `TypeError` at call time.
- **C:** Correct. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. In this case: Omitting required positional argument `seat` raises `TypeError` at call time.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Omitting required positional argument `seat` raises `TypeError` at call time.

### Question 51 — A, E

Answers: `calc(rate=0.2, base=100)`; `calc(100, rate=0.2)`. `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value. In this case: `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword.
- **B:** Incorrect for this question. Passing an unknown keyword parameter name `tax` when the signature is `def calc(base, rate):` raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword.
- **C:** Incorrect for this question. Placing positional `0.2` after keyword `base=100` raises `SyntaxError`. Why the correct answer wins: `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword.
- **D:** Incorrect for this question. Passing `100` to `base` positionally and `base=200` by keyword raises `TypeError`. Why the correct answer wins: `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword.
- **E:** Correct. Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python's call-site rules. In this case: `calc(rate=0.2, base=100)` supplies both parameters by keyword and `calc(100, rate=0.2)` places positional before keyword.

### Question 52 — B

Answer: `15`. Omitting `per_ticket` uses its default value `5`, returning `3 * 5 == 15`. Evaluates to the integer `15`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Omitting `per_ticket` uses its default value `5`, returning `3 * 5 == 15`.
- **B:** Correct. Evaluates to the integer `15`. In this case: Omitting `per_ticket` uses its default value `5`, returning `3 * 5 == 15`.
- **C:** Incorrect for this question. Evaluates to the integer `25`. Why the correct answer wins: Omitting `per_ticket` uses its default value `5`, returning `3 * 5 == 15`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Omitting `per_ticket` uses its default value `5`, returning `3 * 5 == 15`.

### Question 53 — D

Answer: `6`. Passing `2` explicitly overrides default `bags_each=1`, so `allowance(3, 2)` returns `3 * 2 == 6`. Evaluates to the integer `6`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Passing `2` explicitly overrides default `bags_each=1`, so `allowance(3, 2)` returns `3 * 2 == 6`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Passing `2` explicitly overrides default `bags_each=1`, so `allowance(3, 2)` returns `3 * 2 == 6`.
- **C:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Passing `2` explicitly overrides default `bags_each=1`, so `allowance(3, 2)` returns `3 * 2 == 6`.
- **D:** Correct. Evaluates to the integer `6`. In this case: Passing `2` explicitly overrides default `bags_each=1`, so `allowance(3, 2)` returns `3 * 2 == 6`.

### Question 54 — B

Answer: `global`. `global issued_count` directs rebinding inside `issue_one` to the module-level variable instead of a local name. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. Why the correct answer wins: `global issued_count` directs rebinding inside `issue_one` to the module-level variable instead of a local name.
- **B:** Correct. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. In this case: `global issued_count` directs rebinding inside `issue_one` to the module-level variable instead of a local name.
- **C:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `global issued_count` directs rebinding inside `issue_one` to the module-level variable instead of a local name.
- **D:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `global issued_count` directs rebinding inside `issue_one` to the module-level variable instead of a local name.

### Question 55 — C, D

Answers: Assigning to a name inside a function without `global` creates a separate local variable, leaving the module-level variable unchanged; Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`. Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable. Under Python's LEGB rule, local assignment binds in the function's local frame rather than mutating the module global. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable.
- **B:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable.
- **C:** Correct. Under Python's LEGB rule, local assignment binds in the function's local frame rather than mutating the module global. In this case: Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable.
- **D:** Correct. `global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`. In this case: Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable.
- **E:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Reading a module-level name without assigning to it resolves via module scope, whereas assigning to that name without `global` creates a separate local variable.

### Question 56 — A

Answer: `LookupError`. Both `KeyError` and `IndexError` inherit directly from `LookupError`. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. In this case: Both `KeyError` and `IndexError` inherit directly from `LookupError`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Both `KeyError` and `IndexError` inherit directly from `LookupError`.
- **C:** Incorrect for this question. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Why the correct answer wins: Both `KeyError` and `IndexError` inherit directly from `LookupError`.
- **D:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Both `KeyError` and `IndexError` inherit directly from `LookupError`.

### Question 57 — B

Answer: `UnboundLocalError`. `UnboundLocalError` inherits directly from `NameError` and signals a local variable read prior to assignment. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `UnboundLocalError` inherits directly from `NameError` and signals a local variable read prior to assignment.
- **B:** Correct. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. In this case: `UnboundLocalError` inherits directly from `NameError` and signals a local variable read prior to assignment.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: `UnboundLocalError` inherits directly from `NameError` and signals a local variable read prior to assignment.
- **D:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `UnboundLocalError` inherits directly from `NameError` and signals a local variable read prior to assignment.

### Question 58 — A

Answer: `raise`. `raise` triggers the `ValueError` instance and unwinds the call stack until caught. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. In this case: `raise` triggers the `ValueError` instance and unwinds the call stack until caught.
- **B:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `raise` triggers the `ValueError` instance and unwinds the call stack until caught.
- **C:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `raise` triggers the `ValueError` instance and unwinds the call stack until caught.
- **D:** Incorrect for this question. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Why the correct answer wins: `raise` triggers the `ValueError` instance and unwinds the call stack until caught.

### Question 59 — D

Answer: `KeyError`. Subscripting a dictionary with an absent key `'FL99'` raises `KeyError`. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Subscripting a dictionary with an absent key `'FL99'` raises `KeyError`.
- **B:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Subscripting a dictionary with an absent key `'FL99'` raises `KeyError`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Subscripting a dictionary with an absent key `'FL99'` raises `KeyError`.
- **D:** Correct. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. In this case: Subscripting a dictionary with an absent key `'FL99'` raises `KeyError`.

### Question 60 — C, D

Answers: The `else:` block runs only when the `try:` block completes normally without raising an exception; The `finally:` block always runs on the way out — whether `try:` succeeded, an `except:` ran, an uncaught exception propagated, or `return` executed. `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct. In `try / except / else / finally`, `else:` executes after `try:` only if no exception was raised in `try:`, and before `finally:`. `finally:` is guaranteed cleanup code that runs before control leaves the `try` statement. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct.
- **B:** Incorrect for this question. `except:` and `else:` are mutually exclusive on any single execution of a `try` statement. Why the correct answer wins: `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct.
- **C:** Correct. `finally:` is guaranteed cleanup code that runs before control leaves the `try` statement. In this case: `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct.
- **D:** Correct. In `try / except / else / finally`, `else:` executes after `try:` only if no exception was raised in `try:`, and before `finally:`. In this case: `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct.
- **E:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: `else:` runs only if `try:` completed with no exception, whereas `finally:` runs unconditionally before control leaves the `try` construct.
