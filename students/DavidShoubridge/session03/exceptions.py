user_input = raw_input("Enter a number: ")
user_input = int(user_input)


def string_error(n):
    """ Can I return an error if the value given to me is a number but I want \
    a string?

    Arg(n): User Input.
    Return: An error if given a number
    """
    try:
        n == str(n)
    except TypeError:
        print("Input must be a string, sorreeeeeee")

string_error(user_input)
