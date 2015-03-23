"""
1. What's the ordinal values of my name: Karen?

"""

for i in "Karen":
    print(ord(i), end="")


"""
2. How to create a greeting using the __format__() method?

"""

name = input("What's your name")

if name == "Karen":
    print("{}, you have a cool name".format(name))
else:
    print("{}, you have a awesome name".format(name))
