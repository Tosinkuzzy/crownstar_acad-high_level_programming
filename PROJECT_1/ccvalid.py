"""
*****Luhn Algorithm: This algorithm checks the validity of credit card numbers. 
Here is a Python code that uses the Luhn Algorithm to validate credit card numbers:
*******
"""
print("CREDIT CARD VALIDATION LOADING.....")

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    nums = digits_of(card_number)
    check_sum = sum(nums[::-2] + [sum(divmod(d * 2, 10)) for d in nums[-2::-2]])
    return check_sum % 10 == 0

# Get input from user
card_number = int(input("ENTER CARD NUMBER:"))
# Specify the filename
filename = "user_data.txt"
try:
	# Open the file in write mode ('w')
    with open(filename, 'w') as file:
	# Write the user input to the file
	wt = file.write(str(card_number))
except FileNotFoundError:
    	print(f"The file {filename} was not found.")
except PermissionError:
    	print(f"You don't have permission to write to {filename}.")
except Exception as e:
    	print(f"An error occurred: {str(e)}")
try:
	# Read the file in read mode ('r')
    with open(filename, 'r') as file:
	# Read the contents of the file
	contents = file.read()
        # Print the contents of the file
	print(contents)
except FileNotFoundError:
	print(f"The file {filename} was not found.")
except PermissionError:
    	print(f"You don't have permission to read {filename}.")
except Exception as e:
    	print(f"An error occurred: {str(e)}")

status = print("VALIDATING CARD...")
if luhn_check(card_number):
    print("THE CREDIT CARD NUMBER IS VALID.")
else:
    print("THE CREDIT CARD NUMBER IS NOT VALID.")

print("DONE!")
