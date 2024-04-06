#!/usr/bin/env python3

""" 
Removing Spaces from the string:
We can use the following 3 methods
- rstrip() -> To remove spaces at right hand side
lstrip() -> To remove spaces at left hand side
strip() -> To remove spaces both sides
"""

city = input("Enter your city Name: ")
scity = city.strip()
if scity=='Abuja':
    print("Hello Abuja..Beri")
elif scity=='Lagos':
    print("Hello Lagos...Tosinkuzzy")
elif scity=="Ondo":
    print("Hello Ondo...Toy")
else:
    print("Your entered city is invalid")
