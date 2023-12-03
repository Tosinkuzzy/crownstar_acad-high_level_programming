import re

# Function to validate an email address using a regular expression
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Function to validate a phone number with a country code using a regular expression
def validate_phone(phone):
    # This regex will match a phone number that starts with a '+' followed by the country code and 10 digits
    phone_regex = r'^\+\d{1,3}\d{10}$'
    return re.match(phone_regex, phone) is not None

# Prompt the user to enter an email address
email = input("ENTER MAIL ADDRESS: ")
# Prompt the user to enter a phone number with a country code
phone = input("ENTER PHONE NUMBER WITH COUNTRY CODE: ")

# Validate the email and phone number
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")

if validate_phone(phone):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")

# If both the email and phone number are valid, proceed to write them to the file
if validate_email(email) and validate_phone(phone):
    try:
        # Attempt to open the file in append mode and write the email and phone number
        with open('mail_phone.json', 'a') as file:
            file.write(f"{email},{phone}\n")
    except FileNotFoundError:
        # If the file is not found, inform the user
        print(f"The file mail_phone.json was not found.")
    except PermissionError:
        # If there is a permission error, inform the user
        print(f"You don't have permission to write to mail_phone.json.")
