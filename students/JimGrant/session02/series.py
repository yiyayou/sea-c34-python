def fibonacci(n):
    """Return the nth number in the Fibonacci series.
    Args:
        n - positive int. The position in the series to return.
    """

    value1, value2 = 0, 1
    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1


def lucas(n):
    """Return the nth number in the Lucas Numbers.
    Args:
        n - positive int. The position in the series to return.
    """

    value1, value2 = 2, 1
    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1


def sum_series(n, value1=0, value2=1):
    """Return the nth number in a recursive integer series.
    Args:
        n - positive int. The position in the series to return.
        value1 - int (optional, default 0). The first number in the sequence to use.
        value2 - int (optional, default 1). The second number in the sequence to use.
    """

    for i in range(n - 1):
        value1, value2 = value2, value1 + value2

    return value1


if __name__ == "__main__":
    # test that the internally supplied numbers in the series are returned properly
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1

    # test a large-ish n for the correct number in the series
    assert fibonacci(10) == 34
    assert lucas(10) == 76
    
    # test the default values act as a fibonacci series
    assert sum_series(10) == 34

    # test a couple different series with large-ish n
    assert sum_series(10, 2, 1) == 76
    assert sum_series(10, 2, 4) == 178
    print("Tests completed successfully!")
