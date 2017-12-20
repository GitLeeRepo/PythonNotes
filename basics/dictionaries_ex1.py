#!/usr/bin/python3

# start with an empty dictionary

d = {}

# creates the following key value pairs
# Keys      Values
# a         'alpha'
# b         'beta'
# g         'gamma'
# o         'omega'

d['a'] = 'alpha'
d['b'] = 'beta'
d['g'] = 'gamma'
d['o'] = 'omega'

# prints in random order
print("random order")
print("{:4}   {:6}".format("key", "value"))
for key in d:
    print("{:4} = {:6}".format(key, d[key]))

# to access a specific value in a dictionary, simply index it with the key
print("From", d['a'], "to", d['o'], "i.e., sorted")

# to print in sorted order
print("{:4}   {:6}".format("key", "value"))
for key in sorted(d.keys()):
    print("{:4} = {:6}".format(key, d[key]))

# indexing a key that doesn't exist will throw an error.  To get around
# this you can use the get() method instead.
print("d.get('x') gets:", d.get('x'))
print("while d.get('g') gets:", d.get('g'))

# to test if an item is in a dictionary use 'in'
print("'x' in d:", 'x' in d)
print("'b' in d:", 'b' in d)

# to retrieve a list of keys and values separately
print("d.keys():", d.keys())
print("d.values():", d.values())

# convert the key/value pairs to a list of tuples, print random and sorted
print("d.items():", d.items())
print("d.items() sorted:", sorted(d.items()))

# this time initialize a dictionary to begin with
items = {
    "item1" : 5.53,
    "item2" : 9.99,
    "item3" : 3.99,
    "item4" : 4.99,
    "item5" : 2.21
}

# print the sorted dictionary 
for item in sorted(items.keys()):
    print(item, items[item])

# a couple of ways to add to dictionary
items["item6"] = 7.57
items.update({"item7" : 3.33})

print("new item6 found?", 'item6' in items)
print("new item7 found?", 'item7' in items)

# delete an entry
del items["item2"]
print("deleted item2.  Found?", "item2" in items)

# print the full list again
print("Now with two new items, and one removed item:")
for item in sorted(items.keys()):
    print(item, items[item])
