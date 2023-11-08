# WAP that can be used to slice strings
# N.B SLICE means a piece.
# [] is called slice operator (used to retrive part of strings)
# In python, strings follow zero based index. The index can either be +ve or -ve. +ve means forward direction from Left to Right. -ve means backward direction from Right to Left
s = "Mangong"
s[0]
s[1]
s[-1]
s4[40]
print(s)
print(s[0])
print(s[1])
print(s[-1])
print(s4[40])

# Looking at the code above, lines 9 and 14 will give an error because 40 is out of range of number of strings given by the user
# Study the codes bellow
s = "Mangong"
s[1:40]
s[1:]
s[:4]
s[:]
s*3
len(s)
print(s)
print(s[1:40])
print(s[1:])
print(s[:4])
print(s*3)
print(len("Mangong"))

# In py we can represent char values also by using str type and explicitly char type is not available. This code bellow isn't to be runned

c ='a'
type(c)
<class 'str'>
