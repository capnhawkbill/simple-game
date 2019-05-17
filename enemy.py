import actions
import random

enemy_action = action()

class enemy(object):
	"""enemy"""
	def __init__(self, name, weapon, armour, attackchance):
		self.name = name
		self.weapon = weapon
		self.armour = armour
		self.attackchance = attackchance
		

	def interact(self):
		#make him say some stuff from a textfile
		pass

	def action(self):
		#decide if attack or defend
		chance = random.randint(1, self.attackchance)

		if chance == 1:
			enemy_action.attack(self.name)
		else:
			enemy_action.defend(self.name)