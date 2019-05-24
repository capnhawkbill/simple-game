import sys
import os
import json
import os
import random
import actions
import stats
import items
from inventory import player_inventory
import enemy
from randomfunctions import cls, player_input

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

#select and make an enemy
if selectenemy:
	enemies = os.listdir(path='.//enemy')
	enemy_name = enemies[random.randint(0, (len(enemies) - 1))]

enemy_file = open("./enemy/{}".format(enemy_name), "r")
enemy_name, enemy_health, enemy_weapon, enemy_armour, enemy_attackchace, enemy_reward = json.load(enemy_file)
print(enemy_attackchace)
enemy = enemy.enemy(enemy_name, enemy_health, enemy_weapon, enemy_armour, 
	enemy_attackchace, enemy_reward, 'placeholder')

#get inventory json
inventory_file = open("./inventory/{}.json".format(inventory_file), 
	"r+")
equipped, inventory = json.load(inventory_file)
print(equipped, "\n", inventory)
inventory = player_inventory(equipped, items)

#make actions
player_action = actions.action("player", equipped[0], equipped[1])
player_health = stats.Health("player", 100)

#make all the items
all_armour = os.listdir(path='./items/armour')
armour_insts = {}
for i in range(len(all_armour)):
	file = open("./items/armour/{}".format(all_armour[i]))
	itemtype, name, dmg_reduction, dodgechance = json.load(file)
	armour_insts[name] = items.armour(name, 
		dmg_reduction, dodgechance)

all_weapons = os.listdir(path='./items/weapons')
weapon_insts = {}
for i in range(len(all_weapons)):
	file = open("./items/weapons/{}".format(all_weapons[i]))
	itemtype, name, dmg_multiplier, critchance = json.load(file)
	weapon_insts[name] = items.weapon(name, 
		dmg_multiplier, critchance)

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
		break

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
		print("Work in progress")
		break

	elif action == "q":
		print("are you sure? [Y,n]")
		sure = input("> ")
		if sure == "Y":
			sys.exit()
	else:
		print("That option is not recognised")

#health calculations
player_health.health.decrease(damage)
