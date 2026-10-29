# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 6

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 18 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A bakery runs `python3 scale_batch.py` to recalculate dough weights for morning loaves. Which statement accurately describes how standard CPython executes `scale_batch.py`?

- A. CPython flattens all imported modules into static ROM microcode before parsing syntax
- B. CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime
- C. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- D. CPython executes `.py` source only inside an HTML5 browser DOM engine

### 2. In a pantry inventory script, a typo writes `jar_cap = 0x1G` using letter `'G'` inside a hexadecimal literal. Because `0x1G` is not a legal hexadecimal token in Python, which error category does this represent?

- A. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- B. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- C. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning
- D. A lexical error because the character or token itself does not belong to valid Python token forms

### 3. A culinary student writing a recipe-scaling script checks which candidate names are reserved keywords in Python 3. Which two identifiers are hard reserved keywords? Select two.

- A. `false`
- B. `case`
- C. `del`
- D. `lambda`
- E. `dict`

### 4. A smart-oven controller stores preset bit flags using non-decimal integer literals. Which two literals are valid integer literals in Python 3? Select two.

- A. `1__000`
- B. `0x2A`
- C. `0o27`
- D. `0b102`
- E. `500_`

### 5. Complete `____ = 500` in a sourdough hydration calculator so the variable name obeys Python 3 identifier syntax and PEP-8 snake_case conventions. Which identifier fills the blank?

- A. `fx-rate`
- B. `total$usd`
- C. `flour_grams_1`
- D. `2nd_quarter`

### 6. A freezer-shelf offset formula evaluates `shelf_step = -17.0 // 5` with one `float` operand and one `int` operand. What value does Python 3 assign to `shelf_step`?

- A. `-4`
- B. `-2`
- C. `-3.0`
- D. `-4.0`

### 7. A yeast-growth estimate evaluates `cells = 3 * 3 ** 3` without parentheses. Because `**` binds tighter than `*`, what integer is assigned to `cells`?

- A. `18`
- B. `81`
- C. `27`
- D. `36`

### 8. A pantry barcode reader packs and unpacks bit fields inside integers. Which two tokens are bitwise shift operators in Python 3? Select two.

- A. `**`
- B. `>>`
- C. `//`
- D. `<<`
- E. `and`

### 9. Complete `grams = 120; grams ____ 3` so tripling a cookie batch scales `grams` in place to `360`. Which augmented assignment operator fills the blank?

- A. `%`
- B. `+=`
- C. `//=`
- D. `*=`

### 10. A recipe API helper executes `print('https://api.local', 'v2', 'users', sep='/')`. What text does `print()` write to standard output?

- A. `A-B/C`
- B. `A-B` on line 1 and `C` on line 2
- C. `https://api.local/v2/users`
- D. `TypeError`

### 11. Complete `aisle_letter = ____(65)` in a pantry bin labeler so integer code point `65` converts into single-character string `'A'`. Which built-in callable fills the blank?

- A. `int`
- B. `chr`
- C. `float`
- D. `ord`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete `if oven_c >= 230: mode = 'PIZZA'` / `____ oven_c >= 180: mode = 'BAKE'` / `else: mode = 'WARM'` so `oven_c = 200` selects `'BAKE'` exclusively. Which keyword fills the blank?

- A. `else`
- B. `elif`
- C. `while`
- D. `with`

### 13. A pantry expiry monitor sets `days_left = 3` and runs `if days_left <= 0: print('CRIT')` / `elif days_left <= 2: print('ALERT')` / `elif days_left <= 5: print('WARN')` / `else: print('OK')`. What is printed?

- A. `ALERT`
- B. `CRIT`
- C. `WARN`
- D. `OK`

### 14. A grocery delivery script selects inline Python 3 conditional expressions for delivery fees and loyalty tags. Which two expressions are syntactically valid? Select two.

- A. `subtotal >= 50 ? 0 : 5`
- B. `if subtotal >= 50 then 0 else 5`
- C. `0 if subtotal >= 50 else 5`
- D. `0 if subtotal >= 50`
- E. `'VIP' if points >= 100 else 'STD'`

### 15. A spice-blend adjuster sets `heat = 9; grams = 10` and runs two independent `if` blocks: `if heat >= 5: grams += 2` followed by `if heat >= 8: grams += 4`. What integer does `grams` hold afterward?

- A. `11`
- B. `14`
- C. `16`
- D. `10`

### 16. A pantry audit checks `if container:` on Python collection objects. Which two values of `container` evaluate to `True` in a Boolean context? Select two.

- A. `{0: None}`
- B. `{}`
- C. `()`
- D. `(0,)`
- E. `0.0`

### 17. An allergen filter sets `flagged = []` and runs `if flagged: print('WARN')` / `else: print('IDLE')`. What is printed?

- A. `IDLE`
- B. `OK`
- C. `TypeError`
- D. `WARN`

### 18. Complete `if ____ pantry_empty: start_cooking()` so `start_cooking()` runs whenever Boolean flag `pantry_empty` is `False`. Which unary logical operator fills the blank?

- A. `not`
- B. `is`
- C. `or`
- D. `and`

### 19. A kitchen safety guard evaluates `ready = not True and False` without parentheses. Because `not` binds tighter than `and`, what Boolean value is assigned to `ready`?

- A. `False`
- B. `TypeError`
- C. `True`
- D. `0`

### 20. Complete `cups_needed = 8` / `____ cups_needed >= 2:` / `    cups_needed -= 2` so two-cup scoops repeat until `cups_needed` reaches `0`. Which keyword fills the blank?

- A. `pass`
- B. `elif`
- C. `while`
- D. `for`

### 21. A batch-timer developer checks five `while` loop patterns. Which two loops are guaranteed to terminate after finitely many steps? Select two.

- A. `n = 4` followed by `while n % 2 == 0: n += 2`
- B. `n = 5` followed by `while n > 0: pass`
- C. `n = 6` followed by `while n > 0: n -= 2`
- D. `n = 1` followed by `while n > 0: n += 1`
- E. `n = 16` followed by `while n >= 2: n //= 2`

### 22. A tray-numbering helper inspects `range()` calls to find which ones yield zero numbers. Which two `range()` calls are empty? Select two.

- A. `range(10, 2, -2)`
- B. `range(3, 12, 3)`
- C. `range(2, 8, -2)`
- D. `range(8, 2)`
- E. `range(0, 10, 2)`

### 23. A proofing-timer schedule evaluates `print(sum(range(3, 12, 3)))`. What integer is printed?

- A. `27`
- B. `12`
- C. `18`
- D. `9`

### 24. A label scanner counts hyphens with `dashes = 0` / `for ch in 'JAR-04-B':` / `    if ch == '-': dashes += 1` / `print(dashes)`. What integer is printed?

- A. `5`
- B. `TypeError`
- C. `3`
- D. `2`

### 25. Complete `for item in ['oats', 'peanuts', 'rice']:` / `    if item == 'peanuts': nut_alert = True; ____` so scanning stops immediately as soon as `'peanuts'` is detected. Which keyword fills the blank?

- A. `return`
- B. `break`
- C. `continue`
- D. `pass`

### 26. Complete `if metric_units:` / `    ____` / `else: convert_ounces()` so the `if` branch acts as a syntactic placeholder without raising `IndentationError`. Which keyword fills the blank?

- A. `raise`
- B. `pass`
- C. `break`
- D. `continue`

### 27. A pantry check sets `spoiled = 0` and runs `while spoiled > 0:` / `    print('HALT'); break` / `else: print('CLEAN')`. Because `spoiled > 0` is `False` on the very first check, what is printed?

- A. Nothing is printed
- B. `HALT`
- C. `CLEAN`
- D. `SyntaxError`

### 28. A tasting-menu planner sets `combos = 0` and runs `for soup in ['miso', 'lentil']:` / `    for bread in ['rye', 'brioche', 'pita', 'naan']: combos += 1` / `print(combos)`. What integer is printed?

- A. `8`
- B. `4`
- C. `12`
- D. `6`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. Jar weights in grams are stored in `jars = [10, 20, 30, 40, 50]`. What list does `jars[-4:-2]` evaluate to?

- A. `IndexError`
- B. `[40, 50]`
- C. `[40, 30, 20, 10]`
- D. `[20, 30]`

### 30. A spice list sets `base = [1, 2]`, runs `base.extend([3, 4])`, and prints `base`. What list is printed?

- A. `TypeError`
- B. `None`
- C. `[1, 2, 3, 4]`
- D. `[1, 2, [3, 4]]`

### 31. Complete `steps = ['mix', 'knead']; steps.____('bake')` so `'bake'` is added as a single string at the end rather than split into `'b'`, `'a'`, `'k'`, `'e'`. Which list method name fills the blank?

- A. `append`
- B. `remove`
- C. `extend`
- D. `pop`

### 32. A recipe card holds `items = ['salt', 'cumin', 'basil']`. Which two expressions mutate `items` in place? Select two.

- A. `items.sort()`
- B. `items.insert(0, x)`
- C. `items + [x]`
- D. `sorted(items)`
- E. `items[:]`

### 33. Complete `pantry = ['milk', 'expired', 'eggs']; ____ pantry[1]` so `'expired'` at index `1` is removed in place without needing to save a return value. Which keyword fills the blank?

- A. `del`
- B. `with`
- C. `from`
- D. `pass`

### 34. A chef holds flat list `items = [50, 100, 150]` and needs a shallow copy before scaling a test recipe. Which two expressions return a new shallow-copied list? Select two.

- A. `items.remove(x)`
- B. `backup = items`
- C. `items[:]`
- D. `items.pop()`
- E. `items.copy()`

### 35. Complete `doubled = [g * 2 ____ g in [15, 30, 45]]` to build the scaled ingredient list `[30, 60, 90]`. Which keyword fills the blank?

- A. `for`
- B. `elif`
- C. `while`
- D. `with`

### 36. Complete `if 'gluten' ____ allergens: print('Contains gluten')` so the check tests membership in list `allergens`. Which operator fills the blank?

- A. `in`
- B. `or`
- C. `is`
- D. `not`

### 37. A nutrition-label helper creates a 1-element tuple storing integer `42`. Which two expressions produce a `tuple` of length `1`? Select two.

- A. `{}`
- B. `(42,)`
- C. `tuple()`
- D. `(42)`
- E. `42,`

### 38. A pantry sensor stores `pair = (5, [10, 20])` and evaluates `~pair[0]`. Knowing `pair[0]` is integer `5`, what integer does bitwise inversion `~pair[0]` produce?

- A. `TypeError`
- B. `-6`
- C. `-2`
- D. `5`

### 39. A pantry stock map `rates = {'flour': 5, 'sugar': 3}` lacks key `'CHF'`. Which two expressions access or pop `'CHF'` with default `0` without raising `KeyError`? Select two.

- A. `rates.pop('CHF', 0)`
- B. `except KeyError, IndexError:`
- C. `rates.get('CHF', 0)`
- D. `rates['CHF']`
- E. `calc(100, base=200)`

### 40. Complete `for spice, grams in recipe.____():` so each loop step unpacks both the dictionary key `spice` and its mapped value `grams`. Which dictionary method name fills the blank?

- A. `pop`
- B. `get`
- C. `find`
- D. `items`

### 41. A label test stores `brand = 'Python'` and evaluates `brand[::-1]`. Which new string is returned?

- A. `'Pto'`
- B. `'nohtyP'`
- C. `IndexError`
- D. `None`

### 42. A recipe normalizer calls `spice.upper()` on `spice = 'thyme'` without reassigning `spice`. Which statement accurately describes `spice` after `spice.upper()` runs?

- A. `False`, because Python compares strings case-insensitively by alphabetical order
- B. Membership `k in d` checks both keys and values simultaneously
- C. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- D. String case methods such as `.upper()`, `.lower()`, and `.title()` always return a new string and leave the original unchanged

### 43. Complete `idx = notes.____('unsalted')` so searching recipe `notes` returns `-1` rather than raising `ValueError` when `'unsalted'` does not appear. Which string method name fills the blank?

- A. `index`
- B. `split`
- C. `replace`
- D. `find`

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Complete `____ scale_grams(amount, factor):` / `    return amount * factor` to declare a named recipe-scaling function. Which keyword fills the blank?

- A. `function`
- B. `var`
- C. `lambda`
- D. `def`

### 45. Which two statements accurately describe return values from ordinary Python functions? Select two.

- A. Declaring every parameter `global` inside the function header
- B. Returning `a, b` packs and returns a 2-element `tuple` `(a, b)` that the caller can unpack
- C. Replacing every `return` statement with `break` inside the `def` body
- D. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- E. `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`

### 46. Complete `def timer_beeps():` / `    ____ 'ready'` / `    return` so calling `timer_beeps()` returns a generator iterator that produces `'ready'` on its first `next()` call. Which keyword fills the blank?

- A. `return`
- B. `yield`
- C. `break`
- D. `pass`

### 47. A kitchen timer uses a generator function containing `yield` statements. Which two statements accurately describe its runtime behaviour? Select two.

- A. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- B. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes
- C. Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet
- D. `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call
- E. Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production

### 48. A recursive menu-arrangement counter defines `def arrange(n): return 1 if n <= 1 else n * arrange(n - 1)` and calls `arrange(5)`. What integer is returned?

- A. `RecursionError`
- B. `15`
- C. `120`
- D. `24`

### 49. A dough-folding helper writes `def fold(k): return 1 + fold(k)` where `k` never changes and there is no base branch. Calling `fold(2)` causes which outcome?

- A. `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit
- B. `0`
- C. `SyntaxError`
- D. `None`

### 50. Given `def bake_mins(loaves, per_loaf=12, preheat=8): return loaves * per_loaf + preheat`, what integer does `bake_mins(2)` return?

- A. `32`
- B. `SyntaxError`
- C. `TypeError`
- D. `24`

### 51. Given `def bake_mins(loaves, per_loaf=12): return loaves * per_loaf`, what happens when a caller runs `bake_mins(loaves=2, trays=3)` passing an unknown keyword `trays`?

- A. `32`
- B. `KeyError`
- C. `TypeError`
- D. `None`

### 52. A shopping-list helper defines `def add_item(x, cart=[]): cart.append(x); return cart` and sees items carry over between separate recipes. Which two statements explain the cause and fix? Select two.

- A. Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production
- B. Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body
- C. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- D. Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument
- E. Declaring every parameter `global` inside the function header

### 53. Given `def cups_to_half(cups, divisor=2.0): return cups / divisor`, what float does `cups_to_half(7)` return?

- A. `3.5`
- B. `3`
- C. `TypeError`
- D. `2.5`

### 54. Complete `jar_total = 10` / `def use_jar():` / `    ____ jar_total` / `    jar_total -= 1` so calling `use_jar()` decrements module-level `jar_total` to `9`. Which keyword fills the blank?

- A. `with`
- B. `global`
- C. `nonlocal`
- D. `from`

### 55. A pantry script sets `base_salt = 3`, defines `def salted(grams): return grams + base_salt`, and calls `salted(10)`. What integer is returned?

- A. `UnboundLocalError`
- B. `3`
- C. `NameError`
- D. `13`

### 56. A recipe ratio block catches `except ArithmeticError:` around `grams / servings`. Why does that handler catch `ZeroDivisionError` when `servings` is `0`?

- A. `LookupError`
- B. `KeyError`
- C. `ArithmeticError`
- D. `ValueError`

### 57. Which built-in exception class is the direct parent of both `KeyError` and `IndexError` in Python 3?

- A. `SyntaxError`
- B. `LookupError`
- C. `TypeError`
- D. `ArithmeticError`

### 58. Complete `____ servings > 0, 'servings must be positive'` so a recipe invariant raises `AssertionError` if `servings <= 0`. Which keyword fills the blank?

- A. `assert`
- B. `finally`
- C. `except`
- D. `from`

### 59. A pantry CSV parser executes `grams = int('250g')` on a string containing trailing letter `'g'`. Which exception is raised?

- A. `IndexError`
- B. `KeyError`
- C. `TypeError`
- D. `ValueError`

### 60. A scaler runs `steps = []` then `try: steps.append('T'); _ = 10 // 0` / `except ZeroDivisionError: steps.append('X')` / `else: steps.append('E')` / `finally: steps.append('F')` and joins `steps` with `'-'`. Which two items accurately identify the joined output string and the rule governing `finally:`? Select two.

- A. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- B. The `finally:` block always runs on the way out — whether `try:` succeeded, an `except:` ran, an uncaught exception propagated, or `return` executed
- C. `T-X-F`
- D. `T-X-E-F`
- E. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes

---

## Answer key and explanations

### Question 1 — B

Answer: CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime. Standard CPython compiles `.py` source to bytecode and executes that bytecode inside the Python virtual machine at runtime rather than linking a native CPU binary ahead of time. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. CPython parses source into an AST and bytecode at import or execution time rather than burning microcode. Why the correct answer wins: Standard CPython compiles `.py` source to bytecode and executes that bytecode inside the Python virtual machine at runtime rather than linking a native CPU binary ahead of time.
- **B:** Correct. In this case: Standard CPython compiles `.py` source to bytecode and executes that bytecode inside the Python virtual machine at runtime rather than linking a native CPU binary ahead of time.
- **C:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Standard CPython compiles `.py` source to bytecode and executes that bytecode inside the Python virtual machine at runtime rather than linking a native CPU binary ahead of time.
- **D:** Incorrect for this question. CPython is a native host process written in C, not a browser-embedded DOM engine. Why the correct answer wins: Standard CPython compiles `.py` source to bytecode and executes that bytecode inside the Python virtual machine at runtime rather than linking a native CPU binary ahead of time.

### Question 2 — D

Answer: A lexical error because the character or token itself does not belong to valid Python token forms. Hexadecimal digits stop at `F`/`f`, so `'G'` breaks token formation at the lexical layer before grammar or runtime semantics are evaluated. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Why the correct answer wins: Hexadecimal digits stop at `F`/`f`, so `'G'` breaks token formation at the lexical layer before grammar or runtime semantics are evaluated.
- **B:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Hexadecimal digits stop at `F`/`f`, so `'G'` breaks token formation at the lexical layer before grammar or runtime semantics are evaluated.
- **C:** Incorrect for this question. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Why the correct answer wins: Hexadecimal digits stop at `F`/`f`, so `'G'` breaks token formation at the lexical layer before grammar or runtime semantics are evaluated.
- **D:** Correct. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. In this case: Hexadecimal digits stop at `F`/`f`, so `'G'` breaks token formation at the lexical layer before grammar or runtime semantics are evaluated.

### Question 3 — C, D

Answers: `del`; `lambda`. `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Python keywords are case-sensitive: `False` is reserved, whereas lowercase `false` is an ordinary identifier. Why the correct answer wins: `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved.
- **B:** Incorrect for this question. `case` is a soft keyword in Python 3.10+, so assigning `case = 1` remains legal outside `match` headers. Why the correct answer wins: `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved.
- **C:** Correct. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. In this case: `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved.
- **D:** Correct. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. In this case: `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved.
- **E:** Incorrect for this question. `dict` is a built-in type name in `builtins`, not a reserved keyword. Why the correct answer wins: `del` and `lambda` are hard reserved keywords in Python 3, whereas `case` is a soft keyword, `dict` is a built-in type identifier, and lowercase `false` is not reserved.

### Question 4 — B, C

Answers: `0o27`; `0x2A`. `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`. `0o27` is a valid octal integer literal equal to `2 * 8 + 7 == 23`. `0x2A` is a valid hexadecimal integer literal equal to `2 * 16 + 10 == 42`. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Consecutive underscores inside a numeric literal (`1__000`) raise `SyntaxError`. Why the correct answer wins: `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`.
- **B:** Correct. `0x2A` is a valid hexadecimal integer literal equal to `2 * 16 + 10 == 42`. In this case: `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`.
- **C:** Correct. `0o27` is a valid octal integer literal equal to `2 * 8 + 7 == 23`. In this case: `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`.
- **D:** Incorrect for this question. Binary literals allow only `0` and `1`, so `2` in `0b102` raises `SyntaxError`. Why the correct answer wins: `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`.
- **E:** Incorrect for this question. Numeric literals cannot end with a trailing underscore (`500_` raises `SyntaxError`). Why the correct answer wins: `0o27` (`23` in octal) and `0x2A` (`42` in hexadecimal) are valid integer literals, whereas `0b102`, `500_`, and `1__000` raise `SyntaxError`.

### Question 5 — C

Answer: `flour_grams_1`. `flour_grams_1` starts with a letter and uses lowercase letters, underscores, and digits, whereas `2nd_quarter`, `fx-rate`, and `total$usd` are invalid identifiers. `flour_grams_1` starts with a letter and uses snake_case recommended by PEP-8. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `fx-rate` is parsed as subtraction `fx - rate` because hyphens are illegal in Python identifiers. Why the correct answer wins: `flour_grams_1` starts with a letter and uses lowercase letters, underscores, and digits, whereas `2nd_quarter`, `fx-rate`, and `total$usd` are invalid identifiers.
- **B:** Incorrect for this question. `$` is not a valid identifier character in Python 3. Why the correct answer wins: `flour_grams_1` starts with a letter and uses lowercase letters, underscores, and digits, whereas `2nd_quarter`, `fx-rate`, and `total$usd` are invalid identifiers.
- **C:** Correct. `flour_grams_1` starts with a letter and uses snake_case recommended by PEP-8. In this case: `flour_grams_1` starts with a letter and uses lowercase letters, underscores, and digits, whereas `2nd_quarter`, `fx-rate`, and `total$usd` are invalid identifiers.
- **D:** Incorrect for this question. `2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier. Why the correct answer wins: `flour_grams_1` starts with a letter and uses lowercase letters, underscores, and digits, whereas `2nd_quarter`, `fx-rate`, and `total$usd` are invalid identifiers.

### Question 6 — D

Answer: `-4.0`. Floor division with at least one `float` operand returns a `float` rounded toward negative infinity (`math.floor(-3.4)` as a float), producing `-4.0`. Evaluates to the floating-point value `-4.0`. Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `-4`. Why the correct answer wins: Floor division with at least one `float` operand returns a `float` rounded toward negative infinity (`math.floor(-3.4)` as a float), producing `-4.0`.
- **B:** Incorrect for this question. Evaluates to the integer `-2`. Why the correct answer wins: Floor division with at least one `float` operand returns a `float` rounded toward negative infinity (`math.floor(-3.4)` as a float), producing `-4.0`.
- **C:** Incorrect for this question. Evaluates to the floating-point value `-3.0`. Why the correct answer wins: Floor division with at least one `float` operand returns a `float` rounded toward negative infinity (`math.floor(-3.4)` as a float), producing `-4.0`.
- **D:** Correct. Evaluates to the floating-point value `-4.0`. In this case: Floor division with at least one `float` operand returns a `float` rounded toward negative infinity (`math.floor(-3.4)` as a float), producing `-4.0`.

### Question 7 — B

Answer: `81`. Python evaluates `3 ** 3` (`27`) before multiplying by `3`, yielding `3 * 27 == 81`. Evaluates to the integer `81`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `18`. Why the correct answer wins: Python evaluates `3 ** 3` (`27`) before multiplying by `3`, yielding `3 * 27 == 81`.
- **B:** Correct. Evaluates to the integer `81`. In this case: Python evaluates `3 ** 3` (`27`) before multiplying by `3`, yielding `3 * 27 == 81`.
- **C:** Incorrect for this question. Evaluates to the integer `27`. Why the correct answer wins: Python evaluates `3 ** 3` (`27`) before multiplying by `3`, yielding `3 * 27 == 81`.
- **D:** Incorrect for this question. Evaluates to the integer `36`. Why the correct answer wins: Python evaluates `3 ** 3` (`27`) before multiplying by `3`, yielding `3 * 27 == 81`.

### Question 8 — B, D

Answers: `<<`; `>>`. `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic. Left shift `x << n` multiplies integer `x` by `2 ** n`. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic.
- **B:** Correct. Right shift `x >> n` floor-divides integer `x` by `2 ** n`. In this case: `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic.
- **C:** Incorrect for this question. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic.
- **D:** Correct. Left shift `x << n` multiplies integer `x` by `2 ** n`. In this case: `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic.
- **E:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `<<` shifts bits left and `>>` shifts bits right on integers, whereas `**` is exponentiation, `//` is floor division, and `and` is Boolean short-circuit logic.

### Question 9 — D

Answer: `*=`. `grams *= 3` multiplies `120` by `3` and rebinds `grams` to `360`. `*=` scales a number or repeats a sequence in place / by rebinding. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Why the correct answer wins: `grams *= 3` multiplies `120` by `3` and rebinds `grams` to `360`.
- **B:** Incorrect for this question. `+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets. Why the correct answer wins: `grams *= 3` multiplies `120` by `3` and rebinds `grams` to `360`.
- **C:** Incorrect for this question. `//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable. Why the correct answer wins: `grams *= 3` multiplies `120` by `3` and rebinds `grams` to `360`.
- **D:** Correct. `*=` scales a number or repeats a sequence in place / by rebinding. In this case: `grams *= 3` multiplies `120` by `3` and rebinds `grams` to `360`.

### Question 10 — C

Answer: `https://api.local/v2/users`. Passing `sep='/'` joins all three string arguments with forward slashes, outputting `https://api.local/v2/users`. `print('https://api.local', 'v2', 'users', sep='/')` joins all three strings with `'/'`. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. First `print('A', 'B', sep='-', end='/')` writes `A-B/`, and the second `print('C')` appends `C` on the same line. Why the correct answer wins: Passing `sep='/'` joins all three string arguments with forward slashes, outputting `https://api.local/v2/users`.
- **B:** Incorrect for this question. A line break between `B` and `C` appears only when `end` is left at its default newline. Why the correct answer wins: Passing `sep='/'` joins all three string arguments with forward slashes, outputting `https://api.local/v2/users`.
- **C:** Correct. `print('https://api.local', 'v2', 'users', sep='/')` joins all three strings with `'/'`. In this case: Passing `sep='/'` joins all three string arguments with forward slashes, outputting `https://api.local/v2/users`.
- **D:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Passing `sep='/'` joins all three string arguments with forward slashes, outputting `https://api.local/v2/users`.

### Question 11 — B

Answer: `chr`. Built-in `chr(65)` converts Unicode code point `65` into `'A'`, whereas `ord` performs the reverse conversion from character to integer. `chr(code)` returns the 1-character string for integer Unicode code point `code` (for example `chr(65) == 'A'`). Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: Built-in `chr(65)` converts Unicode code point `65` into `'A'`, whereas `ord` performs the reverse conversion from character to integer.
- **B:** Correct. `chr(code)` returns the 1-character string for integer Unicode code point `code` (for example `chr(65) == 'A'`). In this case: Built-in `chr(65)` converts Unicode code point `65` into `'A'`, whereas `ord` performs the reverse conversion from character to integer.
- **C:** Incorrect for this question. `float(...)` parses a numeric string such as `'19.95'` into a floating-point number. Why the correct answer wins: Built-in `chr(65)` converts Unicode code point `65` into `'A'`, whereas `ord` performs the reverse conversion from character to integer.
- **D:** Incorrect for this question. `ord(ch)` returns the integer Unicode code point of a 1-character string (for example `ord('A') == 65`). Why the correct answer wins: Built-in `chr(65)` converts Unicode code point `65` into `'A'`, whereas `ord` performs the reverse conversion from character to integer.

### Question 12 — B

Answer: `elif`. `elif` links an exclusive secondary condition to the initial `if` header. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `elif` links an exclusive secondary condition to the initial `if` header.
- **B:** Correct. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. In this case: `elif` links an exclusive secondary condition to the initial `if` header.
- **C:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: `elif` links an exclusive secondary condition to the initial `if` header.
- **D:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `elif` links an exclusive secondary condition to the initial `if` header.

### Question 13 — C

Answer: `WARN`. `days_left <= 0` and `days_left <= 2` are `False`, so the first true condition `days_left <= 5` prints `WARN`. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `ALERT`. Why the correct answer wins: `days_left <= 0` and `days_left <= 2` are `False`, so the first true condition `days_left <= 5` prints `WARN`.
- **B:** Incorrect for this question. Prints `CRIT`. Why the correct answer wins: `days_left <= 0` and `days_left <= 2` are `False`, so the first true condition `days_left <= 5` prints `WARN`.
- **C:** Correct. In this case: `days_left <= 0` and `days_left <= 2` are `False`, so the first true condition `days_left <= 5` prints `WARN`.
- **D:** Incorrect for this question. Prints `OK`. Why the correct answer wins: `days_left <= 0` and `days_left <= 2` are `False`, so the first true condition `days_left <= 5` prints `WARN`.

### Question 14 — C, E

Answers: `0 if subtotal >= 50 else 5`; `'VIP' if points >= 100 else 'STD'`. Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`.
- **B:** Incorrect for this question. Python has no `then` keyword and does not start an inline conditional expression with `if`. Why the correct answer wins: Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`.
- **C:** Correct. In this case: Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`.
- **D:** Incorrect for this question. A conditional expression (unlike a list comprehension filter) requires an `else` clause or raises `SyntaxError`. Why the correct answer wins: Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`.
- **E:** Correct. A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`. In this case: Python conditional expressions require `<when_true> if <cond> else <when_false>`; `? :`, missing `else`, and `if ... then` raise `SyntaxError`.

### Question 15 — C

Answer: `16`. Because both `if` statements execute independently, `grams` increases by `2` and then by `4` to reach `16`. Evaluates to the integer `16`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `11`. Why the correct answer wins: Because both `if` statements execute independently, `grams` increases by `2` and then by `4` to reach `16`.
- **B:** Incorrect for this question. Evaluates to the integer `14`. Why the correct answer wins: Because both `if` statements execute independently, `grams` increases by `2` and then by `4` to reach `16`.
- **C:** Correct. Evaluates to the integer `16`. In this case: Because both `if` statements execute independently, `grams` increases by `2` and then by `4` to reach `16`.
- **D:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Because both `if` statements execute independently, `grams` increases by `2` and then by `4` to reach `16`.

### Question 16 — A, D

Answers: `(0,)`; `{0: None}`. `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy. `(0,)` is a 1-element tuple (`len((0,)) == 1`), so it evaluates to `True` even though its element is `0`. `{0: None}` has one key-value entry (`len == 1`), so it evaluates to `True`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `{0: None}` has one key-value entry (`len == 1`), so it evaluates to `True`. In this case: `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy.
- **B:** Incorrect for this question. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy.
- **C:** Incorrect for this question. An empty tuple `()` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy.
- **D:** Correct. `(0,)` is a 1-element tuple (`len((0,)) == 1`), so it evaluates to `True` even though its element is `0`. In this case: `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy.
- **E:** Incorrect for this question. Numeric zero `0.0` evaluates to `False` in a Boolean context. Why the correct answer wins: `(0,)` has one tuple element and `{0: None}` has one dictionary entry, so both have `len == 1` and evaluate to `True`, whereas `()`, `{}`, and `0.0` are falsy.

### Question 17 — A

Answer: `IDLE`. An empty list `[]` has length `0` and is falsy, so Python runs the `else` branch and prints `IDLE`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. In this case: An empty list `[]` has length `0` and is falsy, so Python runs the `else` branch and prints `IDLE`.
- **B:** Incorrect for this question. Prints `OK`. Why the correct answer wins: An empty list `[]` has length `0` and is falsy, so Python runs the `else` branch and prints `IDLE`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: An empty list `[]` has length `0` and is falsy, so Python runs the `else` branch and prints `IDLE`.
- **D:** Incorrect for this question. Prints `WARN`. Why the correct answer wins: An empty list `[]` has length `0` and is falsy, so Python runs the `else` branch and prints `IDLE`.

### Question 18 — A

Answer: `not`. `not pantry_empty` negates `False` to `True`. `not` is Python's unary logical negation operator and returns `True` or `False`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `not` is Python's unary logical negation operator and returns `True` or `False`. In this case: `not pantry_empty` negates `False` to `True`.
- **B:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `not pantry_empty` negates `False` to `True`.
- **C:** Incorrect for this question. `or` is Python's short-circuit logical disjunction operator. Why the correct answer wins: `not pantry_empty` negates `False` to `True`.
- **D:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `not pantry_empty` negates `False` to `True`.

### Question 19 — A

Answer: `False`. Python evaluates `(not True) and False`, where `not True` is `False` and `False and False` short-circuits to `False`. Evaluates to Boolean `False`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to Boolean `False`. In this case: Python evaluates `(not True) and False`, where `not True` is `False` and `False and False` short-circuits to `False`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Python evaluates `(not True) and False`, where `not True` is `False` and `False and False` short-circuits to `False`.
- **C:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Python evaluates `(not True) and False`, where `not True` is `False` and `False and False` short-circuits to `False`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Python evaluates `(not True) and False`, where `not True` is `False` and `False and False` short-circuits to `False`.

### Question 20 — C

Answer: `while`. `while` re-evaluates `cups_needed >= 2` before every scoop iteration. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `while` re-evaluates `cups_needed >= 2` before every scoop iteration.
- **B:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` re-evaluates `cups_needed >= 2` before every scoop iteration.
- **C:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` re-evaluates `cups_needed >= 2` before every scoop iteration.
- **D:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` re-evaluates `cups_needed >= 2` before every scoop iteration.

### Question 21 — C, E

Answers: `n = 6` followed by `while n > 0: n -= 2`; `n = 16` followed by `while n >= 2: n //= 2`. Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Adding `2` to an even integer keeps `n` even on every step, so `n % 2 == 0` never turns `False`. Why the correct answer wins: Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations.
- **B:** Incorrect for this question. Because `pass` never updates `n`, `n > 0` remains `True` indefinitely. Why the correct answer wins: Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations.
- **C:** Correct. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. In this case: Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations.
- **D:** Incorrect for this question. Incrementing a positive integer keeps `n > 0` forever, producing an infinite loop. Why the correct answer wins: Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations.
- **E:** Correct. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. In this case: Subtracting `2` from `6` while `n > 0` and floor-dividing `16` by `2` while `n >= 2` both make their loop conditions `False` in finitely many iterations.

### Question 22 — C, D

Answers: `range(8, 2)`; `range(2, 8, -2)`. `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `range(10, 2, -2)` generates `10, 8, 6, 4` (four integers). Why the correct answer wins: `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements.
- **B:** Incorrect for this question. `range(3, 12, 3)` generates `3, 6, 9` (three integers). Why the correct answer wins: `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements.
- **C:** Correct. `range(2, 8, -2)` steps downward away from `8`, yielding zero items. In this case: `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements.
- **D:** Correct. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. In this case: `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements.
- **E:** Incorrect for this question. `range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers). Why the correct answer wins: `range(8, 2)` with positive default step `+1` and `range(2, 8, -2)` with negative step `-2` both start beyond their stop direction and yield zero elements.

### Question 23 — C

Answer: `18`. `range(3, 12, 3)` generates `3, 6, 9` (stopping before exclusive `12`), whose sum is `18`. Evaluates to the integer `18`. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `27`. Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` (stopping before exclusive `12`), whose sum is `18`.
- **B:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` (stopping before exclusive `12`), whose sum is `18`.
- **C:** Correct. Evaluates to the integer `18`. In this case: `range(3, 12, 3)` generates `3, 6, 9` (stopping before exclusive `12`), whose sum is `18`.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` (stopping before exclusive `12`), whose sum is `18`.

### Question 24 — D

Answer: `2`. Iterating directly over `'JAR-04-B'` visits `'-'` twice, incrementing `dashes` to `2`. Evaluates to the integer `2`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Iterating directly over `'JAR-04-B'` visits `'-'` twice, incrementing `dashes` to `2`.
- **B:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Iterating directly over `'JAR-04-B'` visits `'-'` twice, incrementing `dashes` to `2`.
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Iterating directly over `'JAR-04-B'` visits `'-'` twice, incrementing `dashes` to `2`.
- **D:** Correct. Evaluates to the integer `2`. In this case: Iterating directly over `'JAR-04-B'` visits `'-'` twice, incrementing `dashes` to `2`.

### Question 25 — B

Answer: `break`. `break` exits the enclosing `for` loop right away without inspecting `'rice'`. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `break` exits the enclosing `for` loop right away without inspecting `'rice'`.
- **B:** Correct. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. In this case: `break` exits the enclosing `for` loop right away without inspecting `'rice'`.
- **C:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `break` exits the enclosing `for` loop right away without inspecting `'rice'`.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `break` exits the enclosing `for` loop right away without inspecting `'rice'`.

### Question 26 — B

Answer: `pass`. `pass` provides the required statement in an otherwise empty indented block. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Why the correct answer wins: `pass` provides the required statement in an otherwise empty indented block.
- **B:** Correct. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. In this case: `pass` provides the required statement in an otherwise empty indented block.
- **C:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `pass` provides the required statement in an otherwise empty indented block.
- **D:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `pass` provides the required statement in an otherwise empty indented block.

### Question 27 — C

Answer: `CLEAN`. When a `while` condition evaluates to `False` naturally — even before executing a single iteration — its `else:` suite runs and prints `CLEAN`. Prints `CLEAN` from the loop `else` suite. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: When a `while` condition evaluates to `False` naturally — even before executing a single iteration — its `else:` suite runs and prints `CLEAN`.
- **B:** Incorrect for this question. Prints `HALT` before `break` skips the loop `else` suite. Why the correct answer wins: When a `while` condition evaluates to `False` naturally — even before executing a single iteration — its `else:` suite runs and prints `CLEAN`.
- **C:** Correct. Prints `CLEAN` from the loop `else` suite. In this case: When a `while` condition evaluates to `False` naturally — even before executing a single iteration — its `else:` suite runs and prints `CLEAN`.
- **D:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: When a `while` condition evaluates to `False` naturally — even before executing a single iteration — its `else:` suite runs and prints `CLEAN`.

### Question 28 — A

Answer: `8`. Two soups paired with four breads runs the inner body `2 * 4 == 8` times. Evaluates to the integer `8`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `8`. In this case: Two soups paired with four breads runs the inner body `2 * 4 == 8` times.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Two soups paired with four breads runs the inner body `2 * 4 == 8` times.
- **C:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Two soups paired with four breads runs the inner body `2 * 4 == 8` times.
- **D:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Two soups paired with four breads runs the inner body `2 * 4 == 8` times.

### Question 29 — D

Answer: `[20, 30]`. In a 5-element list, `-4` maps to index `1` (`20`) and exclusive `-2` maps to index `3` (`40`), returning `[20, 30]`. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: In a 5-element list, `-4` maps to index `1` (`20`) and exclusive `-2` maps to index `3` (`40`), returning `[20, 30]`.
- **B:** Incorrect for this question. Slice `[-2:]` returns the last two items `[40, 50]`. Why the correct answer wins: In a 5-element list, `-4` maps to index `1` (`20`) and exclusive `-2` maps to index `3` (`40`), returning `[20, 30]`.
- **C:** Incorrect for this question. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. Why the correct answer wins: In a 5-element list, `-4` maps to index `1` (`20`) and exclusive `-2` maps to index `3` (`40`), returning `[20, 30]`.
- **D:** Correct. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. In this case: In a 5-element list, `-4` maps to index `1` (`20`) and exclusive `-2` maps to index `3` (`40`), returning `[20, 30]`.

### Question 30 — C

Answer: `[1, 2, 3, 4]`. `.extend([3, 4])` unpacks its iterable argument and appends `3` and `4` as top-level elements, printing `[1, 2, 3, 4]`. `.extend([3, 4])` iterates its argument and appends each element individually. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `.extend([3, 4])` unpacks its iterable argument and appends `3` and `4` as top-level elements, printing `[1, 2, 3, 4]`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: `.extend([3, 4])` unpacks its iterable argument and appends `3` and `4` as top-level elements, printing `[1, 2, 3, 4]`.
- **C:** Correct. `.extend([3, 4])` iterates its argument and appends each element individually. In this case: `.extend([3, 4])` unpacks its iterable argument and appends `3` and `4` as top-level elements, printing `[1, 2, 3, 4]`.
- **D:** Incorrect for this question. `.append([3, 4])` adds the entire list object as a single nested third element. Why the correct answer wins: `.extend([3, 4])` unpacks its iterable argument and appends `3` and `4` as top-level elements, printing `[1, 2, 3, 4]`.

### Question 31 — A

Answer: `append`. `steps.append('bake')` adds `'bake'` as one element, whereas `steps.extend('bake')` would iterate the string's four characters. `.append(item)` adds `item` as a single element at the end of a list. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `.append(item)` adds `item` as a single element at the end of a list. In this case: `steps.append('bake')` adds `'bake'` as one element, whereas `steps.extend('bake')` would iterate the string's four characters.
- **B:** Incorrect for this question. `.remove(value)` removes the first matching `value` by equality. Why the correct answer wins: `steps.append('bake')` adds `'bake'` as one element, whereas `steps.extend('bake')` would iterate the string's four characters.
- **C:** Incorrect for this question. `.extend(iterable)` appends each element yielded by `iterable` to the list. Why the correct answer wins: `steps.append('bake')` adds `'bake'` as one element, whereas `steps.extend('bake')` would iterate the string's four characters.
- **D:** Incorrect for this question. `.pop([index])` removes and returns the element at `index` (default `-1`). Why the correct answer wins: `steps.append('bake')` adds `'bake'` as one element, whereas `steps.extend('bake')` would iterate the string's four characters.

### Question 32 — A, B

Answers: `items.insert(0, x)`; `items.sort()`. `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists. `.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place. `items.sort()` sorts the list in place and returns `None` rather than a new list. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `items.sort()` sorts the list in place and returns `None` rather than a new list. In this case: `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **B:** Correct. `.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place. In this case: `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **C:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **D:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.
- **E:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: `items.insert(0, x)` and `items.sort()` mutate `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` return new lists.

### Question 33 — A

Answer: `del`. `del pantry[1]` deletes the element at index `1` directly from `pantry`. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices. In this case: `del pantry[1]` deletes the element at index `1` directly from `pantry`.
- **B:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `del pantry[1]` deletes the element at index `1` directly from `pantry`.
- **C:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `del pantry[1]` deletes the element at index `1` directly from `pantry`.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `del pantry[1]` deletes the element at index `1` directly from `pantry`.

### Question 34 — C, E

Answers: `items[:]`; `items.copy()`. Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements. `items[:]` creates a shallow copy as a new outer list object. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent. Why the correct answer wins: Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements.
- **B:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements.
- **C:** Correct. `items[:]` creates a shallow copy as a new outer list object. In this case: Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements.
- **D:** Incorrect for this question. `items.pop()` removes and returns the last element (or element at index `i`), mutating `items`. Why the correct answer wins: Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements.
- **E:** Correct. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. In this case: Both `items[:]` and `items.copy()` allocate a separate outer list containing the same elements.

### Question 35 — A

Answer: `for`. List comprehensions iterate using a `for <var> in <iterable>` clause. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. In this case: List comprehensions iterate using a `for <var> in <iterable>` clause.
- **B:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: List comprehensions iterate using a `for <var> in <iterable>` clause.
- **C:** Incorrect for this question. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Why the correct answer wins: List comprehensions iterate using a `for <var> in <iterable>` clause.
- **D:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: List comprehensions iterate using a `for <var> in <iterable>` clause.

### Question 36 — A

Answer: `in`. `in` tests whether `'gluten'` equals any element of `allergens`. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. In this case: `in` tests whether `'gluten'` equals any element of `allergens`.
- **B:** Incorrect for this question. `or` is Python's short-circuit logical disjunction operator. Why the correct answer wins: `in` tests whether `'gluten'` equals any element of `allergens`.
- **C:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `in` tests whether `'gluten'` equals any element of `allergens`.
- **D:** Incorrect for this question. `not` is Python's unary logical negation operator and returns `True` or `False`. Why the correct answer wins: `in` tests whether `'gluten'` equals any element of `allergens`.

### Question 37 — B, E

Answers: `(42,)`; `42,`. `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`.
- **B:** Correct. A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`). In this case: `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`.
- **C:** Incorrect for this question. `tuple()` with no arguments returns the empty 0-element tuple `()`, not a 1-element tuple. Why the correct answer wins: `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`.
- **D:** Incorrect for this question. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Why the correct answer wins: `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`.
- **E:** Correct. Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`. In this case: `(42,)` and `42,` both include the trailing comma required to construct a singleton `tuple`.

### Question 38 — B

Answer: `-6`. Two's-complement inversion `~x` equals `-(x + 1)`, so `~5` evaluates to `-6`. Evaluates to the integer `-6`. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Two's-complement inversion `~x` equals `-(x + 1)`, so `~5` evaluates to `-6`.
- **B:** Correct. Evaluates to the integer `-6`. In this case: Two's-complement inversion `~x` equals `-(x + 1)`, so `~5` evaluates to `-6`.
- **C:** Incorrect for this question. Evaluates to the integer `-2`. Why the correct answer wins: Two's-complement inversion `~x` equals `-(x + 1)`, so `~5` evaluates to `-6`.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Two's-complement inversion `~x` equals `-(x + 1)`, so `~5` evaluates to `-6`.

### Question 39 — A, C

Answers: `rates.get('CHF', 0)`; `rates.pop('CHF', 0)`. `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`. `.get('CHF', 0)` returns the value for `'CHF'` if present or `0` if `'CHF'` is missing without raising `KeyError`. `.pop(k, default)` removes and returns `rates[k]` if found, or returns `default` without `KeyError` when `k` is absent. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `.pop(k, default)` removes and returns `rates[k]` if found, or returns `default` without `KeyError` when `k` is absent. In this case: `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`.
- **B:** Incorrect for this question. Unparenthesized `except A, B:` was Python 2 syntax and raises `SyntaxError` in Python 3. Why the correct answer wins: `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`.
- **C:** Correct. `.get('CHF', 0)` returns the value for `'CHF'` if present or `0` if `'CHF'` is missing without raising `KeyError`. In this case: `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`.
- **D:** Incorrect for this question. Direct indexing `rates['CHF']` raises `KeyError` when `'CHF'` is absent from `rates`. Why the correct answer wins: `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`.
- **E:** Incorrect for this question. Passing `100` to `base` positionally and `base=200` by keyword raises `TypeError`. Why the correct answer wins: `rates.get('CHF', 0)` and `rates.pop('CHF', 0)` both return `0` when `'CHF'` is absent, whereas `rates['CHF']` raises `KeyError`.

### Question 40 — D

Answer: `items`. `recipe.items()` returns a view of `(key, value)` 2-tuples for simultaneous unpacking. `d.items()` returns a view of `(key, value)` pairs. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.pop([index])` removes and returns the element at `index` (default `-1`). Why the correct answer wins: `recipe.items()` returns a view of `(key, value)` 2-tuples for simultaneous unpacking.
- **B:** Incorrect for this question. `d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing. Why the correct answer wins: `recipe.items()` returns a view of `(key, value)` 2-tuples for simultaneous unpacking.
- **C:** Incorrect for this question. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Why the correct answer wins: `recipe.items()` returns a view of `(key, value)` 2-tuples for simultaneous unpacking.
- **D:** Correct. `d.items()` returns a view of `(key, value)` pairs. In this case: `recipe.items()` returns a view of `(key, value)` 2-tuples for simultaneous unpacking.

### Question 41 — B

Answer: `'nohtyP'`. Slicing with `[::-1]` traverses `'Python'` from right to left by `-1`, returning `'nohtyP'`. `'Python'[::-1]` steps backward from the end and returns `'nohtyP'`. Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `'Python'[::2]` picks characters at indices `0`, `2`, and `4`, returning `'Pto'`. Why the correct answer wins: Slicing with `[::-1]` traverses `'Python'` from right to left by `-1`, returning `'nohtyP'`.
- **B:** Correct. `'Python'[::-1]` steps backward from the end and returns `'nohtyP'`. In this case: Slicing with `[::-1]` traverses `'Python'` from right to left by `-1`, returning `'nohtyP'`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Slicing with `[::-1]` traverses `'Python'` from right to left by `-1`, returning `'nohtyP'`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Slicing with `[::-1]` traverses `'Python'` from right to left by `-1`, returning `'nohtyP'`.

### Question 42 — D

Answer: String case methods such as `.upper()`, `.lower()`, and `.title()` always return a new string and leave the original unchanged. Because `str` objects are immutable, `.upper()` returns a new string `'THYME'` and leaves `spice` bound to `'thyme'`. Because strings are immutable in Python, every transformation method allocates and returns a new `str`. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Standard `<` and `>` on strings are case-sensitive code-point comparisons. Why the correct answer wins: Because `str` objects are immutable, `.upper()` returns a new string `'THYME'` and leaves `spice` bound to `'thyme'`.
- **B:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: Because `str` objects are immutable, `.upper()` returns a new string `'THYME'` and leaves `spice` bound to `'thyme'`.
- **C:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Because `str` objects are immutable, `.upper()` returns a new string `'THYME'` and leaves `spice` bound to `'thyme'`.
- **D:** Correct. Because strings are immutable in Python, every transformation method allocates and returns a new `str`. In this case: Because `str` objects are immutable, `.upper()` returns a new string `'THYME'` and leaves `spice` bound to `'thyme'`.

### Question 43 — D

Answer: `find`. `str.find()` returns `-1` when a substring is not found, whereas `str.index()` raises `ValueError`. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `s.index(sub)` returns the lowest index of `sub`, or raises `ValueError` if `sub` is absent. Why the correct answer wins: `str.find()` returns `-1` when a substring is not found, whereas `str.index()` raises `ValueError`.
- **B:** Incorrect for this question. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. Why the correct answer wins: `str.find()` returns `-1` when a substring is not found, whereas `str.index()` raises `ValueError`.
- **C:** Incorrect for this question. `s.replace(old, new)` returns a new string where occurrences of `old` are replaced with `new`. Why the correct answer wins: `str.find()` returns `-1` when a substring is not found, whereas `str.index()` raises `ValueError`.
- **D:** Correct. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. In this case: `str.find()` returns `-1` when a substring is not found, whereas `str.index()` raises `ValueError`.

### Question 44 — D

Answer: `def`. `def` introduces a named function definition in Python 3. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `function` is a JavaScript keyword, not a Python keyword; Python uses `def`. Why the correct answer wins: `def` introduces a named function definition in Python 3.
- **B:** Incorrect for this question. `var` is not a Python keyword; Python binds variables directly on assignment. Why the correct answer wins: `def` introduces a named function definition in Python 3.
- **C:** Incorrect for this question. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. Why the correct answer wins: `def` introduces a named function definition in Python 3.
- **D:** Correct. In this case: `def` introduces a named function definition in Python 3.

### Question 45 — B, E

Answers: `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`; Returning `a, b` packs and returns a 2-element `tuple` `(a, b)` that the caller can unpack. Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. A comma-separated expression after `return` returns a single `tuple` object. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`.
- **B:** Correct. A comma-separated expression after `return` returns a single `tuple` object. In this case: Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`.
- **C:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`.
- **D:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`.
- **E:** Correct. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. In this case: Omitting a `return` value returns `None`, and writing `return a, b` packs and returns a 2-element `tuple` `(a, b)`.

### Question 46 — B

Answer: `yield`. `yield` compiles `timer_beeps` as a generator function. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `yield` compiles `timer_beeps` as a generator function.
- **B:** Correct. `yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item. In this case: `yield` compiles `timer_beeps` as a generator function.
- **C:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `yield` compiles `timer_beeps` as a generator function.
- **D:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `yield` compiles `timer_beeps` as a generator function.

### Question 47 — C, D

Answers: Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet; `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call. Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step.
- **B:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step.
- **C:** Correct. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. In this case: Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step.
- **D:** Correct. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. In this case: Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step.
- **E:** Incorrect for this question. `.pyc` files are neither encrypted nor able to bypass syntax validation. Why the correct answer wins: Calling the function returns a generator iterator before running the body, and each `yield` pauses local variables until the next `next()` step.

### Question 48 — C

Answer: `120`. `arrange(5)` computes `5 * 4 * 3 * 2 * 1`, reaching `n <= 1` and returning `120`. Evaluates to the integer `120`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `arrange(5)` computes `5 * 4 * 3 * 2 * 1`, reaching `n <= 1` and returning `120`.
- **B:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: `arrange(5)` computes `5 * 4 * 3 * 2 * 1`, reaching `n <= 1` and returning `120`.
- **C:** Correct. Evaluates to the integer `120`. In this case: `arrange(5)` computes `5 * 4 * 3 * 2 * 1`, reaching `n <= 1` and returning `120`.
- **D:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: `arrange(5)` computes `5 * 4 * 3 * 2 * 1`, reaching `n <= 1` and returning `120`.

### Question 49 — A

Answer: `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit. Because `fold(2)` calls `fold(2)` endlessly without a base case, CPython raises `RecursionError`. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). In this case: Because `fold(2)` calls `fold(2)` endlessly without a base case, CPython raises `RecursionError`.
- **B:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Because `fold(2)` calls `fold(2)` endlessly without a base case, CPython raises `RecursionError`.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Because `fold(2)` calls `fold(2)` endlessly without a base case, CPython raises `RecursionError`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Because `fold(2)` calls `fold(2)` endlessly without a base case, CPython raises `RecursionError`.

### Question 50 — A

Answer: `32`. `loaves` is `2`, while `per_loaf` and `preheat` use defaults `12` and `8`, returning `2 * 12 + 8 == 32`. Evaluates to the integer `32`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `32`. In this case: `loaves` is `2`, while `per_loaf` and `preheat` use defaults `12` and `8`, returning `2 * 12 + 8 == 32`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `loaves` is `2`, while `per_loaf` and `preheat` use defaults `12` and `8`, returning `2 * 12 + 8 == 32`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `loaves` is `2`, while `per_loaf` and `preheat` use defaults `12` and `8`, returning `2 * 12 + 8 == 32`.
- **D:** Incorrect for this question. Evaluates to the integer `24`. Why the correct answer wins: `loaves` is `2`, while `per_loaf` and `preheat` use defaults `12` and `8`, returning `2 * 12 + 8 == 32`.

### Question 51 — C

Answer: `TypeError`. Passing an unexpected keyword argument `trays` not present in the signature raises `TypeError`. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `32`. Why the correct answer wins: Passing an unexpected keyword argument `trays` not present in the signature raises `TypeError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Passing an unexpected keyword argument `trays` not present in the signature raises `TypeError`.
- **C:** Correct. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. In this case: Passing an unexpected keyword argument `trays` not present in the signature raises `TypeError`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Passing an unexpected keyword argument `trays` not present in the signature raises `TypeError`.

### Question 52 — B, D

Answers: Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument; Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body. Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `.pyc` files are neither encrypted nor able to bypass syntax validation. Why the correct answer wins: Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call.
- **B:** Correct. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. In this case: Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call.
- **C:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call.
- **D:** Correct. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. In this case: Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call.
- **E:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Default `cart=[]` is evaluated once at `def` time and shared across default calls; `cart=None` with `if cart is None: cart = []` creates a new list per call.

### Question 53 — A

Answer: `3.5`. Using default `divisor=2.0`, `7 / 2.0` evaluates to `3.5`. Evaluates to the floating-point value `3.5`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the floating-point value `3.5`. In this case: Using default `divisor=2.0`, `7 / 2.0` evaluates to `3.5`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Using default `divisor=2.0`, `7 / 2.0` evaluates to `3.5`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: Using default `divisor=2.0`, `7 / 2.0` evaluates to `3.5`.
- **D:** Incorrect for this question. Evaluates to the floating-point value `2.5`. Why the correct answer wins: Using default `divisor=2.0`, `7 / 2.0` evaluates to `3.5`.

### Question 54 — B

Answer: `global`. `global jar_total` binds augmented assignment inside `use_jar` to the module-level variable. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `global jar_total` binds augmented assignment inside `use_jar` to the module-level variable.
- **B:** Correct. `global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace. In this case: `global jar_total` binds augmented assignment inside `use_jar` to the module-level variable.
- **C:** Incorrect for this question. `nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope. Why the correct answer wins: `global jar_total` binds augmented assignment inside `use_jar` to the module-level variable.
- **D:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `global jar_total` binds augmented assignment inside `use_jar` to the module-level variable.

### Question 55 — D

Answer: `13`. `salted` reads `base_salt` without assigning to it, resolving `3` in module scope via LEGB and returning `13`. Evaluates to the integer `13`. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. Why the correct answer wins: `salted` reads `base_salt` without assigning to it, resolving `3` in module scope via LEGB and returning `13`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: `salted` reads `base_salt` without assigning to it, resolving `3` in module scope via LEGB and returning `13`.
- **C:** Incorrect for this question. `NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope. Why the correct answer wins: `salted` reads `base_salt` without assigning to it, resolving `3` in module scope via LEGB and returning `13`.
- **D:** Correct. Evaluates to the integer `13`. In this case: `salted` reads `base_salt` without assigning to it, resolving `3` in module scope via LEGB and returning `13`.

### Question 56 — C

Answer: `ArithmeticError`. `ZeroDivisionError` is a direct subclass of `ArithmeticError`. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Why the correct answer wins: `ZeroDivisionError` is a direct subclass of `ArithmeticError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `ZeroDivisionError` is a direct subclass of `ArithmeticError`.
- **C:** Correct. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. In this case: `ZeroDivisionError` is a direct subclass of `ArithmeticError`.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `ZeroDivisionError` is a direct subclass of `ArithmeticError`.

### Question 57 — B

Answer: `LookupError`. `LookupError` sits immediately above `KeyError` and `IndexError` under `Exception`. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: `LookupError` sits immediately above `KeyError` and `IndexError` under `Exception`.
- **B:** Correct. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. In this case: `LookupError` sits immediately above `KeyError` and `IndexError` under `Exception`.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `LookupError` sits immediately above `KeyError` and `IndexError` under `Exception`.
- **D:** Incorrect for this question. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Why the correct answer wins: `LookupError` sits immediately above `KeyError` and `IndexError` under `Exception`.

### Question 58 — A

Answer: `assert`. `assert` checks the condition and raises `AssertionError` when it evaluates to `False`. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. In this case: `assert` checks the condition and raises `AssertionError` when it evaluates to `False`.
- **B:** Incorrect for this question. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Why the correct answer wins: `assert` checks the condition and raises `AssertionError` when it evaluates to `False`.
- **C:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `assert` checks the condition and raises `AssertionError` when it evaluates to `False`.
- **D:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `assert` checks the condition and raises `AssertionError` when it evaluates to `False`.

### Question 59 — D

Answer: `ValueError`. `int()` accepts a `str` argument (`TypeError` does not apply) and raises `ValueError` because `'250g'` is not a valid base-10 integer string. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: `int()` accepts a `str` argument (`TypeError` does not apply) and raises `ValueError` because `'250g'` is not a valid base-10 integer string.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `int()` accepts a `str` argument (`TypeError` does not apply) and raises `ValueError` because `'250g'` is not a valid base-10 integer string.
- **C:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `int()` accepts a `str` argument (`TypeError` does not apply) and raises `ValueError` because `'250g'` is not a valid base-10 integer string.
- **D:** Correct. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). In this case: `int()` accepts a `str` argument (`TypeError` does not apply) and raises `ValueError` because `'250g'` is not a valid base-10 integer string.

### Question 60 — B, C

Answers: `T-X-F`; The `finally:` block always runs on the way out — whether `try:` succeeded, an `except:` ran, an uncaught exception propagated, or `return` executed. Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes. When `try:` raises a caught exception after printing `T`, Python runs the matching `except` (`X`) and then `finally` (`F`), skipping `else`. `finally:` is guaranteed cleanup code that runs before control leaves the `try` statement. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes.
- **B:** Correct. `finally:` is guaranteed cleanup code that runs before control leaves the `try` statement. In this case: Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes.
- **C:** Correct. When `try:` raises a caught exception after printing `T`, Python runs the matching `except` (`X`) and then `finally` (`F`), skipping `else`. In this case: Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes.
- **D:** Incorrect for this question. `except:` and `else:` are mutually exclusive on any single execution of a `try` statement. Why the correct answer wins: Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes.
- **E:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: Because `10 // 0` is caught by `except ZeroDivisionError:`, `else` is skipped and `finally` runs on exit, producing `T-X-F` while guaranteeing `finally:` always executes.
