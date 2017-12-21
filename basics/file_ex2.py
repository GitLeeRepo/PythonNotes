#!/usr/bin/python3

# file_ex2.py
#
# Example 2 copies a file by reading the lines into a list with readlines(), 
# demonstrating that it can be sliced like a list, and then using a for loop,
# to print the list items (lines) out one by one.  It uses the file.write() 
# method to write to a file.
#
# In this case if it is a large file, be aware that the entire file (list)
# is stored in memory
#
# Other examples
#       file_ex1.py - using an implicit read in the for statement
#       file_ex3.py - read the entire file in one read()
#       file_ex4.py - using readline() in a while loop

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
