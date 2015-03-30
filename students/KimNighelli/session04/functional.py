'''
This is for Task 12- Exploring Session 5- Lambdas and
Functional Programming

The following functions were written to help clarify some
questions and misunderstandings I had while reviewing the
session 5 lecture notes. Each question will be noted by a
comment line #

Kimberlee Nighelli - 30 March 2015
'''

# Question 1: How does one use a list comprehension with
# a map? Given a list, return each element in the list times 5
# if the element is not divisible by 3 and the original values
# if it is divisible by three

def maps_and_lambdas(a_list):
    '''
    Given a list, returns every value. If the value is not
    divisible by 3, it returns value * 5. If it is divisible
    by 3, it returns the original value
    '''
    return map(lambda x: x * 5 if x % 3 else x, a_list)


# Question 2: Given a list, can I use a lambda function to
# remove the values that are not alphanumberic?

def alpha_lambda(a_list):
    '''
    Given a list, this returns only the alphanumeric
    values in the list
    '''
    return filter(lambda x: x.isalnum(), a_list)



if __name__ == "__main__":

    TEST_LIST = [2, 3, 5, 6, 7, 9, 10, 12]
    print maps_and_lambdas(TEST_LIST)

    TEST_LIST_2 = ["Book", "67@@kdhgfkj", "1234", "&&3ihappy!", "801dexter"]
    print alpha_lambda(TEST_LIST_2)
