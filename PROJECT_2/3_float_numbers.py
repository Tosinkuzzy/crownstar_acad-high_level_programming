"""WAP to read 3 float numbers from the keyboard with, seperator and print their sum."""

a,b,c = [float(x) for x in input("Enter 3 float numbers:").split(',')]
print("The Sum is:", a + b + c)

#eval(): eval Function take a String and evaluate the Result.
#E.g 1
x = eval("10 + 20 + 30")
print(x)

#E.g 2
x = eval(input("Enter Expression"))
print(10 + 2 * 3 / 4)

#NOTE: eval() can evaluate the input to list, tuple, set etc based the provided input
#E.g 3 WAP to accept list from the keyboard on the display

l = eval(input("Enter List"))
print(type(l))
print(l)

