from __future__ import print_function


def question01():
    """Can else and finally both get called in the same execution?"""

    print("Question 1: Do else and finally both get called in the same execution?")
    try:
        text = "This operation is just fine "
    except TypeError:
        text += " except that all the laws of logic and reason have broken down "
    else:
        print("{}so the else block was executed".format(text), end=" ")
    finally:
        print("and the finally block was executed.")



def question02():
    """Does anything after the raise statement get executed when handling an error?"""

    print("Question 2: Does anything after the raise statement get executed when handling an error?")
    try:
        nope = 1 / 0
        print(nope)
    except ZeroDivisionError:
        print("This is before the raise statement.")
        raise
        print("This is after the raise statement.")
    finally:
        print("If you didn't see two prints above this one, the answer is no.")


if __name__ == "__main__":
    question01()
    print("")
    question02()
