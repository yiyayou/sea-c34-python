def series01():


    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(lab)
    del lab["cake"]
    print(lab)
    lab["fruit"] = "Mango"
    print(lab.keys())
    print(lab.values())
    print("cake" in lab)
    print(lab["fruit"])

series01()
