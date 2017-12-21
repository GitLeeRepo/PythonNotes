#!/usr/bin/python3

# file_ex3.py
#
# Example 3 copies a file by reading the entire file in one file.read() 
# method.  It uses file.write() method to write the entire file in one
# operation
#
# Other examples
#       file_ex1.py - using an implicit read in the for statement
#       file_ex2.py - reading the file into a list with readlines()
#       file_ex4.py - using readline() in a while loop

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
