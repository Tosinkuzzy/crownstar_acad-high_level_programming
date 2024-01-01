"""Equality Operators: ==, !=. 
We can apply these operators for any type even for incompatible types also."""
10 == 20
10 != 20
10 == True
False == False
"mangong" == "mangong"
10 == "mangong"
print(10 == 20)
print(10 != 20)
print(10 == True)
print(False == False)
print("mangong" == "mangong")
print(10 == "mangong")

"""N.B Changing concept is applicable for equality operators. 
If at least one comparison returns False then the result is False. 
Otherwise the result is True.
"""

10 == 20 == 30 == 40
10 == 10 == 10 == 10
print(10 == 20 == 30 == 40)
print(10 == 10 == 10 == 10)
