#!/usr/local/bin/env python

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

user1 = raw_input("What fruit would you like to add to the list? ")
fruit.append(user1)
print(fruit)

user2 = int(raw_input("What index would you like to call from the fruit list? "))
print(fruit[user2 - 1])

fruit = ["Guava"] + fruit
print(fruit)

fruit.insert(0, "Tomatoes")
print(fruit)

for item in fruit:
    if item[0] is "P":
        print item

print(fruit)

del fruit[-1]
print(fruit)

user3 = str(raw_input("What fruit would you like to remove? "))
while user3 not in fruit:
    user3 = str(raw_input("Please select a fruit from the list. "))
else:
    while user3 in fruit:
        fruit.remove(user3)
    print(fruit)
