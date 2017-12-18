#!/usr/bin/python3


# function with default parameter
def displaymsg(msg="test"):
    print(msg)

# function with parameter (no default)
def displaymsg_nolf(msg):
    print(msg, "", end="")

# recursive function
def recurse(count):
    if count == 6:
        displaymsg("\nReverse")
        return

    displaymsg_nolf(count)
    recurse(count+1)
    displaymsg_nolf(count)
    if count == 1:
        displaymsg("\nDone")

# returns a single value
def remainder(x, y):
    q = x // y  # integer division with truncate
    r = x - (q * y)
    return r

# returns multiple values using a tuple
def divide(x, y):
    q = x // y  # integer division with truncate
    r = x - (q * y)
    return (q, r)

# main function
def main():
    displaymsg()
    displaymsg("Begin Recursion")

    recurse(1)

    print("remainder(5, 2): 5 / 2 has a remainder of", remainder(5, 2))
    quotient, remain = divide(5, 2) # assign tuple return values
    print("divide(5,2): 5 / 2 has a quotient of {} and a remainder of {}".format(quotient, remain))
    
    # when using named parameters, order doesn't matter
    print("remainder(y=2, x=5): 5 / 2 has a remainder of", remainder(y=2, x=5))

# start here
main()
