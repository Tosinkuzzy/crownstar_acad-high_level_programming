""" TRANSFER STATEMENTS
1) break:
We can use break statement inside loops to break loop execution based on some condition."""

for i in range(10):
    if i==7:
        print("Processing is enough..plz break")
        break
    print(i)

# E.g 1

cart=[10, 20, 600, 60, 70]
for item in cart:
    if item>500:
        print("To place this order insurance must be required")
        break
    print(item)
    
    """ Continue:
    We can use continue statement to skip current iteration and continue next iteration
    E.g 1: To print odd numbers in the range 0 to 9"""
    
    for i in range(10):
        if i%2==0:
            continue
        print(i)
        
# E.g 2:

cart=[10, 20, 500, 700, 50, 60]
for item in cart:
    if item>=500:
        print("We cannot process this item :",item)
        continue
    print(item)
    
# E.g 3:

numbers=[10, 20, 0, 5, 0, 30]
for n in numbers:
    if n==0:
        print("Hey how we can divide with zero..just skipping")
        continue
    print("100/{} = {}".format(n,100/n))
