"""
PROGRAM TO CALCULATE THE VALUE OF SOME CHANGE IN DOLLARS.
A QUARTER IS WORTH 25 PENNIES.
A DIME IS WORTH 10 PENNIES.
A NICKELS IS WORTH 5 PENNIES.
A PENNIES IS WORTH 1.
"""

def main():
    print("Dollar Change Counter")
    print()
    print("Please enter the count OF each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("NIckels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies *.01
    print()
    print("The total value of your change is", total)
main()
