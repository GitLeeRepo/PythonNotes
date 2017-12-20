#!/usr/bin/python3

# Original from "Programming in Python 3: A Complete Introduction to the Python Language"
#               by Mark Summerfield
#
# Modified by TK: added detail lines to output, formatting and comments
#
# Demonstrates named tuples, which allows you to refer to the individual elements
# of the tuple by name

import collections

# the named tuple with the individual element names
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

# append to sales using the named Sale tuple
sales = []
sales.append(Sale(432, 921, "2017-12-19", 3, 7.99))
sales.append(Sale(419, 738, "2017-12-20", 3, 19.99))

# print out the detail lines and total using the named elements of the tuple
total = 0
for sale in sales:
    subtotal = sale.quantity * sale.price
    total += subtotal
    print("{:6} {:6} {:12} {:5} {:8} {:8}".format(sale.productid, sale.customerid, \
                                sale.date,  sale.quantity, sale.price, subtotal))
print("Total ${0:43.2f}".format(total))
