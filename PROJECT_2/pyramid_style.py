# WAP to display *'s in Pyramid Style (Also Known as Equivalent Triangle)

n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    print("" * (n-i),end="")
    print("* "*i)

