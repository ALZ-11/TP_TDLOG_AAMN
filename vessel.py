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
		assert len(coordinates) == 3
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
		self.coordinates = (x, y, z)
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
		try:
			assert coordinates[2] == 0
		except:
			raise OutOfCapabilityError
		super().__init__(coordinates, 6, Lance_missiles_antiair())
	def go_to(self, x, y, z):
		try:
			assert z == 0
		except:
			raise OutOfCapabilityError
		super().go_to(x, y, z)

class Submarine(Vessel):
	def __init__(self, coordinates):
		try:
			assert coordinates[2] == 0 or coordinates[2] == -1
		except:
			raise OutOfCapabilityError
		super().__init__(coordinates, 2, Lance_tropilles())
	def go_to(self, x, y, z):
		try:
			assert z == 0 or z == -1
		except:
			raise OutOfCapabilityError
		super().go_to(x, y, z)

class Fregate(Vessel):
	def __init__(self, coordinates):
		try:
			assert coordinates[2] == 0
		except:
			raise OutOfCapabilityError
		super().__init__(coordinates, 5, Lance_missiles_antisurface())
	def go_to(self, x, y, z):
		try:
			assert z == 0
		except:
			raise OutOfCapabilityError
		super().go_to(x, y, z)

class Destroyer(Vessel):
	def __init__(self, coordinates):
		try:
			assert coordinates[2] == 0
		except:
			raise OutOfCapabilityError
		super().__init__(coordinates, 4, Lance_tropilles())
	def go_to(self, x, y, z):
		try:
			assert z == 0
		except:
			raise OutOfCapabilityError
		super().go_to(x, y, z)

class Aircraft(Vessel):
	def __init__(self, coordinates):
		try:
			assert coordinates[2] == 1
		except:
			raise OutOfCapabilityError
		super().__init__(coordinates, 1, Lance_missiles_antisurface())
	def go_to(self, x, y, z):
		try:
			assert z == 1
		except:
			raise OutOfCapabilityError
		super().go_to(x, y, z)