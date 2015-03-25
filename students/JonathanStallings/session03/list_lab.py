from __future__ import print_function


def display(l):
    """
    Display a list as a formatted string.

    Args:
        l: the list to be displayed.
    """
    list_str = ', '.join(l)
    print('\n' + list_str)


if __name__ == '__main__':
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    msg = ""
    display(fruits)

    msg = u'\nPlease enter an additional type of fruit.\n\n>  '
    fruits.append(raw_input(msg).title())
    display(fruits)

    msg = u'\nPlease enter a number between 1 and {length}.\n\n>  ' \
        .format(length=len(fruits))
    num = raw_input(msg)
    print(num + ". " + fruits[int(num) - 1])

    fruits = ['Blueberries'] + fruits
    display(fruits)

    fruits.insert(0, "Snozberries")
    display(fruits)

    p_fruits = []
    for fruit in fruits:
        if fruit[0] == 'P':
            p_fruits.append(fruit)
    display(p_fruits)

    display(fruits)
    fruits.pop()
    display(fruits)

    msg = u'\nPlease enter a fruit to delete.\n\n>  '
    response = raw_input(msg).title()
    for fruit in fruits:
        if fruit == response:
            fruits.remove(fruit)

    for fruit in fruits[:]:
        msg = u'\nDo you like {fruit}? ([Y]es/[n]o):\n\n' \
            .format(fruit=fruit.lower())
        while True:
            response = raw_input(msg).lower()
            if response == 'yes' or response == 'y':
                break
            elif response == 'no' or response == 'n':
                fruits.remove(fruit)
                break
    display(fruits)


