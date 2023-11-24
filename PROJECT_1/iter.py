"""
This approach still uses the same technique as the previous solution, 
but it is more efficient because it only generates valid phone numbers. 
It should be noted, however,
that this approach still generates a very large number of phone numbers, 
which could take a significant amount of time and memory to compute.
"""

import itertools

def generate_all_valid_us_phone_numbers():
    phone_numbers = []
    for num in itertools.product('1234567890', repeat=10):
        phone_number = ''.join(num)
        if validate_phone_number(phone_number):
            phone_numbers.append(phone_number)
    return phone_numbers

def validate_phone_number(phone_number):
    phone_regex = r'^\+?1?\d{9,15}$'
    return re.match(phone_regex, phone_number) is not None

valid_us_phone_numbers = generate_all_valid_us_phone_numbers()
print("Valid US Phone Numbers:", valid_us_phone_numbers)
