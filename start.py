import sys
import os
import json
import os
import random
import actions
import stats
import items
import inventory
from randomfunctions import cls, player_input

len_argv= len(sys.argv)

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
	print(enemies)
	enemy_name = enemies[random.randint(0, (len(enemies) - 1))]

enemy_file = open("{}.json".format(enemy_name), "r")
enemy_name, enemy_weapon, enemy_armour, 
enemy_attackchace, enemy_reward = json.loads(enemy_file)

enemy = enemy.enemy(enemy_name, enemy_weapon, enemy_armour, 
	enemy_attackchace, enemy_reward)

#get inventory json
inventory_file = open("{}.json".format(inventory_file), 
	"r+")
inventory_file = inventory_file.read()
equipped, inventory = json.loads(inventory_file)

inventory_file = open("{}.json".format(inventory_file), 
	"r+")
inventory_file = inventory_file.read()
equipped, inventory = json.loads(inventory_file)

#make actions
player_action = actions.action("player")


player_input()

if enemy.