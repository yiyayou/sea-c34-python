def fibonacci(n):
    """
    Calculates the nth value of the fibonacci series

    Args: 
        n: the number of the sequence desired
    Returns:
        nth value of the fibonacci series

    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n  - 1) + fibonacci(n - 2)



# Test Code
if __name__ == "__main__":
    print("Testing fibonacci sequence")
    for i in range (8):
        print (str(fibonacci(i)) + ", "),
