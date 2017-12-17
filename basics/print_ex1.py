#!/usr/bin/python3

#################################
# Using the newer .format method
#################################

print("The correct answer is {0:d}".format(42))
#>The correct answer is 42

print("{} {}".format("one", "two"))
#>one two

print("{1} {0}".format("one", "two"))
#>two one

print("{:>10}".format("right")) # right justify within 10 space
#>     right

print("{:10}{:>10}".format("left", "right")) # pad both left and right justifies with 10 (total width 20 chars)
#>left           right

print("{:^10}".format("Test")) # center "test" within 10 characters 
#>   Test

print("{:5d}".format(42)) # integer right justified with total 5 characters (3 space on front)
#>   42

print("{:6.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 6 total (incl decimal) so no indent
#>42.988

print("{:9.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 9 total (incl decimal) so 3 space indent
#>   42.988

print("{:15,.2f}".format(-1234567.89)) # display with commas, 2 decimals, and sign (implicit)
#>  -1,234,567.89

print("{:+15,.2f}".format(1234567.89)) # display with commas, 2 decimals, and sign (explicit)
#>  +1,234,567.89

print("{:10.3e}".format(1234567.89)) # display in scientific notation
#> 1.235e+06

print("=" * 30)

#############################
# Using the older % method
# Not as many format options
# Ex, no commas
#############################

print("The correct answer is %d" % (42))
#>The correct answer is 42

print("%s %s" % ("one", "two"))
#>one two

print("%10s" % ("right")) # right justify within 10 space
#>     right

print("%-10s %10s" % ("left", "right")) # pad both left and right justifies with 10 (total width 20 chars)
#>left           right

print("%5d" % (42)) # integer right justified with total 5 characters (3 space on front)
#>   42

print("%6.3f" % (42.987654321)) # rounds to 3 decimals, occupies 6 total (incl decimal) so no indent
#>42.988

print("%9.3f" % (42.987654321)) # rounds to 3 decimals, occupies 9 total (incl decimal) so 3 space indent
#>   42.988

print("{:10.3e}".format(1234567.89)) # display in scientific notation
#> 1.235e+06











