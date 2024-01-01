"""WAF that uses bytearray which is exactly the same as bytes data type except that its elements can be modified."""
# Project 1:
x = [10, 20, 30, 40]
b = bytearray(x)
for i in b : print(i) # This line of code will bring an error
print(b[0])
print(b[1])
print(b[2])
print(b[3])
b[0] = 100
for i in b : print(i) # This line of code will bring an error
# print(b[100]) -> error
print(b[1])
print(b[2])
print(b[3])

# Project 2:
x = [10, 25]#_> try with a different integer
b = bytearray(x)
#ValueError: byte must be in range(0, 256)
