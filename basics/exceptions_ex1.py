#!/usr/bin/python3

num = input("Input an integer, or for an exception don't: ")

try:
    i = int(num) 
    print("{} is a valid integer".format(i))
except ValueError as err:
    print(err)
