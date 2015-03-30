# 1

people = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print people

# Delete the key "cake" from the dictionary
people.pop("cake")

print "\n"
print people

# Add an entry for “fruit” with “Mango” and display the dictionary
people["fruit"] = "Mango"

# Display the dictionary keys.
print "\n"
print "Keys in the dictionary People:"
for key in people:
    print key

# Display the dictionary values.
print "\n"
print "Values in the dictionary People:"
for value in people:
    print people[value]

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print "\n"
desired_key = "cake"
print("Is \"%s\" a key in the dictionary?: " % desired_key)
print desired_key in people

# Display whether or not “Mango” is a value in the dictionary.
print "\n"
desired_value = "Mango"
print("Is \"%s\" a value in the dictionary?: " % desired_value)
print desired_value in people.values()


# 2

# Using the dict constructor and zip, build a dictionary of numbers from zero
# to fifteen and the hexadecimal equivalent (string is fine)
nums_dict = {}
nums_list = []
hexadec_list = []
total_numbers = 15

for i in range(total_numbers + 1):
    nums_list.append(i)
    hexadec_list.append(hex(i))

nums_dict = dict(zip(nums_list, hexadec_list))

"""
# Method 2:
nums_dict = {}
for i in range(16):
    nums_dict[i] = hex(i)

print nums_dict
"""
