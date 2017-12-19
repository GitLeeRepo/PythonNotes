#!/usr/bin/python3

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
