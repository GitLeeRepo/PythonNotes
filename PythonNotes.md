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

## Strings

### Multiline Strings

```python
str = '''This is
written on multiple lines'''

print(str)
>This is
>written on multiple lines
```

### String Concatenation

```python
newStr = str1 + str2
```

### Using Slice on Strings

```python
s = "Hello World!"
print (s)
#using slice syntax below
print (s[:5]) #Hello -  first 5 chars
print (s[6:-1]) #World - start after 6 to 1 less than end of string
print (s[1:8]) #ello wo - start after 1 through 8
print (s[1:-4]) #ello wo - same result indexing from right
```

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

## Print Basic

```python
print("Hello, world")
>Hello, world

print("Hello,", "world") # concatenates with a space in between
>Hello, world

print("Hello,""world") # concatenates without a space in between
>Hello,world"

print("Hello, ",end="") # print without newline
print("world")
>Hello, world

print("=" * 50) # repeat the string 50 times
>==================================================

print(25*4)
>100
```

## Print Formatted

```python
print("The correct answer is {0:d}".format(42))
>The correct answer is 42

print("{} {}".format("one", "two"))
>one two

print("{1} {0}".format("one", "two"))
>two one

print("{:>10}".format("right")) # right justify within 10 space
>     right

print("{:10}{:>10}".format("left", "right")) # pad both left and right justifies with 10 (total width 20 chars)
>left           right

print(":^10".format("Test")) # center "test" within 10 characters 
>   Test

print("{:5d}".format(42)) # integer right justified with total 5 characters (3 space on front)
>   42

print("{:6.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 6 total (incl decimal) so no indent
>42.988

print("{:9.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 9 total (incl decimal) so 3 space indent
>   42.988

print("{:15,.2f}".format(-1234567.89)) # display with commas, 2 decimals, and sign (implicit)
>  -1,234,567.89

print("{:+15,.2f}".format(1234567.89)) # display with commas, 2 decimals, and sign (explicit)
>  +1,234,567.89

print("{:10.3e}".format(1234567.89)) # display in scientific notation
> 1.235e+06
```

### Format Specfiers

Specifier | Description
----------|-----------------------------------------------------------------------------
d         | Signed integer
i         | Signed integer
o         | Unsigned octal
u         | Unsigned integer
x         | Unsigned hexadecimal (lowercase)
X         | Unsigned hexadecimal (uppercase)
e         | Floating point exponential format (lowercase)
E         | Floating point exponential format (uppercase)
f         | Floating point decimal format
F         | Floating point decimal format
g         | Depends on size, either decimal or exponential format (lowercase)
G	      | Depends on size, either decimal or exponential format (luppercase)
c         | Single character (integer or ASCII character).
r         | String (converts any python object using repr()).
s         | String (converts any python object using str()).
,         | include commas (thousand separator) in number
.         | include decimal in floating point numbers
number    | the number of characters, space fill as needed

# File Handling

TODO - Placeholder
