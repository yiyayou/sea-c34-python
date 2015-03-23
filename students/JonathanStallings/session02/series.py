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


fibonacci(7)
