"""
*****user info*****
"""

from faker import Faker
import random

# Create an instance of the Faker class
fake = Faker()

# Generate a random number of user accounts (e.g., 10)
number_of_users = random.randint(1, 10)

for _ in range(number_of_users):
    # Generate a random username
    username = fake.user_name()

    # Generate a random password
    password = fake.password()

    # Generate a random email address
    email = fake.email()

    # Print the user account information
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print("--------")
