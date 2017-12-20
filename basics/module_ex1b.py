#!/usr/bin/python3

# Example of a module imported by module_ex1a.py  This one is in the same
# folder as module_ex1a.py

# uses the __name__ global which contains the module name
def hello():
    print("Hello from", __name__)
