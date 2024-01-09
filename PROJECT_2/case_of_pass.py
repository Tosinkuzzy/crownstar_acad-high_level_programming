"""
Using Case of Pass:
Sometimes in the parent class we have to declare a function with empty body and child class responsible to provide proper implementation. 
Such type of empty body we can define by using pass keyword. (It is something like abstract method in Java)
E.g: def m1(): pass
"""

for i in range(100):
    if i % 9 ==0:
        print(i)
else:pass
