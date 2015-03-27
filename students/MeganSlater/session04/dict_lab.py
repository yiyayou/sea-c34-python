# part 1
dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print dict
del dict["cake"]
print dict
dict.update({"fruit": "Mango"})
print dict
print dict.keys()
print dict.values()
print 'cake' in dict
for key, value in dict.iteritems():
    if value == "Mango":
        print True

# part 2
numberdict = {}
nums = []
for i in range(1, 16):
        nums.append(i)
hex = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1A", "1B", "1C", "1D", "1E"]
for i, j in zip(nums, hex):
    numberdict.update({i: j})
print numberdict

# part 3
a_dict = {}
for key, value in dict.iteritems():
    a_dict.update({key: value.count('a')})

# part 4
s2 = set(filter(lambda x: x % 2 == 0, range(21)))
s3 = set(filter(lambda x: x % 3 == 0, range(21)))
s4 = set(filter(lambda x: x % 4 == 0, range(21)))
print s2
print s3
print s4
print s3.issubset(s2)
print s4.issubset(s2)

# part5
python = set(['P', 'y', 't', 'h', 'o', 'n'])
python.add('i')
marathon = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print python.union(marathon)
print python.intersection(marathon)
