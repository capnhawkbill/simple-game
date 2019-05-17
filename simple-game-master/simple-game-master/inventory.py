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
		self.items.append(name)

	def remove(self, name):
		self.items.pop(name)

	def equip_armour(self, name):
		self.equipped[1] = name

	def equip_weapon(self, name):
		self.equipped[0] = name
