#!/usr/bin/python3

# file_ex4.py
#
# Example 4 copies a file by reading with readline() using a while loop, 
# using both the file.write() method and print() function for outputting
# to a file.  This is a more traditional way that you might find in
# other languages, but in Python file_ex1.py does this in a more concise
# Pythonic manner.  This one uses a second output file just to show
# that the standard print function can also be used to write to files.
#
# Other examples
#       file_ex1.py - using an implicit read in the for statement
#       file_ex2.py - reading the file into a list with readlines()
#       file_ex3.py - read the entire file in one read()

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
