#http://www.scribd.com/doc/10396888/Flowchart-of-Fibonacci-Number-Display-and-Summation

def fibonacci(n):
    """
    Calculate the nth number in a fibonacci sequence

    Args:
            n: the number in the sequence to return
    Returns: the nth number in the fibonacci sequence

    """
    #
    A = 0
    B = 1
    Counter = 1
    C = 0
    
    #
    while Counter <= n :
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            print C

fibonacci(8)

def lucas(n):
    """
      Calculate the nth number in a lucas sequence

    Args:
            n: the number in the sequence to return
    Returns: the nth number in the lucas sequence

    """
    #
    A = 2
    B = 1
    Counter = 1
    C = 0
    
    #
    while Counter <= n :
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            print C

lucas(6)

def sum_series(x, y  = 0, z = 1):
    """
    """
    if y == 2 and z == 1:
        lucas(x)
    else:
        fibonacci(x)
sum_series(10, 0, 1)


    


