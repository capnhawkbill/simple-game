from sys import argv, exit
import json

if len(argv) != 7:
	print("Need exactly 6 arguments")
	exit()

script, name, health, weapon, armour, attackchance, reward = argv

outfile = open('./enemy/{}.json'.format(name), 'w')

json.dump({'name': name, 'health': int(health), 
	'weapon': weapon, 'armour': armour, 
	'attackchance': int(attackchance), 'reward': reward}, 
	outfile)

print("Done wrote to {}.json".format(name))