import random
from operator import xor
from custominput import valid_input

class action(object):
	"""actions in the game"""
	def __init__(self):
		self.critchance = 20
		self.dmg_multiplier = 1
		self.dodgechance = 20
		self.dmg_reduction = 1

	def attack(self, attacker):
		print("{} attacks".format(attacker))
		random_number = int(random.randint(1, 10))

		#implement dmg multiplier for weapons
		damage = random_number * self.dmg_multiplier

		#crit calculation if var critchance is lower the chance is higher
		crit = int(random.randint(1, self.critchance))
		if crit == 1:
			damage = damage * 2
			print("**CRIT**")

		#print(damage)
		return damage

	def defend(self, defender):
		print("{} defended".format(defender))

		#dmg_reduction
		damage = damage * self.dmg_reduction

		#dodgechance
		dodge = int(random.randint(1, self.dodgechance))
		if dodge == 1:
			damage = 0
			print("**DODGE**")

		return damage