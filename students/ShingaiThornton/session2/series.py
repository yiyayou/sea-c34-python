def fibonacci(n):
    """
      Calculates the nth number in a fibonacci sequence

    Args:
            n: the number in the sequence to return
    Returns: the nth number in the fibonacci sequence

    """
    
    A = 0
    B = 1
    Counter = 1
    C = 0
    
    while Counter <= n :
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            return C   

def lucas(n):
    """
      Calculates the nth number in a lucas sequence

    Args:
            n: the number in the sequence to return
    Returns: the nth number in the lucas sequence

    """
    
    A = 2
    B = 1
    Counter = 1
    C = 0   
    
    while Counter <= n :
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            return C 

def sum_series(x, y  = 0, z = 1):
    """
    Calculates number in a series

    Args:
    x: Reqeured paramater specifying number in the sequence to return
    y: Optional parameter determining first number in a series
    z: Optional parameter determining second number in a series

    Returns: The nth number in either a fibonacci or lucas sequence
    """
    if y == 2 and z == 1:
        return lucas(x)
    else:
        return fibonacci(x)

if __name__ == "__main__":
    assert(lucas(5) == 7)
    print lucas(5)
    assert(fibonacci(5) == 3)
    print fibonacci(5)
    assert(sum_series(3,2,1) == 3)
    print sum_series(3, 2, 1)