class item(object):
	"""item"""
	def __init__(self):
		pass
		

class Weapon(item):
	"""Weapon class"""
	def __init__(self, name, dmg_multiplier, owner):
		self.name = name
		self.dmg_multiplier = dmg_multiplier
		self.owner = owner
	
	def set_dmg_multiplier(self):
		self.owner.dmg_multiplier = self.dmg_multiplier

	def obtained(self):
		print("You obtained {}\nDo you want to equip it?\n y or n".format(self.name))
		
		while "true":
			equip = input("> ")

			if equip == "y":
				#equip item
				break
			elif equip == "n":
				#dont equip item
				break
			else:
				print("Type y or n")

class defense(item):
	"""Defensive item"""
	def __init__(self, name, dmg_reduction, owner):
		self.name = name
		self.dmg_reduction = dmg_reduction
		self.owner = owner

	def set dmg_reduction(self):
		self.owner.dmg_reduction = self.dmg_reduction
		
