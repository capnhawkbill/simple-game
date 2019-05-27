import sys
import os
import json
import os
import random
import actions
import stats
import items
import info
from inventory import player_inventory
import enemy
from randomfunctions import cls, player_input, y_or_n

len_argv = len(sys.argv)
if len_argv < 2:
	print("Need at least 1 argument")
	exit()
elif len_argv == 2:
	inventory_file = sys.argv[1]
	selectenemy = "true"
elif len_argv == 3:
	inventory_file = sys.argv[1]
	enemy_name = sys.argv[2]
	selectenemy = "false"

#make actions
player_action = actions.action("player", 
	inventory.equipped[0], inventory.equipped[1])
player_health = stats.Health("player", 100)

#make all the items


#select and make an enemy
if selectenemy:
	enemies = os.listdir(path='.//enemy')
	enemy_name = enemies[random.randint(0, (len(enemies) - 1))]

enemy_file = open("./enemy/{}".format(enemy_name), "r")
enemy_json = {}
enemy_json = json.load(enemy_file)
enemy = enemy.enemy(enemy_json, 'placeholder')

#get inventory json
inventory_file = open("./inventory/{}.json".format(inventory_file), 
	"r+")
inventory_json = {}
inventory_json = json.load(inventory_file)
inventory = player_inventory(inventory_json, 
	all_weapons, all_armour)

#display introduction
print("Do you want to get the introduction?")
intro = y_or_n()
if intro == 1:
	info.intro()

#enemy action
attacked = enemy.decide()
if attacked:
	enemy.attack()

while "true":
	cls()
	print("Your health is: ", player_health.health)
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
		dmg_dealt = player_action.attack()
		enemy.decrease(dmg_dealt)
		break

	elif action == "d":
		player_action.defend(damage)
		break
	elif action == "i":
		inventory.list()

	elif action == "sw":
		cls()
		print("With what weapon do you want to switch?")
		print("-" * 30)
		weapon = input("> ")
		inventory.equip_weapon(weapon)
		break

	elif action == "sa":
		cls()
		print("With what armour do you want to switch?")
		print("-" * 30)
		armour = input("> ")
		inventory.equip_armour(armour)		
		break
	
	elif action == "r":
		info.reference()

	elif action == "q":
		print("are you sure? [y,N]")
		sure = input("> ")
		if sure == "Y":
			sys.exit()
	else:
		print("That option is not recognised")

#health calculations
player_health.health.decrease(damage)
