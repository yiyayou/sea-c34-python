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


nums = []
for i in range(1, 16):
        nums.append(i)
