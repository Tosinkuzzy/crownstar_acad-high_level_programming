""" CONDITIONAL STATEMENTS: if condition : statement OR 
1) If:
 if condition :
   statement-1
   statement-2
   statement-3
   if condition is true then statements will be executed.
   E.g: """
   
name = input("Enter Name:")
if name=="durga" :
    print("Hello Durga Good Morning")
print("How are you!!!")

"""2) if-else:
if condition:
   Action-1
else:
   Action-2
If condition is true then Action-1 will be exwcuted otherwise Action-2 will be executed"""

name = input("Enter Name:")
if name=="durga" :
    print("Hello Durga Good Morning")
else:
    print("Hello Guest Good Morning")
print("How are you!!!")

"""3) if-elif-else:
if condition1:
   Action-1
elif condition2:
   Action-2
elif condition3:
   Action-3
elif condition4:
   Action-4
   ...
else:
   Default Action
   
Based condition the corresponding action will be executed."""

brand = input("Enter Your Favourite Brand:")
if brand=="RC" :
    print("It is childrens brand")
elif brand=="KF":
    print("It is not that much kick")
elif brand=="FO":
    print("Buy one get Free One")
else:
    print("Other Brands are not recommended")
    
""" NOTE: 
a) else part is always optional. Hence the following are various possible syntaxes
    1) if
    2) if-else
    3) if-elif-else
    4) if-elif
b) There is no switch statement in Python
  
