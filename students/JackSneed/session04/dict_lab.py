def series01():


    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(lab)
    del lab["cake"]
    print(lab)
    lab["fruit"] = "Mango"
    print(lab.keys())
    print(lab.values())
    key = lab.keys()
    print("cake" in key)
    value = lab.values()
    print("Mango" in value)

series01()



def series02():
    """Using the dict constructor and zip, build a dictionary of numbers
    from zero to fifteen and the hexadecimal equivalent.
    """

    numbers = range(0, 16)
    result = dict(zip(numbers, [hex(hexadecimal) for hexadecimal in numbers]))
    print(result)

series02()


def series03():
    """Using the dictionary from item 1: Make a dictionary using the same
    keys but with the number of ‘a’s in each value.
    """

    new_lab = {}
    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    for a, number in lab.items():
        new_lab[a] = number.count("a")
        print(new_lab)

series03()




