def fibonacci(n):
    """Return nth value of fibonacci series."""
    first, second = 0, 1
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    print(value)
    return value


def lucas(n):
    """Return nth value of lucas numbers series."""
    first, second = 2, 1
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    print(value)
    return value


def sum_series(n, first=0, second=1):
    """Return nth value of sum series.

    Arguments:
    n -- the number in the series of the returned value
    first -- the first value of the series
    second -- the second value of the series
    """
    first, second = first, second
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    print(value)
    return value


sum_series(6, 2, 1)
