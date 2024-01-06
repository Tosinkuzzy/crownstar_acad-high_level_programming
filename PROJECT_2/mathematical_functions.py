""" Mathematical Functions(math Module)
A module is collection of functions, variables and classes etc.
math is a molule that contains several functions to perform mathematical operations.
If we want to use any module in Python, first we have import that module import math
Once we import a module then we can call any function of that module"""

import math
print(math.sqrt(16))
print(math.pi)

"""We can create alias name by using as keyword. import math as m
once we create alias name, by using that we can access functions and variables of that module."""

import math as m
print(m.sqrt(16))
print(m.pi)

"""We can import a particular member of a module explicitly as follows 
- from math import sqrt
- from math import sqrt,pi
- If we import a member explicitly then it is not required to use module name while accessing."""

from math import sqrt,pi
print(sqrt(16))
print(pi)

