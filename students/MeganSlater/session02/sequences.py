"""How many times does the letter e appear in any string?"""


def countE(str):
    str = string.lower()
    return str.count(u'e')

"""What do I need to buy at the store?"""


def shoppingList(groceries=[]):
    print groceries
    goshop = raw_input("Is this everything you need? (y/n) ").lower()
    if goshop == "n":
        addItem = raw_input("What else do you need? ")
        groceries.append(addItem)
        shoppingList(groceries)
    else:
        print "Great.  Let's go shopping."
shoppingList()

"""Does the entry exceed 140 characters?"""


def twitter(tweet):
    if len(tweet) > 140:
        print True
        return True
    else:
        print False
        return False
