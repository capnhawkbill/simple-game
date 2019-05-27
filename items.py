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

class make_items(object):
	"""Make all the items"""
	def __init__(self):
		self.all_armour = []
		self.all_weapons = []
		self.armour_insts = {}
		self.weapon_insts = {}

	def make(self):
		#need to fix the json loading
		self.all_armour = os.listdir(path='./items/armour')
		self.armour_insts = {}
		for i in range(len(self.all_armour)):
			file = open("./items/armour/{}".format(self.all_armour[i]))
			itemtype, name, dmg_reduction, dodgechance = json.load(file)
			armour_insts[name] = items.armour(name, 
				dmg_reduction, dodgechance)

		self.all_weapons = os.listdir(path='./items/weapons')
		self.weapon_insts = {}
		for i in range(len(self.all_weapons)):
			file = open("./items/weapons/{}".format(self.all_weapons[i]))
			itemtype, name, dmg_multiplier, critchance = json.load(file)
			self.weapon_insts[name] = items.weapon(name, 
				dmg_multiplier, critchance)