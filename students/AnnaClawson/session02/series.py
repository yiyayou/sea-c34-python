def fibonacci(n):
    """This function returns the nth term in the Fibonacci sequence.
    F2 is the (n-1) term and F1 is the (n-2) term.
    """
    F1 = 0
    F2 = 1
    F = 0

    for i in range(1,n):
        F1 = F2
        F2 = F
        F = F2 + F1 
    return F

def lucas(m):
    """This function returns the mth term in the Lucas sequence.
    F2 is the (m-1) term and F1 is the (m-2) term.
    """
    F1 = 2
    F2 = 1
    F = 2

    if m == 0:
        F = 2
    elif m == 1:
        F = 1
    else:
        for i in range(1,m-1):
            F = F2 + F1
            F1 = F2
            F2 = F
    return F

if __name__ == '__main__':
    assert fibonacci(5) == 3
    assert lucas(5) == 7


