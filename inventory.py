from randomfunctions import cls

class player_inventory(object):
	"""Inventory for player"""
	def __init__(self, json, weapons, armour):
		#first item in array is weapon second is armour
		self.equipped = json['equipped']
		self.items = json['items']
		self.weapons = weapons
		self.armour = armour

	def list(self):		
		#print items in inventor
		#cls()	
		print(self.equipped, self.items)
		if len(self.items) > 1:
			print("Here are the items in your inventory:")
			for i in range(len(self.items)):
				print("\t-{}".format(self.items[i]))
		else:
			print("You don't have any items in your inventory")
		
		print("\n")

		#print equipped items

		if self.equipped[0] != "none" or self.equipped[1] != "none":
			print("Here are the items you equipped:")
			print("\tWeapon: {}".format(self.equipped[0]))
			print("\tArmour: {}".format(self.equipped[1]))
			input("")
		else:
			print("You dont have any items equipped")
			input("")

	def add(self, name):
		cls()
		print("{} got added to your inventory".format(name))
		self.items.append(name)

	def remove(self, name):
		cls()
		print("{} got removed from your inventory".format(name))
		self.items.pop(name)

	def equip_armour(self, name):
		cls()
		if name in self.armour and name in self.items:
			print("{} is unequipped".format(self.equipped[1]))
			print("You equipped: {}".format(name))
			self.equipped[1] = name
		elif name in self.armour:
			print("You dont have {} yet".format(name))
		else:
			print("{} doesnt exist".format(name))

	def equip_weapon(self, name):
		cls()
		if name in self.weapons and name in self.items
			print("{} is unequipped".format(self.equipped[0]))
			print("You equipped: {}".format(name))
			self.equipped[0] = name
		elif name in self.weapons:
			print("You dont have {} yet".format(name))
		else:
			print("{} doesnt exist".format(name))

	def write_json(self):
		#call at end of inv modification to write to json
		pass