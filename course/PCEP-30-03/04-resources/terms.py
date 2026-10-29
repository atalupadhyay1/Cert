"""Option bank for the PCEP-30-03 (Certified Entry-Level Python Programmer) practice sets.

Every option is a concrete CPython 3.11 output, runtime or syntax exception, filler token
for a `____` code-fill / gap-fill snippet, operator, collection expression, or Python 3
language rule, paired with a one-sentence explanation of what that option means or produces
so every distractor teaches why it does not fit the question. Keys are internal authoring
identifiers only and never appear in an exported CSV or review copy.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'duplicate option key: {key}')
    TERMS[key] = (label, meaning)


# --- Block 1: Execution model, lexis/syntax/semantics, keywords, literals, operators, I/O ---
t('vm_bytecode_exec', 'CPython compiles `.py` source to bytecode and runs that bytecode inside the Python virtual machine at runtime',
  'Standard CPython translates source code into bytecode instructions executed by its runtime virtual machine rather than linking a native OS binary ahead of time.')
t('aot_elf_binary', 'CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime',
  'Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime.')
t('jit_browser_sandbox', 'CPython executes `.py` source only inside an HTML5 browser DOM engine',
  'CPython is a native host process written in C, not a browser-embedded DOM engine.')
t('static_rom_linker', 'CPython flattens all imported modules into static ROM microcode before parsing syntax',
  'CPython parses source into an AST and bytecode at import or execution time rather than burning microcode.')
t('pyc_cache_role', 'Cached `.pyc` files store compiled Python bytecode so unchanged imported modules skip reparsing on later runs',
  'Files under `__pycache__` hold version-tagged bytecode that speeds up module imports without changing program semantics or removing the need for the PVM.')
t('pyc_native_machine', 'Cached `.pyc` files contain x86-64 machine instructions that run directly on the OS kernel without Python installed',
  '`.pyc` files store portable CPython bytecode for the Python virtual machine, not standalone native CPU machine code.')
t('pyc_encrypt_source', 'Cached `.pyc` files cryptographically sign source code so syntax errors are suppressed in production',
  '`.pyc` files are neither encrypted nor able to bypass syntax validation.')
t('interp_line_stop', 'When an unhandled runtime error occurs, CPython halts execution at the failing bytecode step after running earlier statements',
  'Because CPython executes top-to-bottom at runtime, side effects from earlier statements have already happened when a later line raises an unhandled exception.')
t('interp_rollback_all', 'When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes',
  'Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception.')
t('interp_syntax_before_run', 'CPython parses the entire `.py` file for syntax errors before executing even the first top-level statement',
  'Because CPython compiles a script unit to bytecode before running it, a `SyntaxError` on line 50 prevents line 1 from executing at all.')
t('interp_syntax_at_line', 'CPython runs lines 1 through 49 first and reports a `SyntaxError` on line 50 only if control reaches line 50',
  'Unlike runtime exceptions (`ZeroDivisionError`, `NameError`), `SyntaxError` happens during the parsing pass before execution begins.')

t('err_lexis', 'A lexical error because the character or token itself does not belong to valid Python token forms',
  'Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters.')
t('err_syntax', 'A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules',
  'Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements.')
t('err_semantics', 'A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning',
  'Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary.')
t('err_pep8_style', 'A PEP-8 style violation that causes CPython to refuse compilation before execution begins',
  'PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser.')

t('kw_assert', '`assert`',
  '`assert` is a hard reserved keyword in Python 3 used for debugging assertions.')
t('kw_del', '`del`',
  '`del` is a hard reserved keyword in Python 3 that unbinds names or deletes container items and slices.')
t('kw_elif', '`elif`',
  '`elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch.')
t('kw_except', '`except`',
  '`except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block.')
t('kw_finally', '`finally`',
  '`finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not.')
t('kw_from', '`from`',
  '`from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`.')
t('kw_global', '`global`',
  '`global` is a hard reserved keyword in Python 3 that binds assignments inside a function to the module namespace.')
t('kw_lambda', '`lambda`',
  '`lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function.')
t('kw_nonlocal', '`nonlocal`',
  '`nonlocal` is a hard reserved keyword in Python 3 that targets a name in an enclosing function scope.')
t('kw_pass', '`pass`',
  '`pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement.')
t('kw_raise', '`raise`',
  '`raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception.')
t('kw_return', '`return`',
  '`return` is a hard reserved keyword in Python 3 that exits a function and hands back a value.')
t('kw_with', '`with`',
  '`with` is a hard reserved keyword in Python 3 for context-managed execution blocks.')
t('kw_yield', '`yield`',
  '`yield` is a hard reserved keyword in Python 3 that pauses a generator function and produces the next item.')
t('kw_break', '`break`',
  '`break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop.')
t('kw_continue', '`continue`',
  '`continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration.')
t('kw_while', '`while`',
  '`while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy.')
t('kw_for', '`for`',
  '`for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable.')
t('kw_else', '`else`',
  '`else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks.')
t('kw_in', '`in`',
  '`in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers.')
t('kw_not_in', '`not in`',
  '`not in` tests non-membership and evaluates to `True` when the left operand is absent from the container.')
t('kw_is', '`is`',
  '`is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`).')
t('kw_and', '`and`',
  '`and` is Python\'s short-circuit logical conjunction operator.')
t('kw_or', '`or`',
  '`or` is Python\'s short-circuit logical disjunction operator.')
t('kw_not', '`not`',
  '`not` is Python\'s unary logical negation operator and returns `True` or `False`.')
t('kw_def', '`def`',
  '`def` introduces a named function definition in Python; `function` and `func` are not Python keywords.')
t('kw_bad_func', '`function`',
  '`function` is a JavaScript keyword, not a Python keyword; Python uses `def`.')
t('kw_bad_var', '`var`',
  '`var` is not a Python keyword; Python binds variables directly on assignment.')

t('id_soft_match', '`match`',
  '`match` is a soft keyword in Python 3.10+, so unlike hard keywords it remains usable as a variable identifier.')
t('id_soft_case', '`case`',
  '`case` is a soft keyword in Python 3.10+, so assigning `case = 1` remains legal outside `match` headers.')
t('id_builtin_sum', '`sum`',
  '`sum` is a built-in function name rather than a reserved keyword, though shadowing it is discouraged.')
t('id_builtin_max', '`max`',
  '`max` is a built-in function identifier, not a hard keyword in Python 3.')
t('id_builtin_dict', '`dict`',
  '`dict` is a built-in type name in `builtins`, not a reserved keyword.')
t('id_case_false', '`false`',
  'Python keywords are case-sensitive: `False` is reserved, whereas lowercase `false` is an ordinary identifier.')
t('id_case_none', '`none`',
  'Only capitalized `None` is a reserved keyword; lowercase `none` is a valid variable name.')
t('id_valid_fx_rate', '`fx_rate_2`',
  '`fx_rate_2` starts with a letter and uses only lowercase letters, underscores, and digits, obeying both Python grammar and PEP-8.')
t('id_valid_private', '`_cached_slug`',
  '`_cached_slug` begins with an underscore and contains only letters and underscores, making it a valid Python identifier.')
t('id_valid_seat_row', '`row_14_a`',
  '`row_14_a` starts with an ASCII letter and contains only letters, digits, and underscores.')
t('id_valid_temp', '`dew_point_c`',
  '`dew_point_c` is a legal snake_case identifier starting with a letter.')
t('id_valid_lap', '`_lap_count`',
  '`_lap_count` begins with an underscore and follows valid identifier syntax.')
t('id_valid_flour', '`flour_grams_1`',
  '`flour_grams_1` starts with a letter and uses snake_case recommended by PEP-8.')
t('id_bad_digit', '`2nd_quarter`',
  '`2nd_quarter` starts with a digit and therefore raises `SyntaxError` as an identifier.')
t('id_bad_hyphen', '`fx-rate`',
  '`fx-rate` is parsed as subtraction `fx - rate` because hyphens are illegal in Python identifiers.')
t('id_bad_dollar', '`total$usd`',
  '`$` is not a valid identifier character in Python 3.')
t('id_bad_at', '`user@host`',
  '`@` is the matrix-multiplication / decorator token and cannot appear inside an identifier.')
t('id_bad_space', '`seat count`',
  'Whitespace separates tokens and cannot appear inside a single variable name.')
t('id_bad_dot', '`unit.temp`',
  'A dot `.` performs attribute lookup rather than forming part of one variable name.')

t('indent_4spaces', 'Consistent 4-space indentation for each nested suite without mixing tabs and spaces in the same block',
  'Python defines compound block structure by indentation level, and PEP-8 specifies 4 spaces per level while Python 3 raises `TabError` on inconsistent tab/space mixing.')
t('indent_braces', 'Curly braces `{ ... }` around `if` and `for` bodies so whitespace is completely ignored',
  'In Python, `{ ... }` builds dictionaries or sets rather than delimiting statement suites.')
t('comment_hash', 'Everything after `#` outside a string literal to the end of that physical line is ignored by the parser',
  'Python uses `#` for single-line comments; `#` inside quotes stays an ordinary character in the string.')
t('comment_slashstar', 'C-style `/* ... */` delimiters comment out multi-line blocks in Python',
  'Python has no `/* ... */` comment syntax and raises `SyntaxError` if those tokens appear as code.')

# Literals & bases
t('lit_bin_13', '`0b1101`',
  '`0b1101` is a valid binary integer literal equal to `8 + 4 + 0 + 1 == 13`.')
t('lit_oct_23', '`0o27`',
  '`0o27` is a valid octal integer literal equal to `2 * 8 + 7 == 23`.')
t('lit_hex_42', '`0x2A`',
  '`0x2A` is a valid hexadecimal integer literal equal to `2 * 16 + 10 == 42`.')
t('lit_under_int', '`1_250_000`',
  'Single underscores between digits such as `1_250_000` are legal visual separators in Python 3.6+ numeric literals.')
t('lit_sci_float', '`2.5e-3`',
  'Scientific-notation literals always evaluate to `float` in Python 3 (`2.5e-3 == 0.0025`).')
t('lit_sci_pos', '`4e2`',
  '`4e2` uses exponent notation and evaluates to the `float` `400.0`, not the `int` `400`.')
t('lit_bad_leading0', '`045`',
  'Non-zero decimal integer literals cannot start with a leading `0` in Python 3; octal requires `0o45`.')
t('lit_bad_oct9', '`0o19`',
  'Octal literals allow only digits `0` through `7`, so `9` in `0o19` raises `SyntaxError`.')
t('lit_bad_bin2', '`0b102`',
  'Binary literals allow only `0` and `1`, so `2` in `0b102` raises `SyntaxError`.')
t('lit_bad_trail_under', '`500_`',
  'Numeric literals cannot end with a trailing underscore (`500_` raises `SyntaxError`).')
t('lit_bad_double_under', '`1__000`',
  'Consecutive underscores inside a numeric literal (`1__000`) raise `SyntaxError`.')
t('lit_bad_hex_g', '`0x1G`',
  'Hexadecimal digits stop at `F`/`f`, so `0x1G` raises `SyntaxError`.')

# Operators
t('op_truediv', '`/`',
  'True division `/` always returns a `float` in Python 3, even when both operands divide evenly (`8 / 2 == 4.0`).')
t('op_floordiv', '`//`',
  'Floor division `//` rounds the quotient down toward negative infinity (`math.floor`).')
t('op_mod', '`%`',
  'Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`).')
t('op_pow', '`**`',
  'Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left.')
t('op_iadd', '`+=`',
  '`+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets.')
t('op_imul', '`*=`',
  '`*=` scales a number or repeats a sequence in place / by rebinding.')
t('op_ifloordiv', '`//=`',
  '`//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable.')
t('op_bit_and', '`&`',
  'Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`.')
t('op_bit_or', '`|`',
  'Bitwise OR `|` sets each output bit to `1` whenever at least one integer operand has `1`.')
t('op_bit_xor', '`^`',
  'Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python).')
t('op_bit_inv', '`~`',
  'Bitwise inversion `~x` flips all bits in two\'s-complement arithmetic and equals `-(x + 1)`.')
t('op_lshift', '`<<`',
  'Left shift `x << n` multiplies integer `x` by `2 ** n`.')
t('op_rshift', '`>>`',
  'Right shift `x >> n` floor-divides integer `x` by `2 ** n`.')

# Numbers & scalar values
t('num_neg16', '`-16`', 'Evaluates to the integer `-16`.')
t('num_neg9', '`-9`', 'Evaluates to the integer `-9`.')
t('num_neg7', '`-7`', 'Evaluates to the integer `-7`.')
t('num_neg6', '`-6`', 'Evaluates to the integer `-6`.')
t('num_neg4', '`-4`', 'Evaluates to the integer `-4`.')
t('num_neg3', '`-3`', 'Evaluates to the integer `-3`.')
t('num_neg2', '`-2`', 'Evaluates to the integer `-2`.')
t('num_neg1', '`-1`', 'Evaluates to the integer `-1`.')
t('num_0', '`0`', 'Evaluates to the integer `0`.')
t('num_1', '`1`', 'Evaluates to the integer `1`.')
t('num_2', '`2`', 'Evaluates to the integer `2`.')
t('num_3', '`3`', 'Evaluates to the integer `3`.')
t('num_4', '`4`', 'Evaluates to the integer `4`.')
t('num_5', '`5`', 'Evaluates to the integer `5`.')
t('num_6', '`6`', 'Evaluates to the integer `6`.')
t('num_7', '`7`', 'Evaluates to the integer `7`.')
t('num_8', '`8`', 'Evaluates to the integer `8`.')
t('num_9', '`9`', 'Evaluates to the integer `9`.')
t('num_10', '`10`', 'Evaluates to the integer `10`.')
t('num_11', '`11`', 'Evaluates to the integer `11`.')
t('num_12', '`12`', 'Evaluates to the integer `12`.')
t('num_13', '`13`', 'Evaluates to the integer `13`.')
t('num_14', '`14`', 'Evaluates to the integer `14`.')
t('num_15', '`15`', 'Evaluates to the integer `15`.')
t('num_16', '`16`', 'Evaluates to the integer `16`.')
t('num_17', '`17`', 'Evaluates to the integer `17`.')
t('num_18', '`18`', 'Evaluates to the integer `18`.')
t('num_19', '`19`', 'Evaluates to the integer `19`.')
t('num_20', '`20`', 'Evaluates to the integer `20`.')
t('num_21', '`21`', 'Evaluates to the integer `21`.')
t('num_23', '`23`', 'Evaluates to the integer `23`.')
t('num_24', '`24`', 'Evaluates to the integer `24`.')
t('num_25', '`25`', 'Evaluates to the integer `25`.')
t('num_27', '`27`', 'Evaluates to the integer `27`.')
t('num_28', '`28`', 'Evaluates to the integer `28`.')
t('num_30', '`30`', 'Evaluates to the integer `30`.')
t('num_32', '`32`', 'Evaluates to the integer `32`.')
t('num_36', '`36`', 'Evaluates to the integer `36`.')
t('num_42', '`42`', 'Evaluates to the integer `42`.')
t('num_45', '`45`', 'Evaluates to the integer `45`.')
t('num_48', '`48`', 'Evaluates to the integer `48`.')
t('num_64', '`64`', 'Evaluates to the integer `64`.')
t('num_65', '`65`', 'Evaluates to the integer `65` (`ord(\'A\')`).')
t('num_81', '`81`', 'Evaluates to the integer `81`.')
t('num_97', '`97`', 'Evaluates to the integer `97` (`ord(\'a\')`).')
t('num_120', '`120`', 'Evaluates to the integer `120`.')
t('num_256', '`256`', 'Evaluates to the integer `256`.')

t('flt_0_0', '`0.0`', 'Evaluates to the floating-point value `0.0`.')
t('flt_2_0', '`2.0`', 'Evaluates to the floating-point value `2.0`.')
t('flt_2_5', '`2.5`', 'Evaluates to the floating-point value `2.5`.')
t('flt_3_0', '`3.0`', 'Evaluates to the floating-point value `3.0`.')
t('flt_3_5', '`3.5`', 'Evaluates to the floating-point value `3.5`.')
t('flt_4_0', '`4.0`', 'Evaluates to the floating-point value `4.0`.')
t('flt_4_5', '`4.5`', 'Evaluates to the floating-point value `4.5`.')
t('flt_6_0', '`6.0`', 'Evaluates to the floating-point value `6.0`.')
t('flt_neg3_0', '`-3.0`', 'Evaluates to the floating-point value `-3.0`.')
t('flt_neg4_0', '`-4.0`', 'Evaluates to the floating-point value `-4.0`.')
t('flt_400_0', '`400.0`', 'Scientific literal `4e2` evaluates to the `float` `400.0`.')
t('int_400', '`400`', 'The integer `400` (`int`), whereas exponent literals like `4e2` produce `float` `400.0`.')

t('val_true', '`True`', 'Evaluates to Boolean `True`.')
t('val_false', '`False`', 'Evaluates to Boolean `False`.')
t('val_none', '`None`', 'Evaluates to `None`, Python\'s singleton null value.')
t('str_usd_default', "`'USD'`", "Short-circuit `'' or 'USD'` returns the right-hand truthy string `'USD'`.")
t('str_guest_default', "`'guest'`", "Short-circuit `'' or 'guest'` returns `'guest'`.")
t('str_num_1212', "`'1212'`", "Repeating the two-character string `'12'` with `* 2` concatenates `'1212'` rather than multiplying numerically.")
t('str_num_252525', "`'252525'`", "Multiplying string `'25'` by `3` repeats the characters to form `'252525'`.")
t('flt_imprecise_false', 'It prints `False` because binary IEEE-754 floats store tenths like `0.1` and `0.2` with tiny rounding residuals',
  'Base-2 floating-point cannot represent most base-10 tenths exactly, so `0.1 * 3` (`0.30000000000000004`) is not `== 0.3`.')
t('flt_exact_true', 'It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects',
  'Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly.')

# Console I/O & casts
t('io_sep_slash', "`sep='/'`",
  "`sep='/'` joins multiple `print()` arguments with a forward slash instead of the default single space.")
t('io_sep_colon', "`sep=':'`",
  "`sep=':'` places a colon between consecutive positional arguments passed to `print()`.")
t('io_sep_empty', "`sep=''`",
  "`sep=''` concatenates positional arguments in `print()` with no separator characters between them.")
t('io_end_comma', "`end=', '`",
  "`end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line.")
t('io_end_empty', "`end=''`",
  "`end=''` suppresses the trailing newline at the end of a `print()` call.")
t('io_end_bang', "`end='!'`",
  "`end='!'` finishes the printed line with `!` instead of `'\\n'`.")
t('io_out_url', "`https://api.local/v2/users`",
  "`print('https://api.local', 'v2', 'users', sep='/')` joins all three strings with `'/'`.")
t('io_out_tags', "`A-B/C`",
  "First `print('A', 'B', sep='-', end='/')` writes `A-B/`, and the second `print('C')` appends `C` on the same line.")
t('io_out_tags_space', "`A B/C`",
  "That output would occur only if `sep` were left at its default single space.")
t('io_out_two_lines', r"`A-B` on line 1 and `C` on line 2",
  "A line break between `B` and `C` appears only when `end` is left at its default newline.")
t('cast_int', '`int`',
  '`int(...)` converts a base-10 digit string or truncates a float toward zero into an integer.')
t('cast_float', '`float`',
  '`float(...)` parses a numeric string such as `\'19.95\'` into a floating-point number.')
t('cast_str', '`str`',
  '`str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings.')
t('cast_bool', '`bool`',
  '`bool(...)` tests truthiness; for ANY non-empty string — including `\'0\'` and `\'False\'` — `bool(...)` returns `True`.')
t('cast_ord', '`ord`',
  '`ord(ch)` returns the integer Unicode code point of a 1-character string (for example `ord(\'A\') == 65`).')
t('cast_chr', '`chr`',
  '`chr(code)` returns the 1-character string for integer Unicode code point `code` (for example `chr(65) == \'A\'`).')
t('input_returns_str', '`<class \'str\'>` because `input()` always returns text even when the user types digits',
  '`input()` reads a line from standard input and strips the trailing newline, always returning a `str` object.')
t('input_returns_int', '`<class \'int\'>` because `input()` automatically parses integer digits',
  'Unlike Python 2\'s `input()`, Python 3\'s `input()` never evaluates or auto-casts typed digits.')

# --- Block 2: Conditionals, ternary, truthiness, loops, ranges, else, nested ---
t('tern_valid_fee', "`0 if subtotal >= 50 else 5`",
  "Python's conditional expression has the form `<when_true> if <cond> else <when_false>`.")
t('tern_valid_badge', "`'VIP' if points >= 100 else 'STD'`",
  "A valid conditional expression places the true value first, followed by `if <condition> else <false_value>`.")
t('tern_bad_c_style', "`subtotal >= 50 ? 0 : 5`",
  "C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python.")
t('tern_bad_no_else', "`0 if subtotal >= 50`",
  "A conditional expression (unlike a list comprehension filter) requires an `else` clause or raises `SyntaxError`.")
t('tern_bad_order', "`if subtotal >= 50 then 0 else 5`",
  "Python has no `then` keyword and does not start an inline conditional expression with `if`.")

t('out_tier_gold', '`GOLD`', 'Prints `GOLD`.')
t('out_tier_silver', '`SILVER`', 'Prints `SILVER`.')
t('out_tier_bronze', '`BRONZE`', 'Prints `BRONZE`.')
t('out_tier_both', '`GOLD` followed by `SILVER`', 'Prints both `GOLD` and `SILVER` when two independent `if` statements both match.')
t('out_status_ok', '`OK`', 'Prints `OK`.')
t('out_status_warn', '`WARN`', 'Prints `WARN`.')
t('out_status_alert', '`ALERT`', 'Prints `ALERT`.')
t('out_status_crit', '`CRIT`', 'Prints `CRIT`.')
t('out_status_idle', '`IDLE`', 'Prints `IDLE`.')
t('out_loop_clean', '`CLEAN`', 'Prints `CLEAN` from the loop `else` suite.')
t('out_loop_halt', '`HALT`', 'Prints `HALT` before `break` skips the loop `else` suite.')
t('out_loop_empty', 'Nothing is printed', 'Prints nothing to standard output.')

# Truthy / Falsy items
t('falsy_empty_tuple', '`()`', 'An empty tuple `()` has length `0` and evaluates to `False` in a Boolean context.')
t('falsy_empty_dict', '`{}`', 'An empty dictionary `{}` has length `0` and evaluates to `False` in a Boolean context.')
t('falsy_empty_str', "`''`", "An empty string `''` has length `0` and evaluates to `False` in a Boolean context.")
t('falsy_empty_list', '`[]`', 'An empty list `[]` has length `0` and evaluates to `False` in a Boolean context.')
t('falsy_zero_float', '`0.0`', 'Numeric zero `0.0` evaluates to `False` in a Boolean context.')
t('falsy_none_lit', '`None`', '`None` always evaluates to `False` in a Boolean context.')
t('truthy_str_zero', "`'0'`", "`'0'` is a 1-character string (`len('0') == 1`), so it is truthy (`bool('0') is True`).")
t('truthy_str_false', "`'False'`", "`'False'` is a 5-character non-empty string, so `bool('False')` evaluates to `True`.")
t('truthy_str_space', "`' '`", "`' '` contains one space character (`len(' ') == 1`), so it is truthy.")
t('truthy_list_empty_str', "`['']`", "`['']` is a 1-element list containing an empty string, so the list itself has length `1` and is truthy.")
t('truthy_tuple_zero', '`(0,)`', '`(0,)` is a 1-element tuple (`len((0,)) == 1`), so it evaluates to `True` even though its element is `0`.')
t('truthy_neg_int', '`-1`', 'Every non-zero integer, including negative integers such as `-1`, is truthy in Python.')
t('truthy_dict_none', '`{0: None}`', '`{0: None}` has one key-value entry (`len == 1`), so it evaluates to `True`.')

# Logical & chained comparisons
t('cmp_chain_port', '`1024 <= port <= 65535`',
  'Chained comparison `1024 <= port <= 65535` evaluates `port` once and requires both `1024 <= port` and `port <= 65535` to hold.')
t('cmp_and_port', '`port >= 1024 and port <= 65535`',
  'Combining both relational checks with `and` returns `True` exclusively when `port` lies inside `[1024, 65535]`.')
t('cmp_or_bug', '`port >= 1024 or port <= 65535`',
  'Using `or` here evaluates to `True` for EVERY integer because every number is either `>= 1024` or `<= 65535`.')
t('cmp_bitand_distinct_bug', '`port >= 1024 & port <= 65535`',
  'Because `&` binds tighter than `>=` and `<=`, Python parses `port >= (1024 & port) <= 65535`, which does NOT test the port range.')
t('cmp_assign_syntax', '`port >= 1024 && port <= 65535`',
  '`&&` is not a valid operator in Python and raises `SyntaxError`; Python uses the keyword `and`.')

t('cmp_chain_zone', '`120 <= bpm < 160`',
  'Chained comparison `120 <= bpm < 160` is `True` when `bpm` is at least `120` and strictly below `160`.')
t('cmp_and_zone', '`bpm >= 120 and bpm < 160`',
  'Joining both bounds with `and` checks `[120, 160)` accurately.')
t('cmp_or_zone_bug', '`bpm >= 120 or bpm < 160`',
  'Using `or` returns `True` for every number.')
t('cmp_bit_zone_bug', '`bpm >= 120 & bpm < 160`',
  'Bitwise `&` binds tighter than comparisons, evaluating `120 & bpm` first.')
t('cmp_eq_zone_bug', '`120 <= bpm <= 160`',
  'Using `<= 160` includes `160`, violating a strict upper bound `< 160`.')

# Range expressions
t('rng_4_items_a', '`range(2, 10, 2)`', '`range(2, 10, 2)` generates `2, 4, 6, 8` (four integers).')
t('rng_4_items_b', '`range(10, 2, -2)`', '`range(10, 2, -2)` generates `10, 8, 6, 4` (four integers).')
t('rng_empty_pos', '`range(8, 2)`', '`range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items.')
t('rng_empty_neg', '`range(2, 8, -2)`', '`range(2, 8, -2)` steps downward away from `8`, yielding zero items.')
t('rng_5_items', '`range(0, 10, 2)`', '`range(0, 10, 2)` generates `0, 2, 4, 6, 8` (five integers).')
t('rng_3_items_a', '`range(3, 12, 3)`', '`range(3, 12, 3)` generates `3, 6, 9` (three integers).')
t('rng_3_items_b', '`range(9, 0, -3)`', '`range(9, 0, -3)` generates `9, 6, 3` (three integers).')
t('rng_2_items', '`range(3, 9, 3)`', '`range(3, 9, 3)` stops before `9`, yielding only `3, 6` (two integers).')

# Loop else facts
t('loop_else_exhaust', 'When a `for` loop finishes iterating over every element without executing `break`',
  'Normal exhaustion of a `for` iterable runs the attached `else:` suite.')
t('loop_else_false_while', 'When a `while` loop\'s condition evaluates to `False` (including on the very first check) without executing `break`',
  'Whenever the `while` condition turns falsy naturally — even after zero iterations — its `else:` suite runs.')
t('loop_else_on_break', 'Immediately after a `break` statement jumps out of the loop body',
  '`break` bypasses both the remaining iterations AND the loop\'s `else:` suite.')
t('loop_else_on_exc', 'Whenever an unhandled exception aborts the loop body',
  'An unhandled exception unwinds out of the loop without running its `else:` suite.')
t('loop_else_on_return', 'Right before a `return` statement inside the loop exits the enclosing function',
  '`return` exits the whole function immediately and skips any loop `else:` suite.')

# --- Block 3: Lists, tuples, dicts, strings ---
t('lst_empty', '`[]`', 'The empty list `[]`.')
t('lst_rev_4321', '`[40, 30, 20, 10]`', 'Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`.')
t('lst_mid_20_30', '`[20, 30]`', 'Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`.')
t('lst_stride_15_35', '`[15, 35]`', 'Slice `[1::2]` picks indices `1` and `3`: `[15, 35]`.')
t('lst_stride_10_30_50', '`[10, 30, 50]`', 'Slice `[::2]` picks indices `0`, `2`, and `4`: `[10, 30, 50]`.')
t('lst_neg_tail', '`[40, 50]`', 'Slice `[-2:]` returns the last two items `[40, 50]`.')
t('lst_neg_rev_step', '`[50, 30, 10]`', 'Slice `[::-2]` walks backward from the end by `-2`, yielding `[50, 30, 10]`.')
t('lst_overslice_ok', '`[30, 40]`', 'Slicing past `len(seq)` such as `seq[2:99]` clamps safely without raising `IndexError`.')
t('lst_append_nested', '`[1, 2, [3, 4]]`', '`.append([3, 4])` adds the entire list object as a single nested third element.')
t('lst_extend_flat', '`[1, 2, 3, 4]`', '`.extend([3, 4])` iterates its argument and appends each element individually.')
t('lst_mut_append', '`items.append(x)`', '`.append(x)` mutates `items` in place by adding `x` at the end and returns `None`.')
t('lst_mut_extend', '`items.extend(seq)`', '`.extend(seq)` mutates `items` in place by appending every element of `seq` and returns `None`.')
t('lst_mut_insert', '`items.insert(0, x)`', '`.insert(0, x)` shifts existing elements right and inserts `x` at index `0` in place.')
t('lst_mut_sort', '`items.sort()`', '`items.sort()` sorts the list in place and returns `None` rather than a new list.')
t('lst_mut_pop', '`items.pop()`', '`items.pop()` removes and returns the last element (or element at index `i`), mutating `items`.')
t('lst_mut_remove', '`items.remove(x)`', '`items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent.')
t('lst_nonmut_sorted', '`sorted(items)`', '`sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged.')
t('lst_nonmut_plus', '`items + [x]`', '`items + [x]` allocates and returns a new concatenated list without mutating `items`.')
t('lst_nonmut_slice', '`items[:]`', '`items[:]` creates a shallow copy as a new outer list object.')
t('lst_copy_method', '`items.copy()`', '`items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original.')
t('lst_copy_ctor', '`list(items)`', '`list(items)` constructs a new outer list containing the same element references (a shallow copy).')
t('lst_alias_assign', '`backup = items`', 'Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy).')
t('lst_comp_squares_even', '`[0, 4, 16]`', 'Filtering even numbers `0, 2, 4` from `range(6)` and squaring them produces `[0, 4, 16]`.')
t('lst_comp_squares_odd', '`[1, 9, 25]`', 'Filtering odd numbers `1, 3, 5` from `range(6)` and squaring them produces `[1, 9, 25]`.')
t('lst_comp_syntax_valid', '`[n * 2 for n in nums if n > 0]`', 'In a filtering list comprehension, `if <cond>` comes AFTER the `for` clause.')
t('lst_comp_syntax_bad_if', '`[n * 2 if n > 0 for n in nums]`', 'Putting `if n > 0` before `for` without an `else` branch raises `SyntaxError`.')
t('lst_del_slice_res', '`[10, 50]`', 'Deleting `vals[1:4]` from `[10, 20, 30, 40, 50]` removes indices `1, 2, 3` in place, leaving `[10, 50]`.')
t('lst_method_append_id', '`append`', '`.append(item)` adds `item` as a single element at the end of a list.')
t('lst_method_extend_id', '`extend`', '`.extend(iterable)` appends each element yielded by `iterable` to the list.')
t('lst_method_insert_id', '`insert`', '`.insert(index, item)` places `item` before `index` in the list.')
t('lst_method_pop_id', '`pop`', '`.pop([index])` removes and returns the element at `index` (default `-1`).')
t('lst_method_remove_id', '`remove`', '`.remove(value)` removes the first matching `value` by equality.')
t('lst_builtin_sorted_id', '`sorted`', 'Built-in `sorted(iterable)` returns a new sorted list without mutating its input.')
t('lst_builtin_len_id', '`len`', 'Built-in `len(s)` returns the element count of collection `s`.')

# Tuples
t('tup_singleton_comma', '`(42,)`', 'A trailing comma creates a 1-element `tuple` (`type((42,)) is tuple`).')
t('tup_bare_comma', '`42,`', 'Tuple construction is driven by the comma, so `x = 42,` also packs a 1-element `tuple`.')
t('tup_parens_int', '`(42)`', 'Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`).')
t('tup_empty_ctor', '`tuple()`', '`tuple()` with no arguments returns the empty 0-element tuple `()`, not a 1-element tuple.')
t('tup_inner_list_ok', "`('A', [1, 2, 3])`", 'Although a tuple cannot rebind its slots, mutating an existing list element in place via `t[1].append(3)` succeeds.')
t('tup_hashable_key', 'A tuple of immutable values (`(10, 20)`) can be used as a `dict` key, whereas a `list` (`[10, 20]`) raises `TypeError`',
  'Tuples containing only hashable objects are hashable, whereas lists are mutable and unhashable.')
t('tup_unhashable_inner', 'A tuple containing a `list` (`(10, [20])`) cannot be used as a `dict` key and raises `TypeError`',
  'A tuple is hashable only when every element inside it is also hashable.')

# Dictionaries
t('dict_method_get', '`get`', '`d.get(key, default=None)` looks up `key` safely and returns `default` if `key` is missing.')
t('dict_method_items', '`items`', '`d.items()` returns a view of `(key, value)` pairs.')
t('dict_method_values', '`values`', '`d.values()` returns a view of the dictionary\'s values.')
t('dict_method_keys', '`keys`', '`d.keys()` returns a view of the dictionary\'s keys.')
t('dict_get_default', "`rates.get('CHF', 0)`", "`.get('CHF', 0)` returns the value for `'CHF'` if present or `0` if `'CHF'` is missing without raising `KeyError`.")
t('dict_idx_keyerr', "`rates['CHF']`", "Direct indexing `rates['CHF']` raises `KeyError` when `'CHF'` is absent from `rates`.")
t('dict_pop_default', "`rates.pop('CHF', 0)`", "`.pop(k, default)` removes and returns `rates[k]` if found, or returns `default` without `KeyError` when `k` is absent.")
t('dict_keys_check', 'Membership `k in d` checks only dictionary keys, not dictionary values',
  'Iterating `d` or testing `x in d` inspects the dictionary\'s keys (`d.keys()`); checking values requires `x in d.values()`.')
t('dict_vals_check', 'Membership `k in d` checks both keys and values simultaneously',
  '`x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`.')
t('dict_items_pairs', '`.items()` yields `(key, value)` 2-tuples suitable for `for k, v in d.items():` unpacking',
  '`d.items()` returns a dynamic view of `(key, value)` pairs.')
t('dict_values_view', '`.values()` yields every stored value in insertion order',
  '`d.values()` returns a view over the dictionary\'s values.')
t('dict_keys_view', '`.keys()` yields every key in insertion order',
  '`d.keys()` returns a view over the dictionary\'s keys.')
t('dict_dup_key_last', 'Duplicate keys in a literal keep a single entry whose value is the last assignment evaluated',
  'When a dictionary literal repeats an equal key (including `1` and `True`), the later value overwrites the earlier value.')

# Strings
t('str_escape_len_3', r"`3`, because `\n` is stored as one newline character rather than two separate characters",
  r"Inside a normal string literal, `\n` (and `\t` or `\\`) represents one character, so `'a\nb'` has length `3`.")
t('str_escape_len_4', r"`4`, because Python counts `\` and `n` separately in every string literal",
  r"Only raw strings (`r'a\nb'`) keep both `\` and `n` as two characters (`len == 4`).")
t('str_escaped_quote', r"""`'Chef\'s kiss'`""",
  r"Backslash-escaping `\'` inside single quotes produces a valid string literal containing an apostrophe.")
t('str_double_quote_apos', """`"Chef's kiss"`""",
  'Wrapping a string containing `\'` inside double quotes `"..."` needs no backslash escape.')
t('str_bad_unescaped_apos', """`'Chef's kiss'`""",
  'An unescaped single quote inside single quotes closes the string early and raises `SyntaxError`.')
t('str_bad_trailing_bs', r"""`'C:\temp\'`""",
  r"A single trailing backslash escapes the closing quote and raises `SyntaxError`.")
t('str_join_dash', "`'-'.join(parts)`",
  "`sep.join(iterable)` is a method on the separator string and requires every element of `iterable` to be a `str`.")
t('str_join_wrong_inv', "`parts.join('-')`",
  "`list` has no `.join()` method (`AttributeError`); `.join()` belongs to `str`.")
t('str_method_find', '`find`', '`s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent.')
t('str_method_index', '`index`', '`s.index(sub)` returns the lowest index of `sub`, or raises `ValueError` if `sub` is absent.')
t('str_method_split', '`split`', '`s.split(sep)` splits a string around `sep` and returns a `list` of substrings.')
t('str_method_strip', '`strip`', '`s.strip()` returns a new string with leading and trailing whitespace removed.')
t('str_method_replace', '`replace`', '`s.replace(old, new)` returns a new string where occurrences of `old` are replaced with `new`.')
t('str_find_neg1', '`-1` because `.find()` returns `-1` instead of raising `ValueError` when a substring is absent',
  'Unlike `.index()`, which raises `ValueError` on a miss, `str.find()` returns `-1`.')
t('str_immut_typeerr', '`TypeError` because `str` objects are immutable and do not support item assignment',
  'Assigning to `s[0] = ...` raises `TypeError: \'str\' object does not support item assignment`.')
t('str_split_url', "`['https:', '', 'example.org', 'docs']`",
  "`'https://example.org/docs'.split('/')` preserves the empty string between the two consecutive slashes.")
t('str_strip_res', "`'token-42'`",
  "`.strip()` removes leading and trailing whitespace characters while leaving internal hyphens intact.")
t('str_upper_lower', 'String case methods such as `.upper()`, `.lower()`, and `.title()` always return a new string and leave the original unchanged',
  'Because strings are immutable in Python, every transformation method allocates and returns a new `str`.')
t('str_slice_rev', "`'nohtyP'`", "`'Python'[::-1]` steps backward from the end and returns `'nohtyP'`.")
t('str_slice_step2', "`'Pto'`", "`'Python'[::2]` picks characters at indices `0`, `2`, and `4`, returning `'Pto'`.")
t('str_ascii_order', "`True`, because code-point order places digits (`'0'`–`'9'`) before uppercase (`'A'`–`'Z'`) and uppercase before lowercase (`'a'`–`'z'`)",
  "Python compares strings lexicographically by Unicode code point (`'9' (57) < 'A' (65) < 'a' (97)`).")
t('str_ascii_false', "`False`, because Python compares strings case-insensitively by alphabetical order",
  "Standard `<` and `>` on strings are case-sensitive code-point comparisons.")

# --- Block 4: Functions, generators, recursion, params, scope, exceptions ---
t('fn_implicit_none', '`None`, because reaching the end of a function body or a bare `return` implicitly returns `None`',
  'Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`.')
t('fn_print_vs_return', 'It prints the text inside the function and then assigns `None` to the caller variable because `print()` returns `None`',
  'Confusing `print(x)` with `return x` leaves the function returning `None` after displaying `x` to stdout.')
t('fn_return_tuple', 'Returning `a, b` packs and returns a 2-element `tuple` `(a, b)` that the caller can unpack',
  'A comma-separated expression after `return` returns a single `tuple` object.')
t('fn_early_return', 'The first executed `return` exits the function immediately and skips all remaining statements in its body',
  'Code after an executed `return` inside the same branch does not run (except an enclosing `finally:` block).')
t('gen_returns_iter', 'Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet',
  'Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory.')
t('gen_next_call', '`next`',
  'Built-in `next(gen)` advances a generator to its next `yield` expression and returns the yielded value.')
t('gen_exhaust_empty', '`[]`, because a generator iterator is single-pass and already exhausted after the first `list(g)` call',
  'Unlike a `list` or `range`, a generator object cannot be rewound; iterating it a second time yields zero elements.')
t('gen_stop_iter', '`StopIteration`',
  'Calling `next()` on an exhausted generator raises `StopIteration`.')
t('gen_pause_resume', '`yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call',
  'Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption.')

t('rec_missing_base', '`RecursionError` because without a reachable base case the call stack exceeds Python\'s recursion limit',
  'Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`).')
t('rec_base_needed', 'A reachable base case that returns directly without making another recursive call',
  'Valid finite recursion requires at least one non-recursive base branch.')
t('rec_step_converge', 'A recursive call whose arguments move strictly closer to the base case on each step',
  'Without progress toward the base condition, recursion never terminates cleanly.')
t('rec_needs_global', 'Declaring every parameter `global` inside the function header',
  'Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax.')
t('rec_needs_yield', 'Replacing every `return` statement with `break` inside the `def` body',
  '`break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion.')

t('arg_pos_after_kw_err', '`SyntaxError` because a positional argument cannot follow a keyword argument at a call site',
  'In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments.')
t('arg_dup_val_err', '`TypeError` because the same parameter receives both a positional argument and a keyword argument',
  'Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`.')
t('arg_valid_kw_swap', '`calc(rate=0.2, base=100)`',
  'Keyword arguments may appear in any order as long as each parameter name matches the signature and receives one value.')
t('arg_valid_mixed', '`calc(100, rate=0.2)`',
  'Passing `100` positionally first and `rate=0.2` by keyword second satisfies Python\'s call-site rules.')
t('arg_bad_pos_after_kw', '`calc(base=100, 0.2)`',
  'Placing positional `0.2` after keyword `base=100` raises `SyntaxError`.')
t('arg_bad_dup_base', '`calc(100, base=200)`',
  'Passing `100` to `base` positionally and `base=200` by keyword raises `TypeError`.')
t('arg_bad_unknown_kw', '`calc(100, tax=0.2)`',
  'Passing an unknown keyword parameter name `tax` when the signature is `def calc(base, rate):` raises `TypeError`.')

t('param_def_order_err', '`SyntaxError` because a parameter without a default value cannot follow a parameter with a default value',
  'In a `def` signature (`def f(a=1, b):`), required positional-or-keyword parameters must precede parameters with default values.')
t('param_def_valid_sig', '`def quote(amount, rate=1.1, fee=0):`',
  'Placing required parameter `amount` before defaulted parameters `rate=1.1` and `fee=0` is valid Python signature order.')
t('param_def_bad_sig', '`def quote(rate=1.1, amount, fee=0):`',
  'Placing non-default `amount` after default `rate=1.1` raises `SyntaxError`.')
t('mut_default_shared', 'Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument',
  'A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default.')
t('mut_default_none_fix', 'Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body',
  'Using `None` as a sentinel creates a fresh list on each call that omits `buf`.')
t('mut_out_two_calls', '`[[1, 2], [1, 2]]` or `[1, 2]` on the second call because both calls mutated the same default list',
  'When `def add(x, acc=[]): acc.append(x); return acc` is called as `add(1)` then `add(2)`, the second call returns `[1, 2]`.')
t('lst_1_2', '`[1, 2]`', 'Evaluates to the two-element list `[1, 2]`.')
t('lst_2_only', '`[2]`', 'Evaluates to the single-element list `[2]`.')
t('lst_1_only', '`[1]`', 'Evaluates to the single-element list `[1]`.')

t('scope_shadow_local', 'Assigning to a name inside a function without `global` creates a separate local variable, leaving the module-level variable unchanged',
  'Under Python\'s LEGB rule, local assignment binds in the function\'s local frame rather than mutating the module global.')
t('scope_unbound_err', '`UnboundLocalError` because assigning to the variable anywhere in the function marks it local across the entire function body',
  'Python determines local names at compile time; reading `x` before a later `x += 1` or `x = ...` in the same function raises `UnboundLocalError`.')
t('scope_read_global_ok', 'Reading a module-level variable inside a function without assigning to it succeeds via the `G` step of LEGB without needing `global`',
  '`global` is required only when rebinding (`=`, `+=`, etc.) a module-level name inside a function; read-only lookup or mutating a global list via `.append()` works without `global`.')
t('scope_mutate_global_list', 'Calling `.append()` on a module-level list inside a function mutates that list in place without needing `global`',
  'Method calls mutate an existing object rather than rebinding the variable name, so Python resolves the name in module scope.')

# Exceptions & hierarchy
t('exc_syntax', '`SyntaxError`',
  '`SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts.')
t('exc_indent', '`IndentationError`',
  '`IndentationError` (a subclass of `SyntaxError`) is raised when suite indentation levels do not align validly.')
t('exc_type', '`TypeError`',
  '`TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count.')
t('exc_value', '`ValueError`',
  '`ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int(\'12.5\')` or `int(\'abc\')`).')
t('exc_zero_div', '`ZeroDivisionError`',
  '`ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`.')
t('exc_index', '`IndexError`',
  '`IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range.')
t('exc_key', '`KeyError`',
  '`KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key.')
t('exc_name', '`NameError`',
  '`NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope.')
t('exc_attr', '`AttributeError`',
  '`AttributeError` is raised when accessing a method or attribute name that does not exist on that object\'s type.')
t('exc_lookup', '`LookupError`',
  '`LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`.')
t('exc_arith', '`ArithmeticError`',
  '`ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`.')
t('exc_base', '`BaseException`',
  '`BaseException` sits at the root of the entire exception tree; `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` rather than `Exception`.')
t('exc_exception_cls', '`Exception`',
  '`Exception` is the base class for almost all runtime non-exit errors (`ValueError`, `TypeError`, `LookupError`, `ArithmeticError`), inheriting from `BaseException`.')
t('exc_sys_exit', '`SystemExit`',
  '`SystemExit` inherits directly from `BaseException` (NOT `Exception`) so `except Exception:` does not accidentally swallow `sys.exit()`.')
t('exc_kb_interrupt', '`KeyboardInterrupt`',
  '`KeyboardInterrupt` inherits directly from `BaseException` (NOT `Exception`) so Ctrl-C interrupts are not swallowed by `except Exception:`.')
t('exc_assertion', '`AssertionError`',
  '`AssertionError` is raised when an `assert <condition>` statement evaluates `<condition>` as falsy.')
t('exc_unbound', '`UnboundLocalError`',
  '`UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function.')
t('exc_recursion', '`RecursionError`',
  '`RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded.')

t('try_order_broad_shadow', 'An earlier `except Exception:` (or `except LookupError:`) catches subclass errors first, making a later subclass handler unreachable',
  '`except` clauses are tested top to bottom using `isinstance`, so a parent exception handler placed first intercepts all its subclasses.')
t('try_order_specific_first', 'Place specific subclass handlers (such as `except ZeroDivisionError:`) BEFORE broader parent handlers (such as `except ArithmeticError:` or `except Exception:`)',
  'Ordering narrow subclasses before broader superclasses lets specialized handlers run before general fallbacks.')
t('try_else_meaning', 'The `else:` block runs only when the `try:` block completes normally without raising an exception',
  'In `try / except / else / finally`, `else:` executes after `try:` only if no exception was raised in `try:`, and before `finally:`.')
t('try_finally_meaning', 'The `finally:` block always runs on the way out — whether `try:` succeeded, an `except:` ran, an uncaught exception propagated, or `return` executed',
  '`finally:` is guaranteed cleanup code that runs before control leaves the `try` statement.')
t('try_tuple_syntax', '`except (KeyError, IndexError):`',
  'To catch multiple exception classes in one handler, pass a parenthesized tuple of exception types after `except`.')
t('try_bad_comma_py2', '`except KeyError, IndexError:`',
  'Unparenthesized `except A, B:` was Python 2 syntax and raises `SyntaxError` in Python 3.')
t('try_out_try_else_fin', '`T-E-F`',
  'When no exception occurs in `try:`, Python runs `try` (`T`), then `else` (`E`), and finally `finally` (`F`), skipping `except`.')
t('try_out_try_exc_fin', '`T-X-F`',
  'When `try:` raises a caught exception after printing `T`, Python runs the matching `except` (`X`) and then `finally` (`F`), skipping `else`.')
t('try_out_try_fin_only', '`T-F`',
  'Would omit either `else` (on success) or `except` (on caught failure).')
t('try_out_all_four', '`T-X-E-F`',
  '`except:` and `else:` are mutually exclusive on any single execution of a `try` statement.')

# Additional concrete expressions and outputs for Sets 2-6
t('while_fin_dec', '`n = 6` followed by `while n > 0: n -= 2`',
  'Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations.')
t('while_fin_div', '`n = 16` followed by `while n >= 2: n //= 2`',
  'Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations.')
t('while_inf_inc', '`n = 1` followed by `while n > 0: n += 1`',
  'Incrementing a positive integer keeps `n > 0` forever, producing an infinite loop.')
t('while_inf_pass', '`n = 5` followed by `while n > 0: pass`',
  'Because `pass` never updates `n`, `n > 0` remains `True` indefinitely.')
t('while_inf_mod', '`n = 4` followed by `while n % 2 == 0: n += 2`',
  'Adding `2` to an even integer keeps `n` even on every step, so `n % 2 == 0` never turns `False`.')

