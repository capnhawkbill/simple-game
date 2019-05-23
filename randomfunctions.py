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

def cls():
	#placeholder = os.system("clear")
	#placeholder = os.system("cls")
	print("\033c")

def player_input():
	"""get a valic player action"""
	while "true":
	cls()
	print("What do you want to do?")
	print("\t -Attack (a)")
	print("\t -Defend (d)")
	print("\t -Inventory (i)")
	print("\t -Switch Weapon (sw)")
	print("\t -Switch Armour (sa)")
	print("\t -View Quick Reference (r)")
	print("\t -Quit (q)")
	print("-" * 30)
	action = input("> ")

	if action == "a":
		player_action.attack()
		break

	elif action == "d":
		player_action.defend()
		break

	elif action == "i":
		player_inventory.list()
		break

	elif action == "sw":
		cls()
		print("With what weapon do you want to switch?")
		print("-" * 30)
		weapon = input("> ")
		player_inventory.equip_weapon(weapon)
		break

	elif action == "sa":
		cls()
		print("With what armour do you want to switch?")
		print("-" * 30)
		armour = input("> ")
		player_inventory.equip_armour(armour)		
		break

	elif action == "r":
		print("Work in progress")
		break

	elif action == "q":
		print("are you sure? [Y,n]")
		sure = input("> ")
		if sure == "Y":
			sys.exit()

	else:
		print("That option is not recognised")