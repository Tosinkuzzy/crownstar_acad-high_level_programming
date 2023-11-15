# WAF to represent a group of values as a single entity where insertion order is required to preserve and duplicates are allowed. (Use list data type)
# a. Insertion order is preserved
# b. Heterogeneous Objects are allowed
# c. Duplicates are allowed
# d. Growable in nature
# e. Values should be enclosed within square brackets

list = [10, 20, 30, 40]
list[0]
list[-1]
list[1:3]
list[0] = 100
for i in list : print(i)
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# The list is growable in nature. i.e based on our requirement we can increase or decrease the size.

list = [10, 20, 30]
list.append("Crownstar")
list.remove(20)
list2 = list * 2
print(list.append)
print(list)
print(list.remove)
print(list)
print(list2)
print(list2)

# NOTE: An ordered, mutable, hererogenous collection of elements is nothing but list, where duplicates also allowed.
