""" Logical Operators: and, or, not. We can apply for all types.
FOR BOOLEAN TYPES BEHAVIOR
and -> If both arguments are True then only result is True
or -> If atleast one argument is True the result is True
not -> Complement

True and False -> False
True or False -> True
not False -> True

FOR NON-BOOLEAN TYPES BEHAVIOR
0 means False
non-zero means True
empty string is always treated as False

x and y:
If x is evaluated to x otherwise return y

Example
10 and 20
0 and 20
If the first argument is zero then result is zero otherwise result is y

x or y:
If x evaluates to True then result is x otherwise result is y
"""
10 or 20
0 or 20
print(10 or 20)
print(0 or 20)

10 and 20
0 and 20
print(10 and 20)
print(0 and 20)

# not x: If x is evaluated to False then result is True otherwise False.
not 10
not 0
print(not 10)
print(not 0)

# project
"mangong" and "crownstar"
"" and "mangong"
"mangong" and ""
"" or "mangong"
"mangong" or ""
not ""
not "mangong"
print("mangong" and "crownstar")
print("" and "mangong")
print("mangong" and"")
print("" or "mangong")
print("mangong" or "")
print(not "")
print(not "mangong")
