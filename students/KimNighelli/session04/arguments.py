'''
This is for Task 12- Exploring Session 5- Arguments

The following functions were written to help clarify some
questions and misunderstandings I had while reviewing the
session 5 lecture notes. Each question will be noted by a
comment line #

Kimberlee Nighelli - 30 March 2015
'''

# Question 1: To better understand how to use keyword arguments,
# can I calculate the area of a triangle using keyword arguments?

def area_triange(base=0, height=0):
    '''
    Calculate the area of a triange where A = 1/2 * b * h
    '''
    area = 0.5 * base * height
    print "The area of a triange with base %f and height %f is %f \
            " % (base, height, area)

    return area

measurements = {"base":3, "height":4}
area_triange(**measurements)


# Question 2: To betterunderstand how to use .format(), can I create a
# string that holds various weather data using keyword arguments?


