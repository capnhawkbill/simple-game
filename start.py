import actions
import stats
import items
import inventory
import interaction
from randomfunctions import cls

#make player
player_stats = stats.stat()
player_inventory = inventory.inventory()

#make actions
player_action = actions.action("player")

#get player interaction in battle
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
		break
		player_action.attack()
	elif action == "d":
		break
		player_action.defend()
	elif action == "i":
		break
		
	elif action == "sw":
		break
	elif action == "sa"
		break
	elif action == "r":
		break
	elif action == "q":
		break
	else:
		print("That option is not recognised")