# WAP that uses oct() to convert from any base to octal
# If you look at my previous codes with bin() you will see that I used two other methods to come out with the same code. You can refer to the previous code and implement here.
# Looking at this code below, I just invented another method to print out the output on one line.
x = oct(10)
y = oct(0B1111)
z = oct(0X123)
print(x,y,z)

# If I use the same code above and print out the output on several/different lines.
x = oct(10)
y = oct(0B1111)
z = oct(0X123)
print(x)
print(y)
print(z)
