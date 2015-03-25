#!/usr/bin/env python

def action_one ():
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit_list)
    
    user_fruit = raw_input("Please submit a new fruit to the list: ")
    print("You submitted %s" %user_fruit)
    fruit_list.append(user_fruit)

    user_number = raw_input("Please select a fruit from the list using a numeral: ")
    user_number = int(user_number)
    print("You selsected the number %d which corresponds to  the fruit %s"\
     % (user_number, fruit_list[user_number - 1]))
    
    fruit_list  = ["Apriocts"] + fruit_list
    fruit_list.insert(0, "Strawberries")

    print("Here are the fruits that begin with 'P':")
    for fruit in fruit_list:
        if fruit[0] == 'P':
            print(fruit)

    return fruit_list

def action_two(my_fruit_list):
    print(my_fruit_list)
    my_fruit_list.pop()
    print(my_fruit_list)


    my_fruit_list *= 2
    remove_fruit = raw_input("Please select a fruit you would like to remove from the list: ")
    
    while not(remove_fruit in my_fruit_list):
        print("That fruit is not in the list")
        remove_fruit = raw_input("Please select a fruit you would like to remove from the list: ")

    while remove_fruit in my_fruit_list:
            my_fruit_list.pop(my_fruit_list.index(remove_fruit))

    print(my_fruit_list)

def action_three():
    pass

def action_four():
    pass

#********************* TEST CODE ************************#
if __name__ == '__main__':
   #this_list = action_one()
   this_list = ['Strawberries', 'Apriocts', 'Apples', 'Pears', 'Oranges', 'Peaches', 'Cherries']
   action_two(this_list)