#!/usr/bin/python3

# The following demonstrates the use of passing multiple arguments, which is 
# received either as a tuple (with the param preceded by a single asterisk) 
# or as a dictionary (with the param preceded with a double asterisk)

def multi_arg(*multi):
    print(type(multi), ":", multi) # <class 'tuple'> : (1, 2, 3, 4)

def multi_dict_arg(**mdict):
    print(type(mdict), " :", mdict) # <class 'dict'>  : {'one': 1, 'two': 2, 'three': 3}

multi_arg(1, 2, 3, 4)
multi_dict_arg(one=1, two=2, three=3)
