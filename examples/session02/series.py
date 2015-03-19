

def fibonacci(n):
    """Return (n)th value in a Fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# example run would be:
# print (fibonacci(10))


def lucas(n):
    """Return (n)th value in a Lucas series"""

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# example run would be:
# print (lucas(10))


def sum_series(n, o=0, p=1):
    """Return (n)th value in series defined by two optional args"""
    """if no args are given series defaults to fibonacci"""

    if n == 0:
        return 0
    elif n == 1:
        return o
    elif n == 2:
        return p

    else:
        return sum_series(n - 1, o, p) + sum_series(n - 2, o, p)

# example run would be:
# print (sum_series(8, 6, 3))


# assertions to verify formulae and functions

if __name__ == "__main__":

    assert fibonacci(5) == 5
    # check fibonacci

    assert lucas(5) == 11
    # check lucas

    assert sum_series(8, 6, 3) == 87
    # check sum_series with arbitrary args 6 and 3

"""note that n count starts from 0;
could be compensated by "n-1" for added intuitiveness"""
