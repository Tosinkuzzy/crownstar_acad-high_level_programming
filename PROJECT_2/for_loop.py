""" ITERATIVE STATEMENTS:
- If we want to execute a group of statements multiple times then we should go for iterative statements.
- Python supports 2 types of iterative statements.
a) For Loop
b) While Loop

    1) FOR LOOP:
If we want to execute some action for every element present in 
sequence (it may be string or collection) then we should go for 
for loop.
        syntax: for x in sequence:
                Body
Where sequence can be string or any collection
Body will be executed for every element present in the sequence.

E.g 1: To print characters present in the given string """

s = "Sunny Leone"
for x in s :
    print(x)
    
"""
E.g 2: To print characters present in string index wise:"""

s = input("Enter some String:")
i=0
for x in s :
    print("The character present at ",i,"index is :",x)
    i=i+1
    
# E.g 3: To print Hello 10 times

for x in range(10):
    print("Hello")
    
# E.g 4: To display numbers from 0 to 10

for x in range(11):
    print(x)
    
# E.g 5: To display odd numbers from 0 to 20

for x in range(21):
    if(x%2!=0):
      print(x)
    
# E.g 6: To display numbers from 10 to 1 in descending order

for x in range(10,0,-1):
    print(x)
    
# E.g 7: To print sum of numbers present inside list

list = eval(input("Enter List:"))
sum=0;
for x in list:
    sum=sum+x;
    print("The Sum=",sum)
