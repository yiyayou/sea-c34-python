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
