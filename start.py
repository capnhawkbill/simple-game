import sys
import json
import os
import random
import actions
import stats
import items
import inventory
from randomfunctions import cls

#make player
player_stats = stats.stat()
player_inventory = inventory.player_inventory()

#make actions
player_action = actions.action("player")

#get correct json files
# inventory_file = open("inventory.json", "r+")
# inventory_file = inventory_file.read()
# equipped, inventory = json.loads(inventory_file)
# print(equipped)
# print(inventory)
#select and make an enemy
enemies = os.listdir(path='.//enemy')
print(enemies)
enemy_name = enemies[random.randint(0, (len(enemies) - 1))]
print(enemy_name)
enemy_file = open("{}.json".format(enemy_name), "r")
content = json.loads(enemy_file)
print(content)
# enemy = enemy.enemy(enemy_name, )
#get a enemyjson from the map enemy



#get player interaction
# while "true":
# 	cls()
# 	print("What do you want to do?")
# 	print("\t -Attack (a)")
# 	print("\t -Defend (d)")
# 	print("\t -Inventory (i)")
# 	print("\t -Switch Weapon (sw)")
# 	print("\t -Switch Armour (sa)")
# 	print("\t -View Quick Reference (r)")
# 	print("\t -Quit (q)")
# 	print("-" * 30)
# 	action = input("> ")

# 	if action == "a":
# 		player_action.attack()
# 		break

# 	elif action == "d":
# 		player_action.defend()
# 		break

# 	elif action == "i":
# 		player_inventory.list()
# 		break

# 	elif action == "sw":
# 		cls()
# 		print("With what weapon do you want to switch?")
# 		print("-" * 30)
# 		weapon = input("> ")
# 		player_inventory.equip_weapon(weapon)
# 		break

# 	elif action == "sa":
# 		cls()
# 		print("With what armour do you want to switch?")
# 		print("-" * 30)
# 		armour = input("> ")
# 		player_inventory.equip_armour(armour)		
# 		break

# 	elif action == "r":
# 		print("Work in progress")
# 		break

# 	elif action == "q":
# 		print("are you sure? [Y,n]")
# 		sure = input("> ")
# 		if sure == "Y":
# 			sys.exit()

# 	else:
# 		print("That option is not recognised")