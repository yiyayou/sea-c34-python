#!/usr/bin/env python

def action_one ():
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit_list)
    
    user_fruit = raw_input("Please submit a new fruit to the list: ")
    print("You submitted %s" %user_fruit)

    user_number = raw_input("Please select a fruit from the list using a numeral: ")
    user_number = int(user_number)
    print("You selsected the number %d which corresponds to  the fruit %s"\
     % (user_number, fruit_list[user_number - 1]))
    
    # add fruit using +
    fruit_list.insert(0, "Strawberries")
def action_two():
    pass

def action_three():
    pass

def action_four():
    pass

#********************* TEST CODE ************************#
if __name__ == '__main__':
    action_one()