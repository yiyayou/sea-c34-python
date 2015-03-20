'''
What I'm going to code:

        Print right triangle
        Print equilateral triangle
        is the word a pallendrome?
'''

"""
def right_triangle(n):
        for i in range(1, n+1):
                print "*"*i


right_triangle(7)
right_triangle(45)
"""

"""
def equi_triangle():
        size = raw_input("What size would you like the equilateral triangle? Please enter an odd number. ")
        print size
        character = raw_input("What character should we use to make the triangle? ")

        space_char = " "

        if size % 2 == 0:
                print "The size is now %s, your input - 1. We need to have an odd number for this problem" % ((size)-1)

equi_triangle()
"""

def pallindrome(x):
        if x == x[::-1]:
                print "%s is a pallindrome!" % (x)
        else:
               print "%s is not a pallindrome" % (x)

pallindrome("abcba")
pallindrome("definitelyNot")
