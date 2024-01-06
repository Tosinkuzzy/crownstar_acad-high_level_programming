"""Special Operators in python. They are Identity and Membership Operators.
a) Identity Operators are used for comparison. i.e is and is not.
- r1 is r2 returns True if both r1 and r2 are pointing to the same object
- r1 is not r2 returns True if both r1 and r2 are not pointing to the same object"""

#E.g 1
a = 10
b = 10
print(a is b)
x = True
y = True
print(x is y)

#E.g 2
a = "durga"
b = "durga"
print(id(a))
print(id(b))
print(a is b)

#E.g 3
list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)

#NOTE: We can use is operator for address comparison where as == operator for content comparison.
