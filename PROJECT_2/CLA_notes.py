# Command Line Argument notes
from sys import argv
sum = 0
args = argv[1:]
for x in args  :
    n = int(x)
    sum = sum + n
print("The Sum:", sum)

""" NOTE 1: Usually space is a separator between command line arguments. If our command line argument itself contains space then we should enclose within double quotes(but not single quotes)"""

from sys import argv
print(argv[1])

""" NOTE 2: Within the Python Program command line arguments are available in the string form. Based on our requirement, we can convert into corresponding type by using type casting methods."""

from sys import argv
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))

"""NOTE 3: If we are trying to access command line arguments with out of range index then we will get Error"""

from sys import argv
print(argv[100])

"""NOTE: In Python there is argparse module to parse command line arguments and display some help messages whenever end user enters wrong input"""

input()
raw_input()
