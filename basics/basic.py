#!/usr/bin/python3

'''
    basic.py

    Demonstrate the basic structure of a Python3 program
'''

# imports
import sys



# function
def displaymsg(msg):
    print(msg)

# main function
def main():
    # if command line args then display each one
    if len(sys.argv) > 1:
        for arg in sys.argv:
            displaymsg(arg)
    else:
        displaymsg("Hello, world")

# start here
main()
