# Overview

Notes on the Python3 programming language, examples use Python 3 syntax, not Python 2.

# References

* [Python 3.5.4 Documentation](https://docs.python.org/3.5/)
* [Python Style Guide](https://www.python.org/dev/peps/pep-0008/#naming-conventions) - naming conventions, etc.

## Books

* [Programming in Python 3: A Complete Introduction to the Python Language](https://www.amazon.com/gp/product/B002YYWEHW)
* [Python Essentials](https://www.amazon.com/Python-Essential-Reference-Developers-Library-ebook/dp/B002EF2AQ6)

## YouTube Videos

* [Google Python Class Series](https://www.youtube.com/watch?v=tKTZoB2Vjuk)
* [Python Crash Course](https://www.youtube.com/watch?v=oy4GOI9vn5M) - Traversy
* [Python Programming](https://www.youtube.com/watch?v=N4mEzFDjqtA) - Derek Banas

## My Other Notes

* [PHPNotes](https://github.com/GitLeeRepo/PHPNotes/blob/master/PHPNotes.md#overview)
* [JavaScriptNotes](https://github.com/GitLeeRepo/JavaScriptNotes/blob/master/JavaScriptNotes.md#overview)
* [NodejNotes](https://github.com/GitLeeRepo/NodejsNotes/blob/master/NodejNotes.md#overview)
* [RestApiNotes](https://github.com/GitLeeRepo/RestApiNotes/blob/master/RestApiNotes.md#overview)

# Contents

* [References](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#references)
* [Concepts and Terminology](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#concepts-and-terminology)
* [Installation](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#installation)
* [Python Shell](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#python-shell)
* [Python Script Structure](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#python-script-structure)
* [Python Keywords](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#python-keywords)
* [Types and Objects](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#types-and-objects)
* [Operators and Expressions](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#operators-and-expressions)
* [Conditionals](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#conditionals)
* [Loops](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#loops)
* [Functions](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#functions)
* [Modules and Packages](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#modules-and-packages)
* [Classes / Object Oriented Programming](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#classes--object-oriented-programming)
* [Input / Output](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#input--output)
* [File Handling](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#file-handling)
* [Regular Expressions](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#regular-expressions)
* [Exceptions](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#exceptions)
* [Decorators](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#decorators)
* [Web Frameworks](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#web-frameworks)


# Concepts and Terminology

* **\>\>\>** - as used in this document is simply the prompt as displayed in the **Python Shell**.  It precedes a Python statement, and if followed by a line without these angle brackets, then these lines represents the output of that statement.  These angle brackets are not used for those sections that represent the code as it appears in a script file, rather than in the interactive shell. 

# Installation

For Ubuntu:

```bash
sudo apt install python3
```

# Python Shell

The interactive shell is available when you type **python3** by itself on the command line, or **python3 -i scriptname.py** to load a script into the interactive shell.

## Command line

* **-i scriptname.py** - loads a runs the script inside the interactive environment.

## Internal Prompt >>>

* **help()** - places you into the help subsystem where you can enter help commands.  Type quite to return to the Python interpreter.
* **help(\<object\>)** - loads help on the specified module (if it has been loaded with import) or other built-in function in a man page like interface.  Type "q" to quit.
* **dir(<module>)** - shows the properties and methods of a loaded module, for example, **dir(sys)** (after first typing **import sys**)

* **\_ (underscore)** - holds the value of the last operation, which can be assigned or used, e.g, **newvar = \_**.  This is only available in the interactive environment.

# Python Script Structure

## Basic Python Script Structure

Note these points in the following program
* Specifying where the Python3 interpreter can be found (**#!/usr/bin/python3** on Ubuntu)
* **import** directives for bringing in external code (in this case the built-in **sys** module
* Multiline comments with the **triple opening and closing apostrophe's**
* Single line comments with **#**
* Function definitions, ex., **def displaymsg(msg):**
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
```

# Python Keywords

x      | x        | x       | x       | x        | x      | x
-------|----------|---------|---------|----------|--------|-------
and    | continue | except  | global  | lambda   | pass   | while
as     | def      | False   | if      | None     | raise  | with
assert | del      | finally | import  | nonlocal | return | yield
break  | elif     | for     | in      | not      | True   | n/a
class  | else     | from    | is      | or       | try    | n/a

## Python Built-ins

To see a list of Python's Built-ins, i.e., functions, data types, and exceptions (exceptions start with capital letters) enter the following in the Python Shell:

```python
>>> dir (__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
'BufferError','BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 
'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 
'GeneratorExit', 'IOError', 'ImportError','ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
'IsADirectoryError', 'KeyError', 'KeyboardInterrupt','LookupError', 'MemoryError', 'NameError', 'None', 
'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError','OverflowError', 
'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 
'ValueError', 'Warning','ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', 
'__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 
'bytes', 'callable', 'chr', 'classmethod','compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir',
'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 
'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass','iter', 'len', 'license', 'list',
'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 
'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str','sum', 
'super', 'tuple', 'type', 'vars', 'zip']
```

Note that names that start end end with double underscores should not be used directly.  While those that start with underscores, but don't end with them are intended for special uses.

# Types and Objects

All data types in Python are objects, which have associated methods and properties.  Python is a dynamically typed language, and the type can be dynamically changed in the same scope.  For example, the variable named 'principal' can be assigned 14.51 (float), 12 (integer), and "Mr Smith", all in the same scope within the program, in each case a new instance is created, and the variable name references this new instance.  If the old instance doesn't have any other variable names referencing it then it will be eligible for garbage collection.

## Types

* Numbers (immutable) - includes both integer (including boolean) and floating point
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
* Custom Class Objects

To determine the current type of a variable you can use the **type()** function:

```python
>>> s="Hello"
>>> type(s)
<class 'str'>
>>> f=4.54
>>> type(f)
<class 'float'>
>>> i=34
>>> type(i)
<class 'int'>
>>> l = [ 1, 2, 3]
>>> type(l)
<class 'list'>
>>> t = (4, 5, 6)
>>> type(t)
<class 'tuple'>
>>> d = { 'one' : 1, 'two' : 2 }
>>> type (d)
<class 'dict'>
```

The **is operator** can be used to determine if two variable names are pointing to the same object, for example:

```python
>>> a = [1, 2, 3, "four"]
>>> b = [1, 2, 3, "four"]
>>> a is b
False
>>> a=b
>>> a is b
True
```

Note there can be some inconsistencies when comparing basic data types using **is**, for example:

```python
>>> s1 = "This is a test"
>>> s2 = "This is a test"
>>> s1 is s2
False
>>> s1 = "test"
>>> s2 = "test"
>>> s1 is s2
True
```
For the shorter version, Python appears to try to optimize things by having them point to the same underlying object (even though they were assigned separately).  In these cases it is better to compare values using the **== equality** operator.

The **is operator** can be used to compare to Python's **None**, which is the equivalent of **null** in other languages

```python
>>> s1="Hello"
>>> s2=None
>>> s3=""
>>> s1 is None
False
>>> s2 is None
True
>>> s3 is None
False
```
Note that an empty string is not considered **None**

## Numbers

Numbers can represent **integers** (includes **boolean**), and **float** (includes **double**, **complex**, and **decimal.Decimal**, in Python integers are not limited by any particular byte size, but rather by the available memory on the computer.  Python floats are limited to the size used by the C compiler that compiled Python.

The **decimal.Decimal** numeric type is import from the **decimal** module and is used to represent large numbers that contain decimal points (such as in financial transactions) accurately, which is not possible with standard float because of precision issues.  It is however a slower data type to work with than is a standard float.  **Ints** can also be used to represent large numbers with precision.

In most cases the different numeric types can be mixed (**decimal.Decimal** is the exception).  Using **floats** and **integers** together results in a **float** result, using **complex** and **float** together results in a **complex** number.  **decimal.Decimal** can only be used with other **decimal.Decimal** numbers or with **ints**, which results in a **decimal.Decimal** result.

### Numeric/String Conversions

To convert a string to an integer or float

```python
>>> int("45")
45
>>> float("2.345")
2.345
>>> float("3e+19")
3e+19
>>> float("3e+19") + float("2e+18")
3.2e+19
```

To convert an integer or float to a string:

```python
>>> str("99")
'99'
>>> str("45.345")
'45.345'
>>> str("2e+19")
'2e+19'
>>> s = str("2e+19")
>>> float(s)  # convert the string variable back to a float
2e+19
```

### decimal.Decimal Numeric type

The **decimal.Decimal** numeric type is import from the **decimal** module and is used to represent large numbers that contain decimal points (such as in financial transactions) accurately, which is not possible with standard float because of precision issues.  It is however a slower data type to work with than is a standard float.

Note do NOT try too convert a float to a decimal with decimal.Decimal(1234567.8901) since this will then be just as imprecise as a float (this includes float literals).  Instead either convert from an integer or string representation.

**Example:**

```python
from decimal import *
import locale

# print the current context setting such as rounding and precision
print(getcontext())
# change the precision from the default 28 to 53
getcontext().prec=53
print("After changing precision:")
print(getcontext())
print("")

# setting locale will print thousands separator (us: comma) and local
# decimal point when used with 'n' format specifier in print function
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
# note: locale.setlocale(locale.LC_ALL, "") will set it to system default

# note the use of string conversion, if this was converted from a float
# it would inherit the floats imprecision, you should either convert from
# a string or an integer, never use a float (including a float literal).
dec1 = Decimal('12345678901234567890123456789012345678901234567890.99')
dec2 = Decimal('0.02')
dec3 = dec1 + dec2
print("Decimals with precision=53 {:n} + {:n} = {:n}".format(dec1, dec2, dec3))
dec1 = Decimal('99999999999999999999999999999999999999999999999999.99')
dec2 = Decimal('0.02')
dec3 = dec1 + dec2
print("Decimals with precision=53 {:n} + {:n} = {:n}".format(dec1, dec2, dec3))
```

### Number Bases

By default numbers are displayed in base 10, the following specifiers can be used for other bases:

* **0b10101010** - binary numbers
* **0o675431** - octal numbers
* **0xFE05AB7D** - hexadecimal numbers

Note when uppercase letters are used they result is displayed with uppercase letters.

### Math Module

**Math functions:**

x                         | x
--------------------------|--------------------------------------------------------
math.acos(x)              | math.gamma(x)
math.acosh(x)             | math.gcd(a, b)
math.asin(x)              | math.hypot(x, y)
math.asinh(x)             | math.isclose(a, b, \*, rel_tol=1e-09, abs_tol=0.0)
math.atan(x)              | math.isfinite(x)
math.atan2(y, x)          | math.isinf(x)
math.atanh(x)             | math.isnan(x)
math.ceil(x)              | math.ldexp(x, i)
math.copysign(x, y)       | math.lgamma(x)
math.cos(x)               | math.log(x\[, base]) - exclude base for Natural Log
math.cosh(x)              | math.log1p(x)
math.degrees(x)           | math.log2(x)
math.erf(x)               | math.modf(x)
math.erfc(x)              | math.pow(x, y)
math.exp(x)               | math.radians(x)
math.expm1(x)             | math.sin(x)
math.fabs(x)              | math.sinh(x)
math.factorial(x)         | math.sqrt(x)
math.floor(x)             | math.tan(x)
math.fmod(x, y)           | math.tanh(x)
math.frexp(x)             | math.trunc(x)
math.fsum(iterable)       | n/a

**Math Constants:**

x                          | x
---------------------------|-------------
math.e                     | math.pi
math.inf                   | math.tau
math.nan                   | n/a



## Strings

Strings are an indexed sequence of characters, with individual characters accessible using an index operator, i.e., **str\[i\]**.

### String Quoting

Strings can be either single, or double quoted, both of which are generally acceptable as long as their use is consistent.  When a string contains a single quote within it, you can use double quotes to avoid having to escape it with a backslash, with the same being true of double quotes within single quotes.

### Multiline Strings (triple quotes)

```python
>>> str = '''This is
>>> written on multiple lines'''

>>> print(str)
This is
written on multiple lines
```

### String Concatenation

```python
>>> str1 = "5"
>>> str2 = "3"
>>> newstr = str1 + str2
>>> print(newstr)
53

# to convert to number, so these can be numerically added instead of concatenated:
>>> newnum = int(str1) + int(str2)
>>> print(newnum)
8
```
Note how Python always concatenates numeric strings, not as in some languages which would have converted these to numbers implicitly and added them for a result of 8.

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

### Raw Strings with Regular Expressions

Because **regular expressions** use a lot of special characters that would have to be escaped to work correctly, Python provides a simpler solution using **raw strings**, which don't need to be escaped, all characters a literals.  You create raw strings by preceding the opening quote with an **r**.

```python
import re

phone_re = re.compile(r"((?:[(]\d+[)])?\s*\d+(?:-\d+)?)$")
match = phone_re.search(personstr)
```

Refer to the [**Regular Expression**](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#regular-expressions) section later in this document for more information and examples on the regular expressions themselves.


## Lists

Note the following features in the list below:
* Lists can contain mixed types
* Lists can be sliced with **\[n:n\]** notation
* Lists can be easily sorted
* Lists can be appended to (they are mutable) **empty.append()**
* Lists items can be updated **empty\[1] = "very"**
* List Items can be removed **empty.remove("very")** and **empty.pop()**
* You can create references to lists, in which two variables point to the same list
* You can make copies of lists
* You can concatenate lists creating a combined list
* You can print the entire list with one print (no loops), subsets (through slicing) or individual elements through indexing
* Lists can be created from splitting strings based on a delimiter
* Lists can be converted (joined) to a string with a specified delimiter
* Lists can be iterated with **for** loops
* Example list methods shown: append(), insert(), remove(), pop(), sort(), clear()
* Methods NOT shown: extend(), index(), count(), reverse(), copy()

```python
food = [ 'cereal', 'cheese', 'nuts', 'milk', 'corn' ]
items = [ 'paper', 'soap', 'cleaner' ]
mixed = [ 'one', 1, 'two', 2, 'three', 3 ]
empty = []

# print all elements
print(food)
print(food[:])
print(food[0:])
print(food[0:9])

# print one element
print(food[3], "and", food[0])

# print a range of elements with slice
print(food[0:4])     # print the first 4 elements
print(food[0:-1])    # print all but the last element
print(food[-1])      # print the last element

# concatenate lists, creates a new list

shoppinglist = food + items
print(shoppinglist)

# sort the list
shoppinglist.sort()
print("sorted:", shoppinglist)

# mixed strings and numbers
print(mixed)

# list pointer vs list copy
strptr = mixed     # both point to the same list
strcpy = mixed[:]  # two different copies of the list
mixed[0] = "uno"   # change the original
print(strptr)      # pointer version has the change
print(strcpy)      # the copied version does not have the change

# append to an empty list (works with any list)
empty.append('not')
empty.append('empty')
empty.append('anymore')
print(empty)

# this appends a nested list within a list
empty.append(['with', 'nested', 'list'] )
print(empty)        # prints all list items, including nested list
print(empty[3])     # prints the nested list only
print(empty[3][1])  # prints an individual item from the nested list

# insert to a specific positions in list
empty.insert(1, "new pos 1")
print(empty)

# update the element just added
empty[1] = "very"
print(empty)

# remove what was just added & updated
empty.remove("very")
# del(empty[1]) would remove the same item
print(empty)

# pop the last item from the list (in this case a nested list)
x = empty.pop()
print(x, "has been popped from", empty)

# clear the list completely
empty.clear()
print(empty, "Empty again")

# using split to go from string to list
fromsplit = "item1, item2, item3".split(",")
print(fromsplit)

# join elements into a string separated by the specified delimiter
print(", ".join(food))
print("\n".join(food[0:2]))  # print first 2 on their own line

# using for loop method instead of join. This would be more
# complicated if single line comma delimited used because of
# trailing delimiter, but newline delimited here not too bad
for item in food[2:]: # print the remaining items using for
    print(item)  
```

### Using sorted() function with a list

The **sorted()** function, as opposed to the **.sort()** method offers some additional flexibility, such as defining a function to handle your sort criteria.

```python
# Examples of  using the sorted() function

# example function to be used as key by sorted function
def sortbylen(x):
    return len(x)

# List to sort, first alphabetically, then by length
a = [ 'ccc', 'aaaa', 'd', 'bb']

# Orig list
print(a)

# Sorted ascending alphabetic
print(sorted(a))

# sorted descending alphabetic
print(sorted(a, reverse=True))

# use the len() function to sort by length
print(sorted(a, key=len))

# use my own custom sort key function
print(sorted(a, key=sortbylen))

# use my custom sort key function reversed
print(sorted(a, key=sortbylen, reverse=True))


# Orig list still unchanged
print(a)

# but the sort() method will change the underlying list
# unlike the sorted function call which creates a new one
a.sort()
print(a)
```

## Tuples

**Tuples** are similar to lists (indexing, slicing, concatenation), but are different is several ways.

* They are **immutable**, they can't be changed.  If you want to change it a new version must be created.
* They are declared with parenthesis rather than square brackets
* They are intended to be used as a whole object made up of parts, not as in a collection of distinct objects as in a list
* They can be assigned to multiple variables in one operation **first_name, last_name, phone = person**
* For a large number of small sequences, tuples are generally more memory efficient than lists.  This is because tuples are immutable, while lists are mutable, and therefore the interpreter tends to over allocate for lists in anticipation that they will be expanded.

```python
person = ( 'Bill', 'Jones', '(999)999-9999' )
single = ( 'justone', )  # note the trailing comma

# assign to individual variables
first_name, last_name, phone = person

print(person)
print(first_name, last_name, phone)

print(single) # tuple with one element
```

### Named Tuples

**Named tuples** allow you to refer to the individual elements by name, and not just index.

```python
# Original from "Programming in Python 3: A Complete Introduction to the Python Language"
#               by Mark Summerfield
#
# Modified by TK: added detail lines to output, formatting and comments
#
# Demonstrates named tuples, which allows you to refer to the individual elements
# of the tuple by name

import collections

# the named tuple with the individual element names
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

# append to sales using the named Sale tuple
sales = []
sales.append(Sale(432, 921, "2017-12-19", 3, 7.99))
sales.append(Sale(419, 738, "2017-12-20", 3, 19.99))

# print out the detail lines and total using the named elements of the tuple
total = 0
for sale in sales:
    subtotal = sale.quantity * sale.price
    total += subtotal
    print("{:6} {:6} {:12} {:5} {:8} {:8}".format(sale.productid, sale.customerid, \
                                sale.date,  sale.quantity, sale.price, subtotal))
print("Total ${0:43.2f}".format(total))
```

## Sets

Sets contain an **unordered** collection of **unique** objects.  They are created with the **set()** function.  **Sets** cannot be indexed like **lists** and **tuples**.

Sets support this standard set of operations

* **Union** - set1 | set2
* **Intersection** - set1 & set2
* **difference** - set1 - set2
* **symmetric difference** - set1 ^ set2

### Set Examples

```python
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
set2 = set([1, 3, 5, 7, 9])
set3 = set([2, 4, 6, 8, 10])
dupeslist = [1, 2, 5, 2, 3, 1]
nodupes = set(dupeslist)

# the sets to compare
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

# union operations
print("union set1 | set2:", set1 | set2)
print("union set1 | set3:", set2 | set3)
print("union set2 | set3:", set2 | set3)

# intersection operations
print("intersection set1 & set2:", set1 & set2)
print("intersection set1 & set3:", set1 & set3)
print("intersection set2 & set3:", set2 & set3)

# difference operations
print("difference set1 - set2:", set1 - set2)
print("difference set1 - set3:", set1 - set3)
print("difference set2 - set3:", set2 - set3)

# symmetric difference operations
print("symmetric difference set1 ^ set2", set1 ^ set2)
print("symmetric difference set1 ^ set3", set1 ^ set3)
print("symmetric difference set2 ^ set3", set2 ^ set3)

# duplicates not allowed and are automatically removed
print("duplicates automatically removed:", nodupes, "from", dupeslist)

nodupes.add(4)
nodupes.update([6, 7, 8])
nodupes.remove(1)
print("nodupes after adding (4), updating [6, 7, 8], and removing (1):", nodupes)
```

**Output:**

```
set1: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2: {1, 3, 5, 9, 7}
set3: {8, 2, 10, 4, 6}
union set1 | set2: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
union set1 | set3: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
union set2 | set3: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
intersection set1 & set2: {1, 3, 5, 9, 7}
intersection set1 & set3: {8, 2, 10, 4, 6}
intersection set2 & set3: set()
difference set1 - set2: {8, 2, 10, 4, 6}
difference set1 - set3: {1, 3, 5, 9, 7}
difference set2 - set3: {1, 3, 5, 9, 7}
symmetric difference set1 ^ set2 {2, 4, 6, 8, 10}
symmetric difference set1 ^ set3 {1, 3, 5, 7, 9}
symmetric difference set2 ^ set3 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
duplicates automatically removed: {1, 2, 3, 5} from [1, 2, 5, 2, 3, 1]
nodupes after adding (4), updating [6, 7, 8], and removing (1): {2, 3, 4, 5, 6, 7, 8}
```

## Dictionaries

A **dictionary** is an **associative array** / **hash table** that contains objects that are indexed by keys.  The use **key/value** pairs for storing information.  Dictionaries are one of the most efficient ways of accessing indexed data based on a key value.

### Dictionary Examples

```python
# start with an empty dictionary

d = {}

# creates the following key value pairs
# Keys      Values
# a         'alpha'
# b         'beta'
# g         'gamma'
# o         'omega'

d['a'] = 'alpha'
d['b'] = 'beta'
d['g'] = 'gamma'
d['o'] = 'omega'

# prints in random order
print("random order")
print("{:4}   {:6}".format("key", "value"))
for key in d:
    print("{:4} = {:6}".format(key, d[key]))

# to access a specific value in a dictionary, simply index it with the key
print("From", d['a'], "to", d['o'], "i.e., sorted")

# to print in sorted order
print("{:4}   {:6}".format("key", "value"))
for key in sorted(d.keys()):
    print("{:4} = {:6}".format(key, d[key]))

# indexing a key that doesn't exist will throw an error.  To get around
# this you can use the get() method instead.
print("d.get('x') gets:", d.get('x'))
print("while d.get('g') gets:", d.get('g'))

# to test if an item is in a dictionary use 'in'
print("'x' in d:", 'x' in d)
print("'b' in d:", 'b' in d)

# to retrieve a list of keys and values separately
print("d.keys():", d.keys())
print("d.values():", d.values())

# convert the key/value pairs to a list of tuples, print random and sorted
print("d.items():", d.items())
print("d.items() sorted:", sorted(d.items()))

# this time initialize a dictionary to begin with
items = {
    "item1" : 5.53,
    "item2" : 9.99,
    "item3" : 3.99,
    "item4" : 4.99,
    "item5" : 2.21
}

# print the sorted dictionary
for item in sorted(items.keys()):
    print(item, items[item])

# a couple of ways to add to dictionary
items["item6"] = 7.57
items.update({"item7" : 3.33})

print("new item6 found?", 'item6' in items)
print("new item7 found?", 'item7' in items)

# delete an entry
del items["item2"]
print("deleted item2.  Found?", "item2" in items)

# print the full list again
print("Now with two new items, and one removed item:")
for item in sorted(items.keys()):
    print(item, items[item])
```

# Operators and Expressions

* **+** - addition
* **-** - subtraction
* **\*** - multiplication
* **/** - float division
* **//** - integer division (drops the remainder)
* **%** - modulus
* **\*\*** - exponent
* **=** - assignment
* **+=** - add the right side to the left side, store in variable on left
* **-=** - subtract the right side from the left side, store in variable on left
* **\*=** - multiply the right side by the left side, store in variable on left
* **/=** - divide (float) the left side into from the right side, store in variable on left
* **//=** - divide (integer) the left side into from the right side, store in variable on left
* **in** - membership operator (for example, **item in list**, or **char in str**)
* **and** - and logical operator
* **or** - or logical operator
* **not** - not logical operator

Note **xor** is not included as an operator, but you can use the **xor()** function in the **operators** module

```python
>>> from operator import xor
>>> xor(True, False)
True
>>> xor(False, False)
False
>>> xor(False, True)
True
>>> xor(True, True)
False
```

# Conditionals

## Conditional Operator Chaining

Operator can be chained in Python, so to express that 5 is greater than 4 and less than 7, or that it is not greater than for and greater than 7, you can express it like this:

```python
>>> a=5
>>> 4 < a < 7
True
>>> 4 < a > 7
False
```

## if / elif / else

```python
if a > b:
    print ("a > b")
elif a < b:
    print("a < b")
elif a == b:
    print("a == b")
else:
    print("Now that's interesting")
```

## Using pass in conditions

If you don't want to do anything on a particular branch of a condition you can use **pass** to do nothing,

```python
if a > b:
    pass
else:
    print("b >= a")
    
```

# Loops

Note that both **for** and **while** loops support **break** to break out of the loop, and **continue** to jump back to the top of the loop.

## For Loop

Also demonstates the **range()** function.

```python
# prints 0 to 4
for i in range(5):
    print("for i in range(5):", i)

# prints 1 to 4
for i in range(1, 5):
    print("for i in range(1, 5):", i)

# prints each individual character
for c in "Hello":
    print("Parse Hello", c)

# prints each item in list
for item in ['item1', 'item2', 'item3']:
    print("items list:", item)

# prints each tuple
for tup in ('tuple1', 'tuple2', 'tuple3'):
    print("tuples:", tup)

# print each dictionary entry
entries = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3'}
for entry in entries:
    print("Dictionary key: {};  value: {}".format(entry, entries[entry]))

input("Enter to continue")

# print each line in file
f = open("loops_ex1.py")
for line in f:
    print(line, end="")
f.close()

# print string with 1 less char each time
s = "Hello"
while len(s) > 0:
    print(s)
    s = s[:-1]
```
## While Loop

```python
s = "Hello"
while len(s) > 0:
    print(s)
    s = s[:-1]
```

# Functions

## Function Return Values

Every function has a return value, if it is not specified it defaults to **None**.  You can return either a single value or a **tuple** values.  The **return** keyword is used to return the value(s).  The return values can be ignored, in which case they are discarded.  

## Python 3 Built-in Functions

x             | x           | x             | x          | x
--------------|-------------|---------------|------------|-----------------
abs()         | dict()      | help()        | min()      | setattr()
all()         | dir()       | hex()         | next()     | slice()
any()         | divmod()    | id()          | object()   | sorted()
ascii()       | enumerate() | input()       | oct()      | staticmethod()
bin()         | eval()      | int()         | open()     | str()
bool()        | exec()      | isinstance()  | ord()      | sum()
bytearray()   | filter()    | issubclass()  | pow()      | super()
bytes()       | float()     | iter()        | print()    | tuple()
callable()    | format()    | len()         | property() | type()
chr()         | frozenset() | list()        | range()    | vars()
classmethod() | getattr()   | locals()      | repr()     | zip()
compile()     | globals()   | map()         | reversed() | \_\_import\_\_()
complex()     | hasattr()   | max()         | round()    | n/a
delattr()     | hash()      | memoryview()  | set()      | n/a

## Function Examples

```python
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
```

## Passing Multiple Arguments as a Tuple or Dictionary

The following demonstrates the use of passing multiple arguments, which is received either as a tuple (with the param preceded by a single asterisk) or as a dictionary (with the param preceded with a double asterisk)

```python
def multi_arg(*multi):
    print(type(multi), ":", multi) # <class 'tuple'> : (1, 2, 3, 4)

def multi_dict_arg(**mdict):
    print(type(mdict), " :", mdict) # <class 'dict'>  : {'one': 1, 'two': 2, 'three': 3}

multi_arg(1, 2, 3, 4)
multi_dict_arg(one=1, two=2, three=3)
```

## Generator Functions

Generator functions can be used to generate sequences of results using **yield** and the **\_next()\_** (**next()** in Python2) method.  The **\_next()\_** method runs the **generator function** until the next **yield** is reached, which **suspends execution**. Execution is **resumed** after the **yield** when the **\_next()\_** method is called again.  The **\_next()\_** method is **implied** in the **for statement**, so it doesn't have to be explicitly provided.

## Generator Examples

```python
# examples from Python-Essential-Reference-Developers-Library by David Beazley
# with revisions by TK

import time

# returns multiple values using a tuple
def countdown(n):
    print("generator function counting down")
    while n > 0:
        yield n
        n -= 1

# unix like tail function
def tail(f):
    f.seek(0, 2)  # move to EOF
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line

# main function
def main():
    for i in countdown(20):
        print(i, "", end="")
    print("")

    print("\nNext this tails input1.txt, displaying output when 'test' is added.")
    print("Either run this program in the background and then run")
    print("'echo test >> input1.txt' in the foreground or append to this")
    print("file from another terminal.  Append 'end test' to terminate")
    tailed = tail(open("input1.txt"))
    grepped = grep(tailed, "test")

    for line in grepped:
        print(line, end="")
        if "end" in line:
            break

# start here
main()
```

## Coroutine Functions

Description from [python.org docs](https://docs.python.org/3/library/asyncio-task.html#asyncio.coroutine):

> Coroutines used with asyncio may be implemented using the async def statement, or by using generators. The async def type of coroutine was added in Python 3.5, and is recommended if there is no need to support older Python versions.

> Generator-based coroutines should be decorated with @asyncio.coroutine, although this is not strictly enforced. The decorator enables compatibility with async def coroutines, and also serves as documentation. Generator-based coroutines use the yield from syntax introduced in PEP 380, instead of the original yield syntax.
    
> Calling a coroutine does not start its code running – the coroutine object returned by the call doesn’t do anything until you schedule its execution.
  
A coroutine's execution is suspended until a future event occurs.  A coroutine has similarities to generator in that they suspend execution until an event occurs, but where a generator returns control to its caller, a coroutine returns control somewhere else.

### Coroutine Examples

**Generator Style:**

```python
# original from Python-Essential-Reference-Developers-Library by David Beazley
# modified by TK with comments and changed to be based on user input.
#
# Demonstrates coroutines.  In this case a variable number of coroutines are
# initialized, with the number dependent on the number of key words entered
# by the user.  The user is then prompted for keywords to search for.

# coroutine - generator type compatible with Python 2
def print_matches(matchtext):
    print ("Looking for", matchtext)
    while True:
        line = (yield)  # yield control until send() called
        if matchtext in line:
            print(line)


def main():
    # hold the list of coroutine calls
    matchers = []

    # create a list of coroutines (matchers)
    keyword = "no"
    while keyword != "done":
        keyword = input("Enter a list of key words, one per line ('done' when done): ")
        if keyword != "done":
            matchers.append(print_matches(keyword))

    # initialize each coroutine entered
    for matcher in matchers:
        matcher.__next__() # advance each coroutine to the yield

    #
    response = ""
    while response != "end":
        response = input("Enter the magic word or words ('end' to end): ")
        for matcher in matchers:
            matcher.send(response)

    for matcher in matchers:
        matcher.close()

main()
```

### Function Decorators

Refer to the [Decorators](https://github.com/GitLeeRepo/PythonNotes/blob/master/PythonNotes.md#decorators) section later in this document.

# Modules and Packages

**Modules** provide a means of grouping functions and custom data structures together so that they can be distributed across multiple applications through **import** statements.  **Packages** provide a means of grouping modules together in a logical manner.

A **module** is like any other Python file, typically with a **\*.py** extension.  The difference is that that are not intended to be run as a stand alone program, but to be imported into another script.

## Import examples

**Format:**

```python
import <importable>[, <importable2>,...]
import <importable> as <name>

from <importable> import <object>
from <importable> import <object> as <name>
from <importable> *
```

**Examples:**

Based on example from: [Programming in Python 3: A Complete Introduction to the Python Language](https://www.amazon.com/gp/product/B002YYWEHW)

```python
import os
print(os.path.basename(filename))  # safe fully qualified

import os.path
print(path.basename(filename)) # collisions with path possible

from os import path # same as above, different syntax
print(path.basename(filename)) # collisions with path possible

from os.path import basename
print(basename(filename)) # collisions with basename possible

from os.path import *
print(basement(filename)) # numerous collisions possible
```

## Packages

A package is a collection of modules that are stored in a directory structure, with the subfolders having an \_\_init\_\_.py file (it can be empty or it can contain initialization code for the package).  They are referenced in a Python script by importing the package and one or more of its modules.

### Simple Example

**module_ex1a** - note despite its filename this one is not a module, but imports the modules

```python
# Example of calling custom modules, one of which is in the same folder
# the other one is in the subfolder named common.  This is considered
# a package.  These simply print a message and return.
#
# Note: the common folder contains an empty file called __init__.py
# which is what makes this folder a package.

import module_ex1b               # imports from the same folder or sys.path folder
from  common import module_ex1c  # imports from the common subfolder (package)

module_ex1b.hello()
module_ex1c.hello()
```

**Output:**

```bash
Hello from module_ex1b
Hello from common.module_ex1c
```

**module_ex1b** - this module is in the same folder as **module_ex1a**

```python
# Example of a module imported by module_ex1a.py  This one is in the same
# folder as module_ex1a.py

# uses the __name__ global which contains the module name
def hello():
    print("Hello from", __name__)
```

**module_ex1c** - this module is in the **common** subfolder from where **module_ex1a** is located

```python
# Example of a module imported by module_ex1a.py  This one is in a
# subfolder named 'common' from where module_ex1a is located, which 
# along with the __init_.py file makes it part of a package called 
# common. The __init__.py file can be empty or contain initialization 
# code for the package.

# uses the __name__ global which contains the module name
def hello():
    print("Hello from", __name__)
```

### Example Package directory structure

This example is from: [python.org](https://docs.python.org/2/tutorial/modules.html) on how you might choose to structure a sound package.

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

## Standard Library and Key Third Party Modules & Packages

### Standard Library

Python3 has a very extensive standard library for a number of areas.  Some of them are listed here, but for a complete list refer to Python.org's [The Python Standard Library](https://docs.python.org/3/library/index.html)

* **string**
* **sys**
* **os**
* **io**
* **math**
* **cmath**
* **random**
* **decimal**
* **fractions**
* **statistics**
* **difflib**
* **re**
* **collections**
* **array**
* **pathlib**
* **os.path**
* **fileinput**
* **zlib**
* **gzip**
* **zipfile**
* **tarfile**
* **csv**
* **hashlib**
* **time**
* **calendar**
* **logging**
* **curses**
* **errno**
* **threading**
* **multiprocessing**
* **concurrent**
* **queue**
* **socket**
* **ssl**
* **asyncio**
* **signal**
* **nmap**
* **email**
* **mailbox**
* **json**
* **mimetypes**
* **html**
* **xml**
* **cgi**
* **urllib**
* **http**
* **ftplib**
* **poplib**
* **imaplib**
* **smptplib**
* **smtpd**

### Key Third Party Libraries

* **NumPy**
* **SciPy**

# Classes / Object Oriented Programming

## Terminology

* **access control** - this is NOT explicitly provided in Python as in other object oriented languages, in which you can define data and methods to be private or public.  In effect Python allows data and methods to be private to the class by preceding them with two underscores.
* **aggregation** - also called **composition**.  It is the process of containing other class objects with a class through defining them within the class or passing them in.  They have a **has-a relation** (a car has a color) rather than the **is-a relation** of inheritance.  
* **attributes** - two major types: 1) callable attributes (methods) 2) data attributes, which are often just referred to as attributes
* **base class** - the class which is another class **inherited from**
* **class** - a custom data type that defines both data and methods
* **class variable** - static variables accessible to all instances of a class.  The use of the word 'static' here is not the same as in C++ classes where it is tied to an un-instantiated class, but not accessible from an instance.  In Python, it just means the variable is declared in the class outside of any methods.  If it is set to a default value all instances will see that same default value, but if any instance changes it, only that instance will reflect the change.
* **composition** - refer to **aggregation**
* **derived class** - a class which **inherits** from another class
* **encapsulation** - containing the functionality and data within an object
* **inheritance** - the process of one class inheriting the functionality and data of another class, refer to **specialization**.  Inheritance provides an **is-a relation** (a circle is a shape) rather than a **has-a relation** through **aggregation**.
* **instance** - a class that has been instantiated in memory, a class can have many instances
* **instance variable** - data that is unique to a particular object instance
* **methods** - a function that is encapsulated in a method and has access to the data of the method.  It performs the classes actions.
* **object** - an instance of a class that has memory allocated to it
* **overloading** - Python does NOT provide overloading as in some other object oriented languages, which allow multiple methods to have the same name as long as their parameter signatures are different.  This is not much of an issue because of Python's flexibility in defining parameters, such as optional parameters.
* **override** - the process of a derived class overriding the methods of a base class.  When a method is found in both the base class and derived class the derived method is called.  For a derived method to specifically call a base method the built-in **super()** method is called.  In Python all methods are **virtual methods**.  Refer also to **polymorphism**. 
* **polymorphism** - when calling an objects method, the appropriate **overridden** method is called, if one exists.  This will even occur when a derived method is accessed via a base methods definition (as when passing the derived method to a function/method that specifies the base method as a parameter.  This is a very powerful aspect of object oriented programming, which makes certain things easy that would otherwise be difficult and times consuming to accomplish.  It also is a big part of the **reuse** aspect of object oriented code.  Refer also to **override**.
* **property** - provide access to instance variables, using methods behind the scenes.
* **special methods** - predefined methods that begin and end with two underscores  \_\_len\_\_().  They allow us to add predefined functionality to our classes.
* **specialization** - when a class inherits from a more generic or abstract class and provides a more specialized functionality through adding or replacing the base class methods or instance variables.  The relationship of circle to shape for example.  Also called subclassing.
* **subclass** - refer to specialization
* **super class** - refer to **base class**
* **super()** - method used to call the base class method from the derived method

## Class Syntax

```python
# stand alone class
class classname:
    data & methods
    
# class that inherits from another class or classes
class classname(base_classes)
    data & methods
```

## Examples

### Simple Example

A simple class and derived class

It shows the difference between class and instance variables, with class variables retaining  their values across instances, and with instance variables having unique values per instance.  This is reflected in both the inherited instance and the new instance declarations

```python
class SimpleOne:
    __num = 1  # pseudo private, although accessible with <instance_name>._SimpleOne__num
    # the class variable
    classnums = [11]   # publicly accessible and inherited by SimpleTwo

    # initialization of the instance variable
    def __init__(self):
        self.instnums = [1]

    def show(self):
        print("class name {} with a __num={}, instnums={} and classnums={}". \
                 format(self.__class__.__name__,  self.__num, self.instnums, self.classnums))

class SimpleTwo(SimpleOne):
    __num = 2   # pseudo private

    # class variable
    # classnums is inherited from SimpleOne

    # initialization of the instance variable
    def __init__(self):
        self.instnums = [2]

    def show(self):
        print("derived class name {} with a __num={}, instnums={} and classnums={}". \
                format(self.__class__.__name__,  self.__num, self.instnums, self.classnums))

def main():
    print("\n" + "-"*50)
    print("Values of simpleone & simpletwo after initialization")
    print("-"*50)

    simpleone = SimpleOne()
    simpletwo = SimpleTwo()
    simpleone.show() # __num=1, instnums=[1] and classnums=[11]
    simpletwo.show() # __num=2, instnums=[2] and classnums=[11]

    print("\n" + "-"*50)
    print("Next both simpleone & simpletwo have their own copies of the instnums list")
    print("but each has the same classnums list (values added to one are in the other)")
    print("-"*50)

    simpleone.instnums.append(2)
    simpleone.classnums.append(22)
    simpletwo.instnums.append(3)
    simpletwo.classnums.append(33)
    simpleone.show() # __num=1, instnums=[1, 2] and classnums=[11, 22, 33]
    simpletwo.show() # __num=2, instnums=[2, 3] and classnums=[11, 22, 33]

    print("\n" + "-"*50)
    print("New instance values after initialization, now called simpleone2 & simpletwo2")
    print("Note how the classnums still retains the values from the prior instances")
    print("-"*50)

    simpleone2 = SimpleOne()
    simpletwo2 = SimpleTwo()
    simpleone2.show() # __num=1, instnums=[1] and classnums=[11, 22, 33]
    simpletwo2.show() # __num=2, instnums=[2] and classnums=[11, 22, 33]

    print("")

main()
```

# Input / Output

## Standard Input

```python
import sys

# without a newline stdout needs to be flushed before the input
# also true if print("...", end="") was used instead
sys.stdout.write("Enter your name: ")
sys.stdout.flush()

# using readline for input, strip off the newline
name = sys.stdin.readline().rstrip('\n')

# using input (combines prompt and stdio read)
age = input("How old are you? ")

print("Hello, {}.  You are {} year's old".format(name, age));
```

## Print Basic

```python
>>> print("Hello, world")
Hello, world

>>> print("Hello,", "world") # concatenates with a space in between
Hello, world

>>> print("Hello,""world") # concatenates without a space in between
Hello,world"

>>> print("Hello, ",end="") # print without newline
>>> print("world")
Hello, world

>>> print("=" * 50) # repeat the string 50 times
==================================================

>>> print(25*4)
100
```

## Print Formatted

### Using the newer .format() option

```python
>>> print("The correct answer is {0:d}".format(42))
The correct answer is 42

>>> print("{} {}".format("one", "two"))
one two

>>> print("{1} {0}".format("one", "two"))
two one

>>> print("{:>10}".format("right")) # right justify within 10 space
     right

>>> print("{:10}{:>10}".format("left", "right")) # pad both left and right justifies with 10 (total width 20 chars)
left           right

>>> print("{:^10}".format("Test")) # center "test" within 10 characters 
   Test

>>> print("{:5d}".format(42)) # integer right justified with total 5 characters (3 space on front)
   42
   
>>>print('{:15,d}'.format(123456789)) # display with commas
123,456,789

>>> print("{:6.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 6 total (incl decimal) so no indent
42.988

>>> print("{:9.3f}".format(42.987654321)) # rounds to 3 decimals, occupies 9 total (incl decimal) so 3 space indent
   42.988

>>> print("{:15,.2f}".format(-1234567.89)) # display with commas, 2 decimals, and sign (implicit)
  -1,234,567.89

>>> print("{:+15,.2f}".format(1234567.89)) # display with commas, 2 decimals, and sign (explicit)
  +1,234,567.89

>>> print("{:10.3e}".format(1234567.89)) # display in scientific notation
 1.235e+06
```

### Using the older % option

From Python2, but still works in Python3. Not as many options, for example, no numeric comma thousand separators.

```python
>>> print("The correct answer is %d" % (42))
The correct answer is 42

>>> print("%s %s" % ("one", "two"))
one two

>>> print("%10s" % ("right")) # right justify within 10 space
     right

>>> print("%-10s %10s" % ("left", "right")) # pad both left and right justifies with 10 (total width 20 chars)
left           right

>>> print("%5d" % (42)) # integer right justified with total 5 characters (3 space on front)
   42

>>> print("%6.3f" % (42.987654321)) # rounds to 3 decimals, occupies 6 total (incl decimal) so no indent
42.988

>>> print("%9.3f" % (42.987654321)) # rounds to 3 decimals, occupies 9 total (incl decimal) so 3 space indent
   42.988

>>> print("{:10.3e}".format(1234567.89)) # display in scientific notation
 1.235e+06
```

### Format Specifiers

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
G	      | Depends on size, either decimal or exponential format (uppercase)
n         | Use locale settings for thousand sep and decimal (int, float, decimal)
c         | Single character (integer or ASCII character).
r         | String (converts any python object using repr()).
s         | String (converts any python object using str()).
,         | include commas (thousand separator) in number
.         | include decimal in floating point numbers
number    | the number of characters, space fill as needed

### Setting Locale

Instead of placing a comma in the format string you can use the locale settings to specify what thousands separator to use, along with what character to use to show the decimal value.

```python
import locale

# US based comma thousand separators and period for decimal point.
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# Use the system locale (based on environment variable):
locale.setlocale(locale.LC_ALL, "")

# Reset to the default (no thousand separator)
locale.setlocale(locale.LC_ALL, "C")
```

# File Handling

## File Input/Output Examples

## Example using an Implicit Read

This example copies a file by reading without an explicit readline, the for statement itself performs the read.  It uses the file.write() method for file output

While not the fastest read operation, it is the more memory efficient in that it is processing one line at a time.

```python
fr = open("file_ex1.py", "r")   # open for read
fw = open("out1.txt", "w")      # open for write

for line in fr:
    print(line, end="")    # stdout - remove the newline character to avoid extra line
    fw.write(line)         # write to file, no extra newline (only from read)

fr.close()
fw.close()
```

## Example using an Readlines() into a List

This example copies a file by reading the lines into a list with readlines(), demonstrating that it can be sliced like a list, and then using a for loop, to print the list items (lines) out one by one.  It uses the file.write() method to write to a file.

In this case if it is a large file, be aware that the entire file (list) is stored in memory

```python
fr = open("file_ex2.py")    # open for read
fw = open("out1.txt", "w")  # open for write

# read all the lines of the file into a list
lines = fr.readlines()
# because it is a list it can use list slicing
print("As a sliced list:\n\n", lines[4:6], "\n")

# you can still process the file line by line using for
for line in lines:
    print(line, end="")     # stdout - remove the newline character to avoid extra line
    fw.write(line)          # write to file, no extra newline (only from read)

fr.close()
fw.close()
```

## Example using an Read() of Entire File

This example copies a file by reading the entire file in one file.read() method.  It uses file.write() method to write the entire file in one operation.

Without any parameters, read() reads entire file is read into memory, although the amount read can be controlled by passing in a size parameter, i.e., read(size).

```python
fr = open("file_ex3.py", "r")   # open for read
fw = open("out1.txt", "w")      # open for write

# read the entire file in as one (potentially huge) string in text mode
# note that in binary mode it is read as an object
# also note that the size to be read can be specified as a parameter
text = fr.read()

# write the entire file in one operation
print(text)     # stdout
fw.write(text)  # write to file

fr.close()
fw.close()
```

## Example using Readline() in while Loop

This example copies a file by reading with readline() using a while loop, using both the file.write() method and print() function for outputting to a file.  This is a more traditional way that you might find in other languages, but in Python file_ex1.py does this in a more concise Pythonic manner using a for loop.  This example uses a second output file just to show that the standard print function can also be used to write to files.

```python
fr = open("file_ex4.py")      # open for read
fw1 = open("out1.txt", "w")   # open for write
fw2 = open("out2.txt", "w")   # open for write

line = fr.readline()
while line:
    print(line, end="")             # stdout - remove the newline character to avoid extra line
    fw1.write(line)                 # write to file, no extra newline (only from read)
    print(line, file=fw2, end="")   # also writes to file, extra newline must be removed
    line = fr.readline()

fr.close()
fw1.close()
fw2.close()
```

# Regular Expressions

Refer to my [RegExNotes](https://github.com/GitLeeRepo/RegExNotes/blob/master/RegExNotes.md#overview) for more info on regular expressions themselves (independent of Python)

Note in the example below I always check for **if match:**.  This is important since if a match is not made, match is set to nothing, and therefore anything that attempts to use match will throw an exception.

```python
# Some regular expression examples.  Note the use of raw strings, strings
# preceded by an 'r' to avoid having to escape the special characters

import re

# just for the heck of it start with a list
person  = ["Bill Jones", "123 Main Street", "(999)999-9999"]
person += ["Mike Brown", "34 Elm Street", "(888)888-8888"]
person += ["Sarah Johnson", "456 Main Street", "(999)888-9999"]

# convert the list to a string
personstr = "\n".join( person)
print(personstr)

# find all occurrences within the multiline string
match = re.findall(r".*Jo.*", personstr)
if match:
    print (match)
match = re.findall(r".*Main.*", personstr)
if match:
    print (match)

# create a regular expression for a US phone number pattern
phone_re = re.compile(r"((?:[(]\d+[)])?\s*\d+(?:-\d+)?)$")
match = phone_re.search(personstr)
if match:
    print (match.group(0)) # group zero is the entire match

# create a regular expression for an email address, using groups
# (the parenthesis) both for isolating optional parts and for
# the extraction of the component pieces
email_re = re.compile("^((\w+\.+)?(\w+)@(\w+)\.(\w+\.+)?(com|net|org))$")
match = email_re.search("bob.roberts@smtp.example.com")

# creates a tuple containing the individual groups in the expression
if match:
    grps = match.groups()
    for g in grps:
        if g != None:
            # use a function to remove the trailing period, since the period
            # itself needs to be inside the optional groups
            print (g.strip('.'))

# using the same expression, but with fewer components (e.g, bob, not
# bob.roberts) to show the flexibility of the expression with its optional
# groups (those with the '?' following them)
match = email_re.search("bob@example.com")
if match:
    grps = match.groups()
    for g in grps:
        if g != None:
            print (g.strip('.'))
```

# Exceptions

```python
num = input("Input an integer, or for an exception don't: ")

try:
    i = int(num)
    print("{} is a valid integer".format(i))
except ValueError as err:
    print(err)
```
Note this will generate an error when entering a floating point number, in addition to a string or other non-integer data type.

# Decorators

Example from a PyData YouTube video posted by [Coding Tech](https://www.youtube.com/watch?v=7lmCu8wz8ro&t=3306s):

Demonstrates using a decorator to tie a function to a wrapper function, in this case a 'timer' wrapper function that provides a before and after timing of our function.  As long as the @timer decorator precedes the function we want to time (assuming the wrapper has the same signature as our function, as 'f(x, y)' does with our add(x, y) and sub(x, y) functions), it will call the wrapper, instead of our function directly.  Simply remove the decorator and our function is called directly again (no wrapper).

```python
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
```

# Web Frameworks

* Django - Server side web development
* Flask
* Web2Py
* Pylons
