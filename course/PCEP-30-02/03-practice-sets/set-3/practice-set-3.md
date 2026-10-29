# PCEP – Certified Entry-Level Python Programmer (PCEP-30-02) — Full-Length Mock Exam 3

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 15 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). The live PCEP-30-02 exam has 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item set is an expanded 2x bank timed at 80 minutes to preserve the live pace of about 80 seconds per item. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. Version note: PCEP-30-03 is scheduled for release on October 31, 2026; PCEP-30-02 remains active and earned credentials retain their five-year validity. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. Before CPython translates anything into bytecode for an inventory counter script, what role does the `.py` file on disk play?

- A. A static linker merges Python modules into firmware without needing a runtime interpreter
- B. CPython links source directly into a standalone machine-code binary before the user runs the script
- C. Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it
- D. The plain-text file holding Python instructions written by the programmer

### 2. When reviewing errors in a shopping-cart script, which two statements accurately distinguish lexis, syntax, and semantics? Select two.

- A. Lexis runs only after the program finishes printing its output
- B. Lexis checks that each individual token is legal, whereas syntax checks how tokens are arranged into statements
- C. `True`, because Python stores decimal fractions exactly to two decimal places
- D. Style formatting comments automatically bypass syntax checking during parsing
- E. Semantics determines runtime meaning, so `10 / 0` passes lexis and syntax yet fails at runtime

### 3. An inventory module defines SKU fields. Which two words are reserved Python keywords that raise `SyntaxError` if used as variable names? Select two.

- A. `true`
- B. `print`
- C. `import`
- D. `class`
- E. `_temp_value`

### 4. A warehouse stock limit table writes numeric literals in Python 3. Which two literals are syntactically valid? Select two.

- A. `017`
- B. `4e3`
- C. `0o18`
- D. `1_000_000`
- E. `0x1G`

### 5. An inventory discount script mixes two-space and four-space indentation inside the same `if` block and fails with `IndentationError`. Which Python rule did it violate?

- A. Style formatting comments automatically bypass syntax checking during parsing
- B. Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it
- C. Compiled native binaries require every end user to keep the original C compiler installed to launch the binary
- D. Every statement in the same suite must share the exact same indentation width

### 6. A cart per-unit check evaluates `unit_cost = 10 / 2`. What exact value and type representation does `print(unit_cost)` display?

- A. `5`
- B. `2`
- C. Raises `TypeError`
- D. `5.0`

### 7. A shipping surcharge formula computes `fee = 2 + 3 * 4 ** 2`. Which integer is assigned to `fee`?

- A. `50`
- B. `22`
- C. `100`
- D. `32`

### 8. Complete `scaled = 5 ____ 2` so shifting `5` (`0b0101`) two bit positions to the left multiplies it by `4` to produce `20`. Which bitwise operator fills the blank?

- A. `>>`
- B. `<<`
- C. `%`
- D. `&`

### 9. Complete `divider = '-'` / `divider ____ 4` so augmented assignment repeats the string in place of retyping `divider = divider * 4` to produce `'----'`. Which operator fills the blank?

- A. `*=`
- B. `//=`
- C. `**`
- D. `+=`

### 10. An export helper executes `print('red', 'green', 'blue', sep=';')`. What text is written to standard output?

- A. `a b`
- B. `red;green;blue`
- C. Raises `TypeError`
- D. `a-b-c!`

### 11. A stock adjustment evaluates `delta = int(-3.9)` in Python 3. Which value is bound to `delta`?

- A. Raises `ValueError`
- B. `-3`
- C. `-3.0`
- D. `-4`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass

### 12. A cart promo check sets `qty = 12; label = ''` and runs two separate `if` statements: `if qty > 5: label += 'A'` followed by `if qty > 10: label += ' B'`. What is `label`?

- A. `A B`
- B. `B`
- C. Nothing is printed (zero iterations)
- D. `A`

### 13. Complete `if cart_total ____ 50:` so free shipping applies when `cart_total` is `50` or anything higher. Which relational operator fills the blank?

- A. `<=`
- B. `>`
- C. `>=`
- D. `=`

### 14. When checking whether a customer's saved-coupons container is empty via `if not coupons:`, for which two values of `coupons` does `not coupons` evaluate to `True`? Select two.

- A. `'False'`
- B. `()`
- C. `[0]`
- D. `(7,)`
- E. `{}`

### 15. A stock check sets `bins = [0]` and runs `if bins: print('A')` / `else: print('B')`. What does it print?

- A. `B`
- B. `D`
- C. Nothing is printed (zero iterations)
- D. `A`

### 16. A reorder alert triggers only when warehouse quantity `x` is at least `10` and at most `20`. Which two conditions express that inclusive check in Python 3? Select two.

- A. `x >= 10 and x = 20`
- B. `(x >= 10) or (x <= 20)`
- C. `10 <= x & x <= 20`
- D. `(x >= 10) and (x <= 20)`
- E. `10 <= x <= 20`

### 17. An eligibility flag evaluates `eligible = True or False and False`. What Boolean value is assigned to `eligible`?

- A. `True`
- B. `0`
- C. Raises `SyntaxError`
- D. `False`

### 18. A packing loop sets `stock = 17; boxes = 0` and runs `while stock >= 5: stock -= 5; boxes += 1`. What is `boxes` after the loop ends?

- A. `5`
- B. `4`
- C. `2`
- D. `3`

### 19. A restock loop sets `need = 0` and runs `while need > 0: print(need); need -= 1`. What is printed?

- A. Raises `ValueError`
- B. `1`
- C. `0 1 2`
- D. Nothing is printed (zero iterations)

### 20. In a batch-numbering helper, which two `range()` calls generate sequences of length `3`? Select two.

- A. `range(1, 3)`
- B. `range(2, 9, 2)`
- C. `range(3, 0, -1)`
- D. `range(1, 6, 2)`
- E. `range(5, 1)`

### 21. An aisle-numbering check runs `print(sum(range(2, 9, 2)))`. What integer does it print?

- A. `18`
- B. `12`
- C. `29`
- D. `20`

### 22. A cart script runs `subtotal = 0` / `for price in (12, 8, 5): subtotal += price` / `print(subtotal)`. What is printed?

- A. Raises `TypeError`
- B. `3`
- C. `20`
- D. `25`

### 23. A register tally sets `paid = 0` and runs `for coin in [5, 10, 0, 25]:` / `    if coin == 0: break` / `    paid += coin`. What is `paid` afterward?

- A. `0`
- B. `40`
- C. `15`
- D. `5`

### 24. Complete `for price in cart:` / `    if price <= 0: ____` / `    total += price` so zero or negative adjustments are skipped while positive prices later in `cart` are still added. Which keyword fills the blank?

- A. `return`
- B. `del`
- C. `break`
- D. `continue`

### 25. A backorder loop sets `items_left = 0` and runs `while items_left > 0:` / `    items_left -= 1` / `else: print('DONE')`. What is printed?

- A. `FOUND`
- B. Raises `SyntaxError`
- C. `DONE`
- D. Nothing is printed (zero iterations)

### 26. When scanning SKUs with a `for ... else` loop, which two events prevent the loop's `else:` suite from running? Select two.

- A. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- B. When `break` terminates the loop early before the condition turns `False`
- C. When a `while` condition initially or eventually evaluates to `False` without `break`
- D. When a `for` loop consumes every item in its iterable without hitting `break`
- E. When an unhandled exception aborts the loop body

### 27. A tier matcher runs `combos = 0` / `for tier in [1, 2, 3]:` / `    for coupon in [1, 2, 3]:` / `        if tier == coupon: combos += 1`. What is `combos` afterward?

- A. `6`
- B. `9`
- C. `3`
- D. `1`

### 28. Complete `for shelf in warehouse:` / `    ____ bin_qty in shelf:` / `        grand_total += bin_qty` so the inner loop sums every bin inside each shelf list. Which keyword fills the blank?

- A. `for`
- B. `in`
- C. `elif`
- D. `while`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations

### 29. A catalog page requests `skus[10:20]` when `skus = [101, 102, 103, 104]` has only four items. What does Python return?

- A. `[104, 103, 102, 101]`
- B. `None`
- C. Raises `IndexError`
- D. `[]`

### 30. Given `skus = [101, 102, 103, 104]`, what does the slice `skus[::-1]` evaluate to?

- A. `[104, 103, 102, 101]`
- B. `[1, 2, 3]`
- C. Raises `IndexError`
- D. `[]`

### 31. Complete `cart = [1, 2]; cart.____([3, 4])` so each element of `[3, 4]` is appended individually and `cart` becomes `[1, 2, 3, 4]`. Which `list` method fills the blank?

- A. `append()`
- B. `extend()`
- C. `insert()`
- D. `remove()`

### 32. Complete `last_sku = stack.____()` so the final element of non-empty list `stack` is removed in place and returned into `last_sku`. Which `list` method fills the blank?

- A. `sort()`
- B. `remove()`
- C. `pop()`
- D. `index()`

### 33. Complete `if ____(cart_items) == 0:` so the expression returns the integer item count of `cart_items`. Which built-in function fills the blank?

- A. `sorted()`
- B. `index()`
- C. `len()`
- D. `int()`

### 34. A cart snapshot holds `a = [10, 20, 30]`. Which two assignments create a new shallow copy `b` so mutating `b[0] = 0` keeps `a` unchanged? Select two.

- A. `b = list(a)`
- B. `[1, 99, 3]`
- C. `b = a.sort()`
- D. `b = a.copy()`
- E. `b = a`

### 35. A cart doubler evaluates `[p * 2 for p in [1, 2, 3]]`. Which list is produced?

- A. Raises `SyntaxError`
- B. `[2, 4, 6]`
- C. `[1, 2, 3]`
- D. `6`

### 36. Complete `aisles = [10, 20, 30]` / `if 20 ____ aisles:` so the condition returns `True` when `20` appears as an element of `aisles`. Which operator fills the blank?

- A. `in`
- B. `==`
- C. `not in`
- D. `is`

### 37. Which two expressions construct a one-element `tuple` in Python 3? Select two.

- A. `(7)`
- B. `t = tuple(5)`
- C. `(7,)`
- D. `t = tuple()`
- E. `t = 5,`

### 38. A bundle combiner evaluates `(1, 2) + (3, 4)`. What value is produced?

- A. `[1, 2, 3, 4]`
- B. `(1, 2, 3, 4)`
- C. `(1, 2, 3)`
- D. Raises `TypeError`

### 39. A stock map sets `inv = {'pen': 12, 'pad': 5}`, runs `removed = inv.pop('pad')`, and prints `removed`. What is printed?

- A. `5`
- B. Raises `KeyError`
- C. `None`
- D. `1`

### 40. Complete `total_units = sum(stock_by_sku.____())` so `sum()` adds every quantity mapped in dictionary `stock_by_sku` without reading the SKU string keys. Which `dict` method fills the blank?

- A. `values()`
- B. `get()`
- C. `keys()`
- D. `items()`

### 41. A receipt label needs to represent the text `Item's price` containing an apostrophe. Which two Python string literals are syntactically valid? Select two.

- A. `'C:\temp\'`
- B. `"Item's price"`
- C. `'Item's price'`
- D. `'Item\'s price'`
- E. `"Item price'`

### 42. Which two statements about strings in Python 3 are accurate? Select two.

- A. Every string transformation method returns a brand-new `str` object and leaves the original string unchanged
- B. Running `del s[0]` deletes the first character from `s` in place
- C. An escape sequence such as `\n` or `\\` counts as a single character in `len()`
- D. Calling `t.append(9)` adds an element to the end of tuple `t` in place
- E. Assigning `s[0] = "X"` mutates the first character of `s` in place

### 43. Complete `parts = ['SKU', '42', 'XL']; code = ____` so `code` is bound to the hyphen-separated string `'SKU-42-XL'`. Which expression fills the blank?

- A. `extend()`
- B. `append()`
- C. `'-'.join(parts)`
- D. `line.split()`

---

## Block 4 — Functions and Exceptions (28%) — User-defined functions, generators, recursion, argument passing, scope/global, and exception handling

### 44. A receipt logger defines `def show_banner(msg): print(msg)` with no `return` line, and runs `out = show_banner('HI'); print(out)`. What does the second `print(out)` display?

- A. `False`
- B. `None`
- C. `0`
- D. Raises `TypeError`

### 45. Complete `____ apply_tax(subtotal, rate):` / `    return subtotal * (1 + rate)` so `apply_tax` is defined as a reusable function. Which keyword fills the blank?

- A. `return`
- B. `lambda`
- C. `def`
- D. `class`

### 46. A helper defines `def sq(n):` / `    for k in range(1, n + 1): yield k * k` and runs `print(list(sq(3)))`. What is printed?

- A. Raises `TypeError`
- B. `[1, 4, 9]`
- C. `[0, 1, 2]`
- D. `<class 'generator'>`

### 47. A recursive helper defines `def power(base, exp): return 1 if exp == 0 else base * power(base, exp - 1)` and evaluates `power(3, 4)`. What integer does it return?

- A. `81`
- B. `27`
- C. `12`
- D. Raises `RecursionError`

### 48. Complete the base case `def power(base, exp):` / `    if exp == 0: return ____` / `    return base * power(base, exp - 1)` so `power(5, 0)` equals `1` and `power(5, 2)` equals `25`. Which literal fills the blank?

- A. `0`
- B. `3`
- C. `1`
- D. `None`

### 49. A cart module defines `def calc(base, rate): return base + base * rate`. Which two calls execute without raising `SyntaxError` or `TypeError`? Select two.

- A. `calc(10, rate=2)`
- B. `calc(base=10, 2)`
- C. `calc(rate=2, base=10)`
- D. `calc(10, base=5)`
- E. `calc(10, tax=2)`

### 50. Given `def net_price(gross, discount): return gross - discount`, what does `net_price(discount=3, gross=10)` return?

- A. `7`
- B. `13`
- C. Raises `TypeError`
- D. Raises `SyntaxError`

### 51. Given `def pack_cost(units, box_fee=4, per_unit=2): return box_fee + units * per_unit`, what does `pack_cost(5, per_unit=4)` return?

- A. Raises `TypeError`
- B. `24`
- C. `12`
- D. `36`

### 52. Complete the idiomatic safe-default pattern `def add_sku(sku, bucket=____):` / `    if bucket is None: bucket = []` / `    bucket.append(sku); return bucket` so separate calls do not share one mutated list. Which singleton literal fills the blank?

- A. `0`
- B. `None`
- C. `[]`
- D. `False`

### 53. A cart script defines a module-level list `rates = [10, 20]`. Which two statements accurately describe accessing `rates` from inside a function without `global`? Select two.

- A. Reading a module-level variable inside a function works directly as long as the function never assigns to that same name
- B. Mutating an element via `rates[0] = 99` inside a function modifies the global list in place without needing `global rates`
- C. Rebinding `rates = []` inside a function without `global rates` clears the module-level `rates` variable for all callers
- D. `[1] [2]`
- E. Function parameter names are automatically registered in module-level global scope when the function returns

### 54. A script sets `rates = [10, 20]`, defines `def tweak(): rates[0] = 99`, calls `tweak()`, and prints `rates[0]`. What is printed?

- A. Raises `NameError`
- B. `10`
- C. `99`
- D. Raises `UnboundLocalError`

### 55. Which two statements accurately describe abstract parent classes inside Python's built-in exception hierarchy? Select two.

- A. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`
- B. Calling `t.append(9)` adds an element to the end of tuple `t` in place
- C. `True`, because Python stores decimal fractions exactly to two decimal places
- D. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- E. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler

### 56. Why does a standard `except Exception:` block in an inventory daemon allow `KeyboardInterrupt` (Ctrl-C) to stop the process instead of catching it?

- A. `ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)
- B. `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`
- C. `LookupError` is the abstract parent class of both `IndexError` and `KeyError`
- D. `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`

### 57. A bin lookup sets `bins = ['A1', 'A2']` and evaluates single-element subscript `bins[5]`. Which exception does Python raise?

- A. Raises `KeyError`
- B. Raises `IndexError`
- C. `None`
- D. Raises `ValueError`

### 58. A receipt line evaluates `'Total: ' + 15` without converting `15` to a string first. What happens at runtime?

- A. `15`
- B. Raises `ValueError`
- C. Raises `TypeError`
- D. `123`

### 59. Which two rules hold true for `try ... except ... else` blocks in Python 3? Select two.

- A. Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`
- B. Place a bare `except:` clause above `except TypeError:` as a fallback default
- C. Python runs every `except` clause whose class matches the raised exception from top to bottom
- D. The `else` branch of `try` runs only when the `try` suite finishes with no exception raised
- E. Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler

### 60. Complete `____:` / `    qty = int(user_text)` / `except ValueError:` / `    qty = 1` so Python monitors the conversion for exceptions and jumps to `except ValueError:` on bad input. Which keyword fills the blank?

- A. `try`
- B. `while`
- C. `except`
- D. `finally`

---

## Answer key and explanations

### Question 1 — D

Answer: The plain-text file holding Python instructions written by the programmer. The `.py` source file is plain human-readable text storing Python statements that CPython reads and compiles to bytecode at runtime. A source file stores human-readable Python statements before translation begins. Local study-map skill 1.1 (Compilation vs Interpretation and Execution Model), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Standard Python scripts still require a Python runtime rather than a static hardware linker. Why the correct answer wins: The `.py` source file is plain human-readable text storing Python statements that CPython reads and compiles to bytecode at runtime.
- **B:** Incorrect for this question. Ahead-of-time native machine-code compilation is what a C or Rust compiler performs, not standard CPython. Why the correct answer wins: The `.py` source file is plain human-readable text storing Python statements that CPython reads and compiles to bytecode at runtime.
- **C:** Incorrect for this question. `.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source. Why the correct answer wins: The `.py` source file is plain human-readable text storing Python statements that CPython reads and compiles to bytecode at runtime.
- **D:** Correct. A source file stores human-readable Python statements before translation begins. In this case: The `.py` source file is plain human-readable text storing Python statements that CPython reads and compiles to bytecode at runtime.

### Question 2 — B, E

Answers: Lexis checks that each individual token is legal, whereas syntax checks how tokens are arranged into statements; Semantics determines runtime meaning, so `10 / 0` passes lexis and syntax yet fails at runtime. Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution. Lexical analysis validates vocabulary tokens; syntactic analysis validates statement grammar. A statement can be lexically and syntactically valid while still failing semantically during execution. Local study-map skill 1.2 (Lexis, Syntax, and Semantics Distinctions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Tokenization happens before bytecode compilation and execution. Why the correct answer wins: Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution.
- **B:** Correct. Lexical analysis validates vocabulary tokens; syntactic analysis validates statement grammar. In this case: Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution.
- **C:** Incorrect for this question. Standard Python `float` uses binary IEEE-754 rather than exact base-10 representation. Why the correct answer wins: Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution.
- **D:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution.
- **E:** Correct. A statement can be lexically and syntactically valid while still failing semantically during execution. In this case: Lexis checks individual tokens, syntax checks statement grammar, and semantics governs runtime meaning so `10 / 0` passes parsing yet fails at execution.

### Question 3 — C, D

Answers: `import`; `class`. `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier. `import` is a reserved keyword and therefore cannot be used as an ordinary variable name. `class` is a reserved keyword and cannot be used as a variable identifier. Local study-map skill 1.3 (Keywords, Instructions, Indentation, and Comments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Keywords are case-sensitive: `True` is reserved, whereas lowercase `true` is an ordinary identifier. Why the correct answer wins: `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier.
- **B:** Incorrect for this question. `print` is a built-in function name rather than a hard keyword, though shadowing it is poor practice. Why the correct answer wins: `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier.
- **C:** Correct. `import` is a reserved keyword and therefore cannot be used as an ordinary variable name. In this case: `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier.
- **D:** Correct. `class` is a reserved keyword and cannot be used as a variable identifier. In this case: `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier.
- **E:** Incorrect for this question. A leading underscore is a legal identifier start in Python and signals an internal helper by convention. Why the correct answer wins: `import` and `class` are reserved keywords in Python 3, whereas `print` is a built-in function name, `true` is lowercase, and `_temp_value` is a legal identifier.

### Question 4 — B, D

Answers: `1_000_000`; `4e3`. `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`. Single underscores between digits are legal visual separators in Python numeric literals. Scientific-notation literals like `4e3` are always of type `float` (`4000.0`). Local study-map skill 1.4 (Literals, Numeral Systems, and Scientific Notation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Leading zeros on non-zero decimal integers are illegal in Python 3 and raise `SyntaxError`. Why the correct answer wins: `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`.
- **B:** Correct. Scientific-notation literals like `4e3` are always of type `float` (`4000.0`). In this case: `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`.
- **C:** Incorrect for this question. Digit `8` is out of range for base-8 octal literals (`0` through `7`), causing `SyntaxError`. Why the correct answer wins: `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`.
- **D:** Correct. Single underscores between digits are legal visual separators in Python numeric literals. In this case: `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`.
- **E:** Incorrect for this question. `G` is outside hexadecimal digits `0-9` and `A-F`, so `0x1G` raises `SyntaxError`. Why the correct answer wins: `1_000_000` uses legal digit-grouping underscores (`int`) and `4e3` uses scientific notation (`float` `4000.0`), whereas `0o18`, `017`, and `0x1G` all raise `SyntaxError`.

### Question 5 — D

Answer: Every statement in the same suite must share the exact same indentation width. Every statement within the same suite must use the exact same indentation width (four spaces per level by PEP-8 convention). Python groups blocks by indentation level, and PEP-8 recommends four spaces per level. Local study-map skill 1.5 (Variable Naming Rules and PEP-8 Conventions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Comments are ignored by the parser and never disable syntax checking on surrounding code. Why the correct answer wins: Every statement within the same suite must use the exact same indentation width (four spaces per level by PEP-8 convention).
- **B:** Incorrect for this question. `.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source. Why the correct answer wins: Every statement within the same suite must use the exact same indentation width (four spaces per level by PEP-8 convention).
- **C:** Incorrect for this question. A compiled standalone executable runs directly on the target OS without shipping the compiler. Why the correct answer wins: Every statement within the same suite must use the exact same indentation width (four spaces per level by PEP-8 convention).
- **D:** Correct. Python groups blocks by indentation level, and PEP-8 recommends four spaces per level. In this case: Every statement within the same suite must use the exact same indentation width (four spaces per level by PEP-8 convention).

### Question 6 — D

Answer: `5.0`. True division `/` in Python 3 always produces a `float`, even when `10` divides evenly by `2`, printing `5.0`. Evaluates to the floating-point value `5.0`. Local study-map skill 1.6 (Arithmetic Operators, Floor Division, Modulo, and Exponentiation), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: True division `/` in Python 3 always produces a `float`, even when `10` divides evenly by `2`, printing `5.0`.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: True division `/` in Python 3 always produces a `float`, even when `10` divides evenly by `2`, printing `5.0`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: True division `/` in Python 3 always produces a `float`, even when `10` divides evenly by `2`, printing `5.0`.
- **D:** Correct. Evaluates to the floating-point value `5.0`. In this case: True division `/` in Python 3 always produces a `float`, even when `10` divides evenly by `2`, printing `5.0`.

### Question 7 — A

Answer: `50`. Exponentiation runs first (`4 ** 2 == 16`), multiplication second (`3 * 16 == 48`), and addition last (`2 + 48 == 50`). Evaluates to the integer `50`. Local study-map skill 1.7 (Operator Precedence, Unary Signs, and Right-Sided Binding), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Evaluates to the integer `50`. In this case: Exponentiation runs first (`4 ** 2 == 16`), multiplication second (`3 * 16 == 48`), and addition last (`2 + 48 == 50`).
- **B:** Incorrect for this question. Evaluates to the integer `22`. Why the correct answer wins: Exponentiation runs first (`4 ** 2 == 16`), multiplication second (`3 * 16 == 48`), and addition last (`2 + 48 == 50`).
- **C:** Incorrect for this question. Evaluates to the integer `100`. Why the correct answer wins: Exponentiation runs first (`4 ** 2 == 16`), multiplication second (`3 * 16 == 48`), and addition last (`2 + 48 == 50`).
- **D:** Incorrect for this question. Evaluates to the integer `32`. Why the correct answer wins: Exponentiation runs first (`4 ** 2 == 16`), multiplication second (`3 * 16 == 48`), and addition last (`2 + 48 == 50`).

### Question 8 — B

Answer: `<<`. Left shift `<<` shifts bits toward higher powers of two (`5 * (2 ** 2) == 20`), whereas `>>` shifts right (`5 >> 2 == 1`). Left bit-shift multiplies a non-negative integer by `2 ** n`. Local study-map skill 1.8 (Bitwise, Relational, Boolean Operators, and Short-Circuiting), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Right bit-shift floor-divides an integer by `2 ** n`. Why the correct answer wins: Left shift `<<` shifts bits toward higher powers of two (`5 * (2 ** 2) == 20`), whereas `>>` shifts right (`5 >> 2 == 1`).
- **B:** Correct. Left bit-shift multiplies a non-negative integer by `2 ** n`. In this case: Left shift `<<` shifts bits toward higher powers of two (`5 * (2 ** 2) == 20`), whereas `>>` shifts right (`5 >> 2 == 1`).
- **C:** Incorrect for this question. Modulo returns the remainder `a - (a // b) * b`, taking the sign of the divisor `b` in Python. Why the correct answer wins: Left shift `<<` shifts bits toward higher powers of two (`5 * (2 ** 2) == 20`), whereas `>>` shifts right (`5 >> 2 == 1`).
- **D:** Incorrect for this question. Bitwise AND sets each bit to `1` only where both integer operands have `1`. Why the correct answer wins: Left shift `<<` shifts bits toward higher powers of two (`5 * (2 ** 2) == 20`), whereas `>>` shifts right (`5 >> 2 == 1`).

### Question 9 — A

Answer: `*=`. `*=` performs augmented repetition on sequences and strings, rebinding `divider` to `'----'`. Augmented multiplication scales a number or repeats a sequence/string. Local study-map skill 1.9 (Floating-Point Accuracy, String Operators, and Shortcut Assignments), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Augmented multiplication scales a number or repeats a sequence/string. In this case: `*=` performs augmented repetition on sequences and strings, rebinding `divider` to `'----'`.
- **B:** Incorrect for this question. Augmented floor division replaces the variable with its floored quotient. Why the correct answer wins: `*=` performs augmented repetition on sequences and strings, rebinding `divider` to `'----'`.
- **C:** Incorrect for this question. Exponentiation has higher precedence than unary minus on its left and binds right-to-left (`2 ** 3 ** 2 == 512`). Why the correct answer wins: `*=` performs augmented repetition on sequences and strings, rebinding `divider` to `'----'`.
- **D:** Incorrect for this question. Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings). Why the correct answer wins: `*=` performs augmented repetition on sequences and strings, rebinding `divider` to `'----'`.

### Question 10 — B

Answer: `red;green;blue`. Setting `sep=';'` joins the three positional arguments with semicolons instead of spaces, outputting `red;green;blue`. Passing `sep=";"` joins the three arguments with semicolons. Local study-map skill 1.10 (Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Default `sep` in `print()` is a single space and default `end` is `\n`. Why the correct answer wins: Setting `sep=';'` joins the three positional arguments with semicolons instead of spaces, outputting `red;green;blue`.
- **B:** Correct. Passing `sep=";"` joins the three arguments with semicolons. In this case: Setting `sep=';'` joins the three positional arguments with semicolons instead of spaces, outputting `red;green;blue`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Setting `sep=';'` joins the three positional arguments with semicolons instead of spaces, outputting `red;green;blue`.
- **D:** Incorrect for this question. Joining three arguments with `-` and ending with `!` prints `a-b-c!`. Why the correct answer wins: Setting `sep=';'` joins the three positional arguments with semicolons instead of spaces, outputting `red;green;blue`.

### Question 11 — B

Answer: `-3`. `int()` on a floating-point number truncates the fractional part *toward zero* (unlike `//` which floors toward negative infinity), producing `-3`. Evaluates to the negative integer `-3`. Local study-map skill 1.11 (Console Input with input() and Type Casting (int, float, str, bool)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: `int()` on a floating-point number truncates the fractional part *toward zero* (unlike `//` which floors toward negative infinity), producing `-3`.
- **B:** Correct. Evaluates to the negative integer `-3`. In this case: `int()` on a floating-point number truncates the fractional part *toward zero* (unlike `//` which floors toward negative infinity), producing `-3`.
- **C:** Incorrect for this question. Evaluates to the floating-point value `-3.0` because floor division rounds toward negative infinity. Why the correct answer wins: `int()` on a floating-point number truncates the fractional part *toward zero* (unlike `//` which floors toward negative infinity), producing `-3`.
- **D:** Incorrect for this question. Evaluates to the negative integer `-4`. Why the correct answer wins: `int()` on a floating-point number truncates the fractional part *toward zero* (unlike `//` which floors toward negative infinity), producing `-3`.

### Question 12 — A

Answer: `A B`. Because the second statement is an independent `if` rather than `elif`, both conditions are tested and both match `12`, producing `'A B'`. Prints `A B` when two independent `if` statements (rather than `if`/`elif`) both evaluate to `True`. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Prints `A B` when two independent `if` statements (rather than `if`/`elif`) both evaluate to `True`. In this case: Because the second statement is an independent `if` rather than `elif`, both conditions are tested and both match `12`, producing `'A B'`.
- **B:** Incorrect for this question. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both conditions are tested and both match `12`, producing `'A B'`.
- **C:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both conditions are tested and both match `12`, producing `'A B'`.
- **D:** Incorrect for this question. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both conditions are tested and both match `12`, producing `'A B'`.

### Question 13 — C

Answer: `>=`. `>=` includes the boundary value `50` as well as larger totals, whereas `>` would exclude `50`. Greater-than-or-equal relational operator. Local study-map skill 2.1 (Single and Chained Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Less-than-or-equal relational operator. Why the correct answer wins: `>=` includes the boundary value `50` as well as larger totals, whereas `>` would exclude `50`.
- **B:** Incorrect for this question. Strictly-greater-than relational operator. Why the correct answer wins: `>=` includes the boundary value `50` as well as larger totals, whereas `>` would exclude `50`.
- **C:** Correct. Greater-than-or-equal relational operator. In this case: `>=` includes the boundary value `50` as well as larger totals, whereas `>` would exclude `50`.
- **D:** Incorrect for this question. A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`. Why the correct answer wins: `>=` includes the boundary value `50` as well as larger totals, whereas `>` would exclude `50`.

### Question 14 — B, E

Answers: `()`; `{}`. Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values. Evaluates to an empty `tuple` of length `0`. An empty `{}` literal creates an empty `dict` (not a `set`). Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Any non-empty string, including `'False'`, is truthy in Python; only `''` is a falsy string. Why the correct answer wins: Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values.
- **B:** Correct. Evaluates to an empty `tuple` of length `0`. In this case: Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values.
- **C:** Incorrect for this question. A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy. Why the correct answer wins: Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values.
- **D:** Incorrect for this question. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. Why the correct answer wins: Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values.
- **E:** Correct. An empty `{}` literal creates an empty `dict` (not a `set`). In this case: Empty `()` and empty `{}` are falsy so `not coupons` is `True`, whereas `'False'`, `[0]`, and `(7,)` are non-empty truthy values.

### Question 15 — D

Answer: `A`. List `[0]` contains one element (`len([0]) == 1`), so `bins` is truthy even though element `0` itself is falsy, printing `A`. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. Local study-map skill 2.2 (Nested Conditionals and Truthiness of Built-In Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`. Why the correct answer wins: List `[0]` contains one element (`len([0]) == 1`), so `bins` is truthy even though element `0` itself is falsy, printing `A`.
- **B:** Incorrect for this question. Prints `D` via the final `else` fallback when every preceding condition is `False`. Why the correct answer wins: List `[0]` contains one element (`len([0]) == 1`), so `bins` is truthy even though element `0` itself is falsy, printing `A`.
- **C:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: List `[0]` contains one element (`len([0]) == 1`), so `bins` is truthy even though element `0` itself is falsy, printing `A`.
- **D:** Correct. Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses. In this case: List `[0]` contains one element (`len([0]) == 1`), so `bins` is truthy even though element `0` itself is falsy, printing `A`.

### Question 16 — D, E

Answers: `10 <= x <= 20`; `(x >= 10) and (x <= 20)`. `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. Combining two relational checks with `and` requires both bounds to hold. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Single `=` is assignment rather than comparison and raises `SyntaxError` inside a Boolean expression. Why the correct answer wins: `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error.
- **B:** Incorrect for this question. Using `or` here is `True` for *every* number (for example `x = 99` satisfies `x >= 10`). Why the correct answer wins: `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error.
- **C:** Incorrect for this question. Bitwise `&` binds tighter than `<=`, so `10 <= x & x <= 20` parses as `10 <= (x & x) <= 20` rather than logical `and`. Why the correct answer wins: `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error.
- **D:** Correct. Combining two relational checks with `and` requires both bounds to hold. In this case: `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error.
- **E:** Correct. Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once. In this case: `10 <= x <= 20` and `(x >= 10) and (x <= 20)` enforce both lower and upper bounds; `or` matches every number, `&` is bitwise AND with higher precedence, and `=` is a syntax error.

### Question 17 — A

Answer: `True`. Logical `and` has higher precedence than `or`, so Python evaluates `True or (False and False)` -> `True or False` -> `True`. Evaluates to Boolean `True`. Local study-map skill 2.3 (Compound Boolean Conditions and Chained Comparisons), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to Boolean `True`. In this case: Logical `and` has higher precedence than `or`, so Python evaluates `True or (False and False)` -> `True or False` -> `True`.
- **B:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Logical `and` has higher precedence than `or`, so Python evaluates `True or (False and False)` -> `True or False` -> `True`.
- **C:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Logical `and` has higher precedence than `or`, so Python evaluates `True or (False and False)` -> `True or False` -> `True`.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Logical `and` has higher precedence than `or`, so Python evaluates `True or (False and False)` -> `True or False` -> `True`.

### Question 18 — D

Answer: `3`. Three full packs of `5` reduce `stock` through `12 -> 7 -> 2`, incrementing `boxes` to `3` before `2 >= 5` becomes `False`. Evaluates to the integer `3`. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Three full packs of `5` reduce `stock` through `12 -> 7 -> 2`, incrementing `boxes` to `3` before `2 >= 5` becomes `False`.
- **B:** Incorrect for this question. Evaluates to the integer `4`. Why the correct answer wins: Three full packs of `5` reduce `stock` through `12 -> 7 -> 2`, incrementing `boxes` to `3` before `2 >= 5` becomes `False`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Three full packs of `5` reduce `stock` through `12 -> 7 -> 2`, incrementing `boxes` to `3` before `2 >= 5` becomes `False`.
- **D:** Correct. Evaluates to the integer `3`. In this case: Three full packs of `5` reduce `stock` through `12 -> 7 -> 2`, incrementing `boxes` to `3` before `2 >= 5` becomes `False`.

### Question 19 — D

Answer: Nothing is printed (zero iterations). Because `need > 0` is already `False` on the initial check and there is no `else` clause, the loop body executes zero times and nothing is printed. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Local study-map skill 2.4 (Counting and Accumulator Loops with while), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Because `need > 0` is already `False` on the initial check and there is no `else` clause, the loop body executes zero times and nothing is printed.
- **B:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Because `need > 0` is already `False` on the initial check and there is no `else` clause, the loop body executes zero times and nothing is printed.
- **C:** Incorrect for this question. Prints `0 1 2` across iterations. Why the correct answer wins: Because `need > 0` is already `False` on the initial check and there is no `else` clause, the loop body executes zero times and nothing is printed.
- **D:** Correct. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. In this case: Because `need > 0` is already `False` on the initial check and there is no `else` clause, the loop body executes zero times and nothing is printed.

### Question 20 — C, D

Answers: `range(1, 6, 2)`; `range(3, 0, -1)`. `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). `range(3, 0, -1)` counts down `3, 2, 1` (three iterations). Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three). Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **B:** Incorrect for this question. `range(2, 9, 2)` yields `2, 4, 6, 8`, stopping before `9`. Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **C:** Correct. `range(3, 0, -1)` counts down `3, 2, 1` (three iterations). In this case: `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **D:** Correct. `range(1, 6, 2)` produces `1, 3, 5` (three iterations). In this case: `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.
- **E:** Incorrect for this question. With default step `+1` and `start >= stop`, `range(5, 1)` produces zero iterations. Why the correct answer wins: `range(1, 6, 2)` yields `1, 3, 5` and `range(3, 0, -1)` yields `3, 2, 1` (three integers each); `range(1, 3)` yields two, `range(5, 1)` yields zero, and `range(2, 9, 2)` yields four.

### Question 21 — D

Answer: `20`. `range(2, 9, 2)` starts at `2` and steps by `2` up to exclusive `9`, generating `2, 4, 6, 8` whose sum is `20`. Evaluates to the integer `20`. Local study-map skill 2.5 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `18`. Why the correct answer wins: `range(2, 9, 2)` starts at `2` and steps by `2` up to exclusive `9`, generating `2, 4, 6, 8` whose sum is `20`.
- **B:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `range(2, 9, 2)` starts at `2` and steps by `2` up to exclusive `9`, generating `2, 4, 6, 8` whose sum is `20`.
- **C:** Incorrect for this question. Evaluates to the integer `29`. Why the correct answer wins: `range(2, 9, 2)` starts at `2` and steps by `2` up to exclusive `9`, generating `2, 4, 6, 8` whose sum is `20`.
- **D:** Correct. Evaluates to the integer `20`. In this case: `range(2, 9, 2)` starts at `2` and steps by `2` up to exclusive `9`, generating `2, 4, 6, 8` whose sum is `20`.

### Question 22 — D

Answer: `25`. A `for` loop iterates over tuple elements in order (`12`, `8`, `5`), accumulating `subtotal` to `25`. Evaluates to the integer `25`. Local study-map skill 2.6 (Iterating Directly Over Sequences and Enumerated Values), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: A `for` loop iterates over tuple elements in order (`12`, `8`, `5`), accumulating `subtotal` to `25`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: A `for` loop iterates over tuple elements in order (`12`, `8`, `5`), accumulating `subtotal` to `25`.
- **C:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: A `for` loop iterates over tuple elements in order (`12`, `8`, `5`), accumulating `subtotal` to `25`.
- **D:** Correct. Evaluates to the integer `25`. In this case: A `for` loop iterates over tuple elements in order (`12`, `8`, `5`), accumulating `subtotal` to `25`.

### Question 23 — C

Answer: `15`. The loop adds `5` and `10` (`15`), then hits `break` on `0` and exits before `25` is ever processed. Evaluates to the integer `15`. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: The loop adds `5` and `10` (`15`), then hits `break` on `0` and exits before `25` is ever processed.
- **B:** Incorrect for this question. Evaluates to the integer `40`. Why the correct answer wins: The loop adds `5` and `10` (`15`), then hits `break` on `0` and exits before `25` is ever processed.
- **C:** Correct. Evaluates to the integer `15`. In this case: The loop adds `5` and `10` (`15`), then hits `break` on `0` and exits before `25` is ever processed.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: The loop adds `5` and `10` (`15`), then hits `break` on `0` and exits before `25` is ever processed.

### Question 24 — D

Answer: `continue`. `continue` skips the rest of the current iteration and proceeds with the next item in `cart`. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. Local study-map skill 2.7 (Controlling Loops with break, continue, and pass), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `continue` skips the rest of the current iteration and proceeds with the next item in `cart`.
- **B:** Incorrect for this question. `del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key. Why the correct answer wins: `continue` skips the rest of the current iteration and proceeds with the next item in `cart`.
- **C:** Incorrect for this question. `break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch. Why the correct answer wins: `continue` skips the rest of the current iteration and proceeds with the next item in `cart`.
- **D:** Correct. `continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop. In this case: `continue` skips the rest of the current iteration and proceeds with the next item in `cart`.

### Question 25 — C

Answer: `DONE`. Even though `items_left > 0` is `False` immediately (zero body runs), `break` was never executed, so the `while ... else` suite runs and prints `DONE`. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early. Why the correct answer wins: Even though `items_left > 0` is `False` immediately (zero body runs), `break` was never executed, so the `while ... else` suite runs and prints `DONE`.
- **B:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Even though `items_left > 0` is `False` immediately (zero body runs), `break` was never executed, so the `while ... else` suite runs and prints `DONE`.
- **C:** Correct. Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite. In this case: Even though `items_left > 0` is `False` immediately (zero body runs), `break` was never executed, so the `while ... else` suite runs and prints `DONE`.
- **D:** Incorrect for this question. When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs. Why the correct answer wins: Even though `items_left > 0` is `False` immediately (zero body runs), `break` was never executed, so the `while ... else` suite runs and prints `DONE`.

### Question 26 — B, E

Answers: When `break` terminates the loop early before the condition turns `False`; When an unhandled exception aborts the loop body. Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`. `break` bypasses the loop `else` suite completely. An unhandled exception unwinds the stack rather than running the loop `else` clause. Local study-map skill 2.8 (Post-Loop Execution with while-else and for-else Clauses), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Why the correct answer wins: Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`.
- **B:** Correct. `break` bypasses the loop `else` suite completely. In this case: Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`.
- **C:** Incorrect for this question. A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite. Why the correct answer wins: Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`.
- **D:** Incorrect for this question. Normal exhaustion of a `for` iterable runs the attached `else` suite. Why the correct answer wins: Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`.
- **E:** Correct. An unhandled exception unwinds the stack rather than running the loop `else` clause. In this case: Both terminating early with `break` and aborting with an unhandled exception skip the loop `else:` block, whereas normal exhaustion executes `else:`.

### Question 27 — C

Answer: `3`. Across the nine `(tier, coupon)` pairs, `tier == coupon` holds on `(1, 1)`, `(2, 2)`, and `(3, 3)`, giving `combos == 3`. Evaluates to the integer `3`. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: Across the nine `(tier, coupon)` pairs, `tier == coupon` holds on `(1, 1)`, `(2, 2)`, and `(3, 3)`, giving `combos == 3`.
- **B:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: Across the nine `(tier, coupon)` pairs, `tier == coupon` holds on `(1, 1)`, `(2, 2)`, and `(3, 3)`, giving `combos == 3`.
- **C:** Correct. Evaluates to the integer `3`. In this case: Across the nine `(tier, coupon)` pairs, `tier == coupon` holds on `(1, 1)`, `(2, 2)`, and `(3, 3)`, giving `combos == 3`.
- **D:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Across the nine `(tier, coupon)` pairs, `tier == coupon` holds on `(1, 1)`, `(2, 2)`, and `(3, 3)`, giving `combos == 3`.

### Question 28 — A

Answer: `for`. `for` opens the nested definite iteration over the elements of `shelf`. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. Local study-map skill 2.9 (Nested Loops Over 2D Grids and Pairwise Combinations), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `for` introduces definite iteration over any iterable sequence, dictionary, range, or generator. In this case: `for` opens the nested definite iteration over the elements of `shelf`.
- **B:** Incorrect for this question. `in` tests element or substring membership and also binds loop targets in `for` headers. Why the correct answer wins: `for` opens the nested definite iteration over the elements of `shelf`.
- **C:** Incorrect for this question. `elif` is a reserved Python keyword that introduces an additional conditional branch. Why the correct answer wins: `for` opens the nested definite iteration over the elements of `shelf`.
- **D:** Incorrect for this question. `while` repeats its indented suite as long as its header condition evaluates to truthy. Why the correct answer wins: `for` opens the nested definite iteration over the elements of `shelf`.

### Question 29 — D

Answer: `[]`. Out-of-range list slices never raise `IndexError`; Python clamps both bounds to `len(skus)` and returns an empty list `[]`. Evaluates to an empty `list` of length `0`. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Slicing `[::-1]` returns a reversed shallow copy of the four-element list. Why the correct answer wins: Out-of-range list slices never raise `IndexError`; Python clamps both bounds to `len(skus)` and returns an empty list `[]`.
- **B:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Out-of-range list slices never raise `IndexError`; Python clamps both bounds to `len(skus)` and returns an empty list `[]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: Out-of-range list slices never raise `IndexError`; Python clamps both bounds to `len(skus)` and returns an empty list `[]`.
- **D:** Correct. Evaluates to an empty `list` of length `0`. In this case: Out-of-range list slices never raise `IndexError`; Python clamps both bounds to `len(skus)` and returns an empty list `[]`.

### Question 30 — A

Answer: `[104, 103, 102, 101]`. A slice with omitted bounds and step `-1` walks from the end to the start, returning `[104, 103, 102, 101]`. Slicing `[::-1]` returns a reversed shallow copy of the four-element list. Local study-map skill 3.1 (List Indexing, Negative Indices, and Slicing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Slicing `[::-1]` returns a reversed shallow copy of the four-element list. In this case: A slice with omitted bounds and step `-1` walks from the end to the start, returning `[104, 103, 102, 101]`.
- **B:** Incorrect for this question. Produces the three-element list `[1, 2, 3]`. Why the correct answer wins: A slice with omitted bounds and step `-1` walks from the end to the start, returning `[104, 103, 102, 101]`.
- **C:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Why the correct answer wins: A slice with omitted bounds and step `-1` walks from the end to the start, returning `[104, 103, 102, 101]`.
- **D:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: A slice with omitted bounds and step `-1` walks from the end to the start, returning `[104, 103, 102, 101]`.

### Question 31 — B

Answer: `extend()`. `extend([3, 4])` unpacks the iterable and appends `3` and `4` separately, whereas `append([3, 4])` nests `[3, 4]` as one element. `list.extend(iterable)` appends each element from `iterable` individually and returns `None`. Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.append(x)` adds `x` as a single element at the end of the list in place and returns `None`. Why the correct answer wins: `extend([3, 4])` unpacks the iterable and appends `3` and `4` separately, whereas `append([3, 4])` nests `[3, 4]` as one element.
- **B:** Correct. `list.extend(iterable)` appends each element from `iterable` individually and returns `None`. In this case: `extend([3, 4])` unpacks the iterable and appends `3` and `4` separately, whereas `append([3, 4])` nests `[3, 4]` as one element.
- **C:** Incorrect for this question. `list.insert(i, x)` places `x` before index `i` in place and returns `None`. Why the correct answer wins: `extend([3, 4])` unpacks the iterable and appends `3` and `4` separately, whereas `append([3, 4])` nests `[3, 4]` as one element.
- **D:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: `extend([3, 4])` unpacks the iterable and appends `3` and `4` separately, whereas `append([3, 4])` nests `[3, 4]` as one element.

### Question 32 — C

Answer: `pop()`. `list.pop()` with no argument removes and returns the last element (`index -1`) in O(1) time. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). Local study-map skill 3.2 (List Mutation Methods (append, insert, remove, pop, sort, index)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list. Why the correct answer wins: `list.pop()` with no argument removes and returns the last element (`index -1`) in O(1) time.
- **B:** Incorrect for this question. `list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent. Why the correct answer wins: `list.pop()` with no argument removes and returns the last element (`index -1`) in O(1) time.
- **C:** Correct. `list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item). In this case: `list.pop()` with no argument removes and returns the last element (`index -1`) in O(1) time.
- **D:** Incorrect for this question. `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. Why the correct answer wins: `list.pop()` with no argument removes and returns the last element (`index -1`) in O(1) time.

### Question 33 — C

Answer: `len()`. `len(cart_items)` returns the number of elements currently stored in the list. `len(obj)` returns the item or character count of a sequence or collection. Local study-map skill 3.3 (Deleting Elements or Slices with del, len(), and sorted()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`. Why the correct answer wins: `len(cart_items)` returns the number of elements currently stored in the list.
- **B:** Incorrect for this question. `.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing. Why the correct answer wins: `len(cart_items)` returns the number of elements currently stored in the list.
- **C:** Correct. `len(obj)` returns the item or character count of a sequence or collection. In this case: `len(cart_items)` returns the number of elements currently stored in the list.
- **D:** Incorrect for this question. `int()` converts a base-10 integer string or truncates a `float` toward zero (`int(-3.9) == -3`). Why the correct answer wins: `len(cart_items)` returns the number of elements currently stored in the list.

### Question 34 — A, D

Answers: `b = a.copy()`; `b = list(a)`. `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`. `list.copy()` allocates a new shallow copy of `a`. Passing `a` to `list(a)` constructs a distinct outer list with the same element references. Local study-map skill 3.4 (List Aliasing vs Shallow Slicing/Copying and Nested Matrices), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Passing `a` to `list(a)` constructs a distinct outer list with the same element references. In this case: `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`.
- **B:** Incorrect for this question. Assigning `b = a` binds both names to the same list object, so mutating `b` mutates `a`. Why the correct answer wins: `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`.
- **C:** Incorrect for this question. `a.sort()` sorts `a` in place and assigns `None` to `b`. Why the correct answer wins: `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`.
- **D:** Correct. `list.copy()` allocates a new shallow copy of `a`. In this case: `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`.
- **E:** Incorrect for this question. Plain assignment `b = a` creates an alias to the exact same list object rather than copying. Why the correct answer wins: `b = a.copy()` and `b = list(a)` each allocate a distinct outer list, whereas `b = a` shares the same list object and `a.sort()` returns `None`.

### Question 35 — B

Answer: `[2, 4, 6]`. The list comprehension multiplies each item `1, 2, 3` by `2` in order, returning `[2, 4, 6]`. Selects or computes `[2, 4, 6]` via list comprehension. Local study-map skill 3.5 (List Comprehensions with Filtering and Expressions), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: The list comprehension multiplies each item `1, 2, 3` by `2` in order, returning `[2, 4, 6]`.
- **B:** Correct. Selects or computes `[2, 4, 6]` via list comprehension. In this case: The list comprehension multiplies each item `1, 2, 3` by `2` in order, returning `[2, 4, 6]`.
- **C:** Incorrect for this question. Produces the three-element list `[1, 2, 3]`. Why the correct answer wins: The list comprehension multiplies each item `1, 2, 3` by `2` in order, returning `[2, 4, 6]`.
- **D:** Incorrect for this question. Evaluates to the integer `6`. Why the correct answer wins: The list comprehension multiplies each item `1, 2, 3` by `2` in order, returning `[2, 4, 6]`.

### Question 36 — A

Answer: `in`. `in` tests element membership in lists, tuples, sets, and dictionary keys, returning `True` when `20` is present. `in` tests element or substring membership and also binds loop targets in `for` headers. Local study-map skill 3.6 (Membership Testing with in and not in Across Collections), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `in` tests element or substring membership and also binds loop targets in `for` headers. In this case: `in` tests element membership in lists, tuples, sets, and dictionary keys, returning `True` when `20` is present.
- **B:** Incorrect for this question. `==` tests value equality rather than assignment (`=`) or object identity (`is`). Why the correct answer wins: `in` tests element membership in lists, tuples, sets, and dictionary keys, returning `True` when `20` is present.
- **C:** Incorrect for this question. `not in` evaluates to `True` when the left operand is absent from the right-hand container. Why the correct answer wins: `in` tests element membership in lists, tuples, sets, and dictionary keys, returning `True` when `20` is present.
- **D:** Incorrect for this question. `is` compares object identity rather than value equality. Why the correct answer wins: `in` tests element membership in lists, tuples, sets, and dictionary keys, returning `True` when `20` is present.

### Question 37 — C, E

Answers: `t = 5,`; `(7,)`. Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty. A trailing comma without parentheses packs a single-element tuple `(5,)`. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. Local study-map skill 3.7 (Tuple Construction, Single-Element Syntax, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Parentheses without a comma group an arithmetic expression rather than building a tuple. Why the correct answer wins: Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **B:** Incorrect for this question. `tuple()` expects an iterable, so passing an integer `5` raises `TypeError`. Why the correct answer wins: Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **C:** Correct. A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses. In this case: Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **D:** Incorrect for this question. `tuple()` with no arguments returns the empty tuple `()`. Why the correct answer wins: Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.
- **E:** Correct. A trailing comma without parentheses packs a single-element tuple `(5,)`. In this case: Both `t = 5,` (unparenthesized trailing comma) and `(7,)` construct single-element tuples; `(7)` is an `int`, `tuple(5)` raises `TypeError`, and `tuple()` is empty.

### Question 38 — B

Answer: `(1, 2, 3, 4)`. Although tuples cannot be mutated in place, `+` concatenates two tuples into a brand-new tuple `(1, 2, 3, 4)`. Concatenating tuples with `+` builds a new tuple `(1, 2, 3, 4)`. Local study-map skill 3.8 (Mutable Lists Inside Tuples vs Tuples Inside Lists), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `extend([3, 4])` or `+=` iterates the argument and appends each item individually. Why the correct answer wins: Although tuples cannot be mutated in place, `+` concatenates two tuples into a brand-new tuple `(1, 2, 3, 4)`.
- **B:** Correct. Concatenating tuples with `+` builds a new tuple `(1, 2, 3, 4)`. In this case: Although tuples cannot be mutated in place, `+` concatenates two tuples into a brand-new tuple `(1, 2, 3, 4)`.
- **C:** Incorrect for this question. Evaluates to the three-element tuple `(1, 2, 3)`. Why the correct answer wins: Although tuples cannot be mutated in place, `+` concatenates two tuples into a brand-new tuple `(1, 2, 3, 4)`.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Although tuples cannot be mutated in place, `+` concatenates two tuples into a brand-new tuple `(1, 2, 3, 4)`.

### Question 39 — A

Answer: `5`. `dict.pop('pad')` removes key `'pad'` from `inv` and returns its associated value `5`. Evaluates to the integer `5`. Local study-map skill 3.9 (Dictionary Creation, Key Lookup, Insertion, Update, and Deletion), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Evaluates to the integer `5`. In this case: `dict.pop('pad')` removes key `'pad'` from `inv` and returns its associated value `5`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `dict.pop('pad')` removes key `'pad'` from `inv` and returns its associated value `5`.
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: `dict.pop('pad')` removes key `'pad'` from `inv` and returns its associated value `5`.
- **D:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: `dict.pop('pad')` removes key `'pad'` from `inv` and returns its associated value `5`.

### Question 40 — A

Answer: `values()`. `dict.values()` returns a view of all mapped quantities, whereas `sum(stock_by_sku)` or `.keys()` would try to sum the string keys and raise `TypeError`. `dict.values()` returns a dynamic view of the dictionary values. Local study-map skill 3.10 (Dictionary Iteration with keys(), values(), items(), and get()), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. `dict.values()` returns a dynamic view of the dictionary values. In this case: `dict.values()` returns a view of all mapped quantities, whereas `sum(stock_by_sku)` or `.keys()` would try to sum the string keys and raise `TypeError`.
- **B:** Incorrect for this question. `dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing. Why the correct answer wins: `dict.values()` returns a view of all mapped quantities, whereas `sum(stock_by_sku)` or `.keys()` would try to sum the string keys and raise `TypeError`.
- **C:** Incorrect for this question. `dict.keys()` returns a dynamic view of the dictionary keys. Why the correct answer wins: `dict.values()` returns a view of all mapped quantities, whereas `sum(stock_by_sku)` or `.keys()` would try to sum the string keys and raise `TypeError`.
- **D:** Incorrect for this question. `dict.items()` yields `(key, value)` 2-tuples suitable for two-variable `for k, v in d.items():` unpacking. Why the correct answer wins: `dict.values()` returns a view of all mapped quantities, whereas `sum(stock_by_sku)` or `.keys()` would try to sum the string keys and raise `TypeError`.

### Question 41 — B, D

Answers: `"Item's price"`; `'Item\'s price'`. Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`. Wrapping a string in double quotes lets an apostrophe appear inside without a backslash. Escaping the inner single quote with `\` keeps a single-quoted string literal valid. Local study-map skill 3.11 (String Literals, Escape Sequences, Quotes, and Multiline Strings), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. A trailing single backslash escapes the closing quote itself, causing `SyntaxError: unterminated string literal`. Why the correct answer wins: Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`.
- **B:** Correct. Wrapping a string in double quotes lets an apostrophe appear inside without a backslash. In this case: Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`.
- **C:** Incorrect for this question. An unescaped apostrophe inside single quotes terminates the literal early and raises `SyntaxError`. Why the correct answer wins: Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`.
- **D:** Correct. Escaping the inner single quote with `\` keeps a single-quoted string literal valid. In this case: Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`.
- **E:** Incorrect for this question. Opening with `"` and closing with an apostrophe leaves the string literal unterminated and raises `SyntaxError`. Why the correct answer wins: Double-quoted `"Item's price"` and backslash-escaped `'Item\'s price'` both parse cleanly, whereas unescaped `'Item's price'`, mismatched quotes, and a trailing single backslash raise `SyntaxError`.

### Question 42 — A, C

Answers: Every string transformation method returns a brand-new `str` object and leaves the original string unchanged; An escape sequence such as `\n` or `\\` counts as a single character in `len()`. String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In `"a\nb"`, the backslash-`n` pair represents one newline character, so `len("a\nb") == 3`. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place. In this case: String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`.
- **B:** Incorrect for this question. `str` is immutable, so `del s[0]` raises `TypeError`. Why the correct answer wins: String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`.
- **C:** Correct. In `"a\nb"`, the backslash-`n` pair represents one newline character, so `len("a\nb") == 3`. In this case: String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`.
- **D:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`.
- **E:** Incorrect for this question. `str` does not support item assignment; `s[0] = "X"` raises `TypeError`. Why the correct answer wins: String methods always return new `str` objects because strings are immutable, and escaped characters such as `\n` count as `1` in `len()`; item assignment and `del s[0]` raise `TypeError`.

### Question 43 — C

Answer: `'-'.join(parts)`. `'-'.join(parts)` calls `.join()` on the separator string `'-'` and concatenates every string in `parts`. `sep.join(iterable)` is a method on the separator string, taking an iterable of strings. Local study-map skill 3.12 (String Indexing, Slicing, Immutability, and Common String Methods), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `list.extend(iterable)` appends each element from `iterable` individually and returns `None`. Why the correct answer wins: `'-'.join(parts)` calls `.join()` on the separator string `'-'` and concatenates every string in `parts`.
- **B:** Incorrect for this question. `list.append(x)` adds `x` as a single element at the end of the list in place and returns `None`. Why the correct answer wins: `'-'.join(parts)` calls `.join()` on the separator string `'-'` and concatenates every string in `parts`.
- **C:** Correct. `sep.join(iterable)` is a method on the separator string, taking an iterable of strings. In this case: `'-'.join(parts)` calls `.join()` on the separator string `'-'` and concatenates every string in `parts`.
- **D:** Incorrect for this question. `str.split()` splits text into a `list` of substrings. Why the correct answer wins: `'-'.join(parts)` calls `.join()` on the separator string `'-'` and concatenates every string in `parts`.

### Question 44 — B

Answer: `None`. When a Python function finishes its suite without executing an explicit `return value`, it implicitly returns `None`. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: When a Python function finishes its suite without executing an explicit `return value`, it implicitly returns `None`.
- **B:** Correct. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. In this case: When a Python function finishes its suite without executing an explicit `return value`, it implicitly returns `None`.
- **C:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: When a Python function finishes its suite without executing an explicit `return value`, it implicitly returns `None`.
- **D:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: When a Python function finishes its suite without executing an explicit `return value`, it implicitly returns `None`.

### Question 45 — C

Answer: `def`. `def` defines a named function object in Python. `def` introduces a function or generator definition. Local study-map skill 4.1 (Defining Functions, Invoking Them, return Paths, and Implicit None), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `return` exits the current function immediately and sends a value back to the caller. Why the correct answer wins: `def` defines a named function object in Python.
- **B:** Incorrect for this question. `lambda` is a reserved Python keyword and therefore cannot be used as a variable identifier. Why the correct answer wins: `def` defines a named function object in Python.
- **C:** Correct. `def` introduces a function or generator definition. In this case: `def` defines a named function object in Python.
- **D:** Incorrect for this question. `class` is a reserved keyword and cannot be used as a variable identifier. Why the correct answer wins: `def` defines a named function object in Python.

### Question 46 — B

Answer: `[1, 4, 9]`. Calling `list(sq(3))` iterates the generator across `k = 1, 2, 3`, collecting the yielded squares `[1, 4, 9]`. Collecting yielded squares from the generator produces `[1, 4, 9]`. Local study-map skill 4.2 (Generator Functions Using yield and Lazy Iteration), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Calling `list(sq(3))` iterates the generator across `k = 1, 2, 3`, collecting the yielded squares `[1, 4, 9]`.
- **B:** Correct. Collecting yielded squares from the generator produces `[1, 4, 9]`. In this case: Calling `list(sq(3))` iterates the generator across `k = 1, 2, 3`, collecting the yielded squares `[1, 4, 9]`.
- **C:** Incorrect for this question. Consuming the generator with `list(...)` collects every yielded value until exhaustion. Why the correct answer wins: Calling `list(sq(3))` iterates the generator across `k = 1, 2, 3`, collecting the yielded squares `[1, 4, 9]`.
- **D:** Incorrect for this question. Calling a function whose body contains `yield` returns a generator iterator object. Why the correct answer wins: Calling `list(sq(3))` iterates the generator across `k = 1, 2, 3`, collecting the yielded squares `[1, 4, 9]`.

### Question 47 — A

Answer: `81`. Four multiplications of `3` down to the base case `power(3, 0) == 1` compute `3 * 3 * 3 * 3 * 1 == 81`. Evaluates to the integer `81`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `81`. In this case: Four multiplications of `3` down to the base case `power(3, 0) == 1` compute `3 * 3 * 3 * 3 * 1 == 81`.
- **B:** Incorrect for this question. Evaluates to the integer `27`. Why the correct answer wins: Four multiplications of `3` down to the base case `power(3, 0) == 1` compute `3 * 3 * 3 * 3 * 1 == 81`.
- **C:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: Four multiplications of `3` down to the base case `power(3, 0) == 1` compute `3 * 3 * 3 * 3 * 1 == 81`.
- **D:** Incorrect for this question. `RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth. Why the correct answer wins: Four multiplications of `3` down to the base case `power(3, 0) == 1` compute `3 * 3 * 3 * 3 * 1 == 81`.

### Question 48 — C

Answer: `1`. The multiplicative identity `1` is required at `exp == 0`; returning `0` would collapse every product to `0`. Evaluates to the integer `1`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and Call-Stack Termination), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: The multiplicative identity `1` is required at `exp == 0`; returning `0` would collapse every product to `0`.
- **B:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: The multiplicative identity `1` is required at `exp == 0`; returning `0` would collapse every product to `0`.
- **C:** Correct. Evaluates to the integer `1`. In this case: The multiplicative identity `1` is required at `exp == 0`; returning `0` would collapse every product to `0`.
- **D:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: The multiplicative identity `1` is required at `exp == 0`; returning `0` would collapse every product to `0`.

### Question 49 — A, C

Answers: `calc(10, rate=2)`; `calc(rate=2, base=10)`. `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail. Positional arguments precede keyword arguments and bind each parameter once. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Positional arguments precede keyword arguments and bind each parameter once. In this case: `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail.
- **B:** Incorrect for this question. A positional argument after a keyword argument is a `SyntaxError`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail.
- **C:** Correct. Keyword arguments may appear in any order as long as parameter names match and none are duplicated. In this case: `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail.
- **D:** Incorrect for this question. Passing `base` both positionally and by keyword raises `TypeError: got multiple values for argument`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail.
- **E:** Incorrect for this question. Passing an unexpected keyword argument raises `TypeError` when the function has no `**kwargs`. Why the correct answer wins: `calc(10, rate=2)` and `calc(rate=2, base=10)` bind each parameter once in legal order; positional-after-keyword, duplicate `base`, and unknown `tax` all fail.

### Question 50 — A

Answer: `7`. Keyword arguments match parameters by name rather than position, so `gross` receives `10` and `discount` receives `3`, returning `10 - 3 == 7`. Evaluates to the integer `7`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Argument Passing Rules), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `7`. In this case: Keyword arguments match parameters by name rather than position, so `gross` receives `10` and `discount` receives `3`, returning `10 - 3 == 7`.
- **B:** Incorrect for this question. Evaluates to the integer `13`. Why the correct answer wins: Keyword arguments match parameters by name rather than position, so `gross` receives `10` and `discount` receives `3`, returning `10 - 3 == 7`.
- **C:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: Keyword arguments match parameters by name rather than position, so `gross` receives `10` and `discount` receives `3`, returning `10 - 3 == 7`.
- **D:** Incorrect for this question. `SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar. Why the correct answer wins: Keyword arguments match parameters by name rather than position, so `gross` receives `10` and `discount` receives `3`, returning `10 - 3 == 7`.

### Question 51 — B

Answer: `24`. `units` receives `5` positionally, `box_fee` keeps its default `4`, and `per_unit` is overridden by keyword to `4`, returning `4 + 5 * 4 == 24`. Evaluates to the integer `24`. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Why the correct answer wins: `units` receives `5` positionally, `box_fee` keeps its default `4`, and `per_unit` is overridden by keyword to `4`, returning `4 + 5 * 4 == 24`.
- **B:** Correct. Evaluates to the integer `24`. In this case: `units` receives `5` positionally, `box_fee` keeps its default `4`, and `per_unit` is overridden by keyword to `4`, returning `4 + 5 * 4 == 24`.
- **C:** Incorrect for this question. Evaluates to the integer `12`. Why the correct answer wins: `units` receives `5` positionally, `box_fee` keeps its default `4`, and `per_unit` is overridden by keyword to `4`, returning `4 + 5 * 4 == 24`.
- **D:** Incorrect for this question. Evaluates to the integer `36`. Why the correct answer wins: `units` receives `5` positionally, `box_fee` keeps its default `4`, and `per_unit` is overridden by keyword to `4`, returning `4 + 5 * 4 == 24`.

### Question 52 — B

Answer: `None`. Using immutable `None` as the default parameter sentinel and creating `[]` inside the body guarantees a fresh list per call. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Local study-map skill 4.5 (Default Parameter Values and Shared-Default Pitfalls), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer zero. Why the correct answer wins: Using immutable `None` as the default parameter sentinel and creating `[]` inside the body guarantees a fresh list per call.
- **B:** Correct. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. In this case: Using immutable `None` as the default parameter sentinel and creating `[]` inside the body guarantees a fresh list per call.
- **C:** Incorrect for this question. Evaluates to an empty `list` of length `0`. Why the correct answer wins: Using immutable `None` as the default parameter sentinel and creating `[]` inside the body guarantees a fresh list per call.
- **D:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: Using immutable `None` as the default parameter sentinel and creating `[]` inside the body guarantees a fresh list per call.

### Question 53 — A, B

Answers: Mutating an element via `rates[0] = 99` inside a function modifies the global list in place without needing `global rates`; Reading a module-level variable inside a function works directly as long as the function never assigns to that same name. Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable. Item assignment `rates[0] = ...` mutates the existing list object rather than rebinding the identifier `rates`. Functions look up unassigned names in enclosing and global scopes automatically (LEGB). Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Functions look up unassigned names in enclosing and global scopes automatically (LEGB). In this case: Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable.
- **B:** Correct. Item assignment `rates[0] = ...` mutates the existing list object rather than rebinding the identifier `rates`. In this case: Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable.
- **C:** Incorrect for this question. Plain assignment `rates = []` binds a brand-new local variable and leaves module-level `rates` untouched. Why the correct answer wins: Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable.
- **D:** Incorrect for this question. A fresh list per call happens only when the function uses `None` as the sentinel default and creates `[]` inside the body. Why the correct answer wins: Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable.
- **E:** Incorrect for this question. Parameters are local variables of the function call frame and disappear when the frame exits. Why the correct answer wins: Mutating an element via `rates[0] = 99` mutates the existing list in place without `global`, and reading `rates` works whenever `rates` is not reassigned locally; `rates = []` only rebinds a local variable.

### Question 54 — C

Answer: `99`. Item assignment `rates[0] = 99` mutates the global list object rather than rebinding the name `rates`, so `rates[0]` becomes `99` without needing `global`. Evaluates to the integer `99`. Local study-map skill 4.6 (Name Scopes, Shadowing, and Modifying Globals with global), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Item assignment `rates[0] = 99` mutates the global list object rather than rebinding the name `rates`, so `rates[0]` becomes `99` without needing `global`.
- **B:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: Item assignment `rates[0] = 99` mutates the global list object rather than rebinding the name `rates`, so `rates[0]` becomes `99` without needing `global`.
- **C:** Correct. Evaluates to the integer `99`. In this case: Item assignment `rates[0] = 99` mutates the global list object rather than rebinding the name `rates`, so `rates[0]` becomes `99` without needing `global`.
- **D:** Incorrect for this question. Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`. Why the correct answer wins: Item assignment `rates[0] = 99` mutates the global list object rather than rebinding the name `rates`, so `rates[0]` becomes `99` without needing `global`.

### Question 55 — A, D

Answers: `LookupError` is the abstract parent class of both `IndexError` and `KeyError`; `ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`. `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. In this case: `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`.
- **B:** Incorrect for this question. `tuple` has no `.append()` method; calling it raises `AttributeError`. Why the correct answer wins: `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`.
- **C:** Incorrect for this question. Standard Python `float` uses binary IEEE-754 rather than exact base-10 representation. Why the correct answer wins: `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`.
- **D:** Correct. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). In this case: `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`.
- **E:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: `LookupError` is the abstract parent of `IndexError` and `KeyError`, and `ArithmeticError` is the abstract parent of `ZeroDivisionError` and `OverflowError`.

### Question 56 — D

Answer: `BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`. In Python's hierarchy, `KeyboardInterrupt` and `SystemExit` inherit directly from `BaseException` rather than from `Exception`. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. Local study-map skill 4.7 (Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`. Why the correct answer wins: In Python's hierarchy, `KeyboardInterrupt` and `SystemExit` inherit directly from `BaseException` rather than from `Exception`.
- **B:** Incorrect for this question. `ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`. Why the correct answer wins: In Python's hierarchy, `KeyboardInterrupt` and `SystemExit` inherit directly from `BaseException` rather than from `Exception`.
- **C:** Incorrect for this question. Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`). Why the correct answer wins: In Python's hierarchy, `KeyboardInterrupt` and `SystemExit` inherit directly from `BaseException` rather than from `Exception`.
- **D:** Correct. `except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly. In this case: In Python's hierarchy, `KeyboardInterrupt` and `SystemExit` inherit directly from `BaseException` rather than from `Exception`.

### Question 57 — B

Answer: Raises `IndexError`. Accessing a single sequence index beyond `len(bins) - 1` raises `IndexError` (whereas slicing `bins[5:9]` would return `[]`). `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Accessing a single sequence index beyond `len(bins) - 1` raises `IndexError` (whereas slicing `bins[5:9]` would return `[]`).
- **B:** Correct. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`). In this case: Accessing a single sequence index beyond `len(bins) - 1` raises `IndexError` (whereas slicing `bins[5:9]` would return `[]`).
- **C:** Incorrect for this question. Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value. Why the correct answer wins: Accessing a single sequence index beyond `len(bins) - 1` raises `IndexError` (whereas slicing `bins[5:9]` would return `[]`).
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Accessing a single sequence index beyond `len(bins) - 1` raises `IndexError` (whereas slicing `bins[5:9]` would return `[]`).

### Question 58 — C

Answer: Raises `TypeError`. Adding a `str` and an `int` with `+` is unsupported in Python 3 and raises `TypeError`. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. Local study-map skill 4.8 (Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `15`. Why the correct answer wins: Adding a `str` and an `int` with `+` is unsupported in Python 3 and raises `TypeError`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`). Why the correct answer wins: Adding a `str` and an `int` with `+` is unsupported in Python 3 and raises `TypeError`.
- **C:** Correct. `TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch. In this case: Adding a `str` and an `int` with `+` is unsupported in Python 3 and raises `TypeError`.
- **D:** Incorrect for this question. Concatenating strings `"12" + "3"` yields `"123"` rather than numeric addition `15`. Why the correct answer wins: Adding a `str` and an `int` with `+` is unsupported in Python 3 and raises `TypeError`.

### Question 59 — A, D

Answers: Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`; The `else` branch of `try` runs only when the `try` suite finishes with no exception raised. Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception. `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable. In this case: Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception.
- **B:** Incorrect for this question. A bare `except:` must always be the *last* `except` clause in Python 3; placing it earlier is a `SyntaxError`. Why the correct answer wins: Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception.
- **C:** Incorrect for this question. At most *one* `except` branch executes for a single raised exception. Why the correct answer wins: Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception.
- **D:** Correct. In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally. In this case: Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception.
- **E:** Incorrect for this question. Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code. Why the correct answer wins: Specific subclass handlers must precede broader parent handlers, and the `else` suite executes only when the `try` block raises no exception.

### Question 60 — A

Answer: `try`. `try` opens an exception-handled block whose exceptions are routed to matching `except` clauses. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. Local study-map skill 4.9 (Handling and Propagating Exceptions with Ordered try-except Branches), mapped to the official syllabus: PCEP-30-02 exam syllabus (OpenEDG Python Institute). Primary reference: PCEP-30-02 exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch. In this case: `try` opens an exception-handled block whose exceptions are routed to matching `except` clauses.
- **B:** Incorrect for this question. `while` repeats its indented suite as long as its header condition evaluates to truthy. Why the correct answer wins: `try` opens an exception-handled block whose exceptions are routed to matching `except` clauses.
- **C:** Incorrect for this question. `except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`). Why the correct answer wins: `try` opens an exception-handled block whose exceptions are routed to matching `except` clauses.
- **D:** Incorrect for this question. `finally` introduces cleanup code that runs whether or not an exception was raised or returned. Why the correct answer wins: `try` opens an exception-handled block whose exceptions are routed to matching `except` clauses.
