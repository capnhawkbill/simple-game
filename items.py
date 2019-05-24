from randomfunctions import y_or_n

class item(object):
	"""item class"""
	def __init__(self):
		pass
	
		def obtained(self):
			print("you obtained {}\nDo you want to equip it?\n y or n"
				.format(self.name))
		if y_or_n() == 1:
			print("equipped")
		else:
			print("not equipped")

class weapon(item):
	"""Weapon class"""
	def __init__(self, name, dmg_multiplier, critchance):
		super(item, self).__init__()
		self.name = name
		self.dmg_multiplier = dmg_multiplier
		self.critchance = critchance

class armour(item):
	"""Defensive item class"""
	def __init__(self, name, dmg_reduction, dodgechance):
		super(item, self).__init__()
		self.name = name
		self.dmg_reduction = dmg_reduction
		self.dodgechance = dodgechance