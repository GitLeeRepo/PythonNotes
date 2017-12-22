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

menu_commands = ['1', 'm', 'q']

# class handles command loop processing
commands = []
class CmdParse(cmd.Cmd):
    prompt = "> "
    def do_listall(self, line):
        print(commands)
    def do_help(self, line):
        #super().do_help(line)
        display_help()
    def do_menu(self, line):
        menu_choice("m")
    def do_exit(self, line):
        sys.exit(0)
    def default(self, line):
        if line in menu_commands:
            menu_choice(line)
        else:
            display_help()
        commands.append(line)

def display_help():
    print("listall\t - display command history")
    print("help\t - this text")
    print("menu\t - display menu")
    print("exit\t - exit the program")

def getmarkdown():
    uf = urllib.request.urlopen("https://raw.githubusercontent.com/GitLeeRepo/LinuxKernelNotes/master/KernelGlosssaryConcepts.md")   # open for read

    for line in uf:
        print(line.decode("utf-8"))    # decode coverts byte array to string

def display_menu():
    print("Options")
    print("\t1. Get markdown from my GitHub")
    print("\tm. Display menu")
    print("\tq. Quit")
    print("\n\tType 'help' for additional options")

def menu_choice(opt):
    if opt == "m":
        display_menu()
    elif opt == "1":
        getmarkdown()
    elif opt == "q":
        sys.exit(0)

# display menu then start command loop
display_menu()
CmdParse().cmdloop()
