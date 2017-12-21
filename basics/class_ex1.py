#!/usr/bin/python3

# A simple class and derived class
# It shows the diffence between class and instance variables, with class 
# variables retaining  their values across instances, and with instance 
# variables having unique values per instance.  This is reflected in both 
# the inherited instance and the new instance declarations

class SimpleOne:
    __num = 1  # pseudo private, although accessible with <instance_name>._SimpleOne__num 
    # the class variable
    classnums = [11]   # publicly accessible and inherited by SimpleTwo

    # initialization of the instance variable
    def __init__(self):
        self.instnums = [1]

    def show(self):
        print("class name {} with a __num={}, instnums={} and classnums={}". \
                 format(self.__class__.__name__,  self.__num, self.instnums, self.classnums))

class SimpleTwo(SimpleOne):
    __num = 2   # psuedo private

    # class variable
    # classnums is inherited from SimpleOne
    
    # initialization of the instance variable
    def __init__(self):
        self.instnums = [2]

    def show(self):
        print("derived class name {} with a __num={}, instnums={} and classnums={}". \
                format(self.__class__.__name__,  self.__num, self.instnums, self.classnums))


def main():
    print("\n" + "-"*50)
    print("Values of simpleone & simpletwo after initialization")
    print("-"*50)

    simpleone = SimpleOne()
    simpletwo = SimpleTwo()
    simpleone.show() # __num=1, instnums=[1] and classnums=[11]
    simpletwo.show() # __num=2, instnums=[2] and classnums=[11]

    print("\n" + "-"*50)
    print("Next both simpleone & simpletwo have their own copies of the instnums list")
    print("but each has the same classnums list (values added to one are in the other)")
    print("-"*50)

    simpleone.instnums.append(2)
    simpleone.classnums.append(22)
    simpletwo.instnums.append(3)
    simpletwo.classnums.append(33)
    simpleone.show() # __num=1, instnums=[1, 2] and classnums=[11, 22, 33]
    simpletwo.show() # __num=2, instnums=[2, 3] and classnums=[11, 22, 33]

    print("\n" + "-"*50)
    print("New instance values after initialization, now called simpleone2 & simpletwo2")
    print("Note how the classnums still retains the values from the prior instances")
    print("-"*50)

    simpleone2 = SimpleOne()
    simpletwo2 = SimpleTwo()
    simpleone2.show() # __num=1, instnums=[1] and classnums=[11, 22, 33]
    simpletwo2.show() # __num=2, instnums=[2] and classnums=[11, 22, 33]

    print("")

main()

