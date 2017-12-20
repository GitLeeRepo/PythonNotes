#!/usr/bin/python3

# Example of a module imported by module_ex1a.py  This one is in a
# subfolder named 'common' from where module_ex1a is located, which 
# along with the __init_.py file makes it part of a package called 
# common. The __init__.py file can be empty or contain initaliztion 
# code for the package.

# uses the __name__ global which contains the module name
def hello():
    print("Hello from", __name__)
