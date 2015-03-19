""" Return the nth number of the Fibonacci sequence.

    Arg:
        user: Provide fibUser input, Integer value.

    Return:
        Return single integer value of Fibonacci sequence at index,
        determined by function argument. """


def fib(fibUser):
    first, second, count = 0, 1, 1
    while count < fibUser:
        first, second, count = second, first + second, count+1
    return first


""" Return the nth number of the Lucas sequence.

    Arg:
        user: Provide user input, Integer value.

    Return:
        Return single integer value of Lucas sequence at index,
        determined by function argument. """


def lucas(lucUser):
    first, second, count = 2, 1, 1
    while count < lucUser:
        first, second, count = second, first + second, count + 1
    return first


""" Return the nth number of the Lucas sequence from user input.

    Arg:
        user: Provide user input, Integer value, from the command line.

    Return:
        Return single integer value of Lucas sequence at index,
        determined by user input. """

seriesUser = int(raw_input("nth number of Luc: "))


def sum_series():





"""Both the *fibonacci series* and the *lucas numbers* are based on an
identical formula.

Add a third function called ``sum_series`` with one required parameter
and two optional parameters. The required parameter will determine which
element in the series to print. The two optional parameters will have
default values of 0 and 1 and will determine the first two values for
the series to be produced.

Calling this function with no optional paramters will produce numbers
from the *fibonacci series*. Calling it with the optional arguments 2
and 1 will produce values from the *lucas numbers*. Other values for the
optional parameters will produce other series.

Ensure that your function has a well-formed ``docstring``"""
