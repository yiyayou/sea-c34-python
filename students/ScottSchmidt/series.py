""" Return the nth number of the Fibonacci sequence from user input.

    Arg:
        user: Provide user input, Integer value, from the command line.

    Return:
        Return single integer value of Fibonacci sequence at index,
        determined by user input. """

user = int(raw_input("nth number of Fib: "))


def fib(user):
    x, y, i = 0, 1, 1
    while i < user:
        x, y, i = x+y, x, i+1
    return x

print fib(user)


""" Return the nth number of the Fibonacci sequence from user input.

    Arg:
        user: Provide user input, Integer value, from the command line.

    Return:
        Return single integer value of Fibonacci sequence at index,
        determined by user input. """

user = int(raw_input("nth number of Fib: "))


def fib(user):
    x, y, i = 0, 1, 1
    while i < user:
        x, y, i = x+y, x, i+1
    return x

print fib(user)
