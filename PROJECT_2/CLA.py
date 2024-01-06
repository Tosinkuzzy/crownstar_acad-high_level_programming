"""Command Line Arguments: argv is not Array it is a List. It is available sys Module. The Argument which are passing at the time of execution are called Command Line Arguments.
D:\Python_classes py test.py 10 20 30 (Command Line Arguments)

Within the Python Program this Command Line Arguments are available in argv. Which is present in SYS Module.

test.py 10 20 30
NOTE: 
- argv[0] represents Name of Program. But not first Command Line Argument.
- argv[1] represent First Command Line Argument

Program: To check type of argv from sys"""

import argv
print(type(argv))

# WAP to display Command Line Arguments
from sys import argv
print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv)
print("Command Line Arguments one by one:")
for x in argv:
    print(x)
