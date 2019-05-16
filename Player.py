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

class stat(object):
	"""stats"""
	def __init__(self):
		pass

class Health(stat):
	"""Health actions"""
	def __init__(self):
		self.health = 100

	def current(self):
		print(self.health)

	def decrease(self, count):
		print("Your health got decreased by {}".format(count))
		self.health -= count
		return self.health

	def increase(self, count):
		print("Your health got increased by {}".format(count))
		self.health -= count
		return self.health

class Stamina(stat):
	"""Stamina actions"""
	def __init__(self):
		self.stamina = 100
	
	def current(self):
		print(self.stamina)

	def decrease(self, count):
		print("Your stamina got decreased by {}".format(count))
		self.stamina -= count
		return self.stamina

	def increase(self, count):
		print("Your stamina got increased by {}".format(count))
		self.stamina += count
		return self.stamina

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