"""Special Operators in python. They are Identity and Membership Operators.
b) Membership Operators are used to chech whether the given object present in the given collection is a string, List, Set, Tuple or Dict.
- In -> Returns True if the given object present in the specified Collection
- Not in -> Returns True if the given object is not present in the specified collection."""

#E.g 1
x = "hello learning Python is very easy!!!"
print('h' in x)
print('d' in x)
print('d' not in x)
print('Python' in x)

#E.g 2
list1=["sunny", "bunny", "chinny", "pinny"]
print("sunny" in list1)
print("tunny" in list1)
print("tunny" not in list1)

