#!/usr/bin/python3

# Some regular expression examples.  Note the use of raw strings, strings
# preceded by an 'r' to avoid having to escape the special characters

import re

# just for the heck of it start with a list
person  = ["Bill Jones", "123 Main Street", "(999)999-9999"]
person += ["Mike Brown", "34 Elm Street", "(888)888-8888"]
person += ["Sarah Johnson", "456 Main Street", "(999)888-9999"]

# convert the list to a string
personstr = "\n".join( person)
print(personstr)

# find all occurances within the multiline string
match = re.findall(r".*Jo.*", personstr)
print (match)
match = re.findall(r".*Main.*", personstr)
print (match)

# create a regular expression for a US phone number pattern
phone_re = re.compile(r"((?:[(]\d+[)])?\s*\d+(?:-\d+)?)$")
match = phone_re.search(personstr)
print (match.group(0)) # group zero is the entire match

# create a regular expression for an email address, using groups
# (the parenthesis) both for isolating optional parts and for
# the extraction of the component pieces
email_re = re.compile("^((\w+\.+)?(\w+)@(\w+)\.(\w+\.+)?(com|net|org))$")
match = email_re.search("bob.roberts@smtp.example.com")

# creates a tuple containing the individual groups in the expression
grps = match.groups()
for g in grps:
    if g != None:
        # use a function to remove the trailing period, since the period
        # itself needs to be inside the optional groups
        print (g.strip('.'))

# using the same expression, but with fewer components (e.g, bob, not 
# bob.roperts) to show the flexibility of the expression with its optional 
# groups (those with the '?' following them)
match = email_re.search("bob@example.com")
grps = match.groups()
for g in grps:
    if g != None:
        print (g.strip('.'))

