items = [1, 2, 3, 4, 5]
pairs = [("a", 1), ("b", 2)]
mixed: list[int | None] = [1, None, 2, None, 3]


# -- list comp --
result = [item for item in items]

result: list[int] = []
for item in items:
    result.append(item)


# -- set comp --
unique = {item for item in items}

unique: set[int] = set()
for item in items:
    unique.add(item)


# -- dict comp --
lookup = {key: val for key, val in pairs}

lookup = {}
for key, val in pairs:
    lookup[key] = val


# -- generator --
total = sum(item * 2 for item in items)

total = 0
for item in items:
    total += item * 2


# -- explicit if filter --
filtered = [item for item in items if item > 0]

filtered: list[int] = []
for item in items:
    if item > 0:
        filtered.append(item)


# -- implicit if filter --
filtered = [item for item in mixed if item]

filtered = []
for item in mixed:
    if item is not None:
        filtered.append(item)


# -- filter(None) --
cleaned = list(filter(None, mixed))

cleaned: list[int | None] = []
for item in mixed:
    if item is not None:
        cleaned.append(item)


# -- nested generators --
nested = [item for item in items for other in items]

nested: list[int] = []
for item in items:
    for other in items:
        nested.append(item)
