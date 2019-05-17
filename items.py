from randomfunctions import y_or_n

class item(object):
	"""item"""
	def __init__(self):
		pass
		
class weapon(item):
	"""Weapon class"""
	def __init__(self, name, critchance, dmg_multiplier, owner):
		super(item, self).__init__()
		self.name = name
		self.dmg_multiplier = dmg_multiplier
		self.critchance = critchance
		self.owner = owner

	def obtained(self):
		print("You obtained {}\nDo you want to equip it?\n y or n".format(self.name))
		if y_or_n() == 1:
			print("equipped")
		else:
			print("not equipped")

class armour(item):
	"""Defensive item"""
	def __init__(self, name, dmg_reduction, dodgechance, owner):
		super(item, self).__init__()
		self.name = name
		self.dmg_reduction = dmg_reduction
		self.dodgechance = dodgechance
		self.owner = owner
		
	def obtained(self):
		print("you obtained {}\nDo you want to equip it?\n y or n".format(self.name))
		if y_or_n() == 1:
			print("equipped")
		else:
			print("not equipped")


#script that gets the weapons info from a file

with open(weaponfile) as file:
	