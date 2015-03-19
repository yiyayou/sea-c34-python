""" Return the nth number of the Fibonacci sequence from user input.

    Arg:
        user: Provide user input, Integer value, from the command line.

    Return:
        Return single integer value of Fibonacci sequence at index,
        determined by user input. """

fibUser = int(raw_input("nth number of Fib: "))


def fib(fibUser):
    x, y, i = 0, 1, 1
    while i < fibUser:
        x, y, i = x+y, x, i+1
    return x

print fib(fibUser)


""" Return the nth number of the Lucas sequence from user input.

    Arg:
        user: Provide user input, Integer value, from the command line.

    Return:
        Return single integer value of Lucas sequence at index,
        determined by user input. """

lucUser = int(raw_input("nth number of Luc: "))


def lucas(lucUser):
    first, second, count = 2, 1, 1
    while count < lucUser:
        first, second, count = second, first + second, count + 1
    return first

print lucas(lucUser)
