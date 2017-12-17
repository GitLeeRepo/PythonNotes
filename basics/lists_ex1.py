#!/usr/bin/python3

import sys

food = [ 'cereal', 'cheese', 'nuts', 'milk', 'corn' ]
items = [ 'paper', 'soap', 'cleaner' ]
mixed = [ 'one', 1, 'two', 2, 'three', 3 ]
empty = []

# print all elements
print(food)
print(food[:])
print(food[0:])
print(food[0:9])

# print one element
print(food[3], "and", food[0])

# print a range of elements
print(food[0:4])     # print the first 4 elements
print(food[0:-1])    # print all but the last element
print(food[4:])      # print [ 'corn' ]

# concatenate lists, creates a new list

shoppinglist = food + items
print(shoppinglist)

# mixed strings and numbers
print(mixed)

# list pointer vs list copy
strptr = mixed     # both point to the same list
strcpy = mixed[:]  # two different copies of the list
mixed[0] = "uno"   # change the original
print(strptr)      # pointer version has the change
print(strcpy)      # the copied version does not have the change

# append to an empty list (works with any list)
empty.append('not')
empty.append('empty')
empty.append('anymore')
print(empty)

# using split
fromsplit = "item1, item2, item3".split(",")
print(fromsplit)

# this appends a nested list within a list
empty.append(fromsplit)
print(empty)        # prints all list items, including nested list
print(empty[3])     # prints the nested list only
print(empty[3][1])  # prints an individual item from the nested list

