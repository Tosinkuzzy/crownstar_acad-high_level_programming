"""
****Tons generator***
"""

from faker import Faker
import random

# Define a list of credit card types
credit_card_types = ["Visa", "MasterCard", "Discover", "Amex"]

# Create an instance of the Faker class
fake = Faker()

# Generate a random number of credit card details (e.g., 10)
number_of_cards = random.randint(1, 10)

for _ in range(number_of_cards):
    # Choose a random credit card type
    credit_card_type = random.choice(credit_card_types)

    # Generate a random credit card number
    if credit_card_type == "Visa":
        credit_card_number = fake.credit_card_number(card_type="visa")
    elif credit_card_type == "MasterCard":
        credit_card_number = fake.credit_card_number(card_type="mastercard")
    elif credit_card_type == "Discover":
        credit_card_number = fake.credit_card_number(card_type="discover")
    elif credit_card_type == "Amex":
        credit_card_number = fake.credit_card_number(card_type="amex")

    # Generate a random expiration date
    expiration_date = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

    # Generate a random credit card CVV
    credit_card_cvv = fake.credit_card_provider(card_type=credit_card_type.lower())[-3:]

    # Print the credit card details
    print(f"Credit Card Type: {credit_card_type}")
    print(f"Credit Card Number: {credit
