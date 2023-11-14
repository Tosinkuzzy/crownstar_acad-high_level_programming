""" WAF that shows fundamental data types vs immutability.
 All fundamental data types are immutable.
 Ones we create an object, we cannot perform any changes in that object.
 In py, if a new obj is required, the PVM{python virtual machine} won't create object immediatly.
 First it will check if any obj is available with required content.
 If any then existing obj will be reused.
 If it is not available then only a new obj will be created.
 The adv of this approach is memory utilization and performance will be improved.
But the prob in this approach is, several references pointing to the same object,
 by using one reference if we are allowed to change the content in the existing object then the remaining references will be affected.
 To prevent immutability concept is required. 
According to this, once creates an object we are not allowed to change content.
 If we are trying to change with those changes a new object will be created.
"""
a = 10
b = 10
id(a)#_> to check obj identity
id(b)
a is b
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)

a = 10+5j
b = 10+5j
a is b
id(a)
id(b)
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

a = True
b = True
a is b
id(a)
id(b)
print(a)
print(b)
print(id(a))
print(id(b))

a = 'Crownstar'
b = 'Godson'
a is not b
id(a)
id(b)
print(a)
print(b)
print(a is not b)
print(id(a))
print(id(b))
