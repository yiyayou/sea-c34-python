#Question 1
# What happens when you copy a list and alter its copy?
def question_one():
    """
    Prints contents of two lists to explore the mutability of the list 
    data type. This is accomplished by creating a list, copying it, 
    and then altering the copy.

    """
    test_list = ["happy", "sad"]
    copy_list = test_list
    copy_list.append("mad")
    print ("The test list contains"),
    print(test_list)
    print("The copy list contains: "),
    print(copy_list)

#Question 2:
#
def question_two():
    pass
# Question 3:
#
def question_three():
    pass

# ******************* TEST CODE ************************ #
if __name__ == '__main__':
    question_one()
    question_two()
    question_three()
