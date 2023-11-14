# Relational Operators
a = 10
b = 20
print("a > b is ", a > b)
print("a >= b is ", a >= b)
print("a < b is ", a < b)
print("a <= b is ", a <= b)

# Project 2
""" passing float to the variables,
using if_elif_else chain to verify,
relational operators. """

a = 34.7
b = 32.66
if a > b:
	print("Tosinkuzzy Payment Confirmed.")
elif a >= b:
	print("Order Pending Payment.")
elif a < b:
	print("Mangong Payment Confirmed.")
else:
	print("NO PENDING PAYMENT.")

# Project 3
a = 10
b = 20
if(a > b):
    print("a is greater than b")
else:
        print("a is not greater than b")
        
"""N.B Chaining of relational operators is possibe. In the chaining,
 if all comparisons returns True then only result is True. 
If atleast one comparison returns False then the result is False. """
print(10 < 20)
print(10 < 20 < 30)
print(10 < 20 < 30 < 40)
print(10 < 20 < 30 < 40 > 50)
