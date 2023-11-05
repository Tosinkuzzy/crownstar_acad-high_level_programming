#!/usr/bin/python3

# Welcome Message to Users.
print("Welcome To Crownstar High Level Programming")

# List of projects
print("#### TODO LIST ####")
# Pick any of the project you are interested in!
# list of all items
print(" CODING ")
print(" CONTRIBUTOR ")
print(" DATA ANALYST ")
print(" DEPLOYMENT ")
print(" MAINTENANCE ")

# We have 5 project here now that need to be fixed.
# 1. is that we need to implement some codes
# whenever the user decide to input what they decide to do
# like after displaying those list, the command should prompt for
# input from the user to input his/her selection
# then we will implement this so when they pick one or two we can get the
# user information like, name, email, and social account where we can
# follow each other up.
# put in more ideas before implementations.

def selection_list():
	selection = ['CODING', 'CONTRIBUTOR', 'DATA ANALYST', 'DEPLOYMENT', 'MAINTENANCE']
	type(selection)
	choice = input("Pick Your Choice: ")
	c = choice
	while True:
		#if c in selection:
		print("Thank You For Joining Crownstar!")
		break
	else:
		print("TRY SOMETHING ELSE!!!!!!")

selection_list()
