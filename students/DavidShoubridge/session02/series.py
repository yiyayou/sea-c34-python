x = 0
y = 1


def fibonacci(n):
    """
    Return the nth number in the Fibonacci Series.

    Arg:
        n(int): Element within the Fibonacci series.
    Return:
        The value in the Fibonacci Series that corresponds to the value of n.
    """
    if n == x:
        return 0
    elif n == y:
        return 1
    else:
        series = [0, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]

print fibonacci(4)


def lucas(n):
    """
    Return the nth number in the Lucas Series.

    Arg:
        n(int): Index within the Lucas series.
    Return:
        The value in the Lucas Series that corresponds to the value of n.
    """
    if n == x:
        return 2
    elif n == y:
        return 1
    else:
        series = [2, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]

print lucas(4)


def sum_series(n, x=0, y=1):
    """
    Return numbers from either Fibonacci Series or Lucas Series depending on \
    arguments.

    Args:
        n(int): Determines which element in the series to print.
        x(int): Optional standard argument that will return numbers from \
        Fibonacci Series if used.
        y(int): Optional standard argument that will return numbers from the \
        Fibonacci Series if used.
    """

    if (x == 0) and (y == 1):
        return fibonacci(n)
    elif (x == 2) and (y == 1):
        return lucas(n)

print sum_series(5)
