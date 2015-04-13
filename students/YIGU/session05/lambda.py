# This function returns a list of n functions, such that each one, when\
# called, will return the input value, incremented by an increasing number.

# failed number1
"""def list_functions(n):
    functions = [''] * n
    for i in range(n):
        functions[i] = lambda x: x+i
    return functions"""

# failed number2
"""
def list_functions(n):
    functions = []
    for i in range(n):
        functions.append(lambda x: x+i)
    return functions
"""


def var_factory(n):
    return lambda x: x+n


def list_functions(n):
    functions = []
    for i in range(n):
        functions.append(var_factory(i))
    return functions


functions = list_functions(5)

assert functions[0](2) == 2
assert functions[1](2) == 3
assert functions[2](2) == 4
