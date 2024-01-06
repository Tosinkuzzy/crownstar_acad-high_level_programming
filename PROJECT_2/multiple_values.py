#How to read multiple values from the keyboard in a single line

a , b=[int(x) for x in input("Enter 2 numbers:").split()]
print("Product is:", a * b)

#NOTE: split() function can take space as seperator by default. But we can pass anything as separator.
