"""What is the product of every number in a list?"""


def product(lst):
    total = 1
    for i in lst:
        total = total * i
    return total

"""What is the factorial of any given integer?"""


def factorial(x):
    total = x
    x -= 1
    while x > 0:
        total = total * x
        x -= 1
    return total

"""Is this integer a prime number?"""


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for n in range(2, x-1):
        if x % n == 0:
            return False
        else:
            return True
