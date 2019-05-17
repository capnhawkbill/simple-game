from sys import argv
import json

argv.pop(0)

outfile = open('output', 'w')

json.dump(argv, outfile)