print("CREDIT CARD VALIDATION LOADING.....")

# Function to check if the card number is valid using the Luhn algorithm
def luhn_check(card_number):
    # Function to convert a number into a list of its digits
    def digits_of(n):
        return [int(d) for d in str(n)]

    # Convert the card number into a list of its digits
    nums = digits_of(card_number)
    # Calculate the checksum using the Luhn algorithm
    check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])   
    # The card number is valid if and only if the checksum modulo 10 is equal to 0
    return check_sum % 10 == 0

# Function to get the issuer of the card based on its first digit
def get_card_issuer(card_number):
    first_digit = str(card_number)[0]
    if first_digit == '3':
        return 'AMERICA EXPRESS/DINERS CLUB'
    elif first_digit == '4':
        return 'VISA'
    elif first_digit == '5':
        return 'MASTERCARD'
    elif first_digit == '6':
        return 'DISCOVER CARD'
    else:
        return 'UNKNOWN'

# Specify the filename
filename = "credit_card.txt"

# Main loop
while True:
    # Get input from user
    card_number = input("ENTER CARD NUMBER (OR 'Q' TO QUIT): ")
    if card_number.lower() == 'Q':
        break
    else:
        card_number = int(card_number)

    cvv = input("ENTER CVV: ")
    expiry_date = input("ENTER EXPIRY DATE (MM/YY): ")
    issuer = get_card_issuer(card_number)

    try:
        # Open the file in append mode ('a')
        with open(filename, 'a') as file:
            # Write the user input to the file
            wt = file.write(f"{card_number},{cvv},{expiry_date},{issuer}\n")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        continue
    except PermissionError:
        print(f"You don't have permission to write to {filename}.")
        continue
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        continue

    print("VALIDATING CARD...")

    # Check if the card number is valid
    if luhn_check(card_number):
        print(f"THE {issuer} CREDIT CARD NUMBER IS VALID.")
    else:
        print(f"THE {issuer} CREDIT CARD NUMBER IS NOT VALID.")

print("EXITING PROGRAM....")

