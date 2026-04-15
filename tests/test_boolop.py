# type: ignore
value = True
other = False
count: int = 5


# -- and with implicit operands --
result = value and other

result = value is True and other is False


# -- or with implicit operands --
result = value or other

result = value is True or other is True


# -- mixed: some implicit, some explicit --
result = value and count > 0

result = value is True and count > 0


# -- and with explicit comparisons --
result = count > 0 and count < 10

result = value is True and value is False


# -- or with explicit comparisons --
result = count > 0 or count < 10

result = value is True or value is False


# -- chained --
result = value and other and value

result = count > 0 and count < 10 and count != 5
