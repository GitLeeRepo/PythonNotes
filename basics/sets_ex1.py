#!/usr/bin/python3

import sys

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
set2 = set([1, 3, 5, 7, 9])
set3 = set([2, 4, 6, 8, 10])
dupeslist = [1, 2, 5, 2, 3, 1]
nodupes = set(dupeslist)

# the sets to compare
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

# union operations
print("union set1 | set2:", set1 | set2)
print("union set1 | set3:", set2 | set3)
print("union set2 | set3:", set2 | set3)

# intersection operations
print("intersection set1 & set2:", set1 & set2)
print("intersection set1 & set3:", set1 & set3)
print("intersection set2 & set3:", set2 & set3)

# difference operations
print("difference set1 - set2:", set1 - set2)
print("difference set1 - set3:", set1 - set3)
print("difference set2 - set3:", set2 - set3)

# symetric difference operations
print("symetric difference set1 ^ set2", set1 ^ set2)
print("symetric difference set1 ^ set3", set1 ^ set3)
print("symetric difference set2 ^ set3", set2 ^ set3)

# duplicates not allowed and are automatically removed
print("duplicates automatically removed:", nodupes, "from", dupeslist)

nodupes.add(4)
nodupes.update([6, 7, 8])
nodupes.remove(1)
print("nodupes after adding (4), updating [6, 7, 8], and removing (1):", nodupes)
