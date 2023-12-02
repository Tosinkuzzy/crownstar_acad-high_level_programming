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
    gift_card_balance = random.uniform(1, 10000)

    # Generate a random gift card expiration date
    #gift_card_expiration_date = fake.date_between(start_date="today", end_date="+10y", date_format="%m/%d/%Y")
    #formatted_date = gift_card_expiration_date.strftime("%m/%d/%Y")
    # Generate a random date between today and 10 years from now
    gift_card_expiration_date = fake.date_between(start_date="today", end_date="+10y")

    # Format the date object as a string in the desired format
    formatted_date = gift_card_expiration_date.strftime("%m/%d/%Y")
    filename = "giftcard.txt"
    with open('giftcard.txt', 'r') as f:
        for line in f:
            card_number = line.strip() 
    try:
        with open(filename, 'a') as file:
            wt = file.write(f"{giftcard_card_number},{gift_card_balance},{gift_card_expiration_date}\n")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        continue
    except PermissionError:
        print(f"You don't have permission to write to {filename}.")
        continue
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        continue
    print(formatted_date)

    # Print the gift card details
    print(f"Gift Card Number: {gift_card_number}")
    print(f"Gift Card Balance: ${gift_card_balance:.2f}")
    print(f"Gift Card Expiration Date: {gift_card_expiration_date}")
    print("-" * 50)
