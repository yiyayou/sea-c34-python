def fibonacci(n):
    """
    Calculates the nth value of the fibonacci series

    Args: 
        n: the number of the series desired
    Returns:
        nth value of the fibonacci series

    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n  - 1) + fibonacci(n - 2)

def lucas(n):
    """
    Calculates the nth value of the lucas series

    Args: 
        n: the number of the series desired
    Returns:
        nth value of the lucas series

    """
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else: 
        return lucas(n  - 1) + lucas(n - 2)

# Test Code
if __name__ == "__main__":
    print("Testing Fibonacci series")
    for i in range (8):
        print (str(fibonacci(i)) + ", "),
    print("/nTesting Lucas series")
    for i in range (8):
        print (str(lucas(i)) + ", "),
