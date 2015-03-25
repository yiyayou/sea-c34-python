"""JosephO'Malley"""
"""Session 3 task6"""

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print fruit_list
new_fruit = raw_input("What fruit would you like to add?")
fruit_list.append(new_fruit)
print fruit_list
number = int(raw_input("Please provide a number between 0 and 4"))
print ("Your number is %s and the corresponding fruit is %s." % (number, fruit_list[number]))
fruit_list = ["Mango"] + fruit_list
print fruit_list
fruit_list.insert(0, "Kiwi")
print fruit_list
for fruits in fruit_list:
    if fruits[0] == "P":
        print fruits



