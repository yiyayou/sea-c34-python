# task14 dict_comp.py

food_prefs = {"name": u"Yi",
              u"city": u"Seattle",
              u"cake": u"rum",
              u"fruit": u"orange",
              u"salad": u"chop",
              u"pasta": u"angel hair"}

# 1. Print the dict by passing it to a string format method

p = ("{name} is from {city}, and she likes {cake} cake, {fruit} fruit,"
     "{salad} salad, and {pasta} pasta")
print p.format(**food_prefs)

# 2. build a dict of numbers from zero to fifteen & the hexadecimal equivalent

dict_q2 = {}

numbers = range(16)

hexadecimal = [hex(i) for i in numbers]

for i, j in zip(numbers, hexadecimal):
    dict_q2[i] = j

print dict_q2

# 3.Do the previous entirely with a dict comprehension

dict_q3 = {i: hex(i) for i in range(16)}

print dict_q3

# 4. Make a dictionary using the same keys as food_prefs but with the number\
# of as in each value.

dict_q4 = {i: food_prefs[i].count(u'a') for i in food_prefs}

print dict_q4
# 5.

# 5a
s2 = {n for n in range(21) if (n % 2) == 0}
s3 = {n for n in range(21) if (n % 3) == 0}
s4 = {n for n in range(21) if (n % 4) == 0}

print s2
print s3
print s4

# 5b
s2, s3, s4 = [{i for i in range(21) if not i % j} for j in range(2, 5)]

print s2
print s3
print s4
