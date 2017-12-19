#!/usr/bin/python3

from decimal import *
import locale

# print the current context setting such as rounding and precision
print(getcontext())
# change the precision from the default 28 to 53
getcontext().prec=53
print("After changing precision:")
print(getcontext())
print("")

# setting locale will print thousands separator (us: comma) and local 
# decimal point when used with 'n' format specifier in print function
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
# note: locale.setlocale(locale.LC_ALL, "") will set it to system default

# note the use of string conversion, if this was converted from a float
# it would inherit the floats inprecision, you should either convert from
# a string or an integer, never use a float (including a float literal).
dec1 = Decimal('12345678901234567890123456789012345678901234567890.99')
dec2 = Decimal('0.02')
dec3 = dec1 + dec2
print("Decimals with precision=53 {:n} + {:n} = {:n}".format(dec1, dec2, dec3))
dec1 = Decimal('99999999999999999999999999999999999999999999999999.99')
dec2 = Decimal('0.02')
dec3 = dec1 + dec2
print("Decimals with precision=53 {:n} + {:n} = {:n}".format(dec1, dec2, dec3))
