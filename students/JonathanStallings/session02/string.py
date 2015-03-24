def highest_ordinal(string):
    """
    Return the highest ordinal in a given string.

    Args:
        string: the string to be checked.
    Returns:
        the highest ordinal value in the string.
    """
    msg = u"The max was {maxOrd} and value was {maxValue}." \
        .format(maxOrd=max(string), maxValue=ord(max(string)))
    print(msg)


# highest_ordinal(u"The quick brown fox leaped!")
# result: The max was x and the value was 120.

def lowercase_number(num):
    """
    Attempt to lowercase a number to see what happens.

    Args:
        num: the number to be lowercased
    Returns:
        the result.
    """
    try:
        print num.lower()
    except:
        print u"Use of lowercase method on number raises exception."

# lowercase_number(16)
# result: Using a lowercase (string) method on number throws an error.


def input_type():
    """
    Check type of user input.

    Returns:
        the type of user input.
    """
    user_input = raw_input()
    print type(user_input)


# input_type()
# result: raw_input always returns a string.
