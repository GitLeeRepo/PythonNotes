#!/usr/bin/python3

# imports
import sys

items = {
    "item1" : 5.53,
    "item2" : 9.99,
    "item3" : 3.99,
    "item4" : 4.99,
    "item5" : 2.21
}


for item in items:
    print(item, items[item])


# a couple of ways to add to dictonary
items["item6"] = 7.57
items.update({"item7" : 3.33})

print("added new items")
if "item6" in items:
    print("found new: item6", items["item6"])
if "item7" in items:
    print("found new: item7", items["item7"])

# delete an entry
del items["item2"]
print("deleted item")
if "item2" not in items:
    print("item2 not found")

# print the full list again
print("Now with two new items, and one removed item:")
for item in items:
    print(item, items[item])
