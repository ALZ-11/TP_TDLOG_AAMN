from weapon import Weapon

class Vessel:
	def __init__(self, coordinates : tuple, max_hits : int, weapon : Weapon):
		self.coordinates = coordinates
		self.max_hits = max_hits
		self.weapon = weapon
	def get_coordinates(self):
		return self.coordinates
	def go_to(self, x, y, z):
		self.coordinates = (x, y, z)
	def fire_at(self, x, y, z):
		self.weapon.fire_at(x, y, z)