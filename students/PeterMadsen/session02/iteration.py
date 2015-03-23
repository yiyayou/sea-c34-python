#Question 1: What does it look like when you iterate through a "Truthy" List?
def question_one (test_list):
    """Prints "Happy" every time a given list is true"""

    for value in test_list:
        if value:
            print ("Happy"),

#Question 2: What does "continue" vs "break" look like in  a range of 10?
def question_two():
    """Prints the Values of two for loops inspecting the differences"""
    
    print ("Break Loop: ")
    for i in range (10):
        if i == 8:
            break
        else:
            print(i), 

    print("\nContinue Loop: ")
    for i in range (10):
        if i == 8:
            continue
        else: 
            print(i), 

#Question 3: 
def question_three():
    pass

# ************* TEST CODE *******************#
if __name__ == '__main__':
    print("Testing Question 1: What does it look like when you iterate through a 'Truthy' List?")
    question_one([True, False, True, 1, 0])
    print('\nQuestion 2: What does "continue" vs "break" look like in  a range of 10?')
    question_two()
