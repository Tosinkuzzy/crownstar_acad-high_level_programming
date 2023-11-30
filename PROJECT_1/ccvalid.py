"""
*****Luhn Algorithm: This algorithm checks the validity of credit card numbers. 
Here is a Python code that uses the Luhn Algorithm to validate credit card numbers:
*******
"""
print("CREDIT CARD VALIDATION LOADING.....")

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    nums = digits_of(card_number)
    check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])
    return check_sum % 10 == 0

card_number = int(input("ENTER CARD NUMBER: "))
status = print("VALIDATING CARD...")
if luhn_check(card_number):
    print("THE CREDIT CARD NUMBER IS VALID.")
else:
    print("THE CREDIT CARD NUMBER IS NOT VALID.")

print("DONE!")
