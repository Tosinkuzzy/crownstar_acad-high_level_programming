"""
******Regular Expressions: You can use regular expressions to validate email addresses.
*****
"""

import re
import json

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    phone_regex = r'^\d{10}$'
    return re.match(phone_regex, phone) is not None

email = str(input("ENTER MAIL ADDRESS: "))
phone = int(input("ENTER PHONE NUMBER: "))
phone, mail = "mail_phone.json"
with open('mail_phone.json', 'r') as f:
    print("READING FILE...")
    data = f.read(m, 'r')
try:
    #with open(phone, mail, 'a') as file:
    #t = file.write(f"{mails},{phone}\n")
    def write_to_file(mails, phone):
        with open('mail_phone.json', 'a') as file:
            Dt = file.write(f"{mails},{phone}\n")
except FileNotFoundError:
    print(f"The file {phone, mail} was not found.")
       continue
except PermissionError:
    print(f"You don't have permission to write to {phone, mail}.")
      continue

if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")

if validate_phone(phone):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")
