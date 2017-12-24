#!/usr/bin/python3

# Example from a PyData YouTube video posted by Coding Tech:
#    https://www.youtube.com/watch?v=7lmCu8wz8ro&t=3306s
#
# Demonstrates using a decorator to tie a function to a wrapper function, in
# this case a 'timer' wrapper function that provides a before and after timing
# of our function.  As long as the @timer decorator precedes the function we want
# to time (assuming the wrapper has the same signature as our function, as 
# 'f(x, y)' does with our add(x, y) and sub(x, y) functions), it will call the
# wrapper, instead of our function directly.  Simply remove the decorator and
# our function is called directly again (no wrapper)

from time import time

def timer(func):
    def f(x, y):
        before = time()
        rv = func(x, y)
        after = time()
        print('elapsed', after - before)
        return rv
    return f

@timer
def add(x, y):
    return x + y

@timer
def sub(x, y):
    return x - y

print("add(5, 8)", add(5, 8))
print("sub(5, 8)", sub(5, 8))

