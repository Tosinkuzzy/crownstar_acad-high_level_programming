""" 
Output Statements. We can use print() function to display output
"""

print("Hello" + "World")
print("Hello","World")

# print() with variable number of arguments

a, b, c = 10, 20, 30
print("The Values are : {:d}{:d}{:d}".format(a, b, c))

"""
By default output values are separated by space. 
If we want we can specify separator by using "sep" attribute
"""

a, b, c = 10, 20, 30
print(a, b, c, sep = ',')
print(a, b, c, sep = ':')

# print() with end attribute

print("Hello")
print("Crown")
print("Star")

# If we want output in the same line with space

print("Hello", end = '')
print("Crown", end = '')
print("Star")

"""
NOTE: The default value for end attribute is \n, which is nothing but new line character
"""

# print(object) statement

"""
We can pass any object (like list, tuple, set etc) as argument to the print() statement
"""

l = [10, 20, 30, 40]
t = [10, 20, 30, 40]
print(l)
print(t)

# print(string, variable list)
"""
We can use print() statement with String and any number of arguments
"""

s = "Crownstar"
a = 48
s1 = "Java"
s2 = "Python"
print("Hello", s, "Your Age is", a)
print("You are teaching", s1, "and", s2)

""" print(formatted string)

%i
%d
%f
%s
Syntax: print("formatted string" %(variable list))
"""

# E.g 1:

a = 10
b = 20
c = 30
print("a value is %i" %a)
print("b value is %d and c value is %d" %(b,c))

# E.g 2:

s = "Crownstar"
list = [10, 20, 30, 40]
print("Hello %s ... The List of items are %s" %(s,list))

# FORM 8: print() with replacement operator () E.g:

name = "Crownstar"
salary = 10000
gf = "Kuzzy"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name, salary, gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name, y=salary, z=gf))
