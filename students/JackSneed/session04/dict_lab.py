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
    for hexadecimal in numbers:
        result = dict(zip(numbers, [hex(hexadecimal)]))
        print(result)

series02()
