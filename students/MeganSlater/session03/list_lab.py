#!/usr/bin/env python

# section 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
userfruit = raw_input("What is another fruit? ")
fruits.append(userfruit)
print(fruits)
usernumber = int(raw_input("Give a number between 1 and 4 "))
print(fruits[usernumber - 1])
fruits = ["Grapes"] + fruits
print(fruits)
fruits.insert(0, "Tomato")
print(fruits)
for fruit in fruits:
    if fruit[0] == "P":
        print fruit

# section 2
print(fruits)
fruits.pop()
print(fruits)
deletefruit = raw_input("Which fruit do you want to delete? ")
for fruit in fruits:
    if fruit == deletefruit:
        fruits.remove(fruit)

# section 3
count = 0
userlike = ""


def goodfruits(fruit):
    userlike = raw_input("Do you like " + fruit + "? (yes/no) ").lower()
    if userlike == "no":
        fruits.remove(fruit)
    elif userlike != 'no' and userlike != 'yes':
        print("That was not yes or no.  Try again.")
        goodfruits(fruit)
for fruit in fruits:
        goodfruits(fruit)
print(fruits)

# section 4
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
backwardsfruits = fruits[:]
bfruit = ""
count = 0
for fruit in backwardsfruits:
    for letter in fruit:
        bfruit = letter + bfruit
    backwardsfruits[count] = bfruit
    bfruit = ""
    count += 1
fruits.pop()
print(fruits)
print(backwardsfruits)
