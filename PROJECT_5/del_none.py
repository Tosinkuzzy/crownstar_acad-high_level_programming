""" 
Difference between del and None:
In the case del, the variable will be removed and we cannot access that variable(unbind operation)

s = "durga"
del s
print(s)
NOTE: This code above will produce an error.

But in the case of None assignment the variable won't be removed but the corresponding object is eligible for Garbage Collection (re bind operation). 
Hence after assigning with None value, we can access that variable.
"""

s = "crownstar"
s = None
print(s)

"""
Pattern-1: To print given number of *s in a row
test.py
"""

n = int(input('Enter n value:'))
for i in range(n):
    print('*',end='')
    
"""
Pattern-2: To print square pattern with * symbols
test.py
"""

n = int(input('Enter No Of Rows:'))
for i in range(n):
    print('* '*n)
    
"""
Pattern-3: To print square pattern with provided fixed digit in every row
test.py
"""

n = int(input('Enter No Of Rows:'))
for i in range(n):
    print((str(i+1)+'')*n)
    
"""
Pattern-4: To print square pattern with alphabet symbols
test.py
"""

n = int(input('Enter No Of Rows:'))
for i in range(n):
    print((chr(65+i)+'')*n)
    
"""Pattern-5: To print Right Angle Triangle pattern with * symbols
test.py"""

n = int(input('Enter No Of Rows:'))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
        print()
       
"""Pattern-6: To print inverted Right Angle Triangle pattern with * symbols.
test.py"""

n = int(input('Enter No Of Rows:'))
for i in range(n):
    print('* '*(n-i))
    
""" Pattern-7: To print Pyramid pattern with * symbols
test.py"""

n = int(input('Enter Number of rows:'))
for i in range(n): # 0, 1, 2, 3
    print((''*(n-i-1))+('* ')*(i+1))
    
""" Pattern-8: To print Inverted Pyramid Pattern with * symbols
test.py"""

n = int(input('Enter Number of Rows:'))
for i in range(n): #0, 1, 2, 3
    print(''*i+'* '*(n-i))
    
""" Pattern-9: To print Diamond Pattern with * symbols
test.py"""

n = int(input('Enter n Value:'))
for i in range(n): #0, 1, 2, 3
    print(''*(n-i-1)+'* '*(i+1))
for i in range(n-1):#0, 1, 2
    print(''*(i+1)+'* '*(n-i-1))


