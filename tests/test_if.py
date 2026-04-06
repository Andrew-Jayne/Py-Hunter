value = True


if value:
    pass
if value is True:
    pass

if not value:
    pass
if value is False:  # pyright: ignore[reportUnnecessaryComparison]
    pass

if value and value:
    pass
if value is True and value is True:
    pass

if not value and not value:
    pass
if value is False and value is False:  # pyright: ignore[reportUnnecessaryComparison]
    pass
