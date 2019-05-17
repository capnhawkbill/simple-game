import random
from randomfunctions import valid_input

class action(object):
	"""actions in the game"""
	def __init__(self, operator):
		self.operator = operator
		self.critchance = 20
		self.dmg_multiplier = 1
		self.dodgechance = 20
		self.dmg_reduction = 1

	def attack(self):
		print("{} attacks".format(self.operator))
		random_number = int(random.randint(1, 10))

		#implement dmg multiplier for weapons
		damage = random_number * self.dmg_multiplier

		#crit calculation
		critchance = 1 / self.critchance
		crit = int(random.randint(1, critchance))
		if crit == 1:
			damage = damage * 2
			print("**CRIT**")

		#print(damage)
		return damage

	def defend(self):
		print("{} defended".format(self.operator))

		#dmg_reduction
		damage = damage * self.dmg_reduction

		#dodge calculation
		dodgechance = 1 / self.dodgechance
		dodge = int(random.randint(1, dodgechance))
		if dodge == 1:
			damage = 0
			print("**DODGE**")

		return damage