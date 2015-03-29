def compremath():
    """can you do math in comprehensions?"""
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [var * 8 for var in list1]
    return list2

# print compremath()
# result: yup! Returns [8, 16, 24, 32, 40, 48, 56, 64]


def comprevarimath():
    """can you utilize other variables in comprehensions?"""
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list2 = [var - (var + 1) for var in list1]
    return list2

# print comprevarimath()
# result: yes! Returns [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


def lambdacall():
    """can lambda call another function?"""
    def add(x, y):
        return x + y

    1 = [lambda x, y: x * y + add(x, y)]
    return 1[0](1, 2)

# print lambdacall()
# result: NO! "SyntaxError: can't assign to literal". Makes sense.
