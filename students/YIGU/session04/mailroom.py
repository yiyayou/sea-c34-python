# This python script helps mailroom to print Thank you letter to donor and
# create reports.

# Assuming donor names are unique because task7 asked "If the user types
# a name not in the list, add that name to the data structure and use it."
from collections import OrderedDict

# donner data
donor_his = {}


def safe_input(note):
    """This function catch excepitions from raw_input function and return\
     None"""
    try:
        i = raw_input(note)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return i


def send_thank_you_letters():
    """This function let you input donation amonut to donor history and \
    format a thank you letter with donor's name and donation amount."""
    while True:
        styl_prompt = safe_input(u"Please enter donor's Full Name to enter \
        donation amount and print thank you letter; enter LIST to list out \
        all donors in donor hisotry; enter RETURN to return to the original \
        prompt-->")
        if styl_prompt.upper == u'RETURN':
            break
        elif styl_prompt.upper == u'LIST':
            print donor_his.keys()
        elif styl_prompt.upper not in donor_his:
            print u'Adding %s to donor list\n' % styl_prompt.upper
            donor_his[styl_prompt.upper] = []
        else:
            add_donation(styl_prompt)


def add_donation(styl_prompt):
    """This function is use by send_thank_you_letters to add donation to \
    donor_his. Function ask for donors_amount; make sure input is \
    int/float"""
    while True:
        add_d_prompt = safe_input(u"Please enter donation amount; enter \
        RETURN to return to upper level-->")
        if add_d_prompt == u'RETURN':
            break
        elif add_d_prompt is not (int, float):
            print "I don't know what is %s. Please enter a number.\n"\
             % add_d_prompt
        elif add_d_prompt <= 0:
            print "Donation should be greater than 0. Please try again.\n"
        else:
            # store donation data in donor history
            donor_his[styl_prompt].append(add_d_prompt)
            print_thank_you_letter()
            break


def print_thank_you_letter(styl_prompt):
    """This function print thank you letters"""
    "Dear {name},\n Thank you for your generous donation of {amonut}.\n\
     MR".format(**{'name': styl_prompt, 'amonut': donor_his[-1]})


def create_report():
    """This function create report out of donor hisotry and sort by\
     total of donation amount"""
    print OrderedDict(sorted(donor_his.items(), key=lambda t: t[1][1])[::-1])


if __name__ == '__main__':
    """This function work as the main startup menu"""
    while True:
        main_prompt = safe_input(u'Please enter 1 to send a thank you email;\
         enter 2 to create a report; EXIT to exit the progarm-->')
        if main_prompt.upper == u'EXIT':
            break
        elif main_prompt == 1:
            send_thank_you_letters()
        elif main_prompt == 2:
            create_report()
        else:
            print "I don't know what is %s. Please try again.\n" % main_prompt
