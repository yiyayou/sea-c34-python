#! /usr/bin/env python

# series 1 (first four series of actions)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print "\n"
print fruit_list
print "\n"

while True:
    add_fruit = raw_input("Add another fruit to the list: ")
    add_fruit = add_fruit.capitalize()
    check_add_fruit = add_fruit in fruit_list
    if check_add_fruit is True:
        print("Sorry, %s is on the list already." % add_fruit)
        print "\n"
    else:
        break
fruit_list.append(add_fruit)
print fruit_list
print "\n"

while True:
    user_num = int(raw_input("Pick a number 1-5: "))
    if user_num >= 1 and user_num <= 5:
        print("%i) %s" % (user_num, fruit_list[user_num - 1]))
        print "\n"
        break
    else:
        print("Oops! You entered %i." % user_num)
        print "\n"

fruit_list = ["Durian"] + fruit_list
print fruit_list
print "\n"

fruit_list.insert(0, "Lychee")
print fruit_list
print "\n"

counter = 0
check_letter = "P"
print("Fruits that start with the letter \"%s\": " % check_letter)
for fruit in fruit_list:
    if fruit[0] == "P":
        counter += 1
        print("%i) %s" % (counter, fruit))
print "\n"

# next four steps

print fruit_list
print "\n"
fruit_list.pop()
print fruit_list
while True:
    remove_fruit = raw_input("Which fruit would you like to have removed?: ")
    remove_fruit = remove_fruit.capitalize()
    check_fruit = remove_fruit in fruit_list
    if check_fruit is False:
        print("Sorry, %s is not on the list. \n" % remove_fruit)
    else:
        fruit_list.remove(remove_fruit)
        break
print fruit_list
