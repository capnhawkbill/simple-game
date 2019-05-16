class stat(object):
	"""stats"""
	def __init__(self):
		pass

class Health(stat):
	"""Health actions"""
	def __init__(self):
		super(stat, self).__init__()
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
		super(stat, self).__init__()
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
