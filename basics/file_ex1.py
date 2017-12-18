#!/usr/bin/python3

fr = open("file_ex1.py")    # open for read
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
