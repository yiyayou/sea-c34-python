#############################################
# This is for Task 4- Mathematical Series
############################################

# Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# The function for a Fibonnaci series is F(n) = F(n-1) + F(n-2)
# Where n is the nth number in the series.
# What we know- F(0) = 0, F(1) = 1, F(2) = 1
# For this assignment, we calculate the nth number in the series

def fibonacci(n):
        if n < 0:
                return None
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)

# Lucas Series
# 2, 1, 3, 4, 7, 11, 18, 29, ...
# The function for the Lucas number is the same as Fibonacci,
# except that the first number is a 2 instead of the 0,1 pair. 
# For this assignment, we calculate the nth number in the series


def lucas(n):
        if n < 0:
                return None
        if n == 0:
                return 2
        elif n == 1:
                return 1
        else:
                return lucas(n-1) + lucas (n-2)


print fibonacci(0)
