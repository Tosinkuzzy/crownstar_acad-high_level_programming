"""
PROGRAM TO CALCULATE THE VALUE OF SOME CHANGE IN DOLLARS.
A QUARTER IS WORTH 25 PENNIES.
A DIME IS WORTH 10 PENNIES.
A NICKELS IS WORTH 5 PENNIES.
A PENNIES IS WORTH 1.
"""

def main():
    print("Change Counter")
    print()
    print("PLEASE ENTER THE COUNT OF EACH COIN TYPE.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("NIckels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies *.01
    print()
    print("THE TOTAL VALUE OF YOUR CHANGE IS ", total)
main()
