from weapon import *
from math import sqrt

class OutOfRangeError(Exception):
    def __init__(self, message = "Target is out of range."):
        self.message = message
        super().__init__(self.message)

class OutOfCapabilityError(Exception):
    def __init__(self, message="Coordinates are beyond the vessel's capability."):
        self.message = message
        super().__init__(self.message)

def distance(tuple1 : tuple, tuple2 : tuple):
	return sqrt(sum([(tuple1[i] - tuple2[i]) ** 2 for i in range(len(tuple1))]))

class DestroyedError(Exception):
    def __init__(self, message="The vessel is destroyed."):
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
		try:
			assert self.max_hits > 0
		except:
			raise DestroyedError
	def fire_at(self, x, y, z):
		try:
			assert self.max_hits > 0
		except:
			raise DestroyedError
		self.weapon.fire_at(x, y, z)
		try:
			assert distance((x, y, z), self.get_coordinates()) <= self.weapon.range
		except:
			raise OutOfRangeError
		finally:
			self.weapon.ammunitions -= 1

class Cruiser(Vessel):
	def __init__(self, coordinates):
		super().__init__(coordinates, 6, Lance_missiles_antiair())
	def go_to(self, x, y, z):
		super().go_to(x, y, z) #before, verify that the vessel is not destroyed :)
		try:
			assert z == 0
		except:
			raise OutOfCapabilityError
		self.coordinates = (x, y, z)