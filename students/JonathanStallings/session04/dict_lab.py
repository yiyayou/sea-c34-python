from __future__ import print_function

# Section 1
a = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print(a)

del a["cake"]

print(a)

a["fruit"] = "Mango"

print(a.keys())
print(a.values())
print("cake" in a.keys())  # OR "cake" in d
print("Mango" in a.values())

# Section 2
key_num = []
val_hex = []
b = {}

for x in range(16):
    key_num.append(x)
    val_hex.append(hex(x))

for key, val in zip(key_num, val_hex):
    b[key] = val

print(b)

# Section 3
# c = a.copy()
# print(c)
# c = dict((k, v) for k, v in a.items())
# print(c)
# c = dict((k, v) for k in a.keys() for v in a.values())
# print(c)
c = {k: v.count('a') for k, v in a.items()}
print(c)
