""" Removing Spaces from the string:
We can use the following 3 methods
- rstrip() -> To remove spaces at right hand side
lstrip() -> To remove spaces at left hand side
strip() -> To remove spaces both sides"""

city = input("Enter your city Name:")
scity = city.strip()
if scity=='Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("Your entered city is invalid")
