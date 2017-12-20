#!/usr/bin/python3

# Example of calling custom modules, one of which is in the same folder
# the other one is in the subfolder named common.  This is considered
# a package.  These simply print a message and return.
#
# Note: the common folder contains an empty file called __init__.py
# which is what makes this folder a package.

import module_ex1b               # imports from the same folder or sys.path folder
from  common import module_ex1c  # imports from the common subfolder (package)

module_ex1b.hello()
module_ex1c.hello()
