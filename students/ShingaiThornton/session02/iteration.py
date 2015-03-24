#Q1: How does list enumeration work?
""" Create and print an index for a list

     Args: 

     Returns:
"""
def listEnumerate():
faowiejgawe
    flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip'] 
    print list(enumerate(flavors))

listEnumerate()



#Q2:  Can while loops be placed inside for loops?
""" Print all numbers between in a rangeexcept for 5
     
     Args:

     Returns: numbers 
"""

def printNumbers():

    for x in xrange(20):
       
        while x != 5 :
            print x
            x = x + 1
            break

printNumbers()

 

#Q3: How would I rewrite the for loop from the slides (starting on line 143) as a while loop?
"""
Print the numbers 25 - 50 using a while loop

Args:

Returns:
"""


def forAsWhileLoop():

    i = 1

    while i < 100:
        i = i + 1
       
        if i > 50:
            break
        if i < 25:
            continue
        print(i)    

forAsWhileLoop()




