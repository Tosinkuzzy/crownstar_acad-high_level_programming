"""
*****gift cards generator*****
"""

from faker import Faker
import random

# Create an instance of the Faker class
fake = Faker()

# Generate a random number of gift card details (e.g., 10)
number_of_gift_cards = random.randint(1, 10)

for _ in range(number_of_gift_cards):
    # Generate a random gift card number
    gift_card_number = fake.bban()

    # Generate a random gift card balance
    gift_card_balance = random.uniform(1, 1000)

    # Generate a random gift card expiration date
    gift_card_expiration_date = fake.date_between(start_date="today", end_date="+10y", date_format="%m/%d/%Y")

    # Print the gift card details
    print(f"Gift Card Number: {gift_card_number}")
    print(f"Gift Card Balance: ${gift_card_balance:.2f}")
    print(f"Gift Card Expiration Date: {gift_card_expiration_date}")
    print("-" * 50)
