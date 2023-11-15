# WAP to represent a group of values without duplicates where order is not important (then we should go for set Data type).
# a. Insertion order is not preserved
# b. Duplicates are not allowed
# c. Heterogeneous objects are allowed
# d. Index concept is not applicable
# e. It is mutable collection
# f. Growable in nature

s = {100, 0, 10, 200, 10, 'crownstar'}
s # {0, 100, 'crownstar', 200, 10}
#s[0] -> TypeError: 'set' object does not support indexing

# set is growable in nature, based on our requirement we can increase or decrease the size.

s.add(60)
s
s.remove(100)
s
print(s.add)
print(s)
print(s.remove)
print(s)

# Try doing the same code above and print it out this way to see the output
s.add(60)
s
#s.remove(100)
s
print(s.add(60))
print(s)
#print(s.remove(100))
print(s)
