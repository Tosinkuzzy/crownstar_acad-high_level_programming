"""
******Regular Expressions: You can use regular expressions to validate email addresses.
*****
"""

import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    phone_regex = r'^\d{10}$'
    return re.match(phone_regex, phone) is not None

email = "example@email.com"
phone = "1234567890"

if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")

if validate_phone(phone):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")
