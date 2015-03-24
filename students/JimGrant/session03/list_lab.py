#!/usr/bin/env python


def print_series_header(series_num):
    """Prints a header for each list lab series output, to aid in reading."""
    print(u"-------------------")
    print(u"List Lab - Series {}".format(series_num))
    print(u"-------------------")


def print_fruitlist(series_num, step_num, fruitlist):
    """Prints the current state of the fruit list as a formatted string with the series and step of the lab involved."""
    print(u"{}.{} - Current Fruit List: {}".format(series_num, step_num, fruitlist))


def series1():
    print_series_header(1)
    fruitlist = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
    print_fruitlist(1, 1, fruitlist)

    fruitlist.append(raw_input(u"Enter another fruit: ").capitalize())
    print_fruitlist(1, 2, fruitlist)

    input_number = int(raw_input(u"Enter a number: "))
    chosen_fruit = fruitlist[input_number - 1] if 1 <= input_number <= len(fruitlist) else u"non-existent"

    print(u"1.3 - The number %i fruit in the list is %s." % (input_number, chosen_fruit))

    fruitlist = [u"Papaya"] + fruitlist
    print_fruitlist(1, 4, fruitlist)

    fruitlist.insert(0, u"Watermelon")
    print_fruitlist(1, 5, fruitlist)

    for fruit in fruitlist:
        if fruit.startswith(u"P"):
            print(u"1.6 - Fruits that start with P: {}".format(fruit))

    return fruitlist


def series2(fruitlist):
    pass


def series3(fruitlist):
    pass


def series4(fruitlist):
    pass


if __name__ == "__main__":
    fruitlist = series1()
    series2(fruitlist[:])
    series3(fruitlist[:])
    series4(fruitlist[:])