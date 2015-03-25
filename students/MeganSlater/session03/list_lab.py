#!/usr/bin/env python

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

