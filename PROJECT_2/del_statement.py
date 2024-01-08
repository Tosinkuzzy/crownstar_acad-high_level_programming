""" del statement:
- del is a keyword in Python
- After using a variable, it is highly recommended to delete that variable if it is no longer required, so that the corresponding object is eligible for Garbage Collection.
- We can delete variable by using del keyword"""

x = 10
print(x)
del x

""" After deleting a variable we cannot access that variable otherwise we will get NameError. SEE BELOW.
x = 10
del x
print(x)

NOTE: We can delete variables which are pointing to immutable objects. But we cannot delete the elements present inside immutable object.

s = "durga"
print(s)
del s -> valid
del s[0] -> TypeError: 'str' object doesn't support the deletion """
