#!/usr/bin/env python3
"""Edge case test file for bool-hunter - testing all the lazy/sloppy patterns."""

# ========== COMPREHENSIONS - THE WORST OFFENDERS ==========

# Double nested comprehension with implicit bool
matrix = [[1, 0, 2], [0, 3, 0], [4, 0, 5]]
# This monstrosity has nested comprehensions AND implicit booleans
double_evil = [[val for val in row if val] for row in matrix if row]

# Triple nested comprehension with multiple implicit bools (absolutely heinous)
cube = [[[1, 0], [2, 0]], [[0, 3], [4, 0]]]
triple_evil = [
    [[item for item in plane if item] for plane in layer if plane]
    for layer in cube
    if layer
]

# Comprehension with multiple filter conditions, all implicit
data = [1, 2, 0, -1, 3, None, "", "hello", False]
multi_filter = [x for x in data if x and hasattr(x, "__len__") if x]

# Dict comprehension with walrus operator and implicit bool (Python 3.8+)
scores = {"alice": 85, "bob": 0, "charlie": 92, "diana": None}
walrus_comp = {
    name: score for name, raw_score in scores.items() if (score := raw_score)
}

# Set comprehension with complex boolean logic
mixed_data = [1, 0, "hello", "", None, [], [1, 2], {}, {"a": 1}]
complex_set = {x for x in mixed_data if x or isinstance(x, list) and x}

# Generator with chained comparisons and implicit bool
gen_evil = (x for x in range(-10, 10) if x and -5 < x < 5)

# ========== IMPLICIT BOOLEAN CHECKS ==========

# Classic implicit checks
x = []
if x:  # implicit - should be: if len(x) > 0
    pass

if not x:  # implicit - should be: if len(x) == 0
    pass

# Boolean functions without is True
obj = object()
if hasattr(obj, "attr"):  # should be: if hasattr(obj, 'attr') is True
    pass

if isinstance(obj, object):  # should be: if isinstance(obj, object) is True
    pass

# Method calls that return booleans
text = "hello"
if text.startswith("h"):  # should be: if text.startswith("h") is True
    pass

path = "/tmp/test"
from pathlib import Path

p = Path(path)
if p.exists():  # should be: if p.exists() is True
    pass

# all() and any() without is True
items = [1, 2, 3]
if all(items):  # should be: if all(items) is True
    pass

if any(items):  # should be: if any(items) is True
    pass

# ========== TERNARY OPERATORS (INLINE IF/ELSE) ==========

# Ternary with implicit bool
value = x if x else None  # implicit x

# Nested ternary (extra evil)
result = (x if x else y) if y else z  # multiple implicit checks


# Ternary in function call
def process(val):
    return val * 2 if val else 0  # implicit val


# ========== LAMBDA FUNCTIONS ==========

# Lambda with implicit bool
check_truthy = lambda x: x if x else None

# Lambda in filter/map
numbers = [1, 0, 2, 0, 3]
filtered = filter(lambda x: x, numbers)  # implicit x in lambda
mapped = map(lambda x: x * 2 if x else 0, numbers)  # implicit x in ternary

# ========== BOOLEAN OPERATIONS ==========

# Mixed and/or with implicit checks
a = []
b = {}
c = ""
if a or b or c:  # all implicit
    pass

if a and b and c:  # all implicit
    pass

# Mixed explicit and implicit
if a or len(b) > 0:  # a is implicit, len(b) > 0 is explicit
    pass

# ========== WHILE LOOPS ==========

items = [1, 2, 3]
while items:  # implicit - should be: while len(items) > 0
    items.pop()

# ========== ASSERT STATEMENTS ==========

assert items  # implicit - should be: assert len(items) == 0

# ========== FILTER WITH None ==========

# filter(None, ...) uses implicit truthiness
values = [0, 1, "", "hello", None, [], [1]]
truthy_only = filter(None, values)

# ========== COMPLEX NESTED STRUCTURES ==========


# Function with multiple issues
def bad_function(data):
    # Comprehension with implicit bool
    filtered = [x for x in data if x]

    # Ternary with implicit bool
    result = filtered if filtered else []

    # While with implicit bool
    while result:
        item = result.pop()
        # Nested if with implicit bool
        if item:
            # Another comprehension
            processed = [i * 2 for i in item if i]
            yield processed


# Class with problematic patterns
class BadClass:
    def __init__(self, items):
        # Comprehension in __init__
        self.items = [x for x in items if x]

    def process(self):
        # Method with implicit bool
        if self.items:
            return True
        return False

    def __bool__(self):
        # Even __bool__ can have issues internally
        return True if self.items else False


# ========== ASSIGNMENT EXPRESSIONS (WALRUS) ==========

# Walrus in if statement with implicit bool
import re

text = "hello123"
if match := re.search(r"\d+", text):  # implicit - should check is not None
    print(match.group())

# Walrus in while with implicit bool
data = [1, 2, 3]
while item := data.pop() if data else None:  # implicit item check
    print(item)

# ========== EDGE CASE: NESTED FUNCTION DEFINITIONS ==========


def outer():
    data = [1, 0, 2, 0, 3]

    # Nested function with comprehension
    def inner():
        return [x for x in data if x]

    # Lambda assigned to variable
    checker = lambda x: x if x else 0

    # Generator function with implicit bool
    def gen():
        for item in data:
            if item:  # implicit
                yield item

    return inner, checker, gen


# ========== ONE-LINERS FROM HELL ==========

# The ultimate evil: nested comprehension with ternary, walrus, and implicit bools
nightmare = [
    [(y := x * 2) if x else 0 for x in row if x or hasattr(x, "__len__")]
    for row in matrix
    if row and any(row)
]

# Dictionary comprehension with nested ternary and implicit checks
dict_nightmare = {
    k: (v if v else (0 if isinstance(v, int) else ""))
    for k, v in {"a": 1, "b": 0, "c": None}.items()
    if k
}

print("If bool-hunter doesn't catch all of these, we have a problem!")
