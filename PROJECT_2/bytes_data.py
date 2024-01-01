"""WAF that uses bytes data type to represent a group of byte numbers just like an array.
Write Python 3 code in this online editor and run it.
"""
x = [10, 20, 30, 40]
b = bytes(x)
type(b)
print(b[0])
print(b[1])
print(b[2])
print(b[-1])
for i in b : print(i) # This line of code bring an error

# Conclusion 1: The only allowed values for byte data type are 0 to 256. By mistake if we are trying to provide any other values then we will get value error.
# Conclusion 2: Once we create bytes data type value, we cannot change its values, otherwise we will get TypeError. E.G

x = [10, 20, 30, 40]
b = bytes(x)
b[0] = 100
print(b[1]) # Output is TypeError: 'bytes' object does not support item assignment
