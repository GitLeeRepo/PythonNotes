#!/usr/bin/python3
# Just a sandbox app to explore different Python features and techniques for learning purposes

import sys

def hello(showPrompt=True):
    s = "Hello World!"
    print (s)
    #using slice syntax below
    print (s[:5]) #Hello
    print (s[6:-1]) #World
    print (s[1:8]) #ello wo
    print (s[1:-4]) #ello wo - same result indexing from right
    if len(sys.argv) > 1:
        print ("Command line args: " + str(sys.argv[1:])) #print the command line args if they exists
    if showPrompt:
        name = input ("Name?")
        print ("Hello " + name) 
        print ("Hello", name) #both valid, 2nd adds its own space
    else:
        print ("Input not selected (pass True on hello() method call to display input prompt)")

def listDemos():
    list1 = [1, 2, 3]
    print(list1)
    list2 = [4, 5, 6]
    list3 = list1 + list2 #adds list2 to the end of list1
    print(list3) 
    list4 = list2 + list1 #adds list1 to the end of list2
    print(list4)

    print("List pointer:")
    list1Pointer = list1 #they point to same location
    list1[0] = "1b"
    print(list1)
    print(list1Pointer)

    print("List copy")
    list1Copy = list1[:] #makes a copy, two different lists
    list1[0] = 1
    print(list1)
    print(list1Copy)



def menuChoices():
    print ("Choose:")
    print ("1 - call hello (demo strings and argv command lines)")
    print ("2 - list demo")
    print ("d - display menu choices")
    print ("x - exit program")


def main():
    menuChoices()
    select = input("Selection: ")
    while select != "x":
        if select == "1":
            hello(False) #hello() without arg will use the default specified in parameter def
        elif select == "2":
            listDemos()
        elif select == "d":
            menuChoices()
        select = input("Selection: ")


main()
