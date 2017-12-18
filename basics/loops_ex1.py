#!/usr/bin/python3

# prints 0 to 4
for i in range(5):
    print("for i in range(5):", i)

# prints 1 to 4
for i in range(1, 5):
    print("for i in range(1, 5):", i)

# prints each individual character
for c in "Hello":
    print("Parse Hello", c)

# prints each item in list
for item in ['item1', 'item2', 'item3']:
    print("items list:", item)

# prints each tuple
for tup in ('tuple1', 'tuple2', 'tuple3'):
    print("tuples:", tup)

# print each dictionary entry
entries = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3'}
for entry in entries:
    print("Dictionary key: {};  value: {}".format(entry, entries[entry]))

input("Enter to continue")

# print each line in file
f = open("loops_ex1.py")
for line in f:
    print(line, end="")
f.close()

# print string with 1 less char each time
s = "Hello"
while len(s) > 0:
    print(s)
    s = s[:-1]
