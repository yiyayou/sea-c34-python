# questions about the dictionaries section in slides 4

mydict = {"mary": 20, "josh": 100, "zuleika": 2}


def addtodict(dictname, key, value):
    """
    The question is: can I use a dictionary function to add names for my donor list?
    """
    dictname[key] = value
    return dictname

print mydict

addtodict(mydict, "mary", 50)
addtodict(mydict, "cassie", 500)

print mydict

def gettotals(dictname, key):
    """
    Will a dictionary return total value for multiple same keys?
    """
    for
