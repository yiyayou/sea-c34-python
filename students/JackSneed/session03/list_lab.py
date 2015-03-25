#!/usr/bin/env python


def fruit_list():

    #List Lab part 1

    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit)

    new_fruit = raw_input("Name a new fruit: ")
    fruit.append(new_fruit)
    print(fruit)

    user_pick = int(raw_input("Pick a number 1-5: "))
    fruit_chosen = fruit[user_pick - 1]
    print("The number %i fruit on the index is %s." % (user_pick, fruit_chosen))

    fruit = ["Plums"] + fruit
    print(fruit)
    fruit.insert(0, "Persimmons")
    print(fruit)

    for item in fruit:
        if item.startswith("P"):
            print("This fruit starts with P: %s" % (item))

    #List Lab part 2

    print(fruit)
    del fruit[-1]
    print(fruit)

    user_pick2 = (raw_input("Choose a fruit from the index to remove: "))
    fruit.remove(user_pick2)
    print(fruit)

    #List Lab part 3

    for item in fruit[:]:
        answer = ""
        while answer != "yes" and answer != "no":
            answer = raw_input("Do you like %s? (Enter yes or no): " % (item.lower()))

        if answer == "no":
            fruit.remove(item)

    print(fruit)

    #List Lab part 4

    newest_fruit = fruit[:]
    newest_fruit = [item[::-1] for item in fruit]
    del fruit[-1]
    print(fruit)
    print(newest_fruit)



fruit_list()
