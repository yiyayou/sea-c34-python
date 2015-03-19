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
        if n == 1:
                return 1
        if n > 1:
                return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(0)
