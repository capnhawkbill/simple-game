import random
from operator import xor

def valid_input():
	"""Gets valid input from user"""
	while 1:
		a = int(input("> "))

		if a > 10 or a < 1:
			print("input needs to be between 1 and 10")
		else:
			break
			return a

class action(object):
	"""actions in the game"""
	def __init__(self):
		self.critchance = 20
		self.dmg_multiplier = 1
		pass

	def attack(self):
		print("You attack")
		random_number = int(random.randint(1, 10))

		#implement dmg multiplier for weapons
		damage = random_number * self.dmg_multiplier

		#crit calculation if var critchance is lower the chance is higher
		crit = int(random.randint(1, self.critchance))
		if crit == 1:
			damage = damage * 2
			print("**CRIT**")

		print(damage)
		return damage

	def defend(self):
		print("you defended")