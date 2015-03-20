def question01():
    """Answers the question: what happens if the end of my slice is greater than the beginning?"""
    print("Question 1: What happens if the end of my slice is greater than the beginning?")

    testlist = [1, 2, 3]
    upper_bound = len(testlist) - 1
    print("{} sliced from 0 to {} is: {}".format(testlist, upper_bound, testlist[0:upper_bound]))
    print("However, {} sliced from {} to 0 is: {}".format(testlist, upper_bound, testlist[upper_bound:0]))


def question02():
    pass


def question03():
    pass


if __name__ == "__main__":
    question01()
    question02()
    question03()
