def fibonacci(n):
    """Return the nth number in the Fibonacci series."""

    value1, value2 = 0, 1
    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1


def lucas(n):
    """Return the nth number in the Lucas Numbers."""

    value1, value2 = 2, 1
    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1


def sum_series(n, value1=0, value2=1):
    """Return the nth number in a recursive integer sequence.
    Args:
        value1 - The first number in the sequence to use.
        value2 = The second number in the sequence to use.
    """

    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1
