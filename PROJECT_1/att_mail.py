"""
****att mails****
"""

from faker import Faker
import random

# Create an instance of the Faker class
fake = Faker()

# Generate a random number of email addresses (e.g., 10)
number_of_emails = random.randint(1, 10)

for _ in range(number_of_emails):
    # Generate a random first name
    first_name = fake.first_name()

    # Generate a random last name
    last_name = fake.last_name()

    # Generate a random AT&T email address
    att_email = f"{first_name}.{last_name}@att.com"

    # Print the AT&T email address
    print(att_email)
