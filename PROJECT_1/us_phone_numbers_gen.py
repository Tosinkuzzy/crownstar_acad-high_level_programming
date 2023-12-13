"""
This approach still uses the same technique as the previous solution, 
but it is more efficient because it only generates valid phone numbers. 
It should be noted, however,
that this approach still generates a very large number of phone numbers, 
which could take a significant amount of time and memory to compute.
"""

import itertools
import re
import random

def generate_valid_us_phone_number():
    while True:
        phone_number = ''.join(random.choice('1234567890') for _ in range(10))
        if validate_phone_number(phone_number):
            return phone_number

def validate_phone_number(phone_number):
    phone_regex = r'^\d{10}$'
    return re.match(phone_regex, phone_number) is not None

def generate_valid_us_phone_numbers(n):
    return [generate_valid_us_phone_number() for _ in range(n)]

valid_us_phone_numbers = generate_valid_us_phone_numbers(5)
print("Valid US Phone Numbers:", valid_us_phone_numbers)

