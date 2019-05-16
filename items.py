from custominput import y_or_n

class item(object):
	"""item"""
	def __init__(self):
		pass
		
class weapon(item):
	"""Weapon class"""
	def __init__(self, name, dmg_multiplier, owner):
		super(item, self).__init__()
		self.name = name
		self.dmg_multiplier = dmg_multiplier
		self.owner = owner
	
	def set_dmg_multiplier(self):
		self.owner.dmg_multiplier = self.dmg_multiplier

	def obtained(self):
		print("You obtained {}\nDo you want to equip it?\n y or n".format(self.name))
		if y_or_n() == 1:
			print("equipped")
		else:
			print("not equipped")

class armour(item):
	"""Defensive item"""
	def __init__(self, name, dmg_reduction, owner):
		super(item, self).__init__()
		self.name = name
		self.dmg_reduction = dmg_reduction
		self.owner = owner

	def set_dmg_reduction(self):
		self.owner.dmg_reduction = self.dmg_reduction
		
	def obtained(self):
		print("you obtained {}\nDo you want to equip it?\n y or n".format(self.name))