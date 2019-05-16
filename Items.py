class Weapon(object):
	"""Weapon class"""
	def __init__(self, name, dmg_multiplier, owner):
		self.name = name
		self.dmg_multiplier = dmg_multiplier
		self.owner = owner
	
	def set_dmg_multiplier(self):
		self.owner.dmg_multiplier = self.dmg_multiplier
		