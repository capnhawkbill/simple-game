import actions
import random



class enemy(object):
	"""enemy"""
	def __init__(self, name, weapon, armour, 
		attackchance, reward):
		self.name = name
		self.weapon = weapon
		self.armour = armour
		self.attackchance = attackchance
		self.reward = reward
		self.health = 100
		enemy_action = action.action(self.name, 
			self.weapon, self.armour)

	def interact(self):
		#make him say some stuff from a textfile
		pass

	def action(self):
		#decide if attack or defend
		chance = random.randint(1, self.attackchance)

		if chance == 1:
			damage = enemy_action.attack(self.name)
		else:
			damage = enemy_action.defend(self.name)
		
		self.healt -= damage
		if self.health <= 0:
			return "died"
		else:
			return "lived"

	def die(self):
		#print deadmessage and end battle
		#add self.reward to player inventorygit 