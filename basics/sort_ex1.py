#!/usr/bin/python3

# Examples of  using the sorted() function

# example function to be used as key by sorted function
def sortbylen(x):
    return len(x)

# List to sort, first alphabetically, then by length
a = [ 'ccc', 'aaaa', 'd', 'bb']

# Orig list
print(a)

# Sorted ascending alphabetic
print(sorted(a))

# sorted decending alphabetc
print(sorted(a, reverse=True))

# use the len() function to sort by length
print(sorted(a, key=len))

# use my own custom sort key function
print(sorted(a, key=sortbylen))

# use my custom sort key function reversed
print(sorted(a, key=sortbylen, reverse=True))


# Orig list still unchanged
print(a)

# but the sort() method will change the underlying list
# unlike the sorted function call which creates a new one
a.sort()
print(a)

