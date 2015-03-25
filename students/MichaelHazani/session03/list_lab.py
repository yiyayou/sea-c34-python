#!/usr/bin/env python

fruitlist = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruitlist)


newfruit = raw_input(u'Please add a fruit: ')
fruitlist.append(newfruit)
print(fruitlist)
fruitnum = int(raw_input(u'Enter fruit number: '))
print(u'Fruit number %d is ' % fruitnum + fruitlist[fruitnum - 1])
firstfruitplus = raw_input(u"Now add a fruit to the beginning of the list: ")
fruitlist = [firstfruitplus] + fruitlist
print fruitlist
firstfruitinsert = raw_input(u"That was fun! Let's try that again: ")
fruitlist.insert(0, firstfruitinsert)
print fruitlist

pthere = False
for pword in fruitlist:
    if pword[0] == "P":
        print ("%s begins with P!" % pword)
        pthere = True
if not pthere:
    print (u"Alas! No fruit in this begins with P!")


# For the next step I take it you mean a brand new list
# rather than keep working with this one
# but the instructions are ambiguous at best...
fruitlist = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruitlist)
fruitlist.pop()
print(fruitlist)
fruitpop = raw_input(u"Which fruit should go? ")
fruitlist.remove(fruitpop)

# Didn't understand the bonus question; I'll ask in class
# also you didn't ask to print list again? I'll just assume you wanted it:
print(fruitlist)

# Again, for the next step I take it you mean a brand new list
# rather than keep working with this one
# but the instructions are ambiguous at best...
fruitlist = ["Apples", "Pears", "Oranges", "Peaches"]
newfruitlist = []
for x in fruitlist:
    likefruit = raw_input(u"Do you like %s ? " % x.lower())
    if likefruit != "no" and likefruit != "yes":
        likefruit = raw_input(u"please answer yes or no ")
    if likefruit != "no":
        newfruitlist.append(x)
print(newfruitlist)

# Again, for the next step I take it you mean a brand new list
# rather than keep working with this one
# but the instructions are ambiguous at best...

fruitlist = ["Apples", "Pears", "Oranges", "Peaches"]
newfruitlist = []
for x in fruitlist:
    newfruitlist.append(x[::-1])
fruitlist.pop()
print(fruitlist)
print(newfruitlist)
# The instructions weren't clear on whether I should also pop also the new list
