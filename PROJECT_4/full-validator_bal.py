import json

print("CREDIT CARD VALIDATION LOADING.....")

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    nums = digits_of(card_number)
    check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])
    return check_sum % 10 == 0

def get_card_issuer(card_number):
    first_digit = str(card_number)[0]
    if first_digit == '3':
        return 'AMERICAN EXPRESS/DINERS CLUB'
    elif first_digit == '4':
        return 'VISA'
    elif first_digit == '5':
        return 'MASTERCARD'
    elif first_digit == '6':
        return 'DISCOVER CARD'
    else:
        return 'UNKNOWN'

def get_card_balance(card_number):
    with open('balances.json', 'r') as f:
        balances = json.load(f)
    return balances.get(str(card_number), "Balance not found")

filename = "c-d_card.txt"
with open('c-d_card.txt', 'r') as f:
    for line in f:
        card_number = line.strip() 
	 # Remove any trailing newline
        # Now you can process the card_number


while True:
    card_number = input("ENTER CARD NUMBER (OR 'Q' TO QUIT): ")
    if card_number.lower() == 'Q':
        break
    else:
        card_number = int(card_number)
        cvv = input("ENTER CVV: ")
        expiry_date = input("ENTER EXPIRY DATE (MM/YY): ")
        issuer = get_card_issuer(card_number)
        balance = get_card_balance(card_number)
        print(f"The balance on this card is {balance}")

    try:
        with open(filename, 'a') as file:
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

    if luhn_check(card_number):
        print(f"THE {issuer} CREDIT CARD NUMBER IS VALID.")
    else:
        print(f"THE {issuer} CREDIT CARD NUMBER IS NOT VALID.")

print("EXITING PROGRAM....")

