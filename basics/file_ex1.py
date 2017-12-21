#!/usr/bin/python3

# file_ex1.py
#
# Example 1 copies a file by reading without an explicit readline, 
# the for statement itself performs the read.  It uses the file.write() 
# method for file output
#
# While not the fastest read operation, it is the more memory efficient
# in that it is processing one line at a time.
#
# Other examples
#       file_ex2.py - reading the file into a list with readlines()
#       file_ex3.py - read the entire file in one read()
#       file_ex4.py - using readline() in a while loop

fr = open("file_ex1.py", "r")   # open for read
fw = open("out1.txt", "w")      # open for write

for line in fr:
    print(line, end="")    # stdout - remove the newline character to avoid extra line
    fw.write(line)         # write to file, no extra newline (only from read)

fr.close()
fw.close()
