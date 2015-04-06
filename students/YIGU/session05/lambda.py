# This function returns a list of n functions, such that each one, when called,\
# will return the input value, incremented by an increasing number.


def list_functions(n):
    functions = [lambda x:x] * n
    print functions
    for i in range(n):
        functions[i] = lambda x: x+i
        print functions[i]
