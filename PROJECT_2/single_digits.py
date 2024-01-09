""" WAP to take a single digit number from the key board and print its value in English Word?
0 -> ZERO
1 -> ONE
"""

n = int(input("Enter a digit from 0 to 9:"))
if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")
