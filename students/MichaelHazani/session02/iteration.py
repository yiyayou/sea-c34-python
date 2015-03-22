def indextest():
    """can you still use an index when the list has numbers?"""
    numlist = range(10)
    for idx, num in enumerate(numlist):
        print(idx, num)

# indextest()
# result: you sure can!


def whiletest():
    """Will a condition change mid-iteration cancel the action which hinged"""
    """on that condition, or will the iteration finish before reexamination?"""
    i = 1
    while i < 5:
        i = 67
        print(u"Hello")


# whiletest()
# result: it will keep running before reexamining the condition.

def oprangetest():
    """can you declare ranges that are math operations?"""
    for i in range(3 ** 5):
        print(u"Wow, it's working! So many lines!")

# oprangetest()
# result: seems like you can get away with anything as long as it's a number!
