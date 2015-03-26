#!/usr/bin/env python

# section 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
userfruit = raw_input("What is another fruit? ")
fruits.append(userfruit)
print(fruits)
usernumber = int(raw_input("Give a number between 1 and 4 "))
print(usernumber)
print(fruits[usernumber - 1])  # subtract one b/c user starts at one
fruits = ["Grapes"] + fruits
print(fruits)
fruits.insert(0, "Tomatos")
print(fruits)
for fruit in fruits:  # Check the first letter of every fruit to see if it's P
    if fruit[0] == "P":
        print fruit
seriesonefruit = fruits[:]  # Make a copy of this fruits list for further use

# section 2
sectiontwofruits = seriesonefruit[:]  # Make a copy for this section
print(sectiontwofruits)
sectiontwofruits.pop()
print(sectiontwofruits)
deletefruit = raw_input("Which fruit do you want to delete? ")
for fruit in sectiontwofruits:  # checks every fruit against user input
    if fruit == deletefruit:
        sectiontwofruits.remove(fruit)

# section 3
count = 0
userlike = ""
sectionthreefruits = seriesonefruit[:]  # create a copy for this section
for fruit in sectionthreefruits:  # move every item in this list to lowercase
    fruit = fruit.lower()
unlikedfruits = []

# recursive function checks for valid user input


def goodfruits(fruit):
    userlike = raw_input("Do you like " + fruit + "? (yes/no) ").lower()
    if userlike == "no":
        unlikedfruits = unlikedfruits + [fruit]
    elif userlike != 'no' and userlike != 'yes':
        print("That was not yes or no.  Try again.")
        goodfruits(fruit)
for fruit in sectionthreefruits:
        goodfruits(fruit)
print(unlikedfruits.difference(sectionthreefruits))

# section 4
sectionfourfruits = seriesonefruit[:]
backwardsfruits = sectionfourfruits[:]
bfruit = ""
count = 0
for fruit in backwardsfruits:  # re-spells every fruit backwards
    for letter in fruit:
        bfruit = letter + bfruit
    backwardsfruits[count] = bfruit
    bfruit = ""
    count += 1
sectionfourfruits.pop()
print(sectionfourfruits)
print(backwardsfruits)
