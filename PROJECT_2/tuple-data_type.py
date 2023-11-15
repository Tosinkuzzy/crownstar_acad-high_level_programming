""" WAP with the tuple data type which is exactly same as list data type except that it is immutable.
 i.e we cannot change values.
Tuple elements can be represented within parenthesis. E.g
"""

t = (10, 20, 30, 40)
print(type(t))
#t[0] = 100
#t.append("Almighty")
#AttributeError; 'tuple' object has no attribute 'append'
#t.remove(10)
#AttributeError: 'tuple' object has no attribute 'remove'
#print(t[0])
#print(t.append)
#print(t.remove)

# NOTE: tuple is the read only version of list
