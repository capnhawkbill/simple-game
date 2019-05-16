def valid_input():
	"""Gets valid input from user"""
	while 1:
		a = int(input("> "))

		if a > 10 or a < 1:
			print("input needs to be between 1 and 10")
		else:
			break
			return a

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
