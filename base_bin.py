# WAF that can use bin() to convert from any base to binary
# When we run this code, the output will not be printed to the console.
a = bin(15)
'0b1111'
b = bin(0o11)
'0b1001'
c = bin(0X10)
'0b10000'

# Here is another way to write our code which will get the output printed to the console.
a = bin(15)
b = bin(0o11)
c = bin(0X10)
print(a)
print(b)
print(c)

# With the code written below, you will discover that if you run it the output will be printed in the console because we have used the command print.
a = bin(15)
print('0b1111')
b = bin(0o11)
print('0b1001')
c = bin(0X10)
print('0b10000')


