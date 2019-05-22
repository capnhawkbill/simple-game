from sys import argv, exit
import json

if len(argv) < 2:
	print("Need at least 2 arguments")
	exit()

script, name, weapon, armour, attackchance, reward = argv

outfile = open('./enemy/{}.json'.format(name), 'w')

json.dump({'name': name, 'weapon': weapon, 'armour': armour, 
	'attackchance': attackchance, 'reward': reward}, outfile)

print("Done wrote to {}.json".format(name))