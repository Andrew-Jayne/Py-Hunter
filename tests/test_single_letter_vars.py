#!/usr/bin/env python3
"""Test single-letter variable names that should be flagged."""


# Bad: Single-letter variable names (lazy!)
def calculate(x, y, z):
    a = x + y
    b = a * z
    c = b / 2
    return c


# Bad: Single-letter in loops (except i, j, k maybe?)
for f in files:
    process(f)

for k, v in data.items():
    print(k, v)


# Bad: Single-letter class/function names
class C:
    def m(self, x):
        return x


# Acceptable exceptions?
# - Loop counters: i, j, k
# - Coordinates: x, y, z (debatable)
# - Exceptions: e
# - Temporary: _ (throwaway)

for i in range(10):  # Acceptable?
    print(i)

try:
    risky()
except Exception as e:  # Acceptable?
    print(e)


# Coordinate math (acceptable?)
def distance(x, y):
    return (x**2 + y**2) ** 0.5


# Lambda parameters (current practice)
sorted_items = sorted(items, key=lambda x: x.value)  # x is lazy?

print("Testing single-letter vars...")
