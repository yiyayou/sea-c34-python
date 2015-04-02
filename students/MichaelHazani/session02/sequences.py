def unholymix():
    """What happens when you multiply two strings?"""
    print("I'm a string" * "I'm another string")

# unholymix()
# result: getting a nice 'can't multiply sequence by non-int of type 'str''


def pissingcontest():
    """with min/max, who's 'bigger', letters or numbers?"""
    test = "A string with letters and numbers like 4 and 4574575"
    print(max(test))

# pissingcontest()
# result: apparently letters are 'bigger' than numbers!


def commasexperiment():
    """is nothing BUT commas a proper tuple?"""
    commatuple = (, , , , , , , , , ,)
    print(type(commatuple))

# commasexperiment()
# result: nope, getting a syntax error because containers need values!
