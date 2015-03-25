"""Can I look up keys in dictionaries by their values?"""

d = {"key1": 3, "key2": 5, "key3": 5}
# loop through the dictionary to find the key(s) for stated value
for key, value in d.iteritems():
    if value == 5:
        print key

"""Can I unfreeze a set?"""
frozen = frozenset([1, 2, 3, 4])
# create new set
unfreeze = set("")
# add items from frozen set to set
for item in frozen:
    unfreeze.add(item)
print unfreeze


"""What do all those set operations do?"""
newset = set("Cheese is Awesome!")
other = set("Cheese")
newset.isdisjoint(other)  # check if two sets have no elements in common
newset.issubset(other)  # check if one set is subset of the other
newset.union(other)  # puts the sets together
newset.intersection(other)  # returns all values the sets have in common
newset.difference(other)  # returns all values the sets do not have in common
newset.symmetric_difference(other)  # returns values that exist in only one set

"""Can I change a set into a list?"""
newset = set(["Apple", "Pear", "Orange", "Banana"])
# create new list
newlist = []
# add all items in set to new list
for fruit in newset:
    newlist.append(fruit)
