"""
***real datas***
"""

import random
import string

def generate_card_number():
    digits = ''.join(random.choice(string.digits) for _ in range(16))
    return digits[:6] + '-' + digits[6:11] + '-' + digits[11:16]

def generate_expiry_date():
    current_year = str(datetime.now().year)
    year = str(random.randint(int(current_year[2:]), int(current_year) + 20))
    month = str(random.randint(1, 12)).zfill(2)
    return month + '/' + year[2:]

def generate_cvv():
    return str(random.randint(100, 999))

def generate_credit_card_info():
    card_number = generate_card_number()
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()
    return card_number, expiry_date, cvv

card_number, expiry_date, cvv = generate_credit_card_info()
print("Card Number:", card_number)
print("Expiry Date:", expiry_date)
print("CVV:", cvv)
