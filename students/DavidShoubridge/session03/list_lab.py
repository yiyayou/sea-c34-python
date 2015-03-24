#!/usr/bin/env python

my_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(my_list)


def user_input():
    fruit_input = raw_input("Give me a fruit to add to our list:")

    my_list.append(fruit_input)

    print(my_list)

    number_input = raw_input("Enter a number:")

    print(number_input)

    number_input = int(number_input)

    print(my_list[(number_input - 1)])

user_input()

# my_list[0] = "Bananas"

# print my_list

my_list.insert(0, "Pineapple")

print(my_list)

for fruit in my_list:
    if fruit[0] == "P":
        print fruit
