# Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    """Return the nth value in the fibonacci series, starting at 0"""
    b1 = 0
    b2 = 1
    if n > 2:
        counter = 3
        while (counter <= n):
            b3 = b1 + b2
            b1 = b2
            b2 = b3
            counter += 1
        b3 = b1 + b2
    elif n > 0:
        b3 = 1
    else:
        b3 = 0
    return b3

user_input = raw_input("Enter the index of fibonacci series: ")
user_input = int(user_input)
print "The nth term is: " + str(fibonacci(user_input))


# Lucas Numbers
# 2, 1, 3, 4, 7, 11, 18, 29, ...

def lucas(n):
    """Return the nth value in the lucas series"""
    b1 = 2
    b2 = 1
    if n > 1:
        counter = 3
        while (counter <= n):
            b3 = b1 + b2
            b1 = b2
            b2 = b3
            counter += 1
        b3 = b1 + b2
    elif n > 0:
        b3 = 1
    else:
        b3 = 2
    return b3

user_input = raw_input("Enter the index of lucas series: ")
user_input = int(user_input)
print "The nth term is: " + str(lucas(user_input))