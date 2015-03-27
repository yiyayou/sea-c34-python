donors = {"Megan Slater": []}


def safe_input(x):
    try:
        return raw_input(x)
    except (EOFError, KeyboardInterrupt):
        pass


# define a function that will either send a thank you or create a report
def thankyous():
    """ask user whether to send thank you or create report.  Take action based
    on input
    """
    userprompt = safe_input("Choose Send a Thank You or Create a Report. ")
    userprompt = userprompt.lower()

    if userprompt == "send a thank you":
        donorname = "list"
        while donorname == "list":
            donorname = safe_input("What is the donor's full name? ")
            """if the user doesn't know any names the user will input 'list' and we
            print all the names and let them choose one
            """
            if donorname == "list":
                for name, donation in donors.iteritems():
                    print name
        """If the user enters an unknown name we add that name to the dictionary
            and return to the beginning.
        """
        for name, donation in donors.iteritems():
            if donorname != name:
                donors[donorname] = []
                thankyous()
                """If the donor name is in the dictionary we prompt the user for
                a donated amount and enter it into the dictionary"""
            else:
                amount = ""
# keep asking the user about how much was donated until they enter a number
                while amount.isdigit() == False:
                    amount = safe_input("How much did they donate? ")
                    donors[name] = donation + [amount]
                break

        """Once an amount has been added the user will receive a print
        out of an email for every donor and return to the beginning.
        """
        for name, donation in donors.iteritems():
            print("Thank you " + name + ".")
        thankyous()
"""
# If the user wants a report at the beginning we give them one
    elif userprompt == "Create a Report":
        totaldonated = []
        total = 0
# add up the total donations for each donor and put it in a list
        for name, donation in donors:
            for i in donation:
                total += i
            totaldonated.append(total)
# sort that list highest to lowest
        totaldonated.sort()
        donortotal = 0
# match the list against dictionary entries and print them higest to lowest
        for total in totaldonated:
            for name, donation in donors:
                for i in donation:
                    donortotal += i
                if donortotal == total:
                    print(name, /tab total, /tab length(donations), /tab total/length(donations))
# return to the beginning
        thankyous()
# The user can exit this function from the beginning prompt by typing quit
    elif userprompt == "quit":
        exit()
# If the user enters something unexpected they are asked to try again.
    else:
        print("I'm sorry, I don't understand.  Try again. ")
        thankyous()
"""
thankyous()