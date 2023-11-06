# WAP that uses complex data type.
# N.B A complex number has real and imaginary parts
# 'a' and 'b' contain intergers Or Floating Point Values
# In the REAL PART, if we use int value then we can specify that either by decimal, octal, binary or hexa decimal form
# In the IMAGINARY PART should be specified only by using decimal form
# If we run this code, our value a will not give us a syntax error but our value b will give.
a = 0B11+5j
b = 3+0B11j
print(a)
print(b)

# We can perform operations on complex typr values

x = 10+1.5j
y = 20+2.5j
z = x+y
print(z)
type(z)

# Complex data type has some inbuilt attributes to retrive the real part and imaginary part
# N.B We can use complex type generally in scientific Applications and electrical engineering Applications
c = 10.5+3.6j

c.real => 10.5
c.imag => 3.6
# If we want to print this code above, we just need to add the command print(c).
