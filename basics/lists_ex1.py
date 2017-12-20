#!/usr/bin/python3

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

# print a range of elements with slice
print(food[0:4])     # print the first 4 elements
print(food[0:-1])    # print all but the last element
print(food[-1])      # print the last element

# concatenate lists, creates a new list

shoppinglist = food + items
print(shoppinglist)

# sort the list
shoppinglist.sort()
print("sorted:", shoppinglist)

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

# this appends a nested list within a list
empty.append(['with', 'nested', 'list'] )
print(empty)        # prints all list items, including nested list
print(empty[3])     # prints the nested list only
print(empty[3][1])  # prints an individual item from the nested list

# insert to a specific positions in list
empty.insert(1, "new pos 1")
print(empty)

# update the element just added
empty[1] = "very"
print(empty)

# remove what was just added & updated
empty.remove("very")
# del(empty[1]) would remove the same item
print(empty)

# pop the last item from the list (in this case a nested list)
x = empty.pop()
print(x, "has been popped from", empty)

# clear the list completely
empty.clear()
print(empty, "Empty again")

# using split to go from string to list
fromsplit = "item1, item2, item3".split(",")
print(fromsplit)

# join elements into a string separated by the specified delimeter
print(", ".join(food))
print("\n".join(food[0:2]))  # print first 2 on their own line

# using for loop method instead of join. This would be more
# complicated if single line comma delimeted used because of
# trailing delimiter, but newline delimeted here not too bad
for item in food[2:]:  # print the remaining item using for
    print(item)
