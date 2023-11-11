# Relational Operators
a = 10
b = 20
print("a > b is ", a > b)
print("a >= b is ", a >= b)
print("a < b is ", a < b)
print("a <= b is ", a <= b)

# Example 2
a = "mangong"
b = "mangong"
print("a > b is ", a > b)
print("a >= b is ", a >= b)
print("a < b is ", a < b)
print("a <= b is ", a <= b)

# Example 3
print(True > True)
print(True >= True)
print(10 > True)
print(False > True)
#print(10 > 'durga')

# Example 4
a = 10
b = 20
if( a > b):
    print("a is greater than b")
else:
        print("a is not greater than b")
        
''' N.B Chaining of relational operators is possibe. In the chaining, if all comparisons returns True then only result is True. If atleast one comparison returns False then the result is False '''
print(10 < 20)
print(10 < 20 < 30)
print(10 < 20 < 30 < 40)
print(10 < 20 < 30 < 40 > 50)
