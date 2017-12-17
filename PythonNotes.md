# Overview

Notes on the Python programming language

# References

* [Python 3.5.4 Documentation](https://docs.python.org/3.5/)

## Books

* [Python Essentials](https://www.amazon.com/Python-Essential-Reference-Developers-Library-ebook/dp/B002EF2AQ6)

## YouTube Videos

* [Google Python Class Series](https://www.youtube.com/watch?v=tKTZoB2Vjuk)
* [Python Crash Course](https://www.youtube.com/watch?v=oy4GOI9vn5M) - Traversy
* [Python Programming](https://www.youtube.com/watch?v=N4mEzFDjqtA) - Derek Banas

# Concepts and Terminology

TODO - Placeholder

# Installation

TODO - Placeholder

# IDLE Interactive Environment

TODO - Placeholder

# File Structure

## Basic Python File Structure

Note these points in the following program
* Specifying where the Python3 interpretter can be found (**#!/usr/bin/python3** on Ubuntu)
* **import** directives for brining in external code (in this case the built-in **sys** module
* Multiline comments with the **triple opening and closing apostrophe's**
* Single line comments with **#**
* Functon definitions, ex., **def displayMsg(msg):**
* Python's use of indentation to define blocks of code for functions, loops, and conditional statements
* The processing of command line arguments
* The use of the imported modules methods and properties (**sys.argv** in this case)
* The use of built-in functions (**len()** in this case)

```python
#!/usr/bin/python3

'''
    basic.py

    Demonstrate the basic structure of a Python3 program
'''

# imports
import sys

# function
def displayMsg(msg):
    print(msg)

# main function
def main():
    # if command line args then display each one
    if len(sys.argv) > 1:
        for arg in sys.argv:
            displayMsg(arg)
    else:
        displayMsg("Hello, world")

# start here
main()
```

# Types and Objects


* Numbers (immutable) - includes both integer and floating point
* Sequences
  * Strings (immutable)
  * Tuples (immutable)
  * Bytes (immutable)
  * Lists (mutable)
  * Byte Arrays (mutable)
* Sets (immutable)
* Maps
  * Dictionaries (mutable)
* Callable - callable as functions
* Class Objects

# Operators and Expressions

* **+** - addition
* **-** - subtraction
* **\*** - multiplication
* **/** - division
* **//** - integer division (drops the remainder)
* **%** - modulus
* **\*\*** - exponent

# Functions

TODO - Placeholder

# Classes / Object Oriented Programming

TODO - Placeholder

# Input / Output

TODO - Placeholder

# File Handling

TODO - Placeholder
