user_input = input("Enter a string: ")
"""
Have not been able to make the exceptions occur
"""


def string_error(n):
    """ Can I return an error if the value given to me is a number but I want \
    a string?

    Arg(n): User Input.
    Return: An error if given a number
    """
    try:
        n == str
    except TypeError:
        print("Input must be a string, sorreeeeeee")

string_error(user_input)


def file_opener():
    """ Can I write an exeption statement that works? I don't understand how \
    to use them yet.
    """
    try:
        open("gone.txt", "wb")
    except IOError:
        print("Couldn't open gone.text")

file_opener()
