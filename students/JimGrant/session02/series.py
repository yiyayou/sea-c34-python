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
