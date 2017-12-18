#!/usr/bin/python3

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
