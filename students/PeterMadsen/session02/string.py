#Question 1: How many string conversion types are there?
def question_one():
    print ("There are %d different conversion types according to Python Documentation" % 16)

#Question 2: Why do we have %i and %d for ints and %f and %F for floats?
def question_two(): 
    """Formats two different phrases using 4 different operators"""
    print ("Why are there %i ways to write an int" %2)
    print ("Why are there %d ways to write an int" %2)
    print ("Why are there %f ways to write a float" %2.0)
    print ("Why are there %F ways to write an float" %2.0)

# **************** TEST CODE ***************************#
if __name__ == '__main__':
    question_one()
    question_two()
    