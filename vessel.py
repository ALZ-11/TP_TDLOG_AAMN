from weapon import Weapon

class Vessel:
	def __init__(self, coordinates : tuple, max_hits : int, weapon : Weapon):
		self.coordinates = coordinates
		self.max_hits = max_hits
		self.weapon = weapon