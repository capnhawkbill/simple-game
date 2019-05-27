class Health(object):
	"""Health actions"""
	def __init__(self, name, health):
		self.health = health
		self.name = name

	def current(self):
		print(self.health)

	def decrease(self, count):
		print("{} health got decreased by {}".format(self.name, count))
		self.health -= count

	def increase(self, count):
		print("{} health got increased by {}".format(self.name, count))
		self.health -= count