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



def serieso4():
    """Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    """
    s2 = set(range(0, 21)[::2])
    s3 = set(range(0, 21)[::3])
    s4 = set(range(0, 21)[::4])
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

serieso4()




