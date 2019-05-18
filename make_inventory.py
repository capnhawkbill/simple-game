from sys import argv, exit
import json

if len(argv) < 2:
	print("Need at least 2 arguments")
	exit()

script = argv[0]
argv.pop(0)

equipped_list = []
inventory_list = []
for i in range(len(argv)):
	if i <= 1:
		equipped_list.append(argv[i])
	else:
		inventory_list.append(argv[i])

outfile = open('inventory.json', 'w')

json.dump({"equipped" : equipped_list}, outfile)
json.dump({"inventory" : inventory_list}, outfile)