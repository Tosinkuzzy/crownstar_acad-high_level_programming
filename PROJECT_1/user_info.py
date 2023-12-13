"""
*****user info*****
"""

from faker import Faker
import random

# Create an instance of the data class
data = Faker()

# Generate a random number of user accounts (e.g., 10)
data_of_users = random.randint(1, 10)

for _ in range(data_of_users):
    # Generate a data username
    username = data.user_name()

    # Generate a data password
    password = data.password()

    # Generate a data email address
    email = data.email()

    # Print the user account information
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}@yahoo.com")
    print("--------")
