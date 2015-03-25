#!/usr/bin/env python

# section 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
userfruit = raw_input("What is another fruit? ")
fruits.append(userfruit)
print(fruits)
usernumber = int(raw_input("Give a number between 1 and 4 "))
print(usernumber)
print(fruits[usernumber - 1])
fruits = ["Grapes"] + fruits
print(fruits)
fruits.insert(0, "Tomatos")
print(fruits)
for fruit in fruits:
    if fruit[0] == "P":
        print fruit
seriesonefruit = fruits[:]

# section 2
sectiontwofruits = seriesonefruit[:]
print(sectiontwofruits)
sectiontwofruits.pop()
print(sectiontwofruits)
deletefruit = raw_input("Which fruit do you want to delete? ")
for fruit in sectiontwofruits:
    if fruit == deletefruit:
        sectiontwofruits.remove(fruit)

# section 3
count = 0
userlike = ""
sectionthreefruits = seriesonefruit[:]
for fruit in sectionthreefruits:
    fruit = fruit.lower()


def goodfruits(fruit):
    userlike = raw_input("Do you like " + fruit + "? (yes/no) ").lower()
    if userlike == "no":
        sectionthreefruits.remove(fruit)
    elif userlike != 'no' and userlike != 'yes':
        print("That was not yes or no.  Try again.")
        goodfruits(fruit)
for fruit in sectionthreefruits:
        goodfruits(fruit)
print(sectionthreefruits)

# section 4
sectionfourfruits = seriesonefruit[:]
backwardsfruits = sectionfourfruits[:]
bfruit = ""
count = 0
for fruit in backwardsfruits:
    for letter in fruit:
        bfruit = letter + bfruit
    backwardsfruits[count] = bfruit
    bfruit = ""
    count += 1
sectionfourfruits.pop()
print(sectionfourfruits)
print(backwardsfruits)
