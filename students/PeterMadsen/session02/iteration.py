#Question 1: What does it look like when you iterate through a Boolean List?
def question_one (test_list):
    """Prints "Happy" every time a given list is true"""

    for value in test_list:
        print(value)
        if value:
            print ("Happy")

#Question 2: What is the behaviour of "continue" in a for loop?
def question_two():
    pass

#Question 3: 
def question_three():
    pass

# ************* TEST CODE *******************#
if __name__ == '__main__':
    question_one([True, False, True, 1, 0])