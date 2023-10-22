class NoAmmoError(Exception):
    def __init__(self, message = "No ammo left. Cannot fire."):
        self.message = message
        super().__init__(self.message)

class OutOfRangeError(Exception):
    def __init__(self, message = "Target is out of range. Cannot fire."):
        self.message = message
        super().__init__(self.message)

class Weapon:
    def __init__(self, ammunitions : int, range : int):
        self.ammunitions = ammunitions
        self.range = range
    def fire_at(self, x : int, y : int, z : int):
        try:
            assert self.ammunitions > 0
        except:
            raise NoAmmoError
        
class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        super().__init__(50, 100)
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)
        try:
            assert z == 0
        except:
            raise OutOfRangeError
        finally:
            self.ammunitions -= 1

class Lance_missiles_antiair(Weapon):
    def __init__(self):
        super().__init__(40, 20)
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)
        try:
            assert z > 0
        except:
            raise OutOfRangeError
        finally:
            self.ammunitions -= 1

class Lance_tropilles(Weapon):
    def __init__(self):
        super().__init__(24, 40)
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)
        try:
            assert z <= 0
        except:
            raise OutOfRangeError
        finally:
            self.ammunitions -= 1