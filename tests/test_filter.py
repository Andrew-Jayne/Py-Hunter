# type: ignore
items = [1, None, 2, None, 3]


# -- filter(None) --
result = filter(None, items)

result = list(filter(None, items))


# -- explicit filter predicate --
result = filter(lambda x: x is not None, items)

result = list(filter(lambda x: x is not None, items))


# -- list comprehension with explicit filter --
result = [item for item in items if item is not None]


# -- generator with explicit filter --
result = (item for item in items if item is not None)


# -- filter with other predicates --
result = filter(lambda x: x > 0, [1, -1, 2, -2])

result = list(filter(lambda x: x > 0, [1, -1, 2, -2]))
