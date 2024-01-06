# Program for maximum of 3 numbers

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
min = a if a > b and a > c else b if b > c else c
print("Maximum Value:", max)

#E.g:

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
print("Both numbers are equal" if a==b else "First Number is Less than Second Number" if a < b else "First Number Greater than Second Number")
