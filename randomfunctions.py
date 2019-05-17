import os

def valid_input():
	"""Gets valid input from user"""
	while "true":
		output = int(input("> "))

		if output > 10 or output < 1:
			print("input needs to be between 1 and 10")
		else:
			break
			return output

def y_or_n():
	"""gets y or n from user"""
	while "true":
		output = input("> ")

		if output == "y":
			return 1
			break

		elif output == "n":
			return 0
			break
		else:
			print("Type y or n")

def choose_action():
	"""gets a valid action"""
	while "true":
		output = input("> ")

		#if statement with the actions

def cls():
	#lol = os.system("clear")
	#lol = os.system("cls")
	print("\033c")