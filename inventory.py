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
			for i in range(len(self.items)):
				print("\t-{}".format(self.items[i]))
		else:
			print("You dont have any items equipped")

	def add(self, name):
		pass

	def remove(self, name):
		pass

	def get(self, name):
		pass

	def equip_armour(self, name):
		pass

	def equip_weapon(self, name):
		pass
