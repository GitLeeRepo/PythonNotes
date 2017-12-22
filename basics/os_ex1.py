#!/usr/bin/python3

# Menu driven demo to explore various os and shutil modules

import sys
import os 
import shutil
import subprocess
import cmd

#command history
commands = []

#global var for path used throught this program
curpath = "." 


# derived class for handling command line processing, including command
# history.  It runs in a command loop initiated by CmdParse().cmdloop()
class CmdParse(cmd.Cmd):
    prompt = "> "
    def do_listall(self, line):
        print(commands)
    def default(self, line):
        commands.append(line)
        if line == "q" or line == "exit":
            sys.exit()
        process_menu_option(line)

# runs a shell command with the output and status captured in a tuple
def capture_command_output():
    result = subprocess.getstatusoutput("ls -l")
    # display the command output from the tuple
    print(result[1])
    print("now filter the result:")
    outputlst = result[1].split("\n")
    for line in outputlst:
        if "file_" in line:
            print(line)



# list filenames, relative path, and absolute path names
def filelist(dir=""):
    if dir == "":
        dir = expand_path(input("Directory path> "))
    print("dir", dir)
    try:
        filenames = os.listdir(dir)
        for filename in filenames:
            print(filename)
            path = os.path.join(dir, filename)
            print(path)
            print(os.path.abspath(path))
    except:
        print("Invalid path")

def diskinfo(path):
    print("disk info for disk that contains the '", path, "'path")
    du = shutil.disk_usage(path)
    dudict = du._asdict()  # dictionary version of du tuple inorder to grab labels
    for sz in dict_du_sizes(dudict):
        print("{:7} {:17,d} {:>17} {:>17}".format(sz[0], sz[1], sz[2], sz[3]))

# original tuple based unit size conversions, returns list of converted size strings
def tuple_du_sizes(sizes):
    hsizes = []
    for size in sizes:
        if size > 1000**4:
            hsizes.append([size, str(size*1000**-4)[0:10] + "TB", str(size*1024**-4)[0:10] + "TiB"])
        elif size > 1000**3:
            hsizes.append([size, str(size*1000**-3)[0:10] + "GB", str(size*1024**-3)[0:10] + "GiB"])
        elif size > 1000**2:
            hsizes.append([size, str(size*1000**-2)[0:10] + "MB", str(size*1024**-2)[0:10] + "MiB"])
        elif size > 1000:
            hsizes.append([size, str(size*1000**-1)[0:10] + "KB", str(size*1024**-1)[0:10] + "KiB"])
        else:
            hsizes.append([size, str(size) + "B", str(size) + "B"])
    return hsizes

# current dictionary based unit size conversion, returns list with leading label (dict key) and size strings
def dict_du_sizes(sizes):
    hsizes = []
    for key in sizes.keys():
        if sizes[key] > 1000**4:
            hsizes.append([key, sizes[key], str(sizes[key]*1000**-4)[0:10] + "TB", str(sizes[key]*1024**-4)[0:10] + "TiB"])
        elif sizes[key] > 1000**3:
            hsizes.append([key, sizes[key], str(sizes[key]*1000**-3)[0:10] + "GB", str(sizes[key]*1024**-3)[0:10] + "GiB"])
        elif sizes[key] > 1000**2:
            hsizes.append([key, sizes[key], str(sizes[key]*1000**-2)[0:10] + "MB", str(sizes[key]*1024**-2)[0:10] + "MiB"])
        elif sizes[key] > 1000:
            hsizes.append([key, sizes[key], str(sizes[key]*1000**-1)[0:10] + "KB", str(sizes[key]*1024**-1)[0:10] + "KiB"])
        else:
            hsizes.append([key, sizes[key], str(sizes[key]) + "B", str(sizes[key]) + "B"])
    return hsizes

# exapand path variables.  Does not check validity of path
def expand_path(path):
    tmp = path.replace('~', '$HOME')
    return os.path.expandvars(tmp)

# use to set the curpath variable (from return val) interactively
def set_curpath_var(curpath):
    tmp = expand_path(input("input new curpath value > "))
    if os.path.isdir(tmp):
        curpath = tmp
    else:
        print("invalid path")
    print("curpath = ", curpath)
    return curpath

# displays, but does not process menu choices
def display_menu():

    print("OS Menu:")
    print("\t1. List files in current directory")
    print("\t2. List files in specified directory")
    print("\t3. Disk info")
    print("\t4. Disk size test")
    print("\t5. Get Command Output")
    print("\td. Display curpath value")
    print("\tm. Display menu")
    print("\tp. Set new curpath value")
    print("\tq. Quit program")


def process_menu_option(opt):
    global curpath
    if opt == 'm' or opt == "help":
        display_menu()
    if opt == "1":
        filelist(curpath)
    elif opt == "2":
        filelist()
    elif opt == "3":
        diskinfo(curpath)
    elif opt == "4":
        for sz in tuple_du_sizes((512, 2048, 1048576, 2147483648, 2e+12, 2e+15)):
            print(sz)
    elif opt == "5":
        capture_command_output()
    elif opt == "d":
        print(curpath) 
    elif opt == "p":
        curpath = set_curpath_var(curpath)


# main function - processes menu options
def main():
    # if command line args then display each one
    if len(sys.argv) > 1:
        pass # may add choice to select menu choices from command line
   
    global curpath
    curpath = '.'
    opt = 'm'
    # display the menu before entering the command loop 
    process_menu_option(opt)
    CmdParse().cmdloop()


# start here
main()
