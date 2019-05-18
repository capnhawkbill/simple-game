from sys import argv, exit
import json


if len(argv) < 2:
	print("Need at least 2 arguments")
	exit()

script = argv[0]

argv.pop(0)
equipped = []
inventory = []
for i in range(len(argv)):
	if i <= 1:
		equipped.append(argv[i])
	else:
		inventory.append(argv[i])

print("equipped items: {}\n items in inventory: {}".format(equipped, inventory))

outfile = open('output', 'w')

json.dump(equipped, outfile)
json.dump(inventory, outfile)