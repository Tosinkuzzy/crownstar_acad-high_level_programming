"""
*****Luhn Algorithm: This algorithm checks the validity of credit card numbers. 
Here is a Python code snippet that uses the Luhn Algorithm to validate credit card numbers:
*******
"""

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    nums = digits_of(card_number)
    check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])
    return check_sum % 10 == 0

card_number = "4532015112830361"
if luhn_check(card_number):
    print("The credit card number is valid.")
else:
    print("The credit card number is not valid.")
