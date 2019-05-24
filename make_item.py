from sys import argv, exit
import json

if len(argv) < 2:
	print("Need exactly 3 arguments")
	exit()

script, itemtype, name, mult, chance = argv

if itemtype == "weapon":
	outfile = open('./items/weapons/{}.json'.format(name), 'w')
	json.dump({'itemtype': 'weapon', 'name': name, 
		'dmg_multiplier': mult, 'critchance': chance}, 
		outfile)
elif itemtype == "armour":
	outfile = open ('./items/armour/{}.json'.format(name), 'w')
	json.dump({'itemtype': 'armour', 'name': name, 
		'dmg_reduction': mult, 'dodgechance': chance}, 
		outfile)

print("Done wrote to {}.json".format(name))