#!/usr/bin/python3

# web_ex1.py
#
# Example 1 demo some of the functionality of urllib 
#
#
# Other examples

import urllib.request
import cmd
import sys


# class handles command loop processing
commands = []
class CmdParse(cmd.Cmd):
    prompt = "> "
    def do_listall(self, line):
        print(commands)
        commands.append(line)
    def do_help(self, line):
        #super().do_help(line)
        display_help()
        commands.append(line)
    def do_menu(self, line):
        menu_choice("m")
        commands.append(line)
    def do_exit(self, line):
        sys.exit(0)
    def default(self, line):
        menu_choice(line)
        commands.append(line)

def display_help():
    print("listall\t - display command history")
    print("help\t - this text")
    print("menu\t - display menu")
    print("exit\t - exit the program")

def getmarkdown():
    uf = urllib.request.urlopen("https://raw.githubusercontent.com/GitLeeRepo/LinuxKernelNotes/master/KernelGlosssaryConcepts.md")
    for line in uf:
        print(line.decode("utf-8"))    # decode coverts byte array to string

def getmarkdownfile():
    uf = urllib.request.urlretrieve("https://raw.githubusercontent.com/GitLeeRepo/LinuxKernelNotes/master/KernelGlosssaryConcepts.md", \
                                                                                                                "out1.md")
    if uf:
        print("out1.md saved")

def convert_to_base64():
    try:
        fr = open("out1.md", "r")
        fw = open("out1.b64", "wb") # binary for byte array
        text = fr.read()
        b64text = urllib.request.base64.b64encode(bytearray(text, "utf-8"))
        print(b64text)
        fw.write(b64text)
    except:
        print("unable to read from out1.md, you must run the Get markdown as file option first")

def convert_from_base64():
    try:
        fr = open("out1.b64", "rb") # binary for byte array
        b64text = fr.read()
        decodetext = urllib.request.base64.b64decode(b64text).decode("utf-8")
        print(decodetext)
    except:
        print("unable to open out1.b64, you must run the convert to base64 option first")

def display_menu():
    print("Options")
    print("\t1. Get markdown from GitHub")
    print("\t2. Get markdown as file from GitHub")
    print("\t3. Convert to base64")
    print("\t4. Convert from base64")
    print("\tm. Display menu")
    print("\tq. Quit")
    print("\n\tType 'help' for additional options")

def menu_choice(opt):
    if opt == "m":
        display_menu()
    elif opt == "1":
        getmarkdown()
    elif opt == "2":
        getmarkdownfile()
    elif opt == "3":
        convert_to_base64()
    elif opt == "4":
        convert_from_base64()
    elif opt == "q":
        sys.exit(0)

# display menu then start command loop
display_menu()
CmdParse().cmdloop()
