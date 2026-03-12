#!/usr/bin/env python3
"""More edge cases to test - finding patterns we might miss."""

# ========== all() and any() - do we catch these? ==========
items = [1, 2, 3]
if all(items):  # Should flag - needs: if all(items) is True
    pass

if any(items):  # Should flag - needs: if any(items) is True
    pass

# What about negated?
if not all(items):  # Should flag
    pass

if not any(items):  # Should flag
    pass

# ========== Chained boolean operations ==========
a, b, c = [], {}, ""
if a or b or c:  # Should flag all three
    pass

if a and b and c:  # Should flag all three
    pass

# Mixed with explicit
if a or len(b) > 0 or c:  # Should flag a and c, but not len(b) > 0
    pass


# ========== Default arguments with implicit checks ==========
def bad_default(x=None):
    if x:  # Should flag - needs: if x is not None
        return x
    return []


# ========== Walrus operator in weird places ==========
# In while loop
data = [1, 2, 3]
while item := data.pop() if data else None:  # Multiple issues here
    print(item)

# In comprehension filter
results = [y for x in range(10) if (y := x * 2)]  # Implicit y

# ========== Exception handling patterns ==========
try:
    risky_operation()
except Exception as e:
    if e:  # Should flag - exception objects are always truthy when caught
        print(e)

# ========== Context managers with implicit checks ==========
import contextlib


@contextlib.contextmanager
def maybe_context():
    result = None
    yield result


with maybe_context() as ctx:
    if ctx:  # Should flag
        pass


# ========== Yield with conditions ==========
def generator_with_issues():
    items = [1, 0, 2, 0, 3]
    for item in items:
        if item:  # Should flag
            yield item


# Generator expression in yield
def nested_generator():
    yield [x for x in range(10) if x]  # Should flag comprehension and implicit x


# ========== Class-based edge cases ==========
class EdgeCases:
    def __bool__(self):
        # Even inside __bool__, we might have issues
        return True if self.value else False  # Implicit self.value

    def __len__(self):
        # What about comprehensions in special methods?
        return len([x for x in self.items if x])  # Multiple issues

    @property
    def computed(self):
        # Property with ternary
        return self._value if self._value else 0  # Implicit self._value

    @classmethod
    def from_items(cls, items):
        # Comprehension in classmethod
        return cls([x for x in items if x])  # Should flag

    @staticmethod
    def filter_items(items):
        # Lambda in staticmethod
        return filter(lambda x: x, items)  # Should flag lambda x: x


# ========== Operator overloading with implicit checks ==========
class Container:
    def __contains__(self, item):
        # Implicit check in operator overload
        return item if item else False  # Should flag

    def __getitem__(self, key):
        # Ternary in getitem
        return self.data[key] if key else None  # Should flag


# ========== Decorators with implicit checks ==========
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:  # Should flag
            return result
        return None

    return wrapper


# ========== Type annotations edge cases ==========
from typing import Optional


def typed_function(x: Optional[list] = None) -> list:
    # This is a common pattern but still implicit
    return x if x else []  # Should flag


# ========== F-strings with ternary ==========
value = None
message = f"Value: {value if value else 'N/A'}"  # Should flag


# ========== Match/case with guards (Python 3.10+) ==========
def match_with_guards(x):
    match x:
        case [] if x:  # Should flag - guard has implicit check
            return "empty but truthy?"
        case [first, *rest] if first:  # Should flag
            return f"First is {first}"
        case _:
            return "default"


# ========== Nested functions with closures ==========
def outer_function():
    data = []

    def inner():
        if data:  # Should flag - closure variable
            return data[0]

    # Lambda in nested scope
    checker = lambda: data if data else []  # Should flag

    return inner, checker


# ========== asyncio patterns ==========
import asyncio


async def async_implicit():
    result = await some_async_func()
    if result:  # Should flag
        return result

    # Async comprehension (Python 3.6+)
    async_gen = (x async for x in async_source() if x)  # Should flag


# ========== Set/dict operations ==========
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Using set operations in conditions
if set1 & set2:  # Should flag - intersection used as implicit bool
    pass

if set1 - set2:  # Should flag - difference used as implicit bool
    pass

# ========== More slice edge cases ==========
data = [1, 2, 3, 4, 5]
# Slice with ternary
subset = data[1:] if data else []  # Should flag

# ========== collections patterns ==========
from collections import defaultdict, Counter

dd = defaultdict(list)
if dd["key"]:  # Should flag - checking if list is empty
    pass

counter = Counter()
if counter["item"]:  # Should flag - checking if count > 0
    pass

print("Testing more edge cases...")
