class inventory(object):
	"""Inventory"""
	def __init__(self):
		self.items = []
		pass

	def list(self):
		print("Here are the items in your inventory:")
		
		if len(self.items) > 1:
			for i in range(len(self.items)):
				print("\t-{}".format(self.items[i]))
		else:
			print("You don't have any items in your inventory")

	def add(self, name):
		pass

	def get(self, name):
		pass

	def remove(self, name):
		