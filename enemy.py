import actions
import random

enemy_action = action()

class enemy(object):
	"""enemy"""
	def __init__(self, name, weapon, armour, attackchance, reward):
		self.name = name
		self.weapon = weapon
		self.armour = armour
		self.attackchance = attackchance
		self.reward = reward


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

	def die(self):
		#print deadmessage and end battle
		#add self.reward to player inventory

#do this in start.py
#assemble enemys from jsonfiles in folder enemys
#layout jsonfile:
#list with name, weapon, armour, attackchance and reward
#name of textfile with texts and deadmessages