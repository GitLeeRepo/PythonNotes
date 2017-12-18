#!/usr/bin/python3

import sys

# without a newline stdout needs to be flushed before the input
# also true if print("...", end="") was used instead
sys.stdout.write("Enter your name: ")
sys.stdout.flush()

# use readline for input, strip off the newline
name = sys.stdin.readline().rstrip('\n')

# use input (combines prompt and stdio read)
age = input("How old are you? ")

print("Hello, {}.  You are {} year's old".format(name, age)); 
