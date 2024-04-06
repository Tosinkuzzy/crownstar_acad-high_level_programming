""" Comparison of Strings:
- We can use comparison operators (<, <=, >, >=) and equality operators (==, !=) for strings.
- Comparison will be performed based on alphabetical order"""

s1 = input("Enter first string:")
s2 = input("Enter Second string:")
if s1==s2:
    print("Both strings are equal")
elif s1<s2:
    print("First String is less than Second String")
else:
    print("First String is greater than Second String")
