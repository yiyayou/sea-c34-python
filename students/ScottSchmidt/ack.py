def ack(m, n):
    if m < 0 or n < 0:
        return "Invalid arguments"
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m-1, ack(m, n-1))

"""A(m, n) =
    n+1 if m = 0
    A(m−1, 1) if m > 0 and n = 0
    A(m−1, A(m, n−1)) if m > 0 and n > 0.

    Create a new module called ack.py in your student folder. In that module,
    write a function named ack that performs Ackermann's function.

    Write a good doctoring for your function according to PEP 257 (Links to an
    external site.).
    Ackermann's function is not defined for input values less than 0. Validate
    inputs to your function and return None if they are negative.
    The wikipedia page provides a table of output values for inputs between 0
    and 4. Using this table, add an ``if __name__ == "__main__":`` block to
    test your function.

    Test each pair of inputs for "m" between 0 and 3 and "n" between 0 and 4.
    Assert that the result produced by your function is the result expected by
    the wikipedia table. What happens when you run the function with values
    of "m" greater than 3?

    When your module is run from the command line, these tests should be
    executed. If they all pass, print "All Tests Pass" as the result.

    Add your new module to your git clone and commit frequently while working
    on your implementation. Include good commit messages that explain
    concisely both what you are doing and why.

    When you are finished, push your changes to your fork of the class
    repository in GitHub. Then make a pull request and submit your assignment
    here in canvas."""
