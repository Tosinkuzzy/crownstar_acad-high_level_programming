"""
2) WHILE LOOP
- If we want to execute a group of statemtments iteratively until some is condition false, then we should go for while loop.

Syntax: while condition :
        body

To print numbers from 1 to 10 by using while loop
"""

x = 1
while x <= 10:
    print(x)
x = x + 1

# To display the sum of first n numbers

n = int(input("Enter number:"))
sum=0
i = 1
while i < n:
    sum = sum + 1
    i = i + 1
print("The sum of first",n, "numbers is:",sum)

# WAP to prompt user to enter some name until entering Durga

name = ""
while name != "tosinkuzzy":
    name = input("Enter Name: ")
print("Thanks for confirmation!")
