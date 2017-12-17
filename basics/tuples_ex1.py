#!/usr/bin/python3

import sys

person = ( 'Bill', 'Jones', '(999)999-9999' )
single = ( 'justone', )  # note the trailing comma

# assign to individual variables
first_name, last_name, phone = person

print(person)
print(first_name, last_name, phone)

print(single) # tuple with one element
