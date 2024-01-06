""" Ternary or Conditional Operation. Syntax: x = firstValue if condition else secondValue. If condition is True then firstValue will be considered else secondValue will be considered."""
a , b = 10, 20
x = 30 if a < b else 40
#print(x)

#E.g 2 Read two numbers from the keyboard and print minimum value

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
min = a if a < b else b
print("Minimum Value:", min)
