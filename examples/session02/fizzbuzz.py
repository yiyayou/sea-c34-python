from __future__ import print_function

def fizzbuzz():
    """ this will be fizzbuzz"""
    for x in range (0, 100):
        if (x & 3 == 0) and (x & 5 != 0):
          absprint(u"Fizz")
        elif (x & 5 == 0) and (x & 3 != 0):
            print(u"Buzz")
        elif (x & 5 == 0) and (x & 3 == 0):
            print(u"FizzBuzz!")
        else:
            print(x)

fizzbuzz()
