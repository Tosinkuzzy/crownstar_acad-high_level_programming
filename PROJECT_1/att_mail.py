"""Generating att mails using Fname, Lname"""
print("#" * 25)
print("AT&T VALIDATED MAIL LOADING ",'.' * 7)

from faker import Faker
import random

# Create an instance of the Faker class
fake = Faker()

# Generate number of email addresses (e.g., 10)
number_of_emails = random.randint(1, 10)

for _ in range(number_of_emails):
	# Generate Fname
	att_first_name = fake.name()
	ameritech_first_name = fake.name()
	bellsouth_first_name = fake.name()
	nvbell_first_name = fake.name()
	sbcglobal_first_name = fake.name()

	# Generate Lname
	att_last_name = fake.name()
	ameritech_last_name = fake.name()
	bellsouth_last_name = fake.name()
	nvbell_last_name = fake.name()
	sbcglobal_last_name = fake.name()

	# Generate a number to mail
	att = random.randint(1, 24)
	ameritech = random.randint(23, 55)
	bell = random.randint(32, 65)
	nvbell = random.randint(40, 76)
	sbc = random.randint(43, 86)
	

	# Generate AT&T email address
	att_mail = f"{att_first_name}.{att_last_name}{att}@att.net"
	ameritech_mail = f"{ameritech_first_name{ameritech}}.{last_name}@ameritech.net"
	bellsouth_mail = f"{bellsouth_first_name}{{bell}bellsouth_last_name}@bellsouth.net"
	nvbell_mail = f"{nvbell_first_name}.{nvbell_last_name}{nvbell}@nvbell.net"
	sbcglobal_mail = f"{sbcglobal_first_name}{sbc}{sbcglobal_last_name}@sbcglobal.net"

	# Print the AT&T email address
	print(att_mail)
	print(nvbell_mail)
	print(ameritech_mail)
	print(bellsouth_mail)
	print(sbcglobal_mail)

print("DONE!")
