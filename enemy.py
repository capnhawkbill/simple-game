import random
import actions
import stats



class enemy(object):
	"""enemy"""
	def __init__(self, name, health, weapon, armour, 
		attackchance, reward, deadmessage):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.armour = armour
		self.attackchance = attackchance
		self.reward = reward
		self.deadmessage = deadmessage

		enemy_action = actions.action(self.name, 
			self.weapon, self.armour)
		enemy_health = stats.Health(self.name, self.health)
	def interact(self):
		#make him say some stuff from a textfile
		pass

	def attack(self):
		enemy_action.attack()

	def defend(self, damage):
		enemy_action.defend(damage)

	def decide(self):
		chance = random.randint(1, self.attackchance)

		if chance == 1:
			attack = 1
		else:
			attack = 0
		return attack

	def die(self):
		#print deadmessage and end battle
		#add self.reward to player inventory
		print(self.deadmessage)
		if self.reward in armour_insts:
			armour_insts[self.reward].obtained
		elif self.reward in weapon_insts:
			weapon_insts[self.reward].obtained