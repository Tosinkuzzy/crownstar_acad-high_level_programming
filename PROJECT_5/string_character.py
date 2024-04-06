#!/usr/bin/env python3

""" 
WAP to access each character of string in forward and backward direction by using while loop
"""

s = "Learning Python is very easy!!!"
n = len(s)
i = 0
print("Forward direction")
while i < n:
    print(s[i], end='')
    i += 1
print("Backward direction")
i = -1
while i >= -n:
    print(s[i], end='')
    i = i - 1
    
# Alternative ways:

s = "Learning Python is very easy!!!"
print("Forward direction")
for i in s:
    print(i, end='')
print("Forward direction")
for i in s[::]:
        print(i, end='')
        
print("Backward direction")
for i in s[::-1]:
    print(i, end='')
