#!/usr/bin/python3

# Demonstrates JSON import of user data from GitHub, showing the variation
# of data types depending on the number of JSON items (multiple results
# in lists), whereas a single results in either a dictionary or
# collections.OrderedDic depending on the parameter passed to json.loads
#
# To retain the original JSON order within an equivalent Python data
# structure use collections.OrderedDict, since Python's dict is inherently
# undorder

import json
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict # to retain the original order of the json

# import the JSON to a list of randomly ordered dictionary items
url = urlopen('https://api.github.com/users')
dictlist = json.loads(url.read().decode('utf-8'))
pprint(dictlist)
print(type(dictlist)) # <class 'list'> - contains dicts

input('List of dictionary items in random order. Press Enter to continue')

# import the JSON to a list retaining the JSON order of items
url = urlopen('https://api.github.com/users')
ord_dictlist  = json.loads(url.read().decode('utf-8'), object_pairs_hook=OrderedDict)
pprint(ord_dictlist)
print(type(ord_dictlist)) # <class 'list'> - contains collections.OrderedDicts

input('List retaining the JSON order of items. Press Enter to continue')

# import the JSON to a randomly ordered dictionary 
url = urlopen('https://api.github.com/users/GitLeeRepo')
jdict = json.loads(url.read().decode('utf-8'))
pprint(jdict)
print(type(jdict)) # <class 'dict'>

input('Dictionary items in random order. Press Enter to continue')

# import the JSON to a ordered dictionary (tuples) to retain original JSON order
url = urlopen('https://api.github.com/users/GitLeeRepo')
ord_dict = json.loads(url.read().decode('utf-8'), object_pairs_hook=OrderedDict)
pprint(ord_dict)
print(type(ord_dict)) # <class 'collections.OrderedDict'>

input('Ordered dictionary items (tuples) to retain original JSON order. Press Enter to continue')
