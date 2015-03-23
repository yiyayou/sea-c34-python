"""How many words start with 'a' in a sentence?"""


def startA(str):
    str = str.split()
    count = 0
    for i in str:
        firstLetter = i[0]
        if firstLetter.lower() == 'a':
            count += 1
    return count

"""Is a user entered value a number?"""


def isNum(userInput):
    return userInput.isalnum()
isNum(raw_input("Enter a number: "))

"""Can a computer do mad libs?"""


def madLibs():
    verb = raw_input("Enter a verb ending in ing: ")
    noun = raw_input("Enter a plural noun: ")
    adj = raw_input("Enter an adjective: ")
    print('"There are too many %s %s on this %s plane!" he screamed.' % (verb, noun, adj))
madLibs()
