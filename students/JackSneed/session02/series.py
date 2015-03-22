def fabonacci(n):
    """Return the nth value in the fibonacci series."""

    val1, val2 = 0, 1
    for i in range(n):
        val1, val2 = val2, val1 + val2

    return val1

#Test if fabonacci function works properly
if __name__ == '__main__':
    assert fabonacci(3) == 2

def lucas(n):
    """Return the nth value in the Lucas series."""

    val1, val2 = 2, 1
    for i in range(n):
        val1, val2 = val2, val1 + val2

    return val1

#Test if lucas function works properly
if __name__ == '__main__':
    assert lucas(3) == 4
