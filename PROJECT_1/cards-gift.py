from faker import Faker
import random

# Create an instance of the class
data_generator = Faker()

# Generate a number of gift card details (e.g., 10)
number_of_gift_cards = random.randint(1, 100)

# Initialize a list to store existing card numbers
existing_card_numbers = []

# Read existing card numbers from the file if it exists
try:
    with open('giftcard.csv', 'r') as f:
        for line in f:
            card_number = line.strip().split(',')[0]  # Assuming CSV format
            existing_card_numbers.append(card_number)
except FileNotFoundError:
    print("The file giftcard.txt was not found. A new file will be created.")

for _ in range(number_of_gift_cards):
    # Generate gift card number
    gift_card_number = data_generator.bban()

    # Check if the generated card number already exists
    if gift_card_number in existing_card_numbers:
        print(f"Card number {gift_card_number} already exists. Skipping.")
        continue  # Skip this iteration and generate a new card number

    # Generate gift card balance
    gift_card_balance = random.uniform(1, 100)

    # Generate gift card expiration date
    gift_card_expiration_date = data_generator.date_between(start_date="today", end_date="+10y")

    # Format the date object as a string in the desired format
    formatted_date = gift_card_expiration_date.strftime("%m/%d/%Y")

    # Append the new gift card details to the file
    try:
        with open('giftcard.txt', 'a') as file:
            file.write(f"{gift_card_number},\t\t\t${gift_card_balance},\t\t\t{formatted_date}\n")
    except PermissionError:
        print(f"You don't have permission to write to giftcard.txt.")
        break  # Exit the loop as we can't write to the file
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break  # Exit the loop as an unexpected error occurred

    # Print the gift card details
    print(f"Gift Card Number: {gift_card_number}")
    print(f"Gift Card Balance: ${gift_card_balance:.2f}")
    print(f"Gift Card Expiration Date: {formatted_date}")
    print("-" * 50)

