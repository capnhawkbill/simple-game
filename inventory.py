class inventory(object):
	"""Inventory"""
	def __init__(self):
		self.items = []
		#first item in array is weapon second is armour
		self.equipped = ["", ""]
		pass

	def list(self):		

		#print items in inventory	
		if len(self.items) > 1:
			print("Here are the items in your inventory:")
			for i in range(len(self.items)):
				print("\t-{}".format(self.items[i]))
		else:
			print("You don't have any items in your inventory")
		
		print("\n")

		#print equipped items
		if self.equipped[0] != "" or self.equipped[1] != "":
			print("Here are the items you equipped:")
			print("\tWeapon: {}".format(self.equipped[0]))
			print("\tArmour: {}".format(self.equipped[1]))
		else:
			print("You dont have any items equipped")

	def add(self, name):
		print("{} got added to your inventory".format(name))
		self.items.append(name)

	def remove(self, name):
		print("{} got removed from your inventory".format(name))
		self.items.pop(name)

	def equip_armour(self, name):
		print("{} is unequipped".format(self.equipped[1]))
		print("You equipped: {}".format(name))
		self.equipped[1] = name

	def equip_weapon(self, name):
		print("{} is unequipped".format(self.equipped[0]))
		print("You equipped: {}".format(name))
		self.equipped[0] = name

#script that gets the inventory and equipped items from json file