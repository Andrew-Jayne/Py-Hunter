# type: ignore
# -- implicit boolean: BoolOp --
checker = lambda first, second: first and second

def checker_explicit(first, second):
    return first and second


# -- implicit boolean: UnaryOp(Not) --
negator = lambda value: not value

def negator_explicit(value):
    return not value


# -- implicit boolean: ternary with implicit test --
handler = lambda count: 1 if count else 0

def handler_explicit(count):
    if count is not None:
        return 1
    else:
        return 0


# -- clean lambdas: explicit operations --
doubler = lambda num: num * 2

upper = lambda text: text.upper()

comparator = lambda num: num > 0

identity = lambda value: value


# -- clean lambdas: method/function calls --
getter = lambda obj: obj.value

caller = lambda items: len(items)


# ── --disallow-lambda: all lambdas flagged ──────────────────────────────────
# with this flag, even clean lambdas are flagged

simple_math = lambda num: num + 1  # flagged with --disallow-lambda

simple_call = lambda text: text.upper()  # flagged with --disallow-lambda

def simple_math_explicit(num):
    return num + 1

def simple_call_explicit(text):
    return text.upper()
