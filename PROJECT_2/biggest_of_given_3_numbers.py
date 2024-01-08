# WAP to find Biggest of given 3 Numbers from the Command Prompt

n1 = int(input("Enter First Number:"))
n2 = input(input("Enter Second Number:"))
n3 = input(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggest Number is:",n3)
    
