# WAP where range Data Type represents a sequence of numbers.
# The elements present in range Data type are not modifiable. i.e range Data type is immutable
# Form-1: range(10)
# generate numbers from 0 to 9

r = range(10)
for i in r : print(i)
print(r)

# Form-2: range (10, 20)
# generate numbers from 10 to 19

r = range(10, 20)
for i in r : print(i)
print(r)

# Form-3: range(10, 20, 2)
# 2 means in increment value

r = range(10, 20, 2)
for i in r : print(i)
print(r)

# We can access elements present in the range Data Type by using index
r = range(10, 20)
r[0]
#r[15] # IndexError: range object index out of range

# We cannot modify the values of range data type
#r[0] = 100
#TypeError: 'range' object does not support item assignment

# We can create a list of values with range data type

I = list(range(10))
print(I)
