from weapon import *

class DestroyedError(Exception):
    def __init__(self, message="The vessel is destroyed. Cannot get coordinates."):
        self.message = message
        super().__init__(self.message)

class Vessel:
	def __init__(self, coordinates : tuple, max_hits : int, weapon : Weapon):
		self.coordinates = coordinates
		self.max_hits = max_hits
		self.weapon = weapon
	def get_coordinates(self):
		try:
			assert self.max_hits > 0
		except:
			raise DestroyedError
		return self.coordinates
	def go_to(self, x, y, z):
		self.coordinates = (x, y, z)
	def fire_at(self, x, y, z):
		self.weapon.fire_at(x, y, z)

class Cruiser(Vessel):
	def __init__(self, coordinates):
		super().__init__(coordinates, 6, Lance_missiles_antiair())