
def listtest():
    """what happens when you use list characters to split/join the list?"""
    list1 = "this, is, a, comma, ,, end"

    print(list1.split(', '))

# listtest()
# result: the split method is smart and could tell that's a member!"""


def inputtest():
    """what if raw_input is given a function or a Python keyword?"""
    userinpt = raw_input(u'enter a Python keyword and see what happens: ')
    print(userinpt)

# inputtest()
# result: even when user input defines a function it functions as a string!"""


def swappertest():
    """does Swapcase work on strings with mixed uppercases and lowercases?"""
    userinpt = raw_input(u'enter a mixed phrase and watch what happens: ')
    print(userinpt.swapcase())

# swappertest()
# result: totally does"""
